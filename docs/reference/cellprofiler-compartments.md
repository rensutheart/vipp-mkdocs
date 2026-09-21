# CellProfiler compartment profile

Use these stages to reproduce the **CellProfiler 4.2.6 settings** supplied with
the statistics paper. The [worked workflow](../workflows/statistics-paper-compartments.md)
shows how to connect them. This is a specific nuclei/cell/cytoplasm profile,
not an implementation of every CellProfiler module or setting.

!!! info "New in 0.16.0a1"
    The six profile nodes and **Grow Regions from Seeds — CellProfiler
    Propagation** require 0.16.0a1 or newer.

## Inputs and execution

Every input must have exactly **YX** spatial axes. Select a channel, time point
or Z plane explicitly, even when an extra axis has length one. Paired images
and labels must have the same shape and physical grid; nothing is resampled.
All distances and diameters below use **pixels**, not calibrated units.

Profile intensity inputs require **float32**, explicitly scaled to **0–1**.
For the paper's uint16 images, CellProfiler loads values with a denominator of
**65535**, rather than stretching each image's observed range. One float32
rounding step above 1 is accepted unchanged because CellProfiler's Gaussian
edge normalization can produce it. Larger values, negative values and NaN/Inf
are rejected. No profile node clips or rescales its guidance input.

Label inputs require non-negative integers fitting `int32`, with zero as
background; outputs use `int32`. Inputs are preserved. The nodes run on CPU.
**Segment Nuclei** and **Grow Regions from Seeds** use manual/cached execution;
click **Calculate** after their inputs or settings change. Cancellation is
checked before and after blocking library work.

## Nodes and settings

| Node | Inputs → output | Published setting and effect |
| --- | --- | --- |
| **Smooth — CellProfiler Gaussian** | Intensity → intensity | **Artifact diameter (pixels): 2**. Gaussian sigma is diameter / 2.35; constant-zero edges are normalized by the filtered valid mask. Output is float32. |
| **Threshold — CellProfiler Minimum Cross-Entropy** | Intensity → Boolean mask | **Threshold smoothing scale: 0** for the Actin mask. Global Li threshold, correction 1, bounds 0–1, no logarithm. |
| **Segment Nuclei — CellProfiler Shape** | Smoothed nuclear intensity → **Retained nuclei**, **Before filtering** | **Minimum diameter: 15**, **Maximum diameter: 50**, **Threshold smoothing scale: 1.3488**. Both outputs are needed downstream. |
| **Prepare Seeds — CellProfiler Propagation** | **Before filtering**, **Retained nuclei** → seed labels | Retains excluded border nuclei as competitors during growth; removes excluded interior nuclei. No tunable parameter. |
| **Finish Cell Regions — CellProfiler** | **Grown regions**, **Retained nuclei** → cell labels | **Fill labelled holes: enabled**. Maps regions back to retained nucleus IDs and removes regions belonging only to excluded nuclei. |
| **Extract Cytoplasm — CellProfiler** | **Cell labels**, **Nucleus labels** → cytoplasm labels | **Shrink nuclei before subtraction: enabled**. Keeps the one-pixel nuclear outline in the cytoplasm. |

The existing [Propagation node](seeded-segmentation.md#cellprofiler-propagation)
fits between Prepare Seeds and Finish Cell Regions, using smoothed Actin as
guidance, the prepared labels as seeds, the Actin threshold mask and
**Distance regularization: 0.05**. Its standalone intensity contract is broader
than this normalized float32 profile.

## Rules that affect numerical agreement

Threshold smoothing is applied **after calculating** the threshold. A scale of
1.3488 means a Gaussian sigma of 1. The comparison includes equality (`>=`),
and the Li convergence tolerance is at least 0.5 / 65536. Replacing this stage
with a generic Li threshold after blurring can change the mask.
Floating-point reductions can also differ across dependency versions near a
threshold boundary. Check intermediate masks as well as final labels; the
[validation record](validation-status.md#unreleased-cellprofiler-compartment-profile)
preserves the observed boundary-pixel differences.

The nuclear profile uses shape maxima and shape watershed with eight-neighbour
connectivity. It fills holes before and after declumping, uses automatic maxima
suppression with reduced-resolution maxima, and resolves distance-transform
ties with fixed random seed 0. The diameter range defines equivalent circular
areas. Border and size exclusions happen before the retained objects are
renumbered. The **Before filtering** output preserves the original competitors.
The node continues if more than 500 nuclei are detected.

Finish Cell Regions fills labelled holes and maps each grown region to the
largest retained nucleus ID overlapping it. Correctly connected outputs from
this profile preserve the nucleus/cell relationship. This stage does not remove
a cell just because the cell region touches the image border.

With nuclear shrinking enabled, nuclear boundary pixels occur in **both**
the Nuclei and Cytoplasm measurement regions. Simple Boolean subtraction of
all nuclear pixels produces a different compartment.

## Measurement definition and sources

Measure the **unsmoothed protein channel** in retained nuclei and cytoplasm.
The authors' analysis code computes:

`relative nuclear localisation = nuclear mean / (nuclear mean + cytoplasm mean)`

This gives equal weight to the two compartment means. It is not the fraction
of total intensity inside the nucleus and is not nuclear mean divided by
whole-cell mean. The supplementary prose describes a different denominator;
the executable author code is the reference for the reproduced table metric.

The profile comes from the authors' original `Experiment.csv` records, which
include embedded pipelines and identify CellProfiler 4.2.6:
[pinned author repository](https://github.com/FrancisCrickInstitute/Enhancing-Reproducibility/tree/a81d20c9393485e57395cd4a1be9e7ff83c7f11d).
The numerical implementation follows the
[CellProfiler 4.2.6 modules](https://github.com/CellProfiler/CellProfiler/tree/v4.2.6/cellprofiler/modules).
See [validation status](validation-status.md#unreleased-cellprofiler-compartment-profile)
for the distinction between runtime agreement and published-result agreement.
