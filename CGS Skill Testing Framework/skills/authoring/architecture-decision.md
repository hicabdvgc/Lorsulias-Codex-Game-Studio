# Skill Test Spec: $architecture-decision

## Skill Summary

Exercise `.agents/skills/architecture-decision/SKILL.md` and its linked continuation/contract using
isolated project fixtures. Preserve supported invocation modes and inspect the
actual output, saved artifacts, status and downstream usefulness.

## Static Assertions

- SKILL frontmatter has the matching name and useful description; UI metadata parses and its default prompt names `$architecture-decision`.
- References resolve or explicitly identify future/manual inputs.
- Existing task authorization, concurrent edits, missing evidence and required reviews are handled consistently with shared guidance.
- Output locations agree with the workflow catalog and directory guidance.

## Test Cases

### Case 1: Proposal and retrofit

**Scenario:** Author a settled proposal, then retrofit only missing traceability in an existing ADR.

**Expected:** New record stays Proposed; existing valid content/status/history is preserved. No proposed stance becomes active in the registry.

### Case 2: Authorized acceptance

**Scenario:** Explicitly accept one unique Proposed ADR with Accepted transitive dependencies and current required review evidence.

**Expected:** No repeated acceptance prompt. Sets Accepted with authority/date/evidence, synchronizes applicable registry stances and identifies CONTROL/traceability work; no story Ready change.

### Case 3: Dependency failures

**Scenario:** Use unaccepted/missing/ambiguous dependencies, missing or malformed declarations, self-dependency and a cycle.

**Expected:** Prevents acceptance with precise reasons. Explicit None is different from missing. Unrelated cycles do not automatically block this target.

### Case 4: Supersession and rerun

**Scenario:** Authorize replacing an accepted decision, then repeat unchanged acceptance.

**Expected:** Preserves history, replacement identity and affected dependents; rerun reports NO CHANGE without duplicate stance/version updates.

### Case 5: Evidence and authorization boundary

**Scenario:** Request a review/save only, or accept without required independent evidence.

**Expected:** Review/save alone is not acceptance authorization. Missing required evidence stays NOT ASSESSED; no automatic story readiness.

## Evidence and grading

Record the supplied fixture, request, execution method, actual response/files and
observed result for each case. Reading instructions is a static check. A guided
exercise by the current agent is different from native skill invocation, and
neither establishes engine/runtime integration without actual execution. Grade
relevant outcomes using the shared rubric; unavailable required evidence remains
explicit. Rerun affected checks after a demonstrated defect is corrected.
