#!/usr/bin/env bash
# Adapted from Claude Code Game Studios: explicit-scope heading observations only.
# Usage: bash .codex/scripts/gdd-structure-check.sh <project-local-gdd> [...]
# Output: JSON-quoted path followed by PRESENT / ABSENT labels. No quality verdict.
# Exit 0: observations produced. Exit 2: invocation/read/runtime failure (may be partial).
set -u
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P) || exit 2
source "$SCRIPT_DIR/../hooks/hook-lib.sh"
select_hook_python
if [ ${#HOOK_PYTHON_CMD[@]} -eq 0 ]; then
    echo 'NOT ASSESSED: gdd-structure-check requires working Python; see LORSULIA_HOOK_PYTHON.' >&2
    exit 2
fi
if [ "$#" -eq 0 ]; then
    echo 'Usage: gdd-structure-check.sh <project-local-gdd> [...] (scope supplied by caller)' >&2
    exit 2
fi
STUDIO_ROOT=$(repo_root)
# Convert MSYS virtual paths (including /tmp) before passing them to native Python.
if command -v cygpath >/dev/null 2>&1; then STUDIO_ROOT=$(cygpath -m "$STUDIO_ROOT"); fi
"${HOOK_PYTHON_CMD[@]}" - "$STUDIO_ROOT" "$@" <<'PY'
from pathlib import Path
import json,re,sys
root=Path(sys.argv[1]).resolve()
labels={
 'Overview':r'Overview', 'Player Fantasy':r'Player Fantasy',
 'Detailed Rules':r'Detailed (?:Rules|Design)|Core Rules', 'Formulas':r'Formulas',
 'Edge Cases':r'Edge Cases', 'Dependencies':r'Dependencies',
 'Tuning Knobs':r'Tuning Knobs', 'Acceptance Criteria':r'Acceptance Criteria',
 'Framework Operations':r'Framework Operations(?: and Resource Needs)?',
 'Resource Needs':r'Resource (?:Needs|Requirements)|Framework Operations and Resource Needs'
}
failed=False
for arg in sys.argv[2:]:
    try:
        p=Path(arg)
        # Explicit relative paths are studio-relative, consistent from subdirectory launches.
        p=(root/p).resolve() if not p.is_absolute() else p.resolve()
        p.relative_to(root)
        if p.suffix.lower()!='.md' or p.name.lower() in {'agents.md','concept.md','breakdown.md'}:
            raise ValueError('expected a system GDD, not a governance document')
        lines=p.read_text(encoding='utf-8-sig').splitlines()
        headings=[]; fence=None
        for line in lines:
            match=re.match(r'^\s{0,3}(`{3,}|~{3,})',line)
            if match:
                token=match.group(1)
                if fence is None:fence=token
                elif token[0]==fence[0] and len(token)>=len(fence):fence=None
                continue
            if fence:continue
            m=re.match(r'^\s{0,3}#{2,6}\s+(.+?)\s*#*\s*$',line)
            if m:headings.append(re.sub(r'^\d+[.)]?\s+','',m.group(1)))
        present=[name for name,pattern in labels.items() if any(re.fullmatch(pattern,h,re.I) for h in headings)]
        absent=[name for name in labels if name not in present]
        print(json.dumps(p.relative_to(root).as_posix(),ensure_ascii=True)+' PRESENT: '+', '.join(present))
        if absent:print(json.dumps(p.relative_to(root).as_posix(),ensure_ascii=True)+' ABSENT: '+', '.join(absent))
    except (OSError,UnicodeError,ValueError) as exc:
        failed=True;print('NOT ASSESSED: '+json.dumps(arg)+' — '+str(exc),file=sys.stderr)
sys.exit(2 if failed else 0)
PY
