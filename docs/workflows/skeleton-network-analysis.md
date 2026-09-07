# Skeleton And Network Analysis

Skeleton workflows analyze curvilinear structures such as mitochondria,
neurites, vessels, fibers, and similar networks.

## Basic QC Workflow

```text
binary mask
  -> Skeletonize
  -> Skeleton Graph Overlay
```

Use the overlay to check endpoints, junctions, isolated voxels, and branch
structure before trusting tables.

## Choose 2D or volumetric 3D skeletonization

Select **Skeletonize** and review both **Spatial processing** and **Method**:

- **Auto from axes** resolves declared `YX` as 2D and declared `ZYX` as one 3D
  volume. An ambiguous `QYX` source is rejected until its page meaning is
  declared.
- **2D YX** processes each leading YX plane independently.
- **3D ZYX** processes each ZYX block once as a volume. For `TZYX`, each time
  point is an independent 3D block; time points are never joined.

Auto chooses Zhang for 2D and Lee for 3D. **Zhang 2D** cannot be combined with
a resolved 3D ZYX volume. The output preserves shape, effective axes,
calibration, and leading dimensions, and its history records the resolved
method and whether processing used a 2D plane or a volumetric block. The 3D
Lee route uses a 3x3x3 neighbourhood with the image boundary treated as
background.

!!! warning "Slice-wise and volumetric results answer different questions"
    Independent YX thinning can change cross-Z connectivity, endpoints,
    junctions, cycles, and branch lengths even when every individual slice
    looks plausible. Use 3D only when Z semantics and spacing are independently
    supported by the acquisition record.

For visual QC, duplicate a representative mask branch and run one Skeletonize
node as **2D YX** and the other as **3D ZYX**. Inspect XY, XZ, and YZ views in
napari, then compare overlays, component counts, endpoints, junctions, and
branch lengths. A bundled synthetic phantom is useful for regression, but it
does not validate a biological segmentation or the acquisition's Z scale.

## Measurement Workflows

Per-component measurements:

```text
binary mask
  -> Skeletonize
  -> Analyze Skeleton
```

Branch-level measurements:

```text
binary mask
  -> Skeletonize
  -> Measure Skeleton Branches
```

Branch summaries:

```text
binary mask
  -> Skeletonize
  -> Measure Skeleton Branches
  -> Summarize Skeleton Branches
```

Whole-network summary:

```text
binary mask
  -> Skeletonize
  -> Measure Overall Skeleton Network
```

Explicit graph tables:

```text
binary mask
  -> Skeletonize
  -> Skeleton Graph Tables
```

## Cleanup Workflow

```text
binary mask
  -> Skeletonize
  -> Prune Skeleton Branches
  -> Analyze Skeleton / Measure Skeleton Branches
```

Pruning removes short terminal spurs and optionally isolated skeleton voxels.

## Reference Workflows

| Workflow | Purpose |
| --- | --- |
| `synthetic-skeleton-qc.json` | Compact 3D skeleton QC with keypoints, branch/component labels, pruning, and tables. |
| `synthetic-advanced-skeleton-network.json` | Time-indexed 3D skeleton/network stress test with loops, fragments, graph tables, and anisotropic scale. |

## What To Check

The [skeleton node reference](../reference/skeleton-nodes.md) lists each node's
outputs, units, graph terms, and pruning behavior.

- Is the input a binary mask or an already skeletonized mask?
- Should analysis be 2D per slice or 3D volumetric?
- Is z-spacing correct before reporting physical lengths?
- Are short spurs biological or threshold/skeletonization artifacts?
- Are endpoint and junction counts plausible in the graph overlay?
