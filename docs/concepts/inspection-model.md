# Inspection Model

The point of VIPP is not only to run a pipeline. It is to make each processing
decision inspectable.

## Inspection Surfaces

| Surface | Use |
| --- | --- |
| Node thumbnail | Quick scan of what each stage is doing. |
| Napari inspect layer | Full-resolution inspection of the selected node output. |
| Pinned layer | Keep important outputs visible while editing other nodes. |
| Histogram panel | Check intensity distributions and threshold choices. |
| Input histogram | Review cutoffs for threshold-like nodes. |
| Label-volume histogram | Tune label filtering against the incoming object-size distribution. |
| Table preview | Check measurement columns, row count, and units before export. |
| Graph notes | Record why a parameter or branch exists. |

## Calculation And Display Are Different Contracts

VIPP separates a node's declared scientific calculation from the compact view
used to draw it. Where a complete-population summary is described below, every
required value contributes even though the result is grouped for display.

| Inspector item | What is exact | What is display-only |
| --- | --- | --- |
| Node thumbnail contrast | Stack Percentile/Min-max summarizes the complete node output. Native `uint8`/`uint16` Percentile uses an exact histogram with identical CPU/CuPy limits; Min-max uses an exact native reduction; float and other-dtype percentiles retain the exact NumPy-compatible CPU path. Slice contrast instead normalizes the spatially sampled current view at the selected detail. | Low/Standard/High/Very High backing detail, Slice versus Stack scope, contrast mode, colormap, and the CPU/GPU statistics backend affect the card image only. Slice limits can change slightly with detail; Stack limits cannot. |
| Intensity histogram | Every finite value in the selected slice or stack is counted. | Counts are grouped for drawing: two bars for Boolean data, one for a constant image, 256 for non-negative integer data within 0–255, and otherwise 128 display bins. These bins are not the automatic-threshold bin setting. |
| Automatic-threshold guide | The guide uses the node's saved scope and scientific method parameters. | Line colour, plot scale, and the chart's display bins do not change the mask. |
| Colocalization scatter | Every ROI voxel contributes to the configured density; ROI population and the number meeting both thresholds are exact. Threshold-independent density can be reused while an exact recount runs. | Interactive rendering is capped at 1,024 bins per axis; graph scatter nodes can request up to 4,096. Colormap, logarithmic display, guide styling, and rendered output size do not change thresholds or metric tables. |
| Inspect or pinned image contrast | The final display range spans every finite value and zero, using exact finite extrema. | Contrast limits affect only rendering in napari, never the stored node output or downstream calculations. |

### Progressive inspection during a run

As each node completes in a background run, its card becomes current and its
sampled thumbnail updates immediately; later cards can still be calculating or
waiting. If the active cache policy already retains that node, selecting or
pinning it and opening its table or metadata uses the same newly completed
run-scoped payload. An otherwise prunable Low-memory intermediate gets the card
state and thumbnail without forcing VIPP to retain its full-volume payload.

This is a progress view, not by itself a partial scientific commit. Normal
success publishes the new workflow cache only when the complete run is accepted
against the same graph and source revisions. Cancellation, a newer edit, or a
superseding run removes the temporary overlays and restores the last coherent
inspection state. On failure, VIPP may accept a verified source boundary; it
may additionally accept completed processing data from a cleanup-failed result,
but only with matching actual-implementation provenance. Unreported processing
overlays are discarded and their earlier coherent inspection state is restored.

### Thumbnail detail, scope, and statistics provenance

VIPP renders cards at **Low (90 × 55)**, **Standard (180 × 110)**,
**High (360 × 220)**, or **Very High (720 × 440)** detail inside the same card
viewport. VIPP retains that source image and scales from it, so High and Very
High can improve HiDPI display, downsampling, or maximum graph zoom; they do not
guarantee a larger on-screen card. Very High uses four times the backing pixels
of High. This is a spatial
display choice. Changing it rerenders the graph but neither reruns scientific
nodes nor invalidates cached exact Stack limits.

**Stack** contrast provides a stable, resolution-independent brightness window
across T/Z/C by summarizing the complete node output once. **Slice** normalizes
the selected detail's spatially sampled current view on CPU and avoids that
full-output scan. It is intentionally responsive, but Low/Standard/High/Very High can
change its display limits slightly. Percentile Stack contrast uses
the 0.5th/99.9th percentiles. Exact native-dtype histograms avoid a full float
sort for `uint8` and `uint16`; Min-max uses a faster exact native reduction.
Float and other-dtype percentiles stay on the exact NumPy-compatible CPU path
in this release.

Presentation statistics have their own local **Auto / CPU / Prefer GPU**
preference. Auto uses the complete output dtype and byte count. Before the GPU
histogram path is warm, its conservative crossover is 384 MiB for `uint8` and
512 MiB for `uint16`; both become 32 MiB after a successful GPU calculation.
These measured defaults are heuristics, not universal fastest guarantees,
because distribution, hardware, CUDA startup, residency, and competing work can
move the crossover. Render detail is not part of this decision. **Prefer GPU**
is the explicit override. Main compute **CPU** always forces statistics CPU;
main **Prefer GPU** biases statistics Auto to GPU; main **Auto** and **Custom**
leave it adaptive.

