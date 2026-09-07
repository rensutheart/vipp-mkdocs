# Install VIPP

## Windows installer — recommended

For Windows, use the VIPP installer. It creates and maintains a private
VIPP environment, so you do not need to activate Python or choose individual
packages.

**[Check the official VIPP releases](https://github.com/rensutheart/napari-vipp/releases)**

!!! warning "Use only the exact qualified 0.15.0a1 files"
    The `v0.15.0a1` prerelease carries the installers, checksums, wheel, and
    source archive on the
    [official release page](https://github.com/rensutheart/napari-vipp/releases/tag/v0.15.0a1).
    The release manifest identifies the exact immutable tag and embedded wheel.
    Do not use a similarly named file from another site.

!!! warning "Unsigned alpha — verify before running"
    Download
    `VIPP-Setup-0.15.0a1-Windows-x86_64-UNSIGNED.exe` only from the official
    `v0.15.0a1` entry on the
    [VIPP GitHub releases page](https://github.com/rensutheart/napari-vipp/releases).
    This alpha is intentionally not Authenticode-signed, so Windows will report
    **Unknown publisher**. The `-UNSIGNED` filename is intentional. Do
    not use a similarly named file from another site.

### Verify the download and pass the Windows warning

1. Download the installer and
   `SHA256SUMS-Windows-0.15.0a1.txt` from the same
   official GitHub release.
2. Open PowerShell in the download folder and run:

    ```powershell
    Get-FileHash -Algorithm SHA256 `
      .\VIPP-Setup-0.15.0a1-Windows-x86_64-UNSIGNED.exe
    ```

3. Compare the full 64-character result with the line for the installer in
   `SHA256SUMS-Windows-0.15.0a1.txt`. If it differs, stop and delete the file.
4. Double-click the installer. At **Windows protected your PC**, choose **More
   info**, check that the app name ends in `-UNSIGNED.exe` and the publisher is
   **Unknown publisher**, then choose **Run anyway**.

Do not continue if Microsoft Defender or another antivirus identifies a
threat, and never disable Windows security. Work/school policy or Windows 11
Smart App Control may block unsigned applications without a **Run anyway**
choice; use the manual installation below in that case.

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

1. Keep **Automatic** for the simplest choice. Setup recommends CPU or a
   qualified NVIDIA CUDA 13 installation from the computer it finds.
2. To choose manually, expand **Advanced details**, then use **Computer use**
   to select **CPU** or **NVIDIA GPU**. An unavailable GPU route stays blocked
   and explains what is missing.
3. Under **Reviewed settings**, confirm the fixed installation location, compute
   route, and whether to add a Desktop shortcut.
4. Select **Install VIPP** and wait for setup and its final acceptance checks.
5. Open **VIPP** for a CPU installation. A CUDA installation provides
   **VIPP Automatic**, **VIPP CPU**, and **VIPP Prefer GPU** shortcuts; begin
   with **VIPP Automatic**.

!!! important "CUDA location in 0.15.0a1"
    One-click setup obtains canonical Windows Local App Data through
    `SHGetKnownFolderPath(FOLDERID_LocalAppData)` and accepts only
    `VIPP\environments\cpu` or `VIPP\environments\cuda13` beneath it. A custom
    managed root is not accepted. CuPy 14.1.1 requires the complete CUDA path
    to contain ASCII characters in this release; spaces are supported. If
    canonical Local App Data contains a non-ASCII character, one-click CUDA is
    unavailable before environment creation or download and setup offers CPU.
    The fixed CPU root remains Unicode-safe. Expert-selected existing
    environments are inspected separately and remain unchanged.

Changing the compute choice or Desktop-shortcut choice requires
**Check these settings** again. Setup never enables **Install VIPP** for settings it
has not checked.

GPU setup is a large download. It currently needs at least 15 GiB free on the
installation drive while setup runs; CPU setup needs at least 5 GiB there.
Those are disk-storage requirements, not GPU memory (VRAM). GPU setup also
needs at least 5 GiB free on every drive used for Windows temporary files and
VIPP installer records; CPU setup needs at least 1 GiB in those
temporary/record locations. Setup identifies the exact location when a check
fails.

Before confirmation, the review separates approximate capacity from those
conservative enforced minimums:

| Track | Approximate download | Approximate installed | Approximate peak working space |
| --- | ---: | ---: | ---: |
| CPU | 250 MiB | 1.5 GiB | 2.5 GiB |
| CUDA 13 | 1.5 GiB | 5 GiB | 7 GiB |

Actual transfer can vary with the package index and cache. During setup, the
current phase, elapsed time, latest concrete activity, and a quiet-operation
heartbeat remain visible. The activity bar is indeterminate unless the
dependency tool supplies a trustworthy byte total. Expand **Advanced details**
to see or open the setup log; a long quiet operation is not itself reported as
a failure.

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

An installer-owned CUDA copy already stored under a non-ASCII path cannot be
updated or repaired in place by 0.15.0a1. Setup may first complete and record
recovery from an earlier interrupted transaction; after that separate
recovery, the newly blocked selection performs no new mutation of the old
environment, shortcuts, or ownership record. Do not move or rename that
virtual environment or start a second managed CUDA installation: the CUDA
track has one Windows Apps entry and shared shortcut names. Select **Open
Installed apps**, uninstall **VIPP (GPU)**, and wait for the ownership-bound
removal to finish. If canonical Local App Data is non-ASCII, this account still
cannot use one-click CUDA and setup offers CPU. This is an explicit release
boundary, not an in-place or fallback migration.

Remove either installation from **Windows Settings → Apps → Installed apps**.
Each entry has its own ownership-bound uninstaller, so removing CPU does not
remove CUDA and removing CUDA does not remove CPU.

## macOS installer — recommended

VIPP 0.15.0a1 has separate offline packages for Apple Silicon and Intel Macs.
Each package includes Python and napari, installs a private CPU-only environment
under `~/Library/vipp`, and creates `~/Applications/VIPP.app`. No terminal or
separate Python installation is required for the normal route.

The alpha packages are explicitly unsigned and not notarized. Download the PKG
and architecture-matched checksum only from the official release, verify the
SHA-256, and use macOS **Open Anyway** only for that verified file. See
[Install VIPP on macOS](macos.md) for architecture selection, installation,
launch, and removal.

## Linux and advanced manual installation

VIPP 0.15.0a1 supports CPython 3.12 and 3.13 for CPU use. Create a dedicated
environment, then install the exact alpha. An exact prerelease pin does not need
pip's `--pre` option.

The commands below use the exact `0.15.0a1` package pin.

=== "Windows manual"

    ```powershell
    py -3.12 -m venv ".venv-vipp"
    & ".\.venv-vipp\Scripts\python.exe" -m pip install --upgrade pip
    & ".\.venv-vipp\Scripts\python.exe" -m pip install `
      "napari[pyqt6]>=0.6" `
      "napari-vipp==0.15.0a1"
    & ".\.venv-vipp\Scripts\vipp.exe"
    ```

=== "macOS"

    ```bash
    python3.12 -m venv vipp-env
    source vipp-env/bin/activate
    python -m pip install --upgrade pip
    python -m pip install "napari[pyside6]>=0.6" \
      "napari-vipp==0.15.0a1"
    vipp
    ```

=== "Linux"

    ```bash
    python3.12 -m venv vipp-env
    source vipp-env/bin/activate
    python -m pip install --upgrade pip
    python -m pip install "napari[pyqt6]>=0.6" \
      "napari-vipp==0.15.0a1"
    vipp
    ```

macOS is CPU-only in this alpha. Native Linux GPU qualification is **not run**;
Linux remains on the CPU path even if CUDA packages import.

Installing into an existing napari environment is an advanced route. Use that
environment's Python explicitly and keep the VIPP version pinned. Do not use a
global Python, an environment that exposes system site-packages, an editable
VIPP checkout, or an environment with multiple Qt bindings.

## Confirm the installation

For an installer-managed copy, open the created VIPP shortcut and choose
**Gear menu → Open example…**. For a manually managed environment, you can also run:

```text
python -c "import importlib.metadata as m; print(m.version('napari-vipp'))"
```

Expected for this release:

```text
0.15.0a1
```

Inside napari, choose **Plugins → VIPP Workflow (napari-vipp)**.

## Optional NVIDIA CUDA acceleration

The Windows installer is the recommended GPU path. The standard CUDA setup
installs its pinned CUDA libraries and every current reviewed CuPy/CuPyX
provider inside the managed VIPP environment. There is no separate provider
installer or local source-build step.

VIPP admits a successfully probed NVIDIA CUDA device only when every released
gate passes: native 64-bit Windows, CPython 3.12, compute capability 7.5 or
newer, driver API 13.3 or newer, CUDA runtime API 13.2, the pinned scientific
and CuPy/CuPyX packages, provider probes, memory, workload, and scientific
parity. GPU names are recorded for provenance rather than used as an allowlist.
Unsupported work stays on CPU with an explanation.

For a manual CUDA environment:

Run these commands from an ASCII-only working directory:

```powershell
py -3.12 -m venv ".venv-vipp-gpu-cu13"
& ".\.venv-vipp-gpu-cu13\Scripts\python.exe" -m pip install --upgrade pip
& ".\.venv-vipp-gpu-cu13\Scripts\python.exe" -m pip install `
  "napari[pyqt6]>=0.6" `
  "napari-vipp[gpu-cuda13]==0.15.0a1"
& ".\.venv-vipp-gpu-cu13\Scripts\vipp-compute-doctor.exe" --track cuda13
& ".\.venv-vipp-gpu-cu13\Scripts\vipp.exe"
```

This advanced manual environment is separate from one-click management. The
installer does not move or edit it. Create a fresh manual environment rather
than moving or renaming one whose complete path is incompatible.

Read the complete [Windows NVIDIA GPU guide](windows-cuda.md) before adding GPU
packages manually.

If you are evaluating this alpha for the project, use the short
[Windows installer field checklist](windows-field-acceptance.md). It records
what was actually tried without turning an unperformed CPU, CUDA, rollback, or
novice check into a pass.

## Optional microscope readers

Install an optional reader with the Python from the exact environment that
launches VIPP, then restart napari.

| File family | Command |
| --- | --- |
| Nikon ND2 | `python -m pip install "napari-vipp[nd2]==0.15.0a1"` |
| Zeiss CZI | `python -m pip install "napari-vipp[czi]==0.15.0a1"` |
| Mixed microscope formats, including Imaris IMS | `python -m pip install "napari-vipp[microscope]==0.15.0a1"` |
| BioIO/Bio-Formats fallback | `python -m pip install "napari-vipp[bioformats]==0.15.0a1"` |

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
