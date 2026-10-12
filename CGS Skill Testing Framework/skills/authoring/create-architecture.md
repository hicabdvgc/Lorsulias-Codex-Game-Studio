# Skill Test Spec: $create-architecture

## Skill Summary

Exercise `.agents/skills/create-architecture/SKILL.md` and its linked continuation/contract using
isolated project fixtures. Preserve supported invocation modes and inspect the
actual output, saved artifacts, status and downstream usefulness.

## Static Assertions

- SKILL frontmatter has the matching name and useful description; UI metadata parses and its default prompt names `$create-architecture`.
- References resolve or explicitly identify future/manual inputs.
- Existing task authorization, concurrent edits, missing evidence and required reviews are handled consistently with shared guidance.
- Output locations agree with the workflow catalog and directory guidance.

## Test Cases

### Case 1: Master architecture

**Scenario:** Supply full BREAKDOWN, system GDDs, full FRAMEWORK and selected technical choices.

**Expected:** Produces ARCHITECTURE_MASTER with requirement provenance, ownership, interfaces, lifecycle/data flow and framework operations. No forced five layers.

### Case 2: Focused modes

**Scenario:** Exercise layers, data-flow, api-boundaries and adr-audit on the same input.

**Expected:** Each stays within its requested analysis/output scope and distinguishes Proposed from Accepted ADRs.

### Case 3: Missing evidence

**Scenario:** Remove full FRAMEWORK or required engine API evidence.

**Expected:** Identifies incomplete scope and unresolved technical checks; a requested draft does not imply a passing gate or accepted architecture.

## Evidence and grading

Record the supplied fixture, request, execution method, actual response/files and
observed result for each case. Reading instructions is a static check. A guided
exercise by the current agent is different from native skill invocation, and
neither establishes engine/runtime integration without actual execution. Grade
relevant outcomes using the shared rubric; unavailable required evidence remains
explicit. Rerun affected checks after a demonstrated defect is corrected.
