# Windows NVIDIA GPU setup

VIPP 0.16.0a4 uses one standard CUDA 13 installation for every current
reviewed GPU implementation. The normal Windows installer is the recommended
route. It installs CuPy/CuPyX and the matching CUDA component packages inside a
private VIPP environment; no separate CUDA Toolkit or build tools are required.

!!! warning "Use the exact 0.16.0a4 release"
    Download the installer and checksum only from the
    [official v0.16.0a4 release](https://github.com/rensutheart/napari-vipp/releases/tag/v0.16.0a4).
    Verify `VIPP-Setup-0.16.0a4-Windows-x86_64-UNSIGNED.exe` against
    `SHA256SUMS-Windows-0.16.0a4.txt` before opening it. This alpha is
    intentionally unsigned, so **Unknown publisher** is expected.

## Choose the standard NVIDIA route

In setup, keep **Automatic** or expand **Advanced details** and select
**NVIDIA GPU**. Setup checks the computer before enabling **Install VIPP** and
explains any failed requirement. A blocked GPU choice never silently becomes a
different managed installation.

| Requirement | 0.16.0a4 boundary |
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

## Set up GPU from inside VIPP

!!! info "Unreleased — nightly only"
    The steps below apply to the in-app setup added after 0.16.0a3. Numbered
    releases without this action use the standard installer described above.

If **Compute setup and memory…** reports that CuPy is missing, the current VIPP
environment does not have the optional GPU library. On supported Windows
computers, VIPP can install it without copying commands into a terminal:

1. Open **Compute setup and memory…**. Read the status and select the prominent
   **Set up GPU…** or **Repair GPU setup…** action beside its next-step guidance.
   You do not need to open advanced details.
2. Let VIPP check the hardware, Python, available disk space and the exact VIPP
   build. The setup window groups its status, next action and installation
   information into cards. Review **Installation location**—the separate copy
   where GPU support will be installed—then select **Install GPU support** or
   **Repair GPU setup**. An internet connection is needed to download dependencies.
   If this exact build is already verified, the window instead offers **Open
   VIPP with GPU**; another installation is not needed.
3. Follow the installation progress. Use **Cancel setup** to stop, or **Try
   again** after addressing a reported failure. VIPP verifies the GPU
   environment before offering **Open VIPP with GPU**.
4. Select **Open VIPP with GPU** to launch that environment in a new window.
   Your current window and its workflows remain open. Save any edits there,
   then open the saved workflows in the new window; unsaved tabs are not
   transferred automatically.

The primary action and **Close** or **Cancel setup** stay in the footer while
long content scrolls. **Technical details** is collapsed initially; expand its
chevron to read the monospaced setup log. Opening details does not install or
change anything. When a verified GPU copy is already ready, the summary focuses
on opening it rather than showing download estimates for a new installation.

Setup uses a separate managed CUDA environment and leaves the current CPU
environment unchanged. Its reviewed location is specific to this VIPP build,
so a standard GPU installation can remain alongside it. It retains the exact
VIPP wheel used by this build, including local unreleased changes. If that
wheel is unavailable or no longer
matches, setup stops with an explanation; it does not substitute another build
with the same version number. Keep the original build bundle available and
follow the reported recovery instruction.

The supported route requires native 64-bit Windows, CPython 3.12, and the
NVIDIA hardware and driver requirements above. Setup cannot install a display
driver or turn an unsupported GPU into a supported one. It reports the
specific blocker when this route is unavailable.

Installing the GPU environment does not change saved compute choices or make
every node GPU-capable. Reopen the workflow, select its desired compute policy,
and inspect the actual-run badges as described in [Choose and verify
compute](../how-to/choose-compute.md).

## Managed location and temporary files

The standard installer obtains canonical Windows Local App Data through
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

The review gives separate rounded orientation: approximately 1.5 GiB to
download, 5 GiB installed, and 7 GiB peak temporary working space for CUDA.
Those estimates do not replace the 15 GiB installation-drive and 5 GiB
temp/records-drive gates. Setup names the current phase and elapsed time, keeps
the latest concrete activity visible through quiet periods, and exposes its log
under **Advanced details**. A determinate percentage appears only when the
underlying dependency tool reports a trustworthy byte total.

!!! note "New in 0.16.0a1"
    The visible **Installation log** shows package download and installation
    messages. Scroll up without losing your place, then select **Jump to latest**
    to follow new messages again. See [Read the live installation
    log](installation.md#read-the-live-installation-log) for the full-log option.

## Verify the installation

Open the [installed VIPP launcher](launching.md#use-the-installed-shortcut-on-windows).
**New in 0.15.0a5:** CUDA installations use one **VIPP** shortcut and
start in **Auto**; choose other compute modes inside the app. The separate
CUDA installation is still required for its optional GPU dependencies.

Open **Compute setup and memory** to refresh the concise qualification rows:

1. **CUDA and GPU** — can the pinned CUDA/CuPy runtime allocate and execute;
2. **VIPP GPU coverage** — which reviewed operation regions are available.

Advanced technical detail remains under **Show advanced details**. A
privacy-redacted report suitable for support can be saved from the window or
created with `vipp-compute-doctor --track cuda13 --support-bundle
".\vipp-compute-support.json"` from the active CUDA environment.

In the unreleased nightly layout, the session GPU choice stays visible and the
status groups the recommended setup or repair action with its explanation.
Expand the chevron beside **Advanced details** for the package track, technical
evidence and labelled **Manual command**. Its explanation distinguishes manual
setup from verification; copying a command does not run it. **Verify GPU setup**
only checks the environment—it does not install packages. **Save support report…**
and **Close** remain in the footer while long content scrolls.

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
  "napari[pyqt6]>=0.6" `
  "napari-vipp[gpu-cuda13]==0.16.0a4"
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
- Connected Components;
- the basic **Measure Objects** and **Measure Objects + Intensity** schemas;
- GPU label preparation for hybrid **Measure 3D Mesh Morphology**; and
- **Analyze Skeleton** on already-skeletonized Boolean inputs.

Mesh morphology retains CPU marching cubes, convex hulls, and table construction.
Skeletonization itself remains CPU work. See the
[compute matrix](../how-to/choose-compute.md#gpu-regions-in-0150a2) for the exact
regions and requirements.

Coverage is region-specific, not node-wide. Unsupported dtypes, dimensionality,
parameters, extended measurement columns, scientific parity, or memory needs
remain on CPU with an explanation. **Auto** can correctly select CPU when the
complete workload is faster there. **Prefer GPU** still allows visible CPU
fallback.

The completed-node badge reports what actually ran. GPU providers in 0.16.0a4
appear as **GPU · CuPy**; an amber **CPU fallback** badge identifies a failed or
ineligible accelerator request.

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

In 0.16.0a4, Prefer GPU preserves exact workload facts across intervening
CPU-only nodes. A required CPU Rescale Axes, Rescale Intensity, or Unsharp Mask
step therefore does not by itself make reviewed downstream GPU work
ineligible. If an affected downstream node still uses CPU, its compute details
identify the actual runtime, provider, workload, or memory gate.

### GPU VRAM preflight fails before calculation

This is a conservative device-admission result, not an ordinary RAM error or a
CUDA allocation failure. The diagnostic names the GPU and affected nodes and
shows estimated peak use, available VRAM, the shortfall, and whether the safety
reserve or configured cap is binding. Exact bytes remain in technical details.

Start with its listed remedies: reduce or crop the input, move one listed node
to CPU to split the device segment, close other GPU applications, or accept
visible CPU fallback when offered. Change the reserve or memory cap only when
you can still leave adequate device headroom.

### First GPU run is slow

CuPy compiles kernels lazily. Compare warmed repeated runs and include transfer
and result-finalization time. A cold first run is not a stable speed claim.

### The selected assignment changed

Machine-local evidence is invalidated when the graph, source revision,
parameters, compute intent, implementation catalogue, environment, or device
changes. Run **Find fastest pipeline…** again and review the new evidence.

## Earlier cuCIM support

[VIPP 0.13.0a7](../releases/0.13.0a7.md) was the last release with optional
cuCIM support. Current releases use CuPy/CuPyX for GPU processing.

In the historical RTX 5090 comparison, the clearest cuCIM gain over a ready
CuPy/CuPyX equivalent was the **Median Filter** primitive with a `uint16`
31 × 31 window: **1.42× faster** (57.2 ms versus 81.3 ms, including transfers).
Gaussian, small-window median, Sobel, and binary closing showed little benefit.
These were library-primitive timings on one machine, not complete VIPP-node
benchmarks. See the
[comparison benchmark table](https://github.com/rensutheart/napari-vipp/blob/b4ef16e100143336a5f7488aca8879b667204361/docs/cucim-windows-source-evaluation.md#standard-benchmark-results).

The later **Measure Objects** and **Measure Objects + Intensity** comparison
favored CuPy in all 14 matched cases; see the
[measurement benchmarks](https://github.com/rensutheart/napari-vipp/blob/23e5866cfad7562cb1490e4405ff874cedf964b2/docs/benchmarks/measurements-cupy-windows-rtx5090.md#historical-provider-comparison).

Continue with [Choose CPU or GPU compute](../how-to/choose-compute.md) and the
[official v0.16.0a4 release](https://github.com/rensutheart/napari-vipp/releases/tag/v0.16.0a4).
