# Resource Preparation

Use this procedure for the workflow's resource-schema and preparation activities.
Read `RES_TYPE.md` and relevant definitions under `resource_templates/` when they
exist. Their authoring templates are [resource-type-catalog](templates/resource-type-catalog.md)
and [resource-type-definition](templates/resource-type-definition.md).

## Define the contract

Derive types from MDA needs, system GDD resource requirements and FRAMEWORK
operations. Map producers, consumers and relationships. Resolve consequential
choices with the developer; use the selected format and naming rules for each
type. Initial GDDs may precede these contracts; resource-integration review uses
the actual definitions and identifies incompatibilities in affected systems.

## Prepare and preserve

1. Collect or author loose material within the requested scope. Record its source,
   creator, intended use and applicable supplied usage terms. Preserve source files.
2. Apply the type's usable template and preparation instructions. Manual formatting
   or existing tools can satisfy the task. Define a custom tool only for a demonstrated
   unmet need using [tool development](tool-development.md).
3. Preserve stable identities and source/output linkage through formatting. Record
   unknown properties rather than manufacturing content or validation results.
4. Validate the applicable information, format and relationships using available
   checks. Distinguish missing resources from unreadable or unassessed resources.
5. Place prepared outputs in root `res_lib/` according to the selected type contract.
   Verify promised files by reading them back. Record selected import destinations
   and transformations; engine copies remain traceable to the authoritative resource.

## Review and maintain

Use `$asset-audit` for declared file/format constraints, `$content-audit` for
expected-content coverage, and `$review-all-gdds` or `$design-review` for the
applicable resource integration scope. These reviews require the corresponding
inputs; syntax alone cannot establish usability or approval.

For an addition or modification, follow `docs/FRAMEWORK.md`, identify affected
definitions, GDDs, relationships, prepared outputs and imports, and perform the
necessary checks. Re-read shared manifests/registries immediately before writing;
preserve concurrent changes and existing IDs. Keep completed work when a dependent
step fails and identify exactly which activity needs the missing result.

Audits are conversational by default. Existing explicit authorization can include
bounded saved reports. Record actual file, tool, engine and human observations
separately; pending human evaluation remains pending.

Use `.codex/docs/review-workflow.md` and the applicable director-gate requirements.
Optional review breadth never waives required independent review or human evidence.
Identify self-review and missing evidence; no required unassessed check can pass.
Follow the current environment's delegation policy. Use available qualified people
or agents; a missing persona can change executor but cannot erase required work.
`qa-tester`, `gameplay-programmer`, and `ui-programmer` are available; tool development
and game test infrastructure are supported by the installed work-preparation and testing skills; actual runner selection and human evidence remain project-specific.

Authoring saves stay within existing task authorization. Reviews/audits return
findings in conversation by default; an explicit request to save authorizes the
bounded report output, not design acceptance. Before shared writes, re-read the
current registry/manifest and preserve concurrent changes and stable identities.
Verify promised saved outputs by reading them back. Keep completed work and identify
which dependent activity lacks a result if a write or evaluation fails.


