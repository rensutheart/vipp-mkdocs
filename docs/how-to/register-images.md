# Register images and correct drift

Align two images, or correct a time-lapse by moving each complete XY image or
XYZ volume as one unit. Estimate the motion once, then reuse it for the original
intensity data and compatible masks or labels.

!!! info "New in 0.16.0a2"
    These registration nodes and examples require 0.16.0a2 or newer.
    Registration is CPU-only in this implementation.

## Start with a known-answer example

Choose **Open example…** from the three-dot workflow menu after **Save**, then
open an example in **Registration & Alignment**:

| Example | What to inspect |
| --- | --- |
| **Subpixel 2D Registration** | Recover a known fractional-pixel shift despite a brightness change and light noise. |
| **Anisotropic 3D Rigid Registration** | Align a rotated volume with unequal Z/Y/X voxel spacing and a nonzero origin. Check several Z positions, not just one slice. |
| **Whole-volume XYZ Drift Correction** | Estimate motion from one channel at six time points, then align both channels and companion object labels with the same transforms. |

The canvas notes state the synthetic motion. Use **Calculate all** to calculate
the manual nodes, then select **Apply Transform** to inspect the aligned image.
Select its **Valid coverage** output to inspect the usable region. Synthetic
success does not validate a biological experiment.

## Correct time-lapse drift

1. Check that the input has explicit axes such as `TYX`, `TZYX` or `TCZYX`.
   Verify its pixel/voxel sizes and units in the metadata inspector.
2. Add **Estimate Registration** under **Image Data → Registration** and connect
   the time series. Set **Register** to **Time series**.
3. Start with **Motion model → Translation**. Choose the **Estimation channel**
   that shows stable, distinctive structures. Channel indices start at `0`.
4. Choose **Reference time**, also starting at `0`. Every volume is aligned
   directly to this one time point, not to the preceding time point.
5. Calculate the node. Review the **Diagnostics** table in its inspector for
   overlap, displacement and optimization messages. The transform summary
   describes the motion instructions; it is not an image preview.
6. Under **Next step**, choose **Add Apply Transform**. VIPP adds and selects the
   node, connecting the original time series and the estimated transform for
   you. Review its settings, then calculate; adding the node does not calculate it.
7. Inspect the aligned result across time and Z. Use **Valid coverage** to exclude
   filled borders from comparisons or measurements.

One transform is estimated for each complete spatial volume. It is shared by
every channel at that time. T and C are never treated as spatial axes, and Z
slices are never independently registered.

!!! warning "Choose a reference that answers your question"
    Correct acquisition drift; do not force genuinely changing structures to
    coincide. Similarity scores cannot distinguish drift from biological motion.
    Use independent landmarks or another justified reference when assessing
    alignment.

## Align two images

Set **Register → Two images** and connect the **Moving image** and **Reference
image**. Choose the estimation channel in each. Calculate **Estimate
Registration**, then use **Next step → Add Apply Transform** to connect the
original moving image and its transform. Calculate **Apply Transform** to create
the aligned image. The reference determines the output spatial grid.

If that continuation already exists, **Show Apply Transform** selects it instead
of adding a duplicate. You can still explicitly add another. Adding a node and
its connections is one undoable change and leaves existing branches intact.

Use **Rigid** when translation alone is insufficient and rotation is expected.
Use **Affine** only when scale or shear is scientifically justified: it can alter
object shapes, sizes and the measurements derived from them. See the
[model comparison and input limits](../reference/registration.md).

## Reuse motion and review results

- Connect another **Apply Transform** to a sibling channel, mask or label output
  derived from the same original moving data. Matching shape alone is not enough:
  the source coordinate frame and spatial calibration must also match.
- Leave **Interpolation → Automatic** for linear intensity interpolation and
  nearest-neighbour mask/label interpolation. Linear intensity output is
  floating-point; masks and labels retain exact IDs.
- Use **Compare Images** for images already on the same physical grid. Enable
  its coverage input to exclude border fill, and compare before and after on the
  same valid region. Set its intensity range explicitly for SSIM and PSNR;
  changing this range does not normalize the images.
- Use **Export diagnostics…** for the readable table, **Export transform…** for
  versioned transform JSON, or **Export both…** to save both outputs. Keep the
  workflow, source data and calibration alongside the transform. JSON loading
  is available to Python callers; this first implementation does not add a GUI
  transform-import control.

If registration rejects an input or overlap, review the channel, axes,
calibration and reference rather than treating the error as zero motion. See
[registration limits and diagnostics](../reference/registration.md#limits-and-review).
