---
name: team-level
description: "Coordinate scoped level or area design, integration and evaluation planning from project requirements."
---

# Team Level

Invoke `$team-level [level name or area to design]`. A target is required; missing target returns usage
without writes or delegation. Reject unknown control flags and ambiguous targets.

## Responsibility and evidence

Select only work needed by the request. Follow the current environment's delegation
policy. Available qualified people/agents can perform the responsibilities below;
roles do not require a fixed team. Identify self-review; preserve required independent
review and actual human evidence under `.codex/docs/review-workflow.md`.

Use existing bounded task authorization. Ask about consequential unresolved choices
or material scope expansion, without per-phase approval prompts. Before concurrent
work, assign one writer per output and keep shared sources read-only for other
executors. The current agent can write within its assigned scope. Re-read shared
records before saving and preserve concurrent changes and stable identities.

Read `.codex/docs/resource-preparation.md`; connect loose material and design outputs
to root RES_TYPE.md, relevant resource_templates/TYPE_TEMP definitions and res_lib/
when defined. Initial content design may record unresolved contracts. Prepared
resources and runtime integration require their actual contracts and evidence.
Use `.codex/docs/tool-development.md` only for a demonstrated unmet tooling need.

## Recovery and result

Read back every promised saved output before reporting delivery. Preserve completed
work if an executor fails. Assign the missing work to a qualified available executor
or mark the dependent activity BLOCKED; never invent the missing result. Report
selected scope, output paths, actual evaluation and remaining dependencies.
COMPLETE applies only to the requested deliverable when all its requirements are
met. A draft can be delivered as a draft; canon acceptance, implemented behavior,
produced media and human/play evaluation require their separate evidence.

## Context and output boundary

Preserve the display name and derive a non-empty safe filename slug. Reject path
separators/traversal. Read the existing target before an update. The default output
is `design/levels/[level-name-slug].md`, using the level-design-document template.
Read developer CONCEPT, relevant GDD/FRAMEWORK decisions, selected accessibility,
visual direction and explicitly related levels/world/narrative content. A missing
required input remains a design dependency; unrelated lore is not mandatory.

## Work sequence

1. **Applicable direction** — establish the area's gameplay purpose and selected
   visual/narrative/world requirements. Narrative-director, world-builder and
   art-director expertise apply where needed. Resolve conflicting directions before
   using them as layout constraints.
2. **Layout and navigation** — level design follows the selected traversal model,
   landmarks, pacing, encounters and entry/exit connections. Critical paths, secrets,
   combat and puzzles are conditional. Resolve adjacent areas by exact identity and
   inspect reciprocal connections. Missing areas remain UNRESOLVED; do not invent them.
3. **Systems integration** — link actual mechanics, encounter/reward formulas,
   resources, dependencies and framework operations. Use supplied units, targets and
   constraints. Systems-designer can support the relevant interactions.
4. **Presentation and accessibility** — specify location-specific visual/audio needs,
   shared versus unique resources, sight lines and applicable accessibility responses.
   Evaluate against docs/ACCESSIBILITY.md and actual player tasks; do not impose a
   universal simultaneous-state limit. Required unresolved concerns block the affected
   design conclusion. Recheck corrections against the final candidate.
5. **Evaluation planning** — include feasible checks for traversal, boundaries,
   sequence breaks, softlocks, accessibility and experience as applicable. `qa-tester`
   is available; `$qa-plan` and qa-lead support the bounded plan
   with an available qualified executor. Planning is separate from executing a playtest.

Compile the relevant results in the one level document, including open dependencies
and its QA/Acceptance section. Separate standalone narrative/resource/code outputs
require their own inclusion in the authorized task. COMPLETE describes the scoped
design deliverable; Graybox, Art Pass, Polish or Final require supporting project
stage evidence. `$dev-story` is installed; `$qa-plan` is installed for scoped evidence planning.
