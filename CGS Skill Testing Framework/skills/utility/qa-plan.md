# Skill Test Spec: $qa-plan

## Skill Summary

Author scoped QA plans linking every applicable acceptance criterion to feasible automated, inspection, manual, engine and human evidence.

## Static assertions

- Package identity and UI metadata parse; registered paths resolve.
- Retained modes and outputs agree with work-preparation.md and actual consumers.
- Governance, stable IDs, authorization, concurrent edits and saved-output checks are preserved.
- Required independent review and human evidence remain required across review depths.

## Test cases

### Case 1: Mixed criterion methods

**Request / fixture:** $qa-plan story:path includes numerical formula, resource reference, tool end-to-end and human usability criteria. Exercise feature/epic/exact and active sprint selection.

**Expected outcome:** Saved output identifies exact scope and every criterion/method/evaluator/revision/destination; required methods not reduced by type.

### Case 2: Missing scope/evidence

**Request / fixture:** Sprint references one missing story and one valid one; no runner or intended-user evaluation, ambiguous feature and empty scope variants.

**Expected outcome:** Partial coverage retains missing count; empty/ambiguous scope prevents misleading output. Plan never claims checks ran; no status writes.

## Evidence and grading
Keep fixture inputs, actual generated artifacts/response, method, observed result
and limitations. Written assertions alone are not behavioral evidence. Separate
static inspection, guided current-agent exercise, script execution and native
dispatch/engine/CI/human evaluation. Inspect results against intended outcomes and
repeat affected checks after corrections. Do not invent an unavailable passing run.
