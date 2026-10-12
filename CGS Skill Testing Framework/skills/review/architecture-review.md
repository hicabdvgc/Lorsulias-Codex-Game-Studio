# Skill Test Spec: $architecture-review

## Skill Summary

Exercise `.agents/skills/architecture-review/SKILL.md` and its linked continuation/contract using
isolated project fixtures. Preserve supported invocation modes and inspect the
actual output, saved artifacts, status and downstream usefulness.

## Static Assertions

- SKILL frontmatter has the matching name and useful description; UI metadata parses and its default prompt names `$architecture-review`.
- References resolve or explicitly identify future/manual inputs.
- Existing task authorization, concurrent edits, missing evidence and required reviews are handled consistently with shared guidance.
- Output locations agree with the workflow catalog and directory guidance.

## Test Cases

### Case 1: Six modes

**Scenario:** Exercise the six invocation modes listed in SKILL.md against a consistent design/architecture fixture.

**Expected:** Each retains its scope, examines applicable evidence and distinguishes draft coverage from accepted governing coverage.

### Case 2: Save boundaries

**Scenario:** Review with no save request, then explicitly request traceability and RTM outputs.

**Expected:** Default performs no writes. Authorized saves are bounded and read back; saving is not approval. New unsaved TR IDs are provisional.

### Case 3: Registry continuity

**Scenario:** Reword a requirement, split another, retire one and introduce a concurrent next-ID allocation.

**Expected:** Preserves original identity for rewording, records replacement/retirement, rereads registry and allocates no duplicate IDs. Durable downstream IDs have saved entries.

### Case 4: Missing evidence

**Scenario:** Remove required independent review, relevant engine evidence or FRAMEWORK coverage.

**Expected:** Affected conclusion is NOT ASSESSED; optional depth cannot waive the missing work. Persisted receipts and automatic skipping are not introduced.

## Evidence and grading

Record the supplied fixture, request, execution method, actual response/files and
observed result for each case. Reading instructions is a static check. A guided
exercise by the current agent is different from native skill invocation, and
neither establishes engine/runtime integration without actual execution. Grade
relevant outcomes using the shared rubric; unavailable required evidence remains
explicit. Rerun affected checks after a demonstrated defect is corrected.
