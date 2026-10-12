# $create-stories — Handoff contract

## Purpose and prerequisites
Decompose an identified existing epic into bounded, verifiable work. Read its sources
and actual dependencies. Work includes code, resource preparation, tools and framework
integration. Use applicable accepted ADRs, saved TR entries, integer CONTROL revision
and selected resource/engine contracts. A produced resource/tool is an output, not
its own prerequisite. Missing actual inputs permit useful non-ready drafts.

## Outputs and permitted changes
Create `production/epics/[epic-slug]/story-NNN-[slug].md`, update the epic's Stories
table and its existing index row when available. Report an absent index instead of
inventing a successful index update. Re-read existing story numbers immediately
before allocation. Preserve identifiers, progress and unrelated fields on reruns.
Read design, ADR, TR and CONTROL sources without changing them.

Every story supplies Epic, a single header Status, Type, applicable Layer or N/A,
Manifest Version (integer or justified N/A), Context, Acceptance Criteria,
Implementation Notes (inputs, outputs, affected consumers), Out of Scope, QA/test
protocol, Test Evidence and Dependencies. Governing ADR references include actual
status, primary decision when applicable and a source-backed summary. TRs may be
N/A with justification; never use provisional or placeholder TR IDs.

## Readiness and handoff
Not Started or Blocked drafts retain open gaps. Ready requires applicable readiness
conditions and actual required review evidence; priority and file creation cannot
promote status. Type describes work, while every criterion retains its required
automated/inspection/manual/engine/human checks. Evidence destinations alone do not
constitute protocols or test execution. `$story-readiness` assesses without editing
status. Installed execution/completion consumers use this interface. No code/resource/tool implementation occurs here.

## Shared guarantees
Apply `.codex/docs/work-preparation.md`. Existing authorization carries through
bounded saves. Re-read shared files before writing, preserve stable identities and
concurrent work, inspect saved outputs and report partial failures without discarding
completed work. Reviews are conversational unless a bounded report save is requested.
Required independent review and human evaluation cannot be waived by depth/executor.
Source templates, directories and layer labels do not create project requirements.
CONTROL revisions are integers. Proposed ADRs cannot govern Ready work. Applicable
TR references must resolve to saved active entries; justified N/A is possible for
all work types. Unknown evidence remains explicit, never a placeholder identifier.
