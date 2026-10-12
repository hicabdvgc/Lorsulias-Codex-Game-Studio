---
name: ux-design
description: "Guided, section-by-section UX spec authoring for a screen, flow, or HUD. Reads game concept, player journey, and relevant GDDs to provide context-aware design guidance. Produces named-screen specifications, design/ux/hud.md, or design/ux/interaction-patterns.md using the studio templates."
---

Read `.codex/docs/resource-preparation.md` for resource locations, shared write,
review/evidence and recovery requirements. Its shared handoff rules apply here;
initial design can record future resource needs before type contracts exist.

## Invocation and execution

Invoke this workflow as `$ux-design`.

Use existing authorization for the bounded task. Describe the intended outputs and preserve unrelated work. Ask only about unresolved consequential choices or material scope expansion; do not repeat file- or section-level approval prompts.

Arguments: `[screen/flow name] or 'hud' or 'patterns'`. Treat bracketed values as optional unless the workflow says otherwise.

Use available qualified `ux-designer` expertise when useful and delegation is authorized. Otherwise perform the applicable responsibilities in the current agent, preserving required independence and human evidence.


When this skill is invoked:

## 1. Parse Arguments & Determine Mode

Three authoring modes exist based on the argument:

| Argument | Mode | Output file |
|----------|------|-------------|
| `hud` | HUD design | `design/ux/hud.md` |
| `patterns` | Interaction pattern library | `design/ux/interaction-patterns.md` |
| Any other value (e.g., `main-menu`, `inventory`) | UX spec for a screen or flow | `design/ux/[argument].md` |
| No argument | Ask the user | (see below) |

**If no argument is provided**, do not fail — ask instead. Ask the user directly:
- "What are we designing today?"
  - Options: "A specific screen or flow (I'll name it)", "The game HUD", "The interaction pattern library", "I'm not sure — help me figure it out"

If the user selects "I'll name it" or types a screen name, normalize it to a non-empty kebab-case filename segment. Reject `/`, `\\`, absolute paths, `.`, `..`, empty slugs, and the reserved slugs `hud` and `interaction-patterns`. Resolve the final path and verify it remains directly inside `design/ux/` before any read or write.

---

## 2. Gather Context (Read Phase)

First resolve the mode as Phase 1 describes; if no mode is known, ask that single
mode question before project reads. Once the target is resolved, read all relevant
context before design questions. Ask about missing input configuration only after
the relevant context read identifies the gap.

### 2a: Required Reads

- **Game concept**: Read `design/gdd/CONCEPT.md` — if missing, warn:
  > "No game concept found. The developer authors CONCEPT; `$brainstorm` can support the game's
  > foundation before designing UX."
  > Continue anyway if the user asks.

### 2b: Player Journey

Read `design/player-journey.md` if it exists. For each relevant section, extract:
- Which journey phase(s) does this screen appear in?
- What is the player's emotional state on arrival at this screen?
- What player need is this screen serving in the journey?
- What critical moments (from the journey map) does this screen deliver?

If the player journey file does not exist, note the gap and proceed:
> "No player journey map found at `design/player-journey.md`. Designing without it
> means we'll be making assumptions about player context. Consider running a player
> journey session after this spec is drafted."

Also add to the UX spec's Open Questions section:
> "Player journey map not yet created. Template available at `.codex/docs/templates/player-journey.md`. Use that template with developer-supplied observations to establish player context for this screen; this skill reads the journey and does not automatically author it."

### 2c: GDD UI Requirements

Prefer explicit GDD links in an existing spec header and the systems index, then
read direct UI Requirements references for this screen. If name/category matching
is ambiguous, list candidate GDDs for user confirmation rather than scanning or
guessing all documents. HUD remains the exception and reads all GDD UI Requirements.

These GDD UI Requirements are the **requirements input** to this spec. Collect them
as a list of constraints the spec must satisfy.

If designing the HUD, read ALL GDD UI Requirements sections — the HUD aggregates
requirements from every system.

### 2d: Existing UX Specs

Find files matching `design/ux/*.md` and note which screens already have specs. For screens that
will link to or from the current screen, read their navigation/flow sections to
find the entry and exit points this spec must match.

### 2e: Interaction Pattern Library

