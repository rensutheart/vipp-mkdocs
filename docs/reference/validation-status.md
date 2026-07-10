# Validation status

This page summarizes the evidence shipped with the 0.11.0a1 application source.
It is a claim boundary, not a certificate that every node is validated for
every assay.

## Evidence available now

- automated tests cover graph behavior, persistence, previews, export,
  operations, UI behavior, I/O routes, and bundled examples;
- 13 deterministic synthetic samples and 12 checked-in workflows support
  regression checks and inspection;
- an analytical phantom report exercises calibrated object/mesh morphology;
- method notes and focused tests cover colocalization calculations;
- tables, CSV/TSV writing, workflow JSON, and Python generation have automated
  behavior checks.

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
| Large data/batch | Functional batch, cache, path, and memory-guard tests | Memory/time benchmarks, interruption recovery, saved configuration, per-item provenance |
| Usability | No release-pinned public usability study | Ethics-reviewed, preregistered task study with a controlled comparator and neutral outcomes |

## For your workflow

Use [validate a workflow](../scientific-practice/validation.md) to choose
assay-specific evidence. If a public claim depends on a gap above, label it as a
limitation or produce the required evidence before making the claim.
