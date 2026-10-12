# Personal and Project Settings

Shared studio registration lives in `.codex/config.toml` and `.codex/hooks.json`.
Personal defaults belong in the user's supported Codex settings. This project
inherits model, reasoning, permissions, concurrency, and UI choices. It does not
install the source project's project-edit permission profile.

Use only settings supported by the active client/version. Avoid duplicate hook
registration across inline config and hooks.json. Project trust/enablement follows
the client's normal mechanism; do not modify personal trust automatically.

The game configuration authority remains docs/technical-preferences.md, with its
template at .codex/docs/technical-preferences.md (both installed; only the live document holds project selections).
Use the live preferences document for game settings; no separate project.yaml
settings resolver is supplied.

If hooks need a specific existing Python executable, supply LORSULIA_HOOK_PYTHON
in the launching environment. See [setup-requirements.md](setup-requirements.md).
Task authorization and runtime execution permissions remain separate.
