# Development Framework

Use this template to author `docs/FRAMEWORK.md`. Begin from the preliminary
BREAKDOWN and developed framework principles. Complete full BREAKDOWN alongside
the preliminary FRAMEWORK; use the initial system GDDs to complete FRAMEWORK.
This is an authoring procedure and document template, not an executable framework.

- Maturity: [Preliminary / Full]
- Revision: [project revision]
- Responsible author / decision maker: [actual people or assigned agents]
- Inputs: [CONCEPT, BREAKDOWN, studies, GDDs as available, and their revisions]
- Open decisions and effect on use: [specific gaps]

## Working Principle
[Explain how the game can be expanded and modified consistently. Describe which
artifacts govern behavior, technical choices, resources, and verification.]

## System and Integration Responsibilities
| System / component | Owns | Consumes / produces | Integration responsibility | Governing document |
|---|---|---|---|---|
| [BREAKDOWN system] | [behavior / shared fact] | [interface] | [how effects reach others] | [GDD or pending design] |

## Addition Routes
| Addition kind | Inputs and decisions | Work sequence | Affected artifacts and systems | Completion evidence |
|---|---|---|---|---|
| [content / mechanic / presentation / tool, as applicable] | [real prerequisites] | [author, prepare, integrate, check] | [explicit references] | [inspection, execution, human evaluation as needed] |

In the preliminary version, identify intended routes and unresolved interfaces.
In the full version, walk an example through actual GDDs. Resource schemas and
tools may still be future outputs; record the contracts their later procedures
must establish without inventing formats, locations, or completed implementation.

## Modification Route
1. Identify the existing behavior and the intended change, with a recoverable prior revision.
2. Trace affected systems, shared facts, decisions, resource needs, tools, and verification.
3. Resolve consequential design/interface choices with the responsible decision maker.
4. Update the governing description and affected consumers within the authorized task.
5. Check the changed behavior and affected integrations; preserve required human and independent evidence.
6. Report completed work, remaining gaps, and which dependent activity is ready or blocked.

## Framework Revision
[State which changes invalidate a route or shared interface, who decides the
revision, how affected work is identified, and how the revised route is checked.]

## Verification and Recovery
| Route / interaction | Representative input | Expected result | Evaluation method | Actual evidence / still pending |
|---|---|---|---|---|
| [route] | [example] | [usable output] | [specific check] | [reference or pending] |

Preserve completed work when an output is missing. Verify promised saved outputs
before a handoff and identify the activity blocked by the gap. The vertical slice
later demonstrates these routes in practice; this document alone cannot pass its gate.

## Executable Support, if Present
[Name actual commands/tools, inputs, outputs, limitations, and their relationship
to the documented routes. Otherwise state that the routes are document-guided.]
