# Batch Processing

Batch processing runs a tuned graph over a collection of local input files.

## Basic Pattern

1. Build and tune the graph interactively.
2. Add `Batch Output` nodes to mark the outputs you want saved.
3. Open `Run batch...`.
4. Bind each collection `Image Source` to a folder and glob pattern.
5. Preview the batch.
6. Run and inspect the output folder.

## Use Batch Output Nodes

`Batch Output` is a pass-through node during interactive graph execution. During
batch execution it marks a specific output for saving.

Use it for:

- final processed image;
- segmentation mask;
- labels;
- RGB QC output;
- measurement table;
- summary table.

## Multi-Source Batch Runs

If several `Image Source` nodes are bound to folders, VIPP sorts each source's
matched files and pairs them by position. All bound sources must have the same
number of files.

## Naming

Default explicit-output naming:

```text
{source_stem}__{tag}
```

Useful template fields include:

- `{batch_id}`
- `{batch_index}`
- `{source_name}`
- `{source_stem}`
- `{primary_source_stem}`
- `{tag}`
- `{node_id}`
- `{node_title}`

## Reproducibility Artifacts

The dialog can write:

- `vipp_batch_workflow.json`
- `vipp_batch_pipeline.py`

Future batch work should add saved batch configuration, output manifests, and
per-item provenance.

## What To Check Before Running

- Does `Preview batch` show the correct file pairing?
- Are all intended outputs marked with `Batch Output`?
- Are tags meaningful?
- Is overwrite behavior correct?
- Are table outputs included?
- Is memory mode appropriate for the image size?

