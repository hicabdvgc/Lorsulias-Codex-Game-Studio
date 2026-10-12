# Director Gates — Shared Review Prompts

These retained identifiers describe review expertise. The installed roster now
includes the installed personas. A gate identifier or installed persona alone does not
establish available expertise, tool access or review evidence. Use an available qualified executor following
[review-workflow.md](review-workflow.md) and [coordination-rules.md](coordination-rules.md).

## Invocation and results

Select prompts relevant to the task and workflow stage. Pass current input paths
or full drafts, their revision/state, the question, scope, and required evidence.
Independent review, when required by the task/procedure, must use an independent
reviewer. Identify any executor fallback. Full/lean/solo settings cannot waive
the approved workflow's required outcomes or human evaluation.

Return `GATE-ID: VERDICT` on the first line, then scope/revision, actual reviewer,
evidence-backed findings, missing/inapplicable checks, and next action. The listed
vocabularies retain their domain meaning. Every gate also accepts `NOT ASSESSED`
when required evidence is unavailable. `NOT APPLICABLE` needs an explicit scope
reason and is allowed only for a check outside the required decision.

Known failures take precedence in a combined result, followed by required
unassessed checks, then concerns, then passing evidence. Keep all findings visible.
Concerns require resolution or the user's documented decision where acceptance is
allowed; accepting a concern cannot waive a hard requirement. Return results in
conversation. Do not write receipts, approve the reviewed artifact, or advance
state unless that distinct action is authorized and its criteria are satisfied.

## Workflow coverage

| Section/checkpoint | Relevant evidence and prompts |
|---|---|
| 1. Conceptualization | Manual concept, reference experience, preliminary/full breakdown, preliminary framework; CD-PILLARS/CD-SYSTEMS, TD-SYSTEM-BOUNDARY/TD-FEASIBILITY as relevant |
| 2. Development Schematics | System GDDs, completed framework, architecture/ADRs/CONTROL, accessibility, resource schema and integration revisions; CD-GDD-ALIGN, TD-ARCHITECTURE/TD-ADR, LP-FEASIBILITY and applicable domain prompts |
| 3. Pre-Implementation | Loose material, formatted resources, specified tools, end-to-end and actual human tests; applicable technical/domain prompts and QL-TEST-COVERAGE |
| 4. Implementation | UX, playable slice, ready work, hard gate, MILESTONE, MVP/Alpha/Beta/Gold playtests, release acceptance and delivery evidence; readiness/completion, PR-MILESTONE, CD-PLAYTEST and relevant phase prompts |

Before production, assess the vertical slice's actual experience, usability,
integration, and demonstrated framework additions/modifications. Missing required
evidence or a known blocking failure prevents passage. Later milestones use
MILESTONE and final acceptance uses RELEASE_CHECKLIST for the delivered build.
No fixed set of four agents, number of criteria, or optional art bible is imposed.

## Creative review prompts

### CD-PILLARS — Pillar Stress Test

**Trigger**: After game pillars and anti-pillars are defined (during brainstorming
or any time pillars are revised)

**Context to pass**:
- Full pillar set with names, definitions, and design tests
- Anti-pillars list
- Core fantasy statement
- Unique hook ("Like X, AND ALSO Y")

**Prompt**:
> "Review these game pillars. Are they falsifiable — could a real design decision
> actually fail this pillar? Do they create meaningful tension with each other? Do
> they differentiate this game from its closest comparables? Would they help resolve
> a design disagreement in practice, or are they too vague to be useful? Return
> specific feedback for each pillar and an overall verdict: APPROVE (strong), CONCERNS
> [list] (needs sharpening), or REJECT (weak — pillars do not carry weight)."

**Verdicts**: APPROVE / CONCERNS / REJECT

---

### CD-GDD-ALIGN — GDD Pillar Alignment Check

**Trigger**: After a system GDD is authored (design-system, quick-design, or any
workflow that produces a GDD)

**Context to pass**:
- GDD file path
- Game pillars (from `design/gdd/CONCEPT.md` or `design/gdd/game-pillars.md`)
- MDA aesthetics target for this game
- System's stated Player Fantasy section

