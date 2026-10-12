# Installed Skill Reference

Read workflow-catalog.yaml for ordering, manual outcomes and prerequisites. This index lists actual
installed skills; specs define test cases, not passed validation. UI metadata retains invocation policy.

## Analysis

- [$asset-audit](../../.agents/skills/asset-audit/SKILL.md): Audits game assets for compliance with naming conventions, file size budgets, format standards, and pipeline requirements. Identifies orphaned assets, missing references, and standard violations.
- [$balance-check](../../.agents/skills/balance-check/SKILL.md): Analyzes game balance data files, formulas, and configuration to identify outliers, broken progressions, degenerate strategies, and economy imbalances. Use after modifying any balance-related data or design. Use when user says 'balance report', 'check game balance', 'run a balance check'.
- [$code-review](../../.agents/skills/code-review/SKILL.md): Review selected implementation against applicable design, accepted architecture, project standards and actual verification evidence.
- [$consistency-check](../../.agents/skills/consistency-check/SKILL.md): Compare shared facts across scoped GDDs and available entity records; distinguish contradictions, stale registries and missing coverage. Supports full, evidence-based incremental and identity-specific checks.
- [$content-audit](../../.agents/skills/content-audit/SKILL.md): Compare declared content requirements with resource inventory and report missing, invalid or unverified content.
- [$estimate](../../.agents/skills/estimate/SKILL.md): Estimates task effort by analyzing complexity, dependencies, historical velocity, and risk factors. Produces a structured estimate with confidence levels.
- [$perf-profile](../../.agents/skills/perf-profile/SKILL.md): Analyze supplied performance measurements or prepare a scoped capture plan, separating measured bottlenecks from inspection candidates.
- [$scope-check](../../.agents/skills/scope-check/SKILL.md): Analyze a feature or sprint for scope creep by comparing current scope against the original plan. Flags additions, quantifies bloat, and recommends cuts. Use when user says 'any scope creep', 'scope review', 'are we staying in scope'.
- [$security-audit](../../.agents/skills/security-audit/SKILL.md): Assess the selected game security surface and evidence, with actionable findings and explicit unassessed coverage.
- [$tech-debt](../../.agents/skills/tech-debt/SKILL.md): Track, categorize, and prioritize technical debt across the codebase. Scans for debt indicators, maintains a debt register, and recommends repayment scheduling.
- [$test-evidence-review](../../.agents/skills/test-evidence-review/SKILL.md): Review actual automated, manual and human evidence for a story, sprint or system without changing work status.
- [$test-flakiness](../../.agents/skills/test-flakiness/SKILL.md): Identify intermittent test results from comparable runs and maintain explicitly authorized evidence-based recommendations.

## Authoring

- [$architecture-decision](../../.agents/skills/architecture-decision/SKILL.md): Propose, retrofit, or explicitly accept an ADR, checking dependencies and governing stances without inventing approval or story readiness.
- [$art-bible](../../.agents/skills/art-bible/SKILL.md): Author or revise visual direction and applicable asset standards from the developer concept, references and selected project needs.
- [$create-architecture](../../.agents/skills/create-architecture/SKILL.md): Author or revise the master architecture from system designs and the full framework, with explicit ownership, interfaces, decision gaps and evidence.
- [$define-milestones](../../.agents/skills/define-milestones/SKILL.md): Author or update project-defined MVP, Alpha, Beta and Gold expectations, playtest questions and progression criteria.
- [$design-system](../../.agents/skills/design-system/SKILL.md): Author or retrofit a system GDD using full BREAKDOWN and preliminary FRAMEWORK, with explicit behavior, integrations, resource needs and evaluation.
- [$quick-design](../../.agents/skills/quick-design/SKILL.md): Create an independent lightweight design spec for a small tuning change, minor mechanic, or tightly scoped addition.
- [$ux-design](../../.agents/skills/ux-design/SKILL.md): Guided, section-by-section UX spec authoring for a screen, flow, or HUD. Reads game concept, player journey, and relevant GDDs to provide context-aware design guidance. Produces named-screen specifications, design/ux/hud.md, or design/ux/interaction-patterns.md using the studio templates.
- [$ux-review](../../.agents/skills/ux-review/SKILL.md): Validates a UX spec, HUD design, or interaction pattern library for completeness, accessibility compliance, GDD alignment, and implementation readiness. Produces APPROVED / NEEDS REVISION / MAJOR REVISION NEEDED verdict with specific gaps.

## Gate

- [$gate-check](../../.agents/skills/gate-check/SKILL.md): Assess a workflow section or named checkpoint against required outcomes and evidence, with separately authorized stage advancement.

## Pipeline

