# Release notes

Release notes describe behavior that changes when VIPP is upgraded. They are
not a substitute for validating an analysis on representative and held-out
data.

## Current alpha release

- [0.13.0a4](0.13.0a4.md) — compatible NVIDIA CUDA 13 admission for
  **Auto / CPU / Prefer GPU / Custom**, with cross-device reproducibility
  guidance and the retained a2/a3 planning, qualification, and Sigma fixes.

The alpha is published on
[GitHub](https://github.com/rensutheart/napari-vipp/releases/tag/v0.13.0a4) and
[PyPI](https://pypi.org/project/napari-vipp/0.13.0a4/). Its immutable
`v0.13.0a4` tag resolves to application commit
[`4bec1e8145b31e161beaf44a290bff24aea36f5e`](https://github.com/rensutheart/napari-vipp/commit/4bec1e8145b31e161beaf44a290bff24aea36f5e),
which passed the complete package and cross-platform test
[matrix](https://github.com/rensutheart/napari-vipp/actions/runs/31300028320).
The exact final artifact hashes are in the
[0.13.0a4 release verification](0.13.0a4.md#release-verification).

0.13.0a4 writes workflow schema 4 and batch config/manifest schema 3. Valid
schema-3 workflows and version-1 batch configs load as explicit CPU requests;
version-2 batch configs retain their saved compute request. Neither older batch
version contains source-axis declarations until reviewed and saved as version
3. The new Batch workspace **Image stack** choice can make one guarded,
visible `QYX -> ZYX` suggestion when the workflow proves that a generic TIFF
page dimension must be Z; it never moves pixels or invents calibration.
Workflow files do not contain cached results. Recalculate and validate after
upgrading, and regenerate any Python export because generated programs require
the exact VIPP runtime version that created them.

## Previous releases

- [0.13.0a1](0.13.0a1.md) — first evidence-gated GPU alpha with durable
  compute provenance, workflow tabs, and the current schema-4 foundation.

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
environment, batch configuration and manifests used for consequential work.
Consult [versions and compatibility](../reference/versioning.md) before opening
an older workflow in a newer release.
