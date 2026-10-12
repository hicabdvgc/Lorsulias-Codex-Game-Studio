# Skill Test Spec: $balance-check

## Skill Summary

Exercise `.agents/skills/balance-check/SKILL.md` and its listed continuation with isolated fixtures.
Retain useful source interfaces while testing the adapted resource and evidence contracts.

## Static assertions

- Frontmatter name/description and UI metadata parse and match the installed identity.
- Retained references resolve or explicitly identify future/manual inputs.
- Output paths, modes and statuses agree with actual consumers and templates.
- Preserve bounded authorization, concurrent edits, required independent review and human evidence.

## Test cases

### Case 1: Calculation

**Request / fixture:** GDD defines cost=2 tokens/use, gain=6 tokens/min and 2 uses/min.

**Expected outcome:** Calculate 2 tokens/min net gain over the supplied horizon; compare actual design target without claiming player behavior.

### Case 2: Missing baseline

**Request / fixture:** Remove use frequency or mix seconds and minutes without defined conversion.

**Expected outcome:** Mark affected calculation NOT EVALUATED; no BALANCED conclusion or invented threshold.

### Case 3: Fix and preserve

**Request / fixture:** Authorize changing one recorded rate, with another file edited concurrently.

**Expected outcome:** Apply only the settled change, re-read current data, preserve unrelated edits and rerun affected calculations; optional report save is separate from approval.

## Evidence and grading

Record raw fixture inputs, request, actual response/artifacts, method and observed
result. Static reading, guided current-agent exercises, script execution and native
runtime dispatch are separate evidence. A fixture or expected answer alone is not
execution. Inspect useful output and failed prerequisites; rerun affected cases after
correction. Apply the shared rubric without arbitrary section or step counts.
