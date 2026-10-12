# Skill Test Spec: $test-flakiness

## Intended interface

Read the installed SKILL.md, its linked shared contracts and selected mode references. Preserve useful source modes while assessing the adapted outcomes.

## Case 1: Observed intermittence

**Request/inputs:** Same revision/environment/test has pass, fail, pass; another test fails all three runs.

**Expected useful outcome:** Report 1/3 observed failures and intermittence for first; persistent failure for second; cause remains hypothesis.

## Case 2: Incomparable/quarantine

**Request/inputs:** Pass and fail from different revisions; registry lacks evidence; save recommendation requested.

**Expected useful outcome:** No same-build flake proof; preserve manifest and distinguish proposed quarantine from actually disabled tests.

## Verification record requirements

Parse package/metadata and resolve retained references/catalog registration. Test representative success
and relevant failure inputs in isolation. Inspect actual responses and saved artifacts for scope,
authority, identity, status, criterion-level evidence and required review/human boundaries. Re-read shared
files before authorized writes and preserve concurrent edits. Distinguish static inspection, guided
current-agent exercise, helper execution and native dispatch/engine/CI/human evidence. Record observed
results and limitations; the assertions or fixture description alone are not execution evidence.
