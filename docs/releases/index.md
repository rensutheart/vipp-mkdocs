# Release notes

Release notes describe behavior that changes when VIPP is upgraded. They are
not a substitute for validating an analysis on representative and held-out
data.

## 0.16.0a1 — unreleased preparation

[Read the 0.16.0a1 overview](0.16.0a1.md) for the combined measurement,
Results Workspace and seeded-segmentation features, suggested first examples,
and compatibility limits. This preparation does not announce a published
package or completed release qualification. The current published
installation instructions remain on 0.15.0a5.

### Changes after 0.15.0a5

- [Name graph nodes](../how-to/edit-graph.md#name-a-node) through the inspector's
  **Name** field or **Rename…**. Table Source, Statistics and Plot Results also
  receive descriptive automatic labels. Names stay consistent in the graph,
  Results Workspace, workflow search and connected-input descriptions, with
  source context and stable identifiers for matching names. Save, undo and
  copy names with the workflow; renaming leaves calculations and figure titles
  unchanged.
- [Results Workspace](../how-to/results-workspace.md) keeps Data, Summary and
  Plots beside their controls. Add or edit ordinary Statistics/Plot Results
  nodes with synchronized inspectors and windows, and explicitly choose
  original measurements or summary rows as the plot source. Table search and
  visible columns do not change the analysis or full-table exports.
  Maximize the window from its title bar, and use **Workflow** to choose any
  open workflow before browsing its data sources. Edits and calculations stay
  with the selected workflow.
- [Plot axis spacing](../how-to/plot-measurement-results.md#set-grid-and-axis-label-spacing)
  offers Auto or custom positive numeric tick intervals, with grid lines at
  those ticks and the same settings in exported figures. Count-axis intervals
  remain integers; category spacing and log axes use automatic ticks.
- [Statistics](../how-to/summarize-measurements.md) expands Summarize
  Measurements with descriptive object, image-mean and sample-mean summaries,
  explicit within-sample weighting, exclusion counts and retained units.
  New recipes report singleton sample SD as undefined; old summaries retain
  their previous behavior until explicit upgrade. No tests, p-values,
  significance labels or confidence intervals are added.
- [Plot measurement results](../how-to/plot-measurement-results.md) as grouped
  points, histograms, cumulative distributions or scatter plots, with an
  editable window and sized raster/vector figure export. Distinguish objects
  from equally weighted image means; plots are descriptive.
- [Dialog buttons](../reference/interface.md#dialog-buttons) follow one
  platform-appropriate order: the main action then **Cancel**/**Close** on
  Windows, and the reverse pair on macOS. Stopping active work stays separate
  from dismissing its window; native file pickers are unchanged.
- [Collect batch measurements](../how-to/collect-measurement-results.md) into
  one reviewed table and export CSV/TSV or Excel directly, without reprocessing
  images. Preserve image/object identities and annotations; retain empty and
  excluded images in the optional CSV/TSV image summary or the workbook's
  always-present **Image summary** sheet. Excel also includes **Measurements**
  and **About this collection** with units and run information. Saving a native
  VIPP dataset and opening it through **Table Source** are separate, optional
  steps. No new plots or statistical tests are included.
- A separate three-dot [Workflow actions menu](../reference/interface.md#workflow-actions-menu)
  after **Save** holds examples, **Save workflow as…** and exports, keeping them
  separate from the gear menu's settings. Saving and export behavior is unchanged.
- Windows setup shows a [live installation log](../getting-started/installation.md#read-the-live-installation-log)
  for package downloads and installation. Scrolling up pauses automatic following;
  **Jump to latest** resumes it. This is not part of the numbered 0.15.0a5 release.
- Six **CellProfiler compartment profile** nodes add the statistics paper's
  explicit 2D smoothing, thresholding, nuclear segmentation, seed preparation,
  cell-region finishing and cytoplasm construction. See the
  [worked workflow](../workflows/statistics-paper-compartments.md) and
  [input and parameter reference](../reference/cellprofiler-compartments.md).
  Agreement with the original CellProfiler runtime is recorded separately
  from reproduction of published measurements.
- **Grow Regions from Seeds — CellProfiler Propagation** adds the 2D CPU
  Centrosome method with image, seed-label and Boolean mask inputs. It preserves
  seed IDs, requires one aligned YX plane and exposes regularization without
  hidden intensity normalization. See the
  [task guide](../how-to/grow-regions-from-seeds.md) and
  [compatibility boundary](../reference/seeded-segmentation.md).
- The seeded-segmentation guide also explains existing 3D watershed, including
  its voxel-grid distance and anisotropic-calibration limits.

## 0.15.0a5 alpha

- [0.15.0a5](0.15.0a5.md) — guided examples, a Boolean colocalization mask and
  overlap-region counting, simpler desktop launch/update controls, and clearer
  inspector histograms and mesh-display warnings.

Use the canonical
[GitHub release](https://github.com/rensutheart/napari-vipp/releases/tag/v0.15.0a5) and
[PyPI page](https://pypi.org/project/napari-vipp/0.15.0a5/). Use only the exact
release assets and their matching checksum files.

0.15.0a5 writes workflow schema 6, batch config 6, and manifest schema 6. Valid
supported earlier records retain explicit migration paths; recalculate and
validate consequential results after upgrading.

## Earlier releases

- [0.15.0a4](0.15.0a4.md) — clearer graph-wire routing and overlapping
  multichannel histograms, including PNG/TIFF exports. Scientific calculations
  are unchanged from a3.

- [0.15.0a3](0.15.0a3.md) — reviewed reproducibility packages,
  original-input checks, verified batch resume, object QC, broader RL GPU
  execution with advisories, and desktop/workflow presentation fixes.

- [0.15.0a2](0.15.0a2.md) — included microscope readers and diagnostics, quiet update guidance, four threshold modes, explicit intensity inversion, safer controls, Convex Hull, and mesh-object creation/refinement/export.

- [0.15.0a1](0.15.0a1.md) — task-based batch workflow, per-item output decisions, readable run reports, redesigned inspector and plots, reproducible intensity histograms, and hybrid mesh/skeleton measurement acceleration.

- [0.14.0a3](0.14.0a3.md) — responsive volumetric Crop Stack, exact bounded
  local OME-Zarr reads for the sole-direct-Crop case, topology-safe bypass,
  improved save/undo behavior, and napari 0.9 compatibility.

- [0.14.0a2](0.14.0a2.md) — native unsigned CPU-only macOS installers for
  Apple Silicon and Intel, detached-window resizing, cross-Qt compatibility,
  and a refreshed unsigned Windows installer. Its historical release page
  records the distinct GitHub and PyPI package hashes from that publication.

- [0.14.0a1](0.14.0a1.md) — durable SourceItem identity, truthful microscope
  reader contracts, dynamic local OME-Zarr preview without changing analysis,
  typed per-sample batch values, restored Batch UX, and clearer installer
  capacity and activity.

The immutable a1 alpha is distributed on
[GitHub](https://github.com/rensutheart/napari-vipp/releases/tag/v0.14.0a1) and
[PyPI](https://pypi.org/project/napari-vipp/0.14.0a1/). Its exact tag packages,
intentionally unsigned installer, checksum, release manifest, and notices are
available from the canonical GitHub release.

0.14.0a1 writes workflow schema 5 and batch config/manifest schema 4. Valid
workflow schemas 3 and 4 and batch versions 1 through 3 retain explicit
migration paths. Older records acquire SourceItems when sources are resolved;
older batch records contain no per-sample parameter overrides. Workflow files
do not contain cached results or source pixels. Recalculate and validate after
upgrading, and regenerate Python exports because generated programs require the
exact VIPP runtime version that created them.

- [0.13.0a9](0.13.0a9.md) — Prefer GPU planning across CPU-only nodes,
  immediate QYX-to-ZYX inspector propagation, explicit volumetric
  skeletonization, stable sibling measurement caches, and actionable GPU VRAM
  preflight errors.

The immutable a9 alpha remains available on
[GitHub](https://github.com/rensutheart/napari-vipp/releases/tag/v0.13.0a9) and
[PyPI](https://pypi.org/project/napari-vipp/0.13.0a9/). Its exact source, CI,
focused GPU evidence, intentionally unsigned normal installer, and artifact
hashes are recorded in the
[a9 release-verification table](0.13.0a9.md#release-verification).

- [0.13.0a8](0.13.0a8.md) — one standard CuPy-only GPU installation,
  CuPy background and basic-measurement providers, Remove Outliers, safer
  optimizer assignment, wire insertion, and explicit source-axis handling.

The immutable a8 alpha remains available on
[GitHub](https://github.com/rensutheart/napari-vipp/releases/tag/v0.13.0a8) and
[PyPI](https://pypi.org/project/napari-vipp/0.13.0a8/). Its exact source,
qualification boundary, installer, and artifact hashes are recorded in the
[a8 release-verification table](0.13.0a8.md#release-verification).

- [0.13.0a7](0.13.0a7.md) — visible one-click dtype repairs, readable
  per-implementation optimizer results, broader RL backend agreement, and a
  connected GPU segmentation/mask-cleanup example.

The immutable a7 alpha is public on
[GitHub](https://github.com/rensutheart/napari-vipp/releases/tag/v0.13.0a7) and
[PyPI](https://pypi.org/project/napari-vipp/0.13.0a7/). Its exact source, CI,
GPU admission, intentionally unsigned installer, seven release assets, hashes,
and numbered-manual publication are recorded in the
[a7 release-verification table](0.13.0a7.md#release-verification).

- [0.13.0a6](0.13.0a6.md) — graph-fragment reuse and tunnel insertion,
  Compute Doctor 2.0, complete public-GPU admission checks, multi-series and
  Imaris sources, microscope metadata editing, and a public field checklist.

The immutable a6 alpha is public on
[GitHub](https://github.com/rensutheart/napari-vipp/releases/tag/v0.13.0a6) and
[PyPI](https://pypi.org/project/napari-vipp/0.13.0a6/). Its exact source, CI,
unsigned-installer status, artifact hashes, and numbered-manual publication
remain recorded in
[0.13.0a6 release verification](0.13.0a6.md#release-verification).

- [0.13.0a5](0.13.0a5.md) — checksum-first unsigned Windows setup, branded
  launchers, transactional install/update/repair, independently removable CPU
  and CUDA installations, and a separate optional cuCIM local-build bundle.

- [0.13.0a4](0.13.0a4.md) — compatible NVIDIA CUDA 13 admission across GPU
  models meeting the released technical and scientific gates.

- [0.13.0a1](0.13.0a1.md) — first evidence-gated GPU alpha with durable
  compute provenance, workflow tabs, and the schema-4 foundation.

- [0.12.0a3](0.12.0a3.md) — direct batch execution, faster complete skips,
  more resilient provenance writes, suggested output destinations, and optional
  workflow-attached Batch workspace settings.

- [0.12.0a2](0.12.0a2.md) — isolated node tuning, clearer actionable and
  waiting execution states, progressive previews, faster exact-pixel display,
  graph port-label controls, and more legible PSF/deconvolution guidance.

- [0.12.0a1](0.12.0a1.md) — architectural and scientific-contract overhaul,
  workflow schema 3, deterministic batch provenance, retained representative
  navigation, and stricter source/grid validation.

VIPP is alpha software. Preserve the application version, workflow, inputs,
environment, batch configuration, and manifests used for consequential work.
Consult [versions and compatibility](../reference/versioning.md) before opening
an older workflow in a newer release.
