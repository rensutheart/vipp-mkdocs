# Example Workflows

Example workflows are checked into the repository under:

```text
examples/
```

They are intended for regression tests, screenshots, tutorials, and manual
review.

In VIPP, open them with:

```text
Open example...
```

The chooser groups workflows by task and opens each template with its bundled
sample `Image Source` nodes already configured. Use `Load workflow...` for
custom or external workflow JSON files.

## Workflow Index

| Workflow | Input sample | Purpose |
| --- | --- | --- |
| `otsu-red-channel-labels.json` | synthetic multichannel volume | Label cleanup: split the red/TRITC-like channel, blur, Otsu threshold, mask cleanup, connected components, border clearing, and volume filtering. |
| `red-channel-object-intensity-measurements.json` | synthetic multichannel volume | Multi-input object measurement using labels plus matching intensity image. |
| `red-channel-merged-measurement-table.json` | synthetic multichannel volume | Morphology, intensity, table merge, and metadata columns. |
| `synthetic-measurement-summary.json` | synthetic measurement summary | Grouped object-count and area summaries. |
| `synthetic-derived-object-morphology.json` | synthetic object morphology | Derived 2D morphology, circularity, perimeter/area ratio, Hu moments, and column selection. |
| `synthetic-3d-mesh-morphology.json` | synthetic 3D mesh morphology | Surface area, mesh volume, convex hull, sphericity, and tiny-object status. |
| `synthetic-skeleton-qc.json` | synthetic skeleton network | Skeleton keypoints, component/branch labels, pruning, branch tables, graph tables, and network summaries. |
| `synthetic-advanced-skeleton-network.json` | synthetic advanced skeleton network | Time-indexed 3D skeleton graph stress test. |
| `synthetic-colocalization-racc.json` | synthetic colocalization | Pixel and ROI-masked colocalization, scatter thresholds, colocalized voxels, and RACC-like output. |
| `synthetic-object-colocalization-association.json` | synthetic colocalization | Object colocalization, label overlap, nearest distance, event localization, and merged tables. |
| `synthetic-deconvolution-rl-tv.json` | 2D deconvolution image plus measured PSF | 2D measured-PSF restoration with ordinary RL and RL-TV. |
| `synthetic-3d-deconvolution-rl-tv.json` | 3D deconvolution volume plus 3D measured PSF | Volumetric PSF-aware restoration. |

## Launcher Names

Use:

```powershell
python scripts\launch_vipp_intensity_workflow.py <name>
```

Known names:

- `intensity`
- `merged`
- `morphology`
- `mesh`
- `object-coloc`
- `deconvolution`
- `deconvolution-3d`

## Adding A Core Example Workflow

When adding a new core example:

1. Add a deterministic bundled sample or document the input source.
2. Save workflow JSON under `examples/`.
3. Add a row to this page and the repository example README.
4. Add a launcher shortcut if it is used often.
5. Add a focused test that checks the expected output type and one meaningful
   invariant.
