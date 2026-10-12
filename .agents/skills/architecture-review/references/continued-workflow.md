# Architecture Review — Results and Traceability

## Review result

Report selected mode/scope, actual reviewer, input revisions, requirement coverage,
conflicts, dependency observations, applicable engine findings, unassessed checks
and required corrections. Include only phases belonging to the selected mode.

Verdict: PASS / CONCERNS / FAIL / NOT ASSESSED. Known blocking conflicts or critical
coverage gaps yield FAIL; otherwise unavailable required evidence yields NOT ASSESSED;
otherwise nonblocking deficiencies yield CONCERNS. PASS needs the applicable required
checks satisfied. Criticality follows actual impact and governing requirements,
not the name of an imposed architecture layer. Keep every finding visible.

## Authorized traceability saving

Use `.codex/docs/templates/architecture-traceability.md` for
`docs/architecture/architecture-traceability.md`. Persist a report only when requested,
at the identified destination. A conversational review does not require a report path.
The saving task is the writer; this is not an automatic review receipt or approval.

Before writing, re-read the TR registry and affected target rows. If another writer
allocated an ID, recompute new IDs against the current registry and update this
changeset's references together. If the same requirement changed incompatibly,
report the conflict and preserve that writer's work. Never overwrite unrelated rows.
Allocate after the highest existing per-system sequence, including retired IDs.
Persist same-intent edits under their original ID; retirement uses deprecated;
replacement uses the registry's quoted `superseded-by: TR-ID[, TR-ID]` string and
new identified requirements. No history deletion or identity reuse.

For `single-gdd`, preserve all other systems' rows. Write only selected index,
registry and report outputs; do not mutate story state, GDD approval or session memory.
Re-read saved outputs and check references before promising a durable handoff.

## RTM

Produce `docs/architecture/requirements-traceability.md` with TR-ID, source GDD,
governing Accepted decision/design, story reference, automated/manual/human evidence
reference and actual evidence state. Read real work-item/evidence locations from
their references and project configuration; do not assume every check lives in tests/.

Distinguish FILE EXISTS (not executed), FILE MISSING, NO STORY, pending human
observation and actual recorded results. File paths alone do not prove verification.
Before story/test authoring, absent future outputs are pending work. When reviewing
implementation completion, missing required evidence prevents a passing conclusion.
Do not fabricate story IDs or test runs. Use installed story/test producers for requested authoring; an installed producer does not establish its outputs exist.
