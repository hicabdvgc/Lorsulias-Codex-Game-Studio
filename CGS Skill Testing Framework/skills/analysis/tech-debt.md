# Skill Test Spec: $tech-debt

## Skill Summary

Track, categorize, and prioritize technical debt across the codebase. Scans for debt indicators, maintains a debt register, and recommends repayment scheduling.

## Static assertions

- Package identity and UI metadata parse; registered paths resolve.
- Retained modes and outputs agree with work-preparation.md and actual consumers.
- Governance, stable IDs, authorization, concurrent edits and saved-output checks are preserved.
- Required independent review and human evidence remain required across review depths.

## Test cases

### Case 1: Accepted debt

**Request / fixture:** $tech-debt add with supplied deferral WHY; existing register, duplicate candidate and concurrent TD allocation. Then prioritize.

**Expected outcome:** Deduplicate and reread stable IDs; preserve prose/unknown columns. Use explained ranking, unranked unknowns, no invented effort days.

### Case 2: Candidates and report

**Request / fixture:** $tech-debt scan with TODO/FIXME but no deferral decision; report without history.

**Expected outcome:** Conversational candidates, no register write or resolved/trend claim; missing root/register remains explicit. Reject unknown modes.

## Evidence and grading
Keep fixture inputs, actual generated artifacts/response, method, observed result
and limitations. Written assertions alone are not behavioral evidence. Separate
static inspection, guided current-agent exercise, script execution and native
dispatch/engine/CI/human evaluation. Inspect results against intended outcomes and
repeat affected checks after corrections. Do not invent an unavailable passing run.
