# Skill Test Spec: $define-milestones

## Skill Summary

Author or update project-defined MVP, Alpha, Beta and Gold expectations, playtest questions and progression criteria.

## Static assertions

- Package identity and UI metadata parse; registered paths resolve.
- Retained modes and outputs agree with work-preparation.md and actual consumers.
- Governance, stable IDs, authorization, concurrent edits and saved-output checks are preserved.
- Required independent review and human evidence remain required across review depths.

## Test cases

### Case 1: Four selected stages

**Request / fixture:** $define-milestones using supplied MVP/Alpha/Beta/Gold outcomes and actual passed slice-gate findings; prepared work available; dates/capacity absent.

**Expected outcome:** Write authoritative MILESTONE with completeness/learning/evaluation/progression per stage, schedules unset, no forced sprints or achievement claim.

### Case 2: Draft/update

**Request / fixture:** Update Beta only; supplied criteria but slice gate unperformed for initial draft variant.

**Expected outcome:** Preserve other stages/decisions; incomplete draft labels missing gate evidence and affected epics/QA/sprint work; cannot settle progression.

## Evidence and grading
Keep fixture inputs, actual generated artifacts/response, method, observed result
and limitations. Written assertions alone are not behavioral evidence. Separate
static inspection, guided current-agent exercise, script execution and native
dispatch/engine/CI/human evaluation. Inspect results against intended outcomes and
repeat affected checks after corrections. Do not invent an unavailable passing run.
