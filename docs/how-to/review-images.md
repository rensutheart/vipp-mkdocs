# Review images in linked views

!!! info "New in 0.16.0a4"
    **Review Images** requires 0.16.0a4 or newer. Use the manual version selector
    to match the software installed for your analysis.

Compare two aligned results with a familiar inspector sidebar: an intensity
image beside its segmentation, red beside green, or an RGB composite beside a
numeric colour-mapped result. Review Images changes presentation only. It does
not calculate an image, run registration, or change measurements.

On the workflow canvas, Review Images is a compact node with **Image A** and
**Image B** inputs and **Open review…**. It has no output thumbnail or **No
output** placeholder: the images are reviewed in the separate window, not
produced as a new node output.

## Open a review

1. Add **Review Images** and connect an image to **Image A**. Connect a second
   image, mask or labelled image to the optional **Image B** port.
2. Calculate the upstream nodes. The review uses their current cached results;
   **Open review…** does not start an analysis calculation.
3. Click **Open review…** on the node or in its inspector.
4. Use the top toolbar to choose **Side by side** or **Overlay** and **2D slice**
   or **3D volume**. Above the left and right panes, select **A**, **B**, or
   **A + B** as available. For a volume, switching from 3D to 2D starts in the
   **XY** plane with **Z** navigation.
5. Use the shared controls below the panes to select the **T** timepoint and
   spatial slice, where those axes are available. Both panes always show the
   same timepoint and slice. The editable number is the current position,
   starting at 1; the total count appears separately as `/ N`, followed by the
   calibrated coordinate.
6. Keep **Link viewpoint** enabled to rotate, pan and zoom together. Disable it
   to inspect the same timepoint from different viewpoints. Use **Fit views**
   beside the orientation buttons below the panes if the image is off screen.
   **XY**, **XZ** and **YZ** select orthogonal planes
   in 2D or aligned viewpoints in 3D. The slice control follows the remaining
   spatial axis (Z, Y or X). **Oblique** selects an angled 3D view when supported.
   These choices do not resample or transform the images.

**Read-only · Native analysis resolution** shares the bottom row with
**Oblique**, **XY**, **XZ**, **YZ** and **Fit views**.

Use the top toolbar's **Axes** switch to show or hide the 3D orientation axes
in both panes together. It is enabled by default and applies only to 3D views.
The arrows and labels have a transparent background, not an opaque box over
the images. This is display-only and does not change source pixels.
Toolbar icons follow the active palette while retaining their text labels.
Beside **Axes**, **Scale bar** shows or hides the scale bars in both panes, in
2D or 3D. It is enabled by default; a bar appears only where compatible spatial
units support meaningful calibration. The bar's background is transparent.

Each framed pane joins its header/selector, native image view and footer title
into one card. The review has its own napari panes and layers. It does not
rearrange the main napari preview or carry a Crop outline into another workflow.
Painting and label editing are disabled.

Both inputs must have explicit matching spatial/time grids, including axis
names, spacing, units and origin. Equal dimensions alone are not enough. If
they do not align, fix calibration or use **Apply Transform** upstream;
Review Images never silently resamples or broadcasts one timepoint.

## Choose the right presentation

| Inputs | Suggested left pane | Suggested right pane |
| --- | --- | --- |
| Intensity and mask/labels | A | A + B |
| Red and green scalar channels | A | B |
| RGB composite and numeric index | A | B |
| Original and processed intensity | A | B |

For two scalar channels, choose their **Colour map** separately, for example
Red and Green. **Link A/B contrast** is optional and off by default;
enable it only when a shared numeric intensity scale is meaningful. The same
input uses the same presentation wherever it appears in the two panes.

An RGB input keeps its original encoded colours; it does not offer a misleading
scalar-colormap selector. Masks have a **Foreground colour…** and transparent
background. Label IDs keep categorical colours rather than being stretched
as scalar intensities.

## Choose a scalar 3D presentation

In **3D volume**, each scalar input has a **3D rendering** choice:

