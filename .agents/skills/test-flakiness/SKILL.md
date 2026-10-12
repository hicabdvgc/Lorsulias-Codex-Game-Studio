---
name: test-flakiness
description: Identify intermittent test results from comparable runs and maintain
  explicitly authorized evidence-based recommendations.
---

# Test Flakiness

Invoke as `$test-flakiness`. Arguments: `[ci-log-path | scan | registry]`.

Read [.codex/docs/execution-and-evidence.md](../../../.codex/docs/execution-and-evidence.md) for authorization, status, criterion-level evidence, review and recovery contracts. Read the relevant sources before editing.


Use an explicit existing log, scan available authorized CI/local logs, or inspect the existing
regression manifest's Quarantined Tests registry. Resolve an unambiguous scope or ask. Repository
CI tools are conditional on actual access; no credentials or new CI setup is implied.

Extract stable test identity, revision/build, runner/environment, pass/fail and run identity.
Compare repeated runs of the same revision and relevant conditions; missing runs mean not observed.
Mixed pass/fail under comparable conditions supports observed intermittence. Show failures/observed
runs and sample limitations without preset minimum samples, probability claims or severity cutoffs.
Separate persistent failures, changed-code regressions and incomparable data. No logs cannot prove
clean tests. Possible timing, shared-state, randomness, ordering and environment causes remain
hypotheses until evidence supports them; remedies must use the selected language/runner's real APIs.

Return affected tests, raw evidence links, comparison basis, impact and proposed investigation or
repair. Registry mode reports current quarantine decisions and stale/missing references. An authorized
update may annotate tests/regression-suite.md and/or save a scoped production/qa report; re-read it,
preserve concurrent entries and list the actual changes. Proposing or recording quarantine does not
skip/disable tests or change CI. A repair or runtime quarantine needs separate scope authorization,
then relevant repeated execution. Never claim that a retry converted a failing run into a clean one.
