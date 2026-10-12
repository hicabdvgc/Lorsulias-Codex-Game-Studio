# [Skill name] Handoff Contract

Use only when a skill's actual producer/consumer relationship needs an explicit
contract. Fill applicable sections; omit irrelevant ones. This template defines
an authoring aid and supplies no test runner, drift monitor, or TESTS.md convention.

## Inputs consumed
[Source artifact or supplied information, authoritative location, relevant
revision/state, and what the activity uses it for.]

## Files that must exist and preconditions
[Actual prerequisites for this activity. Distinguish planned output paths from
existing inputs. State decisions/evidence needed and any supported alternatives.]

## Outputs produced
[Returned result or saved artifacts, their actual format, responsible writer,
and intended consumer. State explicitly when the result is conversation-only.]

## Output guarantees
[Observable required content/behavior, relevant validation, and the meaning of
success, failure, unavailable evidence, and inapplicability.]

## Change boundaries
[Authorized mutable fields/files and content that must be preserved. How relevant
input changes invalidate an earlier result. Avoid inventing universal schemas.]

## Handoff and recovery
[What the next activity receives; what remains incomplete on partial failure.
Refer to the shared error-recovery protocol where applicable.]
