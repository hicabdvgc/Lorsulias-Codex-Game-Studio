#!/usr/bin/env bash
# Read-only observer, also called by SessionStart for startup/resume/clear (not compact).
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
source "$SCRIPT_DIR/hook-lib.sh"
if [ "$#" -ne 0 ]; then
  printf '%s\n' 'NOT ASSESSED: detect-gaps.sh takes no arguments; run from its selected studio.' >&2
  exit 2
fi
ROOT=$(repo_root)
printf '%s\n' 'Observation scope: declared catalog paths and live technical preferences; no phase/completeness inference.'
if [ -r "$ROOT/docs/technical-preferences.md" ]; then
  # Show authority verbatim; parsing prose cannot safely select project roots.
  grep -E '^\- \*\*(Engine|Project / Code Roots|Test Roots and Commands)\*\*:' "$ROOT/docs/technical-preferences.md"
  printf '%s\n' 'Resolve configured roots and project evidence using code-root-resolution.md; no source scan was performed.'
else
  printf '%s\n' 'NOT ASSESSED: live docs/technical-preferences.md is absent or unreadable.'
fi
bash "$SCRIPT_DIR/../scripts/artifact-check.sh"
