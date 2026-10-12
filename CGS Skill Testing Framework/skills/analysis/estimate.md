# Skill Test Spec: $estimate

## Skill Summary

Estimates task effort by analyzing complexity, dependencies, historical velocity, and risk factors. Produces a structured estimate with confidence levels.

## Static assertions

- Package identity and UI metadata parse; registered paths resolve.
- Retained modes and outputs agree with work-preparation.md and actual consumers.
- Governance, stable IDs, authorization, concurrent edits and saved-output checks are preserved.
- Required independent review and human evidence remain required across review depths.

## Test cases

### Case 1: Task and sprint

**Request / fixture:** $estimate qualified story then sprint with two analogous tasks in hours and a task in points; supplied uncertainty basis.

**Expected outcome:** Trace effort to basis, maintain Optimistic <= Expected <= Pessimistic, aggregate only comparable units; include review/resource/tool/human work.

### Case 2: Unknown basis

**Request / fixture:** No history, capacity or executor estimate; missing path and vague natural-language variants.

**Expected outcome:** No fallback day range, unknown estimates explicit, path error or necessary clarification; read-only.

## Evidence and grading
Keep fixture inputs, actual generated artifacts/response, method, observed result
and limitations. Written assertions alone are not behavioral evidence. Separate
static inspection, guided current-agent exercise, script execution and native
dispatch/engine/CI/human evaluation. Inspect results against intended outcomes and
repeat affected checks after corrections. Do not invent an unavailable passing run.
