# Workflow Screenshots

This gallery collects screenshots from real VIPP workflows.

## First Label-Cleanup Workflow

![First VIPP workflow overview](../assets/screenshots/getting-started/first-workflow-overview.png)

Source workflow:

```text
examples/otsu-red-channel-labels.json
```

What the screenshot shows:

- detached, maximized VIPP window;
- hidden node library to give the graph more room;
- graph zoomed out to show the full workflow;
- graph canvas with node thumbnails;
- channel splitting, thresholding, hole filling, connected components, and
  label filtering;
- selected-node inspector for `Filter Labels By Volume`.

Use this screenshot in:

- [First Workflow](../getting-started/first-workflow.md)
- [Segmentation And Label Cleanup](../workflows/segmentation-label-cleanup.md)
- future system-paper figure drafts.

## Planned Screenshot Gallery

| Workflow | Screenshot target |
| --- | --- |
| `red-channel-object-intensity-measurements.json` | Labels plus intensity image feeding a table node. |
| `red-channel-merged-measurement-table.json` | Table merge and metadata columns. |
| `synthetic-3d-mesh-morphology.json` | 3D label output and mesh morphology table. |
| `synthetic-skeleton-qc.json` | Skeleton graph overlay and branch/keypoint QC. |
| `synthetic-colocalization-racc.json` | Scatter threshold panel and colocalized-voxel output. |
| `synthetic-object-colocalization-association.json` | Object association table and merged metrics. |
| `synthetic-deconvolution-rl-tv.json` | Blurred input, ordinary RL, and RL-TV comparison. |
| Batch workflow | Batch preview dialog and explicit `Batch Output` nodes. |
