# Versions and compatibility

This manual has two publication tracks and release-numbered snapshots.

| Selector | Meaning | Use it for |
| --- | --- | --- |
| **stable** | Alias intended for the current supported software release manual | Routine analysis after confirming the displayed version |
| **nightly** | Documentation built from this repository's `main` branch | Previewing unreleased docs and interfaces |
| **0.x.y…** | Immutable snapshot published for a particular release | Reopening old workflows or reporting exact methods |

This manual covers VIPP **0.15.0a4**. Use the
[canonical GitHub release](https://github.com/rensutheart/napari-vipp/releases/tag/v0.15.0a4)
for the exact manual-install wheel, unsigned Windows installer, separate
unsigned Apple Silicon and Intel macOS packages, checksums and qualification
evidence. Use the [PyPI 0.15.0a4 page](https://pypi.org/project/napari-vipp/0.15.0a4/)
for an exact package pin. The nightly manual may describe later unreleased work.

[0.15.0a4](../releases/0.15.0a4.md) retains
workflow, batch-config and manifest schema 6 from a3, including verified resume.
Earlier manifests cannot supply the new recovery evidence. New operations and
reproduction references still require a compatible runtime; unchanged schema
numbers do not promise backward compatibility.

Application publication and manual deployment are separate operations. Always
confirm the version shown by the manual selector; do not assume that the
**stable** alias moved merely because a new package was published.

The `main`/nightly manual can describe behavior newer than the latest tag. Use
the version selector when you need the manual for an installed release.

## Match software and manual

The VIPP interface displays its package version. Compare it with the version
selector in the site header. If they differ:

- switch the manual to the installed release; or
- install the release described by the manual in a separate environment.

Do not assume a workflow saved by one alpha release is compatible with another.
VIPP 0.15.0a4 writes workflow schema version 6, batch configuration version 6,
and manifest schema version 6; workflow versions 1 and 2 are rejected. Valid schema-3
workflows load with explicit CPU intent, schema-4 workflows retain authored
compute intent, and schema-5 workflows retain canonical SourceItem evidence.
Supported earlier batch configurations remain loadable and acquire their newer
fields only after review and save. Workflow JSON contains no source pixels or
cached scientific results. Recalculate and compare graph structure, parameters,
selected items, reader/backend, axes, channels, physical grids, dynamic ports,
compute request, node behavior, actual backend, and results on known sample
data. See the [workflow contract](workflow-contract.md).

## Move from 0.15.0a3 to 0.15.0a4

This is a presentation-fix update: clearer graph-wire routing and detailed
multichannel histogram outlines, including PNG/TIFF exports. Scientific
calculations, histogram values and schema versions are unchanged. Preserve
original analyses and environments, regenerate exported Python for the new
runtime, and recheck consequential results. See
[0.15.0a4 release notes](../releases/0.15.0a4.md).

## Move from 0.15.0a2 to 0.15.0a3

1. Preserve original workflows, inputs, outputs, environments and batch
   manifests. Open a duplicate for review; regenerate Python exports using the
   exact installed VIPP version.
2. Check new label-boundary QC and filter counts against the connected labels.
   These controls do not make or validate a new segmentation for you.
3. Review any RL/RL-TV numerical-difference advisory when choosing GPU execution
   beyond the earlier CPU-comparison region. Execution permission is not a
   guarantee of CPU equivalence or restoration quality.
4. Keep original schema-6 manifests and item sidecars for verified resume.
   Earlier manifests lack the required recovery evidence. A reproducibility
   package is a portable recipe/report, not a resume receipt or an environment.
5. When reopening a recorded package, choose original-run reproduction or new
   input data explicitly. Original-input checks and version acknowledgement do
   not establish matching scientific outputs; compare decisive results.

See [0.15.0a3 release notes](../releases/0.15.0a3.md).

## Move from 0.15.0a1 to 0.15.0a2

The workflow, batch-config and manifest schema numbers remain 6, 6 and 5. New node types and parameters nevertheless require 0.15.0a2; a shared schema number is not a promise that an older runtime understands new operations.

Legacy threshold and rescaling defaults retain equivalent batch-workflow identity after restore. Explicit non-default choices still affect that identity. Range-threshold history records both bounds and the endpoint rule; retain earlier manifests as the original execution record rather than rewriting their history.

1. Preserve original data, environments, workflows, batch configurations and decisive outputs. Open a duplicate for review and recalculate representative data.
2. Review Binary Threshold foreground choices. Above and Below are strict; In range includes both endpoints and Outside range excludes them. Existing nodes retain Above unless authored otherwise; saved range limits matter only in a range mode.
3. Use **Rescale Intensity → Invert intensity** for reversed mapping with ordered output bounds. Old reversed bounds are retained but must be corrected explicitly before calculation. Merely opening a workflow does not swap them.
4. Check reader/backend, selected series, axes, channels and calibration after moving to included native readers. **Reader support** checks installation health, not acquisition interpretation.
5. Review source **Channel display** and **Display settings** independently of scientific parameters. These presentation changes do not resample data or change processing.
6. Recalculate mesh measurements after smoothing or simplification; compare the changed geometry with the original branch. Inspect open-surface status and confirm units before 3MF export.
7. Regenerate Python exports using the exact installed VIPP version, and check batch plans and outputs before a large run.

See the [0.15.0a2 release notes](../releases/0.15.0a2.md) for the full change summary and limits.

## Move from 0.14.0a3 to 0.15.0a1

This is a substantial alpha update: the toolbar, inspector, batch window,
measurement views, and several scientific controls have changed. Supported
older documents still receive explicit migrations, but alpha status is not a
promise that every old workflow or generated program behaves identically.

1. Keep original workflows, configurations, prior manifests, and decisive
   outputs. Open a duplicate in the new release rather than overwriting the
   only record of an earlier analysis.
2. Review the source, axes, calibrated measurements, and results on known data.
   `Clip` is now called **Clamp Intensity**; the bound calculation is unchanged.
3. Review **ImageJ Default Threshold (8-bit)**. New nodes use the fixed Default
   method. An older saved ImageJ Triangle choice is retained as legacy behavior,
   not silently converted to Default.
4. Use the four Batch workflow tabs. Check before running; per-item keep/overwrite
   choices are saved in configuration version 6. Older configurations do not
   acquire invented item choices. Workflow version 6 and manifest version 5
   are unchanged from 0.14.0a3.
5. Regenerate exported Python using 0.15.0a1. Exported programs require the exact
   VIPP runtime version; a successful import is not an end-to-end result check.
6. Recheck actual compute decisions if enabling the new mesh/skeleton GPU
   candidates. A hybrid GPU implementation can still perform substantial CPU
   work; validate important measurements against the reference.

Legacy scatter-raster nodes remain executable but are hidden from the palette.
For new interactive plots, open the scatter window from a metrics node.

## Move from 0.14.0a2 to 0.14.0a3

0.14.0a3 adds responsive volumetric cropping, exact bounded source reads for a
strict direct local OME-Zarr Crop Stack path, safe node bypass and batch
execution profiles, workflow-editing improvements, and napari 0.9
qualification.

1. Preserve the exact 0.14.0a2 environment, original workflows, batch evidence,
   generated programs, and decisive outputs for provenance.
2. Install the exact qualified 0.14.0a3 asset for the platform, or use an exact
   package pin in a fresh environment. Do not replace the preserved a2
   environment in place.
3. Open a duplicate schema-5 workflow and review sources, graph structure,
   parameters, compute intent, and every node's Run/Bypass state. A workflow
   without saved bypass intent continues to run its nodes; saving the reviewed
   duplicate writes workflow schema 6.
4. Review the effective node behavior after loading any schema-4 batch
   configuration. Older configurations contain no whole-batch override and
   therefore use the workflow's authored behavior. Saving after review writes
   batch configuration schema 5, and new runs write manifest schema 5.
5. Recalculate known sample data and compare decisive intermediates and final
   results. Give focused attention to Crop Stack bounds, source identity,
   requested versus actual backends, bypass provenance, and batch outputs.

## Move from 0.14.0a1 to 0.14.0a2

0.14.0a2 is a focused desktop-compatibility and packaging alpha. It does not
change the SourceItem, reader, workflow-schema-5, batch-schema-4, per-sample,
OME-Zarr preview, or scientific CPU/GPU contracts introduced in 0.14.0a1.

1. Keep the original 0.14.0a1 environment, workflow, batch evidence, and
   decisive outputs for provenance.
2. Choose the checksum-verified Windows installer, the architecture-matched
   checksum-verified macOS package, or the wheel attached to the
   [GitHub release](https://github.com/rensutheart/napari-vipp/releases/tag/v0.14.0a2).
   The macOS packages are CPU-only, require macOS 13 or newer, and install a
   current-user environment under `~/Library/vipp` with
   `~/Applications/VIPP.app`.
3. Do not treat `pip install napari-vipp==0.14.0a2` as the resize-fixed build.
   PyPI's immutable a2 files predate that fix. Record the installation surface
   as well as the nominal version when reproducing an a2 environment.
4. Open a duplicate workflow and confirm sources, graph structure, parameters,
   compute intent, and decisive outputs. Schema migration is not expected, but
   an alpha update still warrants a focused comparison.
5. If VIPP is detached from napari, confirm that the floating window can be
   resized in width and height or maximized. Reattaching it should restore
   napari's dock constraints.

## Move from 0.13.0a9 to 0.14.0a1

0.14 introduces SourceItem identity, workflow schema 5, and batch
config/manifest schema 4. Treat the upgrade as a source and scientific review.

1. Preserve the 0.13 environment, workflow, input identities, outputs,
   execution reports, and batch artifacts.
2. Install `0.14.0a1` separately from the official checksum-verified installer
   or an exact package pin. Do not substitute an untagged build.
3. Open a duplicate workflow. Resolve every Image Source and verify the selected
   item, reader/backend, axes, shape, calibration, channels, and decisive
   results before saving schema 5.
4. For attached batch workspaces, let metadata-only discovery complete. Review
   every restored SourceItem and per-sample value; changed or missing sources
   must remain quarantined rather than being reassigned by order or filename.
5. Confirm that an OME-Zarr lower-level preview is labelled presentation-only
   and that analysis/output still use level 0.
6. Run CPU reference checks before relying on accelerator results, then inspect
   actual implementation badges and provenance for the intended compute mode.
7. Regenerate and revalidate exported Python and saved batch runners under a1.

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
   Custom to choose providers per node/apply **Find fastest pipeline…**. Auto uses
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

To reproduce a specific alpha exactly, use a fresh environment and record the
distribution surface as well as the version. An exact prerelease does not need
`--pre`. For 0.15.0a4, use the exact package pin:

```text
python -m pip install "napari[pyqt6]>=0.6" "napari-vipp==0.15.0a4"
```

On macOS use `napari[pyside6]` instead of `napari[pyqt6]`; macOS remains CPU-only.

For the optional CUDA 13 extra, use a separate 64-bit CPython 3.12 environment:

```text
python -m pip install "napari[pyqt6]>=0.6" "napari-vipp[gpu-cuda13]==0.15.0a4"
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