**Prompt**:
> "Review this system GDD for pillar alignment. Does every section serve the stated
> pillars? Are there mechanics or rules that contradict or weaken a pillar? Does
> the Player Fantasy section match the game's core fantasy? Return APPROVE, CONCERNS
> [specific sections with issues], or REJECT [pillar violations that must be
> redesigned before this system is implementable]."

**Verdicts**: APPROVE / CONCERNS / REJECT

---

### CD-SYSTEMS — Systems Decomposition Vision Check

**Trigger**: After the systems index is written by `$map-systems` — validates the
complete system set before GDD authoring begins

**Context to pass**:
- Systems index path (`design/gdd/BREAKDOWN.md`)
- Game pillars and core fantasy (from `design/gdd/CONCEPT.md`)
- Chosen system priorities, if defined at this stage
- Any high-risk or bottleneck systems identified in the dependency map

**Prompt**:
> "Review this systems decomposition against the game's design pillars. Does the
> selected system set collectively deliver the core fantasy? Are there
> systems whose mechanics don't serve any stated pillar — indicating they may be
> scope creep? Are there pillar-critical player experiences that have no system
> assigned to deliver them? Are any systems missing that the core loop requires?
> Return APPROVE (systems serve the vision), CONCERNS [specific gaps or
> misalignments with their pillar implications], or REJECT [fundamental gaps —
> the decomposition misses critical design intent and must be revised before GDD
> authoring begins]."

**Verdicts**: APPROVE / CONCERNS / REJECT

---

### CD-NARRATIVE — Narrative Consistency Check

**Trigger**: After narrative GDDs, lore documents, dialogue specs, or world-building
documents are authored (team-narrative, design-system for story systems, writer
deliverables)

**Context to pass**:
- Document file path(s)
- Game pillars
- Narrative direction brief or tone guide (if exists at `design/narrative/`)
- Any existing lore that the new document references

**Prompt**:
> "Review this narrative content for consistency with the game's pillars and
> established world rules. Does the tone match the game's established voice? Are
> there contradictions with existing lore or world-building? Does the content serve
> the player experience pillar? Return APPROVE, CONCERNS [specific inconsistencies],
> or REJECT [contradictions that break world coherence]."

**Verdicts**: APPROVE / CONCERNS / REJECT

---

### CD-PLAYTEST — Player Experience Validation

**Trigger**: After playtest reports are generated (`$playtest-report`), or after
any session that produces player feedback

**Context to pass**:
- Playtest report file path
- Game pillars and core fantasy statement
- The specific hypothesis being tested

**Prompt**:
> "Review this playtest report against the game's design pillars and core fantasy.
> Is the player experience matching the intended fantasy? Are there systematic issues
> that represent pillar drift — mechanics that feel fine in isolation but undermine
> the intended experience? Return APPROVE (core fantasy is landing), CONCERNS [gaps
> between intended and actual experience], or REJECT [core fantasy is not present —
> redesign needed before further playtesting]."

**Verdicts**: APPROVE / CONCERNS / REJECT

---

### CD-PHASE-GATE — Creative Readiness at Phase Transition

**Trigger**: When creative readiness is relevant to the selected workflow checkpoint

**Context to pass**:
- Target phase name
- List of all artifacts present (file paths)
- Game pillars and core fantasy

**Prompt**:
> "Review the current project state for [target phase] gate readiness from a
> creative direction perspective. Are the game pillars faithfully represented in
> all design artifacts? Does the current state preserve the core fantasy? Are there
> any design decisions across GDDs or architecture that compromise the intended
> player experience? Return READY, CONCERNS [list], or NOT READY [blockers]."

**Verdicts**: READY / CONCERNS / NOT READY

---

## Technical review prompts

Expertise: Architecture, engine risk, performance. The technical-director persona is installed; actual runtime loading is session-dependent.

---

### TD-SYSTEM-BOUNDARY — System Boundary Architecture Review

**Trigger**: After `$map-systems` dependency mapping is agreed but before
GDD authoring begins — validates that the system structure is architecturally
sound before teams invest in writing GDDs against it

**Context to pass**:
- Systems index path (or the dependency map summary if index not yet written)
- Proposed system boundaries and reasons for their separation
- The full dependency graph (what each system depends on)
- Any bottleneck systems flagged (many dependents)
- Any circular dependencies found and their proposed resolutions

