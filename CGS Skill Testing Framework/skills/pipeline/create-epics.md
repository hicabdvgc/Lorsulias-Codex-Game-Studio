# Skill Test Spec: $create-epics

## Skill Summary

Group design, framework, resource and tool outcomes into traceable epics; preserve existing stories and indexes.

## Static assertions

- Package identity and UI metadata parse; registered paths resolve.
- Retained modes and outputs agree with work-preparation.md and actual consumers.
- Governance, stable IDs, authorization, concurrent edits and saved-output checks are preserved.
- Required independent review and human evidence remain required across review depths.

## Test cases

### Case 1: Connected outcomes

**Request / fixture:** $create-epics all; supplied two connected systems, full FRAMEWORK, resource/tool work, accepted scoped governance and slice observations; no MILESTONE.

**Expected outcome:** Save coherent epics/index without one-per-module or layer order; preserve existing story tables. Missing MILESTONE does not block preparation.

### Case 2: Missing scope/governance

**Request / fixture:** Named system missing from BREAKDOWN or a governing ADR still Proposed; layer selector absent from project; required PR-EPIC assessment unavailable.

**Expected outcome:** Clarify ambiguous scope; missing governing inputs/review cannot yield Ready. Useful bounded drafts identify gaps. No implementation.

### Case 3: Concurrent authoring

**Request / fixture:** Existing epic with stories; another writer adds an index row before save; exercise named/all/layer and review-depth options.

**Expected outcome:** Re-read and merge by stable identity; preserve unrelated rows and required reviews in every depth.

## Evidence and grading
Keep fixture inputs, actual generated artifacts/response, method, observed result
and limitations. Written assertions alone are not behavioral evidence. Separate
static inspection, guided current-agent exercise, script execution and native
dispatch/engine/CI/human evaluation. Inspect results against intended outcomes and
repeat affected checks after corrections. Do not invent an unavailable passing run.

## Regression assertion

Review depth is an explicit valid flag or focused default; no review-mode file is read or created.
