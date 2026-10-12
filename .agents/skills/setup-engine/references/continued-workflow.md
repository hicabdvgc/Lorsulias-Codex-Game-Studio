# Setup Engine — Reference and Upgrade Workflow

## Library and project versions

Maintain `docs/engine-reference/[engine]/VERSION.md` with documented version,
verification date, official sources, package/subsystem coverage and limitations.
Its baseline is distinct from the live project selection and installed binary.
Consult relevant module/plugin documents for the requested work. If a project's
selected version differs, verify the applicable behavior for that version before
using a baseline example. No LLM cutoff or assumed training coverage is evidence.

## Refresh

`refresh` reads the selected project engine and version. Refresh its relevant
reference files against official versioned sources, including applicable packages.
If no engine is selected, ask which library to refresh; an explicit request for all
libraries is valid and changes no project choice. Report newer stable releases
without upgrading the project selection. Mark only successfully checked content
as verified; unavailable evidence yields PARTIAL with affected paths/claims.

## Upgrade

1. Identify the old selected version from consistent live preferences and available
   project evidence. Resolve disagreement before writing version choices.
2. Verify the new version and migration requirements through official sources.
3. Inspect actual source/configuration for applicable migration candidates; a text
   match is a candidate until its use is examined. Report implications and gaps.
4. Establish whether actual project migration and its required checks have occurred.
   If absent, return the audit with INCOMPLETE and preserve the current selection.
5. Once migration is evidenced or explicitly confirmed by the user, update the
   authorized live version and reference coverage. Preserve unrelated choices.
   Existing scoped authorization is sufficient; do not add a second approval loop.
6. Re-read changed files and report exactly which documentation was updated,
   migration evidence supplied, remaining runtime checks, and affected ADR/CONTROL
   review. Do not automatically supersede ADRs based on their age or an engine release.

## Optional coherence observation

After resolving an explicit actual project root, use `.codex/scripts/project-coherence.sh
--project <actual root> --root <studio>` when a preferences/metadata comparison helps
readback. Read `.codex/docs/project-coherence.md`. Inspect each finding and any nonzero
execution error; unavailable metadata remains unassessed. The observer treats commands
as data, launches nothing and supplies no readiness or migration verdict.

## Result and boundaries

Report selected choices, installed-version evidence, documented reference coverage,
sources checked, written paths, unresolved fields and next activity. Use COMPLETE
for the requested documentation scope only; missing required evidence is INCOMPLETE
or PARTIAL. Installing engines, changing system configuration, migrating source,
and editing shared personas are separate tasks. Never claim those occurred here.
