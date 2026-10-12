---
name: asset-spec
description: "Generate visual asset specifications, optional generation prompts, inventories and shared manifest entries from design sources or supplied direction."
---

Read `.codex/docs/resource-preparation.md` for resource locations, shared write,
review/evidence and recovery requirements. Its shared handoff rules apply here;
initial design can record future resource needs before type contracts exist.

## Invocation and execution

Invoke this workflow as `$asset-spec`.

Use existing authorization for the bounded task. Describe the intended outputs and preserve unrelated work. Ask only about unresolved consequential choices or material scope expansion; do not repeat file- or section-level approval prompts.

Arguments: `[system:<name> | level:<name> | character:<name> | entity:<name>] [--review full|lean|solo]`. Treat bracketed values as optional unless the workflow says otherwise.


If no argument is provided, check whether `design/assets/entity-inventory.md` exists:
- If it exists: read it, find the first entity or screen with status "Needed" but no spec file yet, and ask the user directly:
  - Prompt: "The next unspecced item is **[name]**. Generate specs for it?"
  - Options: `[A] Yes — spec [name]` / `[B] Pick a different item` / `[C] Stop here`
- If no entity inventory: check `design/assets/asset-manifest.md`. If manifest exists, same flow above but reading from manifest.
- If neither exists: **start the Entity & Screen Inventory flow** (Phase 0b below) rather than failing.

---

## Phase 0b: Entity & Screen Inventory (runs when no arguments and no existing inventory)

This flow produces `design/assets/entity-inventory.md` — the master list of everything
the game needs visually. Run once before asset spec work begins.

### Step 1 — Gather from docs
Read all available source material in parallel:
- `design/gdd/BREAKDOWN.md` — extract every system listed
- All GDDs in `design/gdd/` — extract: Visual/Audio Requirements sections, UI elements mentioned, VFX events, any named entities (characters, enemies, buildings, items)
- `design/art/art-bible.md` — extract: any named visual categories, asset type expectations
- `design/narrative/` — scan for any character or world entity documents if they exist (optional — not required)

### Step 2 — Build proposed inventory
Organize everything found into categories:

```
Characters / Protagonists
Enemies / Creatures
Buildings / Structures
Environment / Terrain
Items / Props
VFX / Particles
UI Screens (list each screen by name)
HUD Elements
Audio (SFX, music — descriptions only, no generation prompts)
Other
```

For each item, note the source doc it was found in.

### Step 3 — Present and collaborate
Present the full proposed inventory to the user in conversation. Then ask the user directly:
- Prompt: "I found **[N] visual entities and [N] UI screens** across your GDDs and art bible. Review the list — what's missing, what's not needed?"
- Options:
  - `[A] Looks good — save this inventory`
  - `[B] Add items I'll describe`
  - `[C] Remove items that don't apply`
  - `[D] Both add and remove — let me edit`

If [B] or [D]: ask the user to describe additional items. Accept brief descriptions ("a medieval keep, used as a level background") or detailed ones — either works. Work through them collaboratively until the user is satisfied.

If [C] or [D]: ask which items to remove and why. Remove them from the list.

### Step 4 — Write inventory
Save the inventory within existing bounded task authorization. Clarify unresolved inventory choices before dependent writes; do not request approval again for already-settled scope.

Write the file:

```markdown
# Visual Entity & Screen Inventory

> Generated: [date]
> Sources: [list of source docs read]

## Entities

| # | Name | Type | Description | Source | Status |
|---|------|------|-------------|--------|--------|
| 1 | [name] | Character / Enemy / Building / Environment / Item / Other | [brief description] | [source doc] | Needed |

## UI Screens

| # | Screen Name | Description | Source | Status |
|---|-------------|-------------|--------|--------|
| 1 | Main Menu | [description] | [source] | Needed |

## HUD Elements

| # | Element | Description | Source | Status |
|---|---------|-------------|--------|--------|

## Audio

| # | Name | Type (SFX / Music / Ambient) | Description | Source | Status |
|---|------|------------------------------|-------------|--------|--------|
```

