# Skill Test Spec: $asset-spec

## Skill Summary

Exercise `.agents/skills/asset-spec/SKILL.md` and its listed continuation with isolated fixtures.
Retain useful source interfaces while testing the adapted resource and evidence contracts.

## Static assertions

- Frontmatter name/description and UI metadata parse and match the installed identity.
- Retained references resolve or explicitly identify future/manual inputs.
- Output paths, modes and statuses agree with actual consumers and templates.
- Preserve bounded authorization, concurrent edits, required independent review and human evidence.

## Test cases

### Case 1: Explicit direction

**Request / fixture:** Use $asset-spec entity:lantern with a developer brief, selected icon TYPE_TEMP and no art bible.

**Expected outcome:** Write the target-level spec and manifest under design/assets using the explicit direction, type/system mapping and stable asset ID; no media-delivery claim.

### Case 2: Inventory and selectors

**Request / fixture:** Exercise no-argument inventory creation and system/level/character/entity selection; include an ambiguous or unsafe target.

**Expected outcome:** Inventory branch ends without empty-target generation; valid selectors resolve their source; unsafe/ambiguous input cannot write.

### Case 3: Rerun and concurrent allocation

**Request / fixture:** Reuse ASSET-001 for a shared icon while another writer adds ASSET-002 before save.

**Expected outcome:** Re-read and preserve both IDs, allocate a new ID only if needed, avoid duplicate context blocks and retain concurrent content.

### Case 4: Missing production evidence

**Request / fixture:** Source is Draft and format/import requirements are unresolved; use full/lean/solo.

**Expected outcome:** A labeled exploratory spec may be saved, but missing acceptance/technical/independent evidence prevents production-ready status in every mode.

## Evidence and grading

Record raw fixture inputs, request, actual response/artifacts, method and observed
result. Static reading, guided current-agent exercises, script execution and native
runtime dispatch are separate evidence. A fixture or expected answer alone is not
execution. Inspect useful output and failed prerequisites; rerun affected cases after
correction. Apply the shared rubric without arbitrary section or step counts.

## Regression assertion

Absent --review uses focused review without a review-mode file. Existing authorization to create the inventory carries through the save.
