"""Check installed identities, parseable metadata and local references.

This is static inspection. It does not execute skill instructions or assess game readiness.
Requires Python 3.11+ and PyYAML. Use --bash for shell syntax checks.
"""
from pathlib import Path
import os
import argparse, ast, datetime, hashlib, json, re, subprocess, tomllib
import yaml

HERE = Path(__file__).resolve().parent
T = HERE.parents[1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bash')
    args = parser.parse_args()
    rows, links = [], []
    def check(name, passed, detail=''):
        rows.append(dict(name=name, passed=bool(passed), detail=detail))
    def text(path): return path.read_text(encoding='utf-8-sig')
    cat = yaml.safe_load(text(T/'CGS Skill Testing Framework/catalog.yaml'))
    skills = {p.parent.name:p for p in (T/'.agents/skills').glob('*/SKILL.md')}
    agents = {p.stem:p for p in (T/'.codex/agents').glob('*.toml')}
    for kind, actual in [('skills', skills), ('agents', agents)]:
        entries = cat[kind]
        check(kind+' catalog identity set', set(actual) == {x['name'] for x in entries})
        check(kind+' catalog unique identities', len(entries) == len({x['name'] for x in entries}))
        for entry in entries:
            check(kind+' specification '+entry['name'], bool(entry.get('spec')) and (T/entry['spec']).is_file())
    for name,p in skills.items():
        try:
            fm = yaml.safe_load(text(p).split('---',2)[1])
            ui = yaml.safe_load(text(p.parent/'agents/openai.yaml'))
            check('skill metadata '+name, fm.get('name') == name and isinstance(fm.get('description'),str) and bool(fm['description'].strip()) and '$'+name in ui['interface']['default_prompt'])
        except Exception as exc: check('skill metadata '+name, False, str(exc))
    for name,p in agents.items():
        try:
            data = tomllib.loads(text(p))
            check('persona schema '+name, data.get('name') == name and all(isinstance(data.get(k),str) and data[k].strip() for k in ['description','developer_instructions']))
            check('inherited runtime '+name, not set(data).intersection({'model','model_reasoning_effort','sandbox_mode','max_turns'}))
        except Exception as exc: check('persona schema '+name,False,str(exc))
    result_root = HERE.parent/'results'
    files = []
    for root, directories, names in os.walk(T):
        directories[:] = [name for name in directories if name not in {'.git', '.venv', '__pycache__'}
                          and Path(root)/name != result_root]
        files.extend(Path(root)/name for name in names)
    for p in files:
        rel = p.relative_to(T).as_posix()
        try:
            if p.suffix == '.toml': tomllib.loads(text(p))
            elif p.suffix in ('.yaml','.yml'): yaml.safe_load(text(p))
            elif p.suffix == '.json': json.loads(text(p))
            elif p.suffix == '.py': compile(text(p),rel,'exec')
            elif p.suffix == '.rules': ast.parse(text(p))
            elif p.suffix == '.sh' and args.bash:
                proc = subprocess.run([args.bash,'-n',str(p)],capture_output=True,text=True)
                if proc.returncode: raise ValueError(proc.stderr)
            else: continue
            check('parse '+rel,True)
        except Exception as exc: check('parse '+rel,False,str(exc))
    workflow = yaml.safe_load(text(T/'.codex/docs/workflow-catalog.yaml'))
    check('four canonical phases',set(workflow['phases']) == {'conceptualization','development-schematics','pre-implementation','implementation'})
    def walk(value):
        if isinstance(value,dict):
            for k,v in value.items():
                if k == 'available_support':
                    for name in re.findall(r'\$([a-z][a-z0-9-]*)',str(v)):
                        check('available support '+name,name in skills)
                yield from walk(v)
        elif isinstance(value,list):
            for v in value: yield from walk(v)
        return
    list(walk(workflow))
    for p in files:
        if p.suffix != '.md': continue
        body = text(p)
        for dest in re.findall(r'\]\(([^\n)]+)\)', body):
            dest = dest.strip().strip('<>')
            if dest.startswith(('http:','https:','#','mailto:')) or any(c in dest for c in '[]*{}'): continue
            resolved = (p.parent/dest.split('#')[0]).resolve()
            if not resolved.exists(): links.append(dict(source=p.relative_to(T).as_posix(),target=dest))
    # Missing literal links are listed for human triage: some intentionally refer to future game outputs.
    report = dict(recorded_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),classification='Static inspection',skills=len(skills),personas=len(agents),checks=rows,missing_literal_links=links,
                  input_sha256={p.relative_to(T).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files})
    out=HERE.parent/'results/structure';out.mkdir(parents=True,exist_ok=True)
    (out/'structure.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(dict(checks=len(rows),passed=sum(x['passed'] for x in rows),missing_links=links,failures=[x for x in rows if not x['passed']]),indent=2))
    return int(any(not x['passed'] for x in rows))

if __name__ == '__main__': raise SystemExit(main())
