# Colocalization And Association

VIPP supports pixel, ROI-masked, object-restricted, and label-association
workflows.

## Pixel Colocalization

```mermaid
flowchart LR
  C1["Channel 1"] --> M["Colocalization Metrics"]
  C2["Channel 2"] --> M
  C1 --> V["Colocalized Voxels"]
  C2 --> V
  C1 --> R["RACC Index"]
  C2 --> R
```

Use `Colocalized Voxels` for visual threshold review. Use metric tables for
quantitative reporting. These are parallel consumers of the two channels; none
is the input to the next.

## ROI-Masked Colocalization

```mermaid
flowchart LR
  C1["Channel 1"] --> M["Masked metrics"]
  C2["Channel 2"] --> M
  ROI["ROI mask"] --> M
  C1 --> V["Masked colocalized voxels"]
  C2 --> V
  ROI --> V
  C1 --> R["Masked RACC index"]
  C2 --> R
  ROI --> R
```

Use masked variants when the analysis population should be restricted to cells,
regions, tissue, or user-defined ROIs.

![An undocked VIPP colocalization graph with parallel metrics and image branches and a scatter plot in the inspector](../assets/screenshots/workflows/colocalization-parallel-branches.png)

*The same red/green channel outputs feed independent metric, voxel, and RACC
branches. The selected calculated node exposes its threshold scatter for QC.*

## Object Colocalization

```text
labels + channel 1 + channel 2
  -> Object Colocalization Metrics
```

This produces one row per object and is designed to merge with object
morphology and intensity tables.

## Label Association

Overlap between two object sets:

```text
reference labels + target labels
  -> Label Overlap Association
```

Nearest centroid association:

```text
reference labels + target labels
  -> Nearest Object Distance
```

Event or puncta assignment:

```text
events / puncta + regions / ROIs
  -> Event Localization
```

## Reference Workflows

| Workflow | Purpose |
| --- | --- |
| `synthetic-colocalization-racc.json` | Pixel and ROI-masked metrics, scatter threshold review, colocalized voxels, and RACC-like index output. |
| `synthetic-object-colocalization-association.json` | Object colocalization rows, label overlap, nearest-object distance, event localization, and merged tables. |

## Reporting Checklist

Report:

- channels analyzed;
- preprocessing steps;
- threshold mode and final thresholds;
- analysis population: whole image, ROI, or object labels;
- whether intensities were normalized or clipped;
- 2D/3D and leading-axis handling;
- ROI or label-generation method;
- RACC parameters if using RACC-like outputs.

## Validation Note

The 0.11.0a2 implementation has method documentation and automated tests. Broad
cross-tool or biological validity claims still require deterministic benchmark
packs, external numerical comparisons, and assay-specific validation.
