# Skill Test Spec: $map-systems

## Skill Summary

Exercise `.agents/skills/map-systems/SKILL.md` and its linked continuation/contract using
isolated project fixtures. Preserve supported invocation modes and inspect the
actual output, saved artifacts, status and downstream usefulness.

## Static Assertions

- SKILL frontmatter has the matching name and useful description; UI metadata parses and its default prompt names `$map-systems`.
- References resolve or explicitly identify future/manual inputs.
- Existing task authorization, concurrent edits, missing evidence and required reviews are handled consistently with shared guidance.
- Output locations agree with the workflow catalog and directory guidance.

## Test Cases

### Case 1: Preliminary mapping

**Scenario:** Supply manual CONCEPT, research/MDA and known engine findings with no FRAMEWORK.

**Expected:** Creates preliminary BREAKDOWN with system identities, boundaries, dependencies and open questions. No invented layer hierarchy or milestone priority.

### Case 2: Full mapping

**Scenario:** Supply developed framework principles and request full BREAKDOWN.

**Expected:** Refines boundaries/integration, preserves stable identities and links, and records maturity. Missing principles leave full maturity incomplete.

### Case 3: Handoffs

**Scenario:** Exercise next and a named system with full BREAKDOWN/preliminary FRAMEWORK, then remove those prerequisites.

**Expected:** Resolves an eligible/unique system and hands off to design-system; missing prerequisites identify affected work. Neither handoff accidentally rebuilds the entire map.

## Evidence and grading

Record the supplied fixture, request, execution method, actual response/files and
observed result for each case. Reading instructions is a static check. A guided
exercise by the current agent is different from native skill invocation, and
neither establishes engine/runtime integration without actual execution. Grade
relevant outcomes using the shared rubric; unavailable required evidence remains
explicit. Rerun affected checks after a demonstrated defect is corrected.
