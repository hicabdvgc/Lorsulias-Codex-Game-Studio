#!/usr/bin/env bash
# PostToolUse observation: JSON syntax in res_lib/ and assets/data/ only.
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
source "$SCRIPT_DIR/hook-lib.sh"
read_hook_input || exit 0
select_hook_python
if [ ${#HOOK_PYTHON_CMD[@]} -eq 0 ]; then
    emit_hook_context "PostToolUse" "NOT ASSESSED: asset JSON syntax requires working Python."
    exit 0
fi
STUDIO_ROOT=$(repo_root)
if command -v cygpath >/dev/null 2>&1; then STUDIO_ROOT=$(cygpath -m "$STUDIO_ROOT"); fi
CHECK_CODE=$(cat <<'PY'
import json, os, re, sys
from pathlib import Path

def emit(message):
    print(json.dumps({'systemMessage': message, 'hookSpecificOutput': {
        'hookEventName': 'PostToolUse', 'additionalContext': message}}))

def native(value):
    value = value.replace('\\', '/')
    if os.name == 'nt' and re.match(r'^/[A-Za-z]/', value):
        value = value[1].upper() + ':' + value[2:]
    return Path(value)

try:
    event = json.load(sys.stdin)
    root = native(sys.argv[1]).resolve()
    if event.get('hook_event_name') not in (None, 'PostToolUse'):
        raise SystemExit(0)
    if event.get('tool_name') not in (None, 'apply_patch'):
        raise SystemExit(0)
    cwd_value = event.get('cwd', str(root))
    if not isinstance(cwd_value, str) or not native(cwd_value).is_absolute():
        raise ValueError('cwd must be an absolute path')
    cwd = native(cwd_value).resolve()
    cwd.relative_to(root)
    value = event.get('tool_input')
    paths, payloads = [], []
    if isinstance(value, str):
        payloads.append(value)
    elif isinstance(value, dict):
        for key in ('file_path', 'path'):
            if isinstance(value.get(key), str): paths.append(value[key])
        if isinstance(value.get('paths'), list):
            paths.extend(p for p in value['paths'] if isinstance(p, str))
        for key in ('command', 'patch', 'input'):
            if isinstance(value.get(key), str): payloads.append(value[key])
    else:
        raise ValueError('tool_input must contain patch text or path fields')
    for payload in payloads:
        for line in payload.splitlines():
            match = re.match(r'^\*\*\* (?:Add File|Update File|Delete File|Move to): (.+)$', line)
            if match: paths.append(match.group(1))
    if not paths:
        emit('NOT ASSESSED: no file paths could be extracted from this apply_patch input.')
        raise SystemExit(0)
    scope = [(root/'res_lib').resolve(), (root/'assets/data').resolve()]
    findings, seen = [], set()
    for raw in paths:
        path = native(raw)
        path = (path if path.is_absolute() else cwd/path).resolve()
        if path in seen: continue
        seen.add(path)
        if path.suffix.lower() != '.json': continue
        try: path.relative_to(root)
        except ValueError: continue
        if not any(path.is_relative_to(base) for base in scope): continue
        label = path.relative_to(root).as_posix()
        if not path.exists():
            findings.append(f'ABSENT: {label} (deleted/missing; syntax not checked)')
            continue
        if not path.is_file():
            findings.append(f'NOT ASSESSED: {label} is not a regular file')
            continue
        try:
            def reject_constant(token):
                raise ValueError(f'non-JSON numeric constant {token}')
            json.loads(path.read_text(encoding='utf-8-sig'), parse_constant=reject_constant)
        except (json.JSONDecodeError, UnicodeError, ValueError) as exc:
            findings.append(f'INVALID JSON: {label}: {exc}')
        except OSError as exc:
            findings.append(f'NOT ASSESSED: {label}: {exc}')
        else:
            findings.append(f'JSON SYNTAX OK: {label}')
    if findings:
        emit('\n'.join(findings) + '\nScope: JSON syntax only. Naming, schema, references, imports and usability are not assessed. The completed edit is unchanged.')
except (ValueError, TypeError, OSError) as exc:
    print(f'NOT ASSESSED: asset hook input/path error: {exc}', file=sys.stderr)
    raise SystemExit(1)
PY
)
printf '%s' "$HOOK_INPUT" | "${HOOK_PYTHON_CMD[@]}" -c "$CHECK_CODE" "$STUDIO_ROOT"
