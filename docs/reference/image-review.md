# Review Images

!!! info "Unreleased after 0.16.0a3"
    This reference describes the development implementation. It is not a claim
    that the feature shipped in the published 0.16.0a3 release.

Review Images is a **presentation-only sink**: required **Image A**, optional
**Image B**, and no scientific output image or table. Its compact graph card
shows the two inputs and **Open review…**, without an output port, output
thumbnail or **No output** placeholder. Its separate window has
an inspector sidebar and one overlay or two selectable linked napari panes.
Each pane is a cohesive framed card containing its header/selector, native
image view and footer title.
Use [the review guide](../how-to/review-images.md) for steps.

## Input contract

| Kind | Accepted representation | Controls |
| --- | --- | --- |
| Scalar intensity | Real numeric image with explicit YX, ZYX, TYX or TZYX axes | Black/white levels, colour map, fixed colour scale, visibility cutoff, opacity, visibility and scalar-only 3D rendering |
| Binary mask | Boolean array with explicit spatial/time axes | Foreground colour, opacity and visibility; background 0 transparent |
| Label image | Explicit labelled image carrying non-negative integer IDs | Categorical colours, opacity and visibility; background 0 transparent |
| RGB/RGBA | Explicit encoded RGB/RGBA metadata with a trailing component axis of length 3/4 | Original colours, opacity and visibility; no scalar contrast/colormap controls |

RGB is never inferred merely because a dimension has length three or four.
Encoded colour inputs use uint8 or finite float values in the explicit 0–1
display range; unsupported encodings must be converted explicitly upstream.
Ordinary C stacks need **Extract Channel** or **Composite to RGB** upstream.
Ambiguous/inferred axes need an explicit declaration upstream. Review requires
resident current NumPy results; it is not a new large-file loading strategy.

Paired inputs must agree in spatial and time axes, shape, scale, translation
and compatible units. There is no hidden registration, time broadcasting,
axis reorder, interpolation, intensity normalization or scientific casting.
The original scientific buffers are read-only.

## Display and navigation

- **Top toolbar:** Side by side or Overlay; 2D slice or 3D volume where the
  spatial data supports it; Link viewpoint, Axes and Scale bar. Icons follow the
  active palette without replacing the controls' text labels.
- **3D → 2D:** switching a volume to 2D resets the plane to XY and exposes Z
  navigation. Deliberately selecting XZ or YZ slices remains supported; reopening
  an already-2D saved recipe preserves its selected plane.
- **Pane selectors:** A, B or A + B above the left and right panes, where a
  second input is connected.
- **Shared navigation below the panes:** T and spatial-slice positions, where
  applicable, always stay synchronized. The spatial-slice label follows the
  currently undisplayed axis (Z, Y or X). The editable number is the one-based
  current position; `/ N` is a separate total-count label immediately after the
  box. The calibrated world-coordinate caption remains visible beside it.
- **Link viewpoint:** optionally synchronizes pan, zoom and camera rotation.
  Disabling it allows different camera viewpoints, not different timepoints or
  slices. It is not an alignment transform or a registration guarantee.
- **XY / XZ / YZ:** orthogonal slice planes in 2D, or axis-aligned viewpoints in
  3D. **Oblique** selects an angled 3D view where supported. These are display
  orientation presets, not resampling or scientific image transforms; they sit
  below the panes beside Fit views.
- **Axes:** show or hide the 3D orientation axes in both panes together. Enabled
  by default and effective only in 3D; this display setting is saved with the
  review recipe. Arrows and labels appear on a transparent background without
  an opaque box. This is presentation only; source arrays are unchanged.
- **Scale bar:** beside Axes, show or hide scale bars in both panes in 2D and
  3D. Enabled by default, with a transparent background. A bar appears only
  where compatible spatial units make calibration meaningful; the switch does
  not supply or repair calibration. Visibility is saved with the review recipe.
- **Link A/B contrast:** optional for two scalar inputs; colours and opacity
  remain independent. Off by default.
- **Fit views:** fit the review data. **Reset display:** restore presentation
  defaults without recalculating the workflow.
- **Read-only · Native analysis resolution:** status text in the same bottom
  row as Oblique/XY/XZ/YZ and Fit views, rather than a separate row.

Scalar black/white levels must be finite and ordered. Opacity ranges from 0 to
1. The visibility cutoff is display alpha, not a numerical segmentation
threshold. Ordinary graphics texture/colormap precision applies, so displayed
boundaries are not an exact scientific acceptance test. The scalar colour bar
retains its black/white mapping as low values are hidden. **Lock colour scale**
prevents edits to the scalar black/white limits when a fixed range is meaningful.