After writing, tell the user:
> "Entity inventory saved. Next steps:
> - Run `$ux-design [screen name]` for each UI screen in the inventory
> - Run `$asset-spec entity:[name]` to spec each visual entity
> - Or run `$asset-spec` again to work through the inventory one item at a time"

Then end this run. The inventory branch never falls through to target parsing or
spec generation with an empty target.

---

## Phase 0: Parse Arguments

Extract:
- **Target type**: `system`, `level`, `character`, or `entity`
- **Target name**: the name after the colon (normalize to kebab-case)
- **Review mode**: a valid `--review [full|lean|solo]` if present; otherwise use
  focused (`lean`) review without reading or creating a review-mode configuration.

Reject an unknown type, empty name, extra target, invalid review value, or a name
that normalizes to empty. Every resolved source path must remain project-local.

**Mode behavior:** `full` adds optional visual and technical specialist breadth;
`lean` uses focused review; `solo` identifies current-agent self-review. All modes
must address applicable visual/technical constraints and retain required independent
review. Use available qualified executors under the current delegation policy.

## Phase 1: Gather Context

Read all source material **before** asking the user anything.

### Required reads:
- **Visual direction**: Read `design/art/art-bible.md` when present, including
  Visual Identity Summary, Art Style/Shape Language, Color Palette and Asset Standards.
  Otherwise use sufficient explicit visual direction from the developer/source brief.
  Record the source; ask for missing consequential direction. A complete art bible is
  optional. Selected direction must cover the asset being specified.
- **Resource mapping**: Link each asset to its system and relevant RES_TYPE/TYPE_TEMP
  when defined, including intended prepared location and import mapping. Unresolved
  contracts can remain explicit in a draft; production readiness requires applicable
  format, identity and consumer constraints to be settled.

- **Technical preferences**: Read `docs/technical-preferences.md` — extract performance budgets and naming conventions.

### Source doc reads (by target type):
Resolve exactly one existing project-local source before reading. For `system` or
`level`, a missing file, directory, non-Markdown file, or multiple normalized
candidate matches stops the run unless the user explicitly supplies a description
as the source. Do not perform a bare read of an unresolved path.

- **system**: Resolve the target through BREAKDOWN and read its declared GDD path. Read the relevant visual/audio requirements by meaning; a matching filename or exact heading is unnecessary. If the required content is absent or only a placeholder:
  > "The Visual/Audio section of `design/gdd/[target-name].md` is empty. Either run `$design-system [target-name]` to complete the GDD, or describe the visual needs manually."
  Ask the user directly: `[A] Describe needs manually` / `[B] Stop — complete the GDD first`
- **level**: Read `design/levels/[target-name].md`. Extract art requirements, asset list, VFX needs, and the art-director's production concept specs from Step 4.
- **character** or **entity**: Read `design/narrative/characters/[target-name].md` or search `design/narrative/` and `design/assets/entity-inventory.md` for a matching entry. Extract visual description, role, and any specified distinguishing features.
  - **If no source doc exists**: do not fail. Instead, ask the user directly:
    - Prompt: "No profile found for **[name]**. Describe it briefly — a sentence or two is enough."
    - Options: `[A] Describe it now` / `[B] Skip this entity` / `[C] Stop here`
    - If [A]: the user's description becomes the source. Brief answers produce concise specs; detailed answers produce detailed specs. Accept whatever level of detail the user provides and work from it.

### Approval status check

Read the source document's actual status and acceptance evidence. If required acceptance is absent or unclear, identify that gap before claiming a production-ready spec. An exploratory draft can still be authored within the requested scope.
A user-provided description may support a clearly partial draft, but it cannot be
called approved or production-ready.

### Optional reads:
- **Existing manifest**: Read `design/assets/asset-manifest.md` if it exists — locate the exact existing context block and IDs for this target.
- **Current target spec**: Read `design/assets/specs/[target]-assets.md` if it exists and map its asset blocks by stable name/ID.
- **Related specs**: Find files matching `design/assets/specs/*.md` — scan for assets that could be shared (e.g., a common UI element specced for one system might apply here too).

On rerun, compute a before/after diff and update the existing target block in
place. Unchanged assets keep their IDs and content; do not append a duplicate
context block or allocate an ID when there is no change.

