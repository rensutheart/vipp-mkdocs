# Release notes

Release notes describe behavior that changes when VIPP is upgraded. They are
not a substitute for validating an analysis on representative and held-out
data.

## Current alpha release

- [0.13.0a6](0.13.0a6.md) — graph-fragment reuse and tunnel insertion,
  Compute Doctor 2.0, complete public-GPU admission checks, multi-series and
  Imaris sources, microscope metadata editing, and a public field checklist.

The immutable alpha is prepared for
[GitHub](https://github.com/rensutheart/napari-vipp/releases/tag/v0.13.0a6) and
[PyPI](https://pypi.org/project/napari-vipp/0.13.0a6/). Its exact application
commit, successful cross-platform CI run, explicit unsigned-installer status,
and qualified artifact hashes are recorded in
[0.13.0a6 release verification](0.13.0a6.md#release-verification). Public
availability remains a separate publication check, and downloaded-installer
field acceptance remains separate from artifact qualification.

0.13.0a6 writes workflow schema 4 and batch config/manifest schema 3. Valid
schema-3 workflows and version-1 batch configs load as explicit CPU requests;
version-2 batch configs retain their saved compute request. Neither older batch
version contains source-axis declarations until reviewed and saved as version
3. Workflow files do not contain cached results. Recalculate and validate after
upgrading, and regenerate Python exports because generated programs require the
exact VIPP runtime version that created them.

## Previous releases

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
