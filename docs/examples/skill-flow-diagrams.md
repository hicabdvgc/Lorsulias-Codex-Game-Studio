# Workflow Examples

These diagrams illustrate the catalog's dependencies. They do not replace manual work or evidence.

```mermaid
flowchart TD
  A[Developer CONCEPT and reference play] --> B[Preliminary BREAKDOWN and framework principles]
  B --> C[Full BREAKDOWN and preliminary FRAMEWORK]
  C --> D[System GDDs then full FRAMEWORK]
  D --> E[Architecture, Accepted ADRs and CONTROL]
  E --> F[Resource contracts, preparation, tools and relevant UX]
  F --> G[Integrated slice and actual human findings]
  G --> H[Prepared epics/stories and required reviews]
  H --> I[Vertical-slice hard gate]
  I --> J[Final milestones and optional sprints]
  J --> K[Execution, evidence and story completion]
  K --> L[Project-defined milestone evaluation]
  L --> M[Release requirements and final acceptance]
  M --> N[Authorized release and observed delivery]
```

```mermaid
flowchart LR
  A[Selected candidate and release requirements] --> B[Internal assessment]
  A --> C[External assessment]
  B --> D[Matching persisted READY reports]
  C --> D
  D --> E[Final acceptance and delivery authorization]
  E --> F[Verified delivery]
  F --> G[Authorized publication and actual monitoring]
```

Missing required evidence blocks the dependent conclusion. For session recovery, hooks read bounded
checkpoint regions; the user/agent verifies current substantive files. Explicit rotation archives
narrative without implying task completion or review approval.
