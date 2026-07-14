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
| Intensity histogram | Every finite value in the selected slice or stack is counted. | Counts are grouped for drawing: two bars for Boolean data, one for a constant image, 256 for non-negative integer data within 0–255, and otherwise 128 display bins. These bins are not the automatic-threshold bin setting. |
| Automatic-threshold guide | The guide uses the node's saved scope and scientific method parameters. | Line colour, plot scale, and the chart's display bins do not change the mask. |
| Colocalization scatter | Every ROI voxel contributes to the 255 × 255 density grid; ROI population and the number meeting both thresholds are also exact. | Colormap, logarithmic count display, and guide styling do not change thresholds or results. |
| Inspect or pinned image contrast | The final display range spans every finite value and zero, using exact finite extrema. | Contrast limits affect only rendering in napari, never the stored node output or downstream calculations. |

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
