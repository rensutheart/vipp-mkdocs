# Versions and compatibility

This manual has two publication tracks and release-numbered snapshots.

| Selector | Meaning | Use it for |
| --- | --- | --- |
| **stable** | Alias for the current supported software release manual | Routine analysis and citation |
| **nightly** | Documentation built from this repository's `main` branch | Previewing unreleased docs and interfaces |
| **0.x.y…** | Immutable snapshot published for a particular release | Reopening old workflows or reporting exact methods |

The current public software baseline is **0.11.0a1**. The `a1` suffix means an
alpha pre-release, not a nightly build.

## Match software and manual

The VIPP interface displays its package version. Compare it with the version
selector in the site header. If they differ:

- switch the manual to the installed release; or
- install the release described by the manual in a separate environment.

Do not assume a workflow saved by one alpha release is compatible with another.
Keep an original copy, migrate a duplicate, and compare graph structure,
parameters, dynamic ports, and results on known sample data.

## Install a release

Because alpha releases are pre-releases, use:

```text
python -m pip install "napari[pyqt6]"
python -m pip install --pre napari-vipp
```

To reproduce an older alpha exactly, specify the version in a fresh environment:

```text
python -m pip install "napari[pyqt6]" "napari-vipp==0.11.0a1"
```

## Nightly policy

Nightly documentation may describe work not yet available from PyPI and can
change without migration support. If unreleased behavior contributes to an
analysis, record the application commit, documentation commit, Python version,
and environment—not only a nominal package version.
