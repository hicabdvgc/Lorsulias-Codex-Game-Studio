# Resolve Project, Source and Test Locations

Adapted from Claude Code Game Studios' code-root guidance. Live
`docs/technical-preferences.md` is authoritative; `.codex/docs/technical-preferences.md`
is only its template. No project.yaml resolver or hook implements this procedure.

1. Read selected engine/language, Project / Code Roots, Test Roots and Commands,
   and Testing framework. Unconfigured fields remain unknown.
2. Inspect the actual project and runner configuration. Project files, package,
   assembly/module definitions and discovery commands establish participation.
   Account for nested projects, multiple roots and packages/plugins.
3. Unambiguous project evidence may identify a candidate location. State that
   evidence and resolve conflicts with preferences before dependent writes. A lone
   src/, Assets/, Source/ or tests/ directory does not establish an engine or root.
   The studio already has skeleton directories, and Windows case-insensitive
   existence checks can confuse its assets/ with an engine Assets/ directory.
4. Resolve relative paths against their documented studio or nested-project base.
   Preserve spaces/apostrophes and use the native form needed by the command.
   Keep writes within selected task locations; never silently scan another project
   or create code in the studio skeleton to resolve uncertainty.

For Godot inspect project.godot, language and addon/runner configuration. For Unity
inspect the selected project, Packages and test assemblies; naming a tests/ folder
does not establish discovery. For Unreal inspect .uproject, modules/plugins and
build/test definitions rather than assuming Source/Tests. These are inspection cues.

An unresolved root means NOT ASSESSED for its scan, not zero findings. Dependent
writes are blocked; independent planning may continue with the gap stated. Missing
installed tools differ from infrastructure the setup task creates. Do not change
personal settings or install runtimes to hide unavailable evidence.

An authorized setup records framework/package version, roots, command working
directory, test command/discovery scope, actual report path and verification in
live preferences or a linked project test README. Keep one editable authority for
each value; link the runner's configuration rather than duplicating it.
See [engine testing references](testing-engine-reference.md).

For bounded declaration/metadata readback, use the optional
[project-coherence observer](project-coherence.md) with an explicit project root.
Its findings leave unsupported or ambiguous checks unassessed; they do not resolve
root conflicts or authorize dependent writes.
