---
name: propagate-design-change
description: Trace a documented design or framework/resource change into affected
  decisions, contracts, work and verification, preserving authority and identities.
---

# Propagate Design Change

Invoke as `$propagate-design-change`. Arguments: `[path/to/changed-document]`.

Read [.codex/docs/execution-and-evidence.md](../../../.codex/docs/execution-and-evidence.md) for authorization, status, criterion-level evidence, review and recovery contracts. Read the relevant sources before editing.


Resolve the changed document; without a path identify actual candidates and ask. The source
may be a GDD, FRAMEWORK, resource contract or another governing design artifact. Read current
contents and obtain an identifiable previous revision from supplied text/history or an explicit
Git commit. A timestamp or guessed HEAD~1 cannot establish the intended baseline. If no baseline
exists, report current dependency/consistency observations and the limitation on historical impact.

## Impact analysis

List material changes with source locations. Trace explicit references and relevant shared
concepts through BREAKDOWN/system GDDs, FRAMEWORK operations, architecture/ADRs, entity and
architecture registries, TRs, CONTROL, RES_TYPE/TYPE_TEMP, prepared resources/import copies,
tools, epics/stories, milestone/QA/regression plans and runtime consumers. Name searched scope
and missing coverage. No reference hits cannot prove no impact across unread or implicit consumers.
Classify confirmed impacts, likely impacts and unresolved dependencies. Highlight affected In
Progress/In Review work and completed work whose evidence no longer covers the changed behavior.

Assess decision conflicts separately from wording changes. Preserve IDs when meaning is unchanged;
explicitly record retirement/replacement when requirements change. Proposed ADRs are candidates;
acceptance/supersession follows `$architecture-decision`. Accepted stances and CONTROL obligations
cannot be silently weakened. Developer CONCEPT revisions require the developer's decision.

## Resolution and handoff

Return a conversational impact report with affected item, reason, proposed action, responsible
available executor and needed verification. No automatic gate or hierarchy traversal is required.
Apply already-authorized bounded downstream corrections; consequential alternatives need resolution.
Re-read registries/manifests/indexes before writing, preserve concurrent entries and stable IDs,
and change integer CONTROL revision only for an actual governing-rule change through its authoring
interface. Identify stories needing readiness reassessment rather than arbitrarily changing progress.

An explicitly requested impact record may be saved at production/change-impact-[date]-[system].md using an
identifiable change scope. Preserve an existing record unless its update is requested. Re-read
outputs and inspect relevant links, shared facts, resource/tool compatibility and affected tests.
Report completed changes and remaining activities; a failed secondary output cannot erase earlier
valid work or justify declaring all consumers synchronized.
