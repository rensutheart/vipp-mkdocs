# Colocalization And Association

VIPP supports pixel, ROI-masked, object-restricted, and label-association
workflows.

## Pixel Colocalization

```text
channel 1 + channel 2
  -> Colocalization Metrics
  -> Colocalized Voxels
  -> RACC Index
```

Use `Colocalized Voxels` for visual threshold review. Use metric tables for
quantitative reporting.

## ROI-Masked Colocalization

```text
channel 1 + channel 2 + ROI mask
  -> Masked Colocalization Metrics
  -> Masked Colocalized Voxels
  -> Masked RACC Index
```

Use masked variants when the analysis population should be restricted to cells,
regions, tissue, or user-defined ROIs.

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

The current implementation has method documentation and automated tests. A
future validation report should add deterministic overlap scenarios and
external numerical comparisons before making broad claims.

