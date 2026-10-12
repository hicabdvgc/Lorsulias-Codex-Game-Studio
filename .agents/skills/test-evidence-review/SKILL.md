---
name: test-evidence-review
description: Review actual automated, manual and human evidence for a story, sprint
  or system without changing work status.
---

# Test Evidence Review

Invoke as `$test-evidence-review`. Arguments: `[story-path | sprint | system-name]`.

Read [.codex/docs/execution-and-evidence.md](../../../.codex/docs/execution-and-evidence.md) for authorization, status, criterion-level evidence, review and recovery contracts. Read the relevant sources before editing.


## Resolve evidence scope

Resolve a story directly, sprint membership from the explicitly selected/current sprint, or
system stories through actual references. Without a scope use unambiguous context or ask.
Missing/unreadable/empty scope is explicit; do not report adequate coverage over zero stories.
Read each story's actual Status, criteria, QA cases, declared evidence and applicable obligations.
Use actual test roots. Inspect the declared path first; fallback matches need proven identity,
criterion and revision relevance. Reading existing evidence does not require its template.

## Assess useful evidence

For every criterion inspect what was actually tested: assertion/action, inputs and expected
outcome, result, revision, environment and evaluator. For automated checks examine assertions,
relevant edges, isolation/reproducibility, formula units and links to requirements. Names and
file presence alone do not prove coverage or a run. This review inspects evidence; run further
checks only within the request's authorization and identify that distinct execution.
For manual/human methods examine the protocol, actual observations, sign-offs and required
independence. A screenshot can support visible-state checks but cannot prove interaction,
listening or feel. Missing sign-off or empty protocol remains unavailable. Config/Data and mixed
work retain all applicable relationship, integration, runtime and human checks.

Return a story/criterion table with evidence path, direct coverage, actual execution, relevance,
limitations and **ADEQUATE / INCOMPLETE / MISSING / NOT ASSESSED**. Preserve known failures.
Aggregate only the identified scope; expose missing stories and exclude unrelated newer reports.
An authorized save uses production/qa/evidence-review-[scope]-[date].md with collision checks;
otherwise return the review in conversation. Never mark stories Complete or confer gate approval.
