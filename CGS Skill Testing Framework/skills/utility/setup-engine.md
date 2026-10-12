# Skill Test Spec: $setup-engine

## Skill Summary

Exercise `.agents/skills/setup-engine/SKILL.md` and its linked continuation/contract using
isolated project fixtures. Preserve supported invocation modes and inspect the
actual output, saved artifacts, status and downstream usefulness.

## Static Assertions

- SKILL frontmatter has the matching name and useful description; UI metadata parses and its default prompt names `$setup-engine`.
- References resolve or explicitly identify future/manual inputs.
- Existing task authorization, concurrent edits, missing evidence and required reviews are handled consistently with shared guidance.
- Output locations agree with the workflow catalog and directory guidance.

## Test Cases

### Case 1: Select each family

**Scenario:** Explicitly select Godot, Unity or Unreal in separate fixtures, while language, target and packages remain undecided.

**Expected:** Routes to that family, records only selected choices in live preferences, reads official evidence and leaves remaining choices unconfigured. No engine install.

After an explicit selection, read the selected engine's VERSION reference alongside
live preferences. The reference must describe library coverage and point to the
live project choice without retaining a conflicting literal project value such as
"Unconfigured". Changing the project choice must not require maintaining a second pin.

### Case 2: Guided and mismatch

**Scenario:** Ask for engine selection without requirements; then supply a project version different from the library.

**Expected:** Explains necessary tradeoffs, asks for consequential missing choices and checks version-specific evidence. It does not silently adopt the library version.

### Case 3: Refresh and upgrade

**Scenario:** Request refresh, then an upgrade assessment for an existing project.

**Expected:** Refresh changes documentation only. Upgrade identifies changed APIs/data/packages, required verification and recoverable migration steps without claiming execution.

### Case 4: Evidence unavailable

**Scenario:** Official API or package compatibility evidence cannot be retrieved.

**Expected:** Affected technical check stays NOT ASSESSED; no inherited verification date or model-cutoff classification supplies a pass.

## Evidence and grading

Record the supplied fixture, request, execution method, actual response/files and
observed result for each case. Reading instructions is a static check. A guided
exercise by the current agent is different from native skill invocation, and
neither establishes engine/runtime integration without actual execution. Grade
relevant outcomes using the shared rubric; unavailable required evidence remains
explicit. Rerun affected checks after a demonstrated defect is corrected.
