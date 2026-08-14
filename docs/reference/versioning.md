# Versions and compatibility

This manual has two publication tracks and release-numbered snapshots.

| Selector | Meaning | Use it for |
| --- | --- | --- |
| **stable** | Alias for the current supported software release manual | Routine analysis and citation |
| **nightly** | Documentation built from this repository's `main` branch | Previewing unreleased docs and interfaces |
| **0.x.y…** | Immutable snapshot published for a particular release | Reopening old workflows or reporting exact methods |

The nightly manual is currently prepared for **0.13.0a7**, but the immutable
a7 tag, public package, installer, hashes, and numbered snapshot are pending.
Its [release verification](../releases/0.13.0a7.md#release-verification) lists
those unresolved items explicitly. Do not interpret the nightly version label
as evidence that a release artifact exists.

The numbered **0.13.0a6** snapshot remains the latest verified public alpha,
published on
[GitHub](https://github.com/rensutheart/napari-vipp/releases/tag/v0.13.0a6) and
[PyPI](https://pypi.org/project/napari-vipp/0.13.0a6/). Its
[historical release verification](../releases/0.13.0a6.md#release-verification)
retains the exact application commit, tag, CI, unsigned-installer status,
artifact hashes, and numbered-manual publication.

The `main`/nightly manual can describe behavior newer than the latest tag. Use
the version selector when you need the manual for an installed release.

## Match software and manual

The VIPP interface displays its package version. Compare it with the version
selector in the site header. If they differ:

- switch the manual to the installed release; or
- install the release described by the manual in a separate environment.

Do not assume a workflow saved by one alpha release is compatible with another.
VIPP 0.13.0a7 writes schema version 4; versions 1 and 2 are rejected. Valid
schema-3 workflows load structurally with an explicit CPU compute request and
become schema 4 only when saved. Workflow JSON contains no cached scientific
pixels/tables. Recalculate and compare graph structure, parameters, sources,
axes, channels, physical grids, dynamic ports, compute request, actual backend,
and results on known sample data. See the
[workflow contract](workflow-contract.md).

## Move from an earlier 0.13 alpha to 0.13.0a7

The workflow and batch schemas do not change between 0.13.0a1 and 0.13.0a7,
but generated programs are version-locked, GPU regions changed, and accepted
dtype conversions are now ordinary visible graph edits.

1. Preserve the earlier environment, workflows, outputs, execution reports,
   batch artifacts, and any private cuCIM wheel and build manifest.
2. After publication, install `0.13.0a7` separately with the
   checksum-verified unsigned Windows installer, or upgrade a dedicated manual
   environment with an exact `napari-vipp==0.13.0a7` or
   `napari-vipp[gpu-cuda13]==0.13.0a7` pin. The a7 artifacts and hashes are
   currently pending; do not substitute an untagged build. Do not mix
   CUDA-major extras.
3. Run `pip check` and, for CUDA, `vipp-compute-doctor --track cuda13 --refresh`.
   Use only the matching a7-tagged cuCIM bundle/helper after it is published;
   never reuse an a6 bundle or copy an old approval record back manually.
4. Open a duplicate workflow, run it on CPU, and compare decisive intermediate
   and final results before enabling Auto or Prefer GPU.
5. Record the exact GPU model, compute capability, driver, CUDA and scientific
   package versions, and actual implementation IDs. Minor floating-point
   differences can occur across otherwise compatible devices.
6. Regenerate and revalidate exported Python and saved batch runners under a7.

## Move from 0.12.0a3 to 0.13.0a1

0.13 introduces durable compute intent and guarded source-axis declarations,
and can also change calculated colocalization values. Treat the upgrade as a
scientific review, not only a file-format conversion.

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
   explicit CPU request; version-2 configs retain their saved compute request.
   Neither older version contains a source-axis declaration. Review the
   source-specific **Image stack** choice, configured/effective requests,
   memory and fallback policy, bindings, paths, collision policy, and fresh
   preflight, then save the reviewed configuration as version 3.
7. Regenerate and revalidate exported Python and the saved batch runner. A
   generated 0.12 program refuses a 0.13 runtime by design.
8. For a consequential batch, test progress, cancellation, and OOM/fallback on
   non-critical data, then inspect the version-3 manifest's raw/effective source
   axes, applied declarations, execution documents, digests, output links,
   cleanup evidence, and partial/skipped/cancelled/failed records.

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
environment. An exact prerelease does not need `--pre`. The a7 examples below
apply only after PyPI publicly lists that version:

```text
python -m pip install "napari[pyqt6]>=0.6" "napari-vipp==0.13.0a7"
```

For the optional CUDA 13 extra, use a separate 64-bit CPython 3.12 environment:

```text
python -m pip install "napari[pyqt6]>=0.6" "napari-vipp[gpu-cuda13]==0.13.0a7"
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
