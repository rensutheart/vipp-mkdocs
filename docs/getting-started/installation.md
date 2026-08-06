# Install VIPP

VIPP 0.13.0a1 supports **CPython 3.12 and 3.13**. The commands below select that
exact alpha with `==0.13.0a1`, so pip's `--pre` option is neither needed nor
desirable: `--pre` affects dependency resolution globally. Use `--pre` only
when asking pip to choose the latest **unpinned** VIPP alpha.

!!! info "Platform and Python verification for 0.13.0a1"
    The base CPU application is intended for Windows, macOS, and Linux. Release
    CI targets CPython 3.12 and 3.13 on all three operating systems;
    package metadata deliberately excludes unqualified Python 3.14 and newer.
    CUDA extras are limited to 64-bit CPython 3.12 on native Windows/Linux.
    Treat the commands below as installation paths, not evidence that every
    reader, dataset, display server, GPU, driver, or scientific stack has been
    validated.

## Recommended: a dedicated environment

A separate environment prevents unrelated scientific packages from changing
VIPP's dependencies. The commands below install napari with PyQt6 and the
tagged 0.13.0a1 alpha release.

=== "Windows"

    ```powershell
    py -3.12 -m venv ".venv-vipp"
    & ".\.venv-vipp\Scripts\python.exe" -m pip install --upgrade pip
    & ".\.venv-vipp\Scripts\python.exe" -m pip install "napari[pyqt6]>=0.6" "napari-vipp==0.13.0a1"
    & ".\.venv-vipp\Scripts\vipp.exe"
    ```

=== "macOS"

    ```bash
    python3.12 -m venv vipp-env
    source vipp-env/bin/activate
    python -m pip install --upgrade pip
    python -m pip install "napari[pyqt6]>=0.6" "napari-vipp==0.13.0a1"
    vipp
    ```

=== "Linux"

    ```bash
    python3.12 -m venv vipp-env
    source vipp-env/bin/activate
    python -m pip install --upgrade pip
    python -m pip install "napari[pyqt6]>=0.6" "napari-vipp==0.13.0a1"
    vipp
    ```

Conda or Mamba environments are also suitable; use Python 3.12 or 3.13 and
activate the environment before running the final
`python -m pip install ...` command.

!!! note "Bounded M1 Max CPU smoke"
    The `e024409` source candidate was manually smoke-tested on one Apple M1
    Max (`arm64`, macOS 26.5.2) for launch, basic processing, batch progress and
    cancellation, and single-budget system-RAM presentation. Focused
    cancellation tests were recorded in follow-up commit `ff21040`. This is not
    a clean-wheel or broad macOS qualification, and it does not provide Apple
    GPU acceleration.

