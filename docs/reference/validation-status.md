# Validation status

This page summarizes the evidence shipped with the 0.13.0a1 application source.
It is a claim boundary, not a certificate that every node is validated for
every assay.

## Evidence available now

- automated tests cover graph behavior, persistence, previews, export,
  operations, UI behavior, I/O routes, and bundled examples;
- architecture tests enforce the Qt-free `core/` dependency boundary, and
  focused tests cover stable source revisions, physical grids, detached
  snapshots, atomic persistence, typed execution, and stale-result rejection;
- 13 deterministic synthetic samples and 13 checked-in workflows support
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
- batch tests cover attached-config validation and round-trip, restore without
  preview, direct plan-only execution, complete-item fast skips, transient
  atomic-write retries, and continuing after a final item-sidecar failure;
- compute tests cover import-safe CPU-only use, workflow-schema-4 and
  batch-schema-2 intent, eligibility planning, exact implementation identity,
  resident device segments, memory admission, classified fallback, optimizer
  review/apply, progress, cancellation, cleanup, and atomic publication; and
- opt-in native-Windows RTX tests exercise a real durable GPU batch and an
  imported generated Python workflow through the same executor.

The 0.13.0a1 candidate at application commit `e024409` passed package/manifest,
lint, and CPython 3.12 and 3.13 CI on Linux, Windows, and macOS. The candidate
wheel and source distribution built and passed Twine metadata checks; a clean
CPU-only wheel environment passed installation/import checks, and the installed
CUDA wheel environment passed compute-doctor plus the two opt-in real-CUDA
durable batch/generated-Python tests. A green CI/package matrix is not
equivalent to a manual GUI smoke pass on every operating system, Qt/display
environment, filesystem, microscope reader, or GPU. See the
[candidate CI run](https://github.com/rensutheart/napari-vipp/actions/runs/30945609407).

A bounded manual Windows acceptance pass inherited from 0.12.0a3 covered direct
unpreviewed batch execution, complete `Skip` items, continued processing after
an item failure, attached-config save/reload, and a representative 3D
deconvolution batch. It does not establish cross-platform behavior, broad
filesystem interoperability, large-collection scalability, or restoration
quality for arbitrary samples.

The 0.13 source-current full local suite passed **3,722 tests**, with **2
skipped**, **2 documented expected failures**, and 83 warnings. The two final
real-CUDA durable execution tests passed when enabled. These numbers describe
one release-candidate checkout and should be paired with the final tagged
commit's CI and artifact-smoke results before publication.

The source-current native-Windows RTX 5090 evidence records operation-level
scientific parity, memory, progress/cancellation, cleanup, and timing for the
declared public GPU regions. Recent large-stack Richardson-Lucy examples ranged
from about 63x to 88x CPU/GPU speedup and Richardson-Lucy TV examples from about
60x to 100x on that one machine. These are descriptive machine-local results,
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
| GPU execution | Exact operation-region tests, immutable policy/evidence records, one installed-wheel native-Windows RTX 5090 environment, real durable batch/generated-export smokes, OOM/cancellation/cleanup coverage, and clean CPU-wheel validation | Native Linux, RTX 40-series Windows, broader clean-host GPU/wheel environments and drivers/runtimes, Apple-provider study, and cross-platform manual GUI acceptance |
| Sources and physical grids | Revision-change, owned-snapshot, stale-worker, semantic-axis, scale/unit/origin, mask-broadcast, and image/PSF grid tests | Independent corpus covering live readers, network filesystems, registration histories, and heterogeneous microscope metadata |
| Large data/batch | Functional cache/path/memory tests plus deterministic attached/standalone config, planner, direct plan-only execution, source verification, complete-item fast skips, staging, retry, manifest/archive, sidecar, collision, replay, continuation, exact-output bundle, and a bounded Windows acceptance pass | Representative memory/time benchmarks, forced-process interruption studies, large collection stress tests, cross-platform/cloud-filesystem studies, semantic-axis iteration, and HCS traversal |
| Workflow/export architecture | Schema-4/schema-3 migration, batch-config/manifest schema 2, optional batch-attachment validation, snapshot materialization, atomic-write failure, shared-executor compute provenance, multi-source binding, cancellation, and runtime-version tests | Independent reproducibility exercises across archived environments and long-lived release migrations |
| Usability | No release-pinned public usability study | Ethics-reviewed, preregistered task study with a controlled comparator and neutral outcomes |

## Release-specific limitations

- Workflow schemas 1 and 2 are intentionally rejected. Valid schema-3 workflows
  load as explicit CPU and save as schema 4; cached pixels/tables are not
  serialized and exported Python is runtime-version pinned. Recalculate,
  regenerate exports, and validate after upgrading.
- Version-1 batch configs load as explicit CPU and save as version 2. A saved
  Auto/Selective request is intent; actual implementation provenance must be
  retained from each run. Standard interactive, saved-batch, and generated
  execution in 0.13.0a1 attaches no local performance evidence, so fresh Auto
  candidates stay CPU; reviewed UI GPU assignments are Selective.
- GPU candidates cover only declared operation/dtype/parameter/shape/memory and
  environment regions. The initial public gate is one exact native-Windows RTX
  5090/CUDA 13/CPython 3.12 stack. macOS is CPU-only in this release.
  The [CPU/GPU matrix](../how-to/choose-compute.md#gpu-regions-in-0130a1) is a
  readable summary; the runtime policy/decision remains authoritative.
- cuCIM's source-built Windows `skimage` wheel is not a general install route
  and omits Clara I/O. Feature-complete cuCIM packaging remains pending.
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
