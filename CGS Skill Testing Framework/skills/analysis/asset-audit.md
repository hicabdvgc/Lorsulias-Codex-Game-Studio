# Skill Test Spec: $asset-audit

## Skill Summary

Exercise `.agents/skills/asset-audit/SKILL.md` and its listed continuation with isolated fixtures.
Retain useful source interfaces while testing the adapted resource and evidence contracts.

## Static assertions

- Frontmatter name/description and UI metadata parse and match the installed identity.
- Retained references resolve or explicitly identify future/manual inputs.
- Output paths, modes and statuses agree with actual consumers and templates.
- Preserve bounded authorization, concurrent edits, required independent review and human evidence.

## Test cases

### Case 1: Mapped data

**Request / fixture:** Audit two declared JSON resources in res_lib/ with specified format/reference rules.

**Expected outcome:** Produce file/check/expected/actual evidence and the existing COMPLIANT/WARNINGS/NON-COMPLIANT vocabulary, scoped to checks actually performed.

### Case 2: Unassessed media

**Request / fixture:** Audit a media file with no readable dimensions or selected naming rule.

**Expected outcome:** NOT CHECKED findings prevent COMPLIANT; no fabricated default naming, format, power-of-two or budget rule.

### Case 3: Reference and scope

**Request / fixture:** Try all/category/invalid selectors, absent directories and dynamically referenced assets.

**Expected outcome:** Reject unknown selector; identify empty/absent scope; NO REFERENCE FOUND never authorizes deletion; distinguish unresolved references from confirmed missing targets.

## Evidence and grading

Record raw fixture inputs, request, actual response/artifacts, method and observed
result. Static reading, guided current-agent exercises, script execution and native
runtime dispatch are separate evidence. A fixture or expected answer alone is not
execution. Inspect useful output and failed prerequisites; rerun affected cases after
correction. Apply the shared rubric without arbitrary section or step counts.
