# Statistics methods and counts

This reference defines the new descriptive **Statistics** recipe. For steps,
see [Summarize measurements](../how-to/summarize-measurements.md).

!!! info "New in 0.16.0a1"
    The new recipe is version 2. Older **Summarize Measurements** workflows
    retain version 1 until explicit upgrade. The node's saved operation
    identity remains `summarize_measurements`.

[Results Workspace](../how-to/results-workspace.md) and the inspector edit
the same saved Statistics recipe. A summary selected as a plot input remains
a table of summary rows, not the original object/image/sample observations.
The workspace does not add inference, implicit SD error bars or a second
summary calculation behind the table view.

## Measurement selection

**Auto-select measurements** discovers columns containing real numeric
measurements, excluding recognized identity/metadata columns and the selected
group, image and sample identity fields. It follows changes in the upstream
table rather than saving the current list of names. Numeric-looking text is
not converted into a measurement.

**Select all** turns off automatic selection and saves the exact currently
eligible field names as a manual selection. It does not bulk-select fields
marked **not automatic**. **Select none** also turns automatic selection off
and leaves an empty manual selection; it never falls back to automatic mode.
At least one measurement must be selected before calculation. Manual
selections retain their exact names; a missing saved field must be reviewed,
not silently replaced by another column.

## Descriptive methods

All methods operate on the selected units: eligible objects, image means or
sample means. Counts and sums therefore change meaning with the level.

| Method | Definition |
| --- | --- |
| Count | Number of eligible summarized units, not always number of objects. |
| Mean | Arithmetic mean of those units. |
| Median | Middle sorted value, or average of the middle pair. |
| Sample SD | Square root of the sum of squared deviations from the mean divided by `n − 1`; undefined for fewer than two units. |
| Q25 / Q75 | Linear-interpolated 25th/75th percentiles. |
| IQR | Q75 minus Q25. |
| Minimum / maximum | Smallest/largest eligible unit value. |
| Sum | Sum of the selected units; a sum of image/sample means is not the raw object total. |

Sample SD describes spread. It is not a confidence interval, and “sample” in
its mathematical name does not assert that the observations are independent.
For at least two identical values, sample SD is zero.

The numerical definitions follow NumPy's
[sample SD with `ddof=1`](https://numpy.org/doc/stable/reference/generated/numpy.std.html)
and [linear quantiles](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html).
No tests, p-values, ANOVA, significance labels or confidence intervals are
included in this scope.

## Invalid values and identities

The saved missing-value policy either excludes invalid measurements with
counts or raises an error. Missing values, non-finite numbers (`NaN`, positive
or negative infinity), and nonnumeric values are reported separately. Text
such as `"12"` is not silently converted into a numeric measurement. Integers
that cannot be represented exactly for the calculation are rejected rather
than silently rounded.

Required identity/group fields must be present and unambiguous regardless of
the measurement exclusion policy. Image means require image identity; sample
means require sample identity, plus image identity for equal-image weighting.
An averaged image/sample must have a consistent group; object-level categories
within an image are allowed. A supplied image ID cannot belong to several
samples.
VIPP does not invent biological samples, resolve conflicting annotations,
transform values, remove outliers or convert measurement units.

Image identity repeats across object rows from one image and distinguishes
different images across the collection. Sample identity links the images of
one declared experimental sample. When an identity is marked **optional
counts**, it adds counts without changing the selected averaging level or
weighting. See [choosing identities](../how-to/summarize-measurements.md#choose-image-and-sample-identities)
for examples.

For multiple selected measurements, eligibility is checked separately. One
measurement can have a smaller included count than another in the same group.

### Empty and singleton groups

A group without eligible values has count zero; all other numeric summaries,
including sum, are unavailable rather than zero. A singleton has undefined
sample SD but defined mean, median, quartiles, range and sum. Status text
explains the missing values and insufficient data.

An empty table has no automatically discoverable measurements: select the
intended columns explicitly. With no grouping, its result is one zero-count
row. With grouping, there are no observed groups and hence no result rows.

## Read the wide result table

Each output row describes a selected group. Statistic columns are named
`<measurement>_<statistic>`, such as `area_mean` and `area_std`. Their units
remain those of the input measurement, except for counts. Distinct source
units remain distinct columns; they are not mixed into one unlabelled value.

| Result field | Meaning |
| --- | --- |
| `row_count` | Input rows in this group, before measurement exclusions. |
| `<measurement>_object_total`, `_object_valid`, `_object_excluded` | Total input objects and eligible/excluded measurements. |
| `<measurement>_missing_count`, `_nonfinite_count`, `_nonnumeric_count` | Reasons for measurement exclusion. |
| `<measurement>_n` | Number of eligible units actually summarized at the chosen level. |
| Image/sample total and valid counts, when identity is supplied | Distinct represented identities versus identities with an eligible value for this measurement. |
| `<measurement>_status` | Explains absent values or insufficient data for sample SD. |
| `summary_version`, `summary_level`, `sample_weighting` | Calculation version, selected level and within-sample weighting. |
| `group_by`, `image_column`, `sample_column`, `missing_policy`, `statistics_recipe` | Fields and policy used, plus the saved descriptive recipe. |

Counts describe rows in this input table, not all attempted images in a batch.
Zero-row images remain in the collection's inventory and image-summary export;
they cannot appear as invented objects in a Statistics input table.

Keep the original measurements and workflow with an exported summary. A
summary alone cannot recover within-image variation or prove independence.
