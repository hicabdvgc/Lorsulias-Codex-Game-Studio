#!/usr/bin/env bash
# Adapted from Claude Code Game Studios. Observations, never acceptance/gate verdicts.
# Usage: bash .codex/scripts/adr-dep-graph.sh [project-local-adr-directory]
# Default directory: docs/architecture. Relative arguments are studio-relative.
# Exit 0: scan completed (including discovered problems). Exit 2: unavailable/partial scan.
set -u
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P) || exit 2
source "$SCRIPT_DIR/../hooks/hook-lib.sh"
select_hook_python
if [ ${#HOOK_PYTHON_CMD[@]} -eq 0 ]; then
    echo 'NOT ASSESSED: adr-dep-graph requires working Python; see LORSULIA_HOOK_PYTHON.' >&2
    exit 2
fi
if [ "$#" -gt 1 ]; then
    echo 'Usage: adr-dep-graph.sh [project-local-adr-directory]' >&2
    exit 2
fi
STUDIO_ROOT=$(repo_root)
# Convert MSYS virtual paths (including /tmp) before passing them to native Python.
if command -v cygpath >/dev/null 2>&1; then STUDIO_ROOT=$(cygpath -m "$STUDIO_ROOT"); fi
"${HOOK_PYTHON_CMD[@]}" - "$STUDIO_ROOT" "${1:-docs/architecture}" <<'PY'
from pathlib import Path
import json,re,sys
root=Path(sys.argv[1]).resolve()
try:
    directory=Path(sys.argv[2]);directory=(root/directory).resolve() if not directory.is_absolute() else directory.resolve()
    directory.relative_to(root)
    if not directory.is_dir():raise ValueError('ADR directory is missing or is not a directory')
    files=sorted((p for p in directory.iterdir() if p.is_file() and re.match(r'^adr-\d{4,}-.+\.md$',p.name,re.I)),key=lambda p:p.name.lower())
except (OSError,ValueError) as exc:
    print('NOT ASSESSED: '+str(exc),file=sys.stderr);sys.exit(2)
records={};failed=False
for p in files:
    ident=re.match(r'^(adr-\d{4,})-',p.name,re.I).group(1).upper()
    records.setdefault(ident,[]).append(p)
print('ADRS: '+str(len(files)))
graph={ident:set() for ident in records};statuses={}
for ident,paths in sorted(records.items()):
    if len(paths)>1:
        print('DUPLICATE_ID: '+ident+' '+json.dumps([p.name for p in paths]));continue
    p=paths[0]
    try:raw=p.read_text(encoding='utf-8-sig')
    except (OSError,UnicodeError) as exc:
        print('NOT ASSESSED: '+json.dumps(p.name)+' '+str(exc),file=sys.stderr);failed=True;continue
    # Ignore quoted examples in fenced code, which are not declarations.
    lines=[];fence=None
    for line in raw.splitlines():
        m=re.match(r'^\s{0,3}(`{3,}|~{3,})',line)
        if m:
            token=m.group(1)
            if fence is None:fence=token
            elif token[0]==fence[0] and len(token)>=len(fence):fence=None
            continue
        if fence is None:lines.append(line)
    s=re.sub(r'<!--.*?-->', '', '\n'.join(lines), flags=re.S)
    heading_ids=re.findall(r'^#\s+(ADR-\d{4,})\s*:',s,re.M|re.I)
    if len(heading_ids)!=1 or heading_ids[0].upper()!=ident:
        print('IDENTITY_MISMATCH: '+ident+' '+json.dumps(heading_ids))
    status_section=re.search(r'^##\s+Status\s*\n(.*?)(?=^##\s|\Z)',s,re.M|re.S|re.I)
    status_text=status_section.group(1).strip() if status_section else ''
    status_match=re.fullmatch(r'(Proposed|Accepted|Superseded)',status_text,re.I)
    # Canonical source-compatible alternative: a standalone Status: line.
    if not status_match:
        status_match=re.search(r'^\s*>?\s*(?:\*\*)?Status(?:\*\*)?\s*:\s*(?:\*\*)?(Proposed|Accepted|Superseded)(?:\*\*)?\s*$',s,re.M|re.I)
    statuses[ident]=status_match.group(1).title() if status_match else 'Unknown'
    print('STATUS: '+ident+' '+statuses[ident])
    dep_sections=re.findall(r'^##\s+ADR Dependencies\s*\n(.*?)(?=^##\s|\Z)',s,re.M|re.S|re.I)
    if len(dep_sections)!=1:
        print(('NO_DEPS_SECTION: ' if not dep_sections else 'MALFORMED_DEPS: ')+ident);continue
    rows=[]
    for line in dep_sections[0].splitlines():
        cells=[x.strip() for x in line.strip().strip('|').split('|')]
        if len(cells)>=2 and cells[0].replace('*','').strip().lower()=='depends on':rows.append(cells[1])
        elif re.match(r'^\s*(?:\*\*)?Depends On(?:\*\*)?\s*:',line,re.I):rows.append(line.split(':',1)[1].strip())
    if len(rows)!=1:
        print('MALFORMED_DEPS: '+ident+' (expected exactly one Depends On declaration)');continue
    value=rows[0].strip().strip('`"')
    if value.lower()=='none':
        print('NO_DEPENDENCIES: '+ident);continue
    deps=set(x.upper() for x in re.findall(r'\bADR-\d{4,}\b',value,re.I))
    if not deps or '[' in re.sub(r'\[[^\]]+\]\([^)]+\)','',value) or re.search(r'\bADR-(?!\d{4,}\b)',value,re.I) or re.search(r'\b(None|TBD|TODO|unknown)\b',value,re.I):
        print('MALFORMED_DEPS: '+ident+' '+json.dumps(value));continue
    graph[ident]=deps
print('EDGES:')
if not any(graph.values()):print('  (none declared)')
for a in sorted(graph):
    for b in sorted(graph[a]):
        print('  '+a+' -> '+b)
        if b==a:print('SELF_DEPENDENCY: '+a)
        if b not in records:print('MISSING_TARGET: '+a+' -> '+b)
        elif len(records[b])>1:print('AMBIGUOUS_TARGET: '+a+' -> '+b)
        elif statuses.get(b)!='Accepted':print('NON_ACCEPTED_TARGET: '+a+' -> '+b+' '+statuses.get(b,'Unknown'))
# Strongly connected components distinguish actual cycles from their dependents.
index=0;indices={};low={};stack=[];onstack=set();cycles=[]
def visit(v):
    global index
    indices[v]=low[v]=index;index+=1;stack.append(v);onstack.add(v)
    for w in sorted(graph[v]):
        if w not in graph:continue
        if w not in indices:visit(w);low[v]=min(low[v],low[w])
        elif w in onstack:low[v]=min(low[v],indices[w])
    if low[v]==indices[v]:
        component=[]
        while True:
            w=stack.pop();onstack.remove(w);component.append(w)
            if w==v:break
        if len(component)>1 or v in graph[v]:cycles.append(sorted(component))
for v in sorted(graph):
    if v not in indices:visit(v)
for component in sorted(cycles):print('CYCLE_MEMBERS: '+', '.join(component))
sys.exit(2 if failed else 0)
PY
