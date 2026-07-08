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

