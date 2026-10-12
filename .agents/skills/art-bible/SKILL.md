---
name: art-bible
description: "Author or revise visual direction and applicable asset standards from the developer concept, references and selected project needs."
---

Read `.codex/docs/resource-preparation.md` for resource locations, shared write,
review/evidence and recovery requirements. Its shared handoff rules apply here;
initial design can record future resource needs before type contracts exist.

## Invocation and execution

Invoke this workflow as `$art-bible`.

Use existing authorization for the bounded task. Describe the intended outputs and preserve unrelated work. Ask only about unresolved consequential choices or material scope expansion; do not repeat file- or section-level approval prompts.

Arguments: `[--review full|lean|solo]`. Treat bracketed values as optional unless the workflow says otherwise.


## Phase 0: Scope and context

Preserve `--review full|lean|solo`; use the shared review-workflow defaults. These
options change optional breadth. Required reviews and technical evidence remain
required in every mode. Identify self-review accurately.

Read developer-authored `design/gdd/CONCEPT.md`, supplied visual decisions and
relevant reference studies under `game_ref/`. If required direction is missing,
ask for it and keep the affected output provisional; `$brainstorm` supports the
developer and does not author CONCEPT. Read applicable GDDs, FRAMEWORK, accessibility
commitments, live technical preferences and resource type contracts when present.
An art bible is optional support and can be authored or revised when needed; its
existence is not a prerequisite for mapping systems or initial GDD authoring.

## Phase 1: Authoring or retrofit boundary

Read `.codex/docs/templates/art-bible.md` and any existing
`design/art/art-bible.md`. Derive applicable sections from the template and actual
needs. Match equivalent headings by meaning, preserve substantive existing content,
and distinguish missing information from an irrelevant section. For retrofit,
fill the requested gaps or revise the identified sections without rewriting others.

Use the requested scope (full applicable direction, visual foundation, standards,
or resume). Ask about references or scope only when the supplied context cannot
resolve them. Standards-only work needs sufficient selected direction for those
standards; it does not require unrelated sections to be authored first. Use existing
bounded authorization to save the selected content. Ask about unsettled consequential
creative choices, without mandatory approvals for each section.

## Phase 2: Visual Identity Foundation (Sections 1–4)

Use the following authoring topics where relevant and map them to the current template headings. Save authorized work incrementally. The topics are guidance rather than a fixed completeness count.

### Visual Identity Statement

**Goal**: A one-line visual rule plus supporting principles that resolve visual ambiguity.

If a visual anchor exists from CONCEPT.md: present it and ask:
- "Build directly from this anchor?"
- "Revise it before expanding?"
- "Start fresh with new options?"

**Visual-direction responsibility**: Use a qualified available executor, optionally `art-director` when delegation is authorized:
- Provide: game concept (elevator pitch, core fantasy), applicable pillar set, platform target, any reference games/art from Phase 1 framing, the visual anchor if it exists
- Ask: "Draft a Visual Identity Statement for this game. Provide: (1) a one-line visual rule that could resolve any visual decision ambiguity, (2) the supporting visual principles needed, each with a one-sentence design test ('when X is ambiguous, this principle says choose Y'). Anchor all principles directly in the stated pillars — each principle must serve a specific pillar."

Present the art-director's draft to the user. Ask the user directly:
- Options: `[A] Lock this in` / `[B] Revise the one-liner` / `[C] Revise a supporting principle` / `[D] Describe my own direction`

Save the settled content within the authorized scope; unresolved choices remain explicit.

### Mood & Atmosphere

**Goal**: Emotional targets by game state — specific enough for a lighting artist to work from.