**Prompt**:
> "Review this systems decomposition from an architectural perspective before GDD
> authoring begins. Are the system boundaries clean — does each system own a
> distinct concern with minimal overlap? Are there God Object risks (systems doing
> too much)? Does the dependency ordering create implementation-sequencing problems?
> Are there implicit shared-state problems in the proposed boundaries that will
> cause tight coupling when implemented? Do any dependencies contradict the stated system boundaries? Return APPROVE
> (boundaries are architecturally sound — proceed to GDD authoring), CONCERNS
> [specific boundary issues to address in the GDDs themselves], or REJECT
> [fundamental boundary problems — the system structure will cause architectural
> issues and must be restructured before any GDD is written]."

**Verdicts**: APPROVE / CONCERNS / REJECT

---

### TD-FEASIBILITY — Technical Feasibility Assessment

**Trigger**: After biggest technical risks are identified during scope/feasibility
(`$brainstorm` technical-feasibility discussion, `$quick-design`, or any early-stage concept with technical unknowns)

**Context to pass**:
- Concept's core loop description
- Platform target
- Engine choice (or "undecided")
- List of identified technical risks

**Prompt**:
> "Review these technical risks for a [genre] game targeting [platform] using
> [engine or 'undecided engine']. Flag any HIGH risk items that could invalidate
> the concept as described, any risks that are engine-specific and should influence
> the engine choice, and any risks that are commonly underestimated by solo
> developers. Return VIABLE (risks are manageable), CONCERNS [list with mitigation
> suggestions], or HIGH RISK [blockers that require concept or scope revision]."

**Verdicts**: VIABLE / CONCERNS / HIGH RISK

---

### TD-ARCHITECTURE — Architecture Review

**Trigger**: Review the complete architecture draft before accepting governing
decisions or handing it to implementation. Saving an identified draft is allowed.

**Context to pass**: The same full saved or inline draft, applicable GDDs,
FRAMEWORK, requirement links, ADR statuses, and selected-engine evidence.

**Prompt**: Examine whether the design can be implemented with the verified
technical capabilities. Check system boundaries, shared information, resource
consumption, and support for framework additions/modifications. Identify missing
decisions and uncertain claims. Assess applicable requirements, without imposing
a fixed layer arrangement or prerequisite requirement-ID count.

**Verdicts**: APPROVE / CONCERNS / REJECT

---

### TD-ADR — Architecture Decision Review

**Trigger**: After an individual ADR is authored (`$architecture-decision`), before
it is marked Accepted

**Context to pass**:
- ADR file path
- Selected engine version and verified API evidence or explicit uncertainty
- Related ADRs (if any)

**Prompt**:
> "Review this Architecture Decision Record. Does it have a clear problem statement
> and rationale? Are the rejected alternatives genuinely considered? Does the
> Consequences section acknowledge the trade-offs honestly? Is the engine version
> stamped? Are unverified API risks flagged? Does it link to the GDD requirements
> it covers? Return APPROVE, CONCERNS [specific gaps], or REJECT [the decision is
> underspecified or makes unsound technical assumptions]."

**Verdicts**: APPROVE / CONCERNS / REJECT

---

### TD-ENGINE-RISK — Engine Version Risk Review

**Trigger**: When making architecture decisions that touch unverified engine APIs,
or before finalizing any engine-specific implementation approach

**Context to pass**:
- The specific API or feature being used
- Selected engine version and current authoritative API evidence (check the installed engine-reference library against the actual project version)
- Relevant excerpt from breaking-changes or deprecated-apis docs

**Prompt**:
> "Review this engine API usage against the version reference. Is this API present
> in [engine version]? Has its signature, behaviour, or namespace changed relative to the project’s pinned version? Are there known deprecations or documented alternatives?
> Return APPROVE (safe to use as described), CONCERNS [verify before implementing],
> or REJECT [API has changed — provide corrected approach]."

**Verdicts**: APPROVE / CONCERNS / REJECT

---

### TD-PHASE-GATE — Technical Readiness at Phase Transition

**Trigger**: When technical readiness is relevant to the selected workflow checkpoint

**Context to pass**:
- Target phase name
- Architecture document path (if exists)
- Engine reference path
- ADR list

