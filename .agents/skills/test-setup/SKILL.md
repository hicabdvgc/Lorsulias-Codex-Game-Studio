---
name: test-setup
description: "Scaffold missing test infrastructure for the selected project and runner; verify existing work and make CI conditional on the chosen route."
---

# Test Setup

Read `.codex/docs/work-preparation.md`, `.codex/docs/code-root-resolution.md` and
`.codex/docs/testing-engine-reference.md`. Live `docs/technical-preferences.md`
and actual project configuration determine selected engine, language, runner,
roots and commands. Library references do not establish installation or selection.
Use existing task authorization. Re-read targets before writes, preserve concurrent
and unrelated work, and inspect promised outputs after saving. Preserve completed
work if a dependent step fails; identify the affected activity.

## Invocation and discovery
`$test-setup [force]` accepts no argument or exactly force. Reject other arguments.
Resolve the actual project, packages/modules, source and test roots. An unconfigured
engine/framework, conflicting roots or unsupported combination blocks affected
scaffolding; explain the missing choice. Skeleton tests/, src/ or lowercase assets/
does not establish a game or compiler root. Inspect real runner installation and
configuration, test assemblies, existing tests, documentation and any selected CI.

Create an exact list of missing targets for the selected infrastructure. Existing
artifacts are inspected for applicability, not replaced. In normal mode, stop after
verification if no selected targets are missing. Force rechecks and fills missing
targets only; it never overwrites tests, configuration or documentation. Conflicting
existing files remain explicit unresolved work. A directory alone is not evidence
of configured infrastructure or passing tests.

## Select the supported route
- **Godot / GDScript / GdUnit4:** verify project.godot, installed addon version and
  compatible engine. Use the documented addon runner with selected suite/report
  locations. Do not invent a gdunit4_runner.gd adapter. Create only needed fixtures
  and instructions using the installed API. Missing addon/runtime remains an
  execution dependency, not proof the generated setup works.
- **Unity / C# / Unity Test Framework (NUnit):** inspect package manifest/lock and
  actual runtime assemblies. Create needed test assemblies in the chosen project
  or package scope using the package's documented assembly configuration. Reference
  the real assembly identities; a missing factory/assembly is not a placeholder to
  invent. Select EditMode, PlayMode or player tests according to actual behavior.
- **Unreal / C++ / Automation Framework:** identify the .uproject, target, module
  and installed engine. Use that version's documented test registration and runner.
  Place test code in the selected module with appropriate build dependencies.
  Document an actual runnable test selection and report destination. Avoid an
  invented universal Source/Tests module, mock world or headless wrapper.
- Other language/framework combinations require an explicitly selected, verified
  route. Report unsupported combinations; never substitute a runner silently.

## Scaffold and document
Use the selected runner's structure and meaningful test categories. A universal
unit/integration/performance/playtest tree is unnecessary. Add a README at the
chosen test documentation location when missing: purpose, selected versions,
project/source/test roots, setup prerequisites, exact invocation and working
directory, report discovery, result interpretation and relevant cleanup. Link
manual/human evidence to `production/qa/evidence/`. Include a critical-path smoke
protocol only for the selected scope, using real entry points and expected outcomes.
No arbitrary checklist size, duration or coverage percentage is imposed.

CI is conditional on an explicitly selected execution route and available runner,
licensing/credentials, platform and repository prerequisites. Preserve existing
workflows. Derive paths/commands from the same local configuration; do not assume
main, GitHub, or automatic every-push execution. Create CI only for the selected
authorized route. When CI is unselected or unavailable, document that boundary. This
skill's scaffolding request does not authorize engine/dependency installations or
credential changes; such missing prerequisites remain explicit.

## Verification and output
Parse generated configuration; compile/discover and execute a representative test
when the selected runtime is available. Inspect actual reports, count discovered
tests, failures and skipped/unassessed scope. Zero discovered tests or a missing
report cannot pass. A process exit alone is insufficient where the runner's result
contract requires report inspection. Distinguish static verification from executed
checks and CI execution. Report created/preserved targets, selected route, actual
results and remaining dependencies. COMPLETE means the requested scaffold is
verified at the stated level; unavailable runtime integration stays NOT ASSESSED.
Hand off to `$test-helpers` and `$qa-plan` with actual saved paths.
