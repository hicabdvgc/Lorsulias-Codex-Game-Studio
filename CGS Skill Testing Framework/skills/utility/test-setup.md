# Skill Test Spec: $test-setup

## Skill Summary

Scaffold missing test infrastructure for the selected project and runner; verify existing work and make CI conditional on the chosen route.

## Static assertions

- Package identity and UI metadata parse; registered paths resolve.
- Retained modes and outputs agree with work-preparation.md and actual consumers.
- Governance, stable IDs, authorization, concurrent edits and saved-output checks are preserved.
- Required independent review and human evidence remain required across review depths.

## Test cases

### Case 1: Supported selected routes

**Request / fixture:** Separate Godot/GDScript/GdUnit4, Unity/C#/UTF and Unreal/C++/Automation fixtures with actual roots/config/version evidence.

**Expected outcome:** Generate only selected missing targets; use real runner/assembly/module interfaces. No synthetic adapter, universal path or CI default.

### Case 2: Force preservation

**Request / fixture:** $test-setup force with existing test/config content and missing README, CI unselected.

**Expected outcome:** Preserve existing bytes, fill missing selected target, document conflicts without overwrite; no CI generated.

### Case 3: Unavailable/unsupported

**Request / fixture:** Only skeleton assets/src/tests, conflicting nested roots, unconfigured/missing runner, unsupported language/runner or absent license.

**Expected outcome:** Dependent writes blocked or scoped partial; no substitution/installation or false execution claim. Static and runtime results separate.

## Evidence and grading
Keep fixture inputs, actual generated artifacts/response, method, observed result
and limitations. Written assertions alone are not behavioral evidence. Separate
static inspection, guided current-agent exercise, script execution and native
dispatch/engine/CI/human evaluation. Inspect results against intended outcomes and
repeat affected checks after corrections. Do not invent an unavailable passing run.
