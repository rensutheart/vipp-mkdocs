# Object colocalization and association

Choose the question before choosing a node:

| Question | Node |
| --- | --- |
| Are two intensities related inside each object? | Object Colocalization Metrics |
| Which objects share voxels? | Label Overlap Association |
| Which target centroid is closest? | Nearest Object Distance |
| Which region contains most of an event? | Event Localization |

Inputs must satisfy VIPP's [physical-grid contract](import-export.md#multi-input-grid-safety).
See the [tutorial](../workflows/colocalization-association.md) for graph setup.

## Object-Restricted Colocalization

`Object Colocalization Metrics` accepts a label image and two matching channel
images. Positive label IDs define the objects. Binary label inputs are
converted to connected-component labels per spatial block, so separate
timepoints or channels are not accidentally connected through leading axes.

VIPP processes each leading non-spatial axis independently. For example, a
`TZYX` label image produces rows with `t_index` plus `label_id`. These identity
columns allow object colocalization tables to merge cleanly with `Measure
Objects` and `Measure Objects + Intensity`.

For each label object, VIPP reports the same metric family used by
whole-image/ROI analysis, but restricted to the object's voxels:

- object voxel count;
- threshold-positive voxel counts for each channel;
- colocalized voxel count and fraction;
- Pearson correlation over the object;
- Pearson correlation over the both-channels-at-or-above-threshold
  intersection;
- Manders M1 and M2;
- intensity overlap coefficients;
- threshold-positive and colocalized intensity sums;
- Costes diagnostics when Costes thresholding is used.

Manual thresholds are reused for all objects. Costes thresholds are calculated
once over all labeled foreground voxels, then reused for all objects.

## Label Overlap Association

`Label Overlap Association` accepts two matching label-like images: a
reference label image and a target label image. Binary inputs are converted to
connected-component labels per spatial block. Positive label IDs are treated
as objects; background is zero.

For every reference/target label pair with at least one shared voxel, VIPP
outputs one row with:

- `label_id`: reference label ID;
- `target_label_id`: target label ID;
- `reference_voxels`;
- `target_voxels`;
- `overlap_voxels`;
- `reference_overlap_fraction = overlap_voxels / reference_voxels`;
- `target_overlap_fraction = overlap_voxels / target_voxels`;
- `intersection_over_union = overlap_voxels /
  (reference_voxels + target_voxels - overlap_voxels)`.

The node reports only overlapping pairs. Non-overlapping labels can still be
summarized by combining this table with object measurement tables.

## Nearest-Object Distance

`Nearest Object Distance` accepts reference and target label-like images. For
each reference label, VIPP calculates the centroid of the reference object and
the centroid of each target object using voxel coordinates. It then reports
the nearest target label and the Euclidean centroid-to-centroid distance in
pixels.

When axis scales and physical units are available, VIPP also reports
`centroid_distance_physical`, calculated after multiplying each spatial-axis
coordinate difference by the corresponding physical scale. If no target labels
exist in the spatial block, `nearest_label_id` is `0` and distances are `NaN`.

Nearest-centroid distance is an association heuristic. It does not imply
overlap, containment, or biological interaction without additional context.

## Event Localization

`Event Localization` assigns event or puncta objects to labels, masks, or ROI
regions. The first input defines events. Binary event inputs are converted to
connected-component labels per spatial block, yielding one event row per
connected component. Integer event labels are used directly.

The second input defines regions. Integer labels are used directly. Binary
region masks are treated as a single ROI with region label ID `1`, rather than
as separate connected components.

For each event, VIPP counts the overlap with each positive region label. The
reported `region_label_id` is the region with the largest overlap. Ties are
resolved by the smaller region ID. If the event overlaps no positive region,
`region_label_id` is `0`, `overlap_voxels` is `0`, and `in_region` is `False`.

The table reports:

- `event_id`;
- `event_voxels`;
- `region_label_id`;
- `overlap_voxels`;
- `event_overlap_fraction = overlap_voxels / event_voxels`;
- `in_region`.

This node is suitable for puncta-in-cell, foci-in-nucleus, event-in-ROI, or
similar localization summaries where event objects and region masks/labels are
already defined.

For Pearson, Manders, and Costes fields, use the
[metric definitions and validation boundary](colocalization-metrics.md).
Report label generation, spatial scope, merge keys, and whether association
means overlap, centroid distance, or dominant event-region overlap.
