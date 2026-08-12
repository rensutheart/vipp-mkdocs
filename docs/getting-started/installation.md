# Install VIPP

## Windows installer — recommended

For Windows, use the signed VIPP installer. It creates and maintains a private
VIPP environment, so you do not need to activate Python or choose individual
packages.

**[Download VIPP 0.13.0a5 for Windows](https://github.com/rensutheart/napari-vipp/releases/download/v0.13.0a5/VIPP-Setup-0.13.0a5-Windows-x86_64.exe)**

!!! warning "Use only the official signed file"
    Download `VIPP-Setup-0.13.0a5-Windows-x86_64.exe` only from the
    [official v0.13.0a5 GitHub release](https://github.com/rensutheart/napari-vipp/releases/tag/v0.13.0a5).
    Windows should report a valid VIPP publisher signature. The release also
    includes its SHA-256 checksum and release manifest. Do not use a similarly
    named file from another site.

### Before you start

- Use 64-bit Windows.
- Install a supported 64-bit Python. CPython 3.12.10 works for both CPU and
  NVIDIA GPU setup; CPython 3.13 is also supported for CPU.
- Keep an internet connection available during the first installation.
- For NVIDIA GPU use, install a sufficiently recent NVIDIA display driver.
  A separate CUDA Toolkit, Visual Studio, CMake, and `nvcc` are not required.

If Python is missing, setup links to the official
[Python 3.12.10 Windows release](https://www.python.org/downloads/release/python-31210/)
and lets you check again after installing it.

### Install

1. Double-click the downloaded `.exe`.
2. Keep **Automatic** for the simplest choice. Setup recommends CPU or a
   qualified NVIDIA CUDA 13 installation from the computer it finds.
3. To choose manually, expand **Advanced details**, then use **Computer use**
   to select **CPU** or **NVIDIA GPU**. An unavailable GPU route stays blocked
   and explains what is missing.
4. Under **Reviewed settings**, confirm the installation location, compute
   route, and whether to add a Desktop shortcut.
5. Select **Install** and wait for setup and its final acceptance checks.
6. Open **VIPP** for a CPU installation. A CUDA installation provides
   **VIPP Automatic**, **VIPP CPU**, and **VIPP Prefer GPU** shortcuts; begin
   with **VIPP Automatic**.

Changing the compute choice, location, or Desktop-shortcut choice requires
**Check these settings** again. Setup never enables **Install** for settings it
has not checked.

GPU setup is a large download. It currently needs at least 15 GiB free on the
installation drive while setup runs; that is disk storage, not GPU memory
(VRAM). It also needs at least 5 GiB free on every drive used for Windows
temporary files and VIPP installer records. CPU setup needs at least 1 GiB in
those temporary/record locations. Setup identifies the exact location when a
check fails.

The network-idle timeout is 120 seconds, not a total installation-time limit.
After a temporary connection failure, the incomplete candidate is rolled back
and any previous working VIPP remains active. Choose **Try again** after the
connection recovers, review the current settings, and install again.

### Update, repair, or remove

The installer does not silently replace an existing installation:

- an older installer-owned copy is offered as **Update** and remains usable
  until the replacement passes acceptance;
- rerunning the same version offers **Open VIPP** and **Repair**;
- a newer version is not downgraded;
- unrelated folders and manually managed napari environments are never
  overwritten; and
- managed CPU and CUDA installations can coexist.

Remove either installation from **Windows Settings → Apps → Installed apps**.
Each entry has its own ownership-bound uninstaller, so removing CPU does not
remove CUDA and removing CUDA does not remove CPU.

## Linux, macOS, and advanced manual installation

VIPP 0.13.0a5 supports CPython 3.12 and 3.13 for CPU use. Create a dedicated
environment, then install the exact alpha. An exact prerelease pin does not
need pip's `--pre` option.

=== "Windows manual"

    ```powershell
    py -3.12 -m venv ".venv-vipp"
    & ".\.venv-vipp\Scripts\python.exe" -m pip install --upgrade pip
    & ".\.venv-vipp\Scripts\python.exe" -m pip install "napari[pyqt6]>=0.6" "napari-vipp==0.13.0a5"
    & ".\.venv-vipp\Scripts\vipp.exe"
    ```

=== "macOS"

    ```bash
    python3.12 -m venv vipp-env
    source vipp-env/bin/activate
    python -m pip install --upgrade pip
    python -m pip install "napari[pyqt6]>=0.6" "napari-vipp==0.13.0a5"
    vipp
    ```

=== "Linux"

    ```bash
    python3.12 -m venv vipp-env
    source vipp-env/bin/activate
    python -m pip install --upgrade pip
    python -m pip install "napari[pyqt6]>=0.6" "napari-vipp==0.13.0a5"
    vipp
    ```

macOS is CPU-only in this alpha. Native Linux GPU qualification is not yet
public; Linux remains on the CPU path even if CUDA packages import.

Installing into an existing napari environment is an advanced route. Use that
environment's Python explicitly and keep the VIPP version pinned. Do not use a
global Python, an environment that exposes system site-packages, an editable
VIPP checkout, or an environment with multiple Qt bindings.

## Confirm the installation

For an installer-managed copy, open the created VIPP shortcut and choose
**Open example…**. For a manually managed environment, you can also run:

```text
python -c "import importlib.metadata as m; print(m.version('napari-vipp'))"
```

Expected for this release:

```text
0.13.0a5
```

Inside napari, choose **Plugins → VIPP Workflow (napari-vipp)**.

## Optional NVIDIA CUDA acceleration

The Windows installer is the recommended GPU path. The standard CUDA setup
installs its pinned CUDA libraries inside the managed VIPP environment and
works without cuCIM.

VIPP admits a successfully probed NVIDIA CUDA device only when every released
gate passes: native 64-bit Windows, CPython 3.12, compute capability 7.5 or
newer, driver API 13.3 or newer, CUDA runtime API 13.2, the pinned scientific
and CuPy/CuPyX packages, provider probes, memory, workload, and scientific
parity. GPU names are recorded for provenance rather than used as an allowlist.
Unsupported work stays on CPU with an explanation.

For a manual CUDA environment:

```powershell
py -3.12 -m venv ".venv-vipp-gpu-cu13"
& ".\.venv-vipp-gpu-cu13\Scripts\python.exe" -m pip install --upgrade pip
& ".\.venv-vipp-gpu-cu13\Scripts\python.exe" -m pip install "napari[pyqt6]>=0.6" "napari-vipp[gpu-cuda13]==0.13.0a5"
& ".\.venv-vipp-gpu-cu13\Scripts\vipp-compute-doctor.exe" --track cuda13
& ".\.venv-vipp-gpu-cu13\Scripts\vipp.exe"
```

Read the complete [Windows CUDA and optional cuCIM guide](windows-cuda.md)
before adding GPU packages manually. The separate cuCIM release bundle builds
the pinned source locally and contains no redistributable cuCIM wheel.

## Optional microscope readers

Install an optional reader with the Python from the exact environment that
launches VIPP, then restart napari.

| File family | Command |
| --- | --- |
| Nikon ND2 | `python -m pip install "napari-vipp[nd2]==0.13.0a5"` |
| Zeiss CZI | `python -m pip install "napari-vipp[czi]==0.13.0a5"` |
| Mixed microscope formats | `python -m pip install "napari-vipp[microscope]==0.13.0a5"` |
| BioIO/Bio-Formats fallback | `python -m pip install "napari-vipp[bioformats]==0.13.0a5"` |

A reader opening a file is not proof that every axis, unit, timestamp, or
acquisition field was interpreted correctly. Check representative facility
files before quantitative use.

## Development installation

Contributors should clone the application repository and install it editable:

```powershell
git clone https://github.com/rensutheart/napari-vipp.git
cd napari-vipp
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
```

Development workflows may not reopen in a stable alpha. Record the application
commit as well as the package version, and continue with the
[development setup](../developer/development-setup.md).
