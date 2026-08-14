# Validation status

This page summarizes the source-current evidence prepared for 0.13.0a7 and
keeps earlier release evidence separate. It is a claim boundary, not a
certificate that every node is validated for every assay.

## Evidence available now

- automated tests cover graph behavior, persistence, previews, export,
  operations, UI behavior, I/O routes, and bundled examples;
- architecture tests enforce the Qt-free `core/` dependency boundary, and
  focused tests cover stable source revisions, physical grids, detached
  snapshots, atomic persistence, typed execution, and stale-result rejection;
- 14 deterministic synthetic samples and 15 checked-in workflows support
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
  axis declarations, representative scientific preflight, restore without
  preview, inspected multi-series expansion and identity retention, direct
  plan-only execution, complete-item fast skips, transient
  atomic-write retries, and continuing after a final item-sidecar failure;
- compute tests cover import-safe CPU-only use, workflow-schema-4 and
  batch-schema-3 intent, eligibility planning, exact implementation identity,
  resident device segments, memory admission, classified fallback, optimizer
  review/apply and grouped result inspection, visible dtype-repair proposals,
  Prefer-GPU selection/serialization/UI/durable behavior, progress,
  cancellation, cleanup, and atomic publication; and
- opt-in native-Windows RTX tests exercise a real durable GPU batch and an
  imported generated Python workflow through the same executor.

## 0.13.0a7 prepublication qualification boundary

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

That result is production-backend lifecycle evidence, not acceptance of the
frozen EXE's visible setup window or a fresh/public-download installation. The
field checklist therefore leaves visual choices, shortcut launch presentation,
the GPU-tip Add conversion/Undo and post-calculation persistence checks,
Find-fastest grouped/readability inspection, SmartScreen, novice comprehension,
unusual account paths, cancellation, network rollback, and visible update
behavior as **not run**.

The local annotated tag has not been pushed. GitHub/PyPI publication, public
asset verification, the numbered manual, its live URL, and the updated stable
alias all remain **pending**. Fresh-account Unicode Known Folder,
public-download SmartScreen, novice-pilot, RTX 40-series Windows, and native
Linux CUDA field evidence remain **not run**. No a6 artifact, hash, URL, or
qualification record is reused as a7 evidence.

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
| I/O and metadata | Focused format, dtype, validation, and round-trip tests | A release-pinned field matrix and licensed corpus of representative microscope files |
| PSF/deconvolution | Deterministic 2D/3D synthetic images, measured-PSF samples, and operation tests | Real bead PSFs, representative microscopy images, artifact/noise analysis, performance characterization |
| Compute/GPU execution | Exact operation-region tests, immutable policy v8, tagged a4 source/artifacts, green cross-platform CI, a qualified private local cuCIM build, real RTX 5090 reference evidence, exact tagged-wheel RTX 4050 Auto/Prefer/all-example parity and cleanup, OOM/cancellation/cleanup coverage, and bounded M1 Max CPU plus Windows UI smokes | Qualify native Linux GPU, more NVIDIA architectures and compatible drivers, an Apple provider if pursued, and broader cross-platform manual GUI acceptance |
| Sources and physical grids | Revision-change, owned-snapshot, stale-worker, semantic-axis, scale/unit/origin, mask-broadcast, and image/PSF grid tests | Independent corpus covering live readers, network filesystems, registration histories, and heterogeneous microscope metadata |
| Large data/batch | Functional cache/path/memory tests plus deterministic attached/standalone config, planner, direct plan-only execution, source verification, complete-item fast skips, staging, retry, manifest/archive, sidecar, collision, replay, continuation, exact-output bundle, a bounded Windows acceptance pass, and bounded M1 Max CPU progress/cancellation evidence | Representative memory/time benchmarks, forced-process interruption studies, large collection stress tests, broader cross-platform/cloud-filesystem studies, semantic-axis iteration, and HCS traversal |
| Workflow/export architecture | Schema-4/schema-3 migration, batch-config/manifest schema 3, guarded source-axis declarations, optional batch-attachment validation, snapshot materialization, atomic-write failure, shared-executor compute provenance, multi-source binding, cancellation, and runtime-version tests | Independent reproducibility exercises across archived environments and long-lived release migrations |
| Usability | No release-pinned public usability study | Ethics-reviewed, preregistered task study with a controlled comparator and neutral outcomes |

## Release-specific limitations

- Workflow schemas 1 and 2 are intentionally rejected. Valid schema-3 workflows
  load as explicit CPU and save as schema 4; cached pixels/tables are not
  serialized and exported Python is runtime-version pinned. Recalculate,
  regenerate exports, and validate after upgrading.
- Version-1 batch configs load as explicit CPU; version-2 configs retain their
  saved compute request. Both older versions have no source-axis declaration
  until reviewed and saved as version 3. A saved Auto, Prefer GPU, or Custom
  request is intent; actual implementation
  provenance must be retained from each run. Auto uses reviewed GPU defaults
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
  [CPU/GPU matrix](../how-to/choose-compute.md#gpu-regions-in-0130a7) is a
  readable summary; the runtime policy/decision remains authoritative.
- cuCIM remains optional and omits Clara I/O. VIPP distributes no Windows
  wheel; each user builds the exact 26.6.0 tag/commit locally with the pinned
  recipe. Admission verifies that build's wheel-file hash, the policy-pinned
  canonical installed payload, source/recipe provenance, and the existing
  scientific environment/workload gates. This private per-user rebuild remains
  the planned 0.13.0a7 route, using only its matching bundle after publication;
  VIPP will not host or redistribute the wheel. Clara
  whole-slide I/O remains outside that build. See the
  [Windows CUDA guide](../getting-started/windows-cuda.md).
- Batch processing is local-file and sorted-position oriented. It does not
  iterate selected T/C/Z combinations or discover plate/well/field structure.
- Many operations are eager even when a source format supports lazy/chunked
  access; background execution improves responsiveness, not total work.
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
