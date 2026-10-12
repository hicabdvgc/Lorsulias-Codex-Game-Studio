# Installed Rules and Guidance

| File | Scope |
|---|---|
| Root AGENTS.md | Shared workflow, task boundaries, and guidance routing |
| docs/AGENTS.md | Documentation/architecture interfaces and evidence boundaries |
| CGS Skill Testing Framework/AGENTS.md | Studio evaluation and coverage |
| .codex/docs/skill-authoring.md | Referenced guidance for skill/persona/check customization |
| .codex/rules/project-safety.rules | Supplemental command prefix rules |

Design, GDD, source and prototype instruction files are installed at
`design/AGENTS.md`, `design/gdd/AGENTS.md`, `src/AGENTS.md` and
`prototypes/AGENTS.md`. Resource, narrative and shader instructions are installed at `assets/data/AGENTS.md`, `design/narrative/AGENTS.md` and `assets/shaders/AGENTS.md`. Game-test guidance is installed at `tests/AGENTS.md`, with actual roots and runner choices resolved from live preferences. Source-subsystem guidance is installed in src/core, gameplay, ai, networking and ui; actual roots and selected architecture still govern.

AGENTS.md files supply behavioral guidance. Execpolicy rules operate according
to the client's effective command-permission handling. The project does not alter
the user's filesystem sandbox or claim an enforced .env deny profile. The command
hook's selected pattern checks are described in [hooks-reference.md](hooks-reference.md).
