# Gameplay guidance

Read ../AGENTS.md and the studio root instructions. Use live technical preferences, code-root-resolution.md
and execution-and-evidence.md before dependent writes.

Implement actual mechanics, state transitions and edge cases from governing GDDs/FRAMEWORK. Keep
values configurable where the selected resource contracts require it. Follow accepted interfaces for
UI and other consumers without imposing events, dependency injection or a singleton ban globally.
Use timing semantics appropriate to simulation and the selected API. Verify applicable logic,
integration, resource and human experience criteria; test counts and story type cannot waive them.
