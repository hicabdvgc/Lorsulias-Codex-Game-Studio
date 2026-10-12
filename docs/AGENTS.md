# Documentation Guidance

Use the artifact locations and shared interfaces in
[directory-structure.md](../.codex/docs/directory-structure.md).

Architecture records explain the question, alternatives, decision, consequences,
and applicable dependencies and design requirements. Verify engine claims against
the actual selected version when relevant. Use the installed ADR template and `$architecture-decision` contract.
Acceptance requires explicit decision authorization, accepted dependencies and
applicable review evidence; it synchronizes the architectural registry. It does
not automatically advance story readiness.

ADR statuses are Proposed → Accepted → Superseded. An implementation relying on a
decision needs its accepted form. Drafting or reviewing a proposal remains possible
before acceptance. Preserve stable TR identities in `architecture/tr-registry.yaml`;
rewording retains IDs, while replacement/retirement preserves explicit history.
Provisional unsaved IDs cannot support durable downstream references.

CONTROL at `architecture/CONTROL.md` records Required / Forbidden / Guardrail rules
for the affected components, with decision provenance and an integer
`Manifest Version:`. Increment that integer for governing/provenance changes;
leave an unchanged manifest unchanged. Recommendations retain their strength. Scope checks
to the work affected by those rules; do not impose a universal architecture layer.

Reviews report findings in conversation by default. Save review records only
when the task explicitly includes them; name the writer and consumers if a later
workflow requires persistence. Preserve actual evidence and distinguish plans,
observations, unresolved questions, and decisions.
