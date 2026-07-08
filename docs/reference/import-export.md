# Import And Export

VIPP uses one headless I/O layer for interactive sources, quick saves, `Save
Image`, batch outputs, and exported Python scripts.

## Import Sources

| Source | Current behavior |
| --- | --- |
| Napari layer | Uses an existing viewer layer as graph input. |
| Bundled sample | Uses VIPP synthetic microscopy samples. |
| OME-TIFF | Reads image series, semantic axes, physical scale, channel names, and selected acquisition metadata. |
| ImageJ TIFF | Reads hyperstack axes, z spacing, frame interval, unit, and XY resolution where present. |
| TIFF | Reads independent TIFF series and basic axes. |
| OME-Zarr 0.4/0.5 | Discovers image and label groups, reads multiscale level 0 for analysis, and marks label groups as labels. |
| NPY/NPZ | Reads one NPY array or selected NPZ member. |
| PNG/JPEG/BMP/GIF/WebP/TGA/PNM | Reads ordinary raster images. Animated rasters use a leading time axis. |

## Export Choices

| Format | Use when |
| --- | --- |
| OME-Zarr | Large or chunked image data, or image plus label analysis packages. |
| OME-TIFF | Portable processed image with OME-XML metadata. |
| ImageJ TIFF | Direct Fiji/ImageJ hyperstack compatibility matters most. |
| TIFF | Broad TIFF compatibility or preservation of 32-bit label IDs. |
| NPY | Exact array exchange without scientific image metadata. |
| PNG/JPEG/BMP/GIF/WebP/TGA/PNM | 2D display image exports. |

## Important Warnings

- Use OME-TIFF, ImageJ TIFF, TIFF, OME-Zarr, or NPY for stacks.
- Use conventional TIFF, OME-TIFF, or OME-Zarr for 32-bit labels.
- ImageJ TIFF cannot safely represent 32-bit integer label IDs.
- Ordinary raster exports are display-oriented and only available for 2D
  intensity or 2D RGB/RGBA outputs.

## OME Analysis Dataset Export

`Export OME dataset...` writes one reference image plus graph label outputs into
one `.ome.zarr` store:

```text
/
  s0
  labels/
    label_output_name/
      s0
```

Use this when label outputs should remain associated with a reference image.

## Current Limitations

- OME-Zarr pyramids and preview-level selection are not exposed.
- Plate/well/field browsing is still planned.
- Remote URI support is still planned.
- Lazy OME-Zarr reads may still materialize when eager operations run.

