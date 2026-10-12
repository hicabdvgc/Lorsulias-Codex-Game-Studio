# Skill Test Spec: $test-evidence-review

## Intended interface

Read the installed SKILL.md, its linked shared contracts and selected mode references. Preserve useful source modes while assessing the adapted outcomes.

## Case 1: Scoped evidence

**Request/inputs:** Story/sprint/system scope with old matching test log and newer unrelated smoke log; actual assertion and human result supplied.

**Expected useful outcome:** Use relevant criterion/revision evidence, report direct coverage and actual results; no preference for newest alone.

## Case 2: Unavailable coverage

**Request/inputs:** Missing declared output, empty/unreadable scope, unused test file, unperformed manual protocol or independence.

**Expected useful outcome:** Report MISSING/INCOMPLETE/NOT ASSESSED and known failures; default no writes or progress changes.

## Verification record requirements

Parse package/metadata and resolve retained references/catalog registration. Test representative success
and relevant failure inputs in isolation. Inspect actual responses and saved artifacts for scope,
authority, identity, status, criterion-level evidence and required review/human boundaries. Re-read shared
files before authorized writes and preserve concurrent edits. Distinguish static inspection, guided
current-agent exercise, helper execution and native dispatch/engine/CI/human evidence. Record observed
results and limitations; the assertions or fixture description alone are not execution evidence.
