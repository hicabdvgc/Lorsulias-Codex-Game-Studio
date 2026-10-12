---
name: gate-check
description: Assess a workflow section or named checkpoint against required outcomes
  and evidence, with separately authorized stage advancement.
---

# Gate Check

Invoke as `$gate-check`. Arguments: `[conceptualization | development-schematics | pre-implementation | implementation | vertical-slice | MVP | Alpha | Beta | Gold | final-acceptance] [--review full|lean|solo]`.

Read [.codex/docs/execution-and-evidence.md](../../../.codex/docs/execution-and-evidence.md) for authorization, status, criterion-level evidence, review and recovery contracts. Read the relevant sources before editing.


Read `.codex/docs/progression.md`, the workflow catalog, director gates and this skill's CONTRACT.md.
Resolve one selector from the request or unambiguous declared phase. Unknown/ambiguous/legacy names
need interpretation; reject malformed options. A requested phase differing from the declared phase
can receive a clearly labeled scoped assessment; it cannot silently move the marker past prerequisites.

## Required outcome assessment

- Conceptualization: developer-authored concept, real reference study evidence, MDA/engine feasibility,
  preliminary/full breakdown progression and preliminary framework outcomes from the catalog.
- Development schematics: relevant system designs, full FRAMEWORK, reviewed architecture, accepted
  governing decisions, scoped integer CONTROL, accessibility commitments and selected resource contracts.
- Pre-implementation: applicable prepared resources, tool library/workflows, executed end-to-end and
  actual intended-user evaluation. Missing real required inputs remain gaps.
- Implementation: assess its catalog outcomes, including slice, prepared work, milestones, playtests,
  final acceptance and authorized delivery outcomes. A partial checkpoint is not whole-section completion.
- Vertical-slice: actual integrated playable path, experience/usability and framework addition AND
  modification evidence, followed by prepared work/readiness. Final MILESTONE is the next output and
  is not a circular prerequisite. Missing human or required independent evidence blocks progression.
- MVP/Alpha/Beta/Gold: use the corresponding settled MILESTONE criteria and actual relevant playtests.
- Final-acceptance: use the supplied RELEASE_CHECKLIST and exact delivery build. Release authoring/
  shipping orchestration uses installed $team-release and release-and-operations.md; this assessment does not ship.

The artifact observer is optional discovery support. Inspect contents and applicable maturity;
file presence never satisfies quality, integration or human outcomes. Match evidence to revision
and scope, inspect contradictions and cross-document dependencies, and preserve required failures
when other checks cannot run. Select relevant creative/technical/production/visual/QA expertise
using director-gate identifiers and current delegation policy. Do not require an irrelevant panel
or let a missing required reviewer pass. Depth only changes optional breadth.

## Required continuation

Read and follow [assessment and advancement](references/continued-workflow.md) to report the result,
resolve consequential decisions and handle an explicitly authorized stage-marker write.
