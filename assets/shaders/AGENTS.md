# Shader and Material Guidance

Use live docs/technical-preferences.md, applicable accepted architecture and the
selected shader/material resource contract. Record the actual engine, version,
render pipeline, target platforms and exposed parameter meanings. Preserve source,
prepared and imported relationships; no shared cross-engine prefix is imposed.

Comment non-obvious calculations and connect tunable values to their purpose.
Choose precision, sampling, branching, passes and variants based on actual behavior,
verified engine support and profiling. Do not impose blanket bans on branches or
loop reads, a universal blur technique, or an invented budget. Record selected
quality/fallback behavior and test relevant minimum-spec hardware when available.

Consult the installed selected-engine shader specialist/reference library and
verify applicable API claims against official versioned documentation. Missing
runtime, compilation or hardware evidence remains unassessed; source inspection
cannot establish visual correctness or performance. Use root resource_templates/
and res_lib/ contracts when preparing shader resources.
