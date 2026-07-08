# Screenshot Plan

Screenshots should be treated as documentation assets and publication assets.

## Screenshot Classes

| Class | Purpose | Style |
| --- | --- | --- |
| Manual screenshot | Help users recognize UI and follow tasks. | Full context, labels in captions. |
| Reference screenshot | Show specific control or node behavior. | Cropped and focused. |
| Publication screenshot | Figure-quality image for papers. | Minimal clutter, high resolution. |
| Regression screenshot | Check visual consistency over time. | Generated from stable workflows. |

## Initial Screenshot Set

| ID | Page | Workflow or sample | Needed view |
| --- | --- | --- | --- |
| `ui-overview` | Home / Launching | sample launch | napari viewer plus VIPP widget |
| `palette-search` | Graph Workflows | any | categorized palette and fuzzy search |
| `first-workflow-graph` | First Workflow | simple labels workflow | graph with thumbnails |
| `threshold-histogram` | Segmentation | Otsu or Binary Threshold | input histogram and marker |
| `label-inspection` | Segmentation | `otsu-red-channel-labels.json` | labels in napari |
| `table-preview` | Measurements | `red-channel-object-intensity-measurements.json` | inspector table preview |
| `mesh-table` | Measurements | `synthetic-3d-mesh-morphology.json` | mesh table and 3D label view |
| `skeleton-overlay` | Skeleton | `synthetic-skeleton-qc.json` | RGB graph overlay |
| `coloc-scatter` | Colocalization | `synthetic-colocalization-racc.json` | scatter threshold panel |
| `object-association` | Colocalization | `synthetic-object-colocalization-association.json` | merged table / association output |
| `deconvolution-comparison` | PSF | `synthetic-deconvolution-rl-tv.json` | blurred, RL, RL-TV comparison |
| `tunnels` | Graph Workflows | skeleton or colocalization workflow | tunnel badges and manager |
| `batch-preview` | Batch | any workflow with `Batch Output` | dry-run batch dialog |

## File Naming

Use:

```text
docs/assets/screenshots/<page>/<short-name>.png
```

Example:

```text
docs/assets/screenshots/workflows/segmentation-label-inspection.png
```

## Capture Rules

- Use the same software release as the docs page.
- Use bundled samples or public data with clear licensing.
- Keep image data non-sensitive.
- Prefer a detached, maximized VIPP window for workflow screenshots.
- Hide the node library once the graph is built unless the palette itself is
  the topic.
- Keep the inspector visible when parameters, histograms, metadata, or table
  previews are part of the teaching point.
- Zoom out enough that the relevant workflow is visible in one screenshot.
- Include the napari viewer only when the viewer output itself is helpful for
  the concept being explained.
- Prefer stable viewport sizes.
- Avoid screenshots that depend on temporary local paths.
- Add captions that state what the user should notice.

## Screenshot Placeholders

Until screenshots are captured, pages should avoid broken image links. Add
screenshots only when the file exists.
