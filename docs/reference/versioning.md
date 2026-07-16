# Versions and compatibility

This manual has two publication tracks and release-numbered snapshots.

| Selector | Meaning | Use it for |
| --- | --- | --- |
| **stable** | Alias for the current supported software release manual | Routine analysis and citation |
| **nightly** | Documentation built from this repository's `main` branch | Previewing unreleased docs and interfaces |
| **0.x.y…** | Immutable snapshot published for a particular release | Reopening old workflows or reporting exact methods |

The current public software baseline is **0.12.0a2**. Its `a2` suffix identifies
the second alpha build in the 0.12.0 release series; it is a tagged pre-release,
not a nightly build. See [installation](../getting-started/installation.md) and
the [0.12.0a2 release notes](../releases/0.12.0a2.md).

The `main`/nightly manual can describe behavior newer than the latest tag. Use
the version selector when you need the manual for an installed release.

## Match software and manual

The VIPP interface displays its package version. Compare it with the version
selector in the site header. If they differ:

- switch the manual to the installed release; or
- install the release described by the manual in a separate environment.

Do not assume a workflow saved by one alpha release is compatible with another.
VIPP 0.12.0a2 retains schema version 3; versions 1 and 2 are rejected rather
than migrated automatically. A valid 0.12.0a1 schema-3 workflow loads
structurally in 0.12.0a2, but workflow JSON contains no cached scientific
pixels/tables. Recalculate and compare graph structure, parameters, sources,
axes, channels, physical grids, dynamic ports, and results on known sample
data. See the [workflow contract](workflow-contract.md).

## Move from 0.12.0a1 to 0.12.0a2

1. Keep the original workflow and 0.12.0a1 environment for provenance.
2. Open a duplicate workflow in 0.12.0a2 and confirm that graph structure,
   parameters, dynamic ports, and sources are as expected.
3. Recalculate the workflow. Cached results are not serialized in workflow
   JSON, so structural loading is not evidence that old outputs were restored.
4. Review the clearer bright-amber actionable and dark-amber waiting states,
   especially around manual nodes and isolated tuning, before calculating.
5. Compare decisive intermediates and final measurements with the validated
   0.12.0a1 results or other reference data.
6. Regenerate and revalidate Python exports. An export refuses a VIPP runtime
   version different from the one that generated it.

## Upgrade to 0.12.0a1

Schema 3 exists because silently supplying new scientific defaults could change
results. In particular, 0.12 requires explicit channel-axis and RGB/intensity
mapping choices for affected operations and strengthens source/grid behavior.

1. Keep the exact older VIPP environment and original workflow read-only.
2. Record the old graph, parameters, dynamic output ports, input series, axes,
   channel mapping, scale, units, and representative outputs.
3. Recreate the workflow in 0.12.0a1. Do **not** edit only the JSON `version`.
4. Resolve each new required scientific choice explicitly. Do not infer
   `channel_axis` from a trailing length-three/four dimension unless the data
   really are declared RGB/RGBA.
5. Verify every multi-input grid. Equal shape alone no longer establishes
   compatible axes, sampling, units, or origin.
6. Compare decisive intermediates and final measurements against known data or
   reference annotations before batch use.
7. Regenerate Python exports; generated programs require the exact VIPP runtime
   version that created them.
8. Create and preview a new `vipp_batch_config.json`; archive the workflow,
   config, manifest, sidecars, environment, and validation evidence together.

If the old environment is unavailable, use the JSON and methods notes as a
reference for manual reconstruction, but do not claim numerical equivalence
without testing it.

## Install a release

Because alpha releases are pre-releases, use:

```text
python -m pip install "napari[pyqt6]"
python -m pip install --pre napari-vipp
```

To reproduce a specific alpha exactly, specify the version in a fresh environment:

```text
python -m pip install "napari[pyqt6]" "napari-vipp==0.12.0a2"
```

## Nightly policy

Nightly documentation may describe work not yet available from PyPI and can
change without migration support. If unreleased behavior contributes to an
analysis, record the application commit, documentation commit, Python version,
and environment—not only a nominal package version.
