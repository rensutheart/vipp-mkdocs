# Save, share, and export

VIPP offers several outputs that solve different problems. They are not
interchangeable.

| Artifact | Use it for | Does not contain |
| --- | --- | --- |
| Workflow JSON (schema 6) | Reopen/edit the graph and authored compute/bypass request in VIPP 0.15.0a2; optionally restore an attached versioned batch configuration | Cached pixels/tables, actual-run implementation provenance, Python environment, source bytes |
| Exported Python | Execute immutable validated workflow JSON through VIPP's shared headless executor with compute/progress/cancellation controls | Interactive UI, caches, a portable runtime environment |
| Saved image/table plus provenance sidecar | Analysis result or QC artifact bound to one execution/output when exported through the generated program | Parameter rationale, input archive, proof of biological validity |
| OME analysis dataset | Reference image plus associated graph label outputs | A complete project/archive, arbitrary standalone table provenance, or an exact compute-provenance sidecar |
| Batch config (version 6) | Recreate source bindings, stable SourceItems, axis declarations, per-sample numeric overrides, batch Run/Bypass profiles, individual existing-output choices, output definitions, naming, policy, workflow association, and compute request | Input bytes, actual run decisions, finalized outcome |
| Batch manifest/archive (version 5) and sidecars | Audit planned inputs/outputs, SourceItems, raw and effective source axes, effective values and bypass choices, identities, hashes, configured/effective compute, exact node implementations, fallbacks, cleanup, errors, and per-item/output status | One atomic transaction or proof of biological validity |
| Reproducibility package (unreleased after 0.15.0a2) | Review and share an offline report, portable recipe, version summaries and sanitized available run evidence | Raw/result data, original run receipts, resumable state, an installed or locked environment |

Use [Export a reproducibility package](export-reproducibility-package.md) for
the review-before-sharing procedure. The workflow action describes a current
recipe; the batch-results action uses recorded archived evidence.

## Open a workflow

Choose **Open** and select a saved workflow `.json` file. VIPP opens it in a new
tab, keeping existing workflows and unsaved edits intact.

**Unreleased after 0.15.0a2:** drag a local workflow `.json` file from your file
manager onto VIPP's workflow canvas, tab strip, or inspector to open it in a new
tab. Dropping a file uses the same workflow validation as **Open**. Recorded
reproducibility workflows still ask whether to **Reproduce original run** or
**Use workflow on new data**; review that choice before continuing to Batch
Setup. See [reopen a reproducibility package](export-reproducibility-package.md).

## Save a workflow

Choose **Save workflow** or press ++ctrl+s++. Use `.json` and include a meaningful analysis name.
The action saves the active workflow tab; other tabs keep their own paths,
dirty baselines, caches, and histories. Closing a dirty tab still uses
Save/Discard/Cancel handling.

The default save policy overwrites the active workflow's existing JSON. A first
save asks for a destination and confirms before replacing an existing file.
Under **Settings → Workflow saving**, choose confirmation on every overwrite or
timestamped copies when that better matches the project's recordkeeping. A
successful save clears the tab's dirty asterisk and reports **Saved workflow**.
Bundled examples remain templates and are never overwritten in place.
Use ++ctrl+shift+s++ or **Settings → Save workflow as…** when the active tab
should be written to a different name or location without changing the normal
save policy.
If a Batch workspace is active, VIPP asks what to save:

- **Yes** attaches the current versioned batch configuration to the same
  workflow JSON. This includes source bindings, local input/output paths,
  patterns, formats, and run policies. It does not include input pixels,
  computed arrays, or output files.
- **No** writes the ordinary graph-only workflow. Use **Save config** in
  Batch workflow if a separate configuration is required.
- **Cancel** writes nothing.

Loading a workflow with a valid attachment restores and opens Batch workspace
with those settings, then checks sources in the background. This rematches
saved SourceItems, per-sample overrides, and exact-item file policies without
loading representative pixels or calculating the graph. **Preview selected**
remains optional, and Run performs a final validation. If the
attachment is unsupported or does not match the workflow, VIPP loads the
scientific workflow but reports that its Batch workspace could not be restored
rather than silently applying the settings.

