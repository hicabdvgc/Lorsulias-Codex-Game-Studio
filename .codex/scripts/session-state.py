#!/usr/bin/env python3
"""Read the bounded studio checkpoint. Shared by status and lifecycle consumers."""
import argparse
import json
from pathlib import Path
import re

REGION_LIMIT = 4096
PHASES = ('conceptualization', 'development-schematics', 'pre-implementation', 'implementation')


def read_state(root):
    path = Path(root) / 'production/session-state/active.md'
    result = {'path': str(path), 'status': 'ABSENT', 'focus': {}, 'checkpoint': '', 'limitations': []}
    if not path.exists():
        return result
    try:
        text = path.read_text(encoding='utf-8-sig')
    except (OSError, UnicodeError) as exc:
        result.update(status='UNREADABLE', limitations=[str(exc)])
        return result
    return parse_state(text, path)


def parse_state(text, path):
    """Validate one supplied snapshot; shared by readers and the rotation writer."""
    result = {'path': str(path), 'status': 'ABSENT', 'focus': {}, 'checkpoint': '', 'limitations': []}
    regions = {}
    positions = {}
    for name in ('STATUS', 'CHECKPOINT'):
        start, end = '<!-- ' + name + ' -->', '<!-- /' + name + ' -->'
        if text.count(start) != 1 or text.count(end) != 1:
            result['limitations'].append(name + ': missing or duplicate markers')
            continue
        a, b = text.index(start), text.index(end)
        if b < a:
            result['limitations'].append(name + ': reversed markers')
            continue
        body = text[a + len(start):b].strip()
        positions[name] = (a, b + len(end))
        if len(body.encode('utf-8')) > REGION_LIMIT:
            result['limitations'].append(name + ': exceeds 4096 UTF-8 bytes; omitted')
        else:
            regions[name] = body
    if len(positions) == 2 and positions['STATUS'][1] > positions['CHECKPOINT'][0]:
        result['limitations'].append('STATUS must precede CHECKPOINT without overlap')
    if result['limitations']:
        result['status'] = 'MALFORMED'
        return result
    focus = {}
    for field in ('Epic', 'Feature', 'Task'):
        values = re.findall(r'^' + field + r':[ \t]*([^\r\n]*)$', regions['STATUS'], re.M)
        if len(values) > 1:
            result.update(status='MALFORMED', limitations=[field + ': duplicate field'])
            return result
        if values and values[0].strip():
            focus[field] = values[0].strip()
    result.update(status='VALID', focus=focus, checkpoint=regions['CHECKPOINT'])
    return result


def read_stage(root):
    path = Path(root) / 'production/stage.txt'
    try:
        lines = [x.strip() for x in path.read_text(encoding='utf-8-sig').splitlines() if x.strip()]
    except FileNotFoundError:
        return {'declared': None, 'status': 'NOT SET'}
    except (OSError, UnicodeError) as exc:
        return {'declared': None, 'status': 'UNREADABLE', 'limitation': str(exc)}
    return {'declared': lines[0] if lines else None,
            'status': 'VALID' if len(lines) == 1 and lines[0] in PHASES else 'MALFORMED'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    result = read_state(args.root.resolve())
    print(json.dumps(result, ensure_ascii=True))
    raise SystemExit(2 if result['status'] in ('MALFORMED', 'UNREADABLE') else 0)