- [$create-control-manifest](../../.agents/skills/create-control-manifest/SKILL.md): Create or update scoped CONTROL obligations from accepted decisions and explicit project choices, preserving provenance and integer revisions.
- [$create-epics](../../.agents/skills/create-epics/SKILL.md): Group design, framework, resource and tool outcomes into traceable epics; preserve existing stories and indexes.
- [$create-stories](../../.agents/skills/create-stories/SKILL.md): Decompose an epic into bounded stories with genuine prerequisites, applicable governance and criterion-level evidence.
- [$dev-story](../../.agents/skills/dev-story/SKILL.md): Implement a prepared story across code, resources, tools or integration, and verify its applicable criteria without closing the story.
- [$integrate-worktrees](../../.agents/skills/integrate-worktrees/SKILL.md): Integrate delivered commits from independent worktree chats into a target branch, reconcile shared documents, and verify the combined result before promotion. Use across design and implementation phases; check-only reports readiness without changing files or Git state.
- [$map-systems](../../.agents/skills/map-systems/SKILL.md): Create or revise preliminary/full BREAKDOWN and route the next selected system into detailed design.
- [$propagate-design-change](../../.agents/skills/propagate-design-change/SKILL.md): Trace a documented design or framework/resource change into affected decisions, contracts, work and verification, preserving authority and identities.
- [$vertical-slice](../../.agents/skills/vertical-slice/SKILL.md): Build and assess a representative integrated slice, including framework addition and modification and actual human play findings.

## Readiness

- [$story-done](../../.agents/skills/story-done/SKILL.md): Verify a story against actual criterion and review evidence, then close it within existing authorization and synchronize derived status.
- [$story-readiness](../../.agents/skills/story-readiness/SKILL.md): Review whether a story has usable pickup inputs and feasible completion evidence without changing work status.

## Review

- [$architecture-review](../../.agents/skills/architecture-review/SKILL.md): Review architecture coverage, consistency and engine evidence; optionally save stable traceability or produce an RTM within the requested scope.
- [$design-review](../../.agents/skills/design-review/SKILL.md): Review a system design for initial completeness or declared framework/resource integration, using actual evidence and conversational findings.
- [$review-all-gdds](../../.agents/skills/review-all-gdds/SKILL.md): Review related system GDDs for cross-system consistency, design coherence and applicable framework/resource integration, with explicit evidence gaps.

## Sprint

- [$changelog](../../.agents/skills/changelog/SKILL.md): Generate internal and player-facing changelogs from a verified Git range and actual work evidence.
- [$milestone-review](../../.agents/skills/milestone-review/SKILL.md): Assess a defined milestone against actual outcome, quality and human play evidence, with separate schedule-risk analysis.
- [$patch-notes](../../.agents/skills/patch-notes/SKILL.md): Generate player-facing patch notes from git history, sprint data, and internal changelogs. Translates developer language into clear, engaging player communication.
- [$retrospective](../../.agents/skills/retrospective/SKILL.md): Generates a sprint or milestone retrospective by analyzing completed work, velocity, blockers, and patterns. Produces actionable insights for the next iteration.
- [$sprint-plan](../../.agents/skills/sprint-plan/SKILL.md): Create, update or inspect optional sprint subdivisions of defined milestones using real capacity, dependencies and story-owned status.
- [$sprint-status](../../.agents/skills/sprint-status/SKILL.md): Report a selected sprint from authoritative story statuses and actual planning evidence without modifying progress.

## Team

- [$team-audio](../../.agents/skills/team-audio/SKILL.md): Coordinate scoped audio direction, event specifications, resource production and authorized integration.
- [$team-combat](../../.agents/skills/team-combat/SKILL.md): Coordinate the relevant design, implementation and evaluation of a combat feature within the actual game contracts.
- [$team-level](../../.agents/skills/team-level/SKILL.md): Coordinate scoped level or area design, integration and evaluation planning from project requirements.
- [$team-live-ops](../../.agents/skills/team-live-ops/SKILL.md): Orchestrate the live-ops team for post-launch content planning: coordinates live-ops-designer, economy-designer, analytics-engineer, community-manager, writer, and narrative-director to design and plan a season, event, or live content update.
- [$team-narrative](../../.agents/skills/team-narrative/SKILL.md): Coordinate scoped narrative direction, lore and writing with canon, resource and evaluation handoffs.
- [$team-polish](../../.agents/skills/team-polish/SKILL.md): Refine a selected implemented area against supplied milestone goals and observed issues, then verify affected behavior.
- [$team-qa](../../.agents/skills/team-qa/SKILL.md): Coordinate actual QA execution and sign-off for the selected sprint or feature using criterion-level evidence.
- [$team-release](../../.agents/skills/team-release/SKILL.md): Orchestrate the release team: coordinates release-manager, qa-lead, devops-engineer, and producer to execute a release from candidate to deployment.
- [$team-ui](../../.agents/skills/team-ui/SKILL.md): Coordinate UX, presentation and implementation of a selected interface with actual accessibility, input and resource contracts.

## Utility

