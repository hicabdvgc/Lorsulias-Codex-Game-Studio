# Lorsulia's Codex Game Studio — Complete Workflow Guide

This guide explains the complete four-section game-development procedure: what
to do, what to carry forward, which studio components can help, and what evidence
is needed before proceeding. It retains all 59 activities and the procedural
instructions of the Lorsulia workflow. The [activity catalog](../.codex/docs/workflow-catalog.yaml)
indexes those activities for navigation and checks. The source numbering skips
2.1.2; this guide preserves that numbering without adding an activity.

## How to use this guide

Begin with the [installation guide](../INSTALL.md) and open the game-project root.
Use `$start` for orientation, `$help` to identify the next relevant activity, and
`$studio-status` to inspect the current project. For existing work, `$adopt`
compares the actual project with these interfaces; preserve its existing evidence
and resolve the applicable entry point.

Read each activity's procedure and studio handoff together. Linked skills provide
their actual invocation syntax and detailed execution rules. The named skills are
available support; activities described as direct work remain part of the workflow
even when there is no dedicated skill. The developer makes game decisions, authors
CONCEPT, plays reference games, and supplies required human evaluations. An agent
can assist applicable research, authoring, implementation, and review within the
authorized task and available tools.

All artifact paths in prose are relative to the game-project root. A template is
an authoring aid; create the game's actual document at its stated destination.
Future game outputs may be absent in a newly installed studio. Follow the
[directory contracts](../.codex/docs/directory-structure.md) for authoritative
locations, document maturity, and shared identifiers.

### Procedure map

