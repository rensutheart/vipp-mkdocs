# Colocalization metric definitions

Use this reference to interpret exported columns and report the exact threshold
population. For graph setup and scatter controls, follow the
[colocalization tutorial](../workflows/colocalization-association.md).

!!! warning "Experimental Fiji compatibility"

    VIPP targets the source semantics of Fiji Coloc 2 3.1.0. Independent
    Fiji-generated golden parity is still pending; regression tests are not
    certification of cross-tool equivalence.

## Input Conventions

Colocalization nodes operate on two same-shaped scalar numeric image channels.
Split RGB/RGBA or multichannel fluorescence data into scalar channels before
connecting it to these nodes.

Quantitative calculations use the finite native intensity values supplied by
the upstream nodes. VIPP does not jointly rescale, clip, or replace values for
colocalization. Manual thresholds, Costes thresholds, regression parameters,
and intensity sums therefore use the same units as the two inputs. Inputs that
contain `NaN` or infinite values are rejected.

Negative values are retained, in
line with the source-aligned Coloc2 target, and produce text in the backward-
compatible `normalization_warnings` column because negative photon-count-like
values can make threshold and Manders results difficult to interpret.

Masked colocalization nodes accept a third ROI input. Voxels with ROI values
greater than zero are included; all other voxels are excluded. When no ROI mask
is supplied, all voxels are included.

## Thresholds And Positive Sets

Let `I1(i)` and `I2(i)` be the native channel intensities at voxel `i`.
Let `R` be the analysis population: either all voxels, ROI-restricted voxels,
or one labeled object. Let `T1` and `T2` be the selected channel thresholds.

VIPP defines:

```text
P1 = {i in R | I1(i) >= T1}
P2 = {i in R | I2(i) >= T2}
C  = P1 intersect P2
```

`P1` and `P2` are the threshold-positive voxels for each channel. `C` is the
colocalized voxel set. Table columns report `channel_1_positive_voxels`,
`channel_2_positive_voxels`, `colocalized_voxels`, and
`colocalized_fraction`. For whole-image and ROI analyses,
`colocalized_fraction = |C| / |R|`. For object-restricted analysis,
`colocalized_fraction = |C| / object_voxels`.

Manual thresholds use the threshold values supplied by the user. `Costes auto`
calculates `T1` and `T2` automatically, as described below, and writes the
calculated values back into the visible node parameters.

## Pearson Correlation

VIPP reports Pearson correlation for the selected intensity population:

```text
pearson(X, Y) =
  sum((X - mean(X)) * (Y - mean(Y)))
  / sqrt(sum((X - mean(X))^2) * sum((Y - mean(Y))^2))
```

For whole-image or ROI-restricted metrics, `pearson_all` is calculated over all
voxels in the analysis population `R`. For object-restricted metrics,
`pearson_object` is calculated over all voxels in the labeled object.
`pearson_no_threshold` is an explicit alias for the same quantity.

Fiji Coloc 2's thresholded Pearson populations use OR, not the intersection of
the two threshold-positive sets. VIPP's canonical exported field names state
that Boolean domain explicitly:

| Canonical field | Voxel population inside `R` |
| --- | --- |
| `pearson_no_threshold` | Every analysis voxel; thresholds are ignored. |
| `pearson_any_channel_below_threshold` | `I1 < T1 OR I2 < T2` (one or both channels are below). |
| `pearson_any_channel_above_threshold` | `I1 > T1 OR I2 > T2` (one or both channels are above). |
| `pearson_both_channels_at_or_above_threshold` | `I1 >= T1 AND I2 >= T2` (the threshold-positive intersection). |

`any` means *at least one*, not *exactly one*. Consequently, a mixed voxel
with one channel strictly above and the other below belongs to both Fiji OR
populations. They are overlapping populations, not complementary partitions.
A voxel exactly equal to both thresholds belongs to the intersection field but
to neither strict OR field. These comparisons implement the Boolean regions
identified in the Coloc2 3.1.0 source; independent golden parity is pending.

The ambiguous older names remain as compatibility aliases only:

