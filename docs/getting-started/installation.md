# Install VIPP

VIPP 0.13.0a1 supports **CPython 3.12 and 3.13**. Because the current release
is a pre-release, pip needs the `--pre` flag to select it from PyPI.

!!! info "Platform and Python verification for 0.13.0a1"
    The base CPU application is intended for Windows, macOS, and Linux. Release
    Release CI targets CPython 3.12 and 3.13 on all three operating systems;
    package metadata deliberately excludes unqualified Python 3.14 and newer.
    CUDA extras are limited to 64-bit CPython 3.12 on native Windows/Linux.
    Treat the commands below as installation paths, not evidence that every
    reader, dataset, display server, GPU, driver, or scientific stack has been
    validated.

## Recommended: a dedicated environment

A separate environment prevents unrelated scientific packages from changing
VIPP's dependencies. The commands below install napari with PyQt6 and the
tagged VIPP release.

=== "Windows"

    ```powershell
    py -3.12 -m venv vipp-env
    .\vipp-env\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    python -m pip install "napari[pyqt6]"
    python -m pip install --pre "napari-vipp==0.13.0a1"
    vipp
    ```

=== "macOS"

    ```bash
    python3.12 -m venv vipp-env
    source vipp-env/bin/activate
    python -m pip install --upgrade pip
    python -m pip install "napari[pyqt6]"
    python -m pip install --pre "napari-vipp==0.13.0a1"
    vipp
    ```

=== "Linux"

    ```bash
    python3.12 -m venv vipp-env
    source vipp-env/bin/activate
    python -m pip install --upgrade pip
    python -m pip install "napari[pyqt6]"
    python -m pip install --pre "napari-vipp==0.13.0a1"
    vipp
    ```

Conda or Mamba environments are also suitable; use Python 3.12 or 3.13 and
activate the environment before running the final
`python -m pip install ...` command.

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
0.13.0a1
```

## Optional NVIDIA CUDA acceleration

The base installation is complete and remains the portable recommendation. A
new session defaults to **Auto**, but Auto uses CPU normally when no admitted
accelerator is present. GPU packages are optional and are not imported merely
to load VIPP or run a CPU workflow.

!!! warning "The first public GPU gate is deliberately narrow"

    The 0.13.0a1 admission evidence covers one exact native-Windows stack:
    64-bit CPython 3.12, NumPy 2.5.1, SciPy 1.18.0, scikit-image 0.26.0,
    CuPy/CuPyX 14.1.1, CUDA runtime API 13.2, driver API 13.3, and the recorded
    RTX 5090/compute-capability-12.0 device. A different GPU, OS, driver,
    runtime, or package set can install successfully and still resolve every
    GPU candidate to CPU because that environment has not passed the release's
    evidence gate. Native Linux and RTX 40-series qualification are pending.

Use a **new** environment and install exactly one CUDA-major extra. For the
current CUDA 13 track:

=== "Windows · CUDA 13"

    ```powershell
    py -3.12 -m venv vipp-gpu-env
    .\vipp-gpu-env\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    python -m pip install --pre "napari[pyqt6]" "napari-vipp[gpu-cuda13]==0.13.0a1"
    vipp-compute-doctor --track cuda13
    vipp
    ```

=== "Linux · CUDA 13"

    ```bash
    python3.12 -m venv vipp-gpu-env
    source vipp-gpu-env/bin/activate
    python -m pip install --upgrade pip
    python -m pip install --pre "napari[pyqt6]" "napari-vipp[gpu-cuda13]==0.13.0a1"
    vipp-compute-doctor --track cuda13
    vipp
    ```

The `gpu-cuda12` extra is a qualification/development track in this alpha; the
current public policy does not admit it. Do not install `gpu-cuda12` and
`gpu-cuda13` into the same environment. A passing import or CUDA kernel probe
does not by itself establish scientific admission for an operation.

`vipp-compute-doctor` reports the selected track, installed packages, runtime
probe, device, and current policy eligibility without asking the GUI to import
a broken accelerator stack. VIPP's **Compute setup and memory…** dialog exposes
the same diagnosis and a copyable fresh-environment repair command. VIPP never
runs that command without the user's action.

cuCIM-backed candidates require a separately reviewed, checksum-recorded build.
There is no general public native-Windows cuCIM extra in 0.13.0a1, and the
validated source-built wheel omits Clara whole-slide I/O. Do not install an
arbitrary cuCIM build and assume it is admitted.

macOS has no CUDA path. Use the base CPU installation on Intel or Apple Silicon;
Metal/MPS/MLX acceleration is a future study, not part of this release.

## Optional microscope readers

The base package supports the documented TIFF, OME-Zarr, NumPy, and ordinary
raster routes. Install only the reader family you need, then restart napari.

| File family | Command |
| --- | --- |
| Nikon ND2 | `python -m pip install --pre "napari-vipp[nd2]==0.13.0a1"` |
| Zeiss CZI | `python -m pip install --pre "napari-vipp[czi]==0.13.0a1"` |
| Mixed microscope formats | `python -m pip install --pre "napari-vipp[microscope]==0.13.0a1"` |
| BioIO/Bio-Formats fallback | `python -m pip install --pre "napari-vipp[bioformats]==0.13.0a1"` |

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

Before upgrading an existing workflow, read
[versions and compatibility](../reference/versioning.md) and preserve the old
environment. Schema-1/2 workflows do not open in 0.13.0a1. Valid schema-3
workflows load structurally with an explicit CPU compute request; saving writes
schema 4. Cached results are not serialized, so recalculate and validate after
upgrading. Version-1 batch configs similarly load as CPU and save as version 2.
Regenerate exported Python too, because it requires the exact VIPP runtime
version that created it.

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
