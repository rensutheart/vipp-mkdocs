# Launching VIPP

## Launch Napari And Open The Widget

Activate the environment and start napari:

```powershell
.\.venv\Scripts\activate
napari
```

Open the workflow widget from:

```text
Plugins > VIPP Workflow (napari-vipp)
```

## Launch With Sample Data

Use the helper script:

```powershell
python scripts\launch_vipp_sample.py
```

This opens napari with the bundled VIPP synthetic microscopy samples.

## Recommended Workspace

For serious workflow building, detach the VIPP widget from napari and maximize
it. The graph is the main work surface, and a full-size VIPP window makes
connections, thumbnails, tunnels, notes, and inspector controls much easier to
read.

Practical layout tips:

- hide the node library after the graph is built to give the canvas more room;
- keep the inspector visible while tuning parameters;
- zoom the graph out when documenting or reviewing the whole workflow;
- show the napari viewer only when the image layer itself is part of the point.

## Launch A Review Workflow

Example:

```powershell
python scripts\launch_vipp_intensity_workflow.py merged
```

Common launcher names include:

- `intensity`
- `merged`
- `morphology`
- `mesh`
- `object-coloc`
- `deconvolution`
- `deconvolution-3d`

You can also load workflow JSON files from the VIPP toolbar with
`Load workflow...`.
