# Sample Data

VIPP ships synthetic microscopy-style samples that are available inside
`Image Source`:

```text
Image Source > Source = sample
```

This is the normal route when building or adapting a workflow. The sample menu
then lists every bundled sample without adding raw layers to napari first.

Napari's sample-data menu is still useful when you want to inspect raw sample
layers directly:

```text
File > Open Sample > VIPP synthetic microscopy samples
```

## Bundled Samples

| Sample | Axes | Purpose |
| --- | --- | --- |
| `VIPP synthetic volume` | `ZYX` | Basic grayscale z-stack with sphere/tube-like structures. |
| `VIPP synthetic multichannel volume` | `CZYX` | Three-channel fluorescence-like volume with blue/DAPI-like nuclei, green/FITC-like neurites, and red/TRITC-like puncta for channel splitting and segmentation. |
| `VIPP synthetic time-lapse multichannel` | `TCZYX` | Preferred starter sample with time, channel, z, y, and x axes. |
| `VIPP synthetic measurement summary` | `TYX` | Known object counts/areas per timepoint for summary validation. |
| `VIPP synthetic object morphology` | `YX` | Circle, ellipse, rectangle, and concave 2D objects for derived morphology. |
| `VIPP synthetic 3D mesh morphology` | `ZYX` | Anisotropic 3D objects for mesh volume, surface, convex hull, and sphericity checks. |
| `VIPP synthetic skeleton network` | `ZYX` | Sparse 3D skeleton-style network with known endpoints, junctions, spur, fragment, and isolated voxel. |
| `VIPP synthetic advanced skeleton network` | `TZYX` | Multi-timepoint skeleton stress test with loops, fragments, graph tables, and anisotropic scale. |
| `VIPP synthetic colocalization` | `CZYX` | Two-channel partial-overlap structures for colocalization, RACC-like output, and object association. |
| `VIPP synthetic deconvolution image` | `YX` | 2D blurred/noisy image for PSF-aware restoration review. |
| `VIPP synthetic measured PSF` | `YX` | 2D measured-PSF-like kernel for PSF preparation. |
| `VIPP synthetic 3D deconvolution volume` | `ZYX` | 3D blurred/noisy volume for volumetric restoration review. |
| `VIPP synthetic 3D measured PSF` | `ZYX` | 3D measured-PSF-like kernel for volumetric deconvolution. |

## Documentation Samples Versus Core Samples

Core samples should stay small, deterministic, testable, and broadly useful.

Documentation-only samples can be more tutorial-specific. A documentation
sample can become a core sample when it supports a stable workflow and has test
coverage.

## Suggested Future Samples

Useful documentation samples to add:

- simple nuclei segmentation sample with known labels;
- touching-object watershed sample with reference markers;
- puncta-in-cell sample for event localization;
- anisotropic z-stack sample showing why pixel size matters;
- batch folder with 3 to 5 matched inputs for batch documentation screenshots.
