# ADR-[NNNN]: [Decision Name]

---
**Status**: Proposed
**Origin**: Reverse-Documented
**Source**: `[path to implementation code]`
**Date**: [YYYY-MM-DD]
**Decision Makers**: [Explicitly provided names or "unknown — not recorded"]
**Implementation Status**: [Deployed | Partial | Planned]
---

> **⚠️ Reverse-Documentation Notice**
>
> This Architecture Decision Record was created **after** the implementation already
> existed. It captures the current implementation approach and clarified rationale
> based on code analysis and user consultation. Some context may be reconstructed
> rather than contemporaneously documented.

---

## Evidence Boundaries

- **Observed implementation:** Record only behavior, structure, and constraints directly evidenced by source code, assets, configuration, build output, or test results.
- **User-stated intent:** Label goals or intended behavior supplied by the user separately; intent is not evidence that a feature is implemented.
- **Gap:** Mark missing, contradictory, or unverified behavior explicitly instead of inferring it.
- **Decision history:** Record an alternative, decision maker, or rejection rationale as historical fact only when an existing artifact or the user explicitly confirms it. Otherwise label it `possible` or `unknown — not recorded`.

Describe source-inspected implementation separately from passing evaluation.
A criterion passes only with the actual evidence method it requires, including
runtime, independent review or human evaluation where applicable.

---

## Context

**Problem Statement**: [What problem did this implementation solve?]

**Background**:
- [Evidence-backed context, or unknown — not recorded]
- [Confirmed constraint, or possible constraint]
- [Do not list alternatives here unless their historical consideration is evidenced]

**System Scope**: [What parts of the codebase does this affect?]

**Stakeholders**:
- [Explicitly identified role/name, or unknown]: [Concern if evidenced]

---

## Decision

**Approach Taken** (as implemented):

[Describe the architectural approach found in the code]

**Key Implementation Details**:
- [Detail 1]: [How it works]
- [Detail 2]: [Pattern or structure used]
- [Detail 3]: [Notable design choice]

**Clarified Rationale** (from user or existing artifact):
- [Confirmed reason, or unknown — not recorded]

**Code Locations**:
- `[file/path 1]`: [What's there]
- `[file/path 2]`: [What's there]

---

## Alternatives Considered

Only use **Considered** when an existing decision artifact or the user confirms
that history. Otherwise title this subsection **Possible Alternatives (not
confirmed as considered)**. Pros/cons may describe current analysis, but why an
alternative was not chosen remains `Unknown — not recorded` without evidence.

### Alternative 1: [Approach Name]

**Historical status**: [Confirmed considered, source: path/user | Possible only]

**Description**: [What this alternative would be]

**Pros**:
- [Advantage 1]
- [Advantage 2]

**Cons**:
- [Disadvantage 1]
- [Disadvantage 2]

**Why Not Chosen**: [Confirmed reason and source | Unknown — not recorded]

### Alternative 2: [Approach Name]

**Historical status**: [Confirmed considered, source: path/user | Possible only]

**Description**: [What this alternative would be]

**Pros**:
- [Advantage 1]
- [Advantage 2]

**Cons**:
- [Disadvantage 1]
- [Disadvantage 2]

**Why Not Chosen**: [Confirmed reason and source | Unknown — not recorded]

### Alternative 3: [Status Quo / No Change]

**Historical status**: [Confirmed considered, source: path/user | Possible only]

**Description**: [What doing nothing would mean]

**Why Not Chosen / Acceptable**: [Confirmed reason and source | Unknown — not recorded]

---

## Consequences

### Positive Consequences (Benefits Realized)

**[Benefit 1]**: [Observed or measured benefit]

**[Benefit 2]**: [Impact]

### Negative Consequences (Trade-offs Observed)

**[Trade-off 1]**: [Observed limitation or cost]

**[Trade-off 2]**: [Impact]

### Neutral Consequences (Observations)

**[Observation 1]**: [Emergent property or side effect]

---

## Implementation Notes

**Patterns Used**:
- [Pattern 1]: [Where and how]
- [Pattern 2]: [Where and how]

**Dependencies Introduced**:
- [Dependency 1]: [Observed use]
- [Dependency 2]: [Observed use]

**Performance Characteristics**:
- Time complexity: [Measured/derived value or unknown]
- Space complexity: [Measured/derived value or unknown]
- Bottlenecks: [Evidence-backed concern or unknown]

**Thread Safety**:
- [Observed approach or unknown]

**Testing Strategy**:
- [Existing tests and paths]
- Coverage: [Measured value or unknown — not estimated]

---

## Validation

**How We Know This Works**:
- [Existing build/test/runtime evidence and source]
- [Unknown where evidence is absent]

**Known Issues** (discovered during analysis):
- [Issue 1]: [Problem and evidence]

**Risks**:
- [Risk 1]: [Evidence-backed risk]
- [Unknown inputs]

---

## Open Questions

**Unresolved During Reverse-Documentation**:
1. **[Question 1]**: [What's unclear about the decision or implementation?]
   - Needs clarification from: [Explicit role/name or unknown]
   - Impact if unresolved: [Consequence]

2. **[Question 2]**: [What needs to be decided for future work?]

---

## Follow-Up Work

**Immediate**:
- [ ] [Task 1]
- [ ] [Task 2]

**Short-Term**:
- [ ] [Task 3]
- [ ] [Task 4]

**Long-Term**:
- [ ] [Task 5]

---

## ADR Dependencies

| Field | Value |
|---|---|
| **Depends On** | [confirmed ADR-NNNN IDs, or explicit None; unknown remains unresolved] |
| **Enables** | [known dependent decisions, or None] |

## Related Decisions

[Identify confirmed supersession/replacement and other relationships separately
from dependency edges. Record unknown history explicitly.]

## References

**Code Locations**:
- `[path/file 1]`: [Primary implementation]
- `[path/file 2]`: [Related code]

**External Resources**:
- [Documentation actually consulted]

**Design Documents**:
- [GDD Section]: [If this implements a design]

---

## Version History

| Date | Author | Changes |
|------|--------|---------|
| [Date] | Codex (reverse-doc) | Initial reverse-documentation from `[source path]` |
| [Date] | [Explicit author or unknown] | Clarified rationale for [X] |

---

## Decision Lifecycle

Reverse-documentation describes observed implementation. It does not establish
acceptance. Recovered decisions are Proposed until explicitly accepted through
`$architecture-decision accept ADR-NNNN`; preserve an existing accepted status
only when its actual decision record supports it. Superseded requires an identified
replacement. Origin (reverse-documented) is separate from decision status.

---

## Appendix: Code Snippets

**Key Implementation Pattern**:

```[language]
[Code snippet showing the core pattern or decision]
```

**Rationale**: [Confirmed rationale and source | Unknown — not recorded]

**Possible Alternative Approach** (not confirmed as historically considered):

```[language]
[Code snippet showing what the alternative would look like]
```

**Why Not**: [Confirmed reason and source | Unknown — not recorded]

## Framework and Handoff

[Identify observed integrations and resource/tool inputs, the relevant framework
route if one exists, and unknown intent. Link governing designs without declaring
recovered material approved or an unexecuted test passed.]
