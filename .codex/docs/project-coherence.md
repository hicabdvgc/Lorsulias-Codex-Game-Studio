# Project coherence observations

This read-only helper adapts the comparison purpose of Claude Code Game Studios'
`.claude/scripts/project-coherence.sh` to this studio's existing live preferences.
It supplies observations for `$setup-engine` readback and `$adopt infrastructure`.
Its output does not establish readiness, compilation, compatibility or progression.

## Invocation and dependencies

Run with Bash and Python 3.9 or later. The shell adapter uses `hook-lib.sh` and
`LORSULIA_HOOK_PYTHON`, including its existing fallback discovery. Native Python
invocation is also supported. No third-party Python packages are required.

```text
bash .codex/scripts/project-coherence.sh --project "games/My Game"
python .codex/scripts/project_coherence.py --root "<studio root>" --project "<actual project root>"
```

The shell adapter defaults to its containing studio, independently of the current
directory and Git. An explicit `--root` overrides that default. Relative `--root`
uses the current directory; relative `--project` uses the studio root. Quote paths
containing spaces or apostrophes according to the invoking shell. Git Bash paths
are converted for native Windows Python, including when automatic conversion is
disabled. The caller identifies the actual project; skeleton folders do not select it.
There is no lifecycle registration.

The helper reads the existing bold bullet fields in
`docs/technical-preferences.md`. A single literal Project / Code Roots value can
be compared with the explicit scan root. Multi-root descriptions and linked/prose
configurations remain `NOT ASSESSED`; callers resolve their meaning using the
[root-resolution procedure](code-root-resolution.md). The helper does not introduce
a new editable configuration or silently override the live authority.
For an unquoted value containing spaces, a resolvable directory provides literal
path evidence; otherwise that value remains unassessed. Quoted single paths are
explicit even when absent. An unclosed example fence or comment is a parser error,
so partial preference declarations cannot support a comparison.

## Output contract

Standard output contains one JSON object with `studio_root`, `project_root`,
`scope`, `findings`, and `errors` for a valid invocation. Each finding identifies
its `check`, `status`, `reason`, and `evidence` paths, with selected/observed values
where available. Statuses are `MATCH`, `DIFFERS`, `NOT ASSESSED`, and
`NOT APPLICABLE`. Missing roots produce JSON errors; argparse invocation errors
and unavailable Python are reported to stderr.

Exit 0 means observation completed, including differences or unavailable optional
evidence. Exit 2 means invalid invocation, discovery, read, or supported-parser
failure. Partial findings survive a metadata-reader error. An unavailable check
cannot support a passing technical conclusion. Do not treat exit 0 as a game gate.

## Supported observations and limits

- Engine selection is compared with markers at the explicitly named root:
  `project.godot`, `ProjectSettings/ProjectVersion.txt`, or one `.uproject` file.
  Competing markers and multiple Unreal projects leave the scope unassessed.
- Godot reads explicit quoted values of `rendering/renderer/rendering_method`
  and `physics/3d/physics_engine`. Forward+, Mobile and Compatibility aliases are
  mapped; named Jolt and GodotPhysics3D choices can be compared. Missing/default
  values remain unknown. The reader is deliberately limited to these scalars;
  it does not validate all Godot Variant syntax or parse scenes. Renderer platform
  overrides, command-line changes and runtime fallback remain unassessed.
  `config_version` and feature tags do not prove an exact engine patch or installation.
- Unity compares the full `m_EditorVersion` declaration with an exact selected
  version. The metadata records an editor version and does not prove installation
  or execution. Rendering, physics and package compatibility require scoped review.
- Unreal reads JSON `EngineAssociation`. Numeric associations are compared at
  equal version precision. A major/minor association cannot prove a selected patch.
  Blank or opaque source-build identifiers remain unassessed; no registry or
  installation discovery occurs. Rendering and physics require scoped review.
- The engine library version, selected version, and Installed Version Evidence
  are displayed separately. Supplied evidence text is not evaluated by this helper.
  A different library version is not an automatic mismatch or compatibility failure.
- Test Roots and Commands is reproduced as data. Commands, runner paths, presets,
  test results and build behavior require their normal scoped verification. Nothing
  in a preference value is evaluated as code.

Duplicate preference fields or supported metadata keys and malformed supported
values are execution errors. Unsupported free-form declarations remain unassessed.
This helper never writes files, starts an engine, alters settings, or acquires game
dependencies. Its readback should be interpreted together with actual project and
runtime evidence; a configuration match alone is not observed runtime behavior.

## Primary references checked on 2026-10-08

- [Godot project settings format](https://docs.godotengine.org/en/stable/tutorials/editor/project_settings.html)
  supports the project.godot text-inspection route.
- [Godot ProjectSettings](https://docs.godotengine.org/en/stable/classes/class_projectsettings.html)
  documents the named renderer/physics keys and runtime override limitations.
- [Unity's official sample ProjectVersion.txt](https://github.com/Unity-Technologies/com.unity.multiplayer.samples.bitesize/blob/main/Basic/2DSpaceShooter/ProjectSettings/ProjectVersion.txt)
  demonstrates `m_EditorVersion` and separate revision metadata. It establishes the
  file shape, without selecting that sample's editor version for a game.
- [Epic's engine association documentation](https://dev.epicgames.com/documentation/unreal-engine/managing-game-code-in-unreal-engine)
  distinguishes numeric launcher associations and source-build identifiers.

These references justify retained metadata interpretations. They do not verify a
specific future game's runtime, dependencies or library compatibility.
