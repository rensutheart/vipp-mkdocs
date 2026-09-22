# Skeleton node reference

Start with the [skeleton workflow tutorial](../workflows/skeleton-network-analysis.md)
to choose 2D or 3D processing and inspect your segmentation. This page lists the
outputs, units, and assumptions needed to interpret the resulting tables.

!!! info "New in 0.16.0a2"
    **Skeletonize Labels** and **Analyze Skeleton per Label** retain the
    original object IDs. Use this label-first route when joining skeleton
    measurements to object morphology. The existing mask-first nodes,
    including **Label Skeleton Components**, retain their behavior.

## Choose what an ID means

| Route | Meaning of an ID | Use |
| --- | --- | --- |
| Labels → Skeletonize Labels → Analyze Skeleton per Label | Original segmented object, retained even if its skeleton contains multiple pieces | Join morphology and skeleton features for the same objects. |
| Mask → Skeletonize → Label Skeleton Components / Analyze Skeleton | Connected piece of the skeleton, assigned a new ID | Inspect disconnected skeleton networks without requiring an original object segmentation. |

Skeleton component IDs from the second route do not identify the original
objects. Do not merge them with morphology by matching their numeric IDs.

## Skeletonize Labels

**New in 0.16.0a2.** Skeletonizes each nonzero integer label
independently and writes that same label into its surviving skeleton voxels.
Background remains zero. Shape, label dtype, spatial calibration and leading
dimensions are retained; the input image is not changed.

Labels must be non-negative integers. Boolean masks, floating-point images
and negative labels are rejected. Label a binary segmentation before using
these nodes; wide or sparse integer IDs retain their exact values.

Different labels are never fused, including where their boundaries touch.
Disconnected regions carrying the same label retain that shared identity.
The node does not relabel objects or infer that two different IDs should be
one biological object.

