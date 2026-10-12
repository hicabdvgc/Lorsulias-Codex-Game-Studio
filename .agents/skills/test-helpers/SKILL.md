---
name: test-helpers
description: "Create runner-compatible test fixtures, assertions and builders from actual system interfaces, or scaffold a selected helper structure."
---

# Test Helpers

Read `.codex/docs/work-preparation.md`, `.codex/docs/code-root-resolution.md` and
`.codex/docs/testing-engine-reference.md`. Live `docs/technical-preferences.md`
and actual project configuration determine selected engine, language, runner,
roots and commands. Library references do not establish installation or selection.
Use existing task authorization. Re-read targets before writes, preserve concurrent
and unrelated work, and inspect promised outputs after saving. Preserve completed
work if a dependent step fails; identify the affected activity.

## Invocation and scope
`$test-helpers [system-name|all|scaffold]`. With no argument identify candidate
systems and ask for the intended scope. Resolve a named system by BREAKDOWN and
explicit GDD/source mapping. All covers identified systems, retaining missing
interfaces as gaps. Scaffold covers the selected reusable helper structure without
pretending to supply domain factories. Reject ambiguous or unknown scope.

## Inspect before designing helpers
Read applicable coding standards, FRAMEWORK, system GDDs, production interfaces,
existing tests/helpers, selected runner/package configuration and source/test roots.
Verify real constructors, data formats, creation/lifetime APIs and cleanup behavior.
Missing infrastructure routes to `$test-setup`; unresolved interfaces block helpers
that depend on them. Human evaluation requirements remain in QA plans.

Identify repeated setup/assertions worth sharing: data builders, scoped fixtures,
test doubles, event capture, resource loading and cleanup. Choose helpers for actual
tests rather than generating every category or an arbitrary sample count. Keep
tests readable; do not hide the behavior being tested or reproduce production logic.

## Implement the selected route
- Godot/GdUnit4: use the installed suite/assertion/scene APIs documented for the
  selected version. Verify node ownership and teardown. Do not invent SceneRunner
  wrappers or assume arbitrary assertion methods exist.
- Unity/NUnit: use actual runtime/test assemblies and their lifecycle. An inclusive
  range assertion can use `Assert.That(value, Is.InRange(min, max))` with verified
  types/version. Domain objects need real creation contracts; do not invent
  CreateDefault factories. Event probes must subscribe and unsubscribe correctly.
- Unreal/Automation: use actual module interfaces and supported engine test APIs.
  Verify world/object setup, flags and cleanup against the installed engine. Avoid
  macros with repeated argument evaluation, global state leakage or fake worlds.

Scaffold may supply a small verified runner-compatible helper and its usage
documentation when sufficient interfaces exist. Unknown domain factories remain
documented gaps, never executable stubs presented as working implementations.
Resource helpers use selected TYPE_TEMP identity/reference/format contracts;
tool helpers exercise real input-to-output workflows with fixtures.

## Save, exercise and report
Choose paths from the actual test assembly/module/package layout, preserving existing
helpers and styles. Add a representative consumer that tests useful helper behavior,
including failure/cleanup where relevant; execute it with the selected runner when
available. Do not claim compilation or execution from inspection. Check that fake
data and generated outputs remain isolated and teardown restores test state.
Document helper API, concrete usage, assumptions and command/report paths at the
selected helper documentation location. Summarize implemented helpers, verified
consumers, preserved files and remaining unsupported scope. Missing evidence yields
PARTIAL/NOT ASSESSED for dependent conclusions. Do not modify production APIs merely
to satisfy an invented helper interface.
