# Release notes

Release notes describe behavior that changes when VIPP is upgraded. They are
not a substitute for validating an analysis on representative and held-out
data.

## Current verified public alpha

- [0.13.0a8](0.13.0a8.md) — one standard CuPy-only GPU installation,
  CuPy background and basic-measurement providers, Remove Outliers, safer
  optimizer assignment, wire insertion, and explicit source-axis handling.

The immutable a8 alpha is distributed on
[GitHub](https://github.com/rensutheart/napari-vipp/releases/tag/v0.13.0a8) and
[PyPI](https://pypi.org/project/napari-vipp/0.13.0a8/). Its exact source, CI,
GPU admission, intentionally unsigned normal installer, and artifact hashes
are recorded in the
[a8 release-verification table](0.13.0a8.md#release-verification).

0.13.0a8 writes workflow schema 4 and batch config/manifest schema 3. Valid
schema-3 workflows and version-1 batch configs load as explicit CPU requests;
version-2 batch configs retain their saved compute request. Neither older batch
version contains source-axis declarations until reviewed and saved as version
3. Workflow files do not contain cached results. Recalculate and validate after
upgrading, and regenerate Python exports because generated programs require the
exact VIPP runtime version that created them.

## Earlier releases

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
