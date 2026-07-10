# Common Pitfalls

## Manual And Manual Version Differ

Symptom:

- a control, node, parameter, or workflow in the manual is absent or renamed;
- a saved workflow opens differently.

Fix:

- compare the VIPP version badge with the manual's version selector;
- use the numbered manual matching the plugin;
- migrate a copy of an alpha workflow and compare it with known sample outputs.

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

## Source Does Not Change The Workflow

Symptom:

- changing a layer in napari does not visibly change the graph output;
- the status still reports that the graph updated from the old sample or file.

Check:

- select the graph's `Image Source` node;
- inspect whether `Source` is set to `napari layer`, `sample`, or `file path`;
- if `Source` is `napari layer`, choose the desired layer in the node inspector;
- if `Source` is `sample` or `file path`, change the sample or file path there.

## File Opens With Wrong Axes Or Scale

Symptom:

- z appears as time or channel;
- physical measurements are implausible;
- a reader opens the wrong series.

Fix:

- inspect source metadata and acquisition records;
- select the intended series/store group;
- use `Reorder Axes` or `Set Pixel Size / Units` only with known values;
- reproduce the issue with a non-sensitive minimal file before reporting it.

## Exported Workflow Is Not A Complete Archive

Symptom:

- another computer cannot find source files;
- generated Python differs from interactive display/caching;
- batch pairing cannot be reconstructed from JSON alone.

Fix:

- read the [workflow and export contract](../reference/workflow-contract.md);
- share an environment and input manifest with the workflow;
- preserve batch bindings, pairings, exclusions, and output checksums separately.
