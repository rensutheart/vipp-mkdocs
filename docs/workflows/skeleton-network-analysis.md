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

- Is the input a binary mask or an already skeletonized mask?
- Should analysis be 2D per slice or 3D volumetric?
- Is z-spacing correct before reporting physical lengths?
- Are short spurs biological or threshold/skeletonization artifacts?
- Are endpoint and junction counts plausible in the graph overlay?

