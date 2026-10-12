# Skill Test Spec: $prototype

## Skill Summary

Exercise `.agents/skills/prototype/SKILL.md` and its linked continuation/contract using
isolated project fixtures. Preserve supported invocation modes and inspect the
actual output, saved artifacts, status and downstream usefulness.

## Static Assertions

- SKILL frontmatter has the matching name and useful description; UI metadata parses and its default prompt names `$prototype`.
- References resolve or explicitly identify future/manual inputs.
- Existing task authorization, concurrent edits, missing evidence and required reviews are handled consistently with shared guidance.
- Output locations agree with the workflow catalog and directory guidance.

## Test Cases

### Case 1: Experiment routes

**Scenario:** Use HTML for a timing hypothesis, an explicitly selected engine for a scene question, paper for a rule question and --spike for a technical uncertainty.

**Expected:** Each route scopes its hypothesis, selected duration/checkpoint and evidence method. Report records actual results or not executed, plus retain/adapt/discard reasoning.

### Case 2: Missing runtime or observation

**Scenario:** Request an engine experiment with no editor or a playability conclusion without a human session.

**Expected:** Reports unavailable execution/evidence and useful next work. Does not convert generated code or a predicted outcome into observation.

### Case 3: Reuse and boundaries

**Scenario:** An existing prototype contains useful code and unrelated edits.

**Expected:** Preserves work, explains integration/retention tradeoffs, and verifies promised report/index outputs. No blanket disposal or arbitrary time budget.

## Evidence and grading

Record the supplied fixture, request, execution method, actual response/files and
observed result for each case. Reading instructions is a static check. A guided
exercise by the current agent is different from native skill invocation, and
neither establishes engine/runtime integration without actual execution. Grade
relevant outcomes using the shared rubric; unavailable required evidence remains
explicit. Rerun affected checks after a demonstrated defect is corrected.
