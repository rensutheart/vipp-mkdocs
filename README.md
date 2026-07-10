# VIPP user manual

This repository contains the public, searchable manual for
[`napari-vipp`](https://github.com/rensutheart/napari-vipp). The manual is
separate from the application repository so documentation releases and the
software release cycle can be managed independently.

## Preview locally

```powershell
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install -r requirements.txt
mkdocs serve
```

On macOS or Linux, activate with `source .venv/bin/activate`. Open the local URL
printed by MkDocs. A production-equivalent check is:

```text
mkdocs build --strict
```

## Versions

The site uses [mike](https://github.com/jimporter/mike):

- **stable** points to the manual for the current supported release;
- **nightly** is rebuilt from the documentation `main` branch;
- release-numbered snapshots remain available for older workflows.

See `docs/developer/docs-releases.md` for the deployment procedure. Publication
plans, manuscripts, private datasets, and internal screenshot roadmaps do not
belong in this repository.
