# Skill Test Spec: $retrospective

## Skill Summary

Generates a sprint or milestone retrospective by analyzing completed work, velocity, blockers, and patterns. Produces actionable insights for the next iteration.

## Static assertions

- Package identity and UI metadata parse; registered paths resolve.
- Retained modes and outputs agree with work-preparation.md and actual consumers.
- Governance, stable IDs, authorization, concurrent edits and saved-output checks are preserved.
- Required independent review and human evidence remain required across review depths.

## Test cases

### Case 1: Observed period

**Request / fixture:** $retrospective sprint-2; matching plan/period record, measured effort and supplied reflection; existing output update authorized.

**Expected outcome:** Save scoped update, cite comparable observations and label causal interpretations, preserve prior records and agreed actions.

### Case 2: Unsupported history

**Request / fixture:** No actual effort or period status, current unrelated YAML, no owner/deadline; milestone goals provided.

**Expected outcome:** Unknown metrics/causes/commitments remain explicit. Today’s status cannot establish historical completion; no manufactured trend.

### Case 3: Existing output choices

**Request / fixture:** Several matching records or explicit new record, no archive request.

**Expected outcome:** Clarify ambiguous target; preserve records, no unsolicited archive and no repeated permission for authorized update.

## Evidence and grading
Keep fixture inputs, actual generated artifacts/response, method, observed result
and limitations. Written assertions alone are not behavioral evidence. Separate
static inspection, guided current-agent exercise, script execution and native
dispatch/engine/CI/human evaluation. Inspect results against intended outcomes and
repeat affected checks after corrections. Do not invent an unavailable passing run.
