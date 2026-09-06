# Release notes

Release notes describe behavior that changes when VIPP is upgraded. They are
not a substitute for validating an analysis on representative and held-out
data.

## Current public alpha

- [0.15.0a1](0.15.0a1.md) — task-based batch workflow, per-item output decisions,
  readable run reports, redesigned inspector and plots, reproducible intensity
  histograms, and hybrid mesh/skeleton measurement acceleration.

The alpha is distributed on
[GitHub](https://github.com/rensutheart/napari-vipp/releases/tag/v0.15.0a1) and
[PyPI](https://pypi.org/project/napari-vipp/0.15.0a1/). Use only the exact
release assets and their matching checksum files.

0.15.0a1 writes workflow schema 6, batch config 6, and manifest schema 5. Valid
supported earlier records retain explicit migration paths; recalculate and
validate consequential results after upgrading.

## Earlier releases

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
