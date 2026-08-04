# Common Pitfalls

## Manual And Manual Version Differ

Symptom:

- a control, node, parameter, or workflow in the manual is absent or renamed;
- a saved workflow opens differently.

Fix:

- compare the VIPP version badge with the manual's version selector;
- use the numbered manual matching the plugin;
- recreate a copy of an alpha workflow and compare it with known sample
  outputs. Schema-1/2 files cannot be migrated by changing the JSON version.

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

For an ND2 file in 0.13, compare the reported ordered shape/axes with the
reader/acquisition record and move every available T, Z, and C slider. Each
control should change the corresponding content in both napari and the linked
VIPP preview. VIPP trusts the reader's ordered dimensions only when their labels
and sizes exactly match the array; otherwise it falls back conservatively. Do
not use `Reorder Axes` as a blind visual repair. If controls remain absent or
move the wrong content, report a minimal non-sensitive file plus reader and VIPP
versions.

## Auto Or Selective Still Shows CPU

For **Auto**, CPU is expected in the standard 0.13.0a1 interfaces: calculation
does not attach local timing evidence, and Auto does not benchmark implicitly.
Use Selective and apply a reviewed provider or **Find fastest** proposal when
GPU execution is intended.

For **Selective**, CPU can still be the only scientifically admitted result for
the exact dtype, parameters, shape, memory, provider, or environment, or it can
be an amber visible fallback from a forced GPU choice. Read the node badge and
decision reason, then run **Compute setup and memory…**. The standard CUDA extra
does not include the separately reviewed cuCIM build used by background and
basic measurement candidates. See
[choose and verify compute](../how-to/choose-compute.md).

## Optimizer Progress Appears Stationary

The current-operation bar advances only at truthful checkpoints. A monolithic
CPU/GPU library call can stay at one percentage until it returns. Cancelling is
also cooperative at those boundaries. If the time limit is reached, read which
comparisons completed and remain: budget exhaustion means the search is
incomplete, not that the current assignment was proved optimal. Exact completed
records can be reused on retry.

## Source Changed But VIPP Keeps The Earlier Revision

Symptom:

- a file was overwritten in place, but the graph still shows the verified
  earlier bytes; or
- calculation reports that a source revision changed.

Fix:

- this is the stable-source contract, not an implicit reload failure;
- finish/archive the current revision or select **Refresh** to accept the new
  file/layer state deliberately;
- preview a batch again after any source change.

## Same Shape But Inputs Are Rejected

Symptom:

- a multi-image, mask/image, or image/PSF node reports incompatible grids even
  though array shapes match.

Check semantic axes, scale, units, and origin. Equal shape does not prove
physical alignment. Register/resample explicitly with a justified method; do
not remove calibration merely to bypass the safety check.

## Batch Plan Became Stale

Symptom:

- Run refreshes the preview and stops; or
- representative navigation remains available but the plan is labelled stale.

The graph, setup, sources, destinations, output declarations, or collision state
changed since review. Inspect the new full plan, navigate representatives again
when relevant, then run only after the fresh preflight is acceptable.

## Exported Workflow Is Not A Complete Archive

Symptom:

- another computer cannot find source files;
- exported Python will not run under a different VIPP version;
- batch pairing cannot be reconstructed from workflow JSON alone.

Fix:

- read the [workflow and export contract](../reference/workflow-contract.md);
- share an environment and input manifest with the workflow;
- preserve `vipp_batch_config.json`, the workflow companion, finalized
  manifests/archives, sidecars, exclusions, and output checksums.
