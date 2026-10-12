# Skill Test Spec: $test-helpers

## Skill Summary

Create runner-compatible test fixtures, assertions and builders from actual system interfaces, or scaffold a selected helper structure.

## Static assertions

- Package identity and UI metadata parse; registered paths resolve.
- Retained modes and outputs agree with work-preparation.md and actual consumers.
- Governance, stable IDs, authorization, concurrent edits and saved-output checks are preserved.
- Required independent review and human evidence remain required across review depths.

## Test cases

### Case 1: Real consumer

**Request / fixture:** $test-helpers named system with real interfaces and selected runner; exercise all and scaffold.

**Expected outcome:** Helpers follow actual lifecycle/cleanup and root, meaningful consumer and usage; selected APIs verified.

### Case 2: Missing factory

**Request / fixture:** No CreateDefault or real constructor/assembly contract; runner absent; mixed resource/tool scope.

**Expected outcome:** No invented factory/API or fake-world wrapper; affected helpers remain blocked, human evaluation planned separately.

## Evidence and grading
Keep fixture inputs, actual generated artifacts/response, method, observed result
and limitations. Written assertions alone are not behavioral evidence. Separate
static inspection, guided current-agent exercise, script execution and native
dispatch/engine/CI/human evaluation. Inspect results against intended outcomes and
repeat affected checks after corrections. Do not invent an unavailable passing run.