**Prompt**:
> "Review the current project state for [target phase] gate readiness from a
> technical direction perspective. Is the architecture sound for this phase? Are
> all high-risk engine domains addressed? Are performance budgets realistic and
> documented? Are applicable decisions complete enough for the activity being assessed?
> Return READY, CONCERNS [list], or NOT READY [blockers]."

**Verdicts**: READY / CONCERNS / NOT READY

---

## Production review prompts

Available persona: producer. Expertise: scope, timeline, dependencies, production risk.

---

### PR-SCOPE — Scope and Timeline Validation

**Trigger**: A scope proposal or change needs production assessment.

**Context to pass**: Proposed scope, accepted baseline, actual constraints,
dependencies, estimates and their basis; milestone criteria when already defined.

**Prompt**: Compare the proposal with the baseline and supplied capacity. Identify
added work, dependencies, and risks. Explain viable adjustments without making
the user's strategic decision. Unknown capacity prevents a feasibility verdict,
but supported scope differences can still be reported. Do not require MILESTONE
before its authoring step or invent a fallback scope tier.

**Verdicts**: REALISTIC / CONCERNS / UNREALISTIC

---

### PR-SPRINT — Sprint Feasibility Review

**Trigger**: Before finalising a sprint plan (`$sprint-plan`), and after any
mid-sprint scope change

**Context to pass**:
- Proposed sprint story list (titles, estimates, dependencies)
- Supplied available capacity and its units; unknown values remain unassessed
- Current sprint backlog debt (if any)
- Milestone constraints

**Prompt**:
> "Review this sprint plan for feasibility. Is the story load realistic for the
> available capacity? Are stories correctly ordered by dependency? Are there hidden
> dependencies between stories that could block the sprint mid-way? Are any stories
> underestimated given their technical complexity? Return REALISTIC (plan is
> achievable), CONCERNS [specific risks], or UNREALISTIC [sprint must be
> descoped — identify which stories to defer]."

Priority never establishes Ready status. Use actual story Status and criterion-level QA coverage; dependencies ordered for future work may still block pickup. Unknown capacity prevents a feasibility pass.

**Verdicts**: REALISTIC / CONCERNS / UNREALISTIC

---

### PR-MILESTONE — Milestone Risk Assessment

**Trigger**: Assessment of an existing project-defined milestone or changes to it.

**Context to pass**: `production/milestones/MILESTONE.md`, actual completed and
remaining work, required playtest results, dependencies, and applicable schedule evidence.

**Prompt**: Compare the identified version with its stated MVP/Alpha/Beta/Gold
criteria. Identify unmet outcomes and supported schedule risks. Distinguish
forecast confidence from demonstrated completion. Use supplied velocity only
when comparable; do not infer capacity, sprint length, or a statistical distribution.

**Verdicts**: ON TRACK / AT RISK / OFF TRACK

---


### PR-EPIC — Epic Structure Feasibility

**Trigger**: Assess coherent outcome groups before settled story breakdown. Identified
drafts can be saved under existing authorization.

**Context**: Complete epic drafts/index changes, systems and framework operations,
inputs/outputs/dependencies, actual slice findings, applicable governance and supplied
capacity/estimates. Milestone constraints apply when already defined.

**Prompt**: Do boundaries support useful outcomes and dependency order? Does resource,
tool or integration work need its own deliverable? Identify missing prerequisites,
unnecessary coupling and unsupported estimates. Assess schedule feasibility only
with supplied capacity/dates. A missing final MILESTONE does not block epic authoring;
unavailable required evidence leaves the affected assessment unassessed.

**Verdicts**: REALISTIC / CONCERNS / UNREALISTIC

---

### PR-PHASE-GATE — Production Readiness at Phase Transition

**Trigger**: When production readiness is relevant to the selected workflow checkpoint

**Context to pass**:
- Target phase name
- Sprint and milestone artifacts present
- Team size and capacity
- Current blocked story count

**Prompt**:
> "Review the current project state for [target phase] gate readiness from a
> production perspective. Is the scope realistic for the stated timeline and team
> size? Are dependencies properly ordered so the team can actually execute in
> sequence? Are there milestone or sprint risks that could derail the phase during
> the planned work? Return READY, CONCERNS [list], or NOT READY [blockers]."

