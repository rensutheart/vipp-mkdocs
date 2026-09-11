# Example Workflows

VIPP 0.15.0a4 contains **21** registered example workflows under:

```text
examples/
```

They are intended for regression tests, screenshots, tutorials, and manual
review.

**Unreleased layout refresh:** the full catalogue has been reviewed for clearer
left-to-right flow, separate analysis branches, and readable notes and tunnel
labels. Spacing also allows for the controls shown after calculation. The
examples keep their existing analysis settings and coverage, including the
recent [RACC example settings](../workflows/colocalization-association.md).
Reopen an example from the chooser to use its revised layout; your saved copies
are not rearranged automatically.

!!! note "Catalog updates in 0.15.0a3"
    VIPP 0.15.0a2 shipped 21 examples. 0.15.0a3 retains the saved interactive
    mesh workflow as **Mesh Objects, Colours & Refinement** and removes the
    duplicate entry. It also adds **Separate Overlapping Objects**, combining
    segmentation, binary logic and meshes. The inventory below reflects both changes.

In VIPP, open them with:

```text
Gear menu → Open example…
```

The chooser groups workflows by task and opens each template with its bundled
sample `Image Source` nodes already configured. Use **Open** for
custom or external workflow JSON files.

## Workflow Index

| Workflow | Input sample | Purpose |
| --- | --- | --- |
| `exhaustive-inspector-showcase.json` | seven synthetic-data lanes including the threshold gallery and label-boundary QC | Comprehensive manual review of every palette operation, connected-input summaries, scientific controls, and result sections. Use a focused tutorial for a first workflow; this is a broad inspector acceptance example. |
| `graph-authoring-acceptance.json` | synthetic object morphology | Numbered canvas notes for tunnel insertion, value transfer, graph-fragment copy/paste, group movement, one-step undo/redo, and a qualified GPU dtype repair. Its deliberately loose demonstration fragments are not calculated. |
| `responsive-volume-crop-acceptance.json` | synthetic time-lapse multichannel | Numbered TCZYX checks for explicit-Z crop margins, immediate 2D/3D ROI feedback, one committed calculation and undo gesture, preserved T/C and physical origins, QYX safety, and truthful CPU/GPU status. |
| `safe-node-bypass-acceptance.json` | synthetic volume | Focused Crop Stack checks for exact pass-through data, would-run thumbnails, bypass styling, undo/save/export, GPU-neutral status, and batch Run/Bypass profiles. |
| `general-node-bypass-acceptance.json` | synthetic deconvolution image plus measured PSF | Generalized unary and multi-input bypass checks, including RL-TV forwarding Image port 0 while retaining but ignoring its PSF input and refusing unsafe boundaries. |
| `synthetic-batch-provenance.json` | generated two-source NumPy collection | Three paired items, explicit NPY/TIFF/TSV outputs, representative navigation, saved config/runner, exact ground truth, manifests, archives, and item sidecars. Open it through the chooser and create a writable working copy. |
| `otsu-red-channel-labels.json` | synthetic multichannel volume | Label cleanup: split the red/TRITC-like channel, blur, Otsu threshold, mask cleanup, connected components, border clearing, and volume filtering. |
| `synthetic-separate-overlapping-objects.json` | synthetic volume | [Separate overlapping objects](../workflows/separate-overlapping-objects.md): compare intensity masks, reconstruct a curve with XOR/OR and morphology, then create, measure and colour two meshes. Six notes explain the saved sample-specific choices. |
| `synthetic-gpu-segmentation-bridge.json` | synthetic GPU segmentation cleanup | Annotated portable path through Extract Channel, exact float32 Preserve conversion, Gaussian Blur, fixed Binary Threshold, Boolean Remove Small Objects and Fill Holes, and 3D Connected Components. Unsupported GPU regions fall back visibly to CPU. |
| `red-channel-object-intensity-measurements.json` | synthetic multichannel volume | Multi-input object measurement using labels plus matching intensity image. |
| `red-channel-merged-measurement-table.json` | synthetic multichannel volume | Morphology, intensity, table merge, and metadata columns. |
| `synthetic-measurement-summary.json` | synthetic measurement summary | Grouped object-count and area summaries. |
| `synthetic-derived-object-morphology.json` | synthetic object morphology | Derived 2D morphology, circularity, perimeter/area ratio, Hu moments, and column selection. |
| `synthetic-3d-mesh-morphology.json` | synthetic 3D mesh morphology | Surface area, mesh volume, convex hull, sphericity, and tiny-object status. |
| `synthetic-mesh-objects.json` | synthetic 3D mesh morphology | Saved interactive workflow with five split objects, Turbo colours by triangle count, two smoothing iterations at strength 1, and a target of 10% of triangles kept at aggressiveness 4. These are sample-specific choices; compare geometry and measurements before reuse. |
| `synthetic-skeleton-qc.json` | synthetic skeleton network | Skeleton keypoints, component/branch labels, pruning, branch tables, graph tables, and network summaries. |
| `synthetic-advanced-skeleton-network.json` | synthetic advanced skeleton network | Time-indexed 3D skeleton graph stress test. |
| `synthetic-colocalization-racc.json` | synthetic colocalization | Pixel and ROI-masked colocalization, scatter thresholds, colocalized voxels, and RACC-like output. |
| `synthetic-object-colocalization-association.json` | synthetic colocalization | Object colocalization, label overlap, nearest distance, event localization, and merged tables. |
| `synthetic-deconvolution-rl-tv.json` | 2D deconvolution image plus measured PSF | 2D measured-PSF restoration with ordinary RL and RL-TV. |
| `synthetic-3d-deconvolution-rl-tv.json` | 3D deconvolution volume plus 3D measured PSF | Volumetric PSF-aware restoration with one shared visible float32 Preserve conversion feeding both 25-iteration branches at the authored `1e-12` filter epsilon. |

## Launcher Names

Use:

```powershell
python scripts\launch_vipp_intensity_workflow.py <name>
```

Use `--list` to print your version's exact IDs. In 0.15.0a4 they are:

| ID | Example title |
| --- | --- |
| `exhaustive-inspector` | Exhaustive Inspector Showcase |
| `graph-authoring` | Graph Editing Acceptance Check |
| `responsive-crop` | Responsive Volumetric Crop Acceptance |
| `safe-node-bypass` | Safe Node Bypass Acceptance |
| `general-node-bypass` | General Node Bypass Acceptance |
| `batch-provenance` | Deterministic Batch & Provenance |
| `label-cleanup` | Red-Channel Label Cleanup |
| `separate-overlapping-objects` | Separate Overlapping Objects |
| `gpu-segmentation` | Portable GPU Segmentation Bridge |
| `object-intensity` | Object Intensity Measurements |
| `merged-measurements` | Merged Measurement Table |
| `summary-table` | Grouped Measurement Summary |
| `derived-morphology` | Derived 2D Object Morphology |
| `mesh-morphology` | 3D Mesh Morphology |
| `mesh-objects` | Mesh Objects, Colours & Refinement |
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
