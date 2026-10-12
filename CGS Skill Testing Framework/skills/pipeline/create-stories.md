# Skill Test Spec: $create-stories

## Skill Summary

Decompose an epic into bounded stories with genuine prerequisites, applicable governance and criterion-level evidence.

## Static assertions

- Package identity and UI metadata parse; registered paths resolve.
- Retained modes and outputs agree with work-preparation.md and actual consumers.
- Governance, stable IDs, authorization, concurrent edits and saved-output checks are preserved.
- Required independent review and human evidence remain required across review depths.

## Test cases

### Case 1: Mixed work

**Request / fixture:** $create-stories named epic; outcomes include code, resource preparation, converter tool and integration; created outputs absent but actual TYPE_TEMP/input sources supplied.

**Expected outcome:** Separate inputs/outputs, criterion methods and applicable governance. Save story-NNN files and tables; absent future outputs do not block creation.

### Case 2: Real blockers

**Request / fixture:** Proposed ADR, missing actual input, missing required independent review or missing applicable CONTROL/TR; compare justified N/A for a nontechnical story.

**Expected outcome:** Save only non-ready draft for blockers; N/A is valid only when justified. No fake TR IDs or automatic Ready.

### Case 3: QA and concurrency

**Request / fixture:** Relevant older QA plan and newer unrelated plan; another writer takes story-003; an existing story is In Progress.

**Expected outcome:** Reuse matching criteria/revision, allocate next unused number after reread, preserve progress and unrelated notes. Verify all saved files.

## Evidence and grading
Keep fixture inputs, actual generated artifacts/response, method, observed result
and limitations. Written assertions alone are not behavioral evidence. Separate
static inspection, guided current-agent exercise, script execution and native
dispatch/engine/CI/human evaluation. Inspect results against intended outcomes and
repeat affected checks after corrections. Do not invent an unavailable passing run.

## Regression assertion

Review depth is an explicit valid flag or focused default; no review-mode file is read or created.
