# Error Recovery Protocol

Use for incomplete execution, review, or delegated handoffs.

1. Verify promised outputs before treating an activity as complete. If a saved
   path was promised, inspect its existence and relevant contents. A fluent reply
   or empty file cannot establish the promised result. Conversation-only reviews
   have a returned result contract and require no invented saved file.
2. Name the missing/failed result and preserve completed work. Identify the next
   activity that actually depends on it; independent activities may continue.
3. Recover within the existing authorization: correct a known issue, or resume an
   available delegated task with the unmet contract made explicit. Verify the
   result again. Avoid repeating an unchanged failing action.
4. When recovery needs a missing decision, input, capability, or expanded scope,
   report it and ask for that specific information/action. Explain completed work
   and remaining limitations in a partial result.
5. Reassign to a qualified available executor when permitted. Preserve the output,
   independence, and human-evidence requirements. Report the actual executor.
   Skipping required work leaves its dependent result incomplete.

Use the actual runtime's tools and delegation policy. No fixed director, question
API, agent count, or permission to message another chat follows from this procedure.
