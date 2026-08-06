# Versions and compatibility

This manual has two publication tracks and release-numbered snapshots.

| Selector | Meaning | Use it for |
| --- | --- | --- |
| **stable** | Alias for the current supported software release manual | Routine analysis and citation |
| **nightly** | Documentation built from this repository's `main` branch | Previewing unreleased docs and interfaces |
| **0.x.y…** | Immutable snapshot published for a particular release | Reopening old workflows or reporting exact methods |

This `main`/nightly manual is being prepared for the **0.13.0a1 release**. Its
`a1` suffix identifies the first alpha build in the 0.13.0 release series.
It becomes a release-numbered public manual only after the matching application
tag/package and documentation snapshot are published. Until then, stable still
points to the previous public release. See
[installation](../getting-started/installation.md) and the
[0.13.0a1 release notes](../releases/0.13.0a1.md).

The prepared application source candidate is
[`c2e88f8a8a9fd5638e4890fba8e8800e1b2450f1`](https://github.com/rensutheart/napari-vipp/commit/c2e88f8a8a9fd5638e4890fba8e8800e1b2450f1).
Its package checks and CPython 3.12/3.13 tests on Windows, Linux, and macOS
passed in the exact-source
[CI run](https://github.com/rensutheart/napari-vipp/actions/runs/31094506727).
The previously prepared `e024409` and `444f682` checkpoints are historical,
not release sources; their hashes remain in the
[release notes](../releases/0.13.0a1.md#historical-prefer-gpu-automated-checkpoint-superseded)
only to prevent accidental reuse. The final tag, freshly built and hashed
release artifacts, publication, numbered manual snapshot, and post-publication
checks remain pending.

The `main`/nightly manual can describe behavior newer than the latest tag. Use
the version selector when you need the manual for an installed release.

## Match software and manual

The VIPP interface displays its package version. Compare it with the version
selector in the site header. If they differ:

- switch the manual to the installed release; or
- install the release described by the manual in a separate environment.

Do not assume a workflow saved by one alpha release is compatible with another.
VIPP 0.13.0a1 writes schema version 4; versions 1 and 2 are rejected. Valid
schema-3 workflows load structurally with an explicit CPU compute request and
become schema 4 only when saved. Workflow JSON contains no cached scientific
pixels/tables. Recalculate and compare graph structure, parameters, sources,
axes, channels, physical grids, dynamic ports, compute request, actual backend,
and results on known sample data. See the
[workflow contract](workflow-contract.md).

## Move from 0.12.0a3 to 0.13.0a1

0.13 introduces durable compute intent and can also change calculated
colocalization values. Treat the upgrade as a scientific review, not only a
file-format conversion.

1. Keep the original schema-3 workflow, 0.12.0a3 environment, generated Python,
   batch config, manifests, sidecars, and validated outputs unchanged.
2. Open a duplicate in 0.13.0a1. Confirm that its migrated compute mode is
   **CPU**. Inspect graph structure, parameters, dynamic ports, source bindings,
   axes/channels, physical grids, Batch Output declarations, and optional Batch
   workspace attachment.
3. Recalculate on CPU and compare decisive intermediates and final results.
   Cached arrays/tables were never embedded in the workflow. Give particular
   attention to colocalization thresholds, native-unit intensity sums, Pearson
   population fields, Manders fields, cropped masks, and ND2 axis order.
4. Save the reviewed duplicate as schema 4. The saved `execution.compute`
   object records `cpu`, `auto`, `prefer_gpu`, or `custom` mode and any
   authored per-node preferences; it does not record a promise about which
   implementation will actually be available on another machine.
5. If acceleration is wanted after the CPU comparison, use **Prefer GPU** to
   place every reviewed eligible operation on GPU regardless of speed, or use
   Custom to choose providers per node/apply **Find fastest**. Auto uses
   reviewed safe GPU defaults without compatible history; accelerated-only
   history schedules one same-surface CPU measurement before later matching
   runs apply the 1.20x/20-ms gate.
   Review CPU/CuPy/cuCIM/fallback badges and retain the actual-run execution
   provenance. Do not add an unplanned `Convert Dtype` merely to make a GPU
   benchmark faster.
6. Load or recreate Batch workspace. Version-1 batch configs migrate to an
   explicit CPU request and save as version 2. Review the configured/effective
   requests, memory and fallback policy, bindings, paths, collision policy, and
   fresh preflight before running.
7. Regenerate and revalidate exported Python and the saved batch runner. A
   generated 0.12 program refuses a 0.13 runtime by design.
8. For a consequential batch, test progress, cancellation, and OOM/fallback on
   non-critical data, then inspect the version-2 manifest's execution documents,
   digests, output links, cleanup evidence, and
   partial/skipped/cancelled/failed records.

The colocalization and ImageJ-threshold revisions have frozen automated
fixtures but still require independent upstream-method review. Treat them as
experimental and perform an external reference comparison before relying on
the revised values.

## Move from 0.12.0a2 to 0.12.0a3

1. Keep the original workflow, 0.12.0a2 environment, standalone batch config,
   manifests, item sidecars, and validated outputs for provenance.
2. Open a duplicate workflow in 0.12.0a3 and confirm that graph structure,
   parameters, dynamic ports, sources, and Batch Output declarations are as
   expected.
3. Recalculate the workflow and compare decisive intermediates and final
   measurements. Cached scientific results are not serialized in workflow
   JSON.
4. If using Batch workspace, review the suggested or restored destination,
   source bindings, patterns, formats, collision policy, and fresh preflight.
   Preview remains optional; Run does not implicitly calculate a representative.
5. Regenerate and revalidate Python exports. An export refuses a VIPP runtime
   version different from the one that generated it.
6. Inspect the finalized manifest and item sidecars after a batch, including
   partial, skipped, and failed items.

A 0.12.0a3 workflow can optionally carry a top-level `batch_config`. VIPP
0.12.0a2 can still reconstruct the schema-3 scientific graph because it ignores
that unknown top-level attachment, but it does not restore it and will omit it
if the workflow is saved again. Preserve the original 0.12.0a3 file when moving
between releases.

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

To ask pip to choose the latest unpinned alpha, use:

```text
python -m pip install "napari[pyqt6]"
python -m pip install --pre napari-vipp
```

To reproduce a specific alpha exactly, specify the version in a fresh
environment. An exact prerelease does not need `--pre`:

```text
python -m pip install "napari[pyqt6]>=0.6" "napari-vipp==0.13.0a1"
```

For the optional CUDA 13 extra, use a separate 64-bit CPython 3.12 environment:

```text
python -m pip install "napari[pyqt6]>=0.6" "napari-vipp[gpu-cuda13]==0.13.0a1"
vipp-compute-doctor --track cuda13
```

The extra installs a reproducible CUDA/CuPy track; it does not make an
unqualified GPU, driver, OS, or scientific stack scientifically admitted.
Never install both CUDA-major extras into one environment. See
[installation](../getting-started/installation.md#optional-nvidia-cuda-acceleration)
and the [64-bit Windows CUDA guide](../getting-started/windows-cuda.md).

## Nightly policy

Nightly documentation may describe work not yet available from PyPI and can
change without migration support. If unreleased behavior contributes to an
analysis, record the application commit, documentation commit, Python version,
and environment—not only a nominal package version.