- [$adopt](../../.agents/skills/adopt/SKILL.md): Audit existing project interfaces and produce a scoped, evidence-based adoption plan.
- [$asset-spec](../../.agents/skills/asset-spec/SKILL.md): Generate visual asset specifications, optional generation prompts, inventories and shared manifest entries from design sources or supplied direction.
- [$brainstorm](../../.agents/skills/brainstorm/SKILL.md): Explore game ideas, experience goals, constraints and research questions to support a developer-authored concept.
- [$bug-report](../../.agents/skills/bug-report/SKILL.md): Record reproducible game defects and verify or close identified bugs using actual evidence and stable IDs.
- [$bug-triage](../../.agents/skills/bug-triage/SKILL.md): Classify and prioritize the actual bug backlog, with evidence-based trends and explicit data limitations.
- [$day-one-patch](../../.agents/skills/day-one-patch/SKILL.md): Prepare a day-one patch for a game launch. Scopes, prioritises, implements, and QA-gates a focused patch addressing known issues discovered after gold master but before or immediately after public launch. Treats the patch as a mini-sprint with its own QA gate and rollback plan.
- [$help](../../.agents/skills/help/SKILL.md): Explain next workflow activities from the actual catalog, outcome evidence and current task.
- [$hotfix](../../.agents/skills/hotfix/SKILL.md): Emergency fix workflow that bypasses normal sprint processes with a full audit trail. Creates hotfix branch, tracks approvals, and ensures the fix is backported correctly.
- [$launch-checklist](../../.agents/skills/launch-checklist/SKILL.md): Complete launch readiness validation covering every department: code, content, store, marketing, community, infrastructure, legal, and go/no-go sign-offs.
- [$localize](../../.agents/skills/localize/SKILL.md): Full localization pipeline: scan for hardcoded strings, extract and manage string tables, validate translations, generate translator briefings, run cultural/sensitivity review, manage VO localization, test RTL/platform requirements, enforce string freeze, and report coverage.
- [$onboard](../../.agents/skills/onboard/SKILL.md): Orient a contributor to an existing role or area using actual project evidence, without writes.
- [$playtest-report](../../.agents/skills/playtest-report/SKILL.md): Prepare or analyze actual playtest records, separating human observations, interpretations and milestone learning.
- [$project-stage-detect](../../.agents/skills/project-stage-detect/SKILL.md): Observe declared workflow section, available outcome evidence and gaps without changing project state.
- [$prototype](../../.agents/skills/prototype/SKILL.md): Build a bounded HTML, engine, paper, or technical-spike experiment and report actual evidence, limitations and retention decisions.
- [$qa-plan](../../.agents/skills/qa-plan/SKILL.md): Author scoped QA plans linking every applicable acceptance criterion to feasible automated, inspection, manual, engine and human evidence.
- [$regression-suite](../../.agents/skills/regression-suite/SKILL.md): Maintain or assess the mapping of critical paths and verified bug fixes to actual regression tests and protocols.
- [$release-checklist](../../.agents/skills/release-checklist/SKILL.md): Generate an internal release readiness checklist from release-scope stories, open bugs, QA evidence, build evidence, and changelog status.
- [$reverse-document](../../.agents/skills/reverse-document/SKILL.md): Recover design, architecture or concept observations from existing implementation while distinguishing evidence, historical intent and unverified behavior.
- [$setup-engine](../../.agents/skills/setup-engine/SKILL.md): Select project engine choices and maintain verified technical preferences and engine references; distinguish configuration documentation from installation or migration.
- [$skill-improve](../../.agents/skills/skill-improve/SKILL.md): Improve a Codex skill with a validate-diagnose-patch-revalidate loop, keeping changes only when structural and behavioral results improve.
- [$skill-test](../../.agents/skills/skill-test/SKILL.md): Validate Codex skills for structural compliance, UI metadata, platform compatibility, behavioral specifications, and catalog coverage. Use for one skill or the complete project skill set.
- [$smoke-check](../../.agents/skills/smoke-check/SKILL.md): Execute a scoped critical-path smoke check with actual configured runners and observations, preserving unavailable coverage.
- [$soak-test](../../.agents/skills/soak-test/SKILL.md): Prepare a reproducible extended-session protocol and analyze supplied observations without implying an unperformed run.
- [$start](../../.agents/skills/start/SKILL.md): Guide new or returning users through the adopted studio workflow and the next relevant activity.
- [$studio-status](../../.agents/skills/studio-status/SKILL.md): Report declared workflow section, current checkout evidence and bounded recovery focus.
- [$test-helpers](../../.agents/skills/test-helpers/SKILL.md): Create runner-compatible test fixtures, assertions and builders from actual system interfaces, or scaffold a selected helper structure.
- [$test-setup](../../.agents/skills/test-setup/SKILL.md): Scaffold missing test infrastructure for the selected project and runner; verify existing work and make CI conditional on the chosen route.