Before sharing:

1. Reopen the file in the same VIPP release.
2. Confirm every `Image Source` intentionally references a sample, layer, file,
   or store.
3. Review graph notes, paths, source names, and metadata for sensitive text.
4. Recalculate manual nodes and compare expected outputs.

Workflow compatibility can change between alpha releases. Keep an unmodified
copy of the original and record the version that created it.

0.15.0a2 writes schema 6 and rejects versions 1 and 2. Valid schema-3 workflows
load with explicit CPU intent. Schema-4 and schema-5 workflows retain authored
compute intent; schema 5 also retains canonical SourceItems, while schema-4
sources acquire them when they resolve. Schema 6 adds persisted safe-node bypass
intent. Cached pixels and tables are not serialized. Inspect selected items,
readers, axes, bypass choices, and decisive outputs before saving the reviewed
duplicate. Earlier release-to-release procedures remain available for older
workflows.
Recreate schema-1/2 graphs deliberately; do not edit only the JSON version. See
the separate [schema-1/2 rebuild procedure](../reference/versioning.md#upgrade-to-0120a1).

## Save a selected output

Select the desired output and choose **Save selected output...**. The available
format depends on the data type and dimensionality. For tables use CSV or TSV;
for scientific images prefer a format that can represent the axes, dtype, and
calibration you need.

Read the [input/output reference](../reference/import-export.md) before using a
display-oriented raster format or ImageJ TIFF for label IDs.

This interactive action writes the selected cached value directly. It does not
rerun the graph through the shared executor or create an exact execution-
provenance sidecar. Use the generated CLI with provenance enabled, or the
durable batch runner, when the saved result must carry that record.

## Export an OME analysis dataset

**Export OME dataset...** serializes the cached reference image and selected graph
label outputs. It likewise does not rerun the graph or add exact per-node
compute provenance. Use it for the documented image/label association, not as
a substitute for generated-CLI provenance or a finalized batch manifest and
item sidecars.

## Export Python

Choose **Export Python...** when a graph needs a reviewable headless program. The
script embeds validated immutable workflow JSON, constructs a fresh pipeline
per call, and uses the same headless executor as VIPP. It carries supported
`ImageState`, accepts explicit multi-source bindings, and fails on missing,
duplicate, or unknown sources.

The script records the exact VIPP version that created it and refuses another
runtime. Regenerate and revalidate it after every upgrade, including alpha
updates. UI caches, pinned layers, and graph layout are presentation state and
are intentionally absent.

Python callers can pass a complete `ComputeRequest`, progress callback, and
cooperative cancellation token. The generated CLI accepts
`--compute-mode`, `--fallback-policy`, repeatable `--node-preference`,
`--progress`, and provenance controls. Omitted CLI fields retain the embedded
workflow compute request; overrides do not mutate the workflow.

`--compute-mode prefer_gpu` requests every scientifically eligible reviewed
public GPU implementation regardless of CPU speed. It requires visible
fallback; when no fallback override is provided, the CLI supplies `visible`,
while an explicit strict combination is rejected. Stored per-node preferences
remain in the workflow but are inactive outside Custom. The generated path
uses the same planner and exact implementation provenance as interactive and
batch execution. Bypassed nodes forward their exact primary input without
invoking a backend and are recorded as bypassed rather than CPU or GPU work.

With provenance enabled, a successful saved output receives an atomic sibling
such as `result.ome.tif.vipp-provenance.json`. The document binds the output
node/port to the effective request, actual CPU/CuPy implementation,
fallbacks, environment, outcome, and cleanup evidence. A failed or cancelled
single-output run also attempts a failure sidecar. Publication fails closed if
GPU cleanup or final promotion cannot be established.

The generated CLI enables provenance by default and exposes
`--provenance` / `--no-provenance`. It stages every requested output and
sidecar privately, rejects duplicate destinations, verifies cleanup, then
commits the requested set with rollback for caught commit failures. Sidecars
promote before their outputs, so an abrupt process crash may leave an orphan
sidecar but not a newly published output missing requested provenance. A
failure sidecar distinguishes execution failure from publication failure.

Generated CLI progress is operation-level. Exit code `0` means success, `2`
means setup/execution/publication failure, and `130` means cooperative
cancellation. A local path opened with the generated `load_image()` helper is
content-hashed before reading and verified again after materialization. The
saved batch runner adds a final source-byte recheck immediately before output
promotion. A generated Python caller remains responsible for the identity and
stability of arbitrary arrays or independently supplied source payloads.

Use `python generated_pipeline.py --help` for the exact source-binding and
output arguments emitted for that graph. Add `--progress` for operation updates
and supply compute overrides only when the run should deliberately differ from
the embedded workflow request.

## Save a batch configuration and evidence

Use **Batch → Save config** to write
`vipp_batch_config.json`. Keep it with its required workflow companion. After a
run, retain the latest manifest, run-id archive, and item sidecars. The optional
`vipp_batch_pipeline.py` is a version-locked launcher for that config and
workflow; it is not a substitute for the pair.

Version-6 configs store the complete configured compute request, reviewed
source-axis declarations, stable SourceItems, typed per-sample numeric
overrides, whole-batch **Use workflow / Run / Bypass** profiles, and exact-item
existing-file choices. Profiles
apply to detached effective workflows without mutating authored graph intent
and are recorded in manifests and hashes. Version-1 configs load as explicit
CPU; version-2 retains its saved compute request; version-3 also retains
reviewed source declarations; version 4 adds SourceItems and numeric overrides.
Version 5 adds node profiles; version 6 adds item file policies. Earlier
supported versions are written as version 6 only after review and save.
The runner uses its saved request by default and can overlay explicit
compute/fallback/per-node CLI choices. `--progress` prints both overall-item and
current-operation progress. One `Ctrl+C` requests normal cooperative
cancellation and allows manifest/sidecar cleanup; a second is an emergency
interrupt that can bypass finalization.

The standalone config remains the appropriate form for the supplied headless
batch runner and for workflows/configs managed as separate automation
artifacts. An attached config is convenient for reopening the interactive
setup as one file; it does not replace the finalized manifests and sidecars
that document an actual run.

Inspect partial, skipped, and failed records as well as successful outputs.
Sidecars help reconstruct an interrupted run, but outputs and provenance files
are not one multi-file transaction.

**Unreleased after 0.15.0a2:** [verified batch resume](../workflows/batch-processing.md#resume-an-interrupted-run)
uses a saved run manifest and its item sidecars, not merely existing filenames.
Newly generated batch runners accept `--resume MANIFEST` with optional
`--progress`; do not combine resume with config, workflow, or compute overrides. Keep
the original and continuation archives together. Older runs without output
verification evidence are not eligible.

For production collection processing, use the saved runner rather than the
generated program's simple `batch_process()` folder helper. The helper varies
one primary source, verifies that local source around materialization, and
privately stages and rollback-protects the requested output/sidecar set in one
destination directory. It does not provide multi-source pairing, collision
planning, a final source recheck immediately before publication, checkpoints,
a manifest, or durable replay/resume.

## Share an analysis package

At minimum include:

- workflow JSON;
- VIPP version and environment record;
- input identifiers/checksums or an accessible dataset citation;
- output tables/images and a description of how they were selected;
- validation/QC evidence;
- method notes for manual decisions, exclusions, source/grid assumptions, and
  batch pairing;
- for batch work: the attached or standalone config, manifest archives,
  sidecars, configured/effective compute requests, actual implementation and
  fallback records, and workflow/config/execution hashes reported by the
  finalized run.

For publication, follow the [reporting checklist](../scientific-practice/reporting.md).