**Verdicts**: READY / CONCERNS / NOT READY

---

## Visual review prompts

Expertise: Visual identity and resource preparation. The art-director persona is installed.

---

### AD-CONCEPT-VISUAL — Visual Identity Anchor

**Trigger**: When the selected concept or pillars need visual exploration

**Context to pass**:
- Game concept (elevator pitch, core fantasy, unique hook)
- Full pillar set with names, definitions, and design tests
- Target platform (if known)
- Any reference games or visual touchstones mentioned by the user

**Prompt**:
> "Based on these game pillars and core concept, propose 2-3 distinct visual identity
> directions. For each direction provide: (1) a one-line visual rule that could guide
> all visual decisions (e.g., 'everything must move', 'beauty is in the decay'), (2)
> mood and atmosphere targets, (3) shape language (sharp/rounded/organic/geometric
> emphasis), (4) color philosophy (palette direction, what colors mean in this world).
> Be specific — avoid generic descriptions. One direction should directly serve the
> primary design pillar. Name each direction. Recommend which best serves the stated
> pillars and explain why."

**Verdicts**: CONCEPTS (multiple valid options — user selects) / STRONG (one direction clearly dominant) / CONCERNS (pillars don't provide enough direction to differentiate visual identity yet)

---

### AD-ART-BIBLE — Art Bible Sign-Off

**Trigger**: When the requested art bible or visual brief is ready for review; assess the intended activity and scope

**Context to pass**:
- Art bible path (`design/art/art-bible.md`) or sufficient explicit visual brief
- Game pillars and core fantasy
- Platform and performance constraints (from `docs/technical-preferences.md` if configured)
- Visual identity anchor chosen during brainstorm (from `design/gdd/CONCEPT.md`)

**Prompt**:
> "Review this art bible for completeness and internal consistency. Does the color
> system match the mood targets? Does the shape language follow from the visual
> identity statement? Are the asset standards achievable within the platform
> constraints? Does the character design direction give artists enough to work from
> without over-specifying? Are there contradictions between sections? Does the document supply the direction needed by the intended recipient? Return APPROVE (the assessed direction is adequate for the stated scope), CONCERNS [specific
> sections needing clarification], or REJECT [fundamental inconsistencies that must
> be resolved before the affected activity proceeds]."

**Verdicts**: APPROVE / CONCERNS / REJECT

---

### AD-PHASE-GATE — Visual Readiness at Phase Transition

**Trigger**: When visual readiness is relevant to the selected workflow checkpoint

**Context to pass**:
- Target phase name
- List of all art/visual artifacts present (file paths)
- Visual identity anchor from `design/gdd/CONCEPT.md` (if present)
- Art bible path if it exists (`design/art/art-bible.md`)

**Prompt**:
> "Review the current project state for [target phase] gate readiness from a visual
> direction perspective. Is the visual identity established and documented at the
> level this phase requires? Are the right visual artifacts in place? Would visual
> teams be able to begin their work without visual direction gaps that cause costly
> rework later? Are there visual decisions that are being deferred past their latest
> responsible moment? Return READY, CONCERNS [specific visual direction gaps that
> could cause production rework], or NOT READY [visual blockers that must be resolved
> before this phase can succeed — specify the missing outcome or evidence and why it
> matters at this stage]."

**Verdicts**: READY / CONCERNS / NOT READY

---

## Implementation and content review prompts

Use these prompts for the relevant review scope with an available qualified executor.

---

### LP-FEASIBILITY — Implementation Feasibility

**Trigger**: Review the complete architecture draft before accepting governing
decisions or handing it to implementation. Saving an identified draft is allowed.

**Context to pass**: The same full saved or inline draft, applicable GDDs,
FRAMEWORK, requirement links, ADR statuses, and selected-engine evidence.

**Prompt**: Examine whether the design can be implemented with the verified
technical capabilities. Check system boundaries, shared information, resource
consumption, and support for framework additions/modifications. Identify missing
decisions and uncertain claims. Assess applicable requirements, without imposing
a fixed layer arrangement or prerequisite requirement-ID count.

**Verdicts**: FEASIBLE / CONCERNS / INFEASIBLE

---

### LP-CODE-REVIEW — Lead Programmer Code Review

**Trigger**: During completion review by `$story-done`, or as part of `$code-review`. `$dev-story` does not embed this director gate

**Context to pass**:
- Implementation file paths
- Story file path (for acceptance criteria)
- Relevant GDD section
- ADR that governs this system

**Prompt**:
> "Review this implementation against the story acceptance criteria and governing
> ADR. Does the code match the architecture boundary definitions? Are there
> violations of the coding standards or forbidden patterns? Is the public API
> testable and documented? Are there any correctness issues against the GDD rules?
> Return APPROVE, CONCERNS [specific issues], or REJECT [must be revised before merge]."

**Verdicts**: APPROVE / CONCERNS / REJECT

---

### QL-STORY-READY — Work Readiness

**Trigger**: Before a work item is picked up.

**Context to pass**: Existing story or complete draft, intended result, applicable
design/framework/CONTROL references, genuine prerequisites, and completion criteria.

**Prompt**: Check whether the result is clear, required inputs/decisions are
available, and completion can be evaluated by an appropriate method. Include
human judgment where the outcome requires it. A resource/tool to be created is
an output. Future execution evidence is a completion obligation. Missing actual
pickup inputs or an undefined evaluation method must be resolved before pickup.

**Verdicts**: ADEQUATE / GAPS / INADEQUATE

---

### QL-TEST-COVERAGE — Outcome Evidence Review

**Trigger**: Completion, milestone, or final acceptance checks for selected work.

**Context to pass**: Applicable criteria, implemented result/revision, and actual
automated, manual, and human evaluation evidence.

**Prompt**: Map each relevant outcome to evidence, inspect whether it establishes
the expected behavior, and identify omissions or failed results. Cover relevant
resources, tools, framework operations, and integrations. File counts and written
plans cannot establish execution or human experience.

**Verdicts**: ADEQUATE / GAPS / INADEQUATE

---

### ND-CONSISTENCY — Narrative Director Consistency Check

**Trigger**: After writer deliverables (dialogue, lore, item descriptions) are
authored, or when a design decision has narrative implications

**Context to pass**:
- Document or content file path(s)
- Narrative bible or tone guide path (if exists)
- Relevant world-building rules
- Character or faction profiles affected

**Prompt**:
> "Review this narrative content for internal consistency and adherence to
> established world rules. Are character voices consistent with their established
> profiles? Does the lore contradict any established facts? Is the tone consistent
> with the game's narrative direction? Return APPROVE, CONCERNS [specific
> inconsistencies to fix], or REJECT [contradictions that break the narrative
> foundation]."

