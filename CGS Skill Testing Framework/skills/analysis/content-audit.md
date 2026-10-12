# Skill Test Spec: $content-audit

## Skill Summary

Exercise `.agents/skills/content-audit/SKILL.md` and its listed continuation with isolated fixtures.
Retain useful source interfaces while testing the adapted resource and evidence contracts.

## Static assertions

- Frontmatter name/description and UI metadata parse and match the installed identity.
- Retained references resolve or explicitly identify future/manual inputs.
- Output paths, modes and statuses agree with actual consumers and templates.
- Preserve bounded authorization, concurrent edits, required independent review and human evidence.

## Test cases

### Case 1: Identity coverage

**Request / fixture:** GDD requires lantern and key; inventory has lantern, lantern import duplicate and coin.

**Expected outcome:** Report key missing, deduplicate lantern and avoid passing from equal file counts; save nothing by default.

### Case 2: Format and usability

**Request / fixture:** Both identities exist but key has the wrong selected format and no build evidence.

**Expected outcome:** Separate format issue from existence and unassessed runtime usability. Preserve explicitly critical versus ordinary gap verdicts.

### Case 3: Modes and unknowns

**Request / fixture:** Use named system, full and --summary; include ambiguous system, no numeric baseline, and zero count.

**Expected outcome:** Respect scope, exclude unspecified rows from totals, avoid division by zero and invented scheduling thresholds; unavailable required evidence prevents COMPLETE.

## Evidence and grading

Record raw fixture inputs, request, actual response/artifacts, method and observed
result. Static reading, guided current-agent exercises, script execution and native
runtime dispatch are separate evidence. A fixture or expected answer alone is not
execution. Inspect useful output and failed prerequisites; rerun affected cases after
correction. Apply the shared rubric without arbitrary section or step counts.

## Regression assertion

Delegation follows current authorization. An already-authorized scoped report save proceeds without repeated approval and preserves a conflicting report.
