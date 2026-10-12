# Skill Test Spec: $localize

## Skill Summary

Exercise `.agents/skills/localize/SKILL.md` and its listed continuation with isolated fixtures.
Retain useful source interfaces while testing the adapted resource and evidence contracts.

## Static assertions

- Frontmatter name/description and UI metadata parse and match the installed identity.
- Retained references resolve or explicitly identify future/manual inputs.
- Output paths, modes and statuses agree with actual consumers and templates.
- Preserve bounded authorization, concurrent edits, required independent review and human evidence.

## Test cases

### Case 1: Configured validation

**Request / fixture:** Use a French source table, German target and selected JSON schema with msg.buy containing {count}; target has matching placeholders.

**Expected outcome:** Report structural coverage against selected locales/format; no English default or linguistic/playthrough PASS.

### Case 2: Missing or malformed

**Request / fixture:** Target omits {count}, contains malformed syntax, or source locale/format is unset.

**Expected outcome:** List key/locale mismatch or parser location; preserve originals; unset choices block dependent writes.

### Case 3: Mode boundaries

**Request / fixture:** Exercise scan/extract/validate/status/brief/cultural-review/vo-pipeline scan,script,validate,integrate/rtl-check/freeze call,lift/qa.

**Expected outcome:** Only needed prerequisites apply; extraction preserves existing IDs/values, briefs do not send messages, cultural claims need evidence, VO presence differs from recording quality, RTL requires selected behavior, freeze records a baseline and QA needs actual human/runtime evidence.

### Case 4: Concurrent freeze

**Request / fixture:** Extract an authorized new key while ACTIVE freeze records concurrent additions.

**Expected outcome:** Re-read tables and freeze state, preserve concurrent entries, record changed source baseline and do not infer filesystem enforcement.

## Evidence and grading

Record raw fixture inputs, request, actual response/artifacts, method and observed
result. Static reading, guided current-agent exercises, script execution and native
runtime dispatch are separate evidence. A fixture or expected answer alone is not
execution. Inspect useful output and failed prerequisites; rerun affected cases after
correction. Apply the shared rubric without arbitrary section or step counts.

## Regression assertion

Optional delegation requires authorization. Freeze records a source baseline/change policy and does not lock files; asset scanning uses declared locations.
