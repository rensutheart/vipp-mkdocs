# napari-vipp MkDocs Material Draft

This is a first-pass searchable documentation scaffold for `napari-vipp`.

It is intentionally separate from the active code repository while the
documentation structure is being planned. Once stable, it can be moved into the
main repository or published as a separate documentation site.

## Preview Locally

```powershell
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install -r requirements.txt
mkdocs serve
```

Then open the local URL printed by MkDocs.

## Current Purpose

- Make VIPP searchable for expert users who want to get going quickly.
- Separate task-oriented docs from long-form training material.
- Identify where more documentation-only examples are needed.
- Identify which examples and samples should graduate into the core plugin.

