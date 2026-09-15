# Plot measurement results

Turn object measurements into distributions, individual-point plots or scatter
plots without leaving VIPP.

!!! info "Unreleased — 0.16 development, after 0.15.0a5"
    **Plot Results** is new in development builds. These are descriptive plots,
    not statistical tests. Existing released workflows are unchanged.

## Start with one image

1. Label the structures, then calculate **Measure Objects** or **Measure
   Objects + Intensity**.
2. Connect the resulting table to **Plot Results**, under **Measurements →
   Tables**.
3. Choose a **Plot type** and **Measurement**. For a scatter plot, also choose
   **X measurement**.
4. Leave **Group by** unset and **Each point represents** set to **Objects**
   when each table row describes one object in this image.
5. Calculate the node, then choose **Open plot…** for a larger editable window.

Your workflow stays open behind the plot window. The inspector and plot window
edit the same saved settings; changing plot settings does not rerun the source
image or its measurements. Save the workflow to keep your choices. Recalculate
if the measurement table itself becomes stale.

While an update is queued, preparing measurements or calculating, the inspector
and plot window show an activity indicator and the current stage, not an
estimated percentage. Any previous drawing is out of date and cannot be
exported until the updated plot is ready.
The activity row stays reserved when its indicator is hidden, so starting and
finishing an update does not shift the plot or controls.

| Plot type | Use it to | Useful choices |
| --- | --- | --- |
| Compare groups | See individual measurements, with or without groups | Mean, median or no summary line; each visible point remains an observation. |
| Distribution | See which values are common or how many fall below a value | Histogram with shared bins, or Cumulative; histogram count or percentage. |
| Scatter | Compare two measurements, such as area and mean intensity | X and Y measurement; optional group colours. No fitted line or significance test is added. |

Axis titles use readable measurement names and show the declared unit once.
Long numeric tick labels are shortened for display without changing their
values. Category labels wrap, rotate or spread out to fit the window or export;
a note appears if some labels must be omitted. All groups remain plotted.
Click a point or choose **View plotted data…** to inspect exact group values.

Histogram **Count** axes and object measurements explicitly recorded in count
units, such as branch counts, use whole-number ticks. Percentages, cumulative
proportions and other measurements retain decimals where useful; **Mean per
image** can be fractional even when the original measurements are counts.

Missing, nonnumeric and non-finite measurements are not treated as zero;
review the included/excluded
counts. Logarithmic axes cannot show zero or negative values, and report those
exclusions. They do not change the original measurements.

### Choose categories or a numeric axis

**Compare groups** treats every distinct **Group by** value as a separate,
equally spaced category—even when the values are numbers. VIPP never silently
bins or merges those values, or changes your plot type. More than 12 numeric
groups triggers a warning to review this choice.

To compare two numeric measurements, choose **Scatter**, put the numeric field
in **X measurement**, and leave **Group by** unset or choose a category such as
treatment. This makes horizontal distances represent numerical differences.

## Try the guided example

Open **Morphology & Intensity Plots** in the example chooser. It contains one
image with 60 separated synthetic ellipses at **0.5 micrometer per pixel**.
Thresholding and labelling lead to shape and intensity tables, joined by label
ID, followed by four Plot Results nodes:

- **Area distribution:** inspect the range of object areas and try a different
  number of histogram bins.
- **Area–intensity scatter:** larger objects were deliberately made brighter.
  Change Y to `eccentricity` to explore shape instead of intensity.
- **Elongation points:** compare individual major-to-minor axis ratios with the
  median line. A ratio near 1 describes a more rounded ellipse.
- **Cumulative circularity:** read the fraction of objects at or below a chosen
  circularity value, without choosing histogram bins.

Click a point to inspect its source label/image identity where available.
**View plotted data…** opens the prepared values and source-row references.
For image means, one point can refer to several source rows.

These are invented demonstration data. The designed size–brightness relation
is not a biological finding, and 60 objects in one image are not automatically
60 independent biological samples.

## Use several images or conditions

For a completed batch, [collect the measurements](collect-measurement-results.md),
add condition/image annotations as needed, save a VIPP collection and open it
through **Table Source**. Connect that table to the same **Plot Results** node.

Choose **Group by** to compare conditions. **Each point represents** changes
the observational level:

- **Objects:** every eligible row contributes. Images containing more objects
  contribute more points to the pooled distribution and its summary.
- **Mean per image:** choose an **Image identity column**. VIPP first averages
  eligible values within each image, then plots one point per image. Image
  means receive equal weight in the displayed group summary.

Image means use the finite measurements before checking whether each mean
can appear on a logarithmic axis. A negative contributor is not silently
dropped to make the mean positive; non-positive image means are excluded
from a log view and reported separately.

Use globally distinguishing image IDs: a local object label is not an image
identity. Different groups cannot silently share one image ID. With a single
image, a mean-per-image plot naturally contains only one point.

An image is not necessarily an independent experimental sample either. The
right independent unit depends on how the experiment was sampled or treated.
Plot Results does not infer biological replication or perform statistical
tests. An empty image contributes no invented zero-valued object or mean;
review the collection's image summary separately for missing or empty images.

### If image means cannot be calculated

**Mean per image** needs one group per image. A **Group by** measurement such
as minor axis length can vary between objects in that image, so it cannot
define the image's group.

- For individual objects, set **Each point represents** to **Objects**.
- For image means, set **Group by** to **None**, or choose an image-level
  category such as treatment that is the same for every object in each image.
- If different images reuse an ID, choose an **Image identity column** that
  uniquely identifies each image.

The inspector and plot window show the problem beside the controls. Choose
**Review plot…** to reopen a failed plot; the compact workflow status offers
**Details…** for the full message. Correct the settings and calculate again.
VIPP does not silently regroup objects or change the averaging rule, and an
outdated plot stays unavailable for export.

## Export a figure

Choose **Export figure…** from a current plot. Set **Width** and **Height** in
millimeters, independently of the on-screen window size.

- **PNG/TIFF:** choose the raster resolution in DPI.
- **SVG/PDF:** save a vector figure for layout/editing software.
- Optionally include a **CSV** of plotted values and a **JSON** settings
  sidecar to describe the selected fields, grouping and preparation.

Exports use a light publication background. Calculating or opening a plot does
not save files; export requires an explicit destination. A stale plot cannot
be exported as a current result. Keep the original measurement table and
workflow alongside any figure you share.

Paired/time-course views, object-count/fraction plots, confidence intervals and
inferential tests are not part of this first plotting release.
