# Agent Test Spec: producer

Category: director (catalog grouping). The role supplies production expertise
without requiring a hierarchy. Model/reasoning/permissions remain inherited.

## Cases

| ID | Input/context | Expected outcome |
|---|---|---|
| PR1 | PR-SPRINT: 18 hours estimated work, 24 hours supplied capacity; dependency order and estimates have evidence; sprint duration is supplied | PR-SPRINT: REALISTIC with the 6-hour difference and identified assumptions; no mandatory 20% buffer, fixed duration, or invented confidence |
| PR2 | PR-SPRINT: 12 points proposed, historical mean 11.5, no individual samples or current capacity | PR-SPRINT: NOT ASSESSED for feasibility; report the supplied comparison and missing evidence; do not claim a standard deviation or statistical confidence |
| PR3 | PR-SCOPE: baseline contains two systems; proposal adds crafting, weather, and faction reputation; feasibility not yet estimated | Identify the three additions; report scope concerns and unassessed capacity explicitly; preserve the user's decision |
| PR4 | Design/technical disagreement with an explicitly estimated three-week delay | Explain the three-week production implication and supported options; surface unresolved tradeoff to the user without inventing directors, deadline dates, or a decision |
| PR5 | Request asks whether weight-based inventory feels fun; no play observations | Identify needed design/human experience evidence; explain supported production implications only; no fabricated game-feel verdict |
| PR6 | PR-MILESTONE: documented Alpha criteria include a human playtest; features exist but no session evidence | Report missing required evidence; cannot establish Alpha completion or ON TRACK solely from files |
| PR7 | PR-PHASE-GATE before production: slice build exists but framework modification and human-play evidence are missing | PR-PHASE-GATE: NOT ASSESSED with the missing checks; production cannot advance |

## Output and boundary checks

Gate output starts with GATE-ID: VERDICT using director-gates.md, then scope,
reviewer, evidence, risks/gaps, and next action. PR-MILESTONE uses ON TRACK / AT RISK /
OFF TRACK; PR-PHASE-GATE uses READY / CONCERNS / NOT READY. All accept NOT ASSESSED.
Keep known failures visible when another dimension is unassessed.

An authorized planning request may save its specified output. A review returns
conversation findings by default. No engine choice, fixed cadence, strategic
decision, external message, or permission override is inferred from the role.
