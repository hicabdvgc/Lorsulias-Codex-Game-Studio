# Work Preparation and Evidence Contracts

Use with the epic/story/milestone/planning skills and their handoff contracts.
This guidance defines work preparation for the four-section workflow.

## Scope, prerequisites and authority

Use developer-authored CONCEPT, full BREAKDOWN, relevant system GDDs, FRAMEWORK,
applicable architecture/accepted ADRs, resource contracts and actual slice findings.
Epics group coherent outcomes; systems, modules and optional project-defined layers
describe scope without imposing one epic per module or a universal build order.
Dependencies determine order. Work may create code, content, resources or tools.
Link additions/modifications to the framework route and affected consumers.

Separate required inputs from outputs to create. Check prerequisites for usable
information, format and relationships where required by the selected TYPE_TEMP;
file existence alone does not establish usability. Initial design may leave future
contracts open; resource preparation needs its actual selected contract. Use
[resource preparation](resource-preparation.md) and [tool development](tool-development.md).

List applicable governing ADRs with actual statuses and an explicit primary when
real ADRs apply. Every governing ADR must be Accepted before dependent work is
Ready. A reasoned `N/A — ...` is valid for any story type when no ADR applies;
it cannot conceal a missing required decision or accompany a contradictory real ADR.
Record applicable stable TR IDs from the saved registry; never allocate provisional
IDs here. Nontechnical work may trace to a precise source requirement with a stated
reason no TR applies. A claimed TR must resolve and remain active.

CONTROL uses integer `Manifest Version:` at `docs/architecture/CONTROL.md`.
Record its revision and scoped rules when applicable; justify N/A otherwise.
A changed revision requires checking affected rules before readiness can pass;
never fix staleness by merely stamping a new number. Preserve Required, Forbidden,
Guardrail and recommendation strength. Engine evidence uses selected versions and
actual observations, not model-cutoff risk labels.

## Work-item identity and status

Keep `production/epics/[epic-slug]/EPIC.md`, the epic index and
`story-NNN-[slug].md`. Story identity includes its parent epic; identical local
numbers in different epics are not automatically duplicates. Resolve explicit paths
first, then exact qualified identity; ambiguity is an unresolved dependency.
Preserve identifiers on wording changes. Re-read indexes and target directories
before allocating IDs; update existing matched work instead of duplicating it.

The story's single header `Status:` is authoritative. Status-like text in test plans,
examples or evidence sections is not work status. Retain this mapping:

| Story status | Derived sprint YAML status |
|---|---|
| Not Started | backlog |
| Ready | ready |
| In Progress | in_progress |
| In Review | review |
| Complete | done |
| Blocked | blocked |

Legacy Done is recognized as completion and maps to derived done without rewriting
the story. The observer reports its raw value. Unknown, absent or conflicting declarations remain explicit.
Readiness verdicts READY / NEEDS WORK / BLOCKED / NOT ASSESSED are assessments, not
automatic edits to story Status. A draft can be Not Started with open gaps, or
Blocked with a known blocker. Only a supported assessment permits an authoring
task to record Ready. Priority and planned dependency ordering never do.

`production/sprint-status.yaml` is a derived view for its identified sprint.
Membership, dates, priorities, ownership and estimates describe the selected plan;
statuses come from referenced stories. Report disagreements. Authorized
synchronization rereads stories and updates the view, never the story to match
a stale view. Preserve notes, unknown fields and unrelated entries. Unreadable
stories produce gaps, not fabricated statuses.

## Acceptance and evidence

Retain Logic, Integration, Visual/Feel, UI and Config/Data as classifications.
Choose the best description and explain mixed scope; split independently useful
work when it improves delivery. Classification cannot discard another criterion's
checks. No universal criterion count or fixed story duration applies.

Each criterion states setup/input, action, expected outcome, evaluation method,
required evidence location and actual evaluator responsibility. Methods include
calculations, automated tests, resource/contract inspection, engine execution,
manual walkthrough, listening and actual player/intended-user use. Subjective goals
need an observable protocol and comparison basis; a path alone is insufficient.
Human judgment can be required in any type. Required checks remain required;
recommendations remain advisory. Use one or several methods according to outcomes.

Automated tests/reports use the actual runner roots and commands under
[code-root resolution](code-root-resolution.md). Manual evidence uses
`production/qa/evidence/[story-slug]-evidence.md`, or an epic-qualified name when
slugs collide; preserve existing specific paths. Evidence identifies revision/build,
input, method/command, result and limitations. Plans, files and screenshots cannot
substitute for execution or human experience.

## Review, writing and recovery

Follow [review workflow](review-workflow.md) and applicable director gates. Assign
qualified available executors under the active delegation policy. Review depth
changes optional breadth only. Identify self-review; missing required independence
leaves that check unassessed. Human observations must come from actual sessions.

Reviews/status reports are conversational and read-only by default. Explicit report
saves remain bounded and never confer approval. Authoring carries existing task
authorization through requested writes; ask only about consequential unresolved
decisions or scope expansion. Re-read shared files before writes and preserve
concurrent work. Read back promised outputs. If a multi-file save fails, report the
actual partial state, preserve completed work and repair the affected handoff
without claiming atomicity or restoring stale contents.

## Milestones and later consumers

Epic/story preparation uses slice experience before final MILESTONE authoring;
MILESTONE is not its universal prerequisite. Pickup readiness does not establish
the vertical-slice hard gate or authorize production progression. Actual play,
integration and framework addition/modification evidence remain required.

`$define-milestones` authors project-defined MVP/Alpha/Beta/Gold expectations in
`production/milestones/MILESTONE.md` after that hard gate; an earlier draft records
missing prerequisites. Sprints are optional subdivisions of selected milestones.
Story execution/completion, slice/gate orchestration and milestone review are available;
read [execution and evidence](execution-and-evidence.md) and [progression](progression.md). Installed navigation/status consumers preserve story authority and
criterion-level evidence. No receipts or automatic review skipping are supplied.
