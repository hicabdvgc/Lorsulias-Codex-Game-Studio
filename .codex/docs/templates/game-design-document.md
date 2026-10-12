# [Mechanic/System Name]

Use for the system path declared in BREAKDOWN. Include applicable sections;
explain inapplicability where a reader would otherwise expect a requirement.
Numerical rules need formulas, units/ranges, boundary behavior, and examples.
Human experience criteria need an observation method and intended participants;
actual play evidence is required to report them as achieved.


> **Status**: Draft | In Review | Approved | Implemented
> **Author**: [Agent or person]
> **Last Updated**: [Date]
> **Last Verified**: [Date — when this doc was last confirmed accurate against current design]
> **Implements Pillar**: [Which game pillar this supports]

## Summary

[2–3 sentences: what this system is, what it does for the player, and why it
exists in this game. Use the summary for discovery; reviews read the full relevant design.]

> **System ID**: [BREAKDOWN ID] · **Framework**: [revision / relevant route] · **Key dependencies**: [system IDs]

## Overview

[One paragraph that explains this mechanic to someone who knows nothing about
the project. What is it, what does the player do, and why does it exist?]

## Player Fantasy

[What should the player FEEL when engaging with this mechanic? What is the
emotional or power fantasy being served? This section guides all detail
decisions below.]

## Detailed Design

### Core Rules

[Precise, unambiguous rules. A programmer should be able to implement this
section without asking questions. Use numbered rules for sequential processes
and bullet points for properties.]

### States and Transitions

[If this system has states (e.g., weapon states, status effects, phases),
document every state and every valid transition between states.]

| State | Entry Condition | Exit Condition | Behavior |
|-------|----------------|----------------|----------|

### Interactions with Other Systems

[How does this system interact with combat? Inventory? Progression? UI?
For each interaction, specify the interface: what data flows in, what flows
out, and who is responsible for what.]

## Formulas

[Every mathematical formula used by this system. For each formula:]

### [Formula Name]

```
result = base_value * (1 + modifier_sum) * scaling_factor
```

| Variable | Type | Range | Source | Description |
|----------|------|-------|--------|-------------|
| base_value | float | 1-100 | data file | The base amount before modifiers |
| modifier_sum | float | -0.9 to 5.0 | calculated | Sum of all active modifiers |
| scaling_factor | float | 0.5-2.0 | data file | Level-based scaling |

**Expected output range**: [min] to [max]
**Illustrative example only**: These variables, ranges and clamp are not project defaults. Replace them with the system's selected formula, units and boundary behavior.

## Edge Cases

[Explicitly document what happens in unusual situations. Each edge case
should have a clear resolution.]

| Scenario | Expected Behavior | Rationale |
|----------|------------------|-----------|
| [What if X is zero?] | [This happens] | [Because of this reason] |
| [What if both effects trigger?] | [Priority rule] | [Design reasoning] |

## Dependencies

[List every system this mechanic depends on or that depends on this mechanic.]

| System | Direction | Nature of Dependency |
|--------|-----------|---------------------|
| [Combat] | This depends on Combat | Needs damage calculation results |
| [Inventory] | Inventory depends on this | Provides item effect data |

## Tuning Knobs

[Every value that should be adjustable for balancing. Include the current
value, the safe range, and what happens at the extremes.]

| Parameter | Current Value | Safe Range | Effect of Increase | Effect of Decrease |
|-----------|--------------|------------|-------------------|-------------------|

## Visual/Audio Requirements

[What visual and audio feedback does this mechanic need?]

| Event | Visual Feedback | Audio Feedback | Priority |
|-------|----------------|---------------|----------|

## Game Feel

Describe applicable interaction qualities and how they will be evaluated.
Use timing/frame data when the mechanic needs it; other systems may use clarity,
legibility or decision feedback. Record undecided targets explicitly.

### Feel Reference

[Name a specific game, mechanic, or moment that captures the target feel. Be precise —
cite the exact mechanic, not just the game. Explain what quality you are borrowing.
Optionally include an anti-reference (what this should NOT feel like).]

> Example: "Should feel like Dark Souls weapon swings — weighty, committed, and
> telegraphed, but satisfying on contact. NOT floaty like early Halo melee."

