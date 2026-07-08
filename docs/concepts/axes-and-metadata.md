# Axes And Metadata

VIPP carries an image state alongside node outputs. This state records array
shape, axes, units, scale, source identity, channel metadata, and operation
history where available.

## Common Axes

| Axis | Meaning |
| --- | --- |
| `T` | time |
| `C` | channel |
| `Z` | depth |
| `Y` | image row |
| `X` | image column |

Examples:

| Shape label | Meaning |
| --- | --- |
| `YX` | 2D image |
| `ZYX` | 3D z-stack |
| `CZYX` | multichannel z-stack |
| `TCZYX` | time-lapse multichannel z-stack |

## Why Axes Matter

Many operations depend on whether data is processed per slice or as a volume.

Examples:

- `Gaussian Blur` and local threshold nodes may operate per `YX` plane.
- `Gaussian Blur 3D`, connected components, hole filling, and skeleton analysis
  can use true `ZYX` spatial processing.
- `Split Channels` should be used for a semantic channel axis.
- `Split Axis` should be used for time, Z, or non-channel axes.

## Physical Scale

Scale-aware measurements use pixel size and units when available.

Use `Set Pixel Size / Units` when input calibration is missing or wrong.

Physical scale affects:

- area and volume;
- centroid and bounding-box coordinates;
- skeleton length;
- branch length;
- 3D mesh surface and volume;
- anisotropic projections and rescaling.

## Metadata Is Not Magic

When files lack reliable metadata, VIPP falls back to inferred axes and should
make that fallback visible. Always check metadata before reporting quantitative
physical units.