| Compatibility alias | Canonical field |
| --- | --- |
| `pearson_below_threshold` | `pearson_any_channel_below_threshold` |
| `pearson_above_threshold` | `pearson_any_channel_above_threshold` |
| `pearson_both_above_threshold` | `pearson_both_channels_at_or_above_threshold` |
| `pearson_colocalized` | `pearson_both_channels_at_or_above_threshold` |

Likewise, `costes_pearson_any_channel_below_threshold` is the canonical name
for the final OR-domain correlation used during Costes threshold search;
`costes_pearson_below` remains its compatibility alias.

If fewer than two voxels are available, or if either channel has effectively
zero variance in the selected population, VIPP reports `NaN`.

Pearson values are intensity-correlation measurements. They do not by
themselves imply spatial overlap unless the analysis population and thresholds
are also reported.

## Manders Coefficients

VIPP targets the Manders definitions identified in Fiji Coloc 2's source.
Unthresholded M1/M2 use an
above-zero test in the opposite channel and the total intensity of the measured
channel as denominator:

```text
M1  = sum(I1(i) where I2(i) > 0) / sum(I1(i) for i in R)
M2  = sum(I2(i) where I1(i) > 0) / sum(I2(i) for i in R)
tM1 = sum(I1(i) where I2(i) > 0 and I2(i) >= T2) / sum(I1(i) for i in R)
tM2 = sum(I2(i) where I1(i) > 0 and I1(i) >= T1) / sum(I2(i) for i in R)
```

The explicit columns are `manders_m1_no_threshold`,
`manders_m2_no_threshold`, `manders_tm1`, and `manders_tm2`. Existing VIPP
workflows commonly select `manders_m1` and `manders_m2`; those names are kept
as compatibility aliases for `manders_tm1` and `manders_tm2` respectively.

The former VIPP quantities—intensity in `C` divided by intensity in `P1` or
`P2`—are not Manders coefficients. They remain available as
`fraction_ch1_above_threshold_intensity_in_both_above` and
`fraction_ch2_above_threshold_intensity_in_both_above`. Their sums are exposed
through `channel_1_positive_sum`, `channel_2_positive_sum`,
`colocalized_channel_1_sum`, and `colocalized_channel_2_sum`.

## Intensity Overlap Coefficient

VIPP reports an intensity overlap coefficient:

```text
overlap_coefficient(X, Y) =
  sum(X * Y) / sqrt(sum(X^2) * sum(Y^2))
```

For whole-image or ROI-restricted metrics, `overlap_coefficient_all` is
calculated over the full analysis population `R`. For object-restricted
metrics, `overlap_coefficient_object` is calculated over each labeled object.

`overlap_coefficient_colocalized` is calculated only over the colocalized voxel
set `C`. If the selected population is empty or both intensity norms are zero,
VIPP reports `NaN`.

This value is not the same as binary overlap or intersection-over-union. It is
an intensity-space similarity measure and should be interpreted alongside the
thresholded voxel counts and Manders coefficients.

## Costes Automatic Thresholding

When `Costes auto` is selected, VIPP uses an experimental source-aligned
implementation targeting Fiji Coloc 2 3.1.0's classic Costes `SimpleStepper` on
native intensities. This is the source path named `Costes`; Fiji's separate
`Bisection` implementation is not targeted by VIPP's existing `Costes auto`
workflow value.

For the selected threshold population, VIPP computes channel means, variances,
and covariance. Source alignment includes a cursor quirk observed in the 3.1.0
implementation: the means use the full ROI, but the regression variance loop
begins at the second ROI voxel because Coloc2 advances its cursor while
obtaining the first sample's numeric type. VIPP also models the source's
combined-variance covariance calculation and double accumulation. It fits a
line:

```text
I2 = slope * I1 + intercept
```

The slope is estimated from the sample variance/covariance terms using Fiji's
orthogonal-regression expression. Degenerate zero-covariance data is rejected
instead of inventing a regression line.

Threshold search proceeds along the fitted line. If `-1 < slope < 1`, the
working threshold starts at the observed channel-1 maximum and is mapped to
channel 2. Otherwise, it starts at the observed channel-2 maximum and maps back
to channel 1. Each candidate pair is rounded with Java `Math.round` semantics
and constrained only to the representable range of its source dtype—not to
`0..255`.

