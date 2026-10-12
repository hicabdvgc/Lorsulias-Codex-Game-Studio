# Coding and Design Standards

Apply the live technical preferences, relevant accepted ADRs, scoped CONTROL,
framework routes and actual engine conventions. Recommendations need project
adoption before becoming obligations. Do not impose an architecture pattern,
external-data format, source layout, or numeric performance budget by default.

Public interfaces explain their inputs, outputs, ownership, errors and relevant
constraints. Code should make the designed behavior understandable and checkable.
Choose data-driven values, composition, dependency injection, or other patterns
when the design and technical decisions call for them.

Design documents use the applicable templates, stable references and explained
values. No fixed section count determines completeness. Behavioral acceptance
criteria identify expected outcomes and an appropriate method of evaluation.

Verification follows the actual change: inspect content/contracts, run meaningful
automated checks where supported, and obtain human observations for experience or
usability conclusions. Record the build/revision, inputs, command/method, actual
result and limitations. Existing test files are not evidence of execution.
Repeatable tests can use controlled seeds/time; do not prohibit all randomness.
Use actual test roots and CI only when configured. Installed `$test-setup` and
`$test-helpers` support selected infrastructure; story execution/completion follows [execution and evidence](execution-and-evidence.md). Follow [root resolution](code-root-resolution.md) and checked
[runner references](testing-engine-reference.md). Criterion-level methods cover
code, resources, tools and framework integration. Use the selected language/runner
and meaningful tests, preserve existing work even in force mode, and keep required
independent review and human evidence explicit.