**Spatial processing** and **Method** follow [Skeletonize](#skeletonize):
Auto uses Zhang in 2D and Lee in 3D, with independent leading-axis blocks.
Thinning operates on the voxel grid; it does not resample anisotropic images
or compute a physical medial axis. Inspect the segmentation and skeleton in
all relevant orientations.

## Analyze Skeleton per Label

**New in 0.16.0a2.** Connect the original label image to **Original labels**.
Optionally connect its output from **Skeletonize Labels** to **Skeleton**.
When Skeleton is unconnected, the node skeletonizes each original label
internally using its **Thinning method** setting.

A supplied skeleton must use the same grid and original label values. Every
nonzero skeleton voxel must lie inside the matching original label. A binary
mask or an independently relabeled skeleton is not a substitute for that
mapping. Invalid matches fail instead of silently assigning measurements to
the wrong objects.

The two table outputs answer different questions:

| Output | Row identity | Measurements |
| --- | --- | --- |
| Objects | Leading-axis block and original `label_id` | Per-label summary: component count, summed skeleton voxel/endpoint/junction/isolate/branch/graph/cycle counts, total skeleton length and skeleton status. |
| Skeleton components | Leading-axis block, original `label_id` and local `component_id` | Existing per-component skeleton measurements, with `component_count_in_label` and `component_voxel_fraction_in_label` describing that original label. |

`skeleton_component_count` counts connected skeleton pieces **inside one
original label**, using the full 8-neighbor graph in 2D or 26-neighbor graph
in 3D. Neighbors belonging to another label are excluded. The component table
may contain multiple rows for one object. Join morphology to the **summary**
for one row per object; joining component details duplicates that object's
morphology once per component.

Every original nonzero label has a summary row, including when it has no
surviving skeleton. `skeleton_status` is `ok` or `empty`; check it alongside zero measurements:
zero length alone also occurs for a one-voxel isolate. An object with no
skeleton has no component-detail row.

Use `label_id` together with every applicable image, time, channel or slice
identifier when joining tables. A label number is only unique within its
source spatial block. IDs and status fields are identifiers, not numerical
features to average or include in PCA.

Physical length requires complete positive spatial spacing and recognized,
compatible length units. Compatible units are converted to the X-axis unit.
With no units or pixel units, the physical-length column is absent: use
`skeleton_length_pixels` in 2D or `skeleton_length_voxels` in 3D. Partial,
unknown or incompatible physical calibration is rejected. The node does not
invent micrometer spacing. Calibration is inherited from the labels and must agree with a
supplied skeleton. Copy calibration from an intensity image only after
confirming acquisition identity, axes and any intervening resampling.

Both new nodes currently calculate on CPU. The
[worked example](../workflows/skeleton-network-analysis.md#join-skeleton-and-morphology-per-object)
shows filtering once and sharing the same objects between both branches.

## Skeletonize

- **Input:** binary mask.
- **Output:** binary skeleton mask.
- **Purpose:** Converts foreground objects into one-pixel/voxel-wide
  centerlines.
- **Spatial processing:** `3D ZYX` thins each complete ZYX volume once. Leading
  non-spatial axes are independent blocks, so `TZYX` runs one ZYX volume per
  timepoint. `2D YX` thins each YX plane independently.
- **Auto from axes:** explicit `ZYX` selects volumetric 3D processing and
  explicit `YX` selects 2D processing. A generic `QYX` stack is ambiguous and
  is rejected until Image Source records a reviewed declaration such as
  `QYX -> ZYX`, or the user deliberately chooses `2D YX`.
- **Methods:** `Auto` resolves deterministically to Lee for 3D and Zhang for
  2D. Lee is valid for 2D and 3D. `Zhang 2D` is never valid for a 3D block,
  including an empty volume.
- **Algorithm contract:** the 3D path uses scikit-image's implementation of the
  Lee, Kashyap, and Chu volumetric thinning algorithm. Lee examines a 3x3x3
  neighbourhood and rechecks deletion candidates to preserve connectivity.
  Each processed block is surrounded by background at its boundary. The
  output preserves input shape, axis records, calibration, and leading-axis
  identity.
- **Provenance:** the output metadata history records the actual Lee or Zhang
  method, resolved 2D/3D block scope, neighbourhood, and boundary assumption.
- **Use before:** `Analyze Skeleton`, `Measure Skeleton Branches`, `Skeleton
  Keypoints`, `Skeleton Graph Overlay`, `Label Skeleton Components`, `Label
  Skeleton Branches`, and `Prune Skeleton Branches`.

The Lee implementation follows T.-C. Lee, R. L. Kashyap, and C.-N. Chu,
"Building skeleton models via 3-D medial surface/axis thinning algorithms",
*Computer Vision, Graphics, and Image Processing* 56(6), 1994. VIPP currently
pins scikit-image 0.26.0 in its supported Python 3.12 application environments.

## Orthogonal 3D Skeleton QC

Use this small comparison before relying on a new volumetric segmentation:

1. Send the same explicit ZYX binary mask to two `Skeletonize` nodes. Set one
   to `3D ZYX` with `Lee` and the other to `2D YX` with `Auto`.
2. Inspect the source mask and both skeleton outputs in XY, XZ, and YZ views.
   A true 3D centerline should remain connected while it curves or branches
   through Z. A slice-wise result often appears plausible in XY but becomes a
   ribbon, a set of parallel paths, or disconnected fragments in XZ/YZ.
3. Connect each result to `Skeleton Keypoints` or `Skeleton Graph Overlay` and
   compare endpoints and junctions in all three orientations.
4. Connect each result to `Analyze Skeleton`. Review component, endpoint,
   junction, branch, and cycle counts. Large changes between the two modes are
   evidence that the spatial-processing choice materially affects network
   topology.
5. Keep `3D ZYX` only when Z is an explicitly declared spatial axis. For an
   anisotropic volume, set the Z/Y/X calibration before interpreting physical
   branch lengths.

## Analyze Skeleton

- **Input:** skeleton mask, or a binary mask if `Input` is set to `Skeletonize
  first`.
- **Output:** table, one row per connected skeleton component.
- **Purpose:** Measures whole-network/component properties.
- **Reports:** skeleton voxel count, endpoint voxels, junction voxels, isolated
  nodes, branch count, graph node/edge counts, voxel-graph edge count, cycle
  count, component context, and skeleton length in pixel/voxel units plus
  physical units when scale metadata is available.
- **Execution:** manual/cached. Use `Calculate` or enable `Auto Recalculate`
  for small data.

## Measure Skeleton Branches

- **Input:** skeleton mask, or a binary mask if `Input` is set to `Skeletonize
  first`.
- **Output:** table, one row per traced graph branch.
- **Purpose:** Measures individual branches between graph nodes.
- **Reports:** component ID, branch ID, branch type, voxel count, graph-edge
  count, branch length, endpoint-to-endpoint distance, tortuosity, start/end
  coordinates, and calibrated physical length when scale metadata is available.
- **Execution:** manual/cached. This can produce many rows on dense networks.

## Summarize Skeleton Branches

- **Input:** a table from `Measure Skeleton Branches`.
- **Output:** table, one row per grouping block. Auto grouping preserves useful
  context columns such as source, time, channel, and spatial block indices.
- **Purpose:** Converts row-per-branch measurements into compact distributions
  suitable for treatment comparison, PCA-style feature extraction, and network
  QC.
- **Reports:** branch count, component count, total branch length, selectable
  length and tortuosity statistics, and branch-type counts/fractions such as
  endpoint-to-junction or junction-to-junction fractions.
- **Use when:** you want table-derived branch distributions without manually
  configuring the generic `Summarize Measurements` node.

## Skeleton Graph Tables

- **Input:** skeleton mask, or a binary mask if `Input` is set to `Skeletonize
  first`.
- **Output:** two table outputs: graph nodes and graph edges.
- **Purpose:** Exports the explicit graph representation for downstream network
  analysis, plotting, or external graph tools.
- **Node table reports:** component ID, graph node ID, node type, node degree,
  skeleton voxel index, and spatial coordinates.
- **Edge table reports:** component ID, edge ID, start/end node IDs, branch
  type, branch voxel count, branch edge count, path length, endpoint distance,
  tortuosity, start/end coordinates, and calibrated physical length when scale
  metadata is available.
- **Execution:** manual/cached. This is the most direct table export of the
  skeleton graph.

## Measure Overall Skeleton Network

- **Input:** skeleton mask, or a binary mask if `Input` is set to `Skeletonize
  first`.
- **Output:** table, one row per analyzed spatial block, such as one image,
  timepoint, channel, or slice depending on spatial processing.
- **Purpose:** Measures whole-network topology directly from the skeleton mask.
  This is not just a table summary of `Measure Skeleton Branches`; it computes
  component-level and graph-level metrics that require the original skeleton
  graph.
- **Reports:** component count, skeleton voxel count, largest-component
  fraction, isolated component count, endpoint/junction/isolated-node counts,
  branch and graph-edge counts, cycle count, total skeleton length, branch
  length summaries, mean tortuosity, connectedness fraction, and fragmentation
  index. It also reports normalized connectedness features such as isolated
  component fraction, branches/endpoints/junctions/cycles per component, and
  components/branches/endpoints/junctions/cycles per skeleton length or
  calibrated physical length when available.
- **Use when:** you want one compact feature row per image, timepoint, channel,
  or other spatial block for treatment comparison, PCA-style analysis, or
  mitochondrial connectedness QC.
- **Execution:** manual/cached.

Use `Measure Skeleton Branches -> Summarize Skeleton Branches` when you want
branch-length distributions and branch-type fractions grouped by image,
timepoint, channel, condition, or branch type. Use the generic `Summarize
Measurements` node only when you need custom statistics on arbitrary table
columns. Use `Measure Overall Skeleton Network` when you need network-level
quantities such as connected components, cycles, isolated nodes,
largest-component fraction, and normalized connectedness metrics.

## Skeleton Keypoints

- **Input:** skeleton mask.
- **Output:** three mask outputs: endpoints, junctions, and isolated nodes.
- **Purpose:** Visual QC of graph topology.
- **Use when:** you need to check whether a segmentation/skeletonization step is
  creating too many breaks, junctions, or isolated fragments.

## Skeleton Graph Overlay

- **Input:** skeleton mask.
- **Output:** channel-last RGB image.
- **Purpose:** Visual QC overlay for graph topology in napari.
- **Display modes:** colored edges with colored nodes, colored edges only, or
  white edges with colored nodes.
- **Node colors:** endpoints are green, junctions are magenta, and isolated
  nodes are cyan/blue.
- **Use when:** you want graph branches and nodes to be visually obvious. 2D
  overlays display as one RGB image layer; 3D overlays display as separate
  additive red/green/blue layers so napari can render the colors reliably.

## Label Skeleton Components

- **Input:** skeleton mask.
- **Output:** label image.
- **Purpose:** Assigns a label ID to each connected skeleton component.
- **Use when:** you need to inspect or count disconnected skeleton networks.
- **Identity:** creates new IDs for connected skeleton pieces. This node
  remains available and unchanged; choose **Skeletonize Labels** when the
  output must retain previously segmented object IDs.

## Label Skeleton Branches

- **Input:** skeleton mask.
- **Output:** label image.
- **Purpose:** Assigns label IDs to branch paths between graph nodes.
- **Use when:** you need an inspectable branch map rather than a table.
- **Note:** Junction voxels are deliberately not assigned to branch labels so
  connected branch paths remain visually separable.

## Prune Skeleton Branches

- **Input:** skeleton mask.
- **Output:** binary skeleton mask.
- **Purpose:** Removes short terminal spurs and optional isolated skeleton
  voxels.
- **Key settings:** minimum terminal branch length, length units
  (`Pixels/voxels` or `Physical units`), pruning passes, isolated-voxel removal,
  and 2D/3D spatial processing.
- **Use when:** thresholding or skeletonization creates small terminal artifacts
  that inflate endpoint and branch counts.
- **Physical units:** require pixel-size/axis-scale metadata. If no calibration
  exists, physical-unit pruning behaves like unit spacing.

## Interpreting Graph Terms

- **Endpoint:** skeleton voxel/pixel with one graph neighbor.
- **Junction:** skeleton voxel/pixel with three or more graph neighbors.
- **Isolated node:** foreground skeleton voxel/pixel with no graph neighbors.
- **Branch:** path between two graph nodes, usually endpoint-to-junction,
  junction-to-junction, endpoint-to-endpoint, or a cycle.
- **Tortuosity:** branch path length divided by endpoint-to-endpoint distance.
  A straight branch has tortuosity near 1.

## Common Pitfalls

- Do not feed a thick binary mask into branch-label or keypoint nodes unless you
  intentionally want graph analysis on the thick mask. Usually run
  `Skeletonize` first.
- For anisotropic 3D data, set pixel size / units before measurement so physical
  length columns use the correct z spacing.
- For slice-wise analysis of a stack, explicitly use 2D spatial processing. For
  true volumetric connectedness, use 3D spatial processing.
- If the graph has many tiny branches, inspect the segmentation first, then try
  `Fill Holes`, `Remove Small Objects`, or `Prune Skeleton Branches`.
