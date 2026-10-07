# Fiji/ImageJ compatibility

Use this reference when translating a Fiji/ImageJ macro or comparing its outputs
with VIPP. Compatibility applies to a specific operation, input domain and
reference version. Record those choices alongside your saved workflow.

**Source-aligned** means that an implementation targets the reference source's
behavior. **Independent numerical evidence** compares VIPP with separately
executed reference software. Neither establishes that an analysis is suitable
for a biological question.

| VIPP operation | Use it for | Evidence boundary |
| --- | --- | --- |
| [ImageJ Gaussian Blur](#imagej-gaussian-blur) | An ImageJ 1.54p slice-wise Gaussian step | 37 independent reference cases; an acquired mask workflow also matches. Unreleased after 0.16.0a3. |
| [ImageJ Default Threshold (8-bit)](#imagej-default-threshold) | Per-plane byte conversion followed by ImageJ Default | Experimental, source-aligned; acquired workflow comparison passes, broad independent goldens remain pending. |
| [Sigma Filter](#sigma-filter) | Sigma Filter Plus edge-preserving smoothing | 14 independent unsigned-image cases match; two intentional differences are documented. |
| [Remove Outliers (Binary)](#remove-outliers-binary) | ImageJ-style bright-speck removal or dark-notch filling on a binary mask | Source-aligned binary specialization with footprint/majority checks; external Fiji execution parity is not established. |
| [Colocalization metrics](#coloc-2-metrics) | Selected Pearson, Manders and Costes outputs shared with Coloc 2 | Experimental, source-aligned to Coloc 2 3.1.0; independent Fiji-generated goldens remain pending. |

## ImageJ Gaussian Blur

**Unreleased after 0.16.0a3:** Choose this separate CPU node for ImageJ 1.54p's
direct Gaussian convolution. It accepts non-empty scalar `uint8`, `uint16` and
finite `float32` images with trailing YX axes. Leading Z, time and channel
positions are processed independently. Shape, dtype and physical grid are
preserved.

**Sigma (pixels)** is the standard deviation, from 0 through 8.5 pixels. The
operation uses nearest-edge extension, float32 X-then-Y passes, dtype-specific
kernel accuracy and final integer rounding. Sigma zero returns an unchanged
copy. Larger sigma requires ImageJ's downsampling branch and is rejected;
unsupported dtypes, non-finite input and float32 arithmetic overflow also fail
explicitly. ROI filtering, physical-unit sigma, encoded RGB, volumetric blur
and GPU execution are outside this node's contract.

Use this node when a macro's Gaussian step must match numerically. On CPU,
ordinary **Gaussian Blur** uses SciPy's reflected edges and a kernel truncated
at four sigma; integer outputs also use integer intermediate passes. The ImageJ
node uses nearest edges and float32 intermediate passes before final integer
rounding. These differences can change thresholded pixels even when the blurred
images look similar. **Gaussian Blur 3D** retains its volumetric algorithm.

The 37 cases execute pinned official ImageJ 1.54p bytecode independently. They
cover all three dtypes, tiny planes, sigma 0/0.5/1.5/8.5 and a 41×41 signed-zero
float32 case. A separate acquired uint16 workflow matches through blur, byte
conversion, threshold, morphology, masks and marker crops. This is bounded
Windows CPU evidence, not a guarantee for every input or platform. See the
[Gaussian qualification record](https://github.com/rensutheart/napari-vipp/blob/main/docs/validation/imagej-gaussian-compatibility.md).

## ImageJ Default Threshold

Choose **ImageJ Default Threshold (8-bit)** when the intended sequence converts
each scalar YX plane to 8-bit, then applies ImageJ 1.54p's modified IsoData
**Default** threshold. The source-aligned target covers `uint8`, `uint16` and
`float32`; leading planes are independent. The output is a Boolean mask.
Existing `uint8` values stay unchanged; `uint16` and `float32` byte conversion
uses each plane's own min/max range. Inspect faint slices against their raw
intensities.

New nodes use the fixed Default method. An older saved ImageJ Triangle choice
retains its fixed legacy calculation. Generic **Triangle Threshold** and
**Isodata Threshold** have different conversion/histogram contracts.

Boolean handling, other floating dtypes and RGB/RGBA luma reduction are VIPP
extensions. NaNs become zero during byte conversion; infinities are rejected.
The acquired Default sequence above matches, but broad independently generated
ImageJ threshold fixtures remain pending. Keep this path experimental and
compare it with the intended reference before consequential use.

## Sigma Filter

Choose **Sigma Filter** for the edge-preserving **Sigma Filter Plus** approach,
rather than Gaussian smoothing. It accepts finite native-endian `uint8`,
`uint16` or `float32`, with radius 0.5–10 pixels. Sigma width must be non-negative
and the minimum accepted fraction must be between 0 and 1. Resolved YX planes,
channels and other leading positions are independent; nearest-edge samples are
used. There is no ROI/mask input or 3D neighborhood.

Fourteen independent cases execute the official published plugin under ImageJ
1.54p and match for `uint8`/`uint16`. Two further cases deliberately differ:
VIPP rounds the minimum sample count up exactly and clamps cancellation-induced
negative variance to zero. External float32 and Fiji ROI behavior are not
qualified by those unsigned fixtures. See the
[Sigma Filter contract and evidence](https://github.com/rensutheart/napari-vipp/blob/main/docs/gpu-phase4-sigma-filter-implementation-report.md).
GPU eligibility has a separate [compute contract](../how-to/choose-compute.md).

## Remove Outliers (Binary)

This node specializes ImageJ's **Remove Outliers** behavior for Boolean or
unambiguous `uint8` 0/1 or 0/255 masks. It uses circular, nearest-edge YX
neighborhoods independently for each leading plane and returns `bool`.
Foreground removal can only turn foreground off; background filling can only
turn background on. Grayscale images and label IDs are outside this contract.

Footprint and majority-decision tests support the source-aligned implementation;
they do not execute Fiji independently. CPU/GPU equality is a separate claim.
See the [binary cleanup workflow](../workflows/segmentation-label-cleanup.md#cpu-and-gpu-boundaries-in-this-workflow).

## Coloc 2 metrics

VIPP targets deterministic Pearson, Manders and classic Costes threshold
semantics from **Fiji Coloc 2 3.1.0** for the shared pixel, masked and object
metrics. Independent Fiji-generated numerical parity remains pending.
This is separate from reproducing a preprocessing mask and does not reproduce
Coloc 2's complete report or randomized Costes significance test.

Preserve the table's `coloc_semantics` and `coloc_validation_status` fields and
exact metric names. Read the [metric definitions and output scope](colocalization-metrics.md#fiji-coloc-2-output-scope)
before comparing tables between applications.

## Match the complete workflow

1. Use the same source pixels, complete planes, channel identities, axes and
   physical grid. Reader and format differences need their own checks.
2. Record the reference version, conversion order, threshold scope and all
   cleanup settings. Fiji Binary Options, including iterations, count,
   background convention and edge padding, can change morphology.
3. Compare intermediate arrays as well as the final result. Compare Boolean
   masks by foreground membership when Fiji uses 0/255 storage.
4. For a tissue ROI, review coverage in every acquired plane and use the
   irregular mask to define the measurement population. A crop rectangle alone
   does not select that population. See the
   [nuclear tissue ROI workflow](../workflows/colocalization-association.md#build-an-independent-tissue-roi-from-nuclei).

**Rolling-Ball Background** and **Subtract Background** provide related
ImageJ-style tasks using VIPP's own implementation; they are not externally
qualified reproductions of ImageJ's background subtracter. **ImageJ TIFF** is
a format interoperability option, not evidence of processing parity; check its
[metadata and dtype limits](import-export.md).
