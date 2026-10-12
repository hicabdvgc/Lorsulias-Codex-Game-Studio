# Prototype — Spike, Report and Handoff

## Technical spike

When --spike is passed, identify one technical uncertainty, available prerequisites,
the cheapest representative experiment and the result needed to resolve it. Use
the supplied time bound if any; do not invent a standard duration. A spike may
inspect or exercise an existing interface when authorized and clearly isolated.
Record borrowed dependencies and limits on generalization to production.

Build/run the relevant experiment in `prototypes/[slug]-spike/`. Report actual
results, constraints, tradeoffs, retained uncertainty and recommendation for the
architecture or design. Lack of execution is NOT ASSESSED, never a measured success.

## Report and index

Use `.codex/docs/templates/prototype-report.md` for REPORT.md in the experiment.
Preserve the supplied task's hypothesis, actual inputs, commands/methods, observations,
human feedback, and what could not be tested. For paper work, label a model-guided
simulation separately from a human play session. Never manufacture quotes or counts.

Update the relevant row in `prototypes/index.md` as part of the authorized prototype
output, recording experiment path, question, route, evidence/result and next activity.
Create the index if absent; preserve unrelated entries. A failed experiment remains
valuable evidence and must not be omitted. Verify both promised outputs after saving.

## Retention and workflow progression

Record retain/revise/archive/remove/undecided with reasoning. Do not delete files
merely because the prototype phase ended. Production reuse requires checking the
actual production contracts, technical quality and relevant verification. No blanket
cross-directory import ban replaces the explicit experiment boundary.

Use a scoped creative review when requested; unavailable human evidence
prevents a feel conclusion. The developer decides consequential pivots or abandonment.
Hand findings to the relevant concept-support, GDD, FRAMEWORK or ADR activity.
Use installed vertical-slice and gate-check for the separate slice and its required human/framework hard gate.
