# Resource JSON Validation After Edits

The historical filename is retained for existing references. The installed handler
is `.codex/hooks/validate-assets.sh`, registered for PostToolUse / `^apply_patch$`.
It is not a Git post-merge hook. A post-merge audit is an explicit `$asset-audit`
activity using the merged project's actual resource contracts.

## Interface

Read one JSON object from stdin. `tool_input.command` may contain an apply_patch
payload (Add/Update/Delete File and Move to headers); direct path/file_path/paths
and patch/input fields are supported for direct checks. Unknown fields are ignored.
Other event/tool names are irrelevant and produce no output. Missing event/tool
names are accepted for direct invocation; malformed input remains unassessed.
Relative paths resolve from supplied absolute `cwd`, or the studio root if omitted.
The shared helper anchors that root outside Git and from nested launches. Windows
native and Git Bash drive paths, spaces and apostrophes are supported.

## Observations and limits

Only changed `.json` files resolving inside root `res_lib/` or `assets/data/` are
parsed. Outside paths, other formats and unrelated events are ignored. Deleted or
missing files are reported ABSENT without a syntax claim. Readable files produce
JSON SYNTAX OK or INVALID JSON with parser details. Unreadable files/unsupported
runtime are NOT ASSESSED. JSON NaN/Infinity are rejected. UTF-8 with BOM is accepted.

Relevant observations use JSON systemMessage and PostToolUse additionalContext on
stdout. Syntax findings are advisory and exit 0; invalid structured hook input or
missing parsers report NOT ASSESSED, and input/path execution errors return nonzero.
No files or logs are changed. The already completed patch cannot be undone here.
Naming, schema, reference integrity, media properties, additional import locations,
engine usability and build success require separate applicable audits/evidence.

## Runtime

Requires Bash plus the shared hook-lib.sh and working Python 3.9+; set the process
variable LORSULIA_HOOK_PYTHON when needed. Use the existing Windows launcher pattern.
Direct tests do not prove live event dispatch or project trust. The interface was
checked against [official Codex hooks documentation](https://learn.chatgpt.com/docs/hooks)
on 2026-10-08; client integration must be observed separately.