Display recipes, including the orientation preset, axes/scale-bar visibility and
per-input 3D rendering controls, are stored per review node in workflow UI
metadata.
Current camera, timepoint and slice positions are
runtime-only navigation. They do not become processing parameters or scientific
cache keys. Review nodes have
no output for downstream analysis, batch image publication or numeric export.
Use **Compare Images** for quantitative RMSE/correlation/SSIM/PSNR instead.

## Live updates and current results

A visible open review retains its last complete inputs during upstream edits
and calculation, clearly marked waiting/noncurrent. It does not initiate
recalculation. After calculation finishes and the complete, current reviewed
inputs are accepted, A/B are replaced together; partial previews do not replace
one side independently. Same-grid replacement preserves camera/navigation,
contrast and display styles.

Failure, cancellation, supersession or a missing required review source cannot
publish a current pair. An unrelated branch may fail while the complete A/B
results are accepted; current review status is not a claim that every node in
the workflow succeeded. A one-input review applies the same acceptance rule to
its connected Image A.

Grid changes (including axes, shape or calibration), image-kind changes and
connected-input presence changes require reopening. There is no implicit
resampling. Visible review inputs are presentation retention targets even in
Low-memory cache mode, still subject to the normal
[memory/resource guards](cache-memory.md#memory-guard). Retention does not make
arbitrary volumes fit memory or turn waiting data into current scientific
results.

## 3D colour-rendering boundary

Scalar volumes offer **3D rendering** controls per input, only in 3D:

| Choice | Meaning and controls |
| --- | --- |
| **Maximum intensity (MIP)** | Default. Maximum displayed intensity along each viewing ray, without depth weighting or surface lighting. |
| **Depth-weighted intensity** | Nearer structures receive more prominence. Attenuation defaults to 0.05 and must be finite and non-negative. It is not opaque foreground occlusion. |
| **Surface (isosurface)** | A lit display surface at a source-intensity value, initially the black/white midpoint if no level is set. Interior structure can be hidden. It does not calculate a scientific segmentation or surface mesh. |

Depth weighting and isosurface lighting change apparent brightness. They are
not quantitative colour-scale/intensity review. In these modes the colour bar
is labelled **Base colour scale (before shading)**: its numeric limits describe
the base mapping, not the shaded pixel brightness. **Lock colour scale** protects
black/white limits only; rendering mode, attenuation and surface level remain
independent presentation controls. Use 2D slices or unshaded MIP to inspect the
base mapping; numerical analysis still uses scientific results, not renderer
pixels. Two scalar inputs in A + B are combined additively, without physically
correct inter-layer occlusion.

These controls are saved presentation metadata and do not alter scientific
arrays, measurements or cache keys. RGB retains the component-MIP adapter below;
the scalar choices do not change mask or categorical-label rendering.
Categorical label volumes use napari's native volume presentation.
Boolean masks use a shaded **3D** surface rather than a flat foreground
maximum-intensity silhouette. Interpolation and lighting approximate the
displayed surface; they do not smooth or change the Boolean mask. Sampled voxel
facets can remain visible, so this is not an exact geometric reconstruction.
Mask **2D slices** use nearest-neighbour display with a transparent zero
background. Native RGB/RGBA **2D slices** retain encoded colours.

Ordinary Boolean masks share their source buffer for 3D display. The rare case
of Boolean True stored with noncanonical bytes requires a separate read-only
display buffer, costing one byte per voxel. VIPP checks available host memory
before allocating it and reports an actionable error if headroom is
insufficient. The scientific mask and its stored bytes are never changed.

RGB **3D** uses a clearly labelled display-only adapter: separate red, green
and blue component maximum-intensity projections combined additively. Component
maxima can originate at different depths. This is **not voxelwise RGB volume
ray-casting**, not a single joint-channel projection and not parity with the
custom napari-racc shader. RGB examples therefore open in 2D slices.

RGBA **3D** is unavailable because this adapter cannot preserve per-voxel
alpha. Use 2D slices; VIPP does not silently discard the alpha channel.

Two panes may use additional graphics memory even when they share read-only
source arrays. Large-volume memory/performance, acquired-microscopy accuracy,
minimum-dependency versions and native Linux/macOS remain unqualified for this
feature. Local Windows checks and synthetic fixtures are not those release
gates. Renderer output is for visual review, not numerical validation.
