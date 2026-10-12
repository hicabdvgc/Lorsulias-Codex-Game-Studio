# Lorsulia's Codex Game Studio

This repository supplies Lorsulia's adapted studio workflow. Follow the four-section
workflow recorded in [.codex/docs/workflow-catalog.yaml](.codex/docs/workflow-catalog.yaml).
The catalog distinguishes manual work and installed support;
the presence of a document or folder does not establish completion.
Read the [complete workflow guide](docs/WORKFLOW-GUIDE.md) for the ordered
procedures, activity handoffs, human responsibilities, and links to studio support.

## Working principles

- Read the relevant existing artifacts before asking about information they contain.
- Preserve user-authored CONCEPT. AI can support research and review; the developer
  writes the concept and supplies actual reference-game and playtest experience.
- Carry an authorized bounded task through editing and verification without repeated
  file-level approval. Ask about unresolved product decisions or material scope changes.
- Apply the framework and governing decisions relevant to the activity. Early system
  design uses the preliminary framework; future resource schemas are later outputs.
- Required human evaluation and the vertical-slice hard gate remain required with any
  executor. Report unavailable evidence explicitly and keep dependent work incomplete.
- Use available people/agents within their responsibilities. Follow the current
  environment's delegation policy; a persona file supplies guidance, not permissions.
- Validate the intended outcome and report what was actually checked. Preserve
  unrelated user changes. Commit, push, publish, and message others only when authorized.

## Read when relevant

- [Directory and artifact contracts](.codex/docs/directory-structure.md)
- [Collaboration](docs/COLLABORATIVE-DESIGN-PRINCIPLE.md)
- [Coordination](.codex/docs/coordination-rules.md) and [installed roles](.codex/docs/agent-roster.md)
- [Review workflow](.codex/docs/review-workflow.md) and [gate prompts](.codex/docs/director-gates.md)
- [Continuity](.codex/docs/context-management.md)
- [Skill authoring](.codex/docs/skill-authoring.md) when adapting skills, personas, or checks
- [Recovery](.codex/docs/error-recovery-protocol.md) when a required handoff is incomplete

The engine, language, platforms, and game-specific requirements remain undecided.
Read `docs/technical-preferences.md` for live configuration;
`.codex/docs/technical-preferences.md` is its separate template. Consult the
selected engine's verified references and distinguish library, selected and installed
versions. Reference studies use root-level `game_ref/` and the reference-game-study
template. FRAMEWORK authoring uses the development-framework template.
Nested AGENTS.md files add guidance for their directory scopes.

For resource-bearing work, use `.codex/docs/resource-preparation.md` and applicable root `RES_TYPE.md` / `resource_templates/` contracts. Use `.codex/docs/tool-development.md` for demonstrated tooling needs. Initial designs may record unresolved resource needs; later integration checks require the relevant contracts and actual evidence.

For epic/story readiness, milestones, sprint status and QA, apply [.codex/docs/work-preparation.md](.codex/docs/work-preparation.md). Story Status fields own progress; sprint YAML is derived. Use [.codex/docs/code-root-resolution.md](.codex/docs/code-root-resolution.md) for actual project/test roots. Final milestone authoring follows the vertical-slice hard gate; earlier drafts identify missing evidence.

For execution/completion and runtime evidence, apply [.codex/docs/execution-and-evidence.md](.codex/docs/execution-and-evidence.md). Use [.codex/docs/progression.md](.codex/docs/progression.md) for four-section gates and milestone checkpoints. New playtest records use production/playtests/.


For release/incident/communication handoffs use [.codex/docs/release-and-operations.md](.codex/docs/release-and-operations.md). Release evidence is candidate-specific; deployment and publication use existing explicit authorization. Continuity uses bounded checkpoints and actual lifecycle observations.
