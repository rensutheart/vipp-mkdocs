# Inspection Model

The point of VIPP is not only to run a pipeline. It is to make each processing
decision inspectable.

## Inspection Surfaces

| Surface | Use |
| --- | --- |
| Node thumbnail | Quick scan of what each stage is doing. |
| Napari inspect layer | Full-resolution inspection of the selected node output. |
| Pinned layer | Keep important outputs visible while editing other nodes. |
| Histogram panel | Check intensity distributions and threshold choices. |
| Input histogram | Review cutoffs for threshold-like nodes. |
| Label-volume histogram | Tune label filtering against the incoming object-size distribution. |
| Table preview | Check measurement columns, row count, and units before export. |
| Graph notes | Record why a parameter or branch exists. |

## Recommended Inspection Sequence

For segmentation:

1. Inspect the raw channel.
2. Inspect background correction or denoising.
3. Inspect the threshold mask.
4. Inspect label IDs.
5. Inspect measurement tables.
6. Save the workflow only after the intermediate stages make sense.

For colocalization:

1. Inspect both channels separately.
2. Inspect the ROI mask if used.
3. Inspect scatter/threshold guides.
4. Inspect colocalized voxels.
5. Inspect metric tables.

For skeletons:

1. Inspect the binary mask.
2. Inspect the skeleton.
3. Inspect keypoints or graph overlay.
4. Inspect branch/component labels.
5. Inspect measurement tables.

