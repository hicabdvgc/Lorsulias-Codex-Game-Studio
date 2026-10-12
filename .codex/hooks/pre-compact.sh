#!/usr/bin/env bash
# PreCompact observer; shared checkpoint parser and installed-root resolution.
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
source "$SCRIPT_DIR/hook-lib.sh"
select_hook_python
if [ ${#HOOK_PYTHON_CMD[@]} -eq 0 ]; then
  emit_continue_json 'NOT ASSESSED: lifecycle observer requires working Python 3.9+.'
  exit 1
fi
"${HOOK_PYTHON_CMD[@]}" "$(native_path "$SCRIPT_DIR/../scripts/session_lifecycle.py")" --event PreCompact --root "$(native_path "$(repo_root)")" --bash "$(native_path "$(command -v bash)")"
