# Skill Test Spec: $scope-check

## Skill Summary

Analyze a feature or sprint for scope creep by comparing current scope against the original plan. Flags additions, quantifies bloat, and recommends cuts. Use when user says 'any scope creep', 'scope review', 'are we staying in scope'.

## Static assertions

- Package identity and UI metadata parse; registered paths resolve.
- Retained modes and outputs agree with work-preparation.md and actual consumers.
- Governance, stable IDs, authorization, concurrent edits and saved-output checks are preserved.
- Required independent review and human evidence remain required across review depths.

## Test cases

### Case 1: Authorized growth

**Request / fixture:** $scope-check sprint-2; baseline plus approved FRAMEWORK addition and separate removal.

**Expected outcome:** Identify authorized change; no automatic creep from addition or net item counts. Read-only verdict with evidence.

### Case 2: Missing historical baseline

**Request / fixture:** Only current GDD available, unmatched feature or incompatible effort values.

**Expected outcome:** Historical creep unproven; NOT ASSESSED where comparison cannot be made; no invented baseline, percentage or cut priority.

## Evidence and grading
Keep fixture inputs, actual generated artifacts/response, method, observed result
and limitations. Written assertions alone are not behavioral evidence. Separate
static inspection, guided current-agent exercise, script execution and native
dispatch/engine/CI/human evaluation. Inspect results against intended outcomes and
repeat affected checks after corrections. Do not invent an unavailable passing run.
