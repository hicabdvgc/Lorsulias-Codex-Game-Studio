#!/usr/bin/env bash
# PreToolUse observer; command text is data, never evaluated.
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
source "$SCRIPT_DIR/hook-lib.sh"
select_hook_python
if [ ${#HOOK_PYTHON_CMD[@]} -eq 0 ]; then
  printf '%s\n' 'NOT ASSESSED: working Python is required for Git command observation.' >&2
  exit 1
fi
"${HOOK_PYTHON_CMD[@]}" "$(native_path "$SCRIPT_DIR/git-command-check.py")" commit "$(native_path "$(repo_root)")"
