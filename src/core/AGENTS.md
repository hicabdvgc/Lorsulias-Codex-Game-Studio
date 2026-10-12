# Core guidance

Read ../AGENTS.md and the studio root instructions. Use live technical preferences, code-root-resolution.md
and execution-and-evidence.md before dependent writes.

Implement the selected runtime interfaces and accepted dependency boundaries. Document resource
ownership, lifecycle, threading and error behavior. Measure performance-sensitive changes with comparable
before/after evidence. Allocation/streaming/pooling choices follow actual budgets and measured need;
no universal zero-allocation or RAII rule applies to every language. Maintain compatibility/migration
information when public consumers need it. Use real APIs for the selected engine version. Do not assume
that this skeleton directory is the project's engine or compilation root.
