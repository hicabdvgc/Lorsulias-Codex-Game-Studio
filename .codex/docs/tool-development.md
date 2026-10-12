# Tool Definition, Development and Evaluation

Use this procedure when resource preparation or framework operations reveal a
specific unmet tooling need. An existing engine feature, manual process or available
tool may already satisfy it. A tool library is built from demonstrated needs.

1. Describe the intended user, blocked activity, representative material and desired
   outcome. Evaluate the available alternatives and record the selected approach.
2. Use the [technical-design template](templates/technical-design-document.md)
   at the scope the tool needs: prerequisites, selected runtime, inputs, outputs,
   identities, error behavior, permitted changes, dependencies and usage. Link the
   relevant TYPE_TEMP and FRAMEWORK contracts; unresolved choices remain explicit.
3. Implement the authorized tool with an available qualified executor. The technical
   artist can support relevant resource pipelines; the installed tools-programmer,
   qa-lead and test-setup/test-helpers/qa-plan support their applicable responsibilities. Role names do not grant
   tools or substitute for required review.
4. Execute an end-to-end example with representative input, inspect the saved output
   and its next consumer, and exercise a relevant failure. Preserve completed source
   work and distinguish tool errors from invalid input or missing dependencies.
5. Have the intended human user perform the relevant activity and record the actual
   outcome and usability issues. An agent walkthrough is separate evidence. Without
   human use, mark that evaluation pending and keep the dependent completion claim open.
6. Keep the selected tool under root `tools_lib/` with its actual setup, dependencies,
   invocation, input/output examples, limitations and verification information. Verify
   instructions against the implemented tool. Record compatibility and affected
   resources when it changes; rerun the affected checks.

No engine installation, fixed tool suite, universal language or automatic testing
runner is supplied by this procedure. Future game tools and their evidence are
outputs of using it. Write only within the task's existing authorization and verify
promised outputs before handing them to resource preparation or implementation.
