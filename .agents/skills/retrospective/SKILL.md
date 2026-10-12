---
name: retrospective
description: "Generates a sprint or milestone retrospective by analyzing completed work, velocity, blockers, and patterns. Produces actionable insights for the next iteration."
---
Read `.codex/docs/work-preparation.md` for status authority, criterion-level evidence, applicable governance, authorization, concurrent writes and recovery.


## Invocation and execution

Invoke this workflow as `$retrospective`.

An authoring or scoped update request authorizes its bounded save. Preserve existing records and ask only about unresolved consequential choices, including ambiguous update targets or a requested archive destination.

Arguments: `[sprint-N|milestone-name]`. Treat bracketed values as optional unless the workflow says otherwise.


## Phase 1: Parse Arguments

Determine whether this is a sprint retrospective (`sprint-N`) or a milestone
retrospective (`milestone-name`). With no argument, list the exact existing
sprint and milestone candidates and ask the user to choose one. Reject unknown
argument forms. If a name matches multiple artifacts, list their paths and ask;
do not pick by filename or modification time.

Resolve one non-empty existing target and retain its identifier for every later
data-source check. If the selected file is empty, stop or accept user-provided
data explicitly. Do not allow a current status file to substitute for a
different or historical target.

---

## Phase 1b: Check for Existing Retrospective

Before loading any data, search for an existing retrospective file:

- For sprint retrospectives: `production/retrospectives/retro-[sprint-slug]-*.md`
  (also check `production/sprints/sprint-[N]-retrospective.md` as an alternate location)
- For milestone retrospectives: `production/retrospectives/retro-[milestone-name]-*.md`

If the request identifies an existing record to update, preserve its unrelated
content and revise the requested scope. If several records could be the target
or fresh versus update is unresolved, clarify that choice. A new dated record
preserves earlier records. Archive or move an earlier record only if explicitly
requested; re-read it immediately before the move and preserve conflicting work.

---

## Phase 2: Load Sprint or Milestone Data

Read the sprint or milestone plan from the appropriate location:

- Sprint plans: `production/sprints/`
- Milestone definitions: the identified stage in `production/milestones/MILESTONE.md`

Use `production/sprint-status.yaml` only when its sprint identifier matches the
exact retrospective target. A milestone retrospective aggregates only the
sprints/goals explicitly included by the milestone artifact and never imports
an unrelated current sprint status. Note discrepancies between matching status
and plan sources. Story Status fields own current work progress; YAML is derived.
Historical conclusions require a record for the assessed period. Today’s story
status cannot establish its status at an earlier sprint boundary.

If the target file does not exist or is empty, offer the user two options:

- provide tasks, dates, and outcomes manually as an explicitly identified source;
- stop with **BLOCKED — no sprint or milestone data available**.

Extract planned tasks, estimated effort, owners, goals, and an explicit period.
Actual effort, bug counts, estimation accuracy, and historical velocity may be
calculated only when existing artifacts explicitly provide the values. Missing
inputs are `N/A — source unavailable`; do not infer time spent from commits or
completion dates.

Read Git history only when the selected artifact provides a clear start/end
period, and constrain the query to it. If the period is absent or the dated
query fails, mark the commit metric unavailable. Do not substitute the most
recent 20 commits or another arbitrary window.

---

## Phase 3: Analyze Completion and Trends

Compare the plan against actual deliverables and identify:

- tasks completed as planned;
- tasks completed but modified from the plan;
- tasks carried over;
- tasks added mid-period;
- tasks removed or descoped.

For TODO/FIXME/HACK reporting, use the same existing project source/content
directories and exclusions for the current and historical counts. State the
scope. If a prior retrospective did not use the same method, report current
counts only and do not claim a growing/shrinking trend.

Read previous retrospectives to check earlier action items and velocity. In the
three-period table, display `N/A` for every unavailable period. Describe a trend
only when at least two periods have comparable definitions and data.

Separate evidence types throughout the analysis:

- **Artifact-backed observation**: cite the plan, status, bug, Git-period, or
  retrospective source.
- **User-provided reflection**: label it as the user's/team's reflection.
- **Unknown cause or sentiment**: write `Unknown — team reflection not supplied`.

Do not infer what went well/poorly or a likely cause solely from commit volume
or status changes.

---

## Phase 4: Generate the Retrospective

