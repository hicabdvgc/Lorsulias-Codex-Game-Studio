"""Run isolated studio helper checks. Requires Python 3.11+, PyYAML, Bash, Git.

Windows launcher cases additionally require PowerShell and Git for Windows.
Fixtures stay in a fresh temporary directory; each run writes a new ignored results directory.
"""
from pathlib import Path
import argparse, datetime, hashlib, json, os, shutil, subprocess, sys, tempfile, uuid

HERE = Path(__file__).resolve().parent
STUDIO = HERE.parents[1]
NAMES = ['foundation', 'design_helpers', 'assets', 'story_status',
         'git_observers', 'git_extra', 'continuity', 'continuity_extra']

def checks(value):
    if isinstance(value, dict):
        if 'passed' in value or 'pass' in value:
            yield value
        else:
            for item in value.values(): yield from checks(item)
    elif isinstance(value, list):
        for item in value: yield from checks(item)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bash', required=True, help='Existing Bash executable')
    parser.add_argument('--only', nargs='+', choices=NAMES+['worktree'], help='Run selected checks; git_extra also runs its git_observers prerequisite')
    args = parser.parse_args()
    if args.only and 'git_extra' in args.only and 'git_observers' not in args.only:
        args.only.insert(0, 'git_observers')  # Establish the disposable repository used by extra cases.
    work = Path(tempfile.mkdtemp(prefix="Lorsulia runtime's "))
    run_id = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:8]
    out = HERE.parent / 'results/runtime' / run_id
    out.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, STUDIO_TEST_BASH=str(Path(args.bash).resolve()),
               PYTHONUTF8='1', PYTHONDONTWRITEBYTECODE='1')
    records = []
    names = [name for name in NAMES if not args.only or name in args.only]
    for name in names:
        if args.only and name not in args.only: continue
        group = 'git_observers' if name == 'git_extra' else name
        casework = work / group
        casework.mkdir(exist_ok=True)
        env['STUDIO_VERIFICATION_WORK'] = str(casework)
        proc = subprocess.run([sys.executable, str(HERE/'runners'/f'{name}.py')],
                              env=env, capture_output=True, text=True, encoding='utf-8',
                              errors='replace', timeout=240)
        result_files = {}
        for path in casework.glob('*.json'):
            result_files[path.name] = json.loads(path.read_text(encoding='utf-8'))
        rows = list(checks(result_files))
        record = dict(runner=name, exit=proc.returncode, stdout=proc.stdout,
                      stderr=proc.stderr, checks=len(rows),
                      passed=sum(bool(x.get('passed', x.get('pass'))) for x in rows),
                      results=result_files)
        # git_extra shares only the disposable Git fixture; do not count the earlier report twice.
        if name == 'git_extra':
            record['results'].pop('runtime-checks.json', None)
            rows = list(checks(record['results']))
            record['checks'] = len(rows)
            record['passed'] = sum(bool(x.get('passed', x.get('pass'))) for x in rows)
        (out/f'{name}.json').write_text(json.dumps(record, indent=2), encoding='utf-8')
        records.append({k:v for k,v in record.items() if k not in ('results','stdout','stderr')})
        print(name, proc.returncode, record['passed'], '/', record['checks'], flush=True)
    # Existing source preflight tests already create and clean disposable repositories.
    env.update(GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull)
    run_worktree = not args.only or 'worktree' in args.only
    preflight_exit = None
    if run_worktree:
        proc = subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', str(STUDIO/'tests'),
                               '-p', 'test_worktree_preflight.py'], cwd=STUDIO,
                              env=env, capture_output=True, text=True, timeout=240)
        (out/'worktree-preflight.json').write_text(json.dumps(dict(exit=proc.returncode,
            stdout=proc.stdout, stderr=proc.stderr), indent=2), encoding='utf-8')
        preflight_exit = proc.returncode
    summary = dict(recorded_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                   classification='Executable isolated fixtures; direct launchers, not native event dispatch',
                   fixture_root=str(work), selected=names, runners=records,
                   worktree_selected=run_worktree, worktree_exit=preflight_exit,
                   implementation_sha256={p.relative_to(STUDIO).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
                       for folder in ['.codex/hooks','.codex/scripts','.agents/skills/integrate-worktrees/scripts']
                       for p in (STUDIO/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts})
    (out/'summary.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
    print('Results:', out, flush=True)
    return int((run_worktree and preflight_exit != 0) or len(records) != len(names) or any(r['exit'] or not r['checks'] or r['passed'] != r['checks'] for r in records))

if __name__ == '__main__':
    raise SystemExit(main())
