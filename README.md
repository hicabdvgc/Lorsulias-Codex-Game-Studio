<h1 align="center">Lorsulia's Codex Game Studio</h1>

<p align="center">
  A game-development workflow for Codex, from a developer-authored concept to release.<br>
  49 personas. 76 skills. Four workflow sections, with human involvement in preparation.
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
  <a href=".codex/agents"><img src="https://img.shields.io/badge/personas-49-blueviolet" alt="49 persona definitions"></a>
  <a href=".agents/skills"><img src="https://img.shields.io/badge/skills-76-green" alt="76 skills"></a>
  <a href=".codex/hooks.json"><img src="https://img.shields.io/badge/hook%20handlers-11-orange" alt="11 registered hook handlers"></a>
  <a href="docs/WORKFLOW-GUIDE.md"><img src="https://img.shields.io/badge/workflow%20activities-59-teal" alt="59 workflow activities"></a>
  <a href="INSTALL.md"><img src="https://img.shields.io/badge/built%20for-Codex-111111" alt="Built for Codex"></a>
</p>

<p align="center">
  A follow-up adaptation of<br>
  <a href="https://github.com/Aesma/ChatGpt-Game-Studios/tree/Release-1.3.1">Aesma / ChatGPT Game Studios — Release 1.3.1</a><br>
  and <a href="https://github.com/Donchitos/Claude-Code-Game-Studios">Donchitos / Claude Code Game Studios</a>.
</p>

Lorsulia retains a very similar project structure while introducing a different
workflow and corresponding skills, templates, and personas that emphasize human
involvement in preparation. The developer authors the game concept, supplies
reference-game experience, and participates in design decisions and evaluation.
See [NOTICE.md](NOTICE.md) for the project's lineage and attribution.

## What this studio provides

This repository supplies a reusable project scaffold for developing games with
Codex. It connects design documents, technical decisions, resource preparation,
implementation tasks, testing, and release records through a shared workflow.
You can use it to start a game or assess how an existing project fits the studio.

The preparation steps make the developer's intentions, system boundaries, and
resource requirements explicit before production work depends on them. Skills
guide individual activities; personas provide relevant expertise; templates
give their outputs a consistent form. You choose the game, engine, scope, and
product decisions, and supply the required human play and usability observations.

The folder starts with unconfigured game-specific choices. Design documents,
game code, resources, and release candidates are produced as the project progresses.

## Contents

