# Level: [Level Name]

Complete the sections relevant to this design; identify omitted topics and their
reason when the reader would otherwise expect them. Examples are illustrative.
Use developer CONCEPT, applicable GDD/FRAMEWORK decisions and `docs/ACCESSIBILITY.md`.
Read live `docs/technical-preferences.md` for selected technical choices. Link resource
requirements to RES_TYPE/TYPE_TEMP when defined; record unresolved needs in early
design. This design document does not substitute for a resource schema or delivered
resource. Save and accept within actual task authorization and required evidence.

## Quick Reference

- **Area/Region**: [Where in the game world]
- **Type**: [Combat / Exploration / Puzzle / Hub / Boss / Mixed]
- **Estimated Play Time**: [X-Y minutes]
- **Difficulty**: [Project-selected measure and reference]
- **Prerequisite**: [What the player must have done to reach this level]
- **Status**: [Concept | Layout | Graybox | Art Pass | Polish | Final]

## Narrative Context

- **Story Moment**: [Where in the narrative arc does this level occur]
- **Narrative Purpose**: [What story beat this level delivers]
- **Emotional Target**: [What the player should feel during this level]
- **Lore Discoveries**: [What world-building the player can find here]

## Layout

### Overview Map

```
[ASCII diagram of the level layout. Use these symbols:]
[S] = Start point
[E] = Exit/end point
[C] = Combat encounter
[P] = Puzzle
[R] = Reward/loot
[!] = Story beat
[?] = Secret/optional
[>] = One-way passage
[=] = Two-way passage
[@] = NPC
[B] = Boss encounter
```

### Critical Path

[The intended route or traversal model; open/nonlinear spaces may have multiple valid paths.]

1. Player enters at [S]
2. [Description of what happens along the path]
3. Player exits at [E]

### Optional Paths

| Path | Access Requirement | Reward | Discovery Hint |
|------|-------------------|--------|---------------|

### Points of Interest

| Location | Type | Description | Purpose |
|----------|------|-------------|---------|

## Encounters

### Combat Encounters

| ID | Position | Enemy Composition | Difficulty | Arena Notes |
|----|----------|------------------|-----------|-------------|
| E-01 | [Map ref] | [2x Grunt, 1x Ranged] | 3/10 | Open area, cover on flanks |
| E-02 | [Map ref] | [1x Elite, 3x Grunt] | 5/10 | Narrow corridor, no retreat |

### Non-Combat Encounters

| ID | Position | Type | Description | Solution Hint |
|----|----------|------|-------------|---------------|

## Pacing Chart

```
Intensity
10 |                              *
 8 |                         *   * *
 6 |            *  *        * * *   *
 4 |     *  *  * ** *   *  *
 2 | * ** ** *        * * *          *
 0 |S-----------------------------------------E
     [Start]    [Mid]              [Climax] [Exit]
```

[Describe the intended rhythm: where are the peaks, valleys, rest points?]

## Audio Direction

| Zone/Moment | Music Track | Ambience | Key SFX |
|-------------|------------|----------|---------|
| [Entry] | [Track] | [Ambient sounds] | [Door opening] |
| [Combat] | [Combat music] | [Muted ambience] | [Combat SFX] |
| [Post-combat] | [Calm transition] | [Return to ambience] | |

## Visual Direction

- **Lighting**: [Key, fill, ambient description]
- **Color Palette**: [Dominant colors and why]
- **Mood Board References**: [Description of visual references]
- **Landmarks**: [Visible navigation aids and their locations]
- **Sight Lines**: [What the player should see from key positions]

## Collectibles and Secrets

| Item | Location | Visibility | Hint | Required For |
|------|----------|-----------|------|-------------|

## Technical Notes

- **Estimated Object Count**: [N]
- **Streaming Zones**: [Where to break the level for streaming]
- **Performance Concerns**: [Any known heavy areas]
- **Required Systems**: [What game systems are active in this level]

## Integration and Resource Requirements
[Link affected systems, framework operations, shared/unique resource identities,
TYPE_TEMP definitions when available, and unresolved adjacent-area connections.]

## QA and Acceptance
| Required outcome | Evaluation method | Evidence / result | Remaining work |
|---|---|---|---|
| [Design, navigation, accessibility or play experience] | [Inspection, execution, human play] | [Pending until performed] | [Dependency] |

A saved design is distinct from a graybox, implemented level or successful playtest.
