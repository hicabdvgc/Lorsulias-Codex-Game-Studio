#!/usr/bin/env bash
# Adapted from Claude Code Game Studios. Read-only, explicitly scoped observations.
set -u
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P) || exit 2
source "$SCRIPT_DIR/../hooks/hook-lib.sh"
select_hook_python
if [ ${#HOOK_PYTHON_CMD[@]} -eq 0 ]; then
  printf '%s\n' 'NOT ASSESSED: project-coherence requires working Python 3.9+; set LORSULIA_HOOK_PYTHON.' >&2
  exit 2
fi
# Convert explicit path arguments even when MSYS argument conversion is disabled.
ARGS=()
while [ "$#" -gt 0 ]; do
  case "$1" in
    --root|--project)
      ARGS+=("$1"); shift
      if [ "$#" -eq 0 ]; then printf '%s\n' 'Missing path argument.' >&2; exit 2; fi
      ARGS+=("$(native_path "$1")"); shift ;;
    *) ARGS+=("$1"); shift ;;
  esac
done
"${HOOK_PYTHON_CMD[@]}" "$(native_path "$SCRIPT_DIR/project_coherence.py")" --root "$(native_path "$(repo_root)")" "${ARGS[@]}"
