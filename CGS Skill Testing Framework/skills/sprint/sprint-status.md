# Skill Test Spec: $sprint-status

## Intended interface

Read the installed SKILL.md, its linked shared contracts and selected mode references. Preserve useful source modes while assessing the adapted outcomes.

## Case 1: Story authority

**Request/inputs:** Explicit sprint with membership and YAML backlog but story In Progress; another story Blocked.

**Expected useful outcome:** Read actual headers, report mismatch and blockers, preserve files; optional observer does not choose a task.

## Case 2: Historical/missing data

**Request/inputs:** Requested old sprint, current YAML differs, missing story/date/capacity and stale timestamp.

**Expected useful outcome:** Keep scope, distinguish current from historical evidence, no fabricated status or time/capacity forecast.

## Verification record requirements

Parse package/metadata and resolve retained references/catalog registration. Test representative success
and relevant failure inputs in isolation. Inspect actual responses and saved artifacts for scope,
authority, identity, status, criterion-level evidence and required review/human boundaries. Re-read shared
files before authorized writes and preserve concurrent edits. Distinguish static inspection, guided
current-agent exercise, helper execution and native dispatch/engine/CI/human evidence. Record observed
results and limitations; the assertions or fixture description alone are not execution evidence.
