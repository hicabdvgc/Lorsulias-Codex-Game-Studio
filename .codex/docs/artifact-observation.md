# Artifact and Gap Observation

Run `bash .codex/scripts/artifact-check.sh [--phase <catalog-phase-id>] [--root <studio-root>]`.
Default root comes from the installed script's location, including nested/non-Git launches. --root
selects an explicit alternate studio/fixture. Python and PyYAML are required; shared hook-lib.sh
selects Python, including process-local LORSULIA_HOOK_PYTHON. A selected runtime may need its existing
PyYAML path available. Missing parser is NOT ASSESSED; no installation or personal configuration edit
is performed.

The observer safely parses workflow-catalog.yaml, checks unique keys/step identities and reports
only explicit artifact.path entries. Output JSON has root, steps_observed, counts and observations
with phase/id/outcome/status and optional path/maturity/error. PRESENT, ABSENT, EMPTY, UNREADABLE
and NO_CHECK describe discovery. NO_CHECK is expected for manual outcomes without a declared path.
Exit 0 means discovery completed with no absent/empty/unreadable paths; 1 means absent/empty paths;
2 means input/catalog/parser/read errors. Invalid arguments use argparse exit 2. Neither exit 0 nor
PRESENT establishes document maturity, manual activity completion or a gate pass.

`bash .codex/hooks/detect-gaps.sh` is an explicit, no-argument observer. It reports the live preferences'
engine/root fields verbatim and invokes artifact observation. Root prose remains subject to
code-root-resolution.md; no automatic source scan or root selection occurs. Missing preferences are
reported separately. SessionStart calls bounded discovery for startup/resume/clear; compact recovery omits the repeated scan. No automatic receipt/skipping behavior
is supplied. Use project-stage-detect or gate-check to assess actual outcomes with the required evidence.

Python observers require Python 3.9 or newer. The native_path helper converts executable script/root paths explicitly for native Windows Python; it does not change personal shell configuration.
