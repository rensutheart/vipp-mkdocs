# Data Types

VIPP uses typed graph data to communicate and check intended scientific
meaning. Port types prevent many category errors; they cannot determine whether
an image, mask, or table is appropriate for your biological question.

| Type | Meaning | Typical napari display |
| --- | --- | --- |
| `image` | Intensity image, RGB image, PSF, or restored image. | Image layer |
| `mask` | Binary foreground/background image. | Labels-style overlay |
| `labels` | Integer object IDs, with zero as background. | Labels layer |
| `table` | Measurement or summary rows. | Inspector table preview and CSV/TSV output |
| `plot` (new in 0.16.0a1) | A measurement-plot recipe with prepared values and inclusion counts, not a spatial image. | Inspector figure and editable plot window; PNG/TIFF/SVG/PDF export |
| `transform` (unreleased) | Reusable motion from moving coordinates to a reference, including a series with one transform per time point. | Metadata and JSON export; connect to Apply Transform to view aligned images. |
| `array` | Generic array accepted by many processing nodes. | Depends on output node |
| `mask_or_labels` | Input may be either a binary mask or label image. | Depends on connected input |
| `any` | Pass-through or generic output where type is resolved from context. | Depends on connected input |

## Images

Images carry array data plus metadata such as axes, scale, unit, channel names,
source identity, and operation history where available.

`Convert Dtype` is an explicit scientific operation. Its scaling choice can
preserve representable values or intentionally remap the range, which may
change thresholds, rounding, writers, memory, and downstream interpretation.
VIPP's optimizer never inserts a cast to make a GPU candidate eligible. Where
`float32` is justified, an authored conversion can unlock much larger Gaussian
or deconvolution gains; record and validate that conversion like any other node.

## Masks

Masks represent inside/outside decisions. They are usually produced by
thresholding, morphology, or colocalized-voxel nodes.

Use masks before label creation when you are still deciding what is foreground.

VIPP stores binary masks as Boolean arrays where possible. If a Boolean mask is
connected to a global automatic-threshold node, VIPP recognizes that it is
already segmented and preserves its `True`/`False` decisions. It does not
reinterpret the two levels through Otsu, Triangle, Li, Yen, Isodata, or Minimum
thresholding.

For floating-point intensity images, non-finite pixels (`NaN`, positive
infinity, or negative infinity) are excluded from global automatic-threshold
estimation and become `False` in the resulting mask. Inspect why those values
exist; treating them as background is a defined calculation rule, not evidence
that the source data are valid.

## Labels

Labels represent object identity. Label `0` is background; positive integers are
objects.

Use labels when you want object measurements, label cleanup, object
colocalization, or event assignment.

## Tables

Tables are first-class outputs, not fake images. They appear in the inspector
and can be saved as CSV or TSV.

Common table nodes include:

- `Measure Objects`
- `Measure Objects + Intensity`
- `Measure 3D Mesh Morphology`
- skeleton and network measurements
- colocalization metrics
- `Merge Tables`
- `Add Metadata Columns`
- `Summarize Measurements`

## Manual Calculation Nodes

**Plot Results** accepts a table directly or from **Table Source**.
Its figure does not acquire image axes or voxel calibration: the axes use the
selected measurement columns' units. See
[Plot measurement results](../how-to/plot-measurement-results.md).

Expensive measurement, graph-analysis, RACC, and deconvolution nodes can be
manual/cached. Select the node and click `Calculate` or use toolbar
`Calculate all`.
