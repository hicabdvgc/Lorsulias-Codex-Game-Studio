# Skill Test Spec: $design-review

## Skill Summary

Exercise `.agents/skills/design-review/SKILL.md` and its linked continuation/contract using
isolated project fixtures. Preserve supported invocation modes and inspect the
actual output, saved artifacts, status and downstream usefulness.

## Static Assertions

- SKILL frontmatter has the matching name and useful description; UI metadata parses and its default prompt names `$design-review`.
- References resolve or explicitly identify future/manual inputs.
- Existing task authorization, concurrent edits, missing evidence and required reviews are handled consistently with shared guidance.
- Output locations agree with the workflow catalog and directory guidance.

## Test Cases

### Case 1: Initial scope

**Scenario:** Review a GDD with BREAKDOWN/preliminary FRAMEWORK and resource needs only.

**Expected:** Checks relevant rules, boundaries and feasible evaluation without demanding future resource schemas. Conversational result, no file writes by default.

### Case 2: Integration scopes

**Scenario:** Review framework, resource and combined scopes with actual supplied contracts; then remove one required contract.

**Expected:** Finds the specific mismatch and blocks only the affected conclusion; missing resource evidence prevents a resource-integration pass.

### Case 3: Observation helper and human evidence

**Scenario:** Supply all headings but incomplete behavior, and no human assessment for a player-feel claim.

**Expected:** Heading presence is an observation, not completeness. Human-dependent conclusions remain NOT ASSESSED and review depth cannot waive them.

## Evidence and grading

Record the supplied fixture, request, execution method, actual response/files and
observed result for each case. Reading instructions is a static check. A guided
exercise by the current agent is different from native skill invocation, and
neither establishes engine/runtime integration without actual execution. Grade
relevant outcomes using the shared rubric; unavailable required evidence remains
explicit. Rerun affected checks after a demonstrated defect is corrected.

## Regression assertion

Default review is conversational. An explicit bounded report-save request writes and verifies that report without editing GDD status or creating automatic receipts.
