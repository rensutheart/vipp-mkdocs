# Node Index

This page lists all **125 operation specifications** registered by
`NODE_LIBRARY` in nightly, including **Find Label Boundaries**, unreleased after
0.15.0a2. The palette exposes **123**: the two legacy scatter raster operations
remain loadable but are hidden from new-node selection. The 0.15.0a2 release has
124 specifications and 122 palette nodes. This includes **Convex Hull** and
eight nodes in **3D Meshes**.

**Save Image** accepts images or 3D meshes and passes the connected
image/mesh type downstream. Its format menu and **Batch Output**'s menu follow
the connected input; see [mesh saving](../workflows/mask-to-mesh.md#save-the-mesh).

!!! info "Scope of this reference"
    Titles and families follow the source registry; post-0.15.0a2 additions are
    marked unreleased.
    Input and output summaries describe the ordinary/default ports; `Split Channels`,
    `Split Axis`, `Born-Wolf PSF`, and other multi-output nodes can resolve ports
    from runtime data. Parameter widgets, defaults, and bounds in the installed
    release remain the source of truth until a generated parameter reference is
    published.

Since 0.14.0a1, manual/cached nodes and nodes selected for isolated tuning use
the same graph-wide execution language.
Bright amber identifies the node that needs action; dark amber identifies
downstream nodes that are stale but waiting for that action. **Tune node in
isolation** recalculates only the selected node until
the session is applied or cancelled. This changes execution and presentation,
not the operation's scientific definition.

Implemented nodes can also show an actual-run **CPU**, **GPU · CuPy**, or amber
**CPU fallback** badge. The badge is execution provenance for
the accepted result, not part of the operation's scientific definition. A GPU
choice appears for an operation with a declared provider; it is not filtered by
the current dtype, parameters, shape, memory, dependencies, or environment.
Call-specific admission happens during planning and can select CPU, visibly
fall back, or fail. See the
[0.15.0a2 CPU/GPU operation matrix](../how-to/choose-compute.md#gpu-regions-in-0150a2)
for the accelerated node families and their current public regions.

| Family | Nodes |
| --- | ---: |
| Image Data | 25 |
| Filtering | 18 |
| Segmentation | 18 |
| Morphology | 15 |
| 3D Meshes | 8 |
| Measurements | 13 |
| Colocalization & Spatial Analysis | 12 |
| Label Operations | 8 |
| Intensity & Contrast | 5 |
| Projection | 3 |
| **Total** | **125** |

## Image Data

### Source & Output

| Node | Input | Output | Use |
| --- | --- | --- | --- |
| `Image Source` | none | image | Load a napari layer, file, store, or bundled sample. |
| `Save Image` | array or mesh | same as input | Save an image or mesh during interactive recompute. |
| `Batch Output` | any | same as input | Mark an output for folder batch execution. |

### Axes & Regions

| Node | Input | Output | Use |
| --- | --- | --- | --- |
| `Crop Stack` | image, mask, or labels | same as input | Crop explicit Y/X and optional Z edges while preserving T/C, graph-port type, calibration, and origin; an eligible sole direct local OME-Zarr source can read only the retained window. |
| `Select Axis Slice` | array | any | Keep or select an index/range along an axis. |
| `Split Axis` | array | dynamic outputs | Split time, z, or other non-channel axes. |
| `Reorder Axes` | array | same as input | Transpose pixels and their existing axis records into a reviewed order; does not rename axes. |
| `Set Pixel Size / Units` | array | same as input | Repair or define physical calibration. |
| `Set Microscope Metadata` | array | same as input | Record missing channel emission wavelengths, objective numerical aperture, or immersion refractive index without changing pixels. |
| `Rescale Axes` | array | same as input | Resample X/Y/Z and update physical scale. |

### Channels & Composites

| Node | Input | Output | Use |
| --- | --- | --- | --- |
| `Extract Channel` | array | image | Select one channel from a multichannel image. |
| `Combine Channels` | array inputs | image | Stack inputs into a multichannel image. |
| `Split Channels` | array | dynamic outputs | Emit one output per channel. |
| `Composite → RGB` | array | image | Render multichannel data as RGB. |
| `Assign Channel Colors` | array | same as input | Change carried channel display colors. |

`Composite → RGB` separates **Channel axis mode** and **RGB mapping mode**.
Each can be Auto, with its resolved choice shown read-only, or Manual. Manual
axis mode permits any valid deliberate axis choice. Manual mapping provides a
dynamic selector for every source channel: Unassigned, Red, Green, Blue,
Magenta, Cyan, or Yellow. Unassigned channels contribute nothing; all assigned
channels, including stacks wider than RGB/RGBA, mix additively. Changing the
mapping invalidates the composite and its descendants only. Every calculated
manual result upstream remains cached in every cache mode; unchanged automatic
intermediates remain eligible for normal Smart/Low-memory pruning. Intensity
mapping is a separate native-preserving versus explicitly lossy percentile
choice.

### Math & Logic

| Node | Input | Output | Use |
| --- | --- | --- | --- |
| `Calculate New Image` | arrays | image | Weighted multi-input image calculation. |
| `Add` | arrays | image | Add images. |
| `Subtract` | arrays | image | Subtract images. |
| `Ratio` | arrays | image | Ratio image with epsilon guard. |
| `Mask Image` | image plus mask/labels | image | Apply mask to image, broadcasting over compatible axes. |
| `Logical AND` | arrays | mask | Combine masks. |
| `Logical OR` | arrays | mask | Combine masks. |
| `Logical XOR` | arrays | mask | Exclusive mask combination. |
| `Invert` | any | any | Invert masks or intensity-like inputs. |

### Utilities

| Node | Input | Output | Use |
| --- | --- | --- | --- |
| `Convert Dtype` | array | any | Convert array dtype. |

## Intensity & Contrast

| Node | Output | Use |
| --- | --- | --- |
| `Linear Scale + Offset` | image | Apply scale and offset. |
| `Gamma Correction` | image | Nonlinear brightness/contrast remapping. |
| `Rescale Intensity` | image | Contrast stretch between input/output ranges. |
| `Normalize` | image | Normalize intensity values. |
| `Clamp Intensity` | image | Clamp values to the chosen lower and upper bounds. |

`Rescale Intensity` offers exact full-input percentiles or saved explicit input
values. `Clamp Intensity` offers an unchanged full-data-range mode or saved explicit clamp
values. Integer percentiles and clipping preserve native int64/uint64 levels;
unrepresentable fractional bounds or intervals too wide for faithful ratio
arithmetic report an error rather than being silently rounded. Auto Contrast
for `Linear Scale + Offset` writes calculated parameters
and is not merely a display adjustment. See
[Tune without fooling yourself](../scientific-practice/parameter-tuning.md).

## Filtering

### Background Correction

| Node | Output | Use |
| --- | --- | --- |
| `Rolling-Ball Background` | image | Estimate background. |
| `Subtract Background` | image | Remove smooth background. |

### Smoothing And Denoising

| Node | Output | Use |
| --- | --- | --- |
| `Average Blur` | image | Simple local averaging. |
| `Gaussian Blur` | image | Gaussian smoothing. |
| `Gaussian Blur 3D` | image | Volumetric Gaussian smoothing. |
| `Median Filter` | image | Remove salt-and-pepper noise. |
| `Sigma Filter` | image | Edge-preserving local smoothing using a sigma-selected circular neighborhood. |
| `Bilateral Filtering` | image | Edge-preserving smoothing. |
| `Non-Local Means` | image | Denoising for suitable data. |

### Edge And Detail

| Node | Output | Use |
| --- | --- | --- |
| `Difference of Gaussians` | image | Enhance features by scale difference. |
| `Unsharp Mask` | image | Sharpen details. |
| `Sobel Edges` | image | Edge magnitude image. |
| `Canny Edges` | mask | Edge mask. |
| `Laplace Filter` | image | Laplacian edge/detail response. |

### Restoration And PSF

These nodes have been public since 0.14.0a1 and remain available in 0.15.0a2.
They have synthetic examples and automated coverage, but broad real-image
restoration validation remains an evidence gap;
see [validation status](validation-status.md).

| Node | Input | Output | Execution | Use |
| --- | --- | --- | --- | --- |
| `Born-Wolf PSF` | image/reference metadata | image | automatic | Generate a PSF from metadata or parameter overrides. |
| `Prepare / Validate PSF` | image | image | automatic | Center, clip, normalize, and validate a PSF. |
| `Richardson-Lucy Deconvolution` | image plus PSF | image | manual | Baseline PSF-aware deconvolution. |
| `Richardson-Lucy TV Deconvolution` | image plus PSF | image | manual | TV-regularized Richardson-Lucy restoration. |

## Projection

| Node | Output | Use |
| --- | --- | --- |
| `Maximum Projection` | image | Quick maximum intensity projection. |
| `Project Image` | image | Axis-aware projection with selectable reducer. |
| `Orthogonal Projection` | image | Orthogonal view respecting physical scale. |

## Segmentation

### Global Thresholds

| Node | Output |
| --- | --- |
| `Otsu Threshold` | mask |
| `Triangle Threshold` | mask |
| `Li Threshold` | mask |
| `Yen Threshold` | mask |
| `Isodata Threshold` | mask |
| `Minimum Threshold` | mask |
| `Binary Threshold` | mask |
| `Hysteresis Threshold` | mask |
| `ImageJ Default Threshold (8-bit)` | mask |

Otsu, Triangle, Yen, Isodata, and Minimum count every finite input value.
Integers use exact native levels for observed spans up to 65,536; floats use the
saved 2–65,536 bin setting (default 256). Li operates on raw finite values.
Minimum also saves its maximum smoothing iterations and fails explicitly when
it cannot identify a valid two-peak histogram. See
[Segmentation and label cleanup](../workflows/segmentation-label-cleanup.md).

### Local Thresholds

| Node | Output |
| --- | --- |
| `Adaptive Mean Threshold` | mask |
| `Adaptive Gaussian Threshold` | mask |
| `Sauvola Threshold` | mask |
| `Niblack Threshold` | mask |

### Object Separation

| Node | Input | Output | Use |
| --- | --- | --- | --- |
| `Auto Watershed From Mask` | mask/array | labels | One-node marker watershed helper. |
| `Euclidean Distance Transform` | array | image | Distance map for watershed. |
| `H-Maxima Markers` | array | labels | Marker generation. |
| `Marker-Controlled Watershed` | image/distance plus markers plus mask | labels | Split touching objects. |
| `Expand Labels` | labels | labels | Grow labels without overlap. |

## Morphology

| Node | Input | Output | Use |
| --- | --- | --- | --- |
| `Dilation` | array | mask | Expand foreground. |
| `Erosion` | array | mask | Shrink foreground. |
| `Convex Hull` | Boolean mask | mask | Fill one convex hull around all foreground per 2D slice or 3D volume. See [scope and caveats](../workflows/segmentation-label-cleanup.md#convex-hull). |
| `Opening` | array | mask | Remove small foreground structures. |
| `Closing` | array | mask | Close small gaps. |
| `Top Hat` | array | mask | Binary top-hat operation. |
| `Black Hat` | array | mask | Binary black-hat operation. |
| `Morphological Gradient` | array | mask | Boundary-like morphology response. |
| `Fill Holes` | mask | mask | Fill enclosed holes by area/volume. |
| `Remove Small Objects` | mask or labels | same type | Remove connected objects below size threshold. |
| `Remove Outliers (Binary)` | mask | mask | Remove foreground specks or fill background notches with Fiji-compatible circular YX neighborhoods. |

### Skeleton / Network QC

| Node | Input | Output |
| --- | --- | --- |
| `Skeletonize` | mask | mask |
| `Skeleton Keypoints` | mask | endpoints, junctions, isolated masks |
| `Skeleton Graph Overlay` | mask | RGB image |
| `Prune Skeleton Branches` | mask | mask |

<span id="3d-meshes-nightly"></span>

## 3D Meshes

All eight nodes are CPU operations, manual/cached by default. Mesh outputs are
inspected as napari surfaces, not graph thumbnails. See the
[mesh-object tutorial](../workflows/mask-to-mesh.md) for grouping, calibration,
refinement caveats and 3MF/OBJ export.

| Group | Node | Input → output | Use |
| --- | --- | --- | --- |
| Create surfaces | `Mask to 3D Mesh` | Boolean 3D mask → mesh | One foreground object or separate face-connected objects. |
| Create surfaces | `Labels to 3D Mesh` | 3D labels → mesh | One mesh object per positive label, retaining IDs. |
| Objects & colours | `Colour Mesh Objects` | mesh → mesh | Categorical IDs or current-geometry measurement colours. |
| Objects & colours | `Combine Meshes` | 2–16 meshes → mesh | Collect objects and colours in one calibrated frame; no union or registration. |
| Objects & colours | `Split Mesh Objects` | mesh → mesh | Separate shared-edge components; cavity walls split too. |
| Objects & colours | `Filter Mesh Objects` | mesh → mesh | Keep objects inside/outside a measurement or ID range. |
| Refine geometry | `Smooth Mesh` | mesh → mesh | Explicit Taubin-style surface smoothing. |
| Refine geometry | `Simplify Mesh` | mesh → mesh | Approximate quadric-error triangle reduction. |

## Label Operations

| Node | Input | Output | Use |
| --- | --- | --- | --- |
| `Label Connected Components` | mask | labels | Convert mask to object IDs. |
| `Clear Border Objects` | mask or labels | same type | Remove objects touching image boundary. |
| `Filter Labels By Volume` | labels | labels | Keep/remove labels by pixel/voxel count. |
| `Filter Labels By Property` | labels plus table | labels | Filter labels using table columns. |
| `Relabel Sequential` | labels | labels | Compact labels after filtering. |
| `Find Label Boundaries` (unreleased after 0.15.0a2) | labels or Boolean mask | Boolean mask | Same-grid boundary QC with inside/outside/both placement; no retained IDs or mesh. |
| `Label Skeleton Components` | mask | labels | Label connected skeleton components. |
| `Label Skeleton Branches` | mask | labels | Label skeleton branch paths. |

See [Inspect label boundaries](../workflows/segmentation-label-cleanup.md#inspect-label-boundaries)
for placement, connectivity, spatial scope and crop-border caveats. Find Label
Boundaries runs on CPU and preserves the input calibration.

## Measurements

| Node | Input | Output | Execution | Use |
| --- | --- | --- | --- | --- |
| `Intensity Histogram` | numeric image | table | manual | Reproducible full-data intensity distribution with saved bin definitions. |
| `Measure Objects` | labels | table | manual | Object morphology. |
| `Measure Objects + Intensity` | labels plus intensity image | table | manual | Object morphology plus intensity statistics. |
| `Measure 3D Mesh Morphology` | labels, Boolean mask or mesh | table | manual | Surface morphology; existing meshes are measured per object without remeshing. |

### Skeleton / Network QC

| Node | Output | Execution |
| --- | --- | --- |
| `Analyze Skeleton` | table | manual |
| `Measure Skeleton Branches` | table | manual |
| `Summarize Skeleton Branches` | table | automatic |
| `Skeleton Graph Tables` | graph-node table and graph-edge table | manual |
| `Measure Overall Skeleton Network` | table | manual |

### Tables

| Node | Input | Output | Use |
| --- | --- | --- | --- |
| `Merge Tables` | tables | table | Join measurement branches. |
| `Add Metadata Columns` | table | table | Add treatment, replicate, condition, batch, or other fields. |
| `Select Table Columns` | table | table | Keep and reorder columns. |
| `Summarize Measurements` | table | table | Group rows and calculate summary statistics. |

## Colocalization And Spatial Analysis

| Node | Input | Output | Execution |
| --- | --- | --- | --- |
| `Colocalization Metrics` | channel 1 plus channel 2 | table | manual |
| `Masked Colocalization Metrics` | channel 1 plus channel 2 plus ROI | table | manual |
| `Colocalized Voxels` | channel 1 plus channel 2 | image | automatic |
| `Masked Colocalized Voxels` | channel 1 plus channel 2 plus ROI | image | automatic |
| `RACC Index` | channel 1 plus channel 2 | image | manual |
| `Masked RACC Index` | channel 1 plus channel 2 plus ROI | image | manual |
| `Colocalization Scatter Plot` (legacy, hidden) | channel 1 plus channel 2 | image | manual |
| `Masked Colocalization Scatter Plot` (legacy, hidden) | channel 1 plus channel 2 plus ROI | image | manual |
| `Object Colocalization Metrics` | labels plus two channels | table | manual |
| `Label Overlap Association` | reference plus target labels | table | manual |
| `Nearest Object Distance` | reference plus target labels | table | manual |
| `Event Localization` | events plus regions | table | manual |
