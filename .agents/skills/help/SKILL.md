---
name: help
description: Explain next workflow activities from the actual catalog, outcome evidence
  and current task.
---

# Studio Help

Invoke `$help [what you finished or where you are stuck]`. This skill is read-only.

Read `.codex/docs/workflow-catalog.yaml`, `.codex/docs/progression.md`, live
`docs/technical-preferences.md` and relevant current artifacts. The four section IDs are
conceptualization, development-schematics, pre-implementation, implementation. Report the declared
section separately from available outcomes and missing prerequisites. Preserve unknown/legacy stage
values until their interpretation is explicitly resolved; counts/existence cannot establish progress.
Story Status fields own progress; selected sprint YAML is derived. Active scope needs an explicit or
unique existing reference, never modification time. There is no review-mode file to create.

## Read the installed workflow

The catalog has phases with steps, completion outcomes, execution, optional artifact path/purpose/maturity,
available_support and pending_support. Read the actual keys and declared outcomes.
Inspect `.agents/skills/*/SKILL.md` for additional installed capabilities. Distinguish installed from
pending and manual activities. Use the artifact observer only for bounded discovery; absence or presence
does not settle maturity. Read relevant outcomes rather than checking boxes from paths.

Read bounded focus with the shared session-state parser described in context-management.md. Report
unavailable/malformed state without guessing. Inspect selected story statuses directly and report any
derived sprint disagreement. Missing active sprint means unknown, not the newest sprint.

## Explain the next activity

Show declared section, established outcomes with evidence, work in progress, required next outcomes,
optional installed support and unresolved dependencies. Identify manual developer authorship/reference
play/human testing. A suggested work candidate is not automatically Ready. Required independent and
human evidence cannot be waived by optional review breadth.

Use `$project-stage-detect` for deeper outcome gaps, `$adopt` for interface compatibility,
`$gate-check` for assessment and `$onboard` for role orientation. Near a gate, state its outstanding
requirements; never advance a stage. HELP COMPLETE describes guidance, not workflow completion.
