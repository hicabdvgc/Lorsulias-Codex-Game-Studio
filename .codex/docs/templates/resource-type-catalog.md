# Resource Types: [Project]

Use this template to author root `RES_TYPE.md` after system resource needs are
understood. The catalog defines types and relationships; actual game choices
remain unset until selected. Initial GDD authoring can record needs before this exists.

## Basis and scope

Record the relevant CONCEPT, MDA goals, BREAKDOWN, system GDDs, FRAMEWORK and
accepted technical constraints. Identify the systems and resource families covered,
the author/responsible person, revision, and unresolved coverage.

## Types

| Type identity | Purpose / MDA need | Producing and consuming systems | Required properties | TYPE_TEMP path | Open decisions |
|---|---|---|---|---|---|
| [stable name or existing ID] | [why needed] | [GDD references and responsibilities] | [summary; definition owns details] | [resource_templates/.../TYPE_TEMP.md] | [unresolved, or none] |

## Relationships

| Source type | Target type | Meaning / reference identity | Cardinality and optionality | Validation and change impact |
|---|---|---|---|---|
| [type] | [type] | [how linked] | [when relevant] | [consumer behavior on missing/replaced target] |

## Coverage and decisions

For each system resource requirement, identify its type or unresolved disposition.
Record shared ownership, conflicting assumptions, and decisions requiring human
input. Preserve existing identities through rewording; document replacement or
retirement and affected references. Do not duplicate the entity registry's design facts.

## Verification and revision

Check that each referenced definition exists and can guide preparation of a
representative resource. Record actual results separately from planned checks.
Re-read before writing and preserve concurrent additions. Changes to type contracts
identify affected GDDs, prepared resources, import mappings, tools and evaluations.
