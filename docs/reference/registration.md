# Registration and image comparison

This reference defines the registration nodes introduced in 0.16.0a2. For a practical
walkthrough, see [Register images and correct drift](../how-to/register-images.md).

!!! info "New in 0.16.0a2"
    These nodes run on the CPU. No GPU registration, deformable registration,
    stitching is included. For position-based object links, use the separate
    [tracking nodes](tracking.md).

!!! info "New in 0.16.0a3"
    The **Previous frame** time-series strategy and its cumulative-quality
    controls below extend the fixed-reference registration introduced in 0.16.0a2.

## Nodes and outputs

| Node | Inputs | Outputs |
| --- | --- | --- |
| **Estimate Registration** | Moving and reference images, or one time series | Reusable spatial **Transform** and **Diagnostics** table |
| **Apply Transform** | Original moving image/mask/labels and a transform | Aligned data on the reference grid and Boolean **Valid coverage** |
| **Compare Images** | Reference and comparison images, optionally valid coverage | One row of comparison metrics per spatial volume and channel |

Estimation and resampling are separate. **Estimate Registration** does not
change input pixels. **Apply Transform** resamples the original data once.
Transforms are first-class graph outputs, not images: they have no intensity
histogram or napari image layer.

### Inspect and export the estimate

Estimate Registration always shows its **Diagnostics** table in the inspector,
alongside a compact transform summary: motion model, transform count, spatial
axes, units and reference. There is no **Displayed output** selector for this
node. Its graph card summarizes both outputs; expand the technical metadata
only when more detail is needed.

- **Export diagnostics…** saves the readable results table.
- **Export transform…** saves the numerical motion instructions and their
  calibration/settings as versioned JSON, not an aligned image.
- **Export both…** saves both outputs, without needing to select either one.

The transform can feed **Apply Transform** within the workflow. JSON loading
is available to Python callers, but there is no GUI transform-import control.

### Add the aligned-image step

The neutral **Next step** suggestion explains what is needed to create the
aligned image. **Add Apply Transform** places and selects a new node, connecting
the estimator's transform and the exact moving-image output used for estimation.
It does not calculate the node, replace connections or remove existing branches.
One **Undo** reverses the addition and its connections.

If a matching Apply Transform is already connected to those two outputs,
**Show Apply Transform** selects it. An explicit add-another action remains
available; compatible masks, labels or other images can also use the transform
through their own Apply Transform nodes.

## Motion models

| Model | Changes allowed | Implementation | Typical use |
| --- | --- | --- | --- |
| **Translation** | Shift only, including subpixel shifts | scikit-image phase cross-correlation | Acquisition drift; start here |
| **Rigid** | Rotation and translation | SimpleITK multiresolution registration | Reorientation without changing physical shape |
| **Affine** | Translation, rotation, scale and shear | SimpleITK, initialized from a rigid fit | Justified global geometric distortion |

Affine is not the default drift correction. It can change measured object size
and shape. Rigid/affine optimization offers **Correlation** for comparable
contrast or **Mutual information** for differing contrasts. Optimization can
converge to an incorrect match; its final score is not a confidence probability.

## Axes, calibration and time

- Explicit YX or ZYX spatial axes are required, with optional T and C. Array
  shape alone does not establish axis meaning.
- Physical spacing and origin are respected, including unequal Z/Y/X spacing.
  Compatible physical length units are converted consistently; uncalibrated
  pixel coordinates remain explicitly pixels.
- Translation requires equal spatial extents and compatible sampling. Rigid and
  affine can use different spatial grids with compatible units and rank.
- **Two images** mode requires individual spatial images/volumes. Select a time
  point first if the input includes T.
- **Time series** estimates one transform per complete spatial volume into the
  selected reference time. **Fixed reference** (the default) estimates directly
  against that time; the **Previous frame** strategy combines
  adjacent-volume estimates. The reference has an identity transform by
  definition. Estimation uses one channel; application reuses the same motion
  for all channels.
- Applying a series requires matching time-point count and time calibration.
  A pairwise transform is not silently broadcast over a time axis.

The saved direction is **moving coordinates → reference coordinates**. A
transform also records both spatial grids, source-frame identities, estimation
settings and implementation information. Reuse is rejected when the moving
frame, extents, origin or sampling do not match. Cropping or recalibration can
therefore require re-estimation.

## Time-series strategies

| Strategy | Estimation reference | Main limitation |
| --- | --- | --- |
| **Fixed reference** (default) | Every original frame is estimated directly against the selected reference time. | Distant frames may share little structure with the reference. |
| **Previous frame** | Each original frame is estimated against its adjacent neighbour toward the reference; motion instructions are then combined. | Adjacent estimation errors accumulate with distance from the reference. |

For a nonzero reference time, frames after it use the preceding frame and
frames before it use the following frame. Both directions end at the chosen
reference. Whole XYZ volumes move as units; no Z slice is fitted independently.
Estimation never uses already-aligned images. **Apply Transform** still resamples
the original data once onto the reference grid.

In **Previous frame**, maximum displacement, minimum overlap and shared-structure
checks always gate each adjacent pair. One failed pair rejects the whole result;
there is no skipped frame, identity replacement or automatic alternative fit.
**Previous-frame cumulative quality** controls the additional reference check:

- **Report only** (default) records combined displacement, valid coverage and
  correlation against the reference. It does not reject on those cumulative
  values, which can include zero remaining coverage.
- **Require local limits** also requires combined displacement and valid coverage
  to meet the same limits specified for adjacent pairs.

Cumulative correlation is diagnostic only under both policies, not a registration
confidence score. It is unavailable if there is insufficient valid support or
no intensity variation. Always inspect **Valid coverage** before using aligned
data in measurements. Good local fits alone do not establish global accuracy.

