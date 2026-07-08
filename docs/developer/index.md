# Developer Overview

This section is for maintainers, contributors, and documentation authors.

For code architecture, the canonical source is the repository docs:

- `docs/architecture.md`
- `docs/developer-notes.md`
- `docs/planning.md`
- `docs/node-roadmap.md`
- `docs/research-and-publication.md`

This MkDocs site is the user-facing searchable manual. It should avoid
duplicating deep implementation notes unless users need the information to run,
inspect, report, or troubleshoot workflows.

## Documentation Roles

| Document type | Belongs here? | Purpose |
| --- | --- | --- |
| Task guide | Yes | Help users perform a workflow. |
| Node reference | Yes | Help users choose and configure nodes. |
| Troubleshooting | Yes | Help users recover from common problems. |
| API docs | Later | Useful when the plugin API stabilizes. |
| Internal design notes | Mostly no | Keep in repository developer docs. |
| Publication planning | No | Keep in publication scratch space. |

