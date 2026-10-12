# Skill Test Spec: $story-readiness

## Skill Summary

Review whether a story has usable pickup inputs and feasible completion evidence without changing work status.

## Static assertions

- Package identity and UI metadata parse; registered paths resolve.
- Retained modes and outputs agree with work-preparation.md and actual consumers.
- Governance, stable IDs, authorization, concurrent edits and saved-output checks are preserved.
- Required independent review and human evidence remain required across review depths.

## Test cases

### Case 1: Human protocol

**Request / fixture:** $story-readiness path with explicit setup, intended-user task, observation questions, comparison criteria, evaluator and input dependencies; future output absent.

**Expected outcome:** Assess feasible protocol without demanding future execution evidence; retain actual required readiness review. No status writes.

### Case 2: Evidence path alone

**Request / fixture:** Criterion says feels good and only links evidence.md; required independent assessment missing; governing ADR Proposed.

**Expected outcome:** NEEDS WORK/BLOCKED with independent check NOT ASSESSED; never READY or silently mark status.

### Case 3: Scope/dependency/governance

**Request / fixture:** all or sprint with missing/read-error scope, self/cyclic/incomplete dependency, inactive TR or changed CONTROL revision.

**Expected outcome:** Report each unavailable/failed check, preserve missing scope in aggregate; affected rules require review rather than restamping.

## Evidence and grading
Keep fixture inputs, actual generated artifacts/response, method, observed result
and limitations. Written assertions alone are not behavioral evidence. Separate
static inspection, guided current-agent exercise, script execution and native
dispatch/engine/CI/human evaluation. Inspect results against intended outcomes and
repeat affected checks after corrections. Do not invent an unavailable passing run.

## Regression assertion

Review depth is an explicit valid flag or focused default; no review-mode file is read or created.
