# ADR-[NNNN]: [Title]

## Status

Proposed

<!-- Keep exactly one status: Proposed, Accepted, or Superseded. New records
remain Proposed. Record acceptance or replacement details in the section below. -->

## Decision History

[Acceptance authority/date/evidence, if accepted. Replacement ADR identity and
affected decisions, if superseded. A technical review alone is not acceptance.]

## Date

[YYYY-MM-DD — when this ADR was written]

## Last Verified

[YYYY-MM-DD — when this ADR was last confirmed accurate against the current
engine version and design. Update this date when you re-read and confirm it
is still correct, even if nothing changed.]

## Decision Makers

[Who was involved in this decision]

## Summary

[Briefly explain what problem this ADR solves, and what was decided. Written for
tiered context loading — a skill scanning 20 ADRs uses this to decide whether
to read the full decision. Be specific: name the system, the problem, and the
chosen approach.]

## Engine Compatibility

| Field | Value |
|---|---|
| Engine / version / packages | [selected project versions, or Not applicable for an engine-independent decision] |
| Domain and APIs used | [specific dependencies] |
| References Consulted | [official versioned source and local reference, with verification date] |
| Evidence and limitations | [documented behavior, runtime observations, or NOT ASSESSED] |
| Verification Required | [checks needed before acceptance or implementation; identify which] |

A reference-library version is not the project's selected version. A changed
engine requires review of affected claims; it does not automatically supersede an ADR.

## ADR Dependencies

| Field | Value |
|-------|-------|
| **Depends On** | [ADR-NNNN (must be Accepted before this decision is accepted), or explicit "None"] |
| **Enables** | [ADR-NNNN (this ADR unlocks that decision), or "None"] |
| **Blocks** | [Epic/Story name — cannot start until this ADR is Accepted, or "None"] |
| **Ordering Note** | [Any sequencing constraint that isn't captured above] |

## Context

### Problem Statement

[What problem are we solving? Why must this decision be made now? What is the
cost of not deciding?]

### Current State

[How does the system work today? What is wrong with the current approach?]

### Constraints

- [Technical constraints -- engine limitations, platform requirements]
- [Timeline constraints -- deadline pressures, dependencies]
- [Resource constraints -- team size, expertise available]
- [Compatibility requirements -- must work with existing systems]

### Requirements

- [Functional requirement 1]
- [Functional requirement 2]
- [Performance requirement -- specific, measurable]
- [Scalability requirement]

## Decision

[The specific technical decision, described in enough detail for someone to
implement it without further clarification.]

### Architecture

```
[ASCII diagram showing the system architecture this decision creates.
Show components, data flow direction, and key interfaces.]
```

### Key Interfaces

```
[Pseudocode or language-specific interface definitions that this decision
creates. These become the contracts that implementers must respect.]
```

### Implementation Guidelines

[Specific guidance for the programmer implementing this decision.]

## Alternatives Considered

### Alternative 1: [Name]

- **Description**: [How this approach would work]
- **Pros**: [What is good about this approach]
- **Cons**: [What is bad about this approach]
- **Estimated Effort**: [Relative effort compared to chosen approach]
- **Rejection Reason**: [Why this was not chosen]

### Alternative 2: [Name]

[Same structure as above]

## Consequences

### Positive

- [Good outcomes of this decision]

### Negative

- [Trade-offs and costs we are accepting]

### Neutral

- [Changes that are neither good nor bad, just different]

## Risks

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|

## Performance Implications

| Metric | Before | Expected After | Budget |
|--------|--------|---------------|--------|
| CPU (frame time) | [X]ms | [Y]ms | [Z]ms |
| Memory | [X]MB | [Y]MB | [Z]MB |
| Load Time | [X]s | [Y]s | [Z]s |
| Network (if applicable) | [X]KB/s | [Y]KB/s | [Z]KB/s |

## Migration Plan

[If this changes existing systems, the step-by-step plan to migrate.]

1. [Step 1 -- what changes, what breaks, how to verify]
2. [Step 2]
3. [Step 3]

**Rollback plan**: [How to revert if this decision proves wrong]

## Validation Criteria

[How we will know this decision was correct after implementation.]

- [ ] [Measurable criterion 1]
- [ ] [Measurable criterion 2]
- [ ] [Performance criterion]

## Framework and Resource Effects

[Describe applicable addition/modification routes, system integration, resource
requirements and tool interfaces. Link existing contracts; record future outputs
as unresolved work without inventing schemas.]

## GDD Requirements Addressed

<!-- This section is MANDATORY. Every ADR must trace back to at least one GDD
     requirement, or explicitly state it is a foundational decision with no GDD
     dependency. Traceability is audited by $architecture-review. -->

| GDD Document | System | Requirement | How This ADR Satisfies It |
|-------------|--------|-------------|--------------------------|
| [e.g. `design/gdd/combat.md`] | [e.g. Combat] | [e.g. "Hitbox detection must resolve within 1 frame"] | [explain the decision and cite relevant evidence] |

> If this is a foundational decision with no direct GDD dependency, write:
> "Foundational — no GDD requirement. Enables: [list what GDD systems this
> decision unlocks or constrains]"

## Related

- [Link to related ADRs — note if supersedes, contradicts, or depends on]
- [Link to relevant code files once implemented]
