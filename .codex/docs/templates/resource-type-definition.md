# TYPE_TEMP: [Resource type]

Author an identifiable definition under root `resource_templates/`, linked from
`RES_TYPE.md`. Place associated usable templates alongside it or link their actual
locations. Select the format for this type; this document imposes no JSON, naming,
engine, folder-per-item, or schema-language default.

## Purpose and consumers

Record type identity, revision, responsible person, relevant GDD/FRAMEWORK needs,
producer and consumer responsibilities, and applicable accepted constraints.

## Information and format

| Information / property | Meaning and unit | Required / conditional | Representation and constraints | Default or absence behavior |
|---|---|---|---|---|
| [field, metadata or media property] | [meaning] | [condition] | [selected format/range] | [explicit behavior; no invented default] |

Specify identity and reference resolution, relationships to other types, and
binary/media requirements where applicable. Link executable schemas only when
they exist. Keep examples distinct from selected requirements.

## Locations and provenance

- Loose-source location and source/creator/evidence references: [selected paths].
- Usable template and instructions: [actual path and use].
- Prepared library location: `res_lib/[selected organization]`.
- Engine import/derived destinations and mapping: [selected paths, or unresolved].
- Source-to-output linkage: [how identities, revisions and transformations are recorded].

## Preparation

Describe collection/authoring, formatting, any selected tool and its version,
required inputs, output checks, and manual steps. Preserve originals and identify
generated copies. State which unknowns block preparation versus later integration.

## Validation and use

| Requirement | Method / existing command or human activity | Expected outcome | Evidence and actual result |
|---|---|---|---|
| [syntax, semantics, references, dimensions, usability as applicable] | [available method] | [criterion] | [pending until performed] |

Separate file existence, format validity, reference integrity, successful import,
and observed usability. Record unavailable checks and the dependent activity they
prevent. A media description or generation prompt is not a delivered media file.

## Changes and compatibility

Describe revision identification, compatible and breaking changes, affected
consumers, conversion or manual migration if needed, and retention of source work.
Preserve identities on rewording; document retirement/replacement. Re-read current
contracts and affected shared records before authorized updates.