| Section | Work in order | Handoff |
|---|---|---|
| [1. Conceptualization](#section-1) | Concept → reference-game studies → preliminary system breakdown → developmental framework principles → full breakdown and preliminary framework. | Developer-authored CONCEPT, actual studies, Full BREAKDOWN, and Preliminary FRAMEWORK. |
| [2. Development Schematics](#section-2) | System designs and integration principle → full framework → architecture, ADRs, CONTROL, accessibility → resource schema → four GDD revision passes. | Connected system designs, governing technical decisions, and usable resource contracts. |
| [3. Pre-Implementation](#section-3) | Loose material → type-specific formatting → resource library → selected tool development → end-to-end and human tool tests → tool library. | Prepared resources and usable tools, with actual evaluation evidence. |
| [4. Implementation](#section-4) | UX → playable slice → epics/stories and readiness → slice hard gate → milestone definitions → MVP/Alpha/Beta/Gold with playtests → final acceptance → release and maintenance. | Verified milestone outcomes, the assessed release candidate, and actual delivery evidence. |

The detailed groups are:

- [1.1 Concept](#group-1-1), [1.2 Reference studies](#group-1-2), [1.3 System breakdown](#group-1-3), and [1.4 Developmental framework](#group-1-4).
- [2.1 System design](#group-2-1), [2.2 Architecture and technical setup](#group-2-2), [2.3 Resource schema](#group-2-3), and [2.4 GDD revision](#group-2-4).
- [3.1 Loose files](#s3-1), [3.2 Resource formatting](#group-3-2), and [3.3 Tool development](#group-3-3).
- [4.1 Pre-production](#group-4-1), [4.2 Production](#group-4-2), [4.3 Final acceptance](#group-4-3), and [4.4 Release](#group-4-4).
- [Working across activities](#working-across-activities) explains story execution, review, changes, continuity, and supporting capabilities.

### Maturity and progression

Preliminary and Full BREAKDOWN share `design/gdd/BREAKDOWN.md`; Preliminary and
Full FRAMEWORK share `docs/FRAMEWORK.md`. Mark their maturity in their contents.
The existence of either file does not establish its maturity. Initial system
design uses Full BREAKDOWN and Preliminary FRAMEWORK. Complete FRAMEWORK using
those designs; then perform the later architecture/resource integration work.

The vertical slice can be built through bounded implementation tasks before
epics and stories exist. Use its experience to prepare work, assess readiness,
and pass the hard gate before final milestone authoring. A tool or resource being
created is an output of its task; require the specifications and source inputs
needed to create it without making its own future output a prerequisite.

Use the [progression procedure](../.codex/docs/progression.md) when assessing a
section or implementation checkpoint. A section declaration in `production/stage.txt`
is separate from completion evidence. The four section IDs are `conceptualization`,
`development-schematics`, `pre-implementation`, and `implementation`; release and
post-launch work remain within Implementation. Required unavailable evidence and
required failures prevent a passing decision. Human evaluation and required review
independence retain their force regardless of executor or review-depth setting.

<a id="section-1"></a>

## Section 1. Conceptualization

Work from the developer’s interests and commitments toward a studied, decomposed concept and a preliminary development procedure. Reference-game experience and framework design are explicit activities in this section.

<a id="group-1-1"></a>

### 1.1. Concept

<a id="s1-1-1"></a>

#### 1.1.1. Brainstorming

- Begin with an idea. What interests you, as a developer, the most? What exites you when you play games? What's a topic you really like and how can it be developed into a full game?

**Studio handoff.** Use `$brainstorm` to explore the developer's interests, intended experience, constraints, and uncertainties. Its output prepares decisions for the developer's own concept writing. Read existing decisions first; concept options and open questions belong in the working discussion or an explicitly requested research record.

**Available support:** [`$brainstorm`](../.agents/skills/brainstorm/SKILL.md).

<a id="s1-1-2"></a>

#### 1.1.2. Record basic design choices

- Write down the basic things that this game would feature, such as what type of a game it would be, would it be real-time or turn-based, would it be online or offline, etc.

**Studio handoff.** Record the choices the developer has actually made and identify undecided choices. Carry them into CONCEPT; keep engine, language, platform, and root selections in live `docs/technical-preferences.md` when selected. `$setup-engine` supports those technical choices without assuming or installing an engine.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="s1-1-3"></a>

#### 1.1.3. Record constraints and commitments

- What would the game absolutely NOT contain? What don't you want in the game? What are some requirements about the game or the game design process?

**Studio handoff.** Carry exclusions, commitments, and development constraints into the developer-authored concept. Later design, architecture, milestones, and release checks need to be able to identify those commitments. Resolve contradictions with the developer before treating a constraint as settled.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="s1-1-4"></a>

#### 1.1.4. Prepare supporting documentations

- Don't begin designing the game right away. Read, watch, and collect relevant materials and background information before doing any work. For instance, if you want a game based on a historical period, you may as well write a summary of relevant historical works to get yourself informed about relevant issues. Don't just daydream and expect to get any work done!

**Studio handoff.** Collect relevant sources and distinguish what a source establishes from a proposed interpretation for the game. Keep the material identifiable for subsequent concept and design work. The reference-game-study template becomes useful for the game-specific studies in 1.2; other background material can use a format suited to its subject.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="s1-1-5"></a>

#### 1.1.5. Produce CONCEPT.md (manually!)

- Write the CONCEPT.md document, in which a basic design document is written for the game. This document MUST be written by the developers manually! It is important for the developer to actually know what they want for the game, and be able to articulate it in a natrual manner.

**Studio handoff.** The developer writes `design/gdd/CONCEPT.md`. The [concept template](../.codex/docs/templates/game-concept.md) can help organize their decisions. AI research, questions, or review do not substitute for the developer's authorship or silently overwrite this document. Carry the concept and unresolved questions into reference studies and system analysis.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="group-1-2"></a>

### 1.2. Reference Game Case Study

<a id="s1-2-1"></a>

#### 1.2.1. Identify games for reference

- Don't even think about building something from your dreams. It is unthinkably more effective to find some existing games within the genre you're working with and play them, study their game design, and then think about what you're going to build.

**Studio handoff.** Choose references in relation to the proposed genre, interactions, presentation, or other questions in CONCEPT. Explain what each game can help investigate. The selection supports actual play in the next activity; a title list alone does not establish that the games were studied.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="s1-2-2"></a>

#### 1.2.2. Play reference games and conduct case studies (with a consistent framework at hand)

- Again, talking to AI may get ideas in your head, but it's not possible to give you the experience of playing a game, which is exactly what your consumer will do once you finish and release the game. If a developer don't even play games and learn from them, the only thing they can create are low-effort slops that no one would really care to spend time with. As you play these reference games, much as scholars read academic papers, you should take notes of their features, what they include as game contents and mechanics, how are things presented, how is the in-game economy system designed, etc. You should put things together as a case study file, written in a coherent framework for every game you have played and analyzed. You can also take screenshots, record videos and audios, and write down specific, supplementary things that you think is worth taking notes of.

**Studio handoff.** Use the [reference-game-study template](../.codex/docs/templates/reference-game-study.md) consistently. The developer supplies actual observations and collected evidence. Distinguish observed behavior, externally sourced facts, and hypotheses about how the game works. Connect the study to questions about mechanics, interactions, presentation, economy, or other relevant features.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="s1-2-3"></a>

#### 1.2.3. Produce game_ref/ (a library of all the reference case studies)

game_ref/
		GAME1.md (case study files for each game you have studied)
		game1/ (additional evidence collected like screen shots, sound & visual effects, UI/UX decomposition, etc.)
		GAME2.md
		game2/
- Here, you want to assemble the case studies they have done under a folder within the root directory, so that not only you but also AIs can read and view them.

**Studio handoff.** Keep each study in root `game_ref/`, with its related screenshots, recordings, and notes in an identifiable evidence folder. Preserve links between each conclusion and its evidence. The studies become inputs to breakdown, design, resource direction, and UX; readers should be able to locate the relevant observation.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="group-1-3"></a>

### 1.3. System Breakdown

<a id="s1-3-1"></a>

#### 1.3.1. Analyze the game concept with the MDA framework

- First, take you CONCEPT.md document, analyze it with an established framework - the Mechanic, Dynamic and Aethetics framework, how could the game be designed in a way that satisfies requirements on all 3 fronts?

**Studio handoff.** Work from the developer's CONCEPT. Identify intended mechanics, the interactions they may produce over play, and the experience those interactions should create. Keep unresolved causal assumptions visible so the preliminary breakdown and any selected prototype can address them. Carry the analysis into the decomposition in 1.3.4.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="s1-3-2"></a>

#### 1.3.2. Analyze the game concept with reference game case studies

- Secondly, think about the games you have played. Have they implemented similar things that you want in your game? What difficulty do you forsee those game's developers have to overcome to deliver those results? How can you potentially do the same, but with your own taste and style in it?

**Studio handoff.** Compare the concept with the actual `game_ref/` studies. Separate demonstrated examples from inferred implementation difficulties and proposed variations. Explain what the proposed game would keep, adapt, or investigate, and carry relevant uncertainties into system boundaries and framework choices.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="s1-3-3"></a>

#### 1.3.3. Analyze the game concept with development docs of the engine

- Then, there's the practical constraint of what can and cannot be achieved with a given platform. Think about something that you want most, what you think could be discarded, what weights more than others, and what the engine of your choosing allows you or doesn't allow you to do.

**Studio handoff.** Use the selected engine's relevant, verified documentation and live technical preferences. The [engine reference library](engine-reference/README.md) is supporting material; check the actual selected version for a consequential claim. Record constraints, tradeoffs, and unresolved feasibility questions that affect the desired systems.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="s1-3-4"></a>

#### 1.3.4. Produce BREAKDOWN.md (preliminary) (breakdown of the game's systems)

- Finally, decompose the game you intend to design into several inter-connected systems, e.g., the map, economy, enemy AI, visual effects, etc. Write what each system would handle, and, crucially, why it is necessary to make them as standalone game systems, rather than a part of something else. At this moment, it might not be possible for you to have a concrete idea of what the game is about, and that's fine! What you create here should be a preliminary version of the BREAKDOWN.md document, something that you can work with without having to delve deeper without anything to return to, instead of an actual, full realization of it.

**Studio handoff.** Use `$map-systems` for the preliminary decomposition. It writes `design/gdd/BREAKDOWN.md` using the [systems-index template](../.codex/docs/templates/systems-index.md), with owned behavior, inputs/outputs, dependencies, and reasons for separate boundaries. A new breakdown starts Preliminary; FRAMEWORK is still being developed. Carry that system inventory into 1.4.

**Available support:** [`$map-systems`](../.agents/skills/map-systems/SKILL.md).

<a id="group-1-4"></a>

### 1.4. Developmental Framework

<a id="s1-4-1"></a>

#### 1.4.1. Develop an overall outlook of the framework

- The developmental framework is an over-reaching instrument that will guide you throughout the development procedure. It exist to enable easy integration of new contents, modifications of existing ones, allowing you to check what you have done, validate process, and potentially transform of what you have done into something else. Without it, expanding the game would look like throwing spaghetti at the wall - you might hit something, you might miss something, but you're definetly not working in an effective and disciplined way. The framework can exist like this, as a document guiding work procedures, or an executable file, or something else, but it must exist, so that it's possible to build and polish something in a long run.

**Studio handoff.** Develop the framework's purpose using CONCEPT and Preliminary BREAKDOWN. Describe how development will support content additions, mechanic additions, presentation work, modifications, validation, and framework revision as applicable. The [framework template](../.codex/docs/templates/development-framework.md) provides an authoring structure; concrete procedures are decided for this game.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="s1-4-2"></a>

#### 1.4.2. Develop sub-components (e.g., content expansion, mechanics addition, visual & audio artifact presentation, etc.) of the dev framework

- Think about how, in the long run, will you be maintaining the game. Will you develop it iteratively? Will you do the mechanics once and leave it there? When do you fall back to edit the framework itself? Or will you do something else in the process of development?

**Studio handoff.** Work out each relevant development route: what initiates the work, which inputs it uses, which systems/resources it affects, how it is checked, and where the result goes. Decide when an existing route is sufficient and when the framework itself needs revision. Preserve uncertainties for the system-design stage to resolve.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="s1-4-3"></a>

#### 1.4.3. Develop an over-reaching work principle

- Put the different subcomponents together to form the actual workable developmental framework. Again, this can be as simple as one md document, or it could be a seperate design tool that you build to track process and modify existing or new things.

**Studio handoff.** Combine those routes into a working principle that explains how related changes travel through the game. Resolve conflicts between sub-components and make their handoffs understandable. If a tool or executable participates in the framework, describe its responsibility and the surrounding human/development procedure.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="s1-4-4"></a>

#### 1.4.4. Produce BREAKDOWN.md (full)

- Think about how different game systems would work and be developed with this framework in mind - and compelte the BREAKDOWN.md document.

**Studio handoff.** Revisit the whole system inventory using the framework principles. Use `$map-systems` with an explicit request for Full maturity, retaining stable system identities and valid prior analysis. Full BREAKDOWN explains the connected system boundaries and their development routes; later detailed GDDs remain outputs of Section 2.

**Available support:** [`$map-systems`](../.agents/skills/map-systems/SKILL.md).

<a id="s1-4-5"></a>

#### 1.4.5. Produce FRAMEWORK.md (preliminary) 

- Put everything together, and produce a preliminary version of the development framework document - should it come as an md file.

**Studio handoff.** Write `docs/FRAMEWORK.md` with explicitly Preliminary maturity using the framework template. It brings together the decisions from 1.4.1–1.4.3 and links them to Full BREAKDOWN. Hand both documents to system design. Completion of FRAMEWORK's actual system-specific procedures follows initial GDD authoring in 2.1.5.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

### Handoff to Development Schematics

Carry forward the developer-authored CONCEPT, actual reference studies and evidence,
MDA and relevant engine findings, Full BREAKDOWN, and Preliminary FRAMEWORK. Assess
the section with `$gate-check conceptualization` when a progression decision is
needed. Resolve the missing required outcome identified by that assessment; an
existing filename or a summary of intended research does not complete the work.

<a id="section-2"></a>

## Section 2. Development Schematics

Use Full BREAKDOWN and Preliminary FRAMEWORK to design the connected systems, then complete FRAMEWORK and develop their technical and resource contracts. Finish with the four distinct GDD revision passes.

<a id="group-2-1"></a>

### 2.1. System Design

<a id="s2-1-1"></a>

#### 2.1.1. Design Game Development Documents for each of the systems in BREAKDOWN.md

- Take each system in BREAKDOWN.md and work out how it should actually function. What does it do, what rules does it follow, and what does it need from other systems? Think through the player's interactions, the results they produce, and the resources needed to make them possible. Keep the developmental framework in mind: how would you add something to this system later, or change something already in it? Work these questions into the design while you are deciding how the system works.

**Studio handoff.** Use `$design-system <system-name>` for a named entry in Full BREAKDOWN, with Preliminary FRAMEWORK and relevant concept/study inputs. Work through purpose, player actions, rules, states, formulas, dependencies, resource needs, and evaluation. Initial design can identify future resource requirements before RES_TYPE, architecture, or templates have been produced.

**Available support:** [`$design-system`](../.agents/skills/design-system/SKILL.md).

<a id="s2-1-3"></a>

#### 2.1.3. Develop an integration principle that connects each system within the dev framework

- Think about how the systems work together. If something changes in one system, which other systems need to respond, and what information do they need? Decide how shared things are handled so that different systems do not give them contradictory meanings. Connect this arrangement to the developmental framework: when you add or modify content, mechanics, or presentation, you should be able to tell where the work belongs and how its effects reach the rest of the game.

**Studio handoff.** Use the actual system designs to define shared meanings, ownership, exchanged information, and effects of changes. Record how addition and modification routes reach each affected system. Maintain relevant shared facts in [`design/registry/entities.yaml`](../design/registry/entities.yaml) when that registry is used, preserving identities and each fact's source. Carry the integration decisions into the GDDs and FRAMEWORK.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="s2-1-4"></a>

#### 2.1.4. Produce GDD.md for each of the systems

- Put each system's design into its own GDD.md. Explain its purpose, rules, interactions, resource needs, and connections to the other systems. Include the details necessary to understand what should happen, such as relevant calculations, conditions, and exceptions. Someone reading the document should be able to understand what they are expected to build and how new things can fit into it. Make the documents identifiable by system so you can return to the right design during development.

**Studio handoff.** Save an individually identifiable GDD under `design/gdd/` for each system, following the [GDD template](../.codex/docs/templates/game-design-document.md) at the relevant scope. Use `$design-system` for authoring or revision, and keep BREAKDOWN's system links current. Verify that the saved description is usable by downstream architecture/resource work; report remaining review obligations separately.

**Available support:** [`$design-system`](../.agents/skills/design-system/SKILL.md).

<a id="s2-1-5"></a>

#### 2.1.5. Produce FRAMEWORK.md (full)

- Return to the preliminary FRAMEWORK.md and complete it using the system designs you have just developed. You can now explain how the framework works with the actual systems of your game: where new content goes, how new mechanics connect, how presentation is supplied, and what must be considered when existing things change. Bring the sub-components and working principle together into an account you can follow during development. If the framework also takes an executable form, explain how that form supports the work.

**Studio handoff.** Complete `docs/FRAMEWORK.md` against the actual GDDs and their integration principle. Explain where content, mechanics, and presentation enter; how changes propagate; and how outcomes are checked. Identify any supporting executable's real role. Mark Full maturity only when the framework's required working procedures have been developed.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="group-2-2"></a>

### 2.2. Architecture and Technical Setup

Use the architecture activities below with the installed studio procedures and document locations.

<a id="s2-2-1"></a>

#### 2.2.1. Produce ARCHITECTURE_MASTER.md (Master Architecture Document)

- Work out how the designed systems will be organized technically. Which components will implement them, how will those components communicate, and how will they use the game's resources? Use the engine's documentation to ground these choices in what is actually available. Explain how this structure supports the developmental framework, especially the addition and modification of things over time. Put the overall arrangement into ARCHITECTURE_MASTER.md so the individual technical decisions have a common structure to fit into.

**Studio handoff.** Use `$create-architecture` with the relevant GDDs, Full FRAMEWORK, and verified technical choices. Save `docs/architecture/ARCHITECTURE_MASTER.md` with the component arrangement, communication, resource consumption, and support for framework operations. Ground implementation choices in the actual game and engine capabilities.

**Available support:** [`$create-architecture`](../.agents/skills/create-architecture/SKILL.md).

<a id="s2-2-2"></a>

#### 2.2.2. Produce separate ADR.md (several Architecture Decision Records, ADRs)

- For each significant architecture decision, write a separate record explaining the question, the options considered, the chosen approach, and the reasons for choosing it. What does this choice make easier, and what limitations does it introduce? Explain how it affects the relevant systems and their continued development. Keep each ADR identifiable, and distinguish proposed decisions from accepted ones. These records should let you understand why the architecture was built this way when you return to it later.

**Studio handoff.** Use `$architecture-decision` and the [ADR template](../.codex/docs/templates/architecture-decision-record.md) for significant decisions under `docs/architecture/`. Record alternatives, rationale, consequences, applicable requirements, and dependencies. Preserve Proposed, Accepted, and Superseded states; acceptance requires the corresponding decision and applicable evidence. Retain stable requirement identities in the TR registry.

**Available support:** [`$architecture-decision`](../.agents/skills/architecture-decision/SKILL.md).

<a id="s2-2-3"></a>

#### 2.2.3. Review architecture documents

- Read the master architecture and the individual ADRs together, then compare them with the GDDs and FRAMEWORK.md. Can the proposed structure actually produce the behavior you designed? Does it support the additions and modifications you expect to make? Check whether connected components agree about the information and behavior they exchange. Resolve conflicting technical decisions and identify any design descriptions that must change because of what you have learned while working out the architecture.

**Studio handoff.** Use `$architecture-review` on the master arrangement and related ADRs together with the GDDs and FRAMEWORK. Check technical feasibility, interfaces, dependency/decision conflicts, and future addition/modification paths. Required independent review must identify an actual reviewer. Feed findings back into the affected architecture and design documents through an authorized revision.

**Available support:** [`$architecture-review`](../.agents/skills/architecture-review/SKILL.md).

<a id="s2-2-4"></a>

#### 2.2.4. Produce CONTROL.md (Control Manifest)

- Turn the accepted architecture decisions into a practical set of instructions for implementation. Write down which approaches are required, which are forbidden, and which limits need to be respected in the relevant parts of the game. Explain where each instruction applies and connect it to the decision behind it. CONTROL.md should help you or another developer carry out work consistently without having to reconstruct every architecture discussion whenever a component is implemented or modified.

**Studio handoff.** Use `$create-control-manifest` to write `docs/architecture/CONTROL.md` from accepted governing decisions. Keep each Required, Forbidden, or Guardrail rule scoped to affected work and traceable to its decision. Retain the integer `Manifest Version:`; increment it when governing rules or their provenance change. Implementation and reviews use the applicable version.

**Available support:** [`$create-control-manifest`](../.agents/skills/create-control-manifest/SKILL.md).

<a id="s2-2-5"></a>

#### 2.2.5. Produce ACCESSIBILITY.md (Accessibility Requirements)

- Think about how people will receive information and interact with the game, including the difficulties they may encounter. Which accessibility requirements will your game address, and what do those requirements mean for its controls, interfaces, visual presentation, and audio? Record the requirements you decide to support in ACCESSIBILITY.md and explain how you will check them. Use this document when preparing resources and designing interfaces so those choices are considered during development.

**Studio handoff.** Author `docs/ACCESSIBILITY.md` using the [accessibility requirements template](../.codex/docs/templates/accessibility-requirements.md) and [authoring guide](../.codex/docs/templates/guidance/accessibility-requirements-guide.md). The developer selects applicable commitments and evaluation methods. Carry the resulting control, interface, visual, and audio requirements into resource preparation and UX. Qualified accessibility expertise can support the work.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="group-2-3"></a>

### 2.3. Resource Schema

<a id="s2-3-1"></a>

#### 2.3.1. Analyze mechanics' requirement on game resources

- Go through the mechanics in the GDDs and ask what each one needs in order to work. What information defines the things it operates on? What material must exist for the player to interact with it? Identify the properties and relationships that those resources need to contain. For example, if a rule uses a value, determine where that value comes from and what it means. This gives you the resource requirements arising from the game's actual rules.

**Studio handoff.** Read each GDD's rules, calculations, conditions, and interactions. Identify the information, values, properties, identities, and relationships its resources must supply. Explain their meanings and consumers. Carry those findings into the resource-to-system mapping and type definitions; keep genuinely undecided properties explicit.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="s2-3-2"></a>

#### 2.3.2. Analyze dynamics' requirement on game resources

- Consider what happens when the mechanics operate together during play. Do the intended interactions require a range of content, particular combinations, or relationships between resources? A mechanic may work with one example while the intended experience requires variation across many examples. Think through those situations and record what the resources must provide to support them. Connect these requirements to the dynamics you want the game to produce, including how additional content would contribute to them.

**Studio handoff.** Examine the expected behavior of mechanics operating together. Identify required variation, combinations, relationships, and content coverage needed to produce the intended dynamics. Connect each need to a gameplay situation and the systems involved, including what additional content must preserve or extend.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="s2-3-3"></a>

#### 2.3.3. Analyze aesthetics' requirement on game resources

- Think about what you want the player to perceive and feel, and what material is needed to produce that experience. Which visual, audio, written, or other resources communicate an action, establish a mood, or make a result understandable? Describe the qualities those resources need and how they work together. Use the concept and reference studies to explain your intentions clearly enough that resource preparation has a direction beyond simply filling an empty place in the game.

**Studio handoff.** Use CONCEPT, GDDs, and reference studies to describe perceptual and emotional goals, then the visual, audio, textual, or other material that communicates them. `$art-bible`, `$asset-spec`, or applicable domain expertise can support selected details. Keep the resource's intended meaning and combined presentation clear.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="s2-3-4"></a>

#### 2.3.4. Mapping resource requirements to each game system

- Put the resource requirements from the three analyses alongside the systems in BREAKDOWN.md. Which system uses each resource, what does it use it for, and does another system need the same material or related information? Identify shared requirements and clarify how the relevant systems use them. This mapping should make it possible to look at a system and see what it needs, or look at a resource and understand where it belongs in the game.

**Studio handoff.** Map the mechanics, dynamics, and aesthetics requirements back to BREAKDOWN's systems. Identify producers, consumers, shared resources, and linked information. Resolve conflicting interpretations so a prepared resource can satisfy all of its intended consumers. The mapping feeds RES_TYPE and later resource integration review.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="s2-3-5"></a>

#### 2.3.5. Produce RES_TYPE.md (each type of resource needed in the game and how they relate to each game system)

- Group the requirements into the resource types your game needs and describe them in RES_TYPE.md. Explain what each type represents, the information or material it contains, and its relationship to the systems that use it. Identify the properties and connections that instances of the type must have. When you prepare a new resource later, this document should help you understand which type it belongs to and what purpose it serves in the game.

**Studio handoff.** Write root `RES_TYPE.md` using the [resource-type catalog template](../.codex/docs/templates/resource-type-catalog.md). Describe each actual type's purpose, required properties, relationships, and system use. The [resource preparation procedure](../.codex/docs/resource-preparation.md) explains contract ownership and later maintenance. Type names and formats follow the game decisions.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="s2-3-6"></a>

#### 2.3.6. Produce separate TYPE_TEMP for each type of resources and resource_templates/ (templates for each type of resource after a formal formatting transformation)

- Define a template for each resource type so individual resources can be prepared in a consistent form. What information must be supplied, how should it be arranged, and what formatting does the game require? The answers will differ between resource types, so describe them separately in the corresponding TYPE_TEMP. Assemble the usable templates in resource_templates/. These templates should give you a concrete way to turn source material into something that fits the spaces defined by the game's systems.

**Studio handoff.** For each selected type, use the [resource-type definition template](../.codex/docs/templates/resource-type-definition.md) to author an identifiable TYPE_TEMP definition and usable template under root `resource_templates/`. Define input information, arrangement, transformation, output format, relationships, and applicable checks. Exact filenames and formats are selected per type; retain a usable route from loose material to the required resource.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="group-2-4"></a>

### 2.4. GDD Revision

· An overall procedure & house-cleaning to revise game design documents

<a id="s2-4-1"></a>

#### 2.4.1. Individual GDD revision

- Return to each GDD after working through the architecture and resource schema. You will now know more about how the system can be built and what its resources need to contain. Revise the document to reflect those decisions, resolve questions left open earlier, and check that its rules and examples still agree. Make the system's description clear enough to use during implementation without having to guess which of several conflicting statements was intended.

**Studio handoff.** Use `$design-review` for the identified system GDD and then revise the authorized scope with the relevant authoring procedure. Incorporate architecture and resource decisions, resolve prior questions, and check consistency between rules and examples. Distinguish review findings from the subsequent edits and from acceptance of those edits.

**Available support:** [`$design-review`](../.agents/skills/design-review/SKILL.md).

<a id="s2-4-2"></a>

#### 2.4.2. Framework integration review (how each GDD sits within the dev framework)

- Read each GDD alongside FRAMEWORK.md. Does the system support the way you intend to add and modify things? Can you follow the framework's working principle through this particular system, including its connections to other systems? Look for places where the system design and the framework expect different things to happen. Revise the affected descriptions so your plans for continued development are supported by the systems you are actually designing.

**Studio handoff.** Pass the GDD and Full FRAMEWORK to `$design-review` with framework integration as the scope. Walk through actual addition/modification routes and their effects on connected systems. Correct disagreements in the documents that own them, then reassess affected conclusions. Early-design feedback cannot stand in for this completed-framework check.

**Available support:** [`$design-review`](../.agents/skills/design-review/SKILL.md).

<a id="s2-4-3"></a>

#### 2.4.3. Resource integration review (how different resources go into the spaces defined by each GDD)

- Compare each GDD's resource needs with RES_TYPE.md and the corresponding templates. Will a resource prepared with those templates contain what the system expects? Are its connections to other resources clear, and does its presentation serve the intended purpose? Identify missing properties or conflicting expectations and revise the affected documents together. This is where you check whether the resource schema really fits the game design before preparing the actual material.

**Studio handoff.** Use `$design-review` with the actual root RES_TYPE and relevant TYPE_TEMP definitions. Compare required fields, relationships, formats, and presentation with each consuming system's expectations. Revise incompatible GDD/type/template descriptions together, preserving stable identities. Resource-integration conclusions require the contracts produced in 2.3.

**Available support:** [`$design-review`](../.agents/skills/design-review/SKILL.md).

<a id="s2-4-4"></a>

#### 2.4.4. GDD consistency review

- Read the GDDs as parts of one game. Check their descriptions of shared concepts, rules, resources, and interactions. Does an outcome produced by one system make sense to the system receiving it? Have changes made during revision been reflected wherever they matter? Resolve contradictions and unclear divisions of responsibility so the documents describe systems that can work together under the developmental framework.

**Studio handoff.** Use `$review-all-gdds` for the connected design scope, Full BREAKDOWN, FRAMEWORK, and relevant shared/resource facts. Check shared meanings, ownership, exchanged results, and propagation of prior revisions. Resolve cross-system findings before treating the designs as an integrated foundation. Review outputs follow the [review procedure](../.codex/docs/review-workflow.md).

**Available support:** [`$review-all-gdds`](../.agents/skills/review-all-gdds/SKILL.md).

### Handoff to Pre-Implementation

Carry forward the system GDDs, Full FRAMEWORK, reviewed master architecture,
applicable accepted ADRs, scoped CONTROL, accessibility commitments, RES_TYPE,
TYPE_TEMP definitions/templates, and the resolved integration-review findings.
Use `$gate-check development-schematics` for the relevant section assessment.
Resource preparation depends on usable type contracts and their consuming-system
expectations; unfinished contracts remain explicit inputs to complete.

<a id="section-3"></a>

## Section 3. Pre-Implementation

Use the revised designs and resource contracts to prepare the actual material and any tools needed by the development process. Tool end-to-end testing and actual human evaluation are separate required outcomes.

<a id="s3-1"></a>

### 3.1. Loose Files Preparation

· For each of the resource types, prepare loose files that satisfy resource requirements
- Start producing or collecting the source material required by the resource types. Depending on the resource, this could involve writing, preparing structured information, creating visual material, recording audio, or other work called for by the design. Use the requirements and templates to understand what you need before starting. Keep related files together and make their intended use clear. At this point, you are preparing the material that will be transformed into the game's required resource formats in the next step, no need to be 100% clean in what you produce.

**Studio handoff.** Use RES_TYPE and each relevant TYPE_TEMP to identify the source material needed. Follow [resource preparation](../.codex/docs/resource-preparation.md), keeping source provenance and intended use identifiable. The source-material location follows the selected type contract. Rough source work can remain rough here; its formatting is the next activity.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="group-3-2"></a>

### 3.2. Resource Formatting

<a id="s3-2-1"></a>

#### 3.2.1. Transform each loose file for resources with TYPE_TEMP in resource_templates/

- Take the prepared source material and apply the template for its resource type. Fill in the required information, perform the necessary formatting, and establish the relationships the resource needs. Check that the result preserves the intended material and meets the requirements of its consuming systems. Keep track of which source files produced it so you can return to them when a change is needed. The specific transformation follows the type's template and the technical environment you have chosen.

**Studio handoff.** Apply the actual TYPE_TEMP using manual work or an available selected tool. Preserve source-to-output linkage, identities, required information, and relationships. Check that the transformed resource meets its consumer's needs. A new tool is selected only for a demonstrated gap, following 3.3; formatting itself remains a required activity.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="s3-2-2"></a>

#### 3.2.2. Produce res_lib/ (a library of all the resources)

- Assemble the formatted resources into res_lib/ so they can be found and used during development. Organize them by the resource types and relationships already defined, and make each resource's intended use understandable. Check that related resources are present and that the files follow their templates. This library becomes the collection you draw from when implementing the game, adding content, or revising existing material through the developmental framework.

**Studio handoff.** Place authoritative prepared outputs under root `res_lib/`, organized according to their type contracts. Check related resources and promised files by reading them back. Record any selected engine import destinations and transformations so derived engine copies remain traceable to their source. `$asset-audit` and `$content-audit` support applicable format and coverage checks.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="group-3-3"></a>

### 3.3. Tool Development

<a id="s3-3-1"></a>

#### 3.3.1. Define tools outside the engine's boundary for development-relevant roles

- Think about the work people need to carry out during development and where the engine's existing facilities are insufficient. What additional tool would help with preparing, editing, checking, or using the game's material? Describe each tool in terms of the activity it supports, who needs to use it, its inputs, and the result it should produce. Base these choices on the actual development process, without assuming a particular team structure or creating tools whose purpose is still unclear.

**Studio handoff.** Use [tool development](../.codex/docs/tool-development.md) to define the actual user, unsupported activity, representative inputs, expected outputs, and next consumer. Evaluate existing engine facilities, tools, and manual routes first. For a selected tool, the [technical-design template](../.codex/docs/templates/technical-design-document.md) supports a specification at the scope needed.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="s3-3-2"></a>

#### 3.3.2. Develop each tool

- Build each tool according to the activity you have defined for it. Use representative project material as you work so its behavior stays connected to the resource specifications and developmental framework. Make the operation understandable to its intended user: they should know what to provide, what the tool is doing, and how to use the result. Check that its output can be passed into the next part of the development process without unexplained manual corrections.

**Studio handoff.** Implement each selected tool against its specification, representative material, TYPE_TEMP, and FRAMEWORK. Available tools-programmer or relevant domain expertise can help; `$test-setup` and `$test-helpers` support selected test infrastructure. Explain inputs and output use. A tool being built is a future output, so its own absence is not a missing pickup input.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="s3-3-3"></a>

#### 3.3.3. Perform end-to-end tests and human-tests

- Test the complete activity the tool is meant to support, beginning with its input and following the output into its intended use. Does the result satisfy the relevant requirements? What happens when something is missing or incorrect? Then have the intended user perform the task with the tool and observe where they become confused or need help. Revise both the behavior and usage instructions where needed so the tool works in practice as well as in a controlled test.

**Studio handoff.** Run representative input through the tool and into its actual next consumer; inspect the result and a relevant failure case. Then observe the intended human user performing the activity. Record actual usability findings and revise behavior and instructions. `$qa-plan` can organize evaluation, but an agent walkthrough or a written plan does not establish human use.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="s3-3-4"></a>

#### 3.3.4. Produce tools_lib/ (a library of all the tools)

- Collect the developed tools into tools_lib/ with the information needed to set them up and use them. Explain what each tool is for, what it expects, and where its result belongs. Keep those explanations connected to the framework and resource specifications they support. You should be able to return to the library during later development and identify the appropriate tool for the work you are carrying out.

**Studio handoff.** Keep selected tools under root `tools_lib/` with purpose, actual dependencies, setup, invocation, input/output examples, destination, limitations, and verification information. Check the instructions against the tool. Preserve actual end-to-end and intended-user evidence; an unperformed human evaluation remains pending.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

### Handoff to Implementation

Carry forward the prepared resource library, source/output relationships, and
selected tools with setup, usage, end-to-end results, and actual human evaluation.
Use `$gate-check pre-implementation` to assess these outcomes. An absent tool
chosen for a demonstrated need or unperformed required human test remains a gap.
The project decides its actual resources and tool needs; this section introduces
no fixed library size or mandatory generic tool suite.

<a id="section-4"></a>

## Section 4. Implementation

Use the prepared designs, resources, and tools to produce the playable game. Complete the pre-production sequence before milestone production; retain actual human play, candidate-specific acceptance, and delivery evidence.

<a id="group-4-1"></a>

### 4.1. Pre-production

<a id="s4-1-1"></a>

#### 4.1.1. Build UX Specs for Key Screens

- Identify the key screens required by the design and work out how people will use them. What does the player need to understand, which actions can they take, and how does the screen show the result? Describe the relevant layouts, information, interaction states, and movement between screens. Connect these specifications to the GDDs and ACCESSIBILITY.md, and identify the resources needed to present them. Use the reference studies where they help explain a particular interaction or presentation choice.

**Studio handoff.** Use `$ux-design` with the key-screen scope, GDDs, ACCESSIBILITY, and relevant resources/studies. The [UX template](../.codex/docs/templates/ux-spec.md) and [UX guide](../.codex/docs/templates/guidance/ux-spec-guide.md) support identifiable screen specifications under `design/ux/`. Use [HUD](../.codex/docs/templates/hud-design.md) and [interaction-pattern](../.codex/docs/templates/interaction-pattern-library.md) guidance where applicable; `$ux-review` supports evaluation.

**Available support:** [`$ux-design`](../.agents/skills/ux-design/SKILL.md).

<a id="s4-1-2"></a>

#### 4.1.2. Build the Vertical Slice

- Build a limited but coherent portion of the game that brings its important systems together into a playable experience. Choose something that shows how the intended game works and can be developed using the architecture, resources, and tools you have prepared. Pay attention to how the developmental framework works in practice: can you put new things into the game and modify them in the way you planned? Use what you learn to correct problems in the design and development process.

**Studio handoff.** Use `$vertical-slice` with current designs, architecture, Full FRAMEWORK, prepared resources, and relevant tools. Build a coherent playable path and demonstrate both framework-based addition and modification, checking affected systems. The [slice report template](../.codex/docs/templates/vertical-slice-report.md) supports an existing report or `prototypes/[concept-slug]-vertical-slice/REPORT.md`. Keep build, play, integration, and human findings distinguishable. Stories and final milestones may be future outputs.

**Available support:** [`$vertical-slice`](../.agents/skills/vertical-slice/SKILL.md).

<a id="s4-1-3"></a>

#### 4.1.3. Create Epics and Stories From Design Artifacts

- Turn the GDDs, architecture, framework, and other prepared design material into concrete development work. Group related outcomes into epics, then break them into stories describing manageable pieces of work. For each story, explain what should be built or changed, which design it follows, what it depends on, and how you will tell whether it is complete. Use the vertical-slice experience to make this work realistic, including the resource preparation and integration needed to achieve the intended result.

**Studio handoff.** Use `$create-epics` and `$create-stories` with applicable designs, accepted architecture, resource/tool contracts, and actual slice findings. Epics live at `production/epics/[epic]/EPIC.md`, with identifiable stories and their index. Each story states the intended change, framework route, dependencies, criteria, and how the result will be evaluated. Preserve existing IDs and link genuine required inputs.

**Available support:** [`$create-epics`](../.agents/skills/create-epics/SKILL.md) / [`$create-stories`](../.agents/skills/create-stories/SKILL.md).

<a id="s4-1-4"></a>

#### 4.1.4. Validate Stories Before Pickup

- Read a story before starting it and check whether it is ready to be carried out. Is the intended result clear? Are the relevant design decisions available, and do the required resources and dependent systems exist? Can you identify how the work fits into the developmental framework? Resolve missing information and contradictions before they turn into implementation guesses. The story should provide enough direction to begin the work and enough detail to evaluate its result.

**Studio handoff.** Use `$story-readiness` for the exact story. Check clear outcomes, available governing decisions and genuine prerequisites, plus a feasible evaluation method for each criterion. Follow [work preparation](../.codex/docs/work-preparation.md): readiness assessment is read-only and does not automatically edit Story Status. Resolve blocking definition/input gaps before pickup; completion evidence remains work to produce.

**Available support:** [`$story-readiness`](../.agents/skills/story-readiness/SKILL.md).

<a id="s4-1-5"></a>

#### 4.1.5. Validate progress against Vertical Slice Hard Gate

- Play and examine the vertical slice to determine whether it provides a sufficient basis for further production. Does it deliver the intended part of the experience, do its systems work together, and can someone understand and play it without the developer explaining every action? Check whether the development framework also supports the work demonstrated by the slice. Identify what must be corrected before moving forward, and use actual play and development experience as evidence for that decision.

**Studio handoff.** Run `$gate-check vertical-slice` against actual playable, usability, integration, resource/tool, and framework-operation evidence, including human findings and required independent review. Demonstrate addition AND modification under FRAMEWORK. Required failures or unavailable evidence block production. Record the basis for any PROCEED/PIVOT/KILL recommendation; the developer owns the consequential decision. Final MILESTONE follows this gate.

**Available support:** [`$gate-check`](../.agents/skills/gate-check/SKILL.md).

<a id="s4-1-6"></a>

#### 4.1.6. Produce MILESTONE.md

- Define the milestones that will organize the rest of development. For each one, explain what the game should contain, how complete or polished those things need to be, and what you need to learn from playing that version. State how you will determine that the milestone has been reached. Define MVP, Alpha, Beta, and Gold according to your game's needs so the later production steps refer to concrete expectations. Put these decisions together in MILESTONE.md.

**Studio handoff.** Use `$define-milestones` and the [milestone template](../.codex/docs/templates/milestone-definition.md) to write `production/milestones/MILESTONE.md` after the hard gate. Define the project's MVP, Alpha, Beta, and Gold scope, quality, playtest learning goals, and completion criteria. Earlier drafts keep missing evidence explicit. Dates, budgets, and capacity are included when selected for this project.

**Available support:** [`$define-milestones`](../.agents/skills/define-milestones/SKILL.md).

<a id="group-4-2"></a>

### 4.2. Production

<a id="s4-2-1"></a>

#### 4.2.1. Minimum Viable Product and play-test

- Build the minimum viable version defined in MILESTONE.md. Bring together the content and systems needed for that version to offer the intended playable experience, using the developmental framework to guide additions and modifications. Play-test the result and observe what players actually do, understand, and struggle with. Compare those findings with the milestone's expectations, then use them to decide what needs correction or further development before proceeding.

**Studio handoff.** Use the settled MVP definition to select and implement work through `$dev-story` and the [execution procedure](../.codex/docs/execution-and-evidence.md). Conduct actual human playtests and use `$playtest-report` to record findings under `production/playtests/`. `$milestone-review` compares the resulting experience and evidence with the MVP criteria. Correct blocking findings before treating the milestone as reached.

**Available support:** [`$dev-story`](../.agents/skills/dev-story/SKILL.md) / [`$playtest-report`](../.agents/skills/playtest-report/SKILL.md) / [`$milestone-review`](../.agents/skills/milestone-review/SKILL.md).

<a id="s4-2-2"></a>

#### 4.2.2. Alpha Version and play-test

- Develop the Alpha version according to the scope and expectations written in MILESTONE.md. Work through the relevant stories and add or revise the systems, content, and presentation required for this stage. Play-test how those parts work together and identify problems that are becoming apparent in the larger game. Record what needs further work and make the corresponding changes through the framework, keeping the affected design documents consistent with the decisions you make.

**Studio handoff.** Follow the Alpha definition and relevant stories. Carry changes through FRAMEWORK and update affected designs, resources, and integrations. Record actual player observations with `$playtest-report`; use `$milestone-review` on the tested Alpha build and its criteria. Track what the larger game reveals and what must change for later work.

**Available support:** [`$dev-story`](../.agents/skills/dev-story/SKILL.md) / [`$playtest-report`](../.agents/skills/playtest-report/SKILL.md) / [`$milestone-review`](../.agents/skills/milestone-review/SKILL.md).

<a id="s4-2-3"></a>

#### 4.2.3. Beta Version and play-test

- Build toward the Beta requirements you have defined, using the findings from Alpha to guide the remaining work. Check the game as a combined experience as well as checking individual features. Play-test the situations and interactions relevant to this milestone, then assess whether the result meets its stated expectations. Decide what must be revised and carry those changes through the appropriate systems, resources, and presentation before treating the milestone as complete.

**Studio handoff.** Use the project's Beta scope and Alpha findings to choose the remaining work. Execute feature and combined-experience checks appropriate to those criteria, including real playtests. Record results against the actual tested revision and use `$milestone-review` to identify remaining blocking work. Carry corrections through the affected framework routes and recheck them.

**Available support:** [`$dev-story`](../.agents/skills/dev-story/SKILL.md) / [`$playtest-report`](../.agents/skills/playtest-report/SKILL.md) / [`$milestone-review`](../.agents/skills/milestone-review/SKILL.md).

<a id="s4-2-4"></a>

#### 4.2.4. Gold Version and play-test

- Prepare the Gold version against the requirements in MILESTONE.md. Complete the work intended for this version and play-test the resulting game, including the parts affected by recent corrections or polishing. Make sure the final combination of systems, content, and presentation works as intended. Resolve findings that prevent the version from meeting its milestone, then carry the resulting game into the final acceptance check.

**Studio handoff.** Complete the Gold scope, then play and check the actual combination of systems, content, and presentation, including recent corrections. Use `$playtest-report` and `$milestone-review` against the Gold criteria. Resolve milestone-blocking findings and identify the resulting version for final acceptance. Gold completion alone does not establish release acceptance.

**Available support:** [`$dev-story`](../.agents/skills/dev-story/SKILL.md) / [`$playtest-report`](../.agents/skills/playtest-report/SKILL.md) / [`$milestone-review`](../.agents/skills/milestone-review/SKILL.md).

<a id="group-4-3"></a>

### 4.3. Final Acceptance Check

<a id="s4-3-1"></a>

#### 4.3.1. Produce RELEASE_CHECKLIST.md

- Turn the requirements for the intended release into a checklist you can actually use. Draw from the concept's commitments, the GDDs, accessibility requirements, milestone expectations, and the preparation needed for the chosen release method. State what needs to be checked and how you will recognize a satisfactory result. Keep the items specific to this game and release so the checklist helps you examine the work you have done.

**Studio handoff.** Use `$release-checklist` in requirements-authoring scope and the [release checklist template](../.codex/docs/templates/release-checklist-template.md) to write `production/releases/RELEASE_CHECKLIST.md`. Record requirement sources, applicability, obligation strength, evaluation methods, and evaluator responsibilities. Preserve developer decisions and unknowns. The requirements document and candidate-specific assessment reports have separate purposes.

**Available support:** [`$release-checklist`](../.agents/skills/release-checklist/SKILL.md).

<a id="s4-3-2"></a>

#### 4.3.2. Check the game against the checklist

- Go through RELEASE_CHECKLIST.md with the version you intend to release. Perform the checks and record the results, including anything that remains unresolved. When a correction changes the game, check the affected parts again so the result applies to the version you will actually ship. Use the completed checklist to determine whether the game meets its release requirements and which issues still require a decision or further work.

**Studio handoff.** Use `$release-checklist` for internal assessment, `$launch-checklist` for applicable external/distribution assessment, and `$gate-check final-acceptance` for the intended release decision. Identify the exact candidate and requirements baseline. Persist the reports needed by release coordination under the [release contract](../.codex/docs/release-and-operations.md). Changed candidates require affected checks again; required failures and unavailable evidence remain blockers.

**Available support:** [`$gate-check`](../.agents/skills/gate-check/SKILL.md) final-acceptance.

<a id="group-4-4"></a>

### 4.4. Release

<a id="s4-4-1"></a>

#### 4.4.1. Generate Player-Facing Content

- Prepare the material players need to understand the game and its release. Depending on how it will be distributed, this may include descriptions, screenshots, instructions, release notes, or other relevant content. Check that the material accurately represents the version being released and communicates in terms useful to players. Draw from the actual game and the decisions already made about its presentation and intended experience.

**Studio handoff.** Prepare only the material needed by the chosen distribution route and verify it against the actual candidate. `$changelog` supports verified Git history; `$patch-notes` supports player-facing version notes at `production/releases/[version]/patch-notes.md`, using the [release-notes template](../.codex/docs/templates/release-notes.md). Screenshots, descriptions, instructions, and applicable localization require their actual inputs. Drafting is separate from publication.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="s4-4-2"></a>

#### 4.4.2. Coordinate the Release

- Put the release preparations together. Identify the version being delivered, where it will be made available, which materials need to accompany it, and the order in which the required actions must happen. If several people are involved, make their responsibilities clear. Check that the game and player-facing content are ready together so the release can be carried out as intended.

**Studio handoff.** Use `$team-release` when coordinating the chosen release. It consumes matching persisted internal and external READY reports for the exact candidate, scope/platforms, and requirements baseline, plus applicable final-acceptance evidence. Identify delivery actions, materials, responsibilities, and existing authorization. A preview, stale assessment, or unresolved required check cannot establish GO.

**Available support:** [`$team-release`](../.agents/skills/team-release/SKILL.md).

<a id="s4-4-3"></a>

#### 4.4.3. Ship

- Carry out the release through the chosen distribution method. Verify that players can obtain or access the intended version and that the delivered game works in that form. Check the accompanying information and address problems encountered during the release. Keep a clear record of what was shipped so later feedback and fixes can be connected to the version players received.

**Studio handoff.** Carry out the authorized delivery operations for the identified candidate and destination. Verify player access, delivered artifact identity, operation, and accompanying information. Record what actually shipped and address delivery failures within the authorized scope. Passing a checklist does not itself perform a push, tag, deployment, publication, or external communication.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

<a id="s4-4-4"></a>

#### 4.4.4. Post-launch

- Follow how the released game performs and how players respond to it. Investigate reported problems, consider feedback, and decide which fixes or additions to pursue. Use the developmental framework to introduce those changes consistently with the existing game. When experience shows that the framework itself needs adjustment, return to it and revise the relevant parts. The preparation done earlier should continue to support maintaining, expanding, and polishing the game over time.

**Studio handoff.** Use actual player feedback, reports, and operational observations to choose work. `$bug-report`, `$bug-triage`, `$hotfix`, `$day-one-patch`, and applicable `$team-live-ops` support selected tasks. Route fixes/additions through FRAMEWORK, keep affected designs/resources consistent, and revise framework procedures when experience warrants it. Use the [incident template](../.codex/docs/templates/incident-response.md) for relevant incidents; record implemented fixes and delivered verification separately.

**Execution:** Direct work with the developer or an available qualified executor, following the responsibilities stated above.

### Continuing after release

Retain the release identity, actual delivery observations, and affected requirement,
design, resource, and framework baselines. Changes return through the relevant
authoring, implementation, review, and release checks. `$gate-check implementation`
assesses the selected section outcomes; a named milestone or final-acceptance
assessment remains scoped to that checkpoint. Post-launch work has no invented
additional section or automatic completion of future maintenance.

<a id="working-across-activities"></a>

## Working across activities

The following procedures explain how the installed studio supports the activities
above. Apply them to the selected work without introducing additional workflow
phases, default schedules, or arbitrary numeric completion thresholds.

### Authoring, review, and decisions

For an authoring task, identify the intended result, current inputs, maturity,
affected readers, and output destination. Read existing work before asking about
decisions it already contains. Save within the authorized scope, preserve stable
identities and concurrent edits, and read back promised outputs before handoff.
If only part of a multi-file change succeeds, retain the completed work and report
the missing handoff accurately.

Reviews use the [review workflow](../.codex/docs/review-workflow.md) and applicable
[director-gate prompts](../.codex/docs/director-gates.md). Supply the artifact or
complete draft, revision, scope, governing decisions, and available evidence.
Identify the actual reviewer and any self-review. If the procedure requires
independence, use an independent qualified reviewer under the active environment's
delegation policy. A persona name by itself does not establish that a review ran.

Return the actual findings, missing/inapplicable checks, verdict, and corrective
work. Reviews report in conversation by default; save only when the task includes
that output. If a later procedure needs a persisted result, identify its writer
and path. A saved review does not itself accept an ADR, set Story Status, advance
the workflow marker, or authorize release. Recheck affected conclusions after
changes to their inputs. Review depth can adjust optional breadth while preserving
required outcomes, independence, and human evaluation.

### Carrying out a story

1. Resolve the exact story and its applicable GDD, FRAMEWORK route, architecture,
   CONTROL version, resource/tool contracts, and genuine prerequisite inputs.
   `$story-readiness` assesses whether the work and evaluation methods are clear.
2. Use `$dev-story` for the selected authorized implementation. Resolve actual
   project and test roots through live preferences and
   [root resolution](../.codex/docs/code-root-resolution.md). Engine-specific
   layouts and runners follow the selected game setup.
3. Evaluate each criterion by its appropriate method: automated checks, engine
   execution, resource inspection, calculations, manual interaction, listening,
   or actual player/intended-user use. `$test-evidence-review`, `$code-review`,
   and relevant domain reviews support the required evaluation. Plans and test
   file existence do not establish observed results.
4. Record the revision/build, inputs, method, outcome, limitations, and actual
   evaluator. Automated outputs use the actual runner locations; manual evidence
   uses `production/qa/evidence/` or the existing agreed evidence path.
5. Use `$story-done` to assess completion. Required failures or unavailable checks
   prevent completion. Within an authorized closure task, update the single
   authoritative story header and applicable derived views, preserving identity
   and previous evidence. Completion does not automatically commit or merge.

The authoritative story header uses Not Started, Ready, In Progress, In Review,
Complete, or Blocked. The mapping and treatment of legacy values are in
[work preparation](../.codex/docs/work-preparation.md). `production/sprint-status.yaml`
derives statuses for the chosen sprint; its contents do not override stories.
Use `$sprint-plan`, `$sprint-status`, `$estimate`, and `$retrospective` when those
planning scopes are selected. Milestone completion still requires the actual
MILESTONE criteria and playtest evidence.

### Adding or modifying something

Follow the applicable route in `docs/FRAMEWORK.md`. Identify what changes, why,
which systems own it, and which resources, consumers, interfaces, and tests are
affected. Use `$propagate-design-change` to trace a design change and its dependent
documents, then carry authorized corrections through the actual implementation
and resource/tool pipeline. `$quick-design` can support a bounded small change
within its documented scope. Preserve the governing requirements and recheck
affected integration conclusions.

If the framework's route no longer fits the work, revise the relevant framework
procedure and its affected contracts. Prototype work can investigate a specific
uncertainty with `$prototype`; retain its actual learning and limits. Prototype
evidence remains distinct from a production milestone or the playable-slice gate.

### Using specialized support

Choose skills and expertise according to the actual task. Visual, audio, narrative,
level, economy, localization, accessibility, engine, and QA work draw on the
[installed roles](../.codex/docs/agent-roster.md), [coordination guidance](../.codex/docs/coordination-rules.md),
and [skill reference](../.codex/docs/skills-reference.md). Persona definitions
describe responsibilities; actual execution depends on available tools and the
current delegation policy. No fixed team is a prerequisite to all activities.

Examples of supporting procedures include `$asset-spec` for applicable resource
requirements, `$asset-audit` for declared format/file constraints, `$content-audit`
for content coverage, `$balance-check` for design/economy questions, `$perf-profile`
for observed performance, and `$security-audit` for the relevant threat scope.
`$smoke-check`, `$regression-suite`, `$soak-test`, and `$test-flakiness` require the
matching execution inputs and selected scope. Their results contribute to the
criterion they actually assess. A studio installation does not install an engine
or establish that these game checks have run.

### Evidence for milestone and release decisions

Use MILESTONE to define what MVP, Alpha, Beta, and Gold mean for this game, including
what should be learned from each playtest. Observe the actual candidate experience,
record the findings, and correct blocking issues through the framework. The
milestone names alone do not impose story counts, durations, bug budgets, or a
fixed number of playtest sessions.

Final acceptance and release coordination follow the
[release and operations contract](../.codex/docs/release-and-operations.md).
`production/releases/RELEASE_CHECKLIST.md` holds requirements. Internal assessments
use `production/releases/release-checklist-[date].md`; external assessments use
`production/launch/launch-checklist-[date].md`. Match each report to the exact
candidate, platforms/scope, and requirements baseline. `$team-release` requires
the matching persisted READY reports and applicable acceptance evidence. Complete
the selected delivery route only within its existing authorization and verify
the result players receive.

### Resuming work and integrating contributions

Use [continuity guidance](../.codex/docs/context-management.md) for bounded session
checkpoints at `production/session-state/active.md`. A recovery summary identifies
actual work, decisions, next activity, and missing evidence; it does not replace
the underlying design, story, or test records. `$onboard` helps a contributor
locate the responsibilities and current artifacts relevant to their assignment.

When the project selects parallel Git worktrees, follow the
[worktree procedure](../.codex/docs/worktree-workflow.md) and `$integrate-worktrees`.
Each contribution carries its scope, fixed baseline, delivered changes, decisions,
checks, and unresolved issues. Combined integration has its own reconciliation and
verification; completion of an individual task does not prove combined correctness.
Commits, merges, pushes, and publication follow the authorized task scope.

### Maintaining the studio itself

Use `$skill-test` and `$skill-improve` for their documented evaluation and bounded
repair modes. The [testing framework](<../CGS Skill Testing Framework/README.md>)
contains specifications, and its [runtime checks](<../CGS Skill Testing Framework/runtime/README.md>)
exercise metadata and helper behavior. Studio test results, game execution,
human play, and native hook dispatch provide different evidence. Keep those
scopes explicit when reporting what is ready.
