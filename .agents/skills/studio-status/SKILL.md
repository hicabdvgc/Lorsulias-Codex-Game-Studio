---
name: studio-status
description: Report declared workflow section, current checkout evidence and bounded
  recovery focus.
---

# Studio Status

Invoke `$studio-status`. This workflow is read-only.

Read `.codex/docs/workflow-catalog.yaml`, `.codex/docs/progression.md`, live
`docs/technical-preferences.md` and relevant current artifacts. The four section IDs are
conceptualization, development-schematics, pre-implementation, implementation. Report the declared
section separately from available outcomes and missing prerequisites. Preserve unknown/legacy stage
values until their interpretation is explicitly resolved; counts/existence cannot establish progress.
Story Status fields own progress; selected sprint YAML is derived. Active scope needs an explicit or
unique existing reference, never modification time. There is no review-mode file to create.

## Root, focus and observations

Resolve the studio root from its installed helper/instructions, including non-Git and nested launches.
If Git exists, identify this checkout's actual branch/full HEAD and dirty state; otherwise report
non-Git or unavailable Git evidence. No terminal status line or cross-chat live monitoring is installed.

Use the available Python runtime to run `.codex/scripts/session-state.py --root <studio>`; it returns
JSON with valid STATUS fields, CHECKPOINT and explicit limitations. This is the same parser used by
hooks. On an unavailable runtime, report recovery NOT ASSESSED and offer manual file inspection;
do not invent a different marker parser. Valid optional Epic, Feature and Task form a focus breadcrumb
at any section. Missing focus remains none recorded. Malformed/oversized regions are not usable focus.

Report Scope, Declared section, Focus, Evidence, Recovery and Warnings. A stage file with unknown ID
or extra nonempty lines is explicitly malformed and remains unchanged. No declared section means
not set; relevant catalog outcomes may be assessed without replacing it with inferred progress.
Use bounded artifact discovery as observation only, and identify missing required outcome evidence.
