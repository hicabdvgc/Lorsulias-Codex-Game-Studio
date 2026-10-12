# Skill Test Spec: $perf-profile

## Intended interface

Read the installed SKILL.md, its linked shared contracts and selected mode references. Preserve useful source modes while assessing the adapted outcomes.

## Case 1: Comparable measurements

**Request/inputs:** Same hardware/workload captures A=12ms B=16ms, supplied budget=14ms; distinct engine version evidence.

**Expected useful outcome:** Report +4ms (+33.3%) comparable regression, B exceeds supplied budget; identify measured contributors only where capture supports them.

## Case 2: No or incomparable capture

**Request/inputs:** No profiler file or changed workload/hardware and no budget.

**Expected useful outcome:** Provide capture plan or limited observations; no numerical bottleneck, performance pass or fixed quick-win estimate.

## Verification record requirements

Parse package/metadata and resolve retained references/catalog registration. Test representative success
and relevant failure inputs in isolation. Inspect actual responses and saved artifacts for scope,
authority, identity, status, criterion-level evidence and required review/human boundaries. Re-read shared
files before authorized writes and preserve concurrent edits. Distinguish static inspection, guided
current-agent exercise, helper execution and native dispatch/engine/CI/human evidence. Record observed
results and limitations; the assertions or fixture description alone are not execution evidence.
