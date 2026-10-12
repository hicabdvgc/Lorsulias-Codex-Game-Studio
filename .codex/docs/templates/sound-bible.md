# Sound Bible: [Project Name]

Complete the sections relevant to this design; identify omitted topics and their
reason when the reader would otherwise expect them. Examples are illustrative.
Use developer CONCEPT, applicable GDD/FRAMEWORK decisions and `docs/ACCESSIBILITY.md`.
Read live `docs/technical-preferences.md` for selected technical choices. Link resource
requirements to RES_TYPE/TYPE_TEMP when defined; record unresolved needs in early
design. This design document does not substitute for a resource schema or delivered
resource. Save and accept within actual task authorization and required evidence.

## Audio Vision

### Sonic Identity
[Describe the overall audio personality of the game at the detail needed by the recipient. What does the game "sound like"? What emotions should the audio evoke?]

### Audio Pillars
1. **[Pillar 1]**: [How this pillar manifests in audio]
2. **[Pillar 2]**: [How this pillar manifests in audio]
3. **[Pillar 3]**: [How this pillar manifests in audio]

### Reference Games / Media
| Reference | What to Take From It | What to Avoid |
| ---- | ---- | ---- |
| [Game/Film 1] | [Specific audio quality to emulate] | [What doesn't fit our vision] |
| [Game/Film 2] | [Specific audio quality to emulate] | [What doesn't fit our vision] |

---

## Music Direction

### Style and Genre
[Primary musical style, instrumentation palette, tempo ranges]

### Instrumentation Palette
- **Core instruments**: [List the primary instruments/synths that define the sound]
- **Accent instruments**: [Used for emphasis, transitions, special moments]
- **Avoid**: [Instruments or styles that do NOT fit the game]

### Adaptive Music System
| Game State | Music Behavior | Transition |
| ---- | ---- | ---- |
| [Applicable state] | [Selected behavior] | [Trigger and transition] |

### Music Rules
- [Rule about looping, e.g., "All exploration tracks must loop seamlessly after 2-4 minutes"]
- [Rule about silence, e.g., "Allow 10-15 seconds of silence between exploration loops"]
- [Rule about intensity, e.g., "Combat music must reach full intensity within 3 seconds of combat start"]
- [Rule about transitions, e.g., "All music transitions use 1.5 second crossfades"]

---

## Sound Effects

### SFX Palette
| Category | Description | Style Notes |
| ---- | ---- | ---- |
| Player Actions | [Movement, attacks, abilities] | [Punchy, responsive, front-of-mix] |
| Enemy Actions | [Attacks, abilities, death] | [Distinct from player, slightly recessed] |
| UI | [Button clicks, menu transitions, notifications] | [Clean, subtle, never annoying on repeat] |
| Environment | [Ambient loops, weather, objects] | [Immersive, layered, spatial] |
| Feedback | [Damage taken, item pickup, level up] | [Clear, satisfying, non-fatiguing] |

### Audio Feedback Priority
[Define priority and conflict behavior for the actual cues and player needs. Cite the applicable accessibility commitments.]

### SFX Rules
- [Rule about repetition, e.g., "Every SFX with >3 plays/minute needs 3+ variations"]
- [Rule about spatial audio, e.g., "All gameplay SFX must be 3D positioned, UI SFX are 2D"]
- [Rule about ducking, e.g., "Player hit SFX ducks all other SFX by 3dB for 200ms"]
- [Rule about response time, e.g., "Action SFX must trigger within 1 frame of the action"]

---

## Mixing

### Mix Bus Structure
| Bus | Content | Target Level |
| ---- | ---- | ---- |
| [Selected bus, if used] | [Content] | [Selected target and unit] |

### Mixing Rules
[Specify selected masking/ducking, clipping evaluation, player controls and output-device expectations, with rationale and methods. No bus topology or mix value is preselected.]

### Dynamic Range
- [Specify loudness targets, e.g., "Target -14 LUFS integrated, -1 dBTP true peak"]
- [Specify compression policy, e.g., "Light compression on SFX bus, no compression on music"]

---

## Technical Specifications

### Format Requirements
| Type | Format | Sample Rate | Bit Depth | Notes |
| ---- | ---- | ---- | ---- | ---- |
| Music | [selected format] | [selected rate] | [selected depth] | [selected loading/streaming behavior] |
| SFX | [selected format] | [selected rate] | [selected depth] | [selected loading/streaming behavior] |
| Ambient | [selected format] | [selected rate] | [selected depth] | [selected loading/streaming behavior] |
| Dialogue | [selected format] | [selected rate] | [selected depth] | [selected loading/streaming behavior] |

### Naming Convention
[Link the selected audio TYPE_TEMP naming and identity contract.]

### Memory Budget
- Total audio memory: [selected target, unit and evidence]
- SFX pool: [target]
- Music streaming buffer: [target]
- Voice streaming buffer: [target]

---

## Accessibility
[Map meaningful cues to the project's selected alternative feedback, subtitles,
controls and sensitivity requirements in docs/ACCESSIBILITY.md. Record evaluation
methods and actual human/listening evidence separately from proposed design.]
