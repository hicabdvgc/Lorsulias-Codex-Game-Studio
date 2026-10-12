# Skill Test Spec: $consistency-check

## Skill Summary

Exercise `.agents/skills/consistency-check/SKILL.md` and its listed continuation with isolated fixtures.
Retain useful source interfaces while testing the adapted resource and evidence contracts.

## Static assertions

- Frontmatter name/description and UI metadata parse and match the installed identity.
- Retained references resolve or explicitly identify future/manual inputs.
- Output paths, modes and statuses agree with actual consumers and templates.
- Preserve bounded authorization, concurrent edits, required independent review and human evidence.

## Test cases

### Case 1: Consistent rewording

**Request / fixture:** Two GDDs share quantity rules with renamed equivalent variables and identical units.

**Expected outcome:** Compare semantics, preserve IDs and return CONSISTENT for the evidenced scope; no false conflict from variable spelling.

### Case 2: Conflict and missing registry

**Request / fixture:** Owning GDD says capacity 4, consumer says 5; registry missing or stale.

**Expected outcome:** Cite both current rules and distinguish conflict, stale record and missing coverage; no automatic winner or registry write.

### Case 3: Modes

**Request / fixture:** Exercise entity/item selectors, malformed/duplicate YAML, missing dependency and since-last-review without an anchored baseline.

**Expected outcome:** Selectors need resolvable records, full document comparisons can continue without registry, dependency gap is named and incremental falls back explicitly to full.

## Evidence and grading

Record raw fixture inputs, request, actual response/artifacts, method and observed
result. Static reading, guided current-agent exercises, script execution and native
runtime dispatch are separate evidence. A fixture or expected answer alone is not
execution. Inspect useful output and failed prerequisites; rerun affected cases after
correction. Apply the shared rubric without arbitrary section or step counts.

## Regression assertion

A supplied reviewed before/after snapshot is a valid incremental baseline without Git. An already-authorized report save proceeds without a repeated approval; a different existing assessment is preserved.
