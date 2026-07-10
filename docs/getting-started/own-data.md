# Use your own images

An `Image Source` can read a napari layer, a local file or store, or a bundled
sample. Changing the source is easy; establishing that the workflow remains
valid is the important part.

## Choose a source route

| Route | Best for | Important limitation |
| --- | --- | --- |
| `napari layer` | Images already opened, cropped, or registered in napari | The workflow depends on a layer being present and correctly selected. |
| `file path` | A repeatable local file input | Moving or renaming the file breaks the local path. |
| `sample` | Tutorials, regression checks, and demonstrations | Synthetic data does not establish performance on your assay. |
| Local OME-Zarr store | Chunked multidimensional data | Many operations are eager and can still materialize large arrays. |

Select `Image Source`, set **Source**, and then use the control specific to that
route. The napari layer chooser is only shown for `napari layer`.

## Check metadata before processing

Confirm at minimum:

- array shape and semantic axes (`T`, `C`, `Z`, `Y`, `X`);
- channel order and names;
- pixel size, z-step, and unit;
- whether the data is intensity, RGB, a binary mask, or labels;
- whether the reader selected the intended image/series.

Use `Reorder Axes` only when you understand the actual stored order. Use
`Set Pixel Size / Units` to repair missing or known-wrong calibration, and
record where the corrected values came from.

## Transfer a workflow deliberately

Do not judge transfer only from the final object count. On representative
images from the new acquisition family:

1. Inspect raw channel quality and background.
2. Inspect every threshold or segmentation boundary.
3. Check objects at image edges and across z.
4. Compare against independent reference annotations or agreed QC examples.
5. Retune only on a defined tuning subset.
6. Evaluate the frozen workflow on held-out images.

Changes in objective, exposure, stain, detector, bit depth, sampling, tissue,
or preprocessing can invalidate parameters that worked previously.

## Protect sensitive data

Workflow JSON may contain local paths, source names, graph notes, or metadata
values. Review it before sharing publicly. Do not use patient identifiers,
restricted paths, or unpublished biological conclusions in screenshots,
examples, notes, or metadata columns.

Continue to [segmentation](../workflows/segmentation-label-cleanup.md),
[measurements](../workflows/object-measurements-tables.md), or the
[scientific-practice checklist](../scientific-practice/index.md).