Keep every metric source-traceable. Use `N/A — source unavailable` where needed.

```markdown
## Retrospective: [Sprint N / Milestone Name]
Period: [Start Date] -- [End Date]
Generated: [Date]

### Metrics

| Metric | Planned | Actual | Delta |
|--------|---------|--------|-------|
| Tasks | [X] | [Y] | [+/- Z] |
| Completion Rate | -- | [Z%] | -- |
| Story Points / Effort Days | [X] | [Y or N/A] | [delta or N/A] |
| Bugs Found | -- | [N or N/A] | -- |
| Bugs Fixed | -- | [N or N/A] | -- |
| Unplanned Tasks Added | -- | [N] | -- |
| Commits | -- | [N or N/A] | -- |

[Cite the existing source path beside each populated metric; use N/A when unavailable.]

### Velocity Trend

| Sprint | Planned | Completed | Rate |
|--------|---------|-----------|------|
| [N-2] | [X/N/A] | [Y/N/A] | [Z%/N/A] |
| [N-1] | [X/N/A] | [Y/N/A] | [Z%/N/A] |
| [N] | [X/N/A] | [Y/N/A] | [Z%/N/A] |

**Trend**: [Increasing / Stable / Decreasing / N/A]
[Only compare at least two like-for-like periods.]

### What Went Well
- [Artifact-backed observation with source]
- [User-provided reflection, labeled]
- [Unknown if no evidence/reflection exists]

### What Went Poorly
- [Artifact-backed observation with impact]
- [User-provided reflection, labeled]
- [Do not infer team sentiment or blame]

### Blockers Encountered

| Blocker | Duration | Resolution | Prevention |
|---------|----------|------------|------------|
| [blocker] | [value/N/A] | [value/N/A] | [reflection/Not supplied] |

### Estimation Accuracy

| Task | Estimated | Actual | Variance | Likely Cause |
|------|-----------|--------|----------|--------------|
| [task] | [X] | [Y/N/A] | [Z/N/A] | [user-provided/Unknown] |

**Overall estimation accuracy**: [evidence-backed percentage or N/A]

### Carryover Analysis

| Task | Original Sprint | Times Carried | Reason | Action |
|------|----------------|---------------|--------|--------|
| [task] | [sprint] | [N/N/A] | [artifact/user/Unknown] | [decision/Not set] |

### Technical Debt Status
- Measurement scope: [directories/exclusions]
- Current TODO/FIXME/HACK counts: [N]
- Comparable previous counts: [N or N/A]
- Trend: [Growing/Stable/Shrinking/N/A]

### Previous Action Items Follow-Up

| Action Item | Status | Notes |
|-------------|--------|-------|
| [previous action] | [Done/In Progress/Not Started] | [source] |

### Action Items for Next Iteration

| # | Action | Owner | Priority | Deadline |
|---|--------|-------|----------|----------|
| 1 | [action] | [provided owner or Unassigned] | [High/Med/Low] | [provided date or Not set] |

### Process Improvements
- [Specific evidence-backed or user-provided proposal]

### Summary
[2-3 sentences distinguishing observations from reflection.]
```

Use agreed actions, owners and deadlines already supplied. Label proposed actions
as proposals; absent commitments remain Unassigned and Not set. Saving the
retrospective does not assign commitments or establish milestone achievement.

---

## Phase 5: Save Retrospective

Present the findings and save within the requested scope. For new records use
`production/retrospectives/retro-[sprint-slug]-[date].md` or
`production/retrospectives/retro-[milestone-name]-[date].md`. Re-read before updates,
preserve concurrent and unrelated content, then inspect the saved file. Report
**COMPLETE — retrospective saved** only after verifying it. A failed dependent
activity preserves the completed record and is reported separately.

---

## Phase 6: Next Steps

End after saving or declining. Provide the generated file path and existing
commands as optional later handoffs:

- `$sprint-plan new` may consume the retrospective when the user invokes it later.
- For a milestone, `$gate-check` is a separate installed assessment; it needs actual outcome evidence.

Do not invoke either workflow from this retrospective run.

### Guidelines

- Be honest and specific; distinguish facts from team reflection.
- Focus on systemic issues, not individual blame.
- Include the actions supported by findings and agreed scope.
- Do not assign an owner, deadline, or cause unless an artifact or the user supplies it.
- For milestone retrospectives, evaluate only explicitly included goals and sprints.
