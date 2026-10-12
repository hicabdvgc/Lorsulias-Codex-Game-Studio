# Skill Test Spec: $design-system

## Skill Summary

Exercise `.agents/skills/design-system/SKILL.md` and its linked continuation/contract using
isolated project fixtures. Preserve supported invocation modes and inspect the
actual output, saved artifacts, status and downstream usefulness.

## Static Assertions

- SKILL frontmatter has the matching name and useful description; UI metadata parses and its default prompt names `$design-system`.
- References resolve or explicitly identify future/manual inputs.
- Existing task authorization, concurrent edits, missing evidence and required reviews are handled consistently with shared guidance.
- Output locations agree with the workflow catalog and directory guidance.

## Test Cases

### Case 1: Initial authoring

**Scenario:** Supply full BREAKDOWN and preliminary FRAMEWORK for inventory, with no resource schemas.

**Expected:** Produces an identifiable GDD with behavioral rules, integration ownership, resource requirements and feasible evaluation; initial design is not blocked by future schemas. The workflow integration handoff and skill must resolve the same installed `design/registry/entities.yaml` file; registered shared facts retain their owning GDD and actual consumers.

### Case 2: Retrofit and extension

**Scenario:** Request a formula-only retrofit to existing content, then a capacity extension affecting inventory and crafting.

**Expected:** Preserves other sections, checks shared-fact ownership, traces addition/modification effects and records affected consumers within scope.

### Case 3: Missing prerequisite and conflict

**Scenario:** Remove full BREAKDOWN or give conflicting inventory/crafting capacity assumptions.

**Expected:** Names the missing input or conflict, leaves affected completeness unassessed, and obtains unresolved consequential decisions rather than choosing them silently.

### Case 4: Review continuity

**Scenario:** Use lean/solo while independent CD-GDD-ALIGN evidence is required but absent.

**Expected:** Discloses self-review and missing required review; no Approved status inferred. Verify saved GDD and authorized BREAKDOWN/registry updates.

## Evidence and grading

Record the supplied fixture, request, execution method, actual response/files and
observed result for each case. Reading instructions is a static check. A guided
exercise by the current agent is different from native skill invocation, and
neither establishes engine/runtime integration without actual execution. Grade
relevant outcomes using the shared rubric; unavailable required evidence remains
explicit. Rerun affected checks after a demonstrated defect is corrected.
