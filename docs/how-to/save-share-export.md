# Save, share, and export

VIPP offers several outputs that solve different problems. They are not
interchangeable.

| Artifact | Use it for | Does not contain |
| --- | --- | --- |
| Workflow JSON | Reopen/edit the graph in VIPP | Cached pixels, cached tables, Python environment, every batch binding |
| Exported Python | Headless calls to supported operations and I/O | Interactive UI, caches, full image-state propagation, every dynamic graph behavior |
| Saved image/table | Analysis result or QC artifact | The graph and parameter rationale |
| OME analysis dataset | Reference image plus associated graph label outputs | A complete project/archive or arbitrary standalone table provenance |
| Batch workflow/script artifacts | Record the graph and generated runner used for a collection | A full per-item manifest in the current release |

## Save a workflow

Choose **Save workflow…**. Use `.json` and include a meaningful analysis name.
Before sharing:

1. Reopen the file in the same VIPP release.
2. Confirm every `Image Source` intentionally references a sample, layer, file,
   or store.
3. Review graph notes, paths, source names, and metadata for sensitive text.
4. Recalculate manual nodes and compare expected outputs.

Workflow compatibility can change between alpha releases. Keep an unmodified
copy of the original and record the version that created it.

## Save a selected output

Select the desired output and choose **Save selected output…**. The available
format depends on the data type and dimensionality. For tables use CSV or TSV;
for scientific images prefer a format that can represent the axes, dtype, and
calibration you need.

Read the [input/output reference](../reference/import-export.md) before using a
display-oriented raster format or ImageJ TIFF for label IDs.

## Export Python

Choose **Export Python…** when a graph needs a readable headless starting point.
Run the script in an environment containing a compatible napari-vipp release.
Review the generated source, input bindings, output paths, and unsupported
assumptions before automation.

Python export expresses direct operation calls; it is not a byte-for-byte
serialization of interactive execution. In particular, UI caches, pinned
layers, and complete runtime metadata behavior are not reproduced.

## Share an analysis package

At minimum include:

- workflow JSON;
- VIPP version and environment record;
- input identifiers/checksums or an accessible dataset citation;
- output tables/images and a description of how they were selected;
- validation/QC evidence;
- method notes for manual decisions, exclusions, and batch pairing.

For publication, follow the [reporting checklist](../scientific-practice/reporting.md).