- **Maximum intensity (MIP)** is the default: show the strongest value along
  each viewing ray.
- **Depth-weighted intensity** gives nearer structures more prominence. Adjust
  attenuation, initially 0.05, to change the depth weighting; it does not create
  opaque foreground occlusion.
- **Surface (isosurface)** shows a lit surface at a source-value display level.
  Set that level explicitly, or start at the midpoint of the black/white levels.
  A surface can hide interior structures.

Depth weighting and surface lighting change apparent brightness. For direct
colour-scale/intensity inspection, use **2D slice** or unshaded MIP instead;
shaded views are not quantitative intensity review. In these shaded 3D modes,
the bar is labelled **Base colour scale (before shading)**. **Lock colour scale**
protects black/white limits only, not shading or the surface level.

An A + B overlay of two scalar inputs is additive, not physically correct
inter-layer occlusion. These choices do not affect RGB's labelled component-MIP
adapter, Boolean mask surfaces or categorical label rendering.

## Review a numeric colour scale

Set the scalar input's **Black level** and **White level**, enable **Lock colour
scale** when that range has a fixed meaning, then use **Hide below…** and
**Visibility cutoff** to suppress weak displayed values.
The **Fixed colour scale** keeps the same mapping while the cutoff changes;
the lock prevents accidental edits to its black/white limits.
These controls do not threshold, clip or normalize the source array. Use an
actual threshold node if you need a scientific mask.

Yellow in a red/green overlay is a visual cue, not a quantitative
colocalization measurement. Review Images does not calculate RACC. A supplied
RACC-like output remains numeric; its interpretation belongs to the
[RACC-like index reference](../reference/racc-index.md).

## Try the synthetic review examples

Open **Open example… → Image Review** and choose:

- **Linked Red and Green Channel Review**: change contrast independently,
  switch to Overlay and try linked viewpoints.
- **3D Intensity and Mask Review**: rotate both panes together, change mask
  opacity, then switch to **2D slice**. The authored mask contains two physical
  spheres with radii 5.4 and 5.0 µm on a 48×64×80 anisotropic grid; it has not been
  smoothed to improve appearance.
- **Time-series Intensity and Label Review**: move through four timepoints and
  verify both panes retain the same time and the original IDs 7 and 42.
- **3D RGB and Synthetic Index Review**: review RGB slices beside a fixed 0–1
  scalar colour scale. Change the visibility cutoff, not the colour scale.

The fourth example's index is a constructed spatial phantom, **not a computed
RACC or colocalization result**. All four examples use synthetic data, not
biological accuracy evidence.

## Save and reopen

Review arrangement, pane choices, orientation preset, axes/scale-bar visibility,
contrast, colormaps, opacity, visibility and per-input 3D rendering settings are saved in
workflow presentation metadata. Save the workflow to retain them.
Reopening a saved 2D review retains its selected XY, XZ or YZ plane; switching
from 3D to 2D deliberately returns to XY.
They are not scientific node parameters and do not invalidate upstream
scientific results. Current camera position, timepoint and slice position are
runtime navigation, not a new scientific transform or saved analysis parameter.

## Keep a review open while editing

Edit and calculate upstream as usual; the review does not initiate
recalculation. While reviewed inputs are changing or calculating, a visible
review keeps the last complete pair clearly marked as waiting/noncurrent.
Do not interpret that snapshot as the current result.

When both reviewed images have finished and their current results have been
accepted, A and B update together automatically. On the same grid and with the
same input kinds, the review preserves the view, contrast and display styles.
Failed, cancelled, superseded or missing review inputs cannot become current.

Changes to the grid, image kind or connected-input presence require reopening
the review when prompted. It never silently resamples the new data. Inputs for
a visible open review are retained as presentation targets in Low-memory mode,
but normal resource guards still apply; keeping a review open is not a way to
bypass memory limits. Closing it does not close the main VIPP or napari window.

See [Review Images reference](../reference/image-review.md) for supported
axes, rendering boundaries and qualification limits.
