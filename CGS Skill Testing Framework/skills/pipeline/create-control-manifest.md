# Skill Test Spec: $create-control-manifest

## Skill Summary

Exercise `.agents/skills/create-control-manifest/SKILL.md` and its linked continuation/contract using
isolated project fixtures. Preserve supported invocation modes and inspect the
actual output, saved artifacts, status and downstream usefulness.

## Static Assertions

- SKILL frontmatter has the matching name and useful description; UI metadata parses and its default prompt names `$create-control-manifest`.
- References resolve or explicitly identify future/manual inputs.
- Existing task authorization, concurrent edits, missing evidence and required reviews are handled consistently with shared guidance.
- Output locations agree with the workflow catalog and directory guidance.

## Test Cases

### Case 1: Accepted obligations

**Scenario:** Supply Accepted and Proposed ADRs, explicit project obligations and an accepted recommendation.

**Expected:** Derives scoped rules only from governing sources; preserves source identity and obligation strength. Proposed candidates are excluded; recommendation is not promoted to Required.

### Case 2: Idempotence and change

**Scenario:** Create initial manifest, rerun unchanged, then change one accepted governing rule.

**Expected:** Initial integer revision is 1. Unchanged content keeps revision and file stable. Governing change increments once and preserves rule provenance/IDs.

### Case 3: Missing or conflicting sources

**Scenario:** Accepted source is missing, contradictory or superseded without a settled replacement.

**Expected:** Reports INCOMPLETE/affected rules without fabricating accepted authority. Existing valid content and concurrent changes are preserved.

## Evidence and grading

Record the supplied fixture, request, execution method, actual response/files and
observed result for each case. Reading instructions is a static check. A guided
exercise by the current agent is different from native skill invocation, and
neither establishes engine/runtime integration without actual execution. Grade
relevant outcomes using the shared rubric; unavailable required evidence remains
explicit. Rerun affected checks after a demonstrated defect is corrected.
