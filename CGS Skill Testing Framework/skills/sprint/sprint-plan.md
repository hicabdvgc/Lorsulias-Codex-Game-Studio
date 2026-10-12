# Skill Test Spec: $sprint-plan

## Skill Summary

Create, update or inspect optional sprint subdivisions of defined milestones using real capacity, dependencies and story-owned status.

## Static assertions

- Package identity and UI metadata parse; registered paths resolve.
- Retained modes and outputs agree with work-preparation.md and actual consumers.
- Governance, stable IDs, authorization, concurrent edits and saved-output checks are preserved.
- Required independent review and human evidence remain required across review depths.

## Test cases

### Case 1: First sprint

**Request / fixture:** $sprint-plan new; defined milestone and goal, no history/capacity; must-have Not Started story plus dependency order.

**Expected outcome:** Useful incomplete feasibility draft, unknown capacity, no fixed buffer or priority-to-Ready promotion.

### Case 2: Derived synchronization

**Request / fixture:** $sprint-plan update; YAML ready disagrees with In Progress story; explicit carryover and concurrent membership addition.

**Expected outcome:** Report conflict and derive in_progress; preserve story, new membership and custom fields; no silent reset/removal.

### Case 3: Read-only status

**Request / fixture:** $sprint-plan status; exact sprint selected with missing member; also exercise missing milestone and ambiguous active sprint.

**Expected outcome:** Read-only summary with gap; no next task/readiness claim. Unknown milestone/scope blocks dependent finalized planning.

## Evidence and grading
Keep fixture inputs, actual generated artifacts/response, method, observed result
and limitations. Written assertions alone are not behavioral evidence. Separate
static inspection, guided current-agent exercise, script execution and native
dispatch/engine/CI/human evaluation. Inspect results against intended outcomes and
repeat affected checks after corrections. Do not invent an unavailable passing run.

## Regression assertion

Review depth is an explicit valid flag or focused default; no review-mode file is read or created.
