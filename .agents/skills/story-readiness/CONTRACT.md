# $story-readiness — Assessment contract

## Inputs
Resolve a story path, all story scope, or the identified sprint's story references.
Before an authoring save, a complete supplied draft with its planned local path
is a valid review candidate; an absent file alone is not.
Read complete story content, epic/GDD/FRAMEWORK sources, actual dependencies,
applicable accepted ADRs, saved TR registry, integer CONTROL and relevant resource,
engine and QA contracts. Empty, unreadable, ambiguous or missing scope remains
explicit; missing references cannot disappear from aggregate coverage.

## Assessment and output
Check usable prerequisites, bounded outcomes, governing authority, dependency
resolution, criterion-level feasible protocols and required review/human evidence.
Future outputs do not block work that creates them. Self/missing/cyclic or incomplete
pickup dependencies do block dependent readiness. A changed CONTROL revision needs
affected-rule review; restamping a header alone cannot repair it.
Return READY, NEEDS WORK, BLOCKED or NOT ASSESSED with the assessed scope, findings,
evidence, missing inputs and corrective work. Required unavailable checks preclude
READY. Distinguish planned evaluation from completed execution where relevant.

## Write boundary and consumers
The assessment does not modify story status, epic indexes or derived sprint YAML.
An explicitly requested report save covers that report only and confers no approval.
Authoring/planning consumers use the findings alongside their own actual write
authorization; later execution consumers must recheck changing prerequisites.
Story-owned status and derived-YAML mappings are documented in work-preparation.md.

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
