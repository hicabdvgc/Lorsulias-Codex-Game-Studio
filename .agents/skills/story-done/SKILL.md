---
name: story-done
description: Verify a story against actual criterion and review evidence, then close
  it within existing authorization and synchronize derived status.
---

# Story Done

Invoke as `$story-done`. Arguments: `[story-file-path] [--review full|lean|solo]`.

Read [.codex/docs/execution-and-evidence.md](../../../.codex/docs/execution-and-evidence.md) for authorization, status, criterion-level evidence, review and recovery contracts. Read the relevant sources before editing.


## Resolve and review

Resolve the named story, or an unambiguous current task. Otherwise show In Progress/In Review
candidates and ask. Read its full criteria, required outputs and evidence, governing source
requirements/Accepted ADRs, active TRs and applicable integer CONTROL rules. Use CONTRACT.md.
A non-ready draft requires readiness and implementation first. Complete/legacy Done can be
revalidated read-only; do not reopen it or change completion dates automatically.

Inspect actual output behavior, values, resource relationships and affected consumers. Compare
registry and design requirements; surface contradictions. A changed CONTROL revision needs
assessment of affected obligations before closure. Do not omit this check because a file is absent.
For each criterion show **criterion | method/evidence | revision/build | actual result | evaluator**.
Look first at declared evidence; other similar files are candidates until relevance is established.
Check actual assertions, execution results and required human sign-offs. Human reports must
identify the activity/build/result; ask for missing actual observations without fabricating them.

Apply QL-TEST-COVERAGE and LP-CODE-REVIEW from `.codex/docs/director-gates.md` where relevant
to the work. Preserve required independent review across full/lean/solo; name self-review
accurately. Non-code work needs its applicable output/contract reviews, with justified code-review
N/A. Coverage gaps are blocking whenever they concern required criteria, regardless of type or
percentage. Missing engine execution or required human assessment cannot be deferred into a pass.

## Verdict and authorized closure

Return **COMPLETE** when all required results/reviews pass, **COMPLETE WITH NOTES** when only
advisory matters remain, or **BLOCKED** for required failed or unavailable checks. Identify
NOT ASSESSED checks and known failures separately. Include governing deviations, scope changes,
criterion traceability and concrete corrective work. A report alone does not change status.

When the request authorizes closure and the result permits it, re-read the story and evidence,
set its header Status to Complete and update Last Updated. Maintain exactly one Completion
Notes section with actual completion date, evidence/revision, reviewers and advisory notes.
Synchronize the selected sprint's matching derived entry afterwards, preserving other fields.
If a save fails, verify completed writes and identify the unsynchronized view. Repeated successful
closure must not duplicate notes or restamp unchanged completion records.

Register advisory debt only when authorized and consciously deferred, using `$tech-debt`'s stable
IDs and existing register structure. Neither closure nor a review authorizes Git operations.
In a worktree distinguish branch completion from verification of a combined delivery.

## Next work

Read actual story statuses and dependencies in the selected scope. Suggest supported candidates
with readiness still to verify; do not choose the highest-numbered sprint or promote backlog by
priority. Blocked required stories remain incomplete. Surface applicable smoke, QA and retrospective
work after the selected sprint's required work is actually complete. Stage progression is a
separate `$gate-check` assessment and requires its own authorization/evidence.