## Controls that need interpretation

| Control | Meaning |
| --- | --- |
| **Estimation channel / Reference channel** | Zero-based channel index. Use `0` for a single-channel image. |
| **Reference time** | Zero-based fixed time anchor; default `0`. |
| **Time-series strategy** | **Fixed reference** by default; **Previous frame** combines original adjacent-volume estimates toward the anchor. |
| **Previous-frame cumulative quality** | **Report only** by default; **Require local limits** additionally enforces displacement and overlap limits after composition to the anchor. |
| **Translation subpixel factor** | `10` resolves shifts in one-tenth-pixel steps; this is numerical precision, not a guarantee of accuracy. |
| **Maximum translation (fraction of image)** | Maximum permitted displacement of the moving grid centre relative to the reference centre, as a fraction of each reference extent. For rotation/affine it is not a bound on every pixel's displacement. Previous-frame registration always applies it locally; the cumulative policy controls the combined result. |
| **Minimum valid overlap (fraction)** | Required fraction of the reference grid supported by the moving image after linear interpolation. Previous-frame registration always applies it locally; the cumulative policy controls the combined result. |
| **Maximum optimization iterations** | Limit at each resolution level for rigid/affine fitting. Review the stopping message. |

The fixed slider windows cover reference channel indices `0` to
`15`, reference time `0` to `100`, optimization iterations `1` to `1,000`,
comparison intensity range `1` to `65,535`, and outside-image fill `-255` to
`255`. Numeric spinners still accept the full valid ranges, subject to the
input and output requirements below. Enter values outside these windows
directly; accepted values remain unchanged when reopening the inspector or
workflow. The windows do not change defaults or scientific limits.

## Resampling and coverage

**Automatic** interpolation uses nearest neighbours for masks/labels and linear
interpolation with `float64` output for intensity images. **Nearest** preserves
the input dtype, including wide integer label IDs. **Linear** is rejected for
masks/labels and for wide integers that cannot be represented exactly before
interpolation. Inputs are not modified or intensity-normalized.

**Outside-image fill** defaults to `0`; it must be finite and representable in
the output dtype. A filled pixel is not measured signal. **Valid coverage** has
the aligned output's axes and shape. It is true only where the selected
interpolation has valid support in the original moving image; it is repeated
consistently across channels.

Interpolation may affect intensity and downstream measurements. Nearest
resampling preserves IDs, but not object volume or topology at subpixel shifts.
Keep this distinction when comparing object measurements before and after.

## Diagnostics and comparisons

**Diagnostics** reports the time/reference indices, model, estimator score,
post-alignment correlation, valid-overlap fraction, centre displacement,
optimizer stopping description and review notes. Scores from different methods
are not interchangeable.

**Previous frame** diagnostics separate local fit quality from the
combined result. All displacement fields use the transform's physical units
(micrometres or explicitly uncalibrated pixels).

| Fields | Meaning |
| --- | --- |
| `time_index`, `reference_time` | Original frame and final reference index, both zero-based |
| `pair_reference_time` | Adjacent frame used for this local fit; the reference row points to itself |
| `pair_optimizer_score`, `pair_correlation`, `pair_valid_overlap_fraction` | Quality of the original adjacent pair, not the full path to the reference |
| `pair_center_displacement_y/x` (and `z` in 3D) | Local displacement of the moving grid centre |
| `cumulative_correlation`, `cumulative_valid_overlap_fraction` | Correlation and valid linear-interpolation coverage after combined motion to the reference |
| `cumulative_center_displacement_y/x` (and `z` in 3D) | Combined displacement to the reference |
| `stop_reason`, `review_note` | Local estimator message and cumulative-error/policy reminder |

Rows remain in original time order. Transform JSON stores the cumulative motion,
the strategy and its quality policy. Older JSON without strategy metadata keeps
its fixed-reference meaning and can still be loaded.

**Compare Images** requires the same shape and physical grid and performs no
alignment or normalization. Its explicit positive **Intensity range for SSIM /
PSNR** is the intensity span used in those metrics, not a scaling operation.
Its odd **SSIM window (pixels per spatial axis)** sets the neighbourhood. With
**Use valid-coverage mask** enabled, connect a Boolean mask on the same grid.

| Output | Interpretation |
| --- | --- |
| `valid_count` | Number of compared pixels/voxels after coverage restriction |
| `rmse` | Root-mean-square intensity difference; sensitive to intensity scale |
| `pearson_r` | Linear intensity correlation; undefined for constant values |
| `ssim` / `ssim_window_count` | Structural similarity and number of valid window centres; only windows wholly inside valid coverage contribute |
| `psnr_db` | Peak signal-to-noise ratio using the supplied intensity range |
| Status fields | Explain unavailable values; an exact match has infinite PSNR recorded as a status, not a non-finite JSON number |

A similarity improvement is not evidence of biological correspondence, and
after-registration scores alone do not establish an improvement. Use the same
population/coverage and intensity range for before/after comparisons.

## Limits and review

Non-finite inputs, ambiguous axes, flat registration images, insufficient
overlap and implausible displacement fail visibly rather than becoming identity
transforms. Repetitive structures can produce ambiguous translation peaks.
Larger rotations and poor initial overlap can still lead to incorrect fitting.

There is no per-slice Z alignment, automatic reference
selection, automatic biological-quality judgement or GPU registration. Review
overlays across the full volume/time range and independent landmarks when
available. The synthetic examples provide known-answer checks, not validation
of every dataset or biological assay.

The algorithms are described in the
[scikit-image registration reference](https://scikit-image.org/docs/stable/api/skimage.registration.html)
and [SimpleITK registration overview](https://simpleitk.readthedocs.io/en/latest/registrationOverview.html).
