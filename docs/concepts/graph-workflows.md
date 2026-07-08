# Graph Workflows

The graph is the visible record of a VIPP analysis.

Each node performs one operation. Each connection says which output feeds which
input. Parameters are adjusted in the inspector, and node outputs can be viewed
as thumbnails, napari layers, histograms, labels, or tables.

## Core Graph Features

| Feature | Use |
| --- | --- |
| Typed ports | Prevent images, masks, labels, and tables from being mixed accidentally. |
| Multi-input nodes | Express operations such as labels plus intensity image, image plus PSF, or two-channel colocalization. |
| Multi-output nodes | Split channels, split axes, skeleton keypoints, or graph tables into separate outputs. |
| Named tunnels | Reuse a source such as a channel, mask, ROI, or reference image without drawing long wires. |
| Graph notes | Record reasoning next to workflow steps. |
| Graph search | Find nodes, operation IDs, tunnel names, and batch output tags. |
| Workflow JSON | Save the graph, node parameters, connections, canvas positions, tunnels, and selected UI state. |
| Python export | Generate a runnable headless script from the graph. |

## Good Graph Habits

- Keep the source image and key masks inspectable.
- Use tunnels when a channel, mask, ROI, or reference image feeds many nodes.
- Add graph notes at scientific decision points.
- Detach and maximize VIPP for longer workflows.
- Hide the node library after building the graph when you need more canvas
  space.
- Zoom out for whole-workflow review, then zoom in for parameter tuning.
- Add explicit `Batch Output` nodes before running a workflow over a folder.
- Save workflow snapshots before major parameter sweeps.

## Avoid

- Treating the final table as trustworthy without inspecting masks and labels.
- Reusing a workflow on structurally different data without retuning.
- Hiding scientific decisions in file names or external notes only.
