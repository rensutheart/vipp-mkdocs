# Example Workflows

The release contains **13** example workflows under:

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
| `synthetic-batch-provenance.json` | generated two-source NumPy collection | Three paired items, explicit NPY/TIFF/TSV outputs, representative navigation, saved config/runner, exact ground truth, manifests, archives, and item sidecars. Open it through the chooser and create a writable working copy. |
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

Use `--list` to print the release's exact IDs. In 0.12.0a3 they are:

| ID | Example title |
| --- | --- |
| `batch-provenance` | Deterministic Batch & Provenance |
| `label-cleanup` | Red-Channel Label Cleanup |
| `object-intensity` | Object Intensity Measurements |
| `merged-measurements` | Merged Measurement Table |
| `summary-table` | Grouped Measurement Summary |
| `derived-morphology` | Derived 2D Object Morphology |
| `mesh-morphology` | 3D Mesh Morphology |
| `skeleton-qc` | Skeleton QC |
| `advanced-skeleton` | Advanced Skeleton Network |
| `racc-colocalization` | RACC Colocalization |
| `object-colocalization` | Object Colocalization Association |
| `deconvolution-2d` | 2D Richardson-Lucy / TV Deconvolution |
| `deconvolution-3d` | 3D Richardson-Lucy / TV Deconvolution |

Legacy launcher aliases such as `intensity`, `merged`, and `mesh` remain for
maintainers, but documentation should use the canonical IDs above. An unknown
ID is an error; it does not silently open another example.

## Adding A Core Example Workflow

When adding a new core example:

1. Add a deterministic bundled sample or document the input source.
2. Save workflow JSON under `examples/`.
3. Add a row to this page and the repository example README.
4. Add a launcher shortcut if it is used often.
5. Add a focused test that checks the expected output type and one meaningful
   invariant.
