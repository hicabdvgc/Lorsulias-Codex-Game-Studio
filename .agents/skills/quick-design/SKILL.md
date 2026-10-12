---
name: quick-design
description: "Create an independent lightweight design spec for a small tuning change, minor mechanic, or tightly scoped addition."
---

Read `.codex/docs/resource-preparation.md` for resource locations, shared write,
review/evidence and recovery requirements. Its shared handoff rules apply here;
initial design can record future resource needs before type contracts exist.

## Invocation and execution

Invoke this workflow as `$quick-design`.

Use existing authorization for the bounded task. Describe the intended outputs and preserve unrelated work. Ask only about unresolved consequential choices or material scope expansion; do not repeat file- or section-level approval prompts.

Arguments: `[brief description of the change]`. Treat bracketed values as optional unless the workflow says otherwise.


# Quick Design

This is the **lightweight design path** for changes that don't need a full GDD.
Full GDD authoring via `$design-system` is the heavyweight path. Use this skill
for changes meeting the small-change criteria in `docs/FRAMEWORK.md` — tuning adjustments,
minor behavioral tweaks, small additions to existing systems, or standalone
features too small to warrant a full document.

**Output:** `design/quick-specs/[name]-[date].md`

**When to run:** Anytime a change is too small for `$design-system` but too
meaningful to implement without a written rationale.

---

## 1. Classify the Change

First, read the argument and determine which category this change falls into:

- **Tuning** — changing numbers or balance values in an existing system with no
  behavioral change (most minimal path). Example: "increase jump height from 5
  to 6 units", "reduce enemy patrol speed by 10%".
- **Tweak** — a small behavioral change to an existing system that introduces no
  new states, branches, or systems. Example: "make dash invincible on frame 1",
  "allow combo to cancel into roll".
- **Addition** — adding a small mechanic to an existing system that may introduce
  narrowly scoped states or interactions. Example: "add a parry window to the block
  mechanic", "add a charge variant to the basic attack".
- **New Small System** — use only where the framework explicitly permits a
  lightweight specification and defines how it is tracked in BREAKDOWN.

Read FRAMEWORK's small-change boundary. Redirect to `$design-system` when the
change crosses that boundary, changes a governing cross-system contract or needs
full system design. If no boundary is defined, clarify the proposed scope with the
developer before treating it as a quick change. Duration alone is not a criterion.
With no argument, ask for the intended change. State the classification and rationale;
ask only when classification depends on an unsettled consequential decision.

## 2. Context Scan

Before drafting anything:

- Search `design/gdd/` by explicit system reference, exact slug, and title.
  List candidate paths. Read the uniquely relevant GDD sections; if more than
  one candidate remains, ask the user to select one rather than choosing by
  filename similarity.
- Check whether `design/gdd/BREAKDOWN.md` exists. If it does, read it to
  understand its identity, dependencies and the selected change scope. Missing required system mapping remains an explicit prerequisite gap.
- Read `docs/technical-preferences.md` and
  `docs/architecture/CONTROL.md` when present to determine the project's
  selected data/config format and constraints. If no format is configured and
  existing data files do not establish one, record the format as "TBD — user
  decision" instead of choosing JSON.
- Check `design/quick-specs/` for prior specs that touched this system. List the
  candidates and compare their relevant rules. If an unresolved contradiction
  remains, surface it and do not claim `COMPLETE` until the user resolves it.
- If this is a Tuning change, also follow its TYPE_TEMP/resource mapping to the existing data
  file and format that hold the relevant values.

Report the selected GDD and section, the data format source, prior specs checked,
and any unresolved conflicts.

---

## 3. Draft the Quick Design Spec

Use the appropriate spec format for the change category.

### For Tuning changes

Produce a single table:

```markdown
# Quick Design Spec: [Title]

**Type**: Tuning
**System**: [System name]
**GDD Reference**: `design/gdd/[filename].md` — Tuning Knobs section
**Date**: [today]

## Change

| Parameter | Old Value | New Value | Rationale |
|-----------|-----------|-----------|-----------|
| [param]   | [old]     | [new]     | [why]     |

## Tuning Knob Mapping

Maps to GDD Tuning Knob: [knob name and its documented range].
New value is [within / at the edge of / outside] the documented range.
[If outside: explain why the range should be extended.]

## Acceptance Criteria

- [ ] [Parameter] reads [new value] from `[existing project data path]`
- [ ] Behavior difference is observable in [specific context]
- [ ] No regression in [related behavior]
```

