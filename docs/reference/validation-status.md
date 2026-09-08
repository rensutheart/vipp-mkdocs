# Validation status

This page preserves exact release evidence and keeps changed-domain
qualification separate from carried-forward scientific and installer records.
It is a claim boundary, not a certificate that every node, reader, or workflow
is validated for every assay.

## Unreleased RL GPU admission with advisories

Nightly builds after 0.15.0a2 broaden RL/RL-TV GPU execution to the
[authored ranges and PSF options](../how-to/choose-compute.md#unreleased-rl-and-rl-tv-gpu-ranges)
without requiring a CPU comparison before execution. Numerical-difference
advisories identify settings outside the earlier prequalified region and are
retained in execution provenance.

This is an execution-policy change, not a claim of CPU equivalence throughout
the new region. Even-sized PSFs can change convolution centering. Historical
benchmarks below retain their original settings and environments; they do not
qualify every newly admitted combination. Memory, runtime, finite-input and
geometry checks still apply. Optional benchmark/optimizer comparisons keep
their own acceptance criteria.

## 0.15.0a2 scope and evidence

The [0.15.0a2 release](https://github.com/rensutheart/napari-vipp/releases/tag/v0.15.0a2) is the canonical source for exact assets, checksums and qualification records. This page describes scope; it does not assert a check passed without its release evidence.

Changed areas include included native-reader dependencies and guided setup, update discovery, workflow/search/display controls, threshold directions and ranges, intensity inversion and numeric guards, Convex Hull, and the mesh-object lifecycle from extraction to export. Dependency and packaging changes require clean-install checks; Windows and the two native macOS architectures have separate qualification boundaries. Changed GPU threshold and shared compute/provenance behavior need matching evidence; unchanged provider kernels may retain earlier evidence only within their recorded environment and contract.

Reader diagnostics verify support loading, not a vendor acquisition's pixels, axes or calibration. Mesh extraction and refinement are CPU, full-resolution operations; smoothing and approximate simplification change geometry. Mesh tests and synthetic examples do not establish biological validity, complete self-intersection detection or print readiness. Existing mesh inputs are measured directly on CPU; the label-morphology GPU route remains hybrid.

Use the [current operation matrix](../how-to/choose-compute.md#gpu-regions-in-0150a2) and each node's admitted region. No Apple GPU execution, general lazy/chunked graph execution, signed/notarized installers or broad assay validation is claimed. Earlier exact records below remain historical; their asset hashes must not be applied to a2 downloads.

## 0.15.0a1 scope and evidence

The [0.15.0a1 release](https://github.com/rensutheart/napari-vipp/releases/tag/v0.15.0a1)
is the canonical source for its exact assets, checksums, application revision,
and release qualification evidence. Do not apply the older asset hashes below
to a 0.15.0a1 download.

This release changes batch execution and cancellation, configuration version 6,
the inspector and diagnostic plots, source/axis presentation, and mesh/skeleton
measurement providers. These changed areas need their own regression or
device evidence; an unchanged CUDA installation alone does not qualify a new
provider. Unaffected scientific regions retain their documented boundaries.

The hybrid mesh path performs label preparation on GPU but retains CPU marching
cubes, convex hulls, and table construction. Analyze Skeleton's device path
measures an already-authored Boolean skeleton, not GPU thinning. See the
[current operation matrix](../how-to/choose-compute.md#gpu-regions-in-0150a1).

The new synthetic threshold gallery and exhaustive inspector example add
review coverage, not independent biological validation. The ImageJ Default
implementation and Fiji-related colocalization methods retain their stated
experimental source-aligned status; external golden parity is not implied by
the UI refresh or version change.

## 0.14.0a3 exact application and artifact record

The annotated `v0.14.0a3` tag resolves to
[`3c61d0c84cc728d90537ae10c4c521e4a4f40809`](https://github.com/rensutheart/napari-vipp/commit/3c61d0c84cc728d90537ae10c4c521e4a4f40809).
The [exact-main application CI](https://github.com/rensutheart/napari-vipp/actions/runs/33257954476),
[Windows installer smoke](https://github.com/rensutheart/napari-vipp/actions/runs/33257982020),
and [native macOS arm64/x86_64 smoke](https://github.com/rensutheart/napari-vipp/actions/runs/33257983570)
passed at that commit. The
[exact-tag unsigned-installer workflow](https://github.com/rensutheart/napari-vipp/actions/runs/33259296811)
then passed for Windows x86_64, macOS arm64, and macOS x86_64.

The [GitHub prerelease](https://github.com/rensutheart/napari-vipp/releases/tag/v0.14.0a3)
contains exactly 20 qualified assets: the wheel and source archive, four Windows
files, seven Apple Silicon files, and seven Intel macOS files. Independent
CPython 3.12.10 builds of the exact-tag wheel and source archive matched before
publication. The
[PyPI publication workflow](https://github.com/rensutheart/napari-vipp/actions/runs/33263567839)
passed, and freshly downloaded [PyPI files](https://pypi.org/project/napari-vipp/0.14.0a3/)
matched the exact GitHub release bytes.

| Public artifact | SHA-256 |
| --- | --- |
| Wheel `napari_vipp-0.14.0a3-py3-none-any.whl` | `7231ab13c76ab8bb2926d0e1569eb527491b392d36dba6b888d4eec03ba616e2` |
| Source archive `napari_vipp-0.14.0a3.tar.gz` | `185bb25e19f8e04ed47df5c45993ac52153c53c5b1c14e4d7c79010d84558cad` |
| Windows installer `VIPP-Setup-0.14.0a3-Windows-x86_64-UNSIGNED.exe` | `8774dd14047cb31f3694a30c05878ff59e50fe2e3f5f200d09e13082eed30d73` |
| Apple Silicon package `VIPP-0.14.0a3-macOS-arm64-UNSIGNED.pkg` | `69b62fd576bdba9c2002457107ea46cd99b6a5cf091558b35281c99cd57f4100` |
| Intel package `VIPP-0.14.0a3-macOS-x86_64-UNSIGNED.pkg` | `5b97d530a58df9f1d3a873e2f22036bcfa6d62d50cbd22b960b063c76e249d73` |

This is application and artifact evidence. The numbered and stable
documentation deployment is verified separately after this exact manual is
deployed.

## 0.14.0a3 changed-domain qualification scope

0.14.0a3 changes core/UI behavior, workflow schema and provenance, local
OME-Zarr source-window planning and memory preflight, shared execution
coordination, napari/Qt compatibility, installer dependency inputs, and
documentation. Qualification must cover responsive Z/Y/X Crop Stack behavior,
opt-in low-RAM crop repair, exact sole-direct source-window parity and refusal
cases, safe interactive and batch bypass, save/undo behavior, workflow schema 6
and batch config/manifest schema 5 migrations, napari 0.6/0.9/latest boundaries,
PyQt6/PySide6 startup, and exact-tag Windows plus both native macOS packages.

GPU provider kernels and their admitted scientific regions are unchanged. Their
recorded catalogue evidence may carry forward only if the a3 shared-execution
checks and changed-domain declaration pass. General branch-aware region
planning, remote or non-OME-Zarr exact reads, general lazy/chunked execution,
Apple GPU support, signed/notarized installers, and broad assay validation are
not claimed.

## Previous exact record: 0.14.0a2 focused qualification boundary

0.14.0a2 changes desktop/Qt compatibility, detached-window sizing, and release
packaging. It adds separate offline CPU-only macOS packages for Apple Silicon
and Intel. SourceItem, reader, workflow schema 5, batch config/manifest schema
4, OME-Zarr preview, per-sample parameter, scientific operation, and GPU
contracts are unchanged from 0.14.0a1 and retain that recorded evidence.

The annotated `v0.14.0a2` tag resolves to
[`4aaf9961b97259c94390c859374d8a6b9f45ec6c`](https://github.com/rensutheart/napari-vipp/commit/4aaf9961b97259c94390c859374d8a6b9f45ec6c).
The [exact-tag CI run](https://github.com/rensutheart/napari-vipp/actions/runs/33048422781)
passed, including the supported Windows, Linux, and macOS Python matrix and
clean distribution installs. The
[unsigned-installer workflow](https://github.com/rensutheart/napari-vipp/actions/runs/33048446173)
passed for Windows x86_64, macOS arm64, and macOS x86_64. Its native macOS jobs
inspected, installed, launched, and cleanly shut down each final package. The
[PyPI publication workflow](https://github.com/rensutheart/napari-vipp/actions/runs/33048727450)
also passed.

The [GitHub prerelease](https://github.com/rensutheart/napari-vipp/releases/tag/v0.14.0a2)
contains 20 assets. Primary public artifact SHA-256 values are:

| Artifact | SHA-256 |
| --- | --- |
| GitHub wheel `napari_vipp-0.14.0a2-py3-none-any.whl` | `a30aa4ff1f4882b06903800d60912be4f6b29f185716a1752b3f8c540690ae8c` |
| GitHub source archive `napari_vipp-0.14.0a2.tar.gz` | `8d1bf13b752bdb4c6777076c5e6bda5a75275073016f15e347ed8698e6b01886` |
| Windows installer `VIPP-Setup-0.14.0a2-Windows-x86_64-UNSIGNED.exe` | `cdab2be65b83c36260ba45b3b700bc1685287e665bb9558585f9f13f9fb3f3be` |
| Apple Silicon package `VIPP-0.14.0a2-macOS-arm64-UNSIGNED.pkg` | `9ad6a01e614277a4abac501a27d8623da5bd22bf4184bfb7b0884c319b67f529` |
| Intel package `VIPP-0.14.0a2-macOS-x86_64-UNSIGNED.pkg` | `15ddfa6378af4bdf69887d35bd107b04143d89a944e68686687f350532546d14` |

The two macOS packages require macOS 13 or newer, are current-user-only,
explicitly unsigned and unnotarized, and install CPU-only managed environments.
Automated native lifecycle evidence does not establish browser-quarantine,
managed-device override, signing/notarization, graphical update/uninstall, or
Apple-accelerator support.

!!! warning "PyPI a2 is a different, earlier build"
    PyPI cannot replace uploaded files. Its a2 wheel
    (`3b066887de739d600a684abf85d599832d5b92c83fb357b6c75a471ed20cd2a8`)
    and source archive
    (`ad72ae95a5595c8bcad6125aada8aab1c30a419b98929a91b405d3560405fd27`)
    are the pre-resize-fix build and do not match the current GitHub release
    wheel/source bytes. Use a platform installer or the GitHub wheel for the
    detached-window fix, and record which distribution surface was used.

This is application and artifact evidence. It does not itself claim that the
numbered or stable documentation deployment succeeded.

## 0.14.0a1 SourceItem and batch qualification boundary

The changed release domains are SourceItem identity and migration,
reader-contract normalization, local OME-Zarr presentation preview, typed
per-sample batch values and retained-workspace UX, source-load preflight, and
installer capacity/activity presentation. Qualification uses focused core/UI,
reader, schema/migration, preview, override, and installer-presentation checks,
the integrated release suite, the strict verified-cache public corpus profile,
and exact-tag package and installer checks.

This scope does not claim remote stores, IMS pyramid preview, HCS traversal,
operation-level lazy execution, broad optional-reader equivalence, or
per-sample expressions/source selectors/topology changes. The lower OME-Zarr
level is presentation-only; scientific analysis remains level 0. The unchanged
full GPU catalogue and installer transactional lifecycle retain their recorded
0.13 evidence rather than being silently counted as newly rerun.

Exact public packages and the immutable release assets are available from the
[v0.14.0a1 GitHub release](https://github.com/rensutheart/napari-vipp/releases/tag/v0.14.0a1)
and [PyPI](https://pypi.org/project/napari-vipp/0.14.0a1/).
The annotated tag resolves to
[`e16ca87161ec7b1041a5e98c5a2bf786b11a1ec8`](https://github.com/rensutheart/napari-vipp/commit/e16ca87161ec7b1041a5e98c5a2bf786b11a1ec8);
[exact-main CI](https://github.com/rensutheart/napari-vipp/actions/runs/32975633514),
the [exact-main installer build](https://github.com/rensutheart/napari-vipp/actions/runs/32975659650),
and the [PyPI publication workflow](https://github.com/rensutheart/napari-vipp/actions/runs/32982120913)
passed. The strict public-corpus manifest SHA-256 is
`3365b4cec7a220f6399f3c030eb3ac751581bde730fac60f01c9fca3b823714d`.
Exact distribution hashes are recorded in the
[0.14.0a1 release-verification table](../releases/0.14.0a1.md#release-verification).
This application evidence does not claim a documentation deployment result.

## 0.13.0a9 qualification boundary

Final a9 application source is commit
[`d476c8976c91679faaaf0fe196c90b1ab4d63458`](https://github.com/rensutheart/napari-vipp/commit/d476c8976c91679faaaf0fe196c90b1ab4d63458).
Its
[exact-main CI](https://github.com/rensutheart/napari-vipp/actions/runs/32825042433)
and
[Windows installer build smoke](https://github.com/rensutheart/napari-vipp/actions/runs/32825073086)
passed. Focused acceptance covered immediate QYX-to-ZYX Gaussian metadata,
explicit volumetric skeletonization, actionable GPU VRAM preflight, stable
sibling measurement caches, and Prefer GPU planning through CPU-only nodes.

On the release workstation, the original affected workflow completed under
Prefer GPU with the reviewed downstream CuPy/CuPyX operations on `cuda:0` and
no fallback across required CPU-only boundaries. This is bounded evidence for
that environment, not a universal device or installation claim.

Installer transaction behavior, dependency/toolchain pins, and release
infrastructure did not change. Their lifecycle evidence therefore carries
forward from a8 rather than being replayed. The a9 tag nevertheless regenerated
and checked the exact frozen payload, embedded wheel, version, `NotSigned`
state, manifests, hashes, GitHub assets, and PyPI bytes. See the
[a9 release-verification table](../releases/0.13.0a9.md#release-verification).

## 0.13.0a8 qualification boundary

Final a8 application source is commit
[`5a66ae9d1098ca5a8d409a4075c585692e3c3638`](https://github.com/rensutheart/napari-vipp/commit/5a66ae9d1098ca5a8d409a4075c585692e3c3638).
Its
[exact-main CI run](https://github.com/rensutheart/napari-vipp/actions/runs/32584690313)
passed all 13 jobs: quality/package checks, the full tests on Windows, Linux,
and macOS with CPython 3.12 and 3.13, and clean wheel/source-archive
installation lanes. The
[Windows installer smoke](https://github.com/rensutheart/napari-vipp/actions/runs/32585512509)
also passed against that commit.

The public GPU catalogue declares **19 implementations** and **24 executable
evidence owners**. The full native-Windows RTX 5090 `cuda:0` qualification
passed all of them. Its aggregate evidence SHA-256 is
`0365366dc23750e000c6e9c4f8b384cdf706afdcb338ae3a9f80cfad3d1d8506`.
The evidence source was candidate commit
`7189cf40280d895b61b061f1468767164ccfbcf4`; the only subsequent
executable-code change was the packaging canonicalizer. Other changes recorded
evidence and documentation and did not alter production GPU code.

Risk-based installer acceptance exercised the a8 behavior affected by this
release. Updating the existing managed CUDA installation from a7 to a8 left
zero cuCIM, `nvimgcodec`, or retired-provider residue in active a8
`site-packages`; `pip check` was clean; Compute Doctor passed **19 of 19**
implementations; and the visible application reported VIPP 0.13.0a8. Both new
CuPy measurement implementations passed parity, cancellation, reuse, and
zero-private-pool-residue checks. The a7 rollback was deliberately preserved.

The separate cuCIM installer, source-build coordinator, private-wheel approval
path, and hosted provider asset were removed. The redundant fresh CPU,
installer-cancellation, same-version repair, and uninstall matrix was not
repeated for this minor alpha; those unperformed paths are not claimed as a8
passes. Exact public artifacts and publication evidence are recorded in the
[a8 release-verification table](../releases/0.13.0a8.md#release-verification).

## Evidence available now

- automated tests cover graph behavior, persistence, previews, export,
  operations, UI behavior, I/O routes, and bundled examples;
- architecture tests enforce the Qt-free `core/` dependency boundary, and
  focused tests cover stable source revisions, physical grids, detached
  snapshots, atomic persistence, typed execution, and stale-result rejection;
- strict public-corpus v4 qualification covers 20 frozen artifacts (210.41 MiB),
  97 biological fields, and the claimed OME-Zarr, TIFF, ND2, LIF, CZI/LSM,
  OIR/OIB/VSI, and IMS routes. All 10 strict vendor cases passed, including the
  IMS case under portable Temurin 21. The corpus-manifest SHA-256 is
  `3365b4cec7a220f6399f3c030eb3ac751581bde730fac60f01c9fca3b823714d`;
- 15 deterministic synthetic samples and 19 checked-in workflows support
  regression checks and inspection;
- a generated two-source batch bundle exercises three paired items, nine exact
  NPY/TIFF/TSV outputs, workflow/config hashes, source identities, manifests,
  archives, and three finalized item sidecars;
- an analytical phantom report exercises calibrated object/mesh morphology;
- method notes and focused tests cover colocalization calculations;
- tables, CSV/TSV writing, workflow JSON, and Python generation have automated
  behavior checks;
- focused UI/execution tests cover isolated-tuning boundaries, actionable and
  waiting stale states, progressive node previews, compatible layer reuse, and
  rejection of stale contrast/histogram results;
- batch tests cover attached-config validation and round-trip, guarded source-
  axis declarations, representative scientific preflight, background
  source checking on restore without calculating representative pixels, inspected
  multi-series expansion and identity retention, direct
  plan-only execution, complete-item fast skips, transient
  atomic-write retries, and continuing after a final item-sidecar failure.
  The current batch suite additionally covers individual existing-output
  choices, reused Run preflight, selection and reset semantics, cooperative
  cancellation, node progress, and the readable report;
- compute tests cover import-safe CPU-only use, workflow-schema-6 and
  batch-config-6 intent, migration from workflow schemas 3/4/5 and batch
  versions 1/2/3/4/5, eligibility planning, exact implementation identity,
  resident device segments, memory admission, classified fallback, optimizer
  review/apply and grouped result inspection, visible dtype-repair proposals, Prefer-GPU
  selection/serialization/UI/durable behavior, progress, cancellation,
  cleanup, and atomic publication; and
- opt-in native-Windows RTX tests exercise a real durable GPU batch and an
  imported generated Python workflow through the same executor.

## Historical 0.13.0a7 published qualification boundary

Final a7 application source merged to `main` through
[pull request #23](https://github.com/rensutheart/napari-vipp/pull/23) at
[`dc8a63912110a75ab1daad0e7f81c2b20e5001e6`](https://github.com/rensutheart/napari-vipp/commit/dc8a63912110a75ab1daad0e7f81c2b20e5001e6).
Its exact-main
[CI run](https://github.com/rensutheart/napari-vipp/actions/runs/31830397900)
passed on Windows, Linux, and macOS. The complete local suite passed **5,084
tests**, with **5 documented skips**, **2 documented expected failures**, and
zero failures.

The clean-source native-Windows RTX 5090 `full` GPU admission profile passed
all **23 executable evidence owners** across **18 public implementations**.
The aggregate evidence SHA-256 is
`3ad655f7d3e36055449bda3e8bb41c914e010fd7607ced26763e23045dcee7ae`,
and its admission-manifest SHA-256 is
`3b6081b0aec45f81227bd86d86bc0f2df1aa4fe6b28752aa4e96aaee3d8e0ce7`.
The new evidence covers exact dtype conversion,
Binary Threshold, Extract Channel, Boolean Remove Small Objects, and Boolean
Fill Holes across parity, difficult inputs, metadata, unchanged inputs, memory,
cancellation, cleanup, fallback, provenance, and end-to-end timing contracts.

Source-current native-Windows RTX 5090 checks exercised a single resident path
from the visible dtype conversion through filtering, thresholding, Boolean
cleanup, and Connected Components. One retained terminal output used one upload
and one final download; retaining an intermediate deliberately added another
download. These are bounded development/reference-system results, not a support
claim for every GPU or a downloaded public artifact.

The exact-source wheel, source archive, unsigned Windows installer and
sidecars, and no-wheel cuCIM bundle were finalized and hash-locked locally.
Their filenames and SHA-256 values are recorded in the
[a7 release-verification table](../releases/0.13.0a7.md#release-verification).
Twine accepted both Python archives; deterministic-wheel and byte-reproducible
cuCIM-bundle checks passed; isolated wheel and source-archive installations
passed package, resource, entry-point, manifest, and headless checks; and
unsigned installer finalization plus native `NotSigned` inspection passed.

A display-independent exact-artifact acceptance exercised the production
Windows installer engine and registration/removal services from the final a7
wheel, bound to the finalized unsigned EXE. CPU and CUDA each completed a new
install, installed-package scientific checks, repair, and ownership-safe
uninstall. The CUDA route additionally passed Compute Doctor with **14 of 18**
public regions admitted, the portable segmentation corridor, 3D RL and RL-TV,
and the non-ASCII effective-TEMP compiler regression. Both routes removed their
owned environments, registry entries, shortcuts, cached a7 setup, and
transaction residue.

That result is production-backend lifecycle evidence; by itself, it did not
operate the frozen EXE's setup window. Separately, on 2026-08-15, the operator
attested that the exact locally finalized EXE's visible setup and installed-UI
checks passed. The attestation covered visible shortcut launch, the GPU-tip Add
conversion/Undo and post-calculation persistence checks, and grouped
Find-fastest result readability.

The local operator pass was not a fresh-account or public-download
installation. The field checklist therefore leaves public-download
SmartScreen, novice comprehension, unusual account paths, cancellation,
network rollback, and update from an older release as **not run**.

The public `v0.13.0a7` tag peels to the exact qualified commit. The official
GitHub prerelease contains exactly seven assets; a fresh download of every asset
matched the recorded SHA-256. The protected
[PyPI workflow](https://github.com/rensutheart/napari-vipp/actions/runs/31871324192)
published only the already-qualified wheel and source archive, and both public
PyPI digests matched. The
[numbered-manual workflow](https://github.com/rensutheart/vipp-mkdocs/actions/runs/31871275481)
succeeded and all required 0.13.0a7 URLs returned HTTP 200. Stable-alias
[workflow 31871941473](https://github.com/rensutheart/vipp-mkdocs/actions/runs/31871941473)
succeeded; at that deployment, public `versions.json` mapped `stable` to
`0.13.0a7`, and the required stable URLs returned HTTP 200 with no stale
prepublication wording.

Fresh-account Unicode Known Folder, public-download SmartScreen, novice-pilot,
RTX 40-series Windows, and native Linux CUDA field evidence remain **not run**.
No a6 artifact, hash, URL, or qualification record is reused as a7 evidence.

## Historical 0.13.0a6 qualification and field boundary

The source candidate's complete local suite passed **4,572 tests**, with **5
documented skips**, **2 documented expected failures**, and zero failures.
Clean wheel and source-archive installations passed in fresh environments, and
the cross-platform workflow now checks both distribution forms across Windows,
Linux, and macOS on the supported Python versions.

On the native-Windows RTX 5090 reference environment, Compute Doctor 2.0
admitted all **13 of 13** current public GPU regions. The strict quick admission
profile passed **130 of 130** mapped checks across all 16 executable
implementation owners, including parity, difficult inputs, metadata, unchanged
inputs, memory, cancellation, cleanup, fallback, provenance, and
transfer-inclusive timing evidence.

The final clean-tag RTX 5090 run also passed the strict `full` admission
profile for **16 of 16** executable owners, **13** public implementations, and
all **10** contract facets. Its aggregate evidence SHA-256 is
`44bd66033afedcbece8d8746e1779d833af2897ac230adc4e8a98d7847f7f56c`.

This is strong engineering evidence for the source candidate, not a substitute
for testing the downloaded installer elsewhere. The
[Windows field checklist](../getting-started/windows-field-acceptance.md)
therefore retains fresh-account CPU/CUDA installation, spaces and non-ASCII
account paths, cancellation and network rollback, repair/update/uninstall, an
RTX 40-series machine, and a novice first workflow as explicit field checks.
Anything not performed remains **not run**.

The immutable `v0.13.0a6` tag resolves to application commit
[`859738a28354981ba784d9e49a04cb6e1158a79f`](https://github.com/rensutheart/napari-vipp/commit/859738a28354981ba784d9e49a04cb6e1158a79f).
Its exact-source
[CI run](https://github.com/rensutheart/napari-vipp/actions/runs/31673890530)
passed on Windows, Linux, and macOS. The tagged wheel, source archive, cuCIM
local-build bundle, and Windows sidecars passed the release qualification
gates. Independent Windows inspection confirmed that the explicitly unsigned
installer is `NotSigned`, with no signer or timestamp certificate. Exact
artifact hashes are recorded in
[0.13.0a6 release verification](../releases/0.13.0a6.md#release-verification).

The public
[GitHub pre-release](https://github.com/rensutheart/napari-vipp/releases/tag/v0.13.0a6)
contains exactly seven assets whose published SHA-256 digests match the release
table. The public [PyPI release](https://pypi.org/project/napari-vipp/0.13.0a6/)
has matching wheel and source-archive hashes. The numbered-manual
[deployment workflow](https://github.com/rensutheart/vipp-mkdocs/actions/runs/31678254836)
succeeded, and its required numbered pages returned HTTP 200.

Publication and clean-tag GPU qualification do not replace the downloaded
installer field checklist. External fresh-machine and novice acceptance remain
**not run** unless a tester records them explicitly.

## Historical 0.13.0a5 installer acceptance and release boundary

The release application commit is
[`067c89559072fbbb101e9d63b91514345e5896e6`](https://github.com/rensutheart/napari-vipp/commit/067c89559072fbbb101e9d63b91514345e5896e6),
merged through [release PR #16](https://github.com/rensutheart/napari-vipp/pull/16).

The development installer passed fresh managed CPU and CUDA installation, real
Auto and Prefer-GPU execution with CPU parity and clean accelerator release,
optional cuCIM installation and execution, update and repair, and independent
CPU/CUDA removal on the Windows reference system. The DEVELOPMENT file is not a
release artifact. The final tagged release route created only the explicit
`-UNSIGNED` filename from the immutable tag's exact wheel after build bytes,
frozen payload, `NotSigned` status, release manifest, and SHA-256 checks passed.

The exact tagged release EXE then passed a clean installer-owned CPU lifecycle:
reviewed/hash-locked resolution, install, package health, shortcuts, responsive
first launch, transactional same-version repair, safe refusal while one DLL was
temporarily locked, and complete removal after the application closed. A local
build has no browser Mark-of-the-Web, so acceptance did not synthesize a
SmartScreen page. The user guide documents the expected **Unknown publisher**
and **Windows protected your PC** warning for browser downloads, the safe
**More info** → **Run anyway** path, checksum verification, and managed-device
fallback. The filename without `-UNSIGNED` remains reserved for a future valid
Authenticode-signed and timestamped installer.

Final CI, tag, signing status, and artifact hashes are recorded in
[0.13.0a5 release verification](../releases/0.13.0a5.md#release-verification).

## Historical 0.13.0a4 release source and artifacts

The immutable annotated
[`v0.13.0a4`](https://github.com/rensutheart/napari-vipp/releases/tag/v0.13.0a4)
tag resolves to application commit
[`4bec1e8145b31e161beaf44a290bff24aea36f5e`](https://github.com/rensutheart/napari-vipp/commit/4bec1e8145b31e161beaf44a290bff24aea36f5e)
on `main`. Its exact-source
[CI run](https://github.com/rensutheart/napari-vipp/actions/runs/31300028320)
passed package, manifest, lint, wheel smoke, and CPython 3.12 and 3.13 tests on
Windows, Linux, and macOS.

The final local source suite completed with **4,018 passed**, **109 expected
skips**, **2 documented expected failures**, and zero failures. The clean
tagged wheel and source distribution passed Twine and content inspection. The
publication artifacts are:

| Artifact | SHA-256 |
| --- | --- |
| `napari_vipp-0.13.0a4-py3-none-any.whl` | `5FA75FC48955E2CA9AD7D5BC13218AD83EF14C23F0B72F74D8A7486CA8453085` |
| `napari_vipp-0.13.0a4.tar.gz` | `B99B829C45BE734B705DEE17829886EF91DEAABC3C3D3C5F76C164DB87A617AF` |

The exact tagged wheel was installed into an isolated overlay over the pinned
native-Windows CUDA 13 environment. On an NVIDIA GeForce RTX 4050 Laptop GPU
(compute capability 8.9), Auto and Prefer GPU selected eligible
CuPy/CuPyX/cuCIM implementations. All 13 bundled examples completed as fresh
CPU, Auto, and Prefer-GPU graphs; every selected GPU node passed its declared
production parity contract, no fallback record was emitted, and cleanup
succeeded. Provider probes also passed for CuPy, CuPyX, and the approved local
cuCIM build.

This complements the retained RTX 5090 evidence rather than turning either
machine into a model allowlist. Public a4 admission accepts a probed NVIDIA CUDA
device with compute capability 7.5 or newer and driver API 13.3 or newer while
retaining the exact supported native-Windows, CPython 3.12, CUDA runtime 13.2,
scientific-stack, provider-provenance, workload, memory, fallback, and cleanup
gates. Minor floating-point differences can occur across GPU models, drivers,
compiler paths, and reduction order within a provider's declared tolerance;
record the full environment and validate consequential work against CPU.

## Historical 0.13.0a1 release source and artifacts

The immutable
[`v0.13.0a1`](https://github.com/rensutheart/napari-vipp/releases/tag/v0.13.0a1)
tag resolves to application commit
[`7520a5bb3ea9fe296bb231c63d1598b833ac10f6`](https://github.com/rensutheart/napari-vipp/commit/7520a5bb3ea9fe296bb231c63d1598b833ac10f6)
on `main`. Its exact-source
[CI run](https://github.com/rensutheart/napari-vipp/actions/runs/31112153743)
passed package, manifest, lint, distribution-metadata, installed-wheel smoke,
and CPython 3.12 and 3.13 tests on Windows, Linux, and macOS. The CI-built
distributions are qualification outputs, not publication artifacts.

On native Windows, the exact selected source's complete local suite completed
with **4,077 passed**, **2 skipped**, **2 documented expected failures**, 83
warnings, and zero failures. The skips are the opt-in real-CUDA tests and the
expected failures are the documented CuPy integer-parity gaps. The exact source
was then covered by the cross-platform CI matrix above.

The final tagged artifacts published through
[PyPI](https://pypi.org/project/napari-vipp/0.13.0a1/) and attached to the
GitHub pre-release are:

| Artifact | SHA-256 |
| --- | --- |
| `napari_vipp-0.13.0a1-py3-none-any.whl` | `C157D2D0E5909A76A1A6093493AB17A245682DF53D83DD0A23FAA0FDF7A3BE02` |
| `napari_vipp-0.13.0a1.tar.gz` | `E3231CF22EA2907C3FE05F73477E5E3CD3B10FF2A053BBA92A8045D140E7F7E0` |

The bundled synthetic-volume example was launched from a clean, non-editable,
release-style Windows environment, and the operator explicitly accepted its
appearance. A separate headless Prefer-GPU smoke selected
`cucim-subtract_background-v2` for Subtract Background without fallback,
returned a `(31, 37)` native-`uint16` result, and reported clean accelerator
cleanup. This is bounded evidence for one example and one declared cuCIM
operation region, not broad manual GUI, reader, filesystem, hardware, or assay
qualification.

The pinned private Windows cuCIM route was exercised against upstream tag
`v26.06.00` at commit
`3c15781c207eab93a317dd9803a6e726fe01f7c4`. Two clean builds from the exact
41-distribution no-dependency lock produced byte-identical wheel files and the
policy-pinned canonical payload
`d640d1e17bcce15d32d03841997252bf915b63da855e406c35f0d70c5a5ea667`.
Metadata, licenses, exact file inventory, install-helper admission, `pip check`,
and a real GPU import/runtime probe passed. This locally built wheel remains
private: VIPP neither ships nor hosts it, and each user must repeat the pinned
build for their own environment.

These are the release files. The historical artifacts below must not be
uploaded or substituted for them.

The earlier pre-Prefer-GPU candidate at application commit `e024409` passed
package/manifest, lint, and CPython 3.12 and 3.13 CI on Linux, Windows, and
macOS. The candidate
wheel and source distribution built and passed Twine metadata checks; a clean
CPU-only wheel environment passed installation/import checks, and the installed
CUDA wheel environment passed compute-doctor plus the two opt-in real-CUDA
durable batch/generated-Python tests. A green CI/package matrix is not
equivalent to a manual GUI smoke pass on every operating system, Qt/display
environment, filesystem, microscope reader, or GPU. See the
[candidate CI run](https://github.com/rensutheart/napari-vipp/actions/runs/30945609407).
Those results remain evidence for that exact tree, but the Prefer-GPU source
change invalidates it as the final release candidate.

The later automated checkpoint is application commit
[`444f68290fe4359b05c68a027d3ae0a413412fe5`](https://github.com/rensutheart/napari-vipp/commit/444f68290fe4359b05c68a027d3ae0a413412fe5)
on `codex/gpu-cross-platform-support`. Its full local suite completed in 299.65
seconds with **3,754 passed, 2 skipped, 2 xfailed, 83 warnings, and zero
failures**. The skips are the opt-in real-CUDA durable batch smokes. The xfails
are the documented CuPy `uint8`/`uint16` integer-parity gaps. Ruff, source and
installed-wheel npe2 manifest validation, package build, Twine, and the
installed-wheel resource smoke passed. These counts describe that exact
historical tree only. Subsequent compute-lifecycle, optimizer, source-loading,
generated-CLI, and cleanup-quarantine hardening changed application behavior,
so `444f682` is superseded and is not the current release candidate.

The checkpoint's real RTX 5090 Prefer-GPU integration test passed and selected
CPU Extract Channel, cuCIM Subtract Background, CPU native-`uint16` Gaussian,
and CuPyX Median without per-node overrides. The complete pipeline had exact
parity, no fallback, and clean accelerator cleanup. This verifies the automated
placement contract for that environment; manual Prefer-GPU UI acceptance is
still pending.

The exact historical checkpoint artifact hashes are:

- wheel: `58b08cbb8396c9fe27d28a69d52b06e160817e58987e6dc3b8c5059f3dae9804`;
- source distribution:
  `00fcb15452d3ed71d344859d4306cbcdcc458686959169a2c47485d8f7abec9b`.

These artifacts must not be uploaded for 0.13.0a1. They are superseded by the
tagged `7520a5b` release source and final hashes above. See the
[release notes](../releases/0.13.0a1.md#historical-prefer-gpu-automated-checkpoint-superseded)
for the historical artifact table.

A bounded source-candidate smoke on 4 August 2026 used application commit
`e024409` on an Apple M1 Max (`arm64`) running macOS 26.5.2. Manual checks
covered launch/basic CPU processing, collection-batch progress and cooperative
cancellation, and memory presentation as one system-RAM budget without a
fabricated VRAM total. Four focused tests additionally covered the
CPU-safe cancel path, worker-token propagation, single-shot UI cancellation,
retained cancelled state, manifest, and cleanup evidence. The follow-up
operator record is commit
[`ff21040`](https://github.com/rensutheart/napari-vipp/commit/ff210402629a7d1f790a48d1f2dfc0f86861ddba).
This is bounded source-checkout evidence, not a raw test log, clean-wheel Mac
qualification, broad reader/display/filesystem coverage, or Apple GPU evidence.

A bounded manual Windows acceptance pass inherited from 0.12.0a3 covered direct
unpreviewed batch execution, complete `Skip` items, continued processing after
an item failure, attached-config save/reload, and a representative 3D
deconvolution batch. It does not establish cross-platform behavior, broad
filesystem interoperability, large-collection scalability, or restoration
quality for arbitrary samples.

On 4 August 2026, the operator also reported a bounded native-Windows napari UI
smoke pass on the later `ff21040` development checkout. A local schema-4
Custom workflow loaded the representative private ND2 acquisition and
exercised the intended channel, slice navigation/display behavior, and
backend-badge presentation. The retained last-run JSON was subsequently
overwritten by an Auto run, so it does not independently preserve the exact
mixed-backend assignment or cleanup result. This is operator-attested UI
regression evidence only; it is not Prefer-GPU, final-wheel, durable-replay, or
broad Windows/GPU qualification.

The `e024409` full local suite passed **3,722 tests**, with **2
skipped**, **2 documented expected failures**, and 83 warnings. The two final
real-CUDA durable execution tests passed when enabled. These numbers describe
that earlier candidate checkout. Preserve them as historical evidence, but do
not use them as final-release counts. Use the release-source and final-artifact
results above for 0.13.0a1 qualification.

The recorded native-Windows RTX 5090 evidence records operation-level
scientific parity, memory, progress/cancellation, cleanup, and timing for the
declared public GPU regions. The source-candidate timing refresh measured
Richardson-Lucy at 24.898/0.414 seconds CPU/GPU (60.20x) on the private ND2
volume, 35.997/0.455 seconds (79.14x) on the medium synthetic volume, and
137.820/1.517 seconds (90.87x) on the large synthetic volume. Richardson-Lucy
TV measured 34.921/0.599 seconds (58.34x) on the private volume and
55.936/0.564 seconds (98.61x) on the medium volume; both RL-TV workloads
reported parity and clean cleanup. These are descriptive machine-local results,
not portable performance guarantees or durable Auto assignments.

The release's generated calibrated-morphology report records **28/28 checks
passed**. Its own scope excludes broad numerical equivalence, biological
interpretation, and all data conditions. The application test suite checks that
the report remains synchronized with the validation script.

## Do not generalize this evidence into

- usability superiority over other tools;
- broad equivalence to Fiji, CellProfiler, scikit-image, or another package;
- scalability to whole-slide or high-content datasets;
- complete OME/acquisition metadata fidelity;
- biological validity of a segmentation, restoration, or measurement workflow;
- user-study evidence beyond explicitly described pilot observations.

## High-priority evidence gaps

Passing deterministic tests is valuable internal evidence, but it is not the
same as an external comparison or assay validation. The distinction matters:

| Area | Current in-repository evidence | Next evidence needed |
| --- | --- | --- |
| Watershed/object separation | Touching-disk split tests, exported-workflow execution, and 3D-default behavior tests | Broader 3D phantoms, split/merge metrics, external comparison, representative real images |
| Colocalization/association | Deterministic metric, overlap, distance, and association tests plus synthetic examples | External numerical comparisons and assay-specific positive/negative controls |
| Skeleton networks | Synthetic network workflows and focused operation tests | Prespecified topology and calibrated-length packs, perturbation tests, external comparison |
| I/O and metadata | Focused format, dtype, validation, and round-trip tests plus strict public-corpus v4 qualification across 20 frozen artifacts, 97 biological fields, and the claimed microscope-reader routes | Broader independent facility files, negative controls for unusual vendor dimensions, network/remote filesystems, and cross-reader comparisons outside the frozen corpus |
| PSF/deconvolution | Deterministic 2D/3D synthetic images, measured-PSF samples, and operation tests | Real bead PSFs, representative microscopy images, artifact/noise analysis, performance characterization |
| Compute/GPU execution | Exact operation-region tests, immutable policy v10, regenerated a3 full-catalogue qualification for 19 CuPy/CuPyX implementations and 24 evidence owners on native Windows RTX 5090, focused a9 and 0.14 shared-planner/source-axis real-GPU evidence, OOM/cancellation/cleanup coverage, bounded M1 Max CPU and Windows UI smokes, a3 exact-main Windows and native macOS smokes, and exact-tag three-platform installer qualification | Qualify native Linux GPU, more NVIDIA architectures and compatible drivers, an Apple provider if pursued, and broader cross-platform manual GUI acceptance |
| Sources and physical grids | Revision-change, owned-snapshot, stale-worker, semantic-axis, scale/unit/origin, mask-broadcast, and image/PSF grid tests | Independent corpus covering live readers, network filesystems, registration histories, and heterogeneous microscope metadata |
| Large data/batch | Functional cache/path/memory tests plus deterministic attached/standalone config, planner, direct plan-only execution, source verification, complete-item fast skips, staging, retry, manifest/archive, sidecar, collision, replay, continuation, exact-output bundle, a bounded Windows acceptance pass, and bounded M1 Max CPU progress/cancellation evidence | Representative memory/time benchmarks, forced-process interruption studies, large collection stress tests, broader cross-platform/cloud-filesystem studies, semantic-axis iteration, and HCS traversal |
| Workflow/export architecture | Workflow schema 6 with explicit schema-3/4/5 migration, batch config 6 and manifest 5 with supported earlier-version migration, canonical SourceItems, typed per-sample overrides, exact-item output choices, safe authored and batch bypass intent, guarded source-axis declarations, attachment validation, snapshot materialization, atomic-write failure, shared-executor compute provenance, multi-source binding, cancellation, and runtime-version tests | Independent reproducibility exercises across archived environments and long-lived release migrations |
| Usability | No release-pinned public usability study | Ethics-reviewed, preregistered task study with a controlled comparator and neutral outcomes |

## Release-specific limitations

- Workflow schemas 1 and 2 are intentionally rejected. Valid schema-3 workflows
  load as explicit CPU, while schema-4 and schema-5 workflows retain authored
  compute intent. Schema 5 also retains canonical SourceItems; schema-4 sources
  acquire them when they resolve. Supported earlier files save as schema 6, and
  nodes without authored bypass intent default to Run. Cached pixels/tables are
  not serialized and exported Python is runtime-version pinned. Recalculate,
  regenerate exports, and validate after upgrading.
- Version-1 batch configs load as explicit CPU; version-2 configs retain their
  saved compute request; and version-3 configs retain guarded source-axis
  declarations and acquire SourceItems when resolved; version 4 adds SourceItems
  and typed numeric overrides. Earlier versions have no batch execution-profile
  override and are written as version 6 only after review and save. A saved
  Auto, Prefer GPU, or Custom request is intent; actual
  implementation provenance must be retained from each run. Auto uses reviewed GPU defaults
  without compatible history; accelerated-only history schedules one
  same-surface CPU measurement before a later matching run applies the
  1.20x/20-ms gate. Prefer GPU instead requests
  every reviewed eligible accelerator regardless of speed; Custom owns per-node
  choices and benchmarking.
- GPU candidates cover only declared operation/dtype/parameter/shape/memory and
  environment regions. Public admission requires native Windows, CPython 3.12,
  the pinned CUDA 13.2/scientific/provider stack, driver API 13.3 or newer, and
  a probed NVIDIA CUDA device with compute capability 7.5 or newer. macOS is
  CPU-only in this release; the bounded M1 Max CPU smoke above does not admit an
  Apple accelerator. The
  [CPU/GPU matrix](../how-to/choose-compute.md#gpu-regions-in-0150a1) is a
  readable summary; the runtime policy/decision remains authoritative.
- The current public GPU catalogue uses CuPy/CuPyX. See the
  [Windows CUDA guide](../getting-started/windows-cuda.md).
- Batch processing remains local-file and pairs source lists positionally,
  although each resolved item is pinned to a canonical SourceItem rather than
  being silently reassigned by a changed series order. It does not iterate
  selected T/C/Z combinations or discover plate/well/field structure.
- Most operations are eager even when a source format supports lazy/chunked
  access. One strictly eligible direct local OME-Zarr Crop Stack can read only
  its exact retained level-0 window; other graphs retain full-read memory
  preflight. Background execution improves responsiveness, not total work.
- Declared-grid validation cannot prove biological registration or metadata
  truth. It can only enforce the axes/calibration supplied to VIPP.
- Richardson-Lucy/TV controls and synthetic tests do not establish a validated
  restoration parameter range for a real microscope or assay.
- Manifest and item sidecar writes improve recovery evidence but are not one
  transaction across all outputs and provenance files.
- Cooperative progress/cancellation cannot split an opaque library call or file
  writer into truthful internal percentages.
- Revised native-intensity colocalization is a source-aligned compatibility
  implementation targeting Fiji Coloc 2 3.1.0, but independent numerical
  parity validation is pending. The ImageJ threshold path similarly targets
  ImageJ 1.54p for scalar `uint8`, `uint16`, and `float32`; Boolean and RGB/RGBA
  handling are VIPP extensions and are not claimed as ImageJ-exact. Treat both
  paths as experimental and validate externally before consequential use.

## For your workflow

Use [validate a workflow](../scientific-practice/validation.md) to choose
assay-specific evidence. If a public claim depends on a gap above, label it as a
limitation or produce the required evidence before making the claim.
