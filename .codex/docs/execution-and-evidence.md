# Execution, Evidence and Completion

Use with [work preparation](work-preparation.md), [review workflow](review-workflow.md),
[code-root resolution](code-root-resolution.md) and the skill's specific contract.
This guidance adapts the ChatGPT and Claude execution/completion handoffs.

## Pickup and execution

Resolve the exact epic-qualified story and genuine prerequisites. Ready and In Progress
stories can enter `$dev-story`; Blocked work needs its blocker resolved. Complete/legacy
Done requires explicit reopening. In Review work requires a scoped rework request before
returning to In Progress. Missing, conflicting or unknown status needs resolution.
Validate current readiness against applicable Accepted ADRs, active saved TRs, integer
CONTROL rules and feasible criterion-level evidence. A reasoned governance N/A is valid
for any work type; it cannot hide a required unresolved decision. Compare registry and
source requirements and surface disagreement. A CONTROL revision change requires examining
affected rules, not merely updating the recorded number.

Resolve actual roots, interfaces, selected tools and version-sensitive APIs before writes
that depend on them. Code, resources, tools and framework integration are all supported
outputs. A creation task's future output is not its own pickup prerequisite. A genuine
incomplete dependency cannot be bypassed by accepting risk or changing its status without
completion evidence. An authorized redesign can change the dependency with its rationale.

State the bounded work and carry existing authorization through implementation and
verification. Ask about consequential unresolved decisions or scope expansion. Use a
qualified available executor under the active delegation policy; no persona grants tools
or authorizes spawning. Preserve independent review where required. Do not claim it for
the same executor's self-review.

Before writes, re-read current files and preserve concurrent changes. Set the story's
single header Status to In Progress first; then update its entry in the identified sprint's
derived YAML if applicable. Preserve membership, notes, unknown fields and unrelated work.
Report a failed secondary update as partial synchronization. Never roll back a valid story
to match stale YAML. Preserve useful implementation when a later check cannot run.

## Evidence

Map each applicable acceptance criterion to its actual method and result. Work type is
descriptive: mixed work retains all its checks. Automated assertions, contract inspection,
calculations, engine execution, manual use, listening and human play may each be relevant.
Required tests must actually run. Required human assessment needs a real person using the
identified build and protocol; an AI assessment, screenshot or unchecked sign-off cannot
stand in for it. Record the actual evaluator and whether independence was required/met.

Every result identifies scope, revision/build, inputs, method or exact command, actual
result and limitations. Distinguish PASS, FAIL, NOT RUN/NOT ASSESSED and justified N/A.
Preserve known failures when other checks are unavailable. Plans, existing files, dates
and counts never prove execution. A stale or unrelated smoke report cannot verify current
work; PASS WITH WARNINGS is usable only when the warning does not concern a required check
in this scope and applicable policy permits it.

Manual criterion evidence uses the story's declared path, normally production/qa/evidence/.
Automated reports use the selected runner's actual locations. New playtest records use
production/playtests/; QA plans, smoke reports and sign-offs remain under production/qa/.
Preserve explicit legacy report references. Name a session/scope/build where same-day
reports would collide; do not overwrite a different session. Use
[run and observe](run-and-observe.md) when runtime observation is needed.

## Completion and review writes

`$dev-story` reports Implemented and Verified, Implemented Not Verified, Partial or Blocked,
with criterion results and output paths. It leaves the story In Progress. `$story-done`
closes only when all required criteria, usable outputs, governing constraints and required
reviews/human evidence pass. Required deferred/unavailable checks block closure. Advisory
follow-ups may support COMPLETE WITH NOTES; they cannot waive required work.

Read-only assessments and reviews remain conversational. An explicit bounded save carries
authorization but confers no approval. A request to close the identified story authorizes
its completion fields and applicable derived status updates once conditions are satisfied.
Revalidation of a completed story does not reopen it or replace its completion date.
Maintain one Completion Notes section with actual evidence, reviews and remaining advisory
items. Use `$tech-debt` for authorized registration of consciously deferred work with stable
IDs and rationale; do not convert every note into debt.

Read back promised saves. A failed output prevents the handoff that consumes it, while
successful work stays intact; apply [recovery](error-recovery-protocol.md). Session checkpoints
are manual and scoped to existing authorization; installed lifecycle observers use context-management.md and never infer completion from notes.
No story closure automatically commits, pushes, closes a sprint, chooses a task or advances
a phase. Suggested candidates need actual declared status and dependency/readiness checks.

For retained `--review full|lean|solo` options, full includes applicable optional expert breadth, lean focuses on the selected scope, and solo identifies self-review. Use an explicit existing task/project choice; otherwise use focused review. Required independent/human evidence is unchanged. No additional review-mode configuration is introduced.
