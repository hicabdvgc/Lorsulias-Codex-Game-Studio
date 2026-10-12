# Studio Skill Testing Framework

This foundation evaluates reusable studio instructions: whether skills/personas
can deliver the requested result in the expected form. Game tests belong to the
later game-development procedures.

## Contents and use

- `catalog.yaml` records installed identities, categories and specification locations.
  The actual filesystem supplies discovery truth; missing coverage is a finding.
- `quality-rubric.md` supplies outcome criteria by category.
- `skills/` and `agents/` contain behavioral specifications.
- `templates/` contains authoring forms for those specifications.
- `results/` is an optional, gitignored destination for separately authorized
  evaluation records; it is not populated by skill-test.
- [runtime/](runtime/README.md) supplies reusable structural and isolated helper checks.
  Generated reports belong in the ignored results directory.

Use `$skill-test static [name|all]`, `$skill-test spec [name]`,
`$skill-test category [name|all]`, or `$skill-test audit`. Each mode returns its
results in conversation. Use `$skill-improve [name]` for a bounded repair and
revalidation cycle based on demonstrated findings.

All 76 installed skills and 49 personas have registered specifications. Specifications
define expected behavior; actual instruction exercises and native integration checks
require their own observed results.
Recompute counts and identities from the filesystem on each audit.

## Evidence

Static/spec/category checks examine the written package or procedure. They do not
execute the target skill. For behavioral evaluation, give an agent a representative
request and necessary inputs, use an isolated fixture for writes, and inspect the
actual result against the expected outcome. Record what ran and any limitations.
No automated model-evaluation runner is shipped here. Manual walkthroughs remain
identified as walkthroughs. Hook execution can be checked separately with event
payloads without executing the command text being inspected.

Missing required evidence prevents a passing result for the affected check. Known
failures remain visible. Inapplicability needs a scope reason. A scoped successful
evaluation does not certify unrelated installed or future components.