### Input Responsiveness

[Maximum acceptable latency from player input to visible/audible response, per action.]

| Action | Max Input-to-Response Latency (ms) | Frame Budget (at selected rate) | Notes |
|--------|-----------------------------------|------------------------|-------|
| [Primary action] | [project-selected target] | [derive from target rate] | |
| [Secondary action] | | | |

### Animation Feel Targets

[Frame data targets for each animation in this mechanic. Startup = windup before the
action has any effect. Active = frames when the action is "happening" (hitbox live,
ability firing, etc.). Recovery = committed/vulnerable frames after the action resolves.]

| Animation | Startup Frames | Active Frames | Recovery Frames | Feel Goal | Notes |
|-----------|---------------|--------------|----------------|-----------|-------|
| [e.g., Light attack] | | | | [e.g., Snappy, low commitment] | |
| [e.g., Heavy attack] | | | | [e.g., Weighty, high commitment] | |

### Impact Moments

[Defines the punctuation of the mechanic — the moments of peak feedback intensity that
make actions feel consequential. Include applicable events and explain required feedback.]

| Impact Type | Duration (ms) | Effect Description | Configurable? |
|-------------|--------------|-------------------|---------------|
| Hit-stop (freeze frames) | [e.g., 80ms] | [Freeze both objects on contact] | Yes |
| Screen shake | [e.g., 150ms] | [Directional, decaying] | Yes |
| Camera impact | | | |
| Controller rumble | | | |
| Time-scale slowdown | | | |

### Weight and Responsiveness Profile

[A short prose description of the overall feel target. Answer the following:]

- **Weight**: Does this feel heavy and deliberate, or light and reactive?
- **Player control**: How much does the player feel in control at every moment?
  (High control = can course-correct mid-action; Low control = committed, momentum-based)
- **Snap quality**: Does this feel crisp and binary, or smooth and analog?
- **Acceleration model**: Does movement/action start instantly (arcade feel) or
  ramp up from zero (simulation feel)? Same question for deceleration.
- **Failure texture**: When the player makes an error, does the mechanic feel fair
  or punishing? What is the read on WHY they failed?

### Feel Acceptance Criteria

[State the intended experience, representative participants/conditions, observation
method and decision criterion. Separate subjective observations from instrumented
latency measurements. These are planned evaluations until performed.]

- [ ] [For example: participants can explain why a rejected action failed; record observations and exceptions.]
- [ ] [Applicable response-time target, measurement method and actual result.]

## UI Requirements

[What information needs to be displayed to the player and when?]

| Information | Display Location | Update Frequency | Condition |
|-------------|-----------------|-----------------|-----------|

## Cross-References

| This system consumes / affects | Target GDD / framework route | Specific element | Responsibility and change effect |
|---|---|---|---|
| [behavior or shared fact] | [explicit reference] | [value / event / rule] | [who owns it and what must be checked when changed] |

These references support the installed `$review-all-gdds` review and relevant
`$consistency-check` comparisons. Their conclusions require the actual selected
scope and evidence; references alone do not establish integration correctness.

## Framework Operations and Resource Needs

| Addition / modification | Required input | Integration steps | Affected systems | Verification |
|---|---|---|---|---|
| [representative operation] | [design/data/material] | [how it fits] | [references] | [evaluation method] |

| Resource need | Required properties / relationships | Consuming behavior | Existing contract or unresolved schema question |
|---|---|---|---|
| [resource] | [what the system needs] | [rule / presentation] | [reference or pending later schema work] |

Initial design uses preliminary FRAMEWORK and can leave future resource schemas
unresolved. Later integration review checks actual RES_TYPE and type templates.

## Acceptance Criteria

[Testable criteria that confirm this mechanic is working as designed.]

- [ ] [Criterion 1: specific, measurable, testable]
- [ ] [Criterion 2]
- [ ] [Criterion 3]
- [ ] Performance: System update completes within [X]ms
- [ ] [Chosen tuning/configuration requirements are met where applicable.]

## Open Questions

[Anything not yet decided. Identify the responsible decision maker and any actual due date or dependency.]

| Question | Owner | Deadline | Resolution |
|----------|-------|----------|-----------|