### Present context summary:
> **Asset Spec: [Target Type] — [Target Name]**
> - Source doc: [path] — [N] asset types identified
> - Visual direction: [actual source and applicable rules]
> - Existing specs for this target: [N already specced / none]
> - Shared assets found in other specs: [list or "none"]

---

## Phase 2: Asset Identification

From the source doc, extract every asset type mentioned — explicit and implied.

**For systems**: look for VFX events, sprite references, UI elements, audio triggers, particle effects, icon needs, and any "visual feedback" language.

**For levels**: look for unique environment props, atmospheric VFX, lighting setups, ambient audio, skybox/background, and any area-specific materials.

**For characters**: look for sprite sheets (idle, walk, attack, death), portrait/avatar, VFX attached to abilities, UI representation (icon, health bar skin).

Group assets into categories:
- **Sprite / 2D Art** — character sprites, UI icons, tile sheets
- **VFX / Particles** — hit effects, ambient particles, screen effects
- **Environment** — props, tiles, backgrounds, skyboxes
- **UI** — HUD elements, menu art, fonts (if custom)
- **Audio** — SFX, music tracks, ambient loops *(note: audio specs are descriptions only — no generation prompts)*
- **3D Assets** — meshes, materials (if applicable per engine)

Present the identified list and distinguish explicit requirements from inferred
candidates. Use the already authorized asset scope. Ask only about unresolved
additions or consequential ambiguity before dependent generation.

---

## Phase 3: Spec Generation

Assign the required visual and technical work to available qualified executors.
The current agent can perform authoring within its capability; required independent
review remains separate. Suggested specialist responsibilities:

- **art-director**: asset description, shape/color/composition rules, relevant references
  and optional generation prompts when useful. Prompts reflect the selected image tool
  rather than assuming one syntax. Audio output describes sound requirements.
- **technical-artist**: dimensions, format/export, naming/identity, selected budgets,
  imports and applicable engine constraints from actual TYPE_TEMP and technical evidence.
  Unknown choices stay unconfigured; do not invent a production size or engine limit.

Compile the available findings and surface unresolved visual/technical conflicts.
A specification or generation prompt does not produce the media. Missing required
technical or independent evidence prevents production-ready status in every mode.

## Phase 4: Compile and Review

Combine the agent outputs into a draft spec per asset. Present all specs in conversation text using this format:

```
## ASSET-[NNN] — [Asset Name]

| Field | Value |
|-------|-------|
| Category | [Sprite / VFX / Environment / UI / Audio / 3D] |
| Dimensions | [e.g. 256×256px, 4-frame sprite sheet] |
| Format | [PNG / SVG / WAV / etc.] |
| Naming | [e.g. vfx_frost_hit_01.png] |
| Polycount | [if 3D — e.g. <800 tris] |
| Texture Res | [e.g. 512px — matches selected TYPE_TEMP budget] |

Retain these useful fields and add the resource type/system mapping and source/output linkage when needed. For animation, record required states in Visual
Description. Put applicable file-size/export limits into Format, dimensions or
frame layout into Dimensions, mesh limits into Polycount, and texture limits into
Texture Res. Mark non-applicable cells `N/A` and unknown required values unresolved.

**Visual Description:**
[2–3 sentences. Specific enough for two artists to produce consistent results.]

**Visual Direction Anchors:**
- Shape Language: [relevant rule applied]
- Color Palette: [color role — e.g. "uses Threat Blue per semantic color rules"]

**Generation Prompt:**
[Ready-to-use prompt. Include: style keywords, composition notes, color palette anchors, lighting direction, negative prompts.]

**Status:** Needed
```

Present the scoped specifications and any unresolved direction choices. Apply settled revisions within existing authorization; preserve required review and identify unverified technical constraints. A change of executor follows the active delegation policy.

---

## Phase 5: Write Spec File

Prepare the complete content for
`design/assets/specs/[target]-assets.md`, but do not write it yet:

```markdown
# Asset Specs — [Target Type]: [Target Name]

> **Source**: [path to source GDD/level/character doc]
> **Visual Direction**: [actual art bible or supplied source]
> **Generated**: [date]
> **Status**: [N] assets specced / [N] approved / [N] in production / [N] done

[all asset specs in ASSET-NNN format]
```

