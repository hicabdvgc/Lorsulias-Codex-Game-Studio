# Skill Test Spec: $brainstorm

## Skill Summary

Exercise `.agents/skills/brainstorm/SKILL.md` and its linked continuation/contract using
isolated project fixtures. Preserve supported invocation modes and inspect the
actual output, saved artifacts, status and downstream usefulness.

## Static Assertions

- SKILL frontmatter has the matching name and useful description; UI metadata parses and its default prompt names `$brainstorm`.
- References resolve or explicitly identify future/manual inputs.
- Existing task authorization, concurrent edits, missing evidence and required reviews are handled consistently with shared guidance.
- Output locations agree with the workflow catalog and directory guidance.

## Test Cases

### Case 1: Exploration and concept boundary

**Scenario:** Ask for two ways to build a game about repairing a shared machine, with a short-session constraint.

**Expected:** Useful core verbs, loops, tradeoffs and open developer choices; research/ref-study guidance is connected. CONCEPT is neither created nor replaced; there is no mandatory prototype.

### Case 2: Research evidence

**Scenario:** Supply a sourced article and no human play record.

**Expected:** Record it as sourced research with provenance. Human observation remains missing; no fabricated play session, MDA conclusion or genre fact.

### Case 3: Modes

**Scenario:** Exercise an idea, core-verb, mashup and experience-first request using the forms supported in SKILL.md.

**Expected:** Each exploration uses the supplied intent, preserves authorship and ends with a useful decision/handoff.

## Evidence and grading

Record the supplied fixture, request, execution method, actual response/files and
observed result for each case. Reading instructions is a static check. A guided
exercise by the current agent is different from native skill invocation, and
neither establishes engine/runtime integration without actual execution. Grade
relevant outcomes using the shared rubric; unavailable required evidence remains
explicit. Rerun affected checks after a demonstrated defect is corrected.
