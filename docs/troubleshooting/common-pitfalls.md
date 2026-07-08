# Common Pitfalls

## Wrong Channel

Symptom:

- segmentation finds objects in the wrong signal;
- colocalization metrics are meaningless;
- measurement intensity looks too low or too high.

Check:

- `Split Channels` output labels;
- channel names and colors;
- selected `Extract Channel` index;
- RGB images versus true multichannel fluorescence arrays.

## 2D Versus 3D Processing

Symptom:

- objects are connected through z when they should not be;
- skeletons break unexpectedly;
- counts differ between slice and volume interpretation.

Check:

- spatial processing setting;
- axes shown in metadata;
- whether the input is `YX`, `ZYX`, `CZYX`, or `TCZYX`.

## Missing Or Wrong Pixel Size

Symptom:

- physical area, volume, length, or surface values are wrong;
- anisotropic z-stack projections look distorted;
- skeleton length in physical units is not meaningful.

Fix:

- use `Set Pixel Size / Units`;
- inspect metadata before measurement;
- confirm z-step separately from x/y pixel size.

## Mask Versus Labels

Symptom:

- object measurements fail or produce unexpected rows;
- labels are merged or renumbered unexpectedly;
- table joins do not match objects.

Check:

- masks are foreground/background;
- labels are integer object IDs;
- `Label Connected Components` has been run before object measurement;
- `Relabel Sequential` is only used when compact IDs are desired.

## Blind Pipeline Transfer

Symptom:

- a workflow tuned on one dataset oversegments or undersegments another;
- noise becomes objects;
- total object count changes by orders of magnitude.

Fix:

- inspect intermediate outputs on every new dataset family;
- retune thresholds and cleanup nodes;
- compare masks and labels before trusting measurements.

## Manual Nodes Not Updating

Symptom:

- table looks stale after upstream changes.

Fix:

- select the node and click `Recalculate`;
- use toolbar `Calculate all`;
- enable `Auto Recalculate` only if the node is fast enough.

## Toolbar Input Does Not Change The Workflow

Symptom:

- selecting another item in the toolbar `Input` dropdown does not visibly change
  the graph output;
- the status still reports that the graph updated from the old sample or file.

Check:

- select the graph's `Image Source` node;
- inspect whether `Source` is set to `sample` or `file path`;
- change the source in the `Image Source` inspector controls, not only in the
  toolbar dropdown.

The toolbar `Input` dropdown is mainly the default/current napari-layer selector.
An explicit `Image Source` node can override it.
