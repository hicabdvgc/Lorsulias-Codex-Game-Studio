# Lorsulia's Codex Game Studio

A reusable game-development studio for Codex, with 76 skills, 49 personas,
document templates, project guidance, and observation helpers.

This studio is a follow-up adaptation of
[ChatGPT Game Studios (Release 1.3.1)](https://github.com/Aesma/ChatGpt-Game-Studios/tree/Release-1.3.1)
and [Claude Code Game Studios](https://github.com/Donchitos/Claude-Code-Game-Studios).
It retains a very similar project structure while introducing a different
workflow and corresponding skills, templates, and personas that emphasize human
involvement in preparation. The developer authors the game concept, supplies
reference-game experience, and participates in design decisions and evaluation
before implementation. See [NOTICE.md](NOTICE.md) for the project's lineage and
attribution.

## Start a project

**READ THE WORKFLOW GUIDE FIRST!**

1. Follow [INSTALL.md](INSTALL.md) to install the entire folder as a project,
   prepare its runtime, and activate skills, personas, and hooks in Codex.
2. Open this directory as your project root and read [AGENTS.md](AGENTS.md).
3. Use `$start` for orientation, `$help` for the next activity, `$adopt` for an
   existing project, or `$onboard` for contributor context.
4. Record selected engine, language, platforms, and conventions in
   [live technical preferences](docs/technical-preferences.md).

Follow the [complete workflow guide](docs/WORKFLOW-GUIDE.md) for all 59 activities,
their procedures, studio support, outputs, and handoffs. The
[activity catalog](.codex/docs/workflow-catalog.yaml) indexes the same four sections: conceptualization,
development schematics, pre-implementation, and implementation. The developer
authors CONCEPT and supplies actual reference-game play. Human evaluation,
required independent reviews, and the vertical-slice hard gate govern progression.
Engine reference libraries support technical work; engines and services are
selected and configured for each game.

## Project organization

| Location | Use |
|---|---|
| `.agents/skills/` | Reusable workflow instructions, metadata, and supporting files. |
| `.codex/agents/` | Persona definitions for the available responsibilities. |
| `.codex/docs/` | Shared procedures, catalogs, and reusable templates. |
| `.codex/hooks/`, `.codex/scripts/`, `.codex/rules/` | Runtime helpers, observations, and command policy. |
| `design/`, `docs/`, `game_ref/` | Game design, technical decisions, and reference studies. |
| `resource_templates/`, `res_lib/`, `tools_lib/` | Per-type contracts, prepared resources, and selected development tools. |
| `src/`, `assets/`, `tests/`, `tools/`, `prototypes/` | Project code, assets, tests, tooling, and experiments; actual roots follow the selected engine. |
| `production/` | Work items, milestones, QA, playtests, release records, and session continuity. |
| `CGS Skill Testing Framework/` | Specifications and reusable checks for customizing the studio. |

Use the [directory and artifact contracts](.codex/docs/directory-structure.md)
for authoritative document locations, maturity, and handoffs.

## Customize and maintain

Use `$skill-test` to inspect skill/specification coverage and `$skill-improve`
for a bounded repair. The [testing framework](<CGS Skill Testing Framework/README.md>)
also supplies isolated runtime checks. Read [CONTRIBUTING.md](CONTRIBUTING.md)
and [UPGRADING.md](UPGRADING.md) before changing shared components.

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

See [NOTICE.md](NOTICE.md) and [LICENSE](LICENSE) for attribution and terms.

> <sub><em>Who's Lorsulia?</em></sub>
>
> <sub>Lorsulia is a character in the game Yes, Your Grace. When fate imposes the burden of duty upon her, she willingly accepted, and when tragedy, through no fault of her own, befalls, she stood fast against it and paid the ultimate price. This project is named after her, so that you, whoever's using this, can be reminded of what could happen when you do not possess the power to deny fate and its animosity, and that we can hopefully all be free to shape our own life, with our own endeavour and efforts.</sub>
