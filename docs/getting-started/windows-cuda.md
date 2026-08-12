# Install CUDA acceleration on 64-bit Windows

This page is the Windows-specific companion to the main
[installation guide](installation.md). VIPP remains fully usable on CPU without
any NVIDIA packages.

!!! note "Use the manual for your installed release"

    The commands on this page are pinned to the 0.13.0a5 package and immutable
    `v0.13.0a5` tag. Select the numbered `0.13.0a5` manual when installing this
    release; the nightly manual can describe changes intended for a later
    version.

## Choose the installation you need

| Goal | 0.13.0a5 route |
| --- | --- |
| Run VIPP on CPU | Use the signed installer from the main installation guide and keep its CPU recommendation. |
| Use the reviewed CuPy/CuPyX operations | Use the signed installer and keep Automatic, or explicitly select NVIDIA GPU under Advanced details. The manual `gpu-cuda13` route below remains available. |
| Use cuCIM-backed background or basic-measurement operations | First complete the standard CUDA installation, then use the separate no-wheel cuCIM bundle or [build and add the pinned cuCIM release](#build-and-add-the-pinned-cucim-release). VIPP does not distribute the wheel. |

## Requirements for the standard CUDA 13 route

You need:

- native x86-64 Windows and 64-bit CPython 3.12;
- an NVIDIA CUDA-capable GPU; and
- an NVIDIA display driver new enough for CUDA 13.

You do **not** need to install a system-wide CUDA Toolkit, `nvcc`, Visual
Studio, CMake, or cuDNN. The `gpu-cuda13` extra installs VIPP's pinned CUDA
13.2 user-space libraries and CuPy inside its virtual environment. The NVIDIA
driver remains a machine-wide prerequisite and must be installed separately.

Check Python before creating the environment:

```powershell
py -3.12 -c "import platform, struct; print(platform.python_implementation(), platform.python_version(), struct.calcsize('P') * 8)"
```

The result must begin with `CPython 3.12` and end with `64`.

Check that Windows can see the NVIDIA driver and GPU:

```powershell
nvidia-smi
```

If that command is missing or reports a driver problem, install or update the
[NVIDIA driver](https://www.nvidia.com/Download/index.aspx) before installing
VIPP's GPU extra. NVIDIA documents driver 580 or newer as the CUDA 13.x
[minor-version compatibility minimum](https://docs.nvidia.com/cuda/archive/13.2.0/cuda-toolkit-release-notes/index.html#cuda-driver),
although VIPP's scientific admission gate below is narrower. The CUDA value
printed by `nvidia-smi` is the newest CUDA version supported by the driver; it
is not the CUDA runtime installed in the VIPP environment.

!!! warning "Scientific admission remains narrower than installability"

    VIPP 0.13.0a5 admits a successfully probed NVIDIA CUDA device with compute
    capability 7.5 or newer and driver API 13.3 or newer. Public GPU execution
    still requires native Windows, CPython 3.12, NumPy 2.5.1, SciPy 1.18.0,
    scikit-image 0.26.0, CuPy/CuPyX 14.1.1, and CUDA runtime API 13.2. A failed
    provider probe, changed runtime or scientific package, unsupported
    operation region, or insufficient memory produces an explained CPU
    decision. Native Linux GPU qualification remains pending.

    Minor floating-point differences can occur across GPU models, drivers,
    compiler paths, and reduction order within a provider's declared parity
    tolerance. Record the complete hardware and software environment and
    validate consequential analyses against the CPU reference.

## Install VIPP with CUDA 13

Use a new environment. The commands call that environment's executables
directly, so PowerShell script-activation policy cannot interfere.

```powershell
py -3.12 -m venv ".venv-vipp-gpu-cu13"
& ".\.venv-vipp-gpu-cu13\Scripts\python.exe" -m pip install --upgrade pip
& ".\.venv-vipp-gpu-cu13\Scripts\python.exe" -m pip install "napari[pyqt6]>=0.6" "napari-vipp[gpu-cuda13]==0.13.0a5"
& ".\.venv-vipp-gpu-cu13\Scripts\vipp-compute-doctor.exe" --track cuda13
& ".\.venv-vipp-gpu-cu13\Scripts\vipp.exe"
```

An exact prerelease such as `==0.13.0a5` does not need pip's `--pre` option.
Use `--pre` only when asking pip to choose the latest unpinned VIPP alpha.

Do not add the `gpu-cuda12` extra to this environment. CUDA 12 is a separate
developer-qualification track in 0.13.0a5, and CuPy's CUDA 12 and CUDA 13
distributions must never share one environment.

### Upgrade an existing manually managed 0.13 alpha CUDA environment

Close VIPP and napari first. Keep the existing environment directory name;
renaming a virtual environment can break its launcher paths. Resolve its Python
and upgrade only the pinned CUDA 13 package set:

```powershell
$installRoot = Join-Path $env:USERPROFILE "VIPP-0.13.0a1"
$vippPython = (Resolve-Path (Join-Path $installRoot ".venv-vipp-gpu-cu13\Scripts\python.exe")).Path

& $vippPython -m pip install --upgrade --upgrade-strategy only-if-needed "napari-vipp[gpu-cuda13]==0.13.0a5"
& $vippPython -c "import importlib.metadata as m; print(m.version('napari-vipp'))"
& $vippPython -m pip check
& (Join-Path $installRoot ".venv-vipp-gpu-cu13\Scripts\vipp-compute-doctor.exe") --track cuda13 --refresh
```

An earlier private cuCIM wheel and manifest remain compatible with a5 because the
cuCIM source, build recipe, payload digest, and approval schema did not change.
Keep those files. If the refreshed cuCIM probe succeeds, do not rebuild or
reinstall it. If it fails, obtain the immutable a5 source and use its
`setup_gpu_dev.py --existing-environment ... --plan-only` command with the
retained wheel and manifest. Reinstall through that helper only when the plan
passes; never copy an old approval JSON back manually. Rebuild from the a5 tag
only when the retained artifact pair is missing, damaged, or rejected.

## Read the compute-doctor result

`vipp-compute-doctor` reports Python, the selected CUDA track, installed GPU
packages, the runtime and driver APIs, the detected device, and whether the
CuPy runtime probe succeeds. It does not decide per-operation scientific-policy
admission; VIPP makes that later decision from the exact environment and
workload.

- **Available** means the CuPy runtime probe completed. It does not promise
  that every node or workload is GPU-eligible.
- **Unsupported** normally identifies the wrong Python implementation, minor
  version, bitness, operating system, or execution mode.
- **Unavailable** normally identifies a missing driver/device, a failed CUDA
  import or kernel, or mixed CuPy distributions.
- A successful runtime with an unqualified device, driver, package version,
  dtype, shape, or parameter set remains on CPU and explains the rejected gate.

Inside VIPP, open **Compute setup and memory...** to see the same diagnosis.
After a calculation, the node badge records what actually ran: **CPU**,
**GPU · CuPy**, **GPU · cuCIM**, or amber **CPU fallback**.

## What the standard extra does not install

The `gpu-cuda13` extra installs CuPy/CuPyX and the pinned CUDA runtime. It does
not install cuCIM. Consequently, Rolling-Ball/Subtract Background and the
cuCIM-backed basic measurement candidates remain on CPU after the standard
installation unless the user completes the optional local-build route below.
Other reviewed CuPy/CuPyX regions can still accelerate when every admission
gate passes.

## cuCIM status on Windows

cuCIM 26.6.0 has no official native-Windows wheel. Its PyPI files are Linux
wheels, and the upstream
[Windows-support request](https://github.com/rapidsai/cucim/issues/454) remains
open. VIPP's research build packages `cucim.core` and `cucim.skimage`, including
runtime-compiled CUDA kernels, but deliberately omits the native
`cucim.clara` whole-slide I/O library.

The local recipe produces
`cucim_cu13-26.6.0-cp312-cp312-win_amd64.whl`. That tag means only:

| Dimension | Scope of the recorded wheel |
| --- | --- |
| Operating system / CPU | native 64-bit Windows on x86-64 |
| Python | CPython 3.12 ABI only |
| CUDA package family | CUDA 13 / `cupy-cuda13x` |
| cuCIM surface | `core` and `skimage`; no Clara/CuImage I/O |
| VIPP public admission | qualifying NVIDIA CUDA device, compute capability 7.5 or newer; exact software and provider gates still apply |

It is therefore **not** a universal Windows 64-bit wheel. The payload contains
Python, data files, and CUDA sources that CuPy compiles for the current GPU at
runtime, so a broader ABI-independent wheel may be technically possible. It
must first be rebuilt with corrected metadata and validated on each advertised
Python/GPU environment; renaming or retagging the existing wheel is not valid.

!!! info "Optional and fail-closed"

    VIPP neither distributes nor requires cuCIM. The build/install steps below
    are opt-in. If cuCIM is absent, its recorded payload is altered, it comes
    from a different source/recipe, or it fails a real probe, VIPP does not
    approve it and the affected operation uses CPU. Other CuPy/CuPyX
    acceleration remains available independently.

## Build and add the pinned cuCIM release

Complete the standard CUDA 13 installation above first. This route additionally
requires Git for Windows, internet access, and enough temporary disk space for
an isolated CUDA build environment. It does **not** require a machine-wide CUDA
Toolkit, Visual Studio, CMake, or a compiler installation.

The recipe is fixed to cuCIM tag `v26.06.00`, version `26.6.0`, upstream commit
`3c15781c207eab93a317dd9803a6e726fe01f7c4`, and VIPP recipe
`napari-vipp-cucim-windows-v1`. Do not substitute another tag or wheel.

The fixed canonical installed-payload SHA-256 is
`d640d1e17bcce15d32d03841997252bf915b63da855e406c35f0d70c5a5ea667`.
Each locally produced wheel file has its own SHA-256, recorded in its manifest,
and that file hash may differ between users or builds even when
the canonical installed payload is identical. VIPP admits only the fixed
canonical payload and source/recipe identity after also verifying the local
wheel recorded by that manifest.

### 1. Record the installed VIPP interpreter

Run this from the directory containing the environment created above:

```powershell
$vippPython = (Resolve-Path ".\.venv-vipp-gpu-cu13\Scripts\python.exe").Path
& $vippPython -c "import sys; print(sys.executable)"
```

### 2. Get the matching VIPP release source

The build and approval scripts are deliberately release-source tools rather
than a bundled cuCIM dependency:

```powershell
$sourceRoot = Join-Path $env:USERPROFILE "napari-vipp-0.13.0a5-source"
git clone --branch v0.13.0a5 --depth 1 https://github.com/rensutheart/napari-vipp.git $sourceRoot
Set-Location $sourceRoot
```

### 3. Build twice and create the manifest

Choose a private output directory that does not already contain artifacts:

```powershell
$python312 = py -3.12 -c "import sys; print(sys.executable)"
$artifactDir = Join-Path $env:USERPROFILE "vipp-cucim-local\0.13.0a5"
New-Item -ItemType Directory -Path $artifactDir -Force | Out-Null

powershell -ExecutionPolicy Bypass -File .\scripts\build_cucim_windows.ps1 `
  -Python $python312 `
  -OutputDirectory $artifactDir
```

The script verifies the exact upstream commit and installs its complete
41-distribution build environment at exact versions with dependency resolution
disabled. It rejects any missing, extra, duplicate, or changed distribution,
performs two clean builds, requires identical canonical payloads, checks
materialized licences and metadata, and runs real cuCIM GPU operations.
It writes exactly one wheel and one `*.build-manifest.json` file to
`$artifactDir` and refuses to overwrite them.

### 4. Inspect the plan, then add cuCIM to the released environment

```powershell
$wheel = Join-Path $artifactDir "cucim_cu13-26.6.0-cp312-cp312-win_amd64.whl"
$manifest = Join-Path $artifactDir "cucim_cu13-26.6.0-cp312-cp312-win_amd64.build-manifest.json"

& $vippPython .\scripts\setup_gpu_dev.py `
  --existing-environment `
  --track cuda13 `
  --python $vippPython `
  --cucim-wheel $wheel `
  --cucim-manifest $manifest `
  --plan-only
```

Check that every displayed path targets the intended `.venv-vipp-gpu-cu13`
environment. Then repeat without `--plan-only`:

```powershell
& $vippPython .\scripts\setup_gpu_dev.py `
  --existing-environment `
  --track cuda13 `
  --python $vippPython `
  --cucim-wheel $wheel `
  --cucim-manifest $manifest
```

This mode does not upgrade `pip`, `setuptools`, or `wheel`, install development
dependencies, or replace the released VIPP package with an editable checkout.
It installs only `click==8.4.2`, `lazy-loader==0.5`,
`nvidia-nvimgcodec-cu13==0.8.0.22`, and the local cuCIM wheel. It verifies the
manifest, wheel-file SHA-256, canonical wheel payload, installed PEP 610
provenance, exact CUDA stack, real CUDA/cuCIM kernels, and `pip check`. It
removes any earlier approval before changing packages and writes a new record
atomically only after every check succeeds. Before admitting cuCIM for use,
VIPP independently recomputes that canonical payload from the installed files.

These checks detect build or installed-payload drift in a user-controlled
environment; they are not a security boundary against someone who can add
unrecorded importable files or otherwise modify that environment. If the
environment is no longer trusted, delete it and repeat the installation rather
than relying on the approval record.

### 5. Verify VIPP can probe cuCIM

```powershell
& $vippPython -c "from napari_vipp.core.compute_registry import ComputeRegistry; r = ComputeRegistry().probe_library('cucim', refresh=True); print(r.available, r.version, r.reason_code, r.message); raise SystemExit(0 if r.available else 2)"
```

An available library is still subject to VIPP's exact hardware, scientific
stack, parameter, dtype, shape, memory, and cleanup gates. Run a representative
Subtract Background workflow and inspect its node badge: **GPU · cuCIM** proves
that invocation used cuCIM; **CPU** or **CPU fallback** remains a valid result
and includes the reason.

cuCIM 26.6.0 can print one line saying its optional CuPy distance test needs
cuVS and that it is falling back. The admitted VIPP operations do not use that
distance feature; `True 26.06.00` from the probe and a **GPU · cuCIM** badge are
the relevant success signals. Do not add an unpinned cuVS package merely to
silence that upstream message.

Keep the wheel and manifest private. They are local build records, not files to
upload, email to other users, or place on a shared package index.

## Distribution decision for 0.13.0a5

Every user who wants the optional Windows cuCIM provider builds and keeps their
own wheel and manifest using the fixed procedure above. VIPP will not host or
redistribute those wheels on `rensu.co.za`, GitHub Releases, PyPI, or a shared
package index. Do not reuse another user's wheel: rebuild it locally so its
manifest and per-build wheel hash describe the artifact you install. This
private local-build boundary is part of the 0.13.0a5 release contract.

Continue with [choose and verify CPU or GPU compute](../how-to/choose-compute.md)
for operation regions, fallback reasons, badges, and provenance.
