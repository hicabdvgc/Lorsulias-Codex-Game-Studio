#!/usr/bin/env python3
"""Lifecycle observations; no task inference, narrative rotation or progression writes."""
import argparse
from datetime import datetime, timezone
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import uuid

spec = importlib.util.spec_from_file_location('session_state', Path(__file__).with_name('session-state.py'))
state = importlib.util.module_from_spec(spec)
spec.loader.exec_module(state)


def git_scope(root):
    try:
        p = subprocess.run(['git', '-C', str(root), 'status', '--short'], capture_output=True,
                           text=True, encoding='utf-8', errors='replace', timeout=3)
        if p.returncode:
            return 'Git unavailable or non-Git studio; no activity attribution.'
        return 'Checkout observations, not session attribution:\n' + (p.stdout[:2048] or '(clean)')
    except (OSError, subprocess.TimeoutExpired):
        return 'Git observations NOT ASSESSED.'


def run(root, event, data, bash=None):
    if not isinstance(data, dict) or data.get('hook_event_name') != event:
        raise ValueError('hook input must be an object with matching hook_event_name')
    if event == 'SessionStart' and data.get('source') not in ('startup', 'resume', 'clear', 'compact'):
        raise ValueError('SessionStart source must be startup, resume, clear or compact')
    if event in ('PreCompact', 'PostCompact') and data.get('trigger') not in ('auto', 'manual'):
        raise ValueError('compaction trigger must be auto or manual')
    for field in ('session_id', 'turn_id'):
        if field in data and not isinstance(data[field], str):
            raise ValueError(field + ' must be a string when supplied')
    if event == 'Stop' and 'stop_hook_active' in data and not isinstance(data['stop_hook_active'], bool):
        raise ValueError('stop_hook_active must be boolean')
    recovery = state.read_state(root)
    stage = state.read_stage(root)
    message = f'Declared section: {stage["declared"] or "not set"} ({stage["status"]}); outcome evidence still required.\n'
    message += f'Recovery: {recovery["status"]} at {recovery["path"]}.\n'
    if recovery['status'] == 'VALID':
        message += 'Focus: ' + (' > '.join(recovery['focus'].values()) or 'none recorded') + '\n'
        message += 'Recorded checkpoint (verify against current files):\n' + recovery['checkpoint']
    else:
        message += '; '.join(recovery['limitations']) + '\nRecover from current task/files; no checkpoint was inferred.'
    if event == 'SessionStart':
        if data['source'] != 'compact':
            message += '\n' + git_scope(root)
            try:
                proc = subprocess.run([bash or 'bash', str(root / '.codex/hooks/detect-gaps.sh')],
                                      capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=6)
                observation = proc.stdout + ('\n' + proc.stderr if proc.stderr else '')
                message += f'\nDiscovery observer exit {proc.returncode} (not a gate):\n' + observation[:2048]
                if len(observation) > 2048:
                    message += '\n[Discovery preview bounded; run detect-gaps.sh explicitly for full findings.]'
            except (OSError, subprocess.TimeoutExpired) as exc:
                message += '\nDiscovery NOT ASSESSED: ' + str(exc)
        return {'hookSpecificOutput': {'hookEventName': event, 'additionalContext': message}}
    if os.environ.get('CGS_HOOK_DRY_RUN') != '1':
        log = root / 'production/session-logs'
        log.mkdir(parents=True, exist_ok=True)
        record = {'event': event, 'timestamp': datetime.now(timezone.utc).isoformat(),
                  'session_id': data.get('session_id'), 'turn_id': data.get('turn_id'),
                  'trigger': data.get('trigger'), 'recovery_status': recovery['status'], 'stage': stage,
                  'meaning': 'turn stopped' if event == 'Stop' else 'compaction lifecycle observation'}
        if event == 'PreCompact':
            record.update(checkpoint=recovery['checkpoint'], limitations=recovery['limitations'],
                          checkout_observations=git_scope(root))
        # Separate event files avoid interleaving concurrent append writes; IDs are data, never paths.
        with (log / ('lifecycle-' + uuid.uuid4().hex + '.json')).open('x', encoding='utf-8') as f:
            json.dump(record, f, ensure_ascii=True, indent=2)
    if event == 'Stop':
        return {'continue': True}
    return {'continue': True, 'systemMessage': f'{event}: recovery {recovery["status"]}; '
            'SessionStart source=compact supplies bounded recovery context. Checkpoint is not task evidence.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--event', choices=('SessionStart', 'Stop', 'PreCompact', 'PostCompact'), required=True)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--bash')
    args = parser.parse_args()
    try:
        output = run(args.root.resolve(), args.event, json.load(sys.stdin), args.bash)
    except (ValueError, OSError) as exc:
        print(json.dumps({'continue': True, 'systemMessage': 'NOT ASSESSED: ' + str(exc)}))
        print('NOT ASSESSED: ' + str(exc), file=sys.stderr)
        return 1
    print(json.dumps(output, ensure_ascii=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
