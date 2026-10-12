---
name: create-stories
description: "Decompose an epic into bounded stories with genuine prerequisites, applicable governance and criterion-level evidence."
---

# Create Stories

Read `.codex/docs/work-preparation.md` for governing inputs, status authority,
criterion-level evidence, review, authorization and recovery rules. Apply them to
the selected scope. Read the package CONTRACT.md when present for its handoff.

## Invocation
`$create-stories [epic-slug | epic-path] [--review full|lean|solo]`.
No target lists existing epics and asks for selection. Reject unknown flags and
project-external/ambiguous targets. Use a valid explicit review-depth flag; otherwise
use focused (lean) review. Required review remains required.

## Load and decompose
Read the selected EPIC, mapped system requirements, FRAMEWORK operation and applicable
architecture/ADRs/CONTROL/TR registry. Read actual resource definitions, required
tools and slice findings for this scope. Do not require final MILESTONE at this step.
Missing required sources prevent a ready handoff; preserve a useful non-ready draft
with its gaps when requested. New resources/tools listed as outputs may be absent.

Group related criteria into independently understandable deliverables. Order by real
dependencies, including resources, tooling and integration. Do not force UI last,
one session per story, or an hours threshold. Use the five existing Type values as
descriptions; mixed criteria retain all their evidence obligations.

Identify governing decisions and preserve their actual statuses. Any applicable
non-Accepted ADR prevents Ready. Real ADR lists name one primary explicitly. A
reasoned N/A is available to all types when no ADR applies. Required TR references
must resolve to saved active entries; no placeholder ID or new allocation here.
Record scoped CONTROL rules and integer revision where applicable.

## Evaluation and readiness
Map each criterion to Given/When/Then or Setup/Action/Observe/Decision basis,
appropriate failure cases and required evidence. Combine automated, manual and human
methods as needed; file existence is not execution. Existing QA plans are reused
by exact story/epic identity and relevant revision, not newest-file selection.
Reconcile conflicts before reusing cases. A current-agent draft is identified as such;
QA expertise may improve it, and required independent review stays separate.

Use QL-STORY-READY and the installed `$story-readiness` checklist on the complete
candidate (pass planned path plus full draft before it exists). Readiness applies
to pickup now: a predecessor merely scheduled earlier is not completed. Missing
required independent assessment prevents Ready. A failed/missing review cannot be
waived with lean/solo. Keep optional consultations proportional to the work.

## Story output
Save `production/epics/[epic-slug]/story-NNN-[slug].md` with this interface:

```markdown
# Story [NNN]: [title]
> Epic: [identity and path]
> Status: [Not Started / Ready / Blocked]
> Layer: [actual project grouping or N/A]
> Type: [Logic | Integration | Visual/Feel | UI | Config/Data]
> Estimate: [basis and unit, or unknown; planning gap does not itself forbid pickup]
> Manifest Version: [integer or justified N/A]
> Last Updated: [actual edit date]

## Context
Readiness basis: [assessment, actual review evidence and unresolved gaps]
GDD / governing requirement: [exact source and active TR when applicable]
Governing ADRs: [all actual statuses, one explicit primary, or reasoned N/A]
Decision summaries and scoped CONTROL rules: [meaning-preserving]
Engine evidence: [selected version and relevant verified/unknown capabilities]
FRAMEWORK operation and affected consumers: [addition/modification route]
## Acceptance Criteria
- [ ] AC-1: [specific result from the governing requirement]
## Implementation Notes
[Applicable design/decision guidance; the actual source remains authoritative.]
### Required inputs / Files to Create or Modify
[Separate usable prerequisites from future outputs and permitted edits.]
## Out of Scope
[Boundaries and related work.]
## QA Test Cases
[Criterion-specific setup, action, expectation and relevant failure cases.]
## Test Evidence
| Criterion | Required method / evaluator | Planned evidence location | State |
|---|---|---|---|
| AC-1 | [one or several methods; actual independence/human needs] | [selected path] | Pending |
## Dependencies
[Explicit qualified IDs/paths and required completion, or None.]
```

## Save and handoff
Reread the directory, stories, EPIC and index before allocation. Preserve IDs;
reuse/update a matched existing story within scope, never reuse an occupied number.
Update the EPIC Stories table and its existing index row with actual counts and
coverage. Missing/ambiguous index targets are a reported incomplete handoff.
Prepare all intended writes within authorization, preserve concurrent progress and
verify saved contents. Never reset In Progress/In Review/Complete work on a rerun.
Report saved paths, readiness gaps and next checks. `$story-readiness` is available;
Implementation and completion use installed `$dev-story` and `$story-done`. No implementation occurs.
