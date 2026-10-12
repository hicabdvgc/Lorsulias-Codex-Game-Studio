---
name: prototype
description: "Build a bounded HTML, engine, paper, or technical-spike experiment and report actual evidence, limitations and retention decisions."
---

# Prototype

Invoke as `$prototype`.

Arguments: `[concept-description] [--path html|engine|paper] [--review full|lean|solo] [--spike]`.

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


## Define the experiment

Read [references/continued-workflow.md](references/continued-workflow.md), including
spike routing, before starting. If --spike is supplied, enter the technical-spike
route directly. Reject invalid flags, conflicting path choices or unsafe output
slugs. Use `prototypes/[slug]-concept/` or `prototypes/[slug]-spike/`; preserve any
existing experiment unless its requested revision is clear.

Identify a bounded hypothesis, its riskiest assumption and a feasible observation.
Read the concept description or existing developer CONCEPT, relevant designs,
preferences and available evidence. Ask for the specific question if it is too vague.
An experiment does not require the final design/architecture it is intended to inform.

## Choose a suitable route

- **HTML:** browser-playable interaction or logic experiment; default output
  prototype.html within the experiment. Browser evidence applies to that environment.
- **Engine:** project/native experiment where actual target rendering, physics or
  interaction is material. Requires a usable selected runtime to execute.
- **Paper:** rules/scenarios with a play log; suitable for exploring decisions without
  engine setup. Simulation and actual human play are distinct.

Honor a supplied route. Explain a concrete mismatch between the route and hypothesis
before proceeding if it would invalidate the experiment. Avoid universal browser
latency figures, genre mandates, or installing a framework solely for convenience.

## Build, observe and report

Plan the smallest experiment capable of answering the question. Identify inputs,
written files, shortcuts, run instructions, duration constraint if supplied, and
required human participation. Carry out the authorized build; run applicable checks
with available tools. Engine interaction, screenshots and play results must be
actually observed. If a runtime or human session is unavailable, preserve the build
and report the unanswered part rather than claiming successful validation.

Use the prototype-report template for REPORT.md, with actual observations and
CONFIRMED / PARTIALLY CONFIRMED / REFUTED / NOT ASSESSED. Record a reasoned
PROCEED / PIVOT / KILL / NOT ASSESSED recommendation and explicit retention choice.
Continue with the report/index and handoff procedure in the reference.