- [What is included](#what-is-included)
- [Start a project](#start-a-project)
- [The four-section workflow](#the-four-section-workflow)
- [Skills](#skills)
- [Personas and responsibilities](#personas-and-responsibilities)
- [Everyday examples](#everyday-examples)
- [Project organization](#project-organization)
- [Configuration and engine support](#configuration-and-engine-support)
- [Reviews, testing and progression](#reviews-testing-and-progression)
- [Hooks and session continuity](#hooks-and-session-continuity)
- [Parallel work and Git worktrees](#parallel-work-and-git-worktrees)
- [Customize and maintain](#customize-and-maintain)
- [How Lorsulia differs](#how-lorsulia-differs)
- [Troubleshooting](#troubleshooting)
- [Contributing and license](#contributing-and-license)

## What is included

| Component | Included | Purpose |
|---|---:|---|
| [Skills](.agents/skills) | 76 | Guided activities for design, architecture, implementation, QA, planning, release and studio maintenance. |
| [Personas](.codex/agents) | 49 | Defined responsibilities across creative, technical, production and engine-specific work. |
| [Workflow activities](docs/WORKFLOW-GUIDE.md) | 59 | Ordered procedures and handoffs across four sections. |
| [Hook registrations](.codex/hooks.json) | 11 handlers / 8 events | Selected command/resource observations, lifecycle records and recovery context. |
| [Templates and supporting guides](.codex/docs/templates) | 53 files | Concepts, GDDs, reference studies, framework, architecture, resources, UX, stories, QA and release documents. |
| [Skill/persona specifications](<CGS Skill Testing Framework/catalog.yaml>) | 125 | Registered evaluation specifications for all 76 skills and 49 personas. |
| [Scoped guidance](.codex/docs/rules-reference.md) | Root and nested `AGENTS.md` files | Instructions relevant to design, documentation, resources, source subsystems and tests. |
| [Engine references](docs/engine-reference/README.md) | Godot, Unity and Unreal | Versioned reference material for the selected engine's APIs, modules and integration choices. |
| [Runtime checks](<CGS Skill Testing Framework/runtime/README.md>) | Structural and executable helpers | Checks for studio metadata, local references, launchers, resources, continuity and other supported interfaces. |

Counts describe shipped files and registrations. Engine installation, active
persona loading, hook dispatch and game readiness are verified separately.

## Start a project

**READ THE WORKFLOW GUIDE FIRST!**

1. Read the [complete workflow guide](docs/WORKFLOW-GUIDE.md) for the activity
   order, developer responsibilities, expected outputs and handoffs.
2. Get the complete repository, including its hidden directories:

   ```bash
   git clone https://github.com/hicabdvgc/Lorsulias-Codex-Game-Studio.git my-game
   cd my-game
   ```

   Access to a private repository requires an authorized GitHub account.
   You can also extract the complete repository ZIP into a new project folder.
3. Follow [INSTALL.md](INSTALL.md) to prepare the runtimes. Open `my-game`
   itself as the Codex project root, and read [AGENTS.md](AGENTS.md).
4. Complete the client's project trust and hook-enablement steps. Check that
   project skills and personas are discovered; inspect the hook registrations
   and any loading errors. The installation guide explains these checks.
5. Start a chat in that project and invoke `$start`. Use `$help` to identify
   the next relevant activity or `$studio-status` to inspect existing work.
6. Use `$setup-engine` when ready to select the engine, language and platform.
   Confirm those choices in [live technical preferences](docs/technical-preferences.md).

### Runtime prerequisites

| Requirement | Used for |
|---|---|
| A Codex client supporting project skills, custom agents and hooks | Loading and using the studio's project configuration. |
| Git | Cloning, repository observations and authorized worktree integration. |
| Python 3.11+ and `PyYAML>=6.0,<7` | The complete studio-maintenance test suite and YAML-based observers. |
| Bash | Shell hooks and observation helpers. |
| Git for Windows and PowerShell on Windows | The checked-in Windows launchers. |
| Your selected engine and game dependencies | Building and running the particular game. |

For example, on Windows, create the project environment from the cloned root:

```powershell
py -3 -m venv .venv
& .\.venv\Scripts\python.exe -m pip install -r 'CGS Skill Testing Framework/runtime/requirements.txt'
```

On macOS or Linux:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r 'CGS Skill Testing Framework/runtime/requirements.txt'
```

The [installation guide](INSTALL.md) covers existing-Python fallbacks, Git Bash
selection, runtime verification and client activation. Hooks look for the
project's `.venv`; a process-level `LORSULIA_HOOK_PYTHON` can select an existing
Python explicitly. Shared files contain no machine-specific executable paths.

### Bringing an existing game

Use `$adopt` to inspect the game's current interfaces and prepare a scoped
adoption plan. Preserve its designs, source, resources, accepted decisions and
progress records. Use `$onboard` to orient a contributor to an existing role or
area. An existing project can enter through its actual evidence and remaining
work; adoption does not reset its progress.

## The four-section workflow

The [workflow catalog](.codex/docs/workflow-catalog.yaml) and
[complete guide](docs/WORKFLOW-GUIDE.md) describe the same 59 activities.
Release and maintenance are included in the Implementation section.

| Section | Main work | Handoff |
|---|---|---|
| **1. Conceptualization** | Explore the idea, write the concept, study reference games, break down the systems and establish development principles. | Developer-authored CONCEPT, actual reference studies, Full BREAKDOWN and Preliminary FRAMEWORK. |
| **2. Development schematics** | Design the systems, complete FRAMEWORK, establish architecture and accepted decisions, define accessibility and resource contracts, and revise the GDDs for integration. | Connected system designs, technical decisions, implementation rules and usable resource definitions. |
| **3. Pre-implementation** | Gather and format resources, assemble the resource library, and develop and evaluate any selected creator tools. | Prepared resources and usable tools, with their instructions and evaluation evidence. |
| **4. Implementation** | Design UX, build a playable slice, prepare work, pass the slice gate, define milestones, implement and test through MVP/Alpha/Beta/Gold, then assess and deliver the release. | Verified milestone outcomes, an assessed candidate, and authorized delivery and maintenance records. |

### Documents that carry decisions forward

- **CONCEPT** records the developer's intended game and experience.
- **BREAKDOWN** identifies systems, responsibilities and dependencies. It has
  preliminary and full states as the design develops.
- **FRAMEWORK** describes how additions, modifications and framework revisions
  are handled. Initial system design uses its preliminary form.
- **GDDs** describe individual systems and their relationships.
- **Architecture, ADRs and CONTROL** record the technical arrangement, accepted
  decisions and applicable implementation rules.
- **Resource contracts** define the formats and validation needed to prepare
  resources for their consumers.
- **Stories, QA evidence and milestone definitions** connect the intended
  outcomes to actual implementation and evaluation.

The playable slice supplies experience before final milestone definitions are
authored. The slice gate requires actual play, integration, and evidence that
the framework supports additions and modifications. The guide explains which
activities are direct developer work and which have installed skill support.

## Skills

Invoke skills with `$skill-name` in a Codex chat opened at the project root.
Each linked skill documents its arguments, inputs and outputs. The groups below
are a navigation aid; the workflow guide determines the order for your project.

| Task | Installed skills |
|---|---|
| Orientation and setup | [$start](.agents/skills/start/SKILL.md), [$help](.agents/skills/help/SKILL.md), [$project-stage-detect](.agents/skills/project-stage-detect/SKILL.md), [$studio-status](.agents/skills/studio-status/SKILL.md), [$adopt](.agents/skills/adopt/SKILL.md), [$onboard](.agents/skills/onboard/SKILL.md), [$setup-engine](.agents/skills/setup-engine/SKILL.md) |
| Design and change propagation | [$brainstorm](.agents/skills/brainstorm/SKILL.md), [$map-systems](.agents/skills/map-systems/SKILL.md), [$design-system](.agents/skills/design-system/SKILL.md), [$quick-design](.agents/skills/quick-design/SKILL.md), [$design-review](.agents/skills/design-review/SKILL.md), [$review-all-gdds](.agents/skills/review-all-gdds/SKILL.md), [$consistency-check](.agents/skills/consistency-check/SKILL.md), [$propagate-design-change](.agents/skills/propagate-design-change/SKILL.md), [$reverse-document](.agents/skills/reverse-document/SKILL.md) |
| Architecture and decisions | [$create-architecture](.agents/skills/create-architecture/SKILL.md), [$architecture-decision](.agents/skills/architecture-decision/SKILL.md), [$architecture-review](.agents/skills/architecture-review/SKILL.md), [$create-control-manifest](.agents/skills/create-control-manifest/SKILL.md) |
| Art, resources and content | [$art-bible](.agents/skills/art-bible/SKILL.md), [$asset-spec](.agents/skills/asset-spec/SKILL.md), [$asset-audit](.agents/skills/asset-audit/SKILL.md), [$content-audit](.agents/skills/content-audit/SKILL.md) |
| UX and localization | [$ux-design](.agents/skills/ux-design/SKILL.md), [$ux-review](.agents/skills/ux-review/SKILL.md), [$localize](.agents/skills/localize/SKILL.md) |
| Prototypes and slice | [$prototype](.agents/skills/prototype/SKILL.md), [$vertical-slice](.agents/skills/vertical-slice/SKILL.md) |
| Work preparation and planning | [$create-epics](.agents/skills/create-epics/SKILL.md), [$create-stories](.agents/skills/create-stories/SKILL.md), [$story-readiness](.agents/skills/story-readiness/SKILL.md), [$define-milestones](.agents/skills/define-milestones/SKILL.md), [$estimate](.agents/skills/estimate/SKILL.md), [$sprint-plan](.agents/skills/sprint-plan/SKILL.md), [$sprint-status](.agents/skills/sprint-status/SKILL.md), [$scope-check](.agents/skills/scope-check/SKILL.md) |
| Implementation and closure | [$dev-story](.agents/skills/dev-story/SKILL.md), [$code-review](.agents/skills/code-review/SKILL.md), [$story-done](.agents/skills/story-done/SKILL.md) |
| QA and regression | [$qa-plan](.agents/skills/qa-plan/SKILL.md), [$test-setup](.agents/skills/test-setup/SKILL.md), [$test-helpers](.agents/skills/test-helpers/SKILL.md), [$smoke-check](.agents/skills/smoke-check/SKILL.md), [$regression-suite](.agents/skills/regression-suite/SKILL.md), [$test-evidence-review](.agents/skills/test-evidence-review/SKILL.md), [$test-flakiness](.agents/skills/test-flakiness/SKILL.md), [$soak-test](.agents/skills/soak-test/SKILL.md) |
| Technical analysis | [$balance-check](.agents/skills/balance-check/SKILL.md), [$perf-profile](.agents/skills/perf-profile/SKILL.md), [$security-audit](.agents/skills/security-audit/SKILL.md), [$tech-debt](.agents/skills/tech-debt/SKILL.md) |
| Evaluation and production records | [$playtest-report](.agents/skills/playtest-report/SKILL.md), [$milestone-review](.agents/skills/milestone-review/SKILL.md), [$gate-check](.agents/skills/gate-check/SKILL.md), [$retrospective](.agents/skills/retrospective/SKILL.md), [$bug-report](.agents/skills/bug-report/SKILL.md), [$bug-triage](.agents/skills/bug-triage/SKILL.md) |
| Release and maintenance | [$release-checklist](.agents/skills/release-checklist/SKILL.md), [$launch-checklist](.agents/skills/launch-checklist/SKILL.md), [$changelog](.agents/skills/changelog/SKILL.md), [$patch-notes](.agents/skills/patch-notes/SKILL.md), [$hotfix](.agents/skills/hotfix/SKILL.md), [$day-one-patch](.agents/skills/day-one-patch/SKILL.md) |
| Team coordination | [$team-audio](.agents/skills/team-audio/SKILL.md), [$team-combat](.agents/skills/team-combat/SKILL.md), [$team-level](.agents/skills/team-level/SKILL.md), [$team-live-ops](.agents/skills/team-live-ops/SKILL.md), [$team-narrative](.agents/skills/team-narrative/SKILL.md), [$team-polish](.agents/skills/team-polish/SKILL.md), [$team-qa](.agents/skills/team-qa/SKILL.md), [$team-release](.agents/skills/team-release/SKILL.md), [$team-ui](.agents/skills/team-ui/SKILL.md) |
| Studio checks and integration | [$skill-test](.agents/skills/skill-test/SKILL.md), [$skill-improve](.agents/skills/skill-improve/SKILL.md), [$integrate-worktrees](.agents/skills/integrate-worktrees/SKILL.md) |

## Personas and responsibilities

The 49 persona definitions describe expertise and work boundaries. Assign work
to the available people or agents suited to the task. They inherit the active
session's model, reasoning, permissions and tools. Their presence in the folder
does not automatically launch a team or authorize delegation.

| Area | Personas |
|---|---|
| Direction and planning | `creative-director`, `technical-director`, `producer` |
| Game and system design | `game-designer`, `systems-designer`, `economy-designer`, `level-designer` |
| Narrative | `narrative-director`, `world-builder`, `writer` |
| Art and audio | `art-director`, `audio-director`, `technical-artist`, `sound-designer` |
| Player experience | `ux-designer`, `ui-programmer`, `accessibility-specialist`, `localization-lead` |
| Engineering and tools | `lead-programmer`, `gameplay-programmer`, `engine-programmer`, `ai-programmer`, `network-programmer`, `tools-programmer`, `prototyper` |
| QA and technical assessment | `qa-lead`, `qa-tester`, `performance-analyst`, `security-engineer` |
| Operations | `release-manager`, `devops-engineer`, `community-manager`, `analytics-engineer`, `live-ops-designer` |

### Engine specialists

| Engine family | Personas |
|---|---|
| Godot | `godot-specialist`, `godot-gdscript-specialist`, `godot-csharp-specialist`, `godot-gdextension-specialist`, `godot-shader-specialist` |
| Unity | `unity-specialist`, `unity-addressables-specialist`, `unity-dots-specialist`, `unity-shader-specialist`, `unity-ui-specialist` |
| Unreal | `unreal-specialist`, `ue-blueprint-specialist`, `ue-gas-specialist`, `ue-replication-specialist`, `ue-umg-specialist` |

The [roster](.codex/docs/agent-roster.md) links to each definition. The
[coordination rules](.codex/docs/coordination-rules.md) cover responsibilities,
dependencies, shared-file ownership and cross-domain decisions. Assignment is
based on the task; work does not have to traverse a fixed hierarchy of roles.

## Everyday examples

### Find the next useful activity

```text
$start
$help
$studio-status
```

Use these individually for orientation, next-step guidance, or a read-only view
of declared stage and recovery context. For an idea still taking shape, use
`$brainstorm` to explore it before writing your concept. With the relevant
concept and framework inputs available, `$map-systems` and `$design-system`
support the breakdown and detailed system design.

### Implement a prepared story

Replace the angle-bracket placeholders below with actual project paths. Each
step consumes the previous work and its evidence; the sequence is not a batch
command to run without checking the intermediate results.

```text
$story-readiness <story-file>
$qa-plan story: <story-file>
$dev-story <story-file>
$code-review <source-file> <story-file>
$test-evidence-review <story-file>
$story-done <story-file>
```

Readiness assesses the pickup inputs. QA planning defines how the criteria will
be checked. Implementation executes the applicable checks and leaves the story
In Progress. Code and evidence reviews assess the actual revision, with
independent reviewers where required. Closure is a separate step after the
required criteria and reviews pass. The story header owns status; sprint YAML
is derived from it.

### Trace a design change

Document the changed requirement and use `$propagate-design-change` to identify
affected GDDs, decisions, resources, implementation and tests. A bounded tuning
change may use `$quick-design` when it fits the project's established scope.
Prepared resources and engine copies keep their source and revision identities
so the corresponding checks can be repeated after the change.

## Project organization

```text
AGENTS.md                          Shared workflow and task instructions
README.md / INSTALL.md             Overview and installation
.agents/skills/                    Skill packages and UI metadata
.codex/
  config.toml                     Project configuration
  agents/                         Persona definitions
  docs/                           Shared procedures, catalog and templates
  hooks.json / hooks/             Hook registrations and implementations
  scripts/                        Explicit observation and continuity helpers
  rules/                          Supplemental command policy
  guidance/                       Repository role guidance
CGS Skill Testing Framework/       Specifications and reusable studio checks
design/                           Concept, system designs, narrative and UX
docs/                             Workflow guide, technical choices and architecture
game_ref/                         Reference-game studies and evidence
resource_templates/               Game-specific resource contracts and templates
res_lib/                          Prepared resource library
tools_lib/                        Selected creator tools and instructions
src/ / assets/                    Game implementation and assets
tests/ / tools/ / prototypes/      Game tests, project tooling and experiments
production/                       Stories, milestones, QA, playtests and release records
```

The [directory and artifact contracts](.codex/docs/directory-structure.md)
define authoritative locations and distinguish studio templates from future
game outputs. For example, `RES_TYPE.md`, `docs/FRAMEWORK.md`, system GDDs and
the game's milestone definitions are authored during the workflow. Empty
scaffold folders are preserved through `.gitkeep` files.

Game code and test roots follow the selected engine. The
[root-resolution guidance](.codex/docs/code-root-resolution.md) connects the
actual engine project to the studio documents. Generated reports, local Python
environments and session logs are excluded from Git by the supplied ignore rules.

## Configuration and engine support

| Setting or decision | Where it belongs |
|---|---|
| Engine, installed version evidence, language, platform, input, test runner and budgets | [Live technical preferences](docs/technical-preferences.md), maintained with `$setup-engine`. |
| Model, reasoning, permissions and concurrency | The user's effective Codex configuration; persona files inherit it. |
| Project hook registration | [.codex/hooks.json](.codex/hooks.json), subject to the active client's trust and enablement. |
| Game architecture and implementation rules | The game's architecture documents, accepted ADRs and CONTROL. |
| Game-specific resource formats and preparation | `RES_TYPE.md`, `resource_templates/` and the [resource procedure](.codex/docs/resource-preparation.md). |
| Creator-tool requirements and verification | The [tool-development procedure](.codex/docs/tool-development.md) and the selected tool's own records. |

Godot, Unity and Unreal each have a reference library and specialist personas.
`$setup-engine` records the selected choices and checks their evidence. Engine
installation, SDKs, plugins and game dependencies remain separate requirements.
A library's recorded version does not establish what is installed on your machine.

The scaffold can be used on Windows, macOS or Linux with the appropriate
runtime dependencies. Windows launchers use PowerShell and Git Bash; Unix
launchers use Bash. Native hook availability follows the installed Codex
client. Consult [setup requirements](.codex/docs/setup-requirements.md) for
the requirements of each capability.

## Reviews, testing and progression

Reviews identify the actual artifact, governing requirements, revision and
evidence. The [review workflow](.codex/docs/review-workflow.md) distinguishes
self-review, required independent review, human evaluation, unavailable checks
and actual failures. Optional review breadth can change; required evidence
continues to govern the affected decision.

The [execution and evidence procedure](.codex/docs/execution-and-evidence.md)
connects acceptance criteria to source, resource, test and build identities.
Automated assertions, rendered observation and human playtests each answer
different questions. A QA plan describes intended checks; results record what
was actually executed and observed.

Use `$define-milestones` to author the game's MVP, Alpha, Beta and Gold criteria
after the slice gate. `$milestone-review` assesses those defined expectations.
`$gate-check` evaluates the applicable workflow outcome; a stage marker or a
document's presence alone does not establish completion.

Release and launch assessments use the identified candidate and requirements.
Delivery, public publication and external communication require the user's
explicit authorization for the relevant operation and destination. See
[release and operations](.codex/docs/release-and-operations.md).

## Hooks and session continuity

The project registers **11 handlers across eight event groups**:

| Event | Handlers | Purpose |
|---|---|---|
| `PreToolUse` | `validate-command-safety.sh`, `validate-commit.sh`, `validate-push.sh` | Inspect selected Bash command patterns, staged resource JSON/content, and literal push context. |
| `PostToolUse` | `validate-skill-change.sh`, `validate-assets.sh` | Remind about changed-skill checks and inspect resource JSON after matching patches. |
| `SubagentStart` | `log-agent.sh` | Record an observed agent start event. |
| `SubagentStop` | `log-agent-stop.sh` | Record an observed agent stop event. |
| `SessionStart` | `session-start.sh` | Supply bounded recovery context and applicable gap discovery. |
| `Stop` | `session-stop.sh` | Record a turn-stop event. |
| `PreCompact` | `pre-compact.sh` | Record available checkpoint and checkout observations. |
| `PostCompact` | `post-compact.sh` | Report recovery availability. |

Gap discovery is called inside SessionStart; it is not a second registered
handler. `hook-lib.sh` supplies shared runtime and path handling. The push
observer does not execute a test suite, and post-edit observations do not undo
edits. These checks supplement the client's effective permission handling.

Authorized continuity work uses bounded checkpoints in
`production/session-state/active.md`. Recovery helps a later session find the
current task and relevant records. Story and QA evidence still establish
completion. Lifecycle logs record actual observed events and stay local.
See the [hook reference](.codex/docs/hooks-reference.md) and
[context-management guide](.codex/docs/context-management.md).

## Parallel work and Git worktrees

When you choose to run independent tasks in separate chats or worktrees, give
each task its scope, starting revision, required inputs and owned files. Shared
checkout writers need non-overlapping ownership. Separate worktrees can carry
their own document changes, which are reconciled during integration.

`$integrate-worktrees` inspects explicitly supplied committed deliveries,
pins their revisions and assesses the target before authorized integration.
Its `--check-only` mode is read-only. A combined revision needs its own relevant
verification even when the source tasks passed separately. The
[worktree workflow](.codex/docs/worktree-workflow.md) explains handoffs and recovery.

The studio follows the active environment's delegation policy. New chats,
cross-chat messages, commits, merges and pushes require the applicable user
authorization; persona definitions and completed tasks do not supply it.

## Customize and maintain

Adapt the project's live choices and requirements first. When a shared skill,
persona or contract needs changing, inspect its inputs, consumers and registered
specification together. Preserve the game's existing work and required reviews.
Use [CONTRIBUTING.md](CONTRIBUTING.md) for changes and
[UPGRADING.md](UPGRADING.md) for merging a newer studio revision into a used project.

`$skill-test` provides read-only static, specification, category and coverage
audit modes. `$skill-improve` supports a demonstrated defect through diagnosis,
repair and revalidation. The [testing framework](<CGS Skill Testing Framework/README.md>)
contains the catalog, specifications and quality rubric.

After preparing the environment, a structural check on Windows is:

```powershell
$studioPython = Join-Path (Get-Location) '.venv/Scripts/python.exe'
$studioGit = (Get-Command git.exe -ErrorAction Stop).Source
$studioBash = Join-Path (Split-Path (Split-Path $studioGit -Parent) -Parent) 'bin/bash.exe'
& $studioPython 'CGS Skill Testing Framework/runtime/check_structure.py' --bash $studioBash
```

The [runtime-check guide](<CGS Skill Testing Framework/runtime/README.md>) lists
the isolated helper suites, selected-group options and their dependencies.
Saved structural results, executable helper results and native client events
are distinct evidence. Run checks appropriate to the change and preserve the
reported limits. Source-project attribution is separate from an update mechanism;
review upgrades against your own project before merging them.

## How Lorsulia differs

[Claude Code Game Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)
provides the original studio structure for Claude Code, and
[ChatGPT Game Studios](https://github.com/Aesma/ChatGpt-Game-Studios/tree/Release-1.3.1)
adapts that approach to Codex. Both emphasize developer decisions and
collaboration. Lorsulia retains a similar structure while organizing its
workflow into four sections: conceptualization, development schematics,
pre-implementation, and implementation.

Its skills, templates, and personas follow that sequence, with explicit steps
for a developer-authored concept, reference-game experience, a shared development
framework, and resource and tool preparation. Required human evaluation remains
part of progression. This arrangement makes preparation and its human
responsibilities explicit, so implementation can follow agreed design choices
and prepared inputs. The [workflow guide](docs/WORKFLOW-GUIDE.md) describes those
steps and their handoffs.

## Troubleshooting

| Symptom | What to check |
|---|---|
| Project skills or personas are missing | Open the repository root itself, start a chat in that project, and check the client's project discovery and trust state. |
| Hooks are present but produce no events | Inspect the active client's hook controls and registered paths. Direct script execution and native event dispatch are separate checks. |
| Python or YAML cannot be loaded | Verify the project `.venv` and declared dependency; use the documented existing-Python fallback when the launcher is unavailable. |
| Bash resolves to WSL on Windows | Select Git for Windows' `bin/bash.exe` as described in INSTALL.md. |
| A gate reports missing evidence | Inspect the specified requirement and actual inputs. A missing game output may be work still to do, rather than a missing studio file. |
| A skill's example does not fit the game layout | Check live technical preferences and actual code/test roots before applying it. |

For interrupted handoffs, follow the
[recovery procedure](.codex/docs/error-recovery-protocol.md) and the existing
project records. Preserve completed work while resolving the missing input.

## Contributing and license

**AI contributor:** Codex (OpenAI) contributed to the studio's workflow, skills,
templates, personas, documentation, and verification under the project author's
direction.

Use the repository's issue and pull-request templates to describe reproducible
problems or proposed changes. Include the affected scope, relevant configuration
and actual checks; keep private game content and credentials out of reports.
See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).

This project retains the upstream MIT license and copyright notice. See
[LICENSE](LICENSE) for the terms and [NOTICE.md](NOTICE.md) for provenance and
the contributions of the source projects and this adaptation.

> <sub><em>Who's Lorsulia?</em></sub>
>
> <sub>Lorsulia is a character in the game Yes, Your Grace. When fate imposes the burden of duty upon her, she willingly accepted, and when tragedy, through no fault of her own, befalls, she stood fast against it and paid the ultimate price. This project is named after her, so that you, whoever's using this, can be reminded of what could happen when you do not possess the power to deny fate and its animosity, and that we can hopefully all be free to shape our own life, with our own endeavour and efforts.</sub>