For each major game state (e.g., exploration, combat, victory, defeat, menus — adapt to this game's states), define:
- Primary emotion/mood target
- Lighting character (time of day, color temperature, contrast level)
- Atmospheric descriptors (specific descriptors)
- Energy level (frenetic / measured / contemplative / etc.)

**Visual-direction responsibility**: Use the selected qualified executor with the Visual Identity Statement and pillar set. Ask: "Define mood and atmosphere targets for each major game state in this game. Be specific — 'dark and foreboding' is not enough. Name the exact emotional target, the lighting character (warm/cool, high/low contrast, time of day direction), and at least one visual element that carries the mood. Explain distinctions only where they serve the intended experience."

Save the settled content within the authorized scope; unresolved choices remain explicit.

### Shape Language

**Goal**: The geometric vocabulary that makes this game's world visually coherent and distinguishable.

Cover:
- Character silhouette philosophy (how readable at thumbnail size? Distinguishing trait per archetype?)
- Environment geometry (angular/curved/organic/geometric — which dominates and why?)
- UI shape grammar (does UI echo the world aesthetic, or is it a distinct HUD language?)
- Hero shapes vs. supporting shapes (what draws the eye, what recedes?)

**Visual-direction responsibility**: Use the selected qualified executor with Visual Identity Statement and mood targets. Ask: "Define the shape language for this game. Connect each shape principle back to the visual identity statement and a specific game pillar. Explain what these shape choices communicate to the player emotionally."

Save the settled content within the authorized scope; unresolved choices remain explicit.

### Color System

**Goal**: A complete, producible palette system that serves both aesthetic and communication needs.

Cover:
- Primary palette (selected colors with roles — not just hex codes, but what each color means in this world)
- Semantic color usage (what does red communicate? Gold? Blue? White? Establish the color vocabulary)
- Per-biome or per-area color temperature rules (if the game has distinct areas)
- UI palette (may differ from world palette — define the divergence explicitly)
- Colorblind safety: which semantic colors need shape/icon/sound backup

**Visual-direction responsibility**: Use the selected qualified executor with Visual Identity Statement and mood targets. Ask: "Design the color system for this game. Every semantic color assignment must be explained — why does this color mean danger/safety/reward in this world? Identify which color pairs might fail colorblind players and specify what backup cues are needed."

Save the settled content within the authorized scope; unresolved choices remain explicit.

---

## Phase 3: Production Guides (Sections 5–8)

These sections translate the visual identity into concrete production rules. They should be specific enough that an outsourcing team can follow them without additional briefing.

### Character Design Direction

**Visual-direction responsibility**: Use the selected qualified executor with relevant visual foundation. Ask: "Define character design direction for this game. Cover: visual archetype for the player character (if any), distinguishing feature rules per character type (how do players tell enemies/NPCs/allies apart at a glance?), expression/pose style targets (stiff/expressive/realistic/exaggerated), and LOD philosophy (how much detail is preserved at game camera distance?)."

Save the settled content within the authorized scope.

### Environment Design Language

**Visual-direction responsibility**: Use the selected qualified executor with relevant visual foundation. Ask: "Define the environment design language for this game. Cover: architectural style and its relationship to the world's culture/history, texture philosophy (painted vs. PBR vs. stylized — why this choice for this game?), prop density rules (sparse/dense — what drives the choice per area type?), and environmental storytelling guidelines (what visual details should tell the story without text?)."

Save the settled content within the authorized scope.

### UI/HUD Visual Direction

**Relevant responsibilities** (may be performed by available qualified executors; delegate only when authorized):
- **`art-director`**: Visual style for UI — diegetic vs. screen-space HUD, typography direction (font personality, weight, size hierarchy), iconography style (flat/outlined/illustrated/photorealistic), animation feel for UI elements
- **`ux-designer`**: UX alignment check — does the visual direction support the interaction patterns this game requires? Flag any conflicts between art direction and readability/accessibility needs.

Collect both. If they conflict (e.g., art-director wants elaborate diegetic UI but ux-designer flags it would reduce combat readability), surface the conflict explicitly with both positions. Do NOT silently resolve — ask the user directly to let the user decide.

Save the settled content within the authorized scope.

### Asset Standards

**Relevant responsibilities** (may be performed by available qualified executors; delegate only when authorized):
- **`art-director`**: File format preferences, naming convention direction, texture resolution tiers, LOD level expectations, export settings philosophy
- **`technical-artist`**: Engine-specific hard constraints — poly count budgets per asset category, texture memory limits, material slot counts, importer constraints, anything from the performance budgets in `docs/technical-preferences.md`

If any art preference conflicts with a technical constraint (e.g., art-director wants 4K textures but performance budget requires 2K for mobile), resolve the conflict explicitly — note both the ideal and the constrained standard, and explain the tradeoff. Ambiguity in asset standards is where production costs are born.

Save the settled content within the authorized scope.

---

## Phase 4: Reference Direction

**Goal**: A curated reference set that is specific about what to take and what to avoid from each source.

**Visual-direction responsibility**: Use the selected qualified executor with the relevant completed direction. Ask: "Compile a reference direction for this game. Provide relevant reference sources (games, films, art styles, or specific artists). For each: name it, specify exactly what visual element to draw from it (not 'the general aesthetic' — a specific technique, color choice, or compositional rule), and specify what to explicitly avoid or diverge from (to prevent the 'trying to copy X' reading). References should be additive — no two references should be pointing in exactly the same direction."

Save the settled content within the authorized scope.

---

## Phase 5: Review and handoff

Check the selected scope against the concept, visual decisions, system requirements,
accessibility commitments and resource contracts. Run AD-ART-BIBLE when that gate
applies under `.codex/docs/director-gates.md`. Missing required evidence or independent
review remains NOT ASSESSED. A partial edit or self-review cannot supply a missing
production sign-off. Preserve actual gate vocabulary and evidence provenance.

Verify the saved file and report changed sections, unresolved decisions, review
coverage and affected asset/type/UX consumers. Recommend next activities from their
actual prerequisites in the workflow catalog; file existence alone never means
mapping, engine setup, review or architecture is complete. Preserve completed work
if another executor fails; assign remaining work to an available qualified executor
or identify the dependent activity as incomplete.