Select a node to see that work in the compact **Thumbnail contrast** row near
the top of its inspector: **Calculating… / CPU · NumPy / GPU · CuPy / CPU
fallback / Error**. The separate scientific CPU/CuPy/cuCIM badge remains in the
node title row and still identifies what produced the node output. Hover the
inspector row or thumbnail for the detailed presentation decision; keyboard
What's This help and screen readers receive the same text. Stack scans publish
the active node/backend/phase through the toolbar
without accepting partial limits. CPU integer histograms and min-max
reductions advance and cancel between bounded chunks. An active GPU
kernel/synchronization or exact float/other-dtype NumPy percentile may contain a
non-interruptible inner pass; the UI identifies that phase and applies
cancellation at the next cooperative boundary.

### Reused and replaced Inspect layers

Recalculating the same logical node/output reuses a compatible active VIPP
**Inspect** layer and replaces only its data reference with a non-writeable view
of the exact output. VIPP preserves the working view—displayed dimensions and
slice positions, camera zoom, translation, and rotation—and compatible user
styling such as colormap, contrast, blending, opacity, visibility, gamma,
interpolation, and compatible rendering settings. Physical layer scale
continues to come from the output metadata; arbitrary napari transforms are not
part of the saved display profile. This lets you zoom into a structure, tune a
node in isolation, and compare the same region after each calculation without
the viewer jumping back to a default. Pinned layers are separate napari viewer
artifacts and do not receive this saved per-output profile behavior.

Display profiles are remembered independently for each node, output port, and
RGB display surface and are saved as presentation state in the workflow. When
you switch to another logical output, VIPP restores that output's own compatible
profile or initializes safe defaults; styling from the previous output does not
leak into it. Use the inspector header's reset action when the selected output
should return deliberately to VIPP defaults.

VIPP creates a replacement Inspect layer when the presentation class or layout is
genuinely incompatible, such as `Image` versus label-ID `Labels`, or an RGB
layout change. A Boolean mask pinned as a `Labels` overlay requires a uint8
presentation copy. The original cached Boolean array remains the scientific
output used by downstream nodes and saving. Any pending display calculation
for a superseded output is invalidated.

### Large generated layers

When an inspect, pinned, or RGB-channel layer is large, VIPP first supplies a
provisional dtype-based contrast range so napari can show the layer without
scanning it on the user-interface thread. VIPP then calculates the exact full
finite range in the background and updates the layer.

This temporary range does **not** mean the processing result is approximate.
It is only a display window. If you manually adjust the napari contrast limits
while the exact calculation is pending, VIPP keeps your adjustment rather than
overwriting it; the exact finite range remains available in the layer metadata.

For large inputs, exact histogram guides, colocalization summaries, Auto
Contrast, and generated-layer ranges may briefly show a calculating state.
Selecting another node or changing the input invalidates stale display results.

Dragging a manual input-histogram guide does not change the input population.
VIPP therefore retains the exact displayed counts while moving Binary
Threshold, Hysteresis, or explicit Rescale/Clip guides, and recalculates only
the node output after the short interaction delay. Its output histogram then
refreshes because that population really did change. Parameters that change an
automatic guide refresh that guide separately. A different connected image,
slice, or histogram scope still invalidates the input counts because it selects
a different population.

For `Rescale Intensity`, both low and high input guides are draggable. Dragging
a guide derived from exact percentiles changes the cutoff mode to explicit
values, retains the other exact cutoff, and recalculates the node. A click that
does not move the guide is not an edit. The same no-movement rule prevents
accidental Binary Threshold changes. Save the workflow after accepting a drag;
guide position is a presentation affordance for a persisted scientific value.

For colocalization, threshold scrubbing moves compatible guides immediately
and keeps the threshold-independent density visible while the exact full-ROI
count is recomputed. Rapid requests are coalesced. A density is reused only
while channels, ROI, native intensity context, and histogram definition still
match. The linked inspector and resizable pop-out colormap selectors redraw
from that cached density without recalculating a scientific result.

### Split Channels presentation output

`Split Channels` produces one scientific graph output per channel, but its node
card and inspector need one channel to present at a time. If downstream
connections use exactly one distinct output port, VIPP presents that channel in
the split node's thumbnail, napari inspect or pinned layer, histogram, output
metadata, dimension controls, and **Save selected output...** action. Multiple
branches may consume the same port; that remains one distinct used output.

If no output is connected, or the graph uses two or more different channel
ports, these presentation surfaces use the saved **Thumbnail channel** instead.
The automatic choice never changes **Thumbnail channel**, rewires a connection,
or alters the arrays supplied to downstream calculations. It only keeps all
ways of inspecting the `Split Channels` node focused on the same unambiguous
channel.

## Recommended Inspection Sequence

For segmentation:

1. Inspect the raw channel.
2. Inspect background correction or denoising.
3. Inspect the threshold mask.
4. Inspect label IDs.
5. Inspect measurement tables.
6. Save the workflow only after the intermediate stages make sense.

For colocalization:

1. Inspect both channels separately.
2. Inspect the ROI mask if used.
3. Inspect scatter/threshold guides.
4. Inspect colocalized voxels.
5. Inspect metric tables.

For skeletons:

1. Inspect the binary mask.
2. Inspect the skeleton.
3. Inspect keypoints or graph overlay.
4. Inspect branch/component labels.
5. Inspect measurement tables.