!!! note "Stable manual versus nightly manual"
    In a numbered/stable manual, the commands above install the documented
    release. Nightly documentation can describe newer, unreleased work; do not
    replace the exact version with an arbitrary `main` checkout. See
    [versions and compatibility](../reference/versioning.md).

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
new session defaults to **Auto**. With no exact compatible history, Auto uses
reviewed GPU defaults wherever the installed stack passes every safety gate.
Accelerated-only history makes the next global Auto run measure CPU once on the
same execution surface; a later matching run applies the 1.20x/20-ms gate.
Select **Prefer GPU** to use every reviewed eligible accelerator
regardless of speed, or use Custom/**Find fastest** for per-node control and
measurement. GPU packages are optional and are not imported merely to load VIPP
or run a CPU workflow.

!!! warning "The first public GPU gate is deliberately narrow"

    The 0.13.0a1 admission evidence covers one exact native-Windows stack:
    64-bit CPython 3.12, NumPy 2.5.1, SciPy 1.18.0, scikit-image 0.26.0,
    CuPy/CuPyX 14.1.1, CUDA runtime API 13.2, driver API 13.3, and the recorded
    RTX 5090/compute-capability-12.0 device. A different GPU, OS, driver,
    runtime, or package set can install successfully and still resolve every
    GPU candidate to CPU because that environment has not passed the release's
    evidence gate. Native Linux and RTX 40-series qualification are pending.

    The standard CUDA extra installs the pinned CuPy/CuPyX stack. It does not
    include the separately reviewed cuCIM build used by the background and
    basic measurement candidates. Those nodes remain CPU after the public
    install below unless the user completes the optional pinned local-build
    route.

Use a **new** environment and install exactly one CUDA-major extra. For the
current CUDA 13 track, Windows users should first read the complete
[driver, Python, installation, diagnosis, and cuCIM guide](windows-cuda.md).

=== "Windows · CUDA 13"

    ```powershell
    py -3.12 -m venv ".venv-vipp-gpu-cu13"
    & ".\.venv-vipp-gpu-cu13\Scripts\python.exe" -m pip install --upgrade pip
    & ".\.venv-vipp-gpu-cu13\Scripts\python.exe" -m pip install "napari[pyqt6]>=0.6" "napari-vipp[gpu-cuda13]==0.13.0a1"
    & ".\.venv-vipp-gpu-cu13\Scripts\vipp-compute-doctor.exe" --track cuda13
    & ".\.venv-vipp-gpu-cu13\Scripts\vipp.exe"
    ```

    Only an NVIDIA display driver is a machine-wide prerequisite. The extra
    installs the pinned CUDA user-space libraries; do not separately install a
    CUDA Toolkit, `nvcc`, Visual Studio, or CMake for this standard route.

=== "Linux · CUDA 13 qualification"

    ```bash
    python3.12 -m venv vipp-gpu-env
    source vipp-gpu-env/bin/activate
    python -m pip install --upgrade pip
    python -m pip install "napari[pyqt6]>=0.6" "napari-vipp[gpu-cuda13]==0.13.0a1"
    vipp-compute-doctor --track cuda13
    vipp
    ```

    This creates the intended qualification/development environment, but the
    0.13.0a1 public policy does not yet admit Linux GPU execution. Expect visible
    CPU decisions until native-Linux evidence is promoted in a future policy.

The `gpu-cuda12` extra is a qualification/development track in this alpha; the
current public policy does not admit it. Do not install `gpu-cuda12` and
`gpu-cuda13` into the same environment. A passing import or CUDA kernel probe
does not by itself establish scientific admission for an operation.

`vipp-compute-doctor` reports the selected track, installed packages, runtime
probe, and device without asking the GUI to import a broken accelerator stack.
It does not by itself grant scientific-policy admission. VIPP's **Compute setup
and memory…** dialog exposes the diagnosis and a copyable fresh-environment
repair command, while the operation decision applies the exact environment and
workload gates. VIPP never runs that command without the user's action.

!!! info "cuCIM is an optional local build on Windows"

    VIPP does not distribute or require cuCIM. A Windows user may build exact
    cuCIM 26.6.0 tag `v26.06.00` at the release-pinned commit with VIPP's fixed
    recipe, then use the generated manifest and setup helper to install it into
    this released environment. The helper verifies the archive and canonical
    wheel payload before recording the completed setup; VIPP then independently
    rehashes the installed files before admitting cuCIM for use. The build omits
    Clara whole-slide I/O. Read the
    complete [Windows local-build instructions](windows-cuda.md#build-and-add-the-pinned-cucim-release).

macOS has no CUDA path. Use the base CPU installation on Intel or Apple Silicon;
the bounded M1 Max source-candidate smoke above supports that CPU path but does
not generalize to every Mac. Metal/MPS/MLX acceleration is a future study, not
part of this release.

Continue with [choose and verify CPU or GPU compute](../how-to/choose-compute.md)
for the per-operation matrix, badge meanings, benchmarks, fallback, and durable
provenance.

## Optional microscope readers

The base package supports the documented TIFF, OME-Zarr, NumPy, and ordinary
raster routes. Install only the reader family you need, then restart napari.

| File family | Command |
| --- | --- |
| Nikon ND2 | `python -m pip install "napari-vipp[nd2]==0.13.0a1"` |
| Zeiss CZI | `python -m pip install "napari-vipp[czi]==0.13.0a1"` |
| Mixed microscope formats | `python -m pip install "napari-vipp[microscope]==0.13.0a1"` |
| BioIO/Bio-Formats fallback | `python -m pip install "napari-vipp[bioformats]==0.13.0a1"` |

Support for optional readers is an experimental foundation. A reader exposing
a file is not proof that every axis, unit, timestamp, or acquisition field was
interpreted correctly. Check representative files from your facility before
quantitative use.

## Development branches

Historical candidate commits and artifact hashes are retained in the
[release notes](../releases/0.13.0a1.md) for audit history. They are not
installation targets and must not be uploaded or represented as the final
0.13.0a1 artifacts.

For newer unreleased `main` work, use:

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
upgrading. Version-1 batch configs load as CPU, while version-2 configs retain
their saved compute request. Neither older version contains source-axis
declarations; after review, saving writes batch config version 3. Regenerate
exported Python too, because it requires the exact VIPP runtime version that
created it.

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
