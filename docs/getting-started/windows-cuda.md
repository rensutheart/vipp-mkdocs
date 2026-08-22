# Windows NVIDIA GPU setup

VIPP 0.13.0a8 uses one standard CUDA 13 installation for every current
reviewed GPU implementation. The normal Windows installer is the recommended
route. It installs CuPy/CuPyX and the matching CUDA component packages inside a
private VIPP environment; no CUDA Toolkit, Visual Studio, CMake, `nvcc`, cuCIM
bundle, or locally built provider wheel is required.

!!! warning "Use the exact a8 release"
    Download the installer and checksum only from the
    [official v0.13.0a8 release](https://github.com/rensutheart/napari-vipp/releases/tag/v0.13.0a8).
    Verify `VIPP-Setup-0.13.0a8-Windows-x86_64-UNSIGNED.exe` against
    `SHA256SUMS-Windows-0.13.0a8.txt` before opening it. This alpha is
    intentionally unsigned, so **Unknown publisher** is expected.

## Choose the standard NVIDIA route

In setup, keep **Automatic** or expand **Advanced details** and select
**NVIDIA GPU**. Setup checks the computer before enabling **Install** and
explains any failed requirement. A blocked GPU choice never silently becomes a
different managed installation.

| Requirement | 0.13.0a8 boundary |
| --- | --- |
| Operating system | Native 64-bit Windows |
| Python | 64-bit CPython 3.12; 3.12.10 is the installer reference |
| GPU | NVIDIA CUDA device with compute capability 7.5 or newer |
| Driver/runtime | Driver API 13.3 and CUDA runtime API 13.2 or newer |
| Scientific stack | Pinned NumPy, SciPy, scikit-image, CuPy/CuPyX, and CUDA 13 components |
| Managed location | Canonical Local App Data `VIPP\environments\cuda13` with an ASCII-only complete path |
| Admission | Runtime/provider probes, device memory, operation region, workload, and scientific parity must all pass |

The public policy does not use a GPU-model allowlist. Device names and ordinals
are recorded for provenance. Every currently visible CUDA device must satisfy
the architecture floor because this release probes all visible ordinals before
choosing its default. A mixed workstation with one older visible device is
therefore blocked even if another device qualifies.

Only the NVIDIA display driver is a system-wide CUDA prerequisite. The VIPP
installer supplies the user-space CUDA libraries inside its environment.

## Managed location and temporary files

One-click setup obtains canonical Windows Local App Data through
`SHGetKnownFolderPath(FOLDERID_LocalAppData)` and accepts only
`VIPP\environments\cuda13` beneath it for the managed GPU track. Spaces are
supported. CuPy 14.1.1 requires this complete environment path to contain ASCII
characters. If canonical Local App Data contains a non-ASCII character, setup
blocks one-click CUDA before creating an environment or downloading packages
and offers CPU instead.

Python's effective temporary directory is a separate path. When it contains a
non-ASCII character, VIPP uses CuPy's process-local in-memory compilation cache.
This preserves the scientific kernels and results but can make Compute Doctor
or the first GPU work compile again after VIPP restarts.

GPU setup is a large download and currently needs at least 15 GiB free on the
installation drive while setup runs. It also needs at least 5 GiB free on each
drive used for Windows temporary files and VIPP installer records. These are
disk-space requirements, not GPU memory requirements.

## Verify the installation

A managed CUDA installation creates **VIPP Automatic**, **VIPP CPU**, and
**VIPP Prefer GPU** shortcuts. Start with **VIPP Automatic**. Open **Compute
setup and memory** to refresh the concise qualification rows:

1. **CUDA and GPU** — can the pinned CUDA/CuPy runtime allocate and execute;
2. **VIPP GPU coverage** — which reviewed operation regions are available.

Advanced technical detail remains under **Show advanced details**. A
privacy-redacted report suitable for support can be saved from the window or
created with `vipp-compute-doctor --track cuda13 --support-bundle
".\vipp-compute-support.json"` from the active CUDA environment.

The exact internal managed environment path can change after update or repair,
so the shortcut and graphical command are preferable to guessing a nested
Python path. For a manually created environment, run its own command directly:

```powershell
& ".\.venv-vipp-gpu-cu13\Scripts\vipp-compute-doctor.exe" --track cuda13
```

`python -m pip check` must also report no broken requirements.

## Manual dedicated environment

Use this only when terminal-level control is required. Run from an ASCII-only
working directory:

```powershell
py -3.12 -m venv ".venv-vipp-gpu-cu13"
& ".\.venv-vipp-gpu-cu13\Scripts\python.exe" -m pip install --upgrade pip
& ".\.venv-vipp-gpu-cu13\Scripts\python.exe" -m pip install `
  "napari[pyqt6]>=0.6" "napari-vipp[gpu-cuda13]==0.13.0a8"
& ".\.venv-vipp-gpu-cu13\Scripts\vipp-compute-doctor.exe" --track cuda13
& ".\.venv-vipp-gpu-cu13\Scripts\vipp.exe"
```

This environment is separate from installer management. Do not move or rename
it after CuPy has compiled kernels, and do not mix CUDA 12 and CUDA 13 packages
in one environment.

## What the standard installation accelerates

Reviewed GPU candidates cover operation-specific regions of:

- Rolling-Ball Background and Subtract Background through CuPy;
- Extract Channel and exact Preserve conversion to `float32`;
- Gaussian, median, and Sigma filtering;
- Richardson-Lucy and Richardson-Lucy TV deconvolution;
- fixed Binary, Canny, and Otsu thresholding;
- boolean Remove Small Objects, Fill Holes, and Remove Outliers;
- Connected Components; and
- the basic **Measure Objects** and **Measure Objects + Intensity** schemas.

Coverage is region-specific, not node-wide. Unsupported dtypes, dimensionality,
parameters, extended measurement columns, scientific parity, or memory needs
remain on CPU with an explanation. **Auto** can correctly select CPU when the
complete workload is faster there. **Prefer GPU** still allows visible CPU
fallback.

The completed-node badge reports what actually ran. Current a8 GPU providers
appear as **GPU · CuPy**; an amber **CPU fallback** badge identifies a failed or
ineligible accelerator request. Old workflows or provenance can still contain
historical cuCIM identities, but a8 does not install or execute that provider.

## Background and basic measurements are CuPy-only

Rolling-Ball Background and Subtract Background no longer need a separately
built provider. **Measure Objects** and **Measure Objects + Intensity** also use
the standard CuPy installation. Their reviewed evidence covers 2D and 3D label
tables, leading blocks, reordered/calibrated axes, sparse and repeated IDs,
zero-row tables, supported intensity dtypes, cancellation, deterministic
repeats, and zero private-pool residue.

Exact saved basic-measurement pins migrate automatically:

| Former saved identity | Current identity |
| --- | --- |
| `cucim-measure-objects-basic-v1` | `cupy-measure-objects-basic-v1` |
| `cucim-measure-objects-intensity-basic-v1` | `cupy-measure-objects-intensity-basic-v1` |

A broad saved `library:cucim` preference is not one unambiguous operation and
therefore remains visibly unavailable. Choose a current implementation or
compute mode explicitly rather than expecting VIPP to guess.

!!! danger "Do not reuse an old provider add-on"
    Do not install a cuCIM ZIP, private wheel, or source-build helper from an
    earlier VIPP release into 0.13.0a8. Those assets describe an older release
    boundary and are not required by the current application.

## Runtime behavior and provenance

VIPP checks RAM, Windows commit headroom, VRAM, transfers, workspaces, and
retained outputs before admitting work. Cancellation completes only after
synchronized cleanup. A runtime failure may retry on CPU when the fallback
contract permits; a cleanup failure disables new compute until VIPP restarts.

Compatible GPUs can produce small floating-point differences because hardware,
drivers, JIT compilation, and reduction order differ. VIPP still applies each
implementation's declared parity contract, but that is not a promise of
bitwise identity across devices. Preserve:

- the VIPP version and workflow/input identities;
- actual implementation IDs and fallback decisions;
- GPU model, ordinal, compute capability, driver/runtime, and VRAM;
- Python, CuPy/CuPyX, NumPy, SciPy, and scikit-image versions; and
- authored parameters and validation against the CPU reference.

## Troubleshooting

### CUDA imports but a node uses CPU

This is often correct. Inspect the node's compute explanation for a dtype,
rank, parameter, memory, workload, or parity exclusion. Do not change a
scientific parameter merely to unlock GPU execution.

### First GPU run is slow

CuPy compiles kernels lazily. Compare warmed repeated runs and include transfer
and result-finalization time. A cold first run is not a stable speed claim.

### The selected assignment changed

Machine-local evidence is invalidated when the graph, source revision,
parameters, compute intent, implementation catalogue, environment, or device
changes. Run **Find fastest pipeline…** again and review the new evidence.

### Need the previous cuCIM procedure

Use the matching archived release page for the old environment. Do not apply
that procedure to a8. The [0.13.0a7 release page](../releases/0.13.0a7.md) is
preserved as the historical record.

Continue with [Choose CPU or GPU compute](../how-to/choose-compute.md) and the
[0.13.0a8 release notes](../releases/0.13.0a8.md).
