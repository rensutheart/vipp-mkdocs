# Release notes

Release notes describe behavior that changes when VIPP is upgraded. They are
not a substitute for validating an analysis on representative and held-out
data.

## Release candidate

- [0.13.0a1](0.13.0a1.md) — evidence-gated
  **Auto / CPU / Prefer GPU / Custom** execution, durable compute provenance and
  cancellation across interactive and automated surfaces, workflow tabs, new
  scientific nodes, and extensive correctness/UI fixes.

This nightly entry is the prepared release manual. It becomes the stable,
numbered release documentation only after the matching application tag/package
and manual snapshot are published. Application commit
[`c2e88f8a8a9fd5638e4890fba8e8800e1b2450f1`](https://github.com/rensutheart/napari-vipp/commit/c2e88f8a8a9fd5638e4890fba8e8800e1b2450f1)
is the prepared source candidate and passed the complete package and
cross-platform test
[matrix](https://github.com/rensutheart/napari-vipp/actions/runs/31094506727).
The earlier `e024409` and `444f682` checkpoints remain historical evidence;
their artifacts must not be uploaded. The final tag, fresh release artifacts,
publication, numbered documentation, and post-publication checks remain
pending.

0.13.0a1 writes workflow schema 4 and batch config/manifest schema 2. Valid
schema-3 workflows and version-1 batch configs load as explicit CPU requests;
VIPP does not infer that an older analysis intended GPU execution. Workflow
files do not contain cached results. Recalculate and validate after upgrading,
and regenerate any Python export because generated programs require the exact
VIPP runtime version that created them.

## Previous releases

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
