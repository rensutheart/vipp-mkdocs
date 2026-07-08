# Installation

## Recommended Local Development Install

From the `napari-vipp` repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install -e ".[dev]"
```

Validate the plugin manifest and tests:

```powershell
python -m npe2 validate src/napari_vipp/napari.yaml
python -m pytest
```

## Optional File-Format Extras

The base package supports OME-TIFF, ImageJ TIFF, conventional TIFF, OME-Zarr,
NumPy, and common 2D raster images.

Optional microscope readers are separated into extras so the core install stays
lighter:

```powershell
python -m pip install -e ".[microscope]"
```

Use optional reader support cautiously until specific file formats have been
validated against real microscope files from your facility.

## Development Status

The current public baseline is the 0.10 alpha line. Some restoration,
deconvolution, and microscope import features are implemented in the working
tree and should be documented as experimental unless they are included in the
release being used.

