# Skill Test Spec: $reverse-document

## Skill Summary

Exercise `.agents/skills/reverse-document/SKILL.md` and its linked continuation/contract using
isolated project fixtures. Preserve supported invocation modes and inspect the
actual output, saved artifacts, status and downstream usefulness.

## Static Assertions

- SKILL frontmatter has the matching name and useful description; UI metadata parses and its default prompt names `$reverse-document`.
- References resolve or explicitly identify future/manual inputs.
- Existing task authorization, concurrent edits, missing evidence and required reviews are handled consistently with shared guidance.
- Output locations agree with the workflow catalog and directory guidance.

## Test Cases

### Case 1: Three recovery modes

**Scenario:** Recover design, architecture and concept separately from a supplied small implementation/prototype.

**Expected:** Uses each matching template; records actual files/behaviors, inferred intent, uncertainty and retention decisions. Concept observations remain separate from CONCEPT; recovered ADRs are Proposed.

### Case 2: Missing source

**Scenario:** A requested source path is absent or a binary asset cannot be inspected.

**Expected:** Identifies the missing evidence and affected conclusions; does not invent code behavior or claim execution.

### Case 3: Existing authoritative design

**Scenario:** Recovery conflicts with a developer-authored design.

**Expected:** Reports divergence without replacing accepted intent. Saves only authorized recovered artifacts and checks their contents.

## Evidence and grading

Record the supplied fixture, request, execution method, actual response/files and
observed result for each case. Reading instructions is a static check. A guided
exercise by the current agent is different from native skill invocation, and
neither establishes engine/runtime integration without actual execution. Grade
relevant outcomes using the shared rubric; unavailable required evidence remains
explicit. Rerun affected checks after a demonstrated defect is corrected.
