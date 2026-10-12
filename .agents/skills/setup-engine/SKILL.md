---
name: setup-engine
description: "Select project engine choices and maintain verified technical preferences and engine references; distinguish configuration documentation from installation or migration."
---

# Setup Engine

Invoke as `$setup-engine`.

Arguments: `[engine] | [engine version] | refresh | upgrade [old-version] [new-version] | no args for guided selection`.

## Shared execution boundary

Read the relevant artifacts before asking about information they contain. Existing
bounded task authorization covers its edits and verification; ask about unresolved
consequential choices or a material scope expansion. Preserve unrelated changes
and re-read a target before writing if its baseline may have changed.

Use available qualified executors under the current environment's delegation
policy. Role names describe expertise. Follow `.codex/docs/review-workflow.md`
and `.codex/docs/director-gates.md`: required independent review and human evidence
remain required with any executor. Identify self-review; unavailable required
evidence is NOT ASSESSED. Review-depth flags change optional breadth, never these
obligations. `full` adds applicable specialist/gate reviews; `lean` is focused;
`solo` identifies self-review. Default to focused review when unspecified.

Apply `.codex/docs/skill-authoring.md` and `.codex/docs/error-recovery-protocol.md`.
Verify promised saved outputs before handoff. Resolve available support from the
installed catalog; require an input only when the selected activity needs its outcome.


## Resolve the request

Preserve guided selection, explicit Godot/Unity/Unreal selection, refresh and upgrade.
Reject unsupported forms; ask for a missing upgrade destination or ambiguous engine.
Read live `docs/technical-preferences.md`, actual engine project files when present,
root instructions, and the selected library's VERSION reference. A supplied engine
choice needs no repeated selection question.

For guided selection, read CONCEPT if available and establish relevant platforms,
inputs, dimensionality, team experience, deployment needs and constraints. Compare
only choices supported by those needs. Verify version, licensing, platform and
API claims against current official sources before recommending them. Missing
evidence remains explicit; do not silently substitute another engine or version.

## Configure confirmed project choices

Use `.codex/docs/technical-preferences.md` as the template for the live document.
Record selected engine/version, actual chosen languages, renderer, physics, inputs,
platforms, libraries, naming, budgets, testing and source/test locations when known.
Leave other fields unconfigured; examples and defaults are not user selections.

Route only relevant installed capabilities:
- Godot: primary godot-specialist; GDScript/C#/GDExtension/shader specialists as selected.
- Unity: primary unity-specialist; Addressables/DOTS/shader/UI specialists as applicable.
- Unreal: primary unreal-specialist; Blueprint/GAS/replication/UMG specialists as applicable.

The roster records availability. Missing routing can be handled by a qualified
available executor, preserving any independent-review requirement. Do not add
languages, packages or networking solely because their personas exist.

The live preferences own the project choice. Root AGENTS links there; VERSION
records the library's documented coverage. Compare them, without creating a
second editable project pin or changing shared persona definitions.

Read [references/continued-workflow.md](references/continued-workflow.md) for
reference refresh, upgrade, evidence handling and completion.
