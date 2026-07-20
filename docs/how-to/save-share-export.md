# Save, share, and export

VIPP offers several outputs that solve different problems. They are not
interchangeable.

| Artifact | Use it for | Does not contain |
| --- | --- | --- |
| Workflow JSON (schema 3) | Reopen/edit the validated scientific graph in VIPP 0.12; optionally restore an attached versioned Batch workspace configuration | Cached pixels/tables, Python environment, source bytes |
| Exported Python | Execute immutable validated workflow JSON through VIPP's shared headless executor | Interactive UI, caches, a portable runtime environment |
| Saved image/table | Analysis result or QC artifact | The graph and parameter rationale |
| OME analysis dataset | Reference image plus associated graph label outputs | A complete project/archive or arbitrary standalone table provenance |
| Batch config | Recreate source bindings, output declarations, naming, collision policy, and workflow association | Input bytes, environment, finalized run outcome |
| Batch manifest/archive/sidecars | Audit planned inputs/outputs, identities, hashes, versions, errors, and per-item/output status | One atomic transaction or proof of biological validity |

## Save a workflow

Choose **Save workflow…**. Use `.json` and include a meaningful analysis name.
If a Batch workspace is active, VIPP asks what to save:

- **Yes** attaches the current versioned batch configuration to the same
  workflow JSON. This includes source bindings, local input/output paths,
  patterns, formats, and run policies. It does not include input pixels,
  computed arrays, or output files.
- **No** writes the ordinary graph-only workflow. Use **Save config…** in
  Batch workspace if a separate configuration is required.
- **Cancel** writes nothing.

Loading a workflow with a valid attachment restores and opens Batch workspace
with those settings. It does not scan the collection, build a preview, load a
representative, or run the graph for the batch setup. **Preview batch** remains
optional, and **Run batch** performs a fresh preflight. If the attachment is
unsupported or does not match the workflow, VIPP loads the scientific workflow
but reports that its Batch workspace could not be restored rather than silently
applying the settings.

Before sharing:

1. Reopen the file in the same VIPP release.
2. Confirm every `Image Source` intentionally references a sample, layer, file,
   or store.
3. Review graph notes, paths, source names, and metadata for sensitive text.
4. Recalculate manual nodes and compare expected outputs.

Workflow compatibility can change between alpha releases. Keep an unmodified
copy of the original and record the version that created it.

0.12.0a2 still writes schema 3 and rejects versions 1 and 2. Valid 0.12.0a1
schema-3 workflows load structurally, but cached pixels and tables are not
serialized in the workflow. Recalculate and revalidate after upgrading.
For a 0.12.0a1 workflow, follow the
[0.12.0a1 to 0.12.0a2 procedure](../reference/versioning.md#move-from-0120a1-to-0120a2).
Recreate schema-1/2 graphs deliberately; do not edit only the JSON version. See
the separate [schema-1/2 rebuild procedure](../reference/versioning.md#upgrade-to-0120a1).

## Save a selected output

Select the desired output and choose **Save selected output…**. The available
format depends on the data type and dimensionality. For tables use CSV or TSV;
for scientific images prefer a format that can represent the axes, dtype, and
calibration you need.

Read the [input/output reference](../reference/import-export.md) before using a
display-oriented raster format or ImageJ TIFF for label IDs.

## Export Python

Choose **Export Python…** when a graph needs a reviewable headless program. The
script embeds validated immutable workflow JSON, constructs a fresh pipeline
per call, and uses the same headless executor as VIPP. It carries supported
`ImageState`, accepts explicit multi-source bindings, and fails on missing,
duplicate, or unknown sources.

The script records the exact VIPP version that created it and refuses another
runtime. Regenerate and revalidate it after every upgrade, including alpha
updates. UI caches, pinned layers,
and graph layout are presentation state and are intentionally absent.

## Save a batch configuration and evidence

Use **Batch workspace... → Save config...** to write
`vipp_batch_config.json`. Keep it with its required workflow companion. After a
run, retain the latest manifest, run-id archive, and item sidecars. The optional
`vipp_batch_pipeline.py` is only a thin launcher for that config; it is not a
substitute for the workflow/config pair.

The standalone config remains the appropriate form for the supplied headless
batch runner and for workflows/configs managed as separate automation
artifacts. An attached config is convenient for reopening the interactive
setup as one file; it does not replace the finalized manifests and sidecars
that document an actual run.

Inspect partial, skipped, and failed records as well as successful outputs.
Sidecars help reconstruct an interrupted run, but outputs and provenance files
are not one multi-file transaction.

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
  sidecars, and the workflow/config hashes reported by the finalized run.

For publication, follow the [reporting checklist](../scientific-practice/reporting.md).
