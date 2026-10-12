---
name: bug-triage
description: Classify and prioritize the actual bug backlog, with evidence-based trends
  and explicit data limitations.
---

# Bug Triage

Invoke as `$bug-triage`. Arguments: `[sprint | full | trend]`.

Read [.codex/docs/execution-and-evidence.md](../../../.codex/docs/execution-and-evidence.md) for authorization, status, criterion-level evidence, review and recovery contracts. Read the relevant sources before editing.


Default to an explicitly identified current sprint when available, otherwise full. Resolve named
sprint membership from actual records; do not infer the highest number as current. Discover
production/qa/bugs/*.md first, then an existing consolidated bugs.md or QA Bugs Found sections when
needed. State source coverage and deduplicate by resolvable BUG identity and reproduction evidence;
ambiguous duplicates stay flagged rather than silently merged.

Read each authoritative status. Open bugs belong to the active backlog; Verified Fixed and Closed
are reported separately/excluded from active counts. Unknown, missing or conflicting statuses are
explicit data-quality gaps. Inspect impact, reproduction, affected system/build and existing severity/
priority. Retain S1-Critical through S4-Trivial and P1-Immediate through P4-Wishlist; explain proposed
changes with evidence. Priority labels do not select capacity, sprint dates or actual assignees.
Suggest qualified available expertise, preserving unresolved ownership.

Full covers identified active records. Sprint focuses on relevant selected work and separately
surfaces cross-scope blockers. Trend needs comparable historical snapshots/periods; a current file
list cannot establish bug creation/closure rates or worsening quality. Describe supported volume,
age, system concentration and regressions with denominators and limitations, without fixed trigger
counts. Missing history leaves trend unassessed.

Return active counts by known severity/priority, uncertain records, urgent candidates, rationale,
capacity/dependency constraints and next actions. No P1 bugs does not prove a build is ready.
Default triage is conversational and read-only. Explicitly authorized reports/record corrections
must re-read records and preserve IDs, progress and concurrent content. Actual assignment, fixes and
sprint changes need authorization covering them. Verify any promised saves.
