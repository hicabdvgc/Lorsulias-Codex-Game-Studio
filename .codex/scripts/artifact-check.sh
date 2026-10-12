#!/usr/bin/env bash
# Explicit read-only observer. Exit 0 observations/no missing paths, 1 absent/empty, 2 error.
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
source "$SCRIPT_DIR/../hooks/hook-lib.sh"
select_hook_python
if [ ${#HOOK_PYTHON_CMD[@]} -eq 0 ]; then
  printf '%s\n' '{"status":"NOT ASSESSED","error":"Working Python with PyYAML is required."}'
  exit 2
fi
"${HOOK_PYTHON_CMD[@]}" "$(native_path "$SCRIPT_DIR/artifact-check.py")" "$@"
