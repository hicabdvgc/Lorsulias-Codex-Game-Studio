---
name: vertical-slice
description: Build and assess a representative integrated slice, including framework
  addition and modification and actual human play findings.
---

# Vertical Slice

Invoke as `$vertical-slice`. Arguments: `[--review full|lean|solo]`.

Read [.codex/docs/execution-and-evidence.md](../../../.codex/docs/execution-and-evidence.md) for authorization, status, criterion-level evidence, review and recovery contracts. Read the relevant sources before editing.


Read `.codex/docs/progression.md` and the vertical-slice-report template. Resolve the intended
experience and learning question from developer-authored CONCEPT, relevant BREAKDOWN/GDDs,
FRAMEWORK, applicable accepted architecture/CONTROL, UX/accessibility and selected resource/tool
contracts. Record missing actual prerequisites. Existing art direction can be sufficient;
no universal art bible, screen count, schedule or ADR count applies.

## Scope and build

Choose a coherent playable path that exercises representative system integration, resource/tool
use and the stated question. Include one meaningful framework addition and one modification,
with connected-system effects and verification. Define the observable success/failure basis with
the developer where unsettled. Preserve previous slice findings for a pivot or rerun.

Plan bounded tasks and available executors. A slice precedes epic/story preparation and final
MILESTONE authoring; use explicit scoped tasks when stories do not yet exist. When stories do
exist, apply their readiness and status contracts. Resolve actual engine/project roots and APIs,
then implement the agreed path. Record usable partial results and blocked dependencies.
Test integration and observe the running build with available capabilities. Actual player and
intended-user evaluation remain pending until performed. Stop or revise a failed experiment
based on evidence and the authorized scope, without fixed day-based sunk-cost thresholds.

## Debrief and report

Collect the actual build/session, participants, protocol, observations, confusion, usability,
intended experience, integration failures and framework operations. Separate interpretation
from direct observations. Use `$playtest-report` for new records in production/playtests/.
No simulated person can supply required human findings.

Fill `.codex/docs/templates/vertical-slice-report.md`; save to
the existing slice report or `prototypes/[concept-slug]-vertical-slice/REPORT.md`, preserving prior runs and their evidence. Implementation locations follow the actual selected project and authorized scope; report placement does not require prototype-only code. Maintain the matching existing prototypes/index.md entry when applicable, preserving other experiments. Record scope,
addition/modification results, learning, gaps, retention/refactoring/disposal decisions and a
supported **PROCEED / PIVOT / KILL** recommendation. Missing required evidence yields **NOT
ASSESSED**, with known failures retained. PIVOT/KILL recommendations need the developer's
consequential direction; do not rewrite CONCEPT. Required creative/technical/independent review
cannot be waived by review depth or executor substitution.

Verify the saved report. Prepare epics/stories from the slice experience, assess readiness and
then use `$gate-check vertical-slice` for the hard gate. The report and recommendation do not
advance the stage or settle milestone definitions.
