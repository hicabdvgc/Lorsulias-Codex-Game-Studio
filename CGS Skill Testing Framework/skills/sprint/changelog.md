# Skill Test Spec: $changelog

## Intended interface

Read the installed skill and linked contracts. Preserve its listed modes and actual downstream outputs.

## Case 1: Historical release

**Request/inputs:** Disposable Git repo with v1 and v2, later HEAD changes; request v2 and save.

**Expected useful outcome:** Use v1..v2 only; preserve other history and stable version section on repeat.

## Case 2: Unavailable history

**Request/inputs:** Non-Git workspace or missing target ref.

**Expected useful outcome:** Stop with evidence limitation, no invented history or changelog save.

## Additional interface checks

Exercise retained argument/style/focus routes and relevant collisions/concurrency. Reviews remain
conversational by default; explicitly requested authored outputs use bounded saves with readback.
Check actual paths, identities, accepted-decision authority, candidate scope, required evidence,
independence and human boundaries. Verify metadata, discovery and catalog registration. Record static
inspection, guided current-agent exercises, executable checks and native integration separately.
An assertion or fixture definition is not execution evidence. Do not weaken a check to obtain a pass.