**Verdicts**: APPROVE / CONCERNS / REJECT

---

### AD-VISUAL — Art Director Visual Consistency Review

**Trigger**: After art direction decisions are made, when new asset types are
introduced, or when a tech art decision affects visual style

**Context to pass**:
- Art bible path (if exists at `design/art/art-bible.md`)
- The specific asset type, style decision, or visual direction being reviewed
- Reference images or style descriptions
- Platform and performance constraints

**Prompt**:
> "Review this visual direction decision for consistency with the established art
> style and production constraints. Does it match the selected art bible or explicit visual brief? Is it achievable
> within the platform's performance budget? Are there asset pipeline implications
> that create technical risk? Return APPROVE, CONCERNS [specific adjustments], or
> REJECT [style violation or production risk that must be resolved first]."

**Verdicts**: APPROVE / CONCERNS / REJECT

---

## Adding a prompt

Add an identifier, trigger, actual context, review question, verdict meanings,
and any special handling only when a consuming procedure needs it. Keep prompts
here and reference their identifiers from consumers. Apply the shared unavailable-
evidence and recovery rules to each new prompt.

## Execution and progression consumers

Apply [execution and evidence](execution-and-evidence.md) and [progression](progression.md) with the existing prompt identifiers. Story completion needs all required criterion evidence; review depth cannot convert required gaps into advisory notes. Slice progression includes actual human findings and framework addition AND modification. Milestone assessments use settled MILESTONE criteria; final acceptance uses the exact delivery checklist/build. Reviews remain conversational unless a bounded save is requested.
