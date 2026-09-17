# Seeded segmentation

Use this reference to distinguish the numerical rules behind methods that grow
regions from labelled seeds. For wiring and inspection steps, see
[Grow regions from seeds](../how-to/grow-regions-from-seeds.md).

## CellProfiler Propagation

!!! info "Unreleased"
    **Grow Regions from Seeds — CellProfiler Propagation**
    (`cellprofiler_propagation`) is documented for nightly development and is
    not part of 0.15.0a5.

VIPP calls **Centrosome 1.3.4**, the library that implements CellProfiler's
Propagation method. It uses CPU execution and returns labels. It does not
require installation of the full CellProfiler application.

| Input or setting | Contract |
| --- | --- |
| Guidance image | Finite real intensities on exactly one YX plane, exactly representable in float64; values are not normalized. |
| Seed labels | Non-negative integer labels; zero is background. IDs must fit signed int32. |
| Foreground mask | Boolean YX array defining allowed growth. |
| Alignment | Identical shape and matching axes and physical grid across all inputs; no automatic resampling. |
| Distance regularization | Finite, non-negative; default 0.05. Larger values favour spatial distance relative to local appearance. |
| Output | YX int32 labels preserving the seed IDs and image grid. Inputs are not modified. |

T, C and Z axes are not accepted, including singleton axes. Select a single
plane explicitly upstream. There is no implicit slice-by-slice or 3D mode.
Numeric ranges that risk overflowing the reference cost calculation are
rejected; any necessary intensity rescaling must be explicit upstream.

Cancellation is checked before and after the Centrosome call. The reference
kernel itself cannot be interrupted mid-calculation.

The kernel compares neighbouring 3 × 3 intensity patches while competing
seeds grow along shortest accumulated paths over eight neighbouring pixels.
Spatial costs are in pixel-grid units; calibrated pixel sizes do not alter
the growth rule. Its tie behaviour is inherited from Centrosome.

Seeds outside the mask are retained in the output but do not seed growth.
Unseeded, unreachable regions stay background. The mask is therefore a growth
constraint, not an instruction to erase the original seed pixels.

Matching the **kernel** means using the same image values, seeds, mask and
regularization in Centrosome and VIPP. It does not establish that the whole
CellProfiler **IdentifySecondaryObjects** workflow has been reproduced.
Normalization, smoothing, thresholding, excluded seed objects, hole filling,
border filtering and cytoplasm construction must each be matched separately.
The unreleased [CellProfiler compartment profile](cellprofiler-compartments.md)
provides those surrounding stages for the statistics paper's specific settings.

See the [Centrosome API implementation](https://github.com/CellProfiler/centrosome/blob/fb6881b5c07221bbe80ff356beeb04d2273ecd78/centrosome/propagate.py)
and the original method, [Jones, Carpenter and Golland (2005)](https://doi.org/10.1007/11569541_54).
VIPP's [implementation contract and validation evidence](https://github.com/rensutheart/napari-vipp/blob/main/docs/seeded-segmentation.md)
record the tested scope separately from full paper-pipeline reproduction.

## Existing 3D watershed

**Marker-Controlled Watershed** floods an elevation image from labelled
markers inside a mask. It supports full ZYX processing through the spatial-mode
setting. Inversion changes the sign of the supplied elevation; it does not
turn watershed into CellProfiler Propagation.

VIPP uses scikit-image's default connectivity: four neighbours in 2D and six in
3D. This is a voxel-grid operation. The existing **Euclidean Distance
Transform**, **Auto Watershed From Mask** and **Expand Labels** likewise do not
pass physical spacing to their distance calculations. Retained scale metadata
does not imply that these calculations account for anisotropy.

See the [scikit-image watershed reference](https://scikit-image.org/docs/stable/api/skimage.segmentation.html#skimage.segmentation.watershed)
and the guide to [choosing 2D or 3D](../scientific-practice/choosing-dimensionality.md).

## Other methods

Random Walker is an established 2D/3D, image-guided segmentation algorithm in
scikit-image, with physical-spacing support. It is a different rule from
Propagation and watershed, and is not currently a VIPP node. The
[bounded acquired-data comparison](validation-status.md#unreleased-seeded-segmentation)
did not establish a quality benefit and exposed a runtime limit on one
mammalian crop. Adding it requires useful results plus runtime, memory and
solver-convergence checks on the intended volumes and seed counts.
