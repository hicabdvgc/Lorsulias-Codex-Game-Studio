# Workflow Progression

Read [workflow catalog](workflow-catalog.yaml), [director gates](director-gates.md),
[execution and evidence](execution-and-evidence.md) and the selected milestone requirements.
The catalog owns required outcomes; installed support does not remove manual responsibilities.

## Declared section and assessment

production/stage.txt, when present, declares one of: conceptualization,
development-schematics, pre-implementation, implementation. These are the four catalog
phase IDs, in that order. Missing/unknown/legacy values are unresolved declarations;
preserve them until the intended mapping is explicitly settled. The marker is not proof
of completion. Do not create a game stage marker while adapting the studio skeleton.

`$project-stage-detect` observes the declaration, current work and outcome evidence.
`$gate-check` accepts a canonical phase ID or vertical-slice, MVP, Alpha, Beta, Gold,
final-acceptance. Without a selector, resolve the intended gate from explicit task context
or the declared phase; ask when ambiguous. Assessment is read-only by default. Checkpoint
results stay within implementation and do not invent additional phase values.

For each applicable requirement, identify source, evidence, result and missing work.
PASS requires all required outcomes/evidence. CONCERNS means only advisory issues remain.
FAIL records a demonstrated required failure. NOT ASSESSED identifies unavailable required
evidence; retain failures alongside gaps. Neither missing evidence nor a required failure
can be waived by selecting a shallower review or accepting a concern. Required independence
and human use apply with every executor. An explicitly authorized advancement may update
the marker to the catalog's next_phase after a passing assessment. Re-read the marker and
relevant evidence before writing; report concurrent changes. No next_phase means no marker
advance. Release actions need their own authorization.

## Implementation checkpoints

1. Specify relevant UX, build a coherent playable vertical slice from actual designs,
   FRAMEWORK and prepared resource/tool contracts. The slice may use bounded implementation
   tasks before epics/stories exist; it does not require final MILESTONE definitions.
2. Use slice experience to prepare epics/stories and assess pickup readiness.
3. Assess the vertical-slice hard gate: actual playable integrated systems, intended
   experience and usability, relevant resource/tool use, and demonstrated framework-based
   addition AND modification with affected-system checks. Actual human findings are required.
   Missing evidence blocks progression to milestone production. Document PROCEED/PIVOT/KILL
   recommendations without inventing a developer decision or fixed numerical thresholds.
4. Finalize production/milestones/MILESTONE.md through `$define-milestones`. Earlier drafts
   identify missing gate evidence and are not settled production definitions.
5. Build and human-playtest project-defined MVP, Alpha, Beta and Gold. `$milestone-review`
   evaluates the selected stage's scope, learning goals, quality and progression criteria.
   Dates, budgets, capacity and sprints apply only when selected. Story counts cannot prove
   that the milestone experience works.
6. Assess final acceptance against production/releases/RELEASE_CHECKLIST.md and the exact
   delivery build. Use installed $release-checklist/$launch-checklist and the release-and-operations.md contract;
   $team-release consumes matching persisted READY reports and applicable final-acceptance evidence. Passing assessment does not ship the build.

Artifact observers only report declared-path discovery. A preliminary and a full document
can occupy the same path; maturity requires inspecting content and evidence. Manual activities
without catalog artifact paths stay visible and require actual outcomes, not invented globs.
