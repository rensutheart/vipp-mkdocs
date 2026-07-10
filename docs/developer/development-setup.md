# Set up a development environment

## Application repository

```powershell
git clone https://github.com/rensutheart/napari-vipp.git
cd napari-vipp
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

On macOS/Linux activate with `source .venv/bin/activate`.

Run the baseline checks before editing:

```text
python -m npe2 validate src/napari_vipp/napari.yaml
python -m ruff check .
python -m pytest
```

Launch a development widget with `python scripts/launch_vipp_sample.py` or list
review workflows with:

```text
python scripts/launch_vipp_intensity_workflow.py --list
```

## Manual repository

```powershell
git clone https://github.com/rensutheart/vipp-mkdocs.git
cd vipp-mkdocs
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
mkdocs serve
```

Before submitting a manual change run:

```text
mkdocs build --strict
```

Use the manual's exact dependency pins so local warning behavior matches CI.

## Useful application maps

The application repository's maintained architecture and contributor notes are
the source of truth for implementation boundaries:

- [`docs/architecture.md`](https://github.com/rensutheart/napari-vipp/blob/main/docs/architecture.md)
- [`docs/developer-notes.md`](https://github.com/rensutheart/napari-vipp/blob/main/docs/developer-notes.md)
- [`docs/cache-and-memory.md`](https://github.com/rensutheart/napari-vipp/blob/main/docs/cache-and-memory.md)

Read only the relevant plan/history material; do not copy speculative roadmap
claims into the public manual as current capability.
