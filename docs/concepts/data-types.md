# Data Types

VIPP uses typed graph data so the workflow can preserve scientific meaning.

| Type | Meaning | Typical napari display |
| --- | --- | --- |
| `image` | Intensity image, RGB image, PSF, or restored image. | Image layer |
| `mask` | Binary foreground/background image. | Labels-style overlay |
| `labels` | Integer object IDs, with zero as background. | Labels layer |
| `table` | Measurement or summary rows. | Inspector table preview and CSV/TSV output |
| `array` | Generic array accepted by many processing nodes. | Depends on output node |
| `mask_or_labels` | Input may be either a binary mask or label image. | Depends on connected input |
| `any` | Pass-through or generic output where type is resolved from context. | Depends on connected input |

## Images

Images carry array data plus metadata such as axes, scale, unit, channel names,
source identity, and operation history where available.

## Masks

Masks represent inside/outside decisions. They are usually produced by
thresholding, morphology, or colocalized-voxel nodes.

Use masks before label creation when you are still deciding what is foreground.

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

Expensive table-producing nodes are manual/cached. Select the node and click
`Calculate` or use toolbar `Calculate all`.