Also prepare the exact update to `design/assets/asset-manifest.md`. If it does
not exist, prepare this initial content, but do not create it yet:

```markdown
# Asset Manifest

> Last updated: [date]

## Progress Summary

| Total | Needed | In Progress | Done | Approved |
|-------|--------|-------------|------|----------|
| [N] | [N] | [N] | [N] | [N] |

## Assets by Context

### [Target Type]: [Target Name]
| Asset ID | Name | Category / Resource Type | Status | Spec File | Referenced By |
|----------|------|--------------------------|--------|-----------|---------------|
| ASSET-001 | [name] | [type] | Needed | design/assets/specs/[target]-assets.md | [contexts] |
```

If the manifest already exists, update the target's existing context block in
place, or append one only when that target has no block. Preserve existing IDs
and update Progress Summary counts without duplicating rows.

Present both the complete spec file and the exact manifest create/edit together
within the bounded authorized changeset, listing both paths. Use existing authorization,
then write both files and verify their content. If authorization is withheld, neither file
changes. Never write the spec first and discover or preview the manifest edit
afterward.

---

## Phase 6: Close

Report actual saved outputs, unresolved decisions and available next steps. Optional follow-up choices:
- Prompt: "Asset specs complete for **[target]**. What's next?"
- Options:
  - `[A] Spec another system — $asset-spec system:[next-system]`
  - `[B] Spec a level — $asset-spec level:[level-name]`
  - `[C] Spec a character — $asset-spec character:[character-name]`
  - `[D] Run $asset-audit — validate delivered assets against specs`
  - `[E] Stop here`

---

## Asset ID Assignment

Asset IDs are assigned sequentially across the entire project — not per-context. Read the manifest before assigning IDs to find the current highest number:

```
Search `design/assets/asset-manifest.md` for `ASSET-`.
```

Start new assets provisionally from `ASSET-[highest + 1]`. Immediately before
the first write, re-read the manifest and shared mappings. If the highest ID or
reusable assets changed, recalculate IDs and identify the affected spec and
manifest lines; never overwrite or duplicate an ID.

If no manifest exists yet, start from `ASSET-001`.

---

## Shared Asset Protocol

Before speccing an asset, check if an equivalent already exists in another context's spec:

- Common UI elements (health bars, score displays) are often shared across systems
- Generic environment props may appear in multiple levels
- Character VFX (hit sparks, death effects) may reuse a base spec with color variants

If a match is found: reference the existing ASSET-ID rather than creating a duplicate. Note the shared usage in the manifest's referenced-by column.

> "ASSET-012 (Generic Hit Spark) already specced for Combat system. Reusing for Tower Defense — adding tower-defense to referenced-by."

---

## Error Recovery Protocol

If any spawned agent returns BLOCKED or cannot complete:

1. Surface immediately: "[AgentName]: BLOCKED — [reason]"
2. In `lean` mode or if `technical-artist` blocks: a partial draft may use art-director output only, but its existing Status/summary must say technical constraints are unverified
3. In `solo` mode or if `art-director` blocks: a partial draft may derive descriptions from explicit selected direction, and its existing Status/summary must say art direction was not reviewed
4. If required visual or technical constraints are missing, do not offer `Approve all` or label the result production-ready; preserve the partial work as visibly unverified

---

## Collaborative Protocol

Identify the scope, resolve consequential choices, generate and assess the requested specifications, then save within existing authorization. Preserve separately required acceptance and review.

- Use the supplied asset scope; clarify unresolved scope choices
- Cite selected visual rules and resolve conflicts with applicable contracts
- Surface all agent disagreements — do not silently pick one
- Write within existing bounded task authorization
- Update the manifest immediately after writing the spec

---

## Recommended Next Steps

- Run `$asset-spec [next-context]` to continue speccing remaining systems, levels, or characters
- Run `$asset-audit` to validate delivered assets against the written specs and identify gaps or mismatches

Spec approval, delivered-file status and asset acceptance are distinct. Preserve the
manifest vocabulary; writing a spec leaves the resource Needed until actual production
evidence supports a change. Shared assets retain one ID across context references.
