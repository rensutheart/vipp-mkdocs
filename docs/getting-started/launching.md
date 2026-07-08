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

## Open A Bundled Example

Use the VIPP toolbar:

```text
Open example...
```

The example chooser is grouped by workflow family. It opens a workflow template
and sets its `Image Source` nodes to bundled samples. This is the recommended
route for first-time use and documentation screenshots.

## Optional: Launch With Raw Sample Layers

Use the helper script:

```powershell
python scripts\launch_vipp_sample.py
```

This opens napari with the bundled VIPP synthetic microscopy samples as layers.
Use it when you specifically want to inspect the raw sample data, not when you
only need a runnable example workflow.

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

## Optional: Launch A Review Workflow From The Command Line

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

Inside VIPP, prefer `Open example...` for bundled templates. Use
`Load workflow...` for custom or external workflow JSON files.