At each iteration, VIPP calculates Pearson correlation for the population:

```text
B = {i | I1(i) < T1 or I2(i) < T2}
```

After every test, the working threshold is decremented by one native intensity
unit. Following the 3.1.0 source target, the search stops when the decremented
working threshold is below one, the tested correlation is below `0.0001`, or
the correlation has increased relative to the previous test. The returned
thresholds are the last pair actually tested. There is no arbitrary
100-iteration cap.

This stopping rule assumes an analysis population with a meaningful
two-channel intensity relationship. If that assumption is not supported, the
first tested correlation can already satisfy the stop condition, leaving an
extreme threshold pair and very few joint-positive voxels. That is an unusable
automatic-threshold population for RACC, but it is not evidence that the
channels have no spatial overlap or co-occurrence; those are different
properties.

VIPP preserves the source-aligned result, exposes its values in the
read-only Costes threshold controls, and reports the failed threshold
population rather than silently replacing the fit. Review the scatter and
resolved thresholds, then use an appropriate reproducible alternative or
switch to `Manual` when justified. RACC requires at least two voxels passing
both thresholds and reports when that requirement is not met.

The output table records:

- `channel_1_threshold`;
- `channel_2_threshold`;
- `costes_slope`;
- `costes_intercept`;
- `costes_pearson_any_channel_below_threshold`;
- `costes_iterations`.

`costes_pearson_below` is retained as a compatibility alias for the canonical
OR-domain field above.

`threshold_units` is `native_intensity`. `coloc_semantics` records
`fiji_coloc2_3.1` as the target contract identity; it is not a validation
certificate. The separate `coloc_validation_status` field records
`experimental_source_aligned_golden_parity_pending` in both pixel and object
tables.

For object-restricted colocalization, Costes thresholds are calculated once
over all foreground voxels in the supplied label image and then reused for each
object. This makes object rows comparable and avoids unstable per-object
threshold estimates for small objects.

### Fiji Coloc 2 output scope

For metrics that both applications emit, VIPP's implementation is derived from
the Coloc2 3.1.0 source and targets its deterministic threshold, regression,
Pearson, and Manders semantics. Independent execution parity has not yet been
established, and the target is not a claim that the two applications produce
the same complete report bundle.

VIPP does not currently emit Coloc 2's zero-zero and saturation percentages,
per-channel min/max/mean/full-sum rows, intercept-to-mean warning text, Li ICQ,
Spearman statistics, randomized Costes significance test, or Fiji's projection,
histogram, log, and PDF artifacts. In particular,
`costes_pearson_any_channel_below_threshold` (and its compatibility alias
`costes_pearson_below`) is the correlation used during threshold search; it is
not the shuffled Costes P-value. The descriptive
`fraction_ch*_above_threshold_intensity_in_both_above` fields are also not
Manders tM1/tM2; use `manders_tm1` and `manders_tm2` for that comparison.

Randomized Costes significance is inherently a separately parameterized,
stochastic calculation. If added in a future release, its PSF/block size,
randomization count, and reproducibility policy must be recorded and validated
statistically rather than described as bitwise Fiji output parity.

## Validation Status

The implementation is covered by automated tests for whole-image/ROI metrics,
Costes threshold write-back, inspector scatter interaction, RACC outputs,
object-level metrics, label-overlap association, nearest-object distances,
event localization, and the bundled example workflows. Those tests are
internal regression coverage. They do not use independently generated Fiji
golden fixtures, so this alpha must not be cited as verified Fiji equivalence.

The bundled synthetic samples are deterministic and intended for software
regression and workflow demonstration. They do not replace biological
validation on real microscopy datasets. A manuscript should still include
representative biological datasets, parameter mappings, and comparison results
against relevant reference tools when making external numerical or biological
claims.

Related: [RACC-like index](racc-index.md), [object association](association-metrics.md),
and the [reporting checklist](../workflows/colocalization-association.md#reporting-checklist).
