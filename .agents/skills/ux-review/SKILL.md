---
name: ux-review
description: "Validates a UX spec, HUD design, or interaction pattern library for completeness, accessibility compliance, GDD alignment, and implementation readiness. Produces APPROVED / NEEDS REVISION / MAJOR REVISION NEEDED verdict with specific gaps."
---

Read `.codex/docs/resource-preparation.md` for resource locations, shared write,
review/evidence and recovery requirements. Its shared handoff rules apply here;
initial design can record future resource needs before type contracts exist.

## Invocation and execution

Invoke this workflow as `$ux-review`.

Arguments: `[file-path or 'all' or 'hud' or 'patterns']`. Treat bracketed values as optional unless the workflow says otherwise.

Use available qualified `ux-designer` expertise when useful and delegation is authorized. Otherwise perform the applicable responsibilities in the current agent, preserving required independence and human evidence.


## Overview

Validates UX design documents before they enter the implementation pipeline.
Supports the workflow's UX activity and relevant integration review. `$team-ui` supplies scoped implementation support.

**Run this skill:**
- After completing a UX spec with `$ux-design`
- Before handing off to `ui-programmer` or `art-director`
- Before the selected UX deliverable is consumed by implementation or the vertical-slice work
- After major revisions to a UX spec

**Verdict levels:**
- **APPROVED** — the selected design-review requirements are satisfied by available evidence; separate implementation/readiness obligations still apply
- **NEEDS REVISION** — specific gaps found; fix before handoff but not a full redesign
- **MAJOR REVISION NEEDED** — fundamental issues with scope, player need, or
  completeness; needs significant rework

---

## Phase 1: Parse Arguments

- **Specific file path** (e.g., `$ux-review design/ux/inventory.md`): validate
  that one document
- **`all`**: find all files in `design/ux/` and validate each
- **`hud`**: validate `design/ux/hud.md` specifically
- **`patterns`**: validate `design/ux/interaction-patterns.md` specifically
- **No argument**: ask the user which spec to validate

For a specific path, require an existing project-local regular Markdown file
directly under `design/ux/`. Reject missing paths, directories, non-Markdown files,
path traversal, and project-external paths; echo the rejected path and stop without
running a checklist or issuing a verdict. `hud`/`patterns` resolve only to their
fixed paths.

Route each file before review. The two reserved paths are `design/ux/hud.md` (HUD) and `design/ux/interaction-patterns.md` (pattern library). Any other candidate must match the header contract of `.codex/docs/templates/ux-spec.md`; otherwise report it as unsupported and issue no verdict. `all` reviews and summarizes only these three supported types, with unsupported Markdown listed separately.

---

## Phase 2: Load Cross-Reference Context

Before validating any spec, load the authoritative template for its routed type: `.codex/docs/templates/ux-spec.md`, `.codex/docs/templates/hud-design.md`, or `.codex/docs/templates/interaction-pattern-library.md`. Use its applicable information needs with the actual GDD, FRAMEWORK and resource contracts. Equivalent headings are valid; no section-count score proves completeness.

Then load:

1. **Input & Platform config**: Read `docs/technical-preferences.md` and
   extract `## Input & Platform`. This is the authoritative source for which input
   methods the game supports — use it to drive the Input Method Coverage checks in
   Phase 3A, not the spec's own header. If unconfigured, review only the spec's
   internal consistency and report `authoritative input unknown`; the reviewed
   document cannot prove the project's supported inputs. Never infer inputs from
   PC/console/mobile platform labels.
2. Applicable commitments and evaluation methods in `docs/ACCESSIBILITY.md`. Missing required decisions/evidence remain NOT ASSESSED; no preset tier or certification claim is inferred.
3. The interaction pattern library at `design/ux/interaction-patterns.md` (if
   it exists)
4. The GDDs referenced in the spec's header (read their UI Requirements sections),
   plus explicit references to the screen/HUD identity found in existing GDD UI
   Requirements. If this cannot establish a complete set, state the coverage scope
   limitation rather than claiming no requirements are missing.
5. The player journey map at `design/player-journey.md` (if it exists) for
   context-arrival validation

---

## Phase 3: Template-Routed Validation

For each supported file, compare it against the current authoritative template selected in Phase 1. Check applicable behavior, information and evidence; explain omissions or unassessed requirements.

