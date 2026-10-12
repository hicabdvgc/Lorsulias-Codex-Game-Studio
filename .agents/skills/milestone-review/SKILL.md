---
name: milestone-review
description: Assess a defined milestone against actual outcome, quality and human
  play evidence, with separate schedule-risk analysis.
---

# Milestone Review

Invoke as `$milestone-review`. Arguments: `[milestone-name | current] [--review full|lean|solo]`.

Read [.codex/docs/execution-and-evidence.md](../../../.codex/docs/execution-and-evidence.md) for authorization, status, criterion-level evidence, review and recovery contracts. Read the relevant sources before editing.


Read production/milestones/MILESTONE.md and `.codex/docs/progression.md`. Resolve the requested section,
or an explicitly identified current milestone; ask if ambiguous. Missing definitions or incomplete
drafts leave achievement unassessed. Read relevant epics/stories, actual output/build, QA/bug evidence,
playtests from production/playtests/ or explicit legacy paths, and applicable technical requirements.
Do not require one milestone file per stage or a sprint structure.

Compare every defined outcome, intended completeness, quality target, playtest learning goal and
progression criterion with actual evidence. Separate fully met, partial and unmet work. Inspect
resource/tool/framework integration and human use where applicable. Story Complete counts and empty
bug lists cannot prove the experience works. Code health and performance observations require actual
scope/method and evidence. Missing roots/runtimes/reviews remain unassessed.

Apply PR-MILESTONE for production-risk reasoning with supplied schedules, capacity and comparable
history. Preserve required reviews across depth options. Unknown capacity cannot support velocity or
schedule forecasts. Discuss protect/at-risk/defer candidates against the actual milestone intent;
changing scope or dates remains a developer decision, not an automatic adjustment to make a pass.

Return **GO / GO WITH CONDITIONS / NO-GO / NOT ASSESSED**. GO WITH CONDITIONS is limited to advisory
matters; required failed/unavailable outcomes prevent GO. Preserve failures alongside missing evidence
and identify concrete next work. Default review is conversational; an explicit save uses
production/milestones/review-[milestone].md, preserving prior review evidence and unrelated sections.
Read back the output. Saving does not change MILESTONE requirements, record automatic achievement,
advance the phase or authorize release.