If `design/ux/interaction-patterns.md` exists, first read only its catalog index.
When the current spec selects a pattern, then read that pattern's complete existing
section before reusing its behavior. Do not load unrelated pattern bodies.

### 2f: Art Bible

Check for `design/art/art-bible.md`. If found, read the visual direction
section. UX layout must align with the aesthetic commitments already made.

### 2g: Accessibility Requirements

Check for `docs/ACCESSIBILITY.md`. If found, read it. The spec
must address the applicable commitments and evaluation methods recorded there.

### 2h: Input Method (from Project Config)

Read `docs/technical-preferences.md` and extract the `## Input & Platform`
section. Store these values for use throughout the skill — they drive the
Interaction Map and inform accessibility requirements:

- **Input Methods** — e.g., Keyboard/Mouse, Gamepad, Touch, Mixed
- **Primary Input** — the dominant input for this game
- **Gamepad Support** — Full / Partial / None
- **Touch Support** — Full / Partial / None
- **Target Platforms** — for safe zone and aspect ratio decisions

If the section is unconfigured (`[TO BE CONFIGURED]`), ask once:
> "Input methods aren't configured yet. What does this game target?"
> Options: "Keyboard/Mouse only", "Gamepad only", "Both (PC + Console)", "Touch (mobile)", "All of the above"
>
> (Run `$setup-engine` to save this permanently so you won't be asked again.)

Store the answer for the rest of this session. Do **not** ask again per section
or per screen.

### 2i: Present Context Summary

Before any design work, present a brief summary to the user:

> **Designing: [Screen/Flow Name]**
> - Mode: [UX Spec / HUD Design / Pattern Library]
> - Journey phase(s): [from player-journey.md, or "unknown — no journey map"]
> - GDD requirements feeding this spec: [count and names, or "none found"]
> - Related screens already specced: [list, or "none yet"]
> - Known patterns available: [count, or "no pattern library yet"]
> - Accessibility commitments: [from requirements doc, or "not yet defined"]
> - Input methods: [from technical-preferences.md, or "asked above"]

Continue within the requested task. Ask only about information or consequential choices still needed.

---

## 2b. Retrofit Mode Detection

Before creating a skeleton, check if the target output file already exists.

Find files matching `design/ux/[filename].md` (where `[filename]` is the resolved output path from Phase 1).

**If the file exists — retrofit mode:**
- Read the mode's current authoritative template, then read the target file in full
- Derive applicable information needs from the template and match equivalent headings by meaning. Treat only explicit template placeholders as placeholders; short but real content is not empty, and existing real sections are never renamed or reordered
- Present a section status summary to the user:

> "Found existing UX spec at `design/ux/[filename].md`. Here's what's already done:
>
> | Section | Status |
> |---------|--------|
> | [section heading read from the current authoritative template] | [Complete / Empty / Placeholder] |
> | ... | ... |
>
> I will fill the requested gaps or revise the identified content while preserving unrelated sections."

- Skip Phase 3 (skeleton creation) — the file already exists
- In Phase 4 (Section Authoring), work on the requested gaps or explicitly requested revisions, preserving other content
- Edit the file to fill placeholders in-place rather than creating a new skeleton

**If the file does not exist — fresh authoring mode:**
Proceed to Phase 3 (Create File Skeleton) as normal.

---

## 3. Create or update the selected design

Read the applicable `.codex/docs/templates/ux-spec.md`, `hud-design.md`, or
`interaction-pattern-library.md`. Use relevant fields and document inapplicable
sections; heading counts are not completeness. Read the matching guidance file
under `.codex/docs/templates/guidance/` for useful worked examples.

Read `docs/FRAMEWORK.md` and identify integration responsibilities. Follow actual
accepted architecture for data ownership and read/write interfaces. Relate resource
needs to TYPE_TEMP where defined, with unresolved needs explicit in early design.

Author the named output and any requested shared-pattern changes within existing
authorization. Re-read existing content before updating it. A locally specified
interaction need not be made a shared pattern, but a shared-pattern reference must
resolve to a complete persisted entry. No automatic session-state writer is supplied;
use the shared manual checkpoint/recovery guidance when needed.

## Required continuation

Read [references/continued-workflow.md](references/continued-workflow.md) for the
remaining authoring, cross-reference, handoff and recovery responsibilities.
