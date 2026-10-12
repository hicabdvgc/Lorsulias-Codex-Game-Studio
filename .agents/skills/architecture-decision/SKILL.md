---
name: architecture-decision
description: "Propose, retrofit, or explicitly accept an ADR, checking dependencies and governing stances without inventing approval or story readiness."
---

# Architecture Decision

Invoke as `$architecture-decision`.

Arguments: `[title | retrofit <project-local ADR path> | accept <ADR-id>] [--review full|lean|solo]`.

## Shared execution boundary

Read the relevant artifacts before asking about information they contain. Existing
bounded task authorization covers its edits and verification; ask about unresolved
consequential choices or a material scope expansion. Preserve unrelated changes
and re-read a target before writing if its baseline may have changed.

Use available qualified executors under the current environment's delegation
policy. Role names describe expertise. Follow `.codex/docs/review-workflow.md`
and `.codex/docs/director-gates.md`: required independent review and human evidence
remain required with any executor. Identify self-review; unavailable required
evidence is NOT ASSESSED. Review-depth flags change optional breadth, never these
obligations. `full` adds applicable specialist/gate reviews; `lean` is focused;
`solo` identifies self-review. Default to focused review when unspecified.

Apply `.codex/docs/skill-authoring.md` and `.codex/docs/error-recovery-protocol.md`.
Verify promised saved outputs before handoff. Resolve available support from the
installed catalog; require an input only when the selected activity needs its outcome.


## Resolve the mode and governing context

Missing subject prompts for the decision to address. Reject ambiguous ADR IDs,
invalid modes and paths outside the project. Read relevant GDD/master-architecture/
FRAMEWORK context, live preferences, affected accepted ADRs and the architecture
registry. Engine evidence applies to the actual decision; an engine-independent
decision can explain inapplicability instead of requiring a fabricated engine pin.
Read [CONTRACT.md](CONTRACT.md) for the produced handoff and permitted changes.

## Propose or retrofit

1. Identify the problem, constraints, alternatives, decision, tradeoffs, interfaces,
   validation criteria, and framework/resource effects. Resolve conflicts with an
   existing accepted stance before presenting the decision as settled.
2. Scan actual `adr-NNNN-[slug].md` records for identity collisions; choose an unused
   number after the highest existing ID. Recheck before writing. If a related ADR
   exists, distinguish revision, new decision and supersession instead of duplicating it.
3. Use the complete applicable `.codex/docs/templates/architecture-decision-record.md`.
   Include explicit ADR Dependencies, using Depends On: None only when confirmed.
   Link GDD requirements and existing TR IDs; new unsaved IDs are provisional.
4. New ADRs are Proposed. Reviewing them does not accept them. Keep candidate
   architectural stances in the proposal until acceptance; they do not govern CONTROL.
5. Retrofit preserves valid existing sections, fills missing relevant fields and
   corrects identified placeholders/contradictions. Do not infer historical acceptance
   from implemented code or silently accept through retrofit.
6. Perform applicable technical review using TD-ADR and actual evidence. A missing
   required review remains NOT ASSESSED; save a requested draft with that limitation
   rather than calling it accepted. Resolve known blockers before seeking acceptance.
7. Save the authorized ADR and explicitly included design-sync edits. Report status,
   evidence, proposed registry effects and the next review/acceptance activity.

## Accept an identified decision

An explicit request to accept the identified ADR supplies acceptance authorization.
Otherwise ask for that consequential decision once. File-write authorization alone
is not a choice to accept an unresolved architecture. Identify actual decision authority.

Read the current ADR and all transitive Depends On records. Use the adapted
`.codex/scripts/adr-dep-graph.sh` observations plus full relevant records. Require:
- A unique target whose filename and heading identity agree, with complete, unambiguous dependency declarations.
- Every applicable dependency exists uniquely and is Accepted.
- No self-dependency or dependency cycle in the target's dependency closure.
- Required technical/design/independent-review evidence exists and applies to this revision.
- No unresolved governing-stance conflict or unsettled consequential decision.

If the helper cannot execute, inspect the same dependency conditions directly;
if they cannot be established, return NOT ASSESSED without acceptance. Missing or
unaccepted dependencies and demonstrated conflicts return BLOCKED with the reason.
Problems in unrelated ADRs can be reported without automatically blocking this target.

On success, re-read affected files, set Accepted with authority/date/evidence,
and synchronize the relevant active architectural stances in one bounded changeset.
For an explicitly authorized replacement, mark the old decision Superseded, identify
the replacement and preserve stance history. Review affected dependents: an old
decision depending on a superseded record cannot silently inherit the new decision.
If already Accepted and unchanged, report NO CHANGE and check recorded provenance;
do not increment versions or duplicate registry entries merely for rerunning the mode.

Report ACCEPTED, NO CHANGE, BLOCKED, or NOT ASSESSED with actual changes and remaining
CONTROL/traceability work. Never mark stories Ready automatically; their other
prerequisites and the installed `$story-readiness` procedure remain independent obligations.