- **UX spec**: validate purpose/player need, arrival context, navigation and entry/exit, layout/component inventory, applicable states, interactions for configured inputs, data ownership, accessibility, localization, and acceptance criteria.
- Loading state is required only when the screen has async data or a user-visible delay; a purely synchronous screen records N/A without losing completeness.
- Basic navigation, feedback, error, and accessibility controls may be justified by UX requirements even when a GDD does not list them. Flag only UI that invents or changes unauthorized gameplay state.
- **HUD**: derive applicable gameplay contexts from the game concept/GDD, then validate the HUD template's information architecture, those contexts, layout zones, element specs, feedback, visual budget, platform adaptation, tuning knobs, accessibility, and acceptance criteria. Nonexistent contexts are N/A.
- **Pattern library**: validate the pattern template's catalog and entries (including the existing `Tab Bar` name), only controls/patterns actually used by current specs/platforms, navigation/loading/error patterns, animation/sound standards, accessibility, and internal consistency. Unused pattern types are N/A. For every pattern named by the current spec, locate a complete persisted entry in `design/ux/interaction-patterns.md` and compare behavior; unwritten/placeholder shared entries leave the dependent conclusion unassessed. A complete local interaction specification need not reference the shared library. Remain read-only and never promote a draft.

Evaluate the relevant outcomes and identify missing evidence. An unsupported document receives a scope error, without a fabricated completeness score.
## Phase 4: Output the Verdict

```markdown
## UX Review: [Document Name]
**Date**: [date]
**Reviewer**: [actual reviewer; self/independent and method]
**Document**: [file path]
**Platform Target**: [from header]
**Accessibility Commitments**: [docs/ACCESSIBILITY.md references]

### Applicable requirements and evidence
- [x] Purpose & Player Need
- [ ] States & Variants — MISSING: error state not documented

### Quality Issues: [N found]
1. **[Issue title]** [BLOCKING / ADVISORY]
   - What's wrong: [specific description]
   - Where: [section name]
   - Fix: [specific action to take]

### GDD Alignment: [ALIGNED / GAPS FOUND]
- GDD [name] UI Requirements — [X/Y requirements covered]
- Missing: [list any uncovered GDD requirements]

### Accessibility: [COMPLIANT / GAPS / NON-COMPLIANT / NOT ASSESSED]
- Selected commitments: [requirements]
- [list specific accessibility findings]

### Pattern Library: [CONSISTENT / INCONSISTENCIES FOUND]
- [findings]

### Verdict: APPROVED / NEEDS REVISION / MAJOR REVISION NEEDED / NOT ASSESSED
**Blocking issues**: [N] — must be resolved before implementation
**Advisory issues**: [N] — recommended but not blocking

Verdict mapping is deterministic:
- **APPROVED**: every applicable required check has evidence and zero blockers. Advisory findings do not lower the verdict. Missing required independent/human review prevents APPROVED.
- **NEEDS REVISION**: one or more localized, fixable blockers with the document's purpose, main flow, input contract, and data ownership otherwise coherent.
- **MAJOR REVISION NEEDED**: Purpose/Player Need is missing; the main flow, input behavior, or data ownership contradicts itself; or multiple core sections from the routed template are substantively missing.

- **NOT ASSESSED**: required evidence is unavailable and no demonstrated revision verdict takes precedence. Preserve known blockers alongside missing evidence.

Always list actual reviewer/method, coverage, blocker locations and evidence gaps. Then use the matching handoff:

[For APPROVED]: Report the scope satisfied and remaining resource, runtime, human and workflow prerequisites before implementation.

[For NEEDS REVISION]: Address the [N] blocking issues above, then re-run
`$ux-review`.

[For MAJOR REVISION NEEDED]: The spec has fundamental gaps in [areas].
Recommend returning to `$ux-design` to rework [sections].
```

---

## Phase 5: Collaborative Protocol

Return findings in conversation by default. Save only an explicitly requested bounded report; do not edit the reviewed designs or their acceptance status.

After delivering the verdict:
- For **APPROVED**: identify the next implementation activity and use installed `$team-ui` for authorized implementation
- For **NEEDS REVISION**: offer to help fix specific gaps ("Would you like me to
  help draft the missing error state?") — but do not auto-fix; wait for user
  instruction
- For **MAJOR REVISION NEEDED**: suggest returning to `$ux-design` with the
  specific sections to rework

The review remains read-only and the user may end it and make a separate product
decision, but NEEDS REVISION/MAJOR REVISION NEEDED is never relabeled APPROVED or
described as implementation-ready. Downstream work must preserve the verdict, scope and missing evidence. `$team-ui` is installed and must preserve these review obligations.
