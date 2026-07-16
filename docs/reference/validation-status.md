# Validation status

This page summarizes the evidence shipped with the 0.12.0a2 application source.
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
  behavior checks; and
- focused UI/execution tests cover isolated-tuning boundaries, actionable and
  waiting stale states, progressive node previews, compatible layer reuse, and
  rejection of stale contrast/histogram results.

Release CI covers package/manifest, lint, and test behavior on Linux and
Windows. A passing CI matrix is not equivalent to a manual GUI smoke pass on
every operating system, Qt/display environment, filesystem, or microscope
reader.

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
| Sources and physical grids | Revision-change, owned-snapshot, stale-worker, semantic-axis, scale/unit/origin, mask-broadcast, and image/PSF grid tests | Independent corpus covering live readers, network filesystems, registration histories, and heterogeneous microscope metadata |
| Large data/batch | Functional cache/path/memory tests plus deterministic saved config, planner, source verification, staging, manifest/archive, sidecar, collision, replay, and exact-output bundle | Representative memory/time benchmarks, forced-process interruption studies, large collection stress tests, semantic-axis iteration, and HCS traversal |
| Workflow/export architecture | Schema-3 rejection/round-trip, snapshot materialization, atomic-write failure, shared-executor export, multi-source binding, and runtime-version tests | Independent reproducibility exercises across archived environments and long-lived release migrations |
| Usability | No release-pinned public usability study | Ethics-reviewed, preregistered task study with a controlled comparator and neutral outcomes |

## Release-specific limitations

- Workflow schema 1 and 2 are intentionally rejected; 0.12.0a2 has no automatic
  migration.
- Valid 0.12.0a1 schema-3 workflows load structurally, but cached pixels/tables
  are not serialized and exported Python is runtime-version pinned. Recalculate,
  regenerate exports, and validate after upgrading.
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

## For your workflow

Use [validate a workflow](../scientific-practice/validation.md) to choose
assay-specific evidence. If a public claim depends on a gap above, label it as a
limitation or produce the required evidence before making the claim.
