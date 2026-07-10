# Install VIPP

VIPP 0.11.0a1 requires **Python 3.10 or newer**. Because the current release is
a pre-release, pip needs the `--pre` flag to select it from PyPI.

## Recommended: a dedicated environment

A separate environment prevents unrelated scientific packages from changing
VIPP's dependencies. The commands below install napari with PyQt6 and the
tagged VIPP release.

=== "Windows PowerShell"

    ```powershell
    py -3.12 -m venv vipp-env
    .\vipp-env\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    python -m pip install "napari[pyqt6]"
    python -m pip install --pre napari-vipp
    napari
    ```

=== "macOS / Linux"

    ```bash
    python3.12 -m venv vipp-env
    source vipp-env/bin/activate
    python -m pip install --upgrade pip
    python -m pip install "napari[pyqt6]"
    python -m pip install --pre napari-vipp
    napari
    ```

If `python3.12` is unavailable, use any installed Python from 3.10 onward.
Conda or Mamba environments are also suitable; activate the environment before
running the final `python -m pip install ...` command.

!!! note "Stable manual versus nightly manual"
    The commands above install the release documented by this version of the
    site. Do not install the development branch just because you are reading
    the nightly manual. See [versions and compatibility](../reference/versioning.md).

## Confirm the installation

After napari opens:

1. Choose **Plugins → VIPP Workflow (napari-vipp)**.
2. In VIPP, choose **Open example…**.
3. Confirm that the example chooser appears.
4. Compare the version shown by VIPP with the version selector in this manual.

For a command-line check:

```text
python -c "import importlib.metadata as m; print(m.version('napari-vipp'))"
```

Expected for this release:

```text
0.11.0a1
```

## Optional microscope readers

The base package supports the documented TIFF, OME-Zarr, NumPy, and ordinary
raster routes. Install only the reader family you need, then restart napari.

| File family | Command |
| --- | --- |
| Nikon ND2 | `python -m pip install --pre "napari-vipp[nd2]"` |
| Zeiss CZI | `python -m pip install --pre "napari-vipp[czi]"` |
| Mixed microscope formats | `python -m pip install --pre "napari-vipp[microscope]"` |
| BioIO/Bio-Formats fallback | `python -m pip install --pre "napari-vipp[bioformats]"` |

Support for optional readers is an experimental foundation. A reader exposing
a file is not proof that every axis, unit, timestamp, or acquisition field was
interpreted correctly. Check representative files from your facility before
quantitative use.

## Install the development branch

Use this only for testing unreleased work:

```text
python -m pip install --upgrade "napari[pyqt6]" "https://github.com/rensutheart/napari-vipp/archive/refs/heads/main.zip"
```

Development workflows may not reopen in a stable alpha release. Record the
commit hash as well as the package version if results depend on an unreleased
build.

## Developer installation

Contributors should clone the application repository and install it editable:

```powershell
git clone https://github.com/rensutheart/napari-vipp.git
cd napari-vipp
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
```

Continue with the [development setup](../developer/development-setup.md).
