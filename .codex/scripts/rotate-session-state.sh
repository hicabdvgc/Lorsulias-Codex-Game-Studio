#!/usr/bin/env bash
# Explicit narrative rotation. --dry-run makes no writes; never lifecycle-registered.
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
source "$SCRIPT_DIR/../hooks/hook-lib.sh"
select_hook_python
if [ ${#HOOK_PYTHON_CMD[@]} -eq 0 ]; then
  printf '%s\n' 'NOT ASSESSED: rotation requires working Python 3.9+.' >&2
  exit 2
fi
"${HOOK_PYTHON_CMD[@]}" "$(native_path "$SCRIPT_DIR/rotate_session_state.py")" --root "$(native_path "$(repo_root)")" "$@"
