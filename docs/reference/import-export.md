# Supported input and output

VIPP routes interactive sources, selected-output saves, `Save Image`, batch
outputs, and generated scripts through a shared headless I/O layer. Format
support does not imply lossless preservation of every source metadata field.

## Input routes

| Source | Behavior in 0.11.0a2 |
| --- | --- |
| Napari layer | Uses an existing viewer layer and the layer metadata exposed to VIPP. |
| Bundled sample | Loads one of 13 deterministic VIPP samples. |
| OME-TIFF | Reads image series and supported semantic axes, scale, channel, and selected acquisition fields from OME metadata. |
| ImageJ TIFF | Reads supported hyperstack axes, XY resolution, z spacing, frame interval, and unit fields where present. |
| Conventional TIFF | Reads TIFF series and infers basic axes where explicit semantic metadata is absent. |
| Local OME-Zarr 0.4/0.5 | Discovers supported image/label groups and reads analysis level 0; label groups are marked as labels. |
| NPY / NPZ | Reads one NPY array or a selected NPZ member; semantic microscopy metadata is not inherent. |
| PNG, JPEG, BMP, GIF, WebP, TGA, PNM | Reads ordinary raster images; animated rasters use a leading time axis. |
| Optional microscope readers | Uses an installed format-specific/BioIO route and normalizes fields the reader exposes. Coverage varies by format. |

Always inspect the resulting shape, axes, scale, unit, channel mapping, dtype,
and chosen series. Missing fields can be inferred; an inference is not the same
as acquisition metadata.

## Export choices

| Format | Use when | Check carefully |
| --- | --- | --- |
| OME-Zarr | Chunked multidimensional image data or an image with associated label outputs | Current export/pyramid scope and downstream reader compatibility |
| OME-TIFF | A portable processed image with supported OME metadata | dtype, axes, scale, and series after reopening |
| ImageJ TIFF | Fiji/ImageJ hyperstack interoperability is required | It cannot safely represent 32-bit integer label IDs |
| TIFF | Broad TIFF compatibility or 32-bit labels are needed | Semantic metadata may be limited compared with OME routes |
| NPY | Exact array/dtype exchange in Python | Axes, scale, units, and channel semantics must be stored separately |
| Ordinary raster | A 2D display image is required | Display-oriented only; not a quantitative stack/archive format |
| CSV / TSV | A table will be analyzed elsewhere | Units, identity columns, missing values, and delimiter handling |

## OME analysis dataset

**Export OME dataset…** writes one reference image and graph label outputs into
one local `.ome.zarr` store:

```text
/
  s0
  labels/
    label_output_name/
      s0
```

Use it when label outputs should remain associated with a reference image. For
a standalone label image, use TIFF/OME-TIFF or provide an image-linked OME-Zarr
dataset; the command is not a general project archiver.

## Current limitations

- Analysis reads use OME-Zarr level 0; preview-level/pyramid selection is not
  exposed.
- Plate/well/field browsing and remote URI input are planned, not current.
- Lazy OME-Zarr arrays may materialize when an eager operation executes.
- Only supported metadata fields propagate through compatible operations and
  writers; complete source metadata fidelity is not claimed.
- Reopen representative outputs in the intended downstream software before a
  large run.

For what workflow and Python export preserve, see the
[workflow and export contract](workflow-contract.md).
