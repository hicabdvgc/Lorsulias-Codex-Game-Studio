---
name: brainstorm
description: "Explore game ideas, experience goals, constraints and research questions to support a developer-authored concept."
---

# Brainstorm

Invoke as `$brainstorm`.

Arguments: `[genre or theme hint | open] [--review full|lean|solo]`.

## Shared execution boundary

Read the relevant artifacts before asking about information they contain. Existing
bounded task authorization covers its edits and verification; ask about unresolved
consequential choices or a material scope expansion. Preserve unrelated changes
and re-read a target before writing if its baseline may have changed.

Use available qualified executors under the current environment's delegation
policy. Role names describe expertise. Follow `.codex/docs/review-workflow.md`
and `.codex/docs/director-gates.md`: required independent review and human evidence
remain required with any executor. Identify self-review; unavailable required
evidence is NOT ASSESSED. Review-depth flags change optional breadth, never these
obligations. `full` adds applicable specialist/gate reviews; `lean` is focused;
`solo` identifies self-review. Default to focused review when unspecified.

Apply `.codex/docs/skill-authoring.md` and `.codex/docs/error-recovery-protocol.md`.
Verify promised saved outputs before handoff. Resolve available support from the
installed catalog; require an input only when the selected activity needs its outcome.


## Explore the developer's intent

Read existing CONCEPT, studies and decisions if present. Ask only about missing
intent that matters: memorable play experiences, desired fantasy, liked/disliked
genres, relevant experience, actual constraints and commitments. Synthesize a
creative brief that distinguishes supplied facts, choices and open questions.

Use the source's useful ideation techniques as appropriate:
- **Verb-first:** start with the player's actions and build the experience around them.
- **Mashup:** combine a genre and an unexpected theme; explain what the combination adds.
- **Experience-first:** work backward from intended aesthetics through dynamics to mechanics.

Present sufficiently distinct options to support the actual choice. For each,
explain the pitch, core actions, intended experience, distinctive hook, scope
drivers and biggest uncertainty. Let the developer select, combine or revise.
Do not impose a number of concepts, pillars, questions or sentences.

## Develop the chosen direction

Discuss the moment-to-moment actions, meaningful decisions, applicable short-term
and session loops, progression if relevant, feedback, and intended player context.
Autonomy, competence, relatedness and player-motivation frameworks are analytical
prompts, not evidence that an audience will enjoy the design. Commercial claims
need actual sources; unknown audience size or feasibility remains unknown.

Record meaningful pillars and exclusions, and tensions the developer must resolve.
Use the optional game-pillars, player-journey and difficulty-curve templates when
they help the requested exploration. Apply CD-PILLARS when that review is requested;
missing visual expertise does not authorize inventing art-director approval.

## Prepare research and manual concept authorship

Use `.codex/docs/templates/reference-game-study.md` to identify supporting research,
reference games, study questions and actual developer play still needed. Root-level
`game_ref/` stores studies and evidence. AI research cannot substitute for play.

Return a creative brief, considered options, developer choices, constraints,
evidence gaps and next preparation activity. Keep these in conversation by default;
save supporting notes only when requested, naming their destination separately.
Never generate or overwrite the authoritative `design/gdd/CONCEPT.md`: the developer
writes it manually using the game-concept aid if helpful.

After a usable CONCEPT and preparation evidence exist, `$map-systems` can produce
the preliminary BREAKDOWN. `$setup-engine` supports technical selection when needed.
`$prototype` is an optional experiment for a specific uncertainty, not a required stage.
