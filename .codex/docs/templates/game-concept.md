# Game Concept: [Working Title]

Developer-filled aid for `design/gdd/CONCEPT.md`. AI may ask questions, research,
and review; it does not write the authoritative concept for the developer.
Optional prompts below apply when relevant to this game.


*Created: [Date]*
*Status: [Draft / Under Review / Approved]*

---

## Elevator Pitch

> [1-2 sentences that capture the entire game. Should be compelling enough to
> make someone want to hear more. Format: "It's a [genre] where you [core
> action] in a [setting] to [goal]."
>
> Test: Can someone who has never heard of this game understand what they'd
> be doing in 10 seconds? If not, simplify.]

---

## Core Identity

| Aspect | Detail |
| ---- | ---- |
| **Genre** | [Primary genre + subgenre(s)] |
| **Platform** | [PC / Console / Mobile / Cross-platform] |
| **Target Audience** | [See Player Profile section below] |
| **Player Count** | [Single-player / Co-op / Multiplayer / MMO / Unknown] |
| **Session Length** | [Typical play session: 10 min / 30 min / 1 hr / 2+ hr] |
| **Monetization** | [Premium / F2P / Subscription / None / Unknown] |
| **Estimated Scope** | [Chosen boundaries and capacity evidence, or Unknown] |
| **Comparable Titles** | [2-3 existing games in the same space] |

---

## Core Fantasy

[What power, experience, or feeling does the player get from this game?
What can they do here that they can't do anywhere else?

The core fantasy is the emotional promise. It's not a feature list — it's the
answer to "why would someone choose THIS game over anything else they could
be doing?"

Examples of strong core fantasies:
- "You are a lone survivor building a new life in a hostile wilderness" (survival)
- "You command a civilization across millennia" (strategy)
- "You explore a vast, beautiful world at your own pace" (open world)
- "You master intricate combat and overcome impossible odds" (soulslike)]

---

## Unique Hook

[What makes this game different from everything else in its genre? This is
the single most important differentiator.

A strong hook passes the "and also" test: "It's like [comparable game],
AND ALSO [unique thing]." If the "and also" doesn't spark curiosity, the
hook needs work.

The hook should be:
- Explainable in one sentence
- Genuinely novel (not just a combination of existing features)
- Connected to the core fantasy (not a gimmick bolted on)
- Something that affects gameplay, not just aesthetics]

---

## Player Experience Analysis (MDA Framework)

The MDA (Mechanics-Dynamics-Aesthetics) framework ensures we design from the
player's emotional experience backward to the systems that create it.

### Target Aesthetics (What the player FEELS)
Rank the following aesthetic goals for this game (1 = primary, mark N/A if not
relevant). These come from the MDA framework's 8 aesthetic categories:

| Aesthetic | Priority | How We Deliver It |
| ---- | ---- | ---- |
| **Sensation** (sensory pleasure) | [1-8 or N/A] | [Visual beauty, audio design, haptics] |
| **Fantasy** (make-believe, role-playing) | [Priority] | [World, characters, player identity] |
| **Narrative** (drama, story arc) | [Priority] | [Plot structure, player-driven stories] |
| **Challenge** (obstacle course, mastery) | [Priority] | [Difficulty curve, skill ceiling] |
| **Fellowship** (social connection) | [Priority] | [Co-op, guilds, shared experiences] |
| **Discovery** (exploration, secrets) | [Priority] | [Hidden areas, emergent systems, lore] |
| **Expression** (self-expression, creativity) | [Priority] | [Build variety, cosmetics, creation tools] |
| **Submission** (relaxation, comfort zone) | [Priority] | [Low-stress loops, ambient gameplay] |

### Key Dynamics (Emergent player behaviors)
[What behaviors do we WANT to emerge from our mechanics? What should players
naturally start doing without being told?

Example: "Players will experiment with ability combinations to find synergies"
Example: "Players will share discoveries with the community"]

### Core Mechanics (Systems we build)
[What are the mechanical systems that generate the dynamics and aesthetics
above? These are the rules, verbs, and systems we actually implement.]

1. [Mechanic 1 — e.g., "Real-time combat with stamina management"]
2. [Mechanic 2 — e.g., "Procedurally generated dungeons with hand-crafted rooms"]
3. [Mechanic 3 — e.g., "Crafting system with discoverable recipes"]

---

## Player Motivation Profile

Understanding WHY players play helps us make every design decision. Based on
Self-Determination Theory (SDT) and the Player Experience of Need Satisfaction
(PENS) model.

### Primary Psychological Needs Served

| Need | How This Game Satisfies It | Strength |
| ---- | ---- | ---- |
| **Autonomy** (freedom, meaningful choice) | [How does the player feel in control?] | [Core / Supporting / Minimal] |
| **Competence** (mastery, skill growth) | [How does the player feel skilled?] | [Core / Supporting / Minimal] |
| **Relatedness** (connection, belonging) | [How does the player feel connected?] | [Core / Supporting / Minimal] |

### Player Type Appeal (Bartle Taxonomy)

Use this taxonomy only if useful for this game; these are hypotheses, not measured player identities. Which motivations are relevant?

- [ ] **Achievers** (goal completion, collection, progression) — How: [...]
- [ ] **Explorers** (discovery, understanding systems, finding secrets) — How: [...]
- [ ] **Socializers** (relationships, cooperation, community) — How: [...]
- [ ] **Killers/Competitors** (domination, PvP, leaderboards) — How: [...]

### Flow State Design

Treat challenge/skill fit as a design hypothesis. How will you evaluate engagement?