### For Tweak and Addition changes

```markdown
# Quick Design Spec: [Title]

**Type**: [Tweak / Addition]
**System**: [System name]
**GDD Reference**: `design/gdd/[filename].md`
**Date**: [today]

## Change Summary

[1-2 sentences describing what changes and why.]

## Motivation

[Why is this change needed? What player experience problem does it solve?
Reference the relevant MDA aesthetic or player feedback if applicable.]

## Design Delta

Current GDD says (quoting `design/gdd/[filename].md`, [section]):

> [exact quote of the relevant rule or description]

This spec changes that to:

[New rule or description, written with the same precision as a GDD Detailed
Rules section. A programmer should be able to implement from this text alone.]

## New Rules / Values

[Full unambiguous statement of the replacement content. If this introduces
new states, list them. If it introduces new parameters, define their ranges.]

## Affected Systems

| System | Impact | Action Required |
|--------|--------|-----------------|
| [system] | [how it is affected] | [update GDD / update data file / no action] |

## Acceptance Criteria

- [ ] [Specific, testable criterion 1]
- [ ] [Specific, testable criterion 2]
- [ ] [Specific, testable criterion 3]
- [ ] No regression: [the original behavior this must not break]

## GDD Update Required?

[Yes / No]
[When required: which file, which section, and what the update should say.]
```

### For New Small System changes

Use a trimmed GDD structure. Include only the sections that are directly
necessary — skip Player Fantasy, full Formulas, and Edge Cases unless the
system specifically requires them.

```markdown
# Quick Design Spec: [Title]

**Type**: New Small System
**Scope**: [1-2 sentence description of what this system does and doesn't do]
**Date**: [today]
**Estimated Implementation**: [hours]

## Overview

[One paragraph a new team member could understand. What does this system do,
when does it activate, and what does it produce?]

## Core Rules

[Unambiguous rules for the system. Use numbered lists for sequential behavior
and bullet lists for conditions. Be precise enough that a programmer can
implement without asking questions.]

## Tuning Knobs

| Knob | Default | Range | Category | Rationale |
|------|---------|-------|----------|-----------|
| [name] | [value] | [min–max] | [feel/curve/gate] | [why this default] |

Store values in the existing project-selected data/config format and path. If
the project has not selected a format, write `TBD — user decision`; do not
default to JSON or hardcode values.

## Acceptance Criteria

- [ ] [Functional criterion: does the right thing]
- [ ] [Functional criterion: handles the edge case]
- [ ] [Experiential criterion: feels right — what a playtest validates]
- [ ] [Regression criterion: does not break adjacent system]

## Systems Index

[Record the framework-selected tracking rule and any required BREAKDOWN update.]
```

---

## 4. Framework and resource impact

Include affected framework operations, system integrations, resource types/templates,
prepared resources/import mappings, tools and evaluation obligations. Cite actual
constraints from accepted ADRs and CONTROL; proposed decisions remain candidates.
Record the exact GDD/BREAKDOWN/contract changes needed. Do not silently broaden a
quick-spec-only request into those changes. If their scope exceeds the framework's
small-change boundary, return REDIRECTED and name the full design work needed.

## 5. Save and handoff

Save `design/quick-specs/[name]-[date].md` within existing authorization. If the
path exists, read and update the requested content while preserving unrelated work.
Verify the saved output. Report Type, System, rationale for quick scope, affected
GDD/resource/framework updates, required reviews, actual evidence and remaining work.
COMPLETE means the scoped specification was written; it does not imply implementation
or waived review. REDIRECTED means full system design is required.

Story readiness and implementation use installed `$story-readiness` and `$dev-story`. Identify any
existing referencing story without selecting an ambiguous target. Do not require
story machinery to finish this design deliverable or claim readiness from its file.
