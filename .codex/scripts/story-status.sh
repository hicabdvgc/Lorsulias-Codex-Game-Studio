#!/usr/bin/env bash
# Adapted from Claude Code Game Studios; read-only observations, no task selection.
# Usage: bash .codex/scripts/story-status.sh [studio-relative epic directory]
# No argument observes production/epics/*/story-*.md. Exit 0: discovery succeeded
# (including EMPTY); exit 2: invocation/runtime/discovery/read error, possibly partial.
set -u
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P) || exit 2
source "$SCRIPT_DIR/../hooks/hook-lib.sh"
select_hook_python
if [ ${#HOOK_PYTHON_CMD[@]} -eq 0 ]; then
    echo 'NOT ASSESSED: story-status requires working Python; see LORSULIA_HOOK_PYTHON.' >&2
    exit 2
fi
if [ "$#" -gt 1 ]; then
    echo 'Usage: story-status.sh [studio-relative epic directory]' >&2
    exit 2
fi
STUDIO_ROOT=$(repo_root)
if command -v cygpath >/dev/null 2>&1; then STUDIO_ROOT=$(cygpath -m "$STUDIO_ROOT"); fi
"${HOOK_PYTHON_CMD[@]}" - "$STUDIO_ROOT" "$@" <<'PY'
from pathlib import Path
import json, os, re, sys
root=Path(sys.argv[1]).resolve()
q=lambda value: json.dumps(str(value),ensure_ascii=True)
failed=False
groups={k:[] for k in ('IN_REVIEW','IN_PROGRESS','TODO','BLOCKED','OTHER','NO_STATUS','MALFORMED','CONFLICT','DONE')}
mapping={'in review':'IN_REVIEW','in progress':'IN_PROGRESS','ready':'TODO',
         'not started':'TODO','blocked':'BLOCKED','complete':'DONE','done':'DONE'}
try:
    base=(root/'production/epics').resolve()
    base.relative_to(root)
    scope=Path(sys.argv[2].replace('\\','/')) if len(sys.argv)>2 else base
    scope=(root/scope).resolve() if not scope.is_absolute() else scope.resolve()
    scope.relative_to(base)
    if not scope.is_dir(): raise ValueError('epic scope is missing or is not a directory')
    if scope!=base and scope.parent!=base: raise ValueError('expected epics root or one direct epic directory')
    # scandir surfaces discovery errors that glob may otherwise suppress.
    dirs=[scope]
    if scope==base:
        with os.scandir(base) as entries:
            dirs=sorted(Path(e.path) for e in entries if e.is_dir())
    files=[]
    for directory in dirs:
        directory.resolve().relative_to(base)
        with os.scandir(directory) as entries:
            files.extend(sorted(Path(e.path) for e in entries if re.fullmatch(r'story-.*\.md',e.name,re.I) and e.is_file()))
except (OSError,ValueError) as exc:
    print('NOT ASSESSED: discovery — '+str(exc),file=sys.stderr);sys.exit(2)
for path in sorted(files):
    rel=path.relative_to(root).as_posix()
    try:
        path.resolve().relative_to(base)
        lines=path.read_text(encoding='utf-8-sig').splitlines()
        statuses=[];malformed=[];fence=None;comment=False
        for number,line in enumerate(lines,1):
            # Strip HTML comments so examples there do not become declarations.
            clean=''
            while line:
                if comment:
                    if '-->' not in line: line='';continue
                    line=line.split('-->',1)[1];comment=False
                elif '<!--' in line:
                    part,line=line.split('<!--',1);clean+=part;comment=True
                else: clean+=line;line=''
            line=clean
            f=re.match(r'^\s{0,3}(`{3,}|~{3,})',line)
            if f:
                token=f.group(1)
                if fence is None:fence=token
                elif token[0]==fence[0] and len(token)>=len(fence):fence=None
                continue
            if fence:continue
            # Work metadata belongs before the first H2+ content section.
            if re.match(r'^\s{0,3}#{2,6}\s',line):break
            line=re.sub(r'^\s*(?:>\s*)?(?:-\s*)?','',line).replace('**','').strip()
            m=re.match(r'^Status\s*:\s*(.*?)\s*$',line,re.I)
            if m:statuses.append((number,m.group(1)))
            elif re.match(r'^Status(?:\s|$|[=：])',line,re.I):malformed.append(number)
        values=[s for _,s in statuses]
        if malformed or (len(values)>1 and len(set(values))==1):group='MALFORMED'
        elif len(values)>1:group='CONFLICT'
        elif not values:group='NO_STATUS'
        elif not values[0]:group='MALFORMED'
        else:group=mapping.get(values[0].casefold().removesuffix('.'),'OTHER')
        detail={'status':values,'lines':[n for n,_ in statuses]}
        if malformed:detail['malformed_lines']=malformed
        groups[group].append(q(rel)+' '+json.dumps(detail,ensure_ascii=True))
    except (OSError,UnicodeError,ValueError) as exc:
        failed=True;print('NOT ASSESSED: '+q(rel)+' — '+str(exc),file=sys.stderr)
if not files:print('STORIES      none (EMPTY: discovery succeeded)')
for group,rows in groups.items():
    for row in rows:print(f'{group:<12} {row}')
print(f'COMPLETE     {len(groups["DONE"])} of {len(files)} (declared status only)')
if failed:print('PARTIAL: one or more files were not assessed.',file=sys.stderr)
sys.exit(2 if failed else 0)
PY