- **Onboarding curve**: [How does the opening interaction teach the player?]
- **Difficulty scaling**: [How does challenge grow with player skill?]
- **Feedback clarity**: [How does the player know they're improving?]
- **Recovery from failure**: [How quickly can they try again? Is failure punishing or educational?]

---

## Core Loop

### Moment-to-Moment
[What is the player physically doing most of the time? The most basic, repeated
action. Describe its intended experience and how play could test that intention.]

### Short-Term
[What objective or cycle structures the moment-to-moment play? Encounters,
puzzles, rounds, quests. This is where "one more turn" or "one more run"
psychology lives.]

### Session-Level
[What does a full play session look like? What does the player accomplish?
Describe relevant stopping points; repeated-session retention is optional.]

### Long-Term Progression
[If sustained progression is intended, how does it work? Character progression, unlocks,
story advancement, mastery. What is the player working toward?]

### Retention Hooks
[What specifically brings the player back for their next session?]
- **Curiosity**: [Unanswered questions, unexplored areas, locked content]
- **Investment**: [Progress they don't want to lose, characters they care about]
- **Social**: [Friends playing, guild obligations, shared goals]
- **Mastery**: [Skills to improve, challenges to overcome, rankings to climb]

---

## Game Pillars

Design pillars are non-negotiable principles that guide EVERY decision. When
two design choices conflict, compare their effects against the selected pillars.
Use as many distinct principles as the project needs; record unresolved tensions.

### Pillar 1: [Name]
[One sentence defining this non-negotiable design principle.]

*Design test*: [A concrete decision this pillar would resolve. "If we're
debating between X and Y, this pillar says we choose __."]

### Pillar 2: [Name]
[Definition]

*Design test*: [Decision it resolves]

### Pillar 3: [Name]
[Definition]

*Design test*: [Decision it resolves]

### Anti-Pillars (What This Game Is NOT)

Anti-pillars are equally important — they prevent scope creep and keep the
vision focused. Every "no" protects the "yes."

- **NOT [thing]**: [Why this is explicitly excluded and what it would compromise]
- **NOT [thing]**: [Why]
- **NOT [thing]**: [Why]

---

## Inspiration and References

| Reference | What We Take From It | What We Do Differently | Why It Matters |
| ---- | ---- | ---- | ---- |
| [Game 1] | [Specific mechanic, feeling, or approach] | [Our twist] | [What it validates about our concept] |
| [Game 2] | [What we learn] | [Our twist] | [Validation] |
| [Game 3] | [What we learn] | [Our twist] | [Validation] |

**Non-game inspirations**: [Films, books, music, art, real-world experiences
that influence the tone, world, or feel. Great games often pull from outside
the medium.]

---

## Target Player Profile

[Be specific. "Gamers" is not a target audience.]

| Attribute | Detail |
| ---- | ---- |
| **Age range** | [e.g., 18-35, or Unknown] |
| **Gaming experience** | [Casual / Mid-core / Hardcore] |
| **Time availability** | [e.g., "30-minute sessions on weeknights, longer on weekends"] |
| **Platform preference** | [Where they play most] |
| **Current games they play** | [2-3 user-provided titles, or Unknown] |
| **What they're looking for** | [The unmet need this game fills] |
| **What would turn them away** | [Dealbreakers for this audience] |

---

## Technical Considerations

| Consideration | Assessment |
| ---- | ---- |
| **Engine Preference** | [Godot / Unity / Unreal / Undecided — `$setup-engine` owns any later recommendation] |
| **Key Technical Challenges** | [What's technically hard about this game?] |
| **Art Style** | [Pixel / 2D / 2.5D / 3D stylized / 3D realistic] |
| **Art Pipeline Complexity** | [Low (asset store + modifications) / Medium (custom 2D) / High (custom 3D)] |
| **Audio Needs** | [Minimal / Moderate / Music-heavy / Adaptive] |
| **Networking** | [None / P2P / Client-Server / Dedicated Servers] |
| **Content Volume** | [Estimate: X levels, Y items, Z hours of gameplay] |
| **Procedural Systems** | [Any procedural generation? What scope?] |

---

## Risks and Open Questions

### Design Risks
[Things that could make the game unfun or uncompelling]
- [Risk 1 — e.g., "Core loop may not sustain sessions > 30 minutes"]
- [Risk 2 — e.g., "Player motivation unclear after main story ends"]

### Technical Risks
[Things that could be hard or impossible to build]
- [Risk 1 — e.g., "Procedural generation quality is unproven"]
- [Risk 2 — e.g., "Networking for 100+ players may require dedicated infrastructure"]

### Market Risks
[Things that could prevent commercial success]
- [Risk 1 — e.g., "Genre is saturated with established competitors"]
- [Risk 2 — e.g., "Target audience may be too niche for financial sustainability"]

### Scope Risks
[Things that could blow the timeline]
- [Risk 1 — e.g., "Content volume exceeds team capacity"]
- [Risk 2 — e.g., "Feature X depends on technology we haven't prototyped"]

### Open Questions
[Things that need prototyping or research before we can answer]
- [Question 1 — and how we plan to answer it]
- [Question 2 — and what prototype would resolve it]

---

## Scope and Preparation

[Record chosen constraints and commitments, supporting research, reference-game
studies still needed, and open feasibility questions. Milestones are defined later
in MILESTONE; any early scope suggestion is provisional.]

## Next Steps

The developer writes `design/gdd/CONCEPT.md` manually. Use the reference-study
template for root-level `game_ref/`; then use `$map-systems` for the preliminary
BREAKDOWN. An experiment is optional when it answers a specific uncertainty.
