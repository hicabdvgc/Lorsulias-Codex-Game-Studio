---
name: sprint-plan
description: "Create, update or inspect optional sprint subdivisions of defined milestones using real capacity, dependencies and story-owned status."
---

# Sprint Plan

Read `.codex/docs/work-preparation.md` for status authority, criterion-level evidence, applicable governance, authorization, concurrent writes and recovery.

## Invocation
`$sprint-plan [new|update|status] [--review full|lean|solo]`; default is new.
Resolve review depth from a valid explicit flag; otherwise use focused (lean) review.
Depth cannot waive required review or human evidence. Do not create
a review-mode configuration. Reject unknown modes and clarify an ambiguous sprint.

## Shared inputs
Read the selected stage in `production/milestones/MILESTONE.md`, relevant epics and
story files, dependencies, current plan and `production/sprint-status.yaml`.
Sprints are optional subdivisions of defined milestones. Missing milestone
definitions leave a proposed subdivision incomplete; use `$define-milestones`
with its gate requirements. Do not impose dates, sprint length or a reserve.
Use supplied availability, estimates with their units, actual obligations and
comparable historical evidence. Missing capacity leaves feasibility unassessed.
Read the selected QA scope and actual readiness/review evidence. A QA filename
or sprint priority cannot establish readiness or coverage.

## New
1. Identify the selected milestone outcomes and a coherent sprint goal.
2. Inventory candidate stories from their actual paths and Status fields. The
   read-only `.codex/scripts/story-status.sh` can assist discovery; its summary
   cannot establish readiness or pick the next task.
3. Order dependencies and identify unresolved blockers. A future dependency
   sequence does not make a dependent story ready for immediate pickup.
4. Use explicit carryover decisions. Show incomplete prior work and its current
   progress; do not silently discard, reset or include it.
5. Fit comparable estimates to supplied capacity, separating unknown estimates,
   units, contingency selected by the project, review and human evaluation effort.
   Mark Must/Should/Nice priorities as planning choices without changing Status.
6. Obtain applicable PR-SPRINT assessment using the director-gates guidance and
   available qualified executor. Record unavailable assessment and missing inputs;
   a draft may be useful, but does not pass a feasibility or independent-review gate.
7. Save `production/sprints/sprint-[N]-plan.md` using the sprint-plan template and
   the selected sprint's derived `production/sprint-status.yaml`. Re-read existing
   sprint identifiers and indexes before choosing an unused identifier.

## Update
Read the identified plan, YAML and every referenced story again. Report disagreements
before synchronizing. The update request authorizes deriving YAML status from stories;
it does not authorize silently changing story progress. Preserve existing membership,
priority, owner, estimates and custom fields except the requested planning changes.
Removal, carryover or rescheduling requires a supplied decision when consequential.
Reassess changed dependencies, capacity and QA scope. Preserve In Progress, In Review
and Complete work in the authoritative files. Keep unknown/malformed statuses visible.

## Status
Read only. Show the selected sprint's membership, story Status, derived YAML status,
disagreements, blockers and unassessed coverage. Do not synchronize, assign readiness,
select an executable next task or claim completion from this summary. Missing,
unreadable or empty scope is explicit, never a healthy empty sprint.

## Derived YAML interface
Retain existing fields and status mappings in work-preparation.md. For a new view:
```yaml
sprint: 1 # actual selected identifier
goal: "selected goal"
start: null
end: null
generated: "actual date"
updated: "actual date"
stories:
  - id: "epic-slug/story-001" # qualified, stable identity
    name: "existing story title"
    file: "production/epics/epic-slug/story-001-example.md"
    priority: must-have
    status: backlog # derived from Not Started, irrespective of priority
    owner: null
    estimate_days: null # only supplied/justified day estimates; keep other units explicit
    blocker: null
    completed: null # actual completion evidence/date, never generated from priority
```
This example is illustrative, not a project default. Preserve existing stable IDs
and map them through their file references; do not renumber existing stories. Report
duplicate identities, ambiguous references and invalid mappings before dependent
updates. A missing/unreadable story retains its membership with unresolved status;
do not fabricate a supported status. Leave that synchronization incomplete.

## Save and handoff
Re-read plan, YAML, stories and shared indexes immediately before writing. Merge
concurrent additions by identity; stop affected conflicting edits for resolution.
Inspect both saved outputs and their agreement with current stories. If one save
fails, retain the completed output and report the unsynchronized view. Summarize
goal, membership, capacity basis, blockers, QA coverage and actual review result.
Report COMPLETE only for the requested planning work; PARTIAL/NOT ASSESSED identifies
unresolved feasibility or synchronization. Story execution/completion uses installed dev-story/story-done and execution-and-evidence.md.
