# Plot measurement results

Turn object measurements into distributions, individual-point plots or scatter
plots without leaving VIPP.

!!! info "New in 0.16.0a1"
    **Plot Results** provides descriptive plots, not statistical tests.
    Opening a plot does not change an existing summary recipe.

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

For controls beside tables, summaries and figures in one window, choose
**Open Results Workspace…**. Its **Plots** view edits the same Plot Results
node. The top selection bar (**Workflow → Data source → Statistics node →
Plot**) lets you activate any open workflow and browse its connected nodes
without changing graph connections; choose **None — use input
data** for plots directly connected to the data source. Tabs only change the
view. **Change plot input…** opens controls to deliberately reconnect the
selected plot; see [Results Workspace](results-workspace.md#choose-what-the-plot-uses)
before interpreting the plotted values.

**Plot settings** groups the measurement, grouping and observation choices.
**Appearance** contains the title, axis and styling controls. Bold text marks
these section headings; individual field labels use regular text. Its outlined
chevron points right when collapsed and down when expanded, and stays readable
in light and dark themes across the inspector, plot window and Results Workspace.

The node's optional **Name** is for navigating the workflow and Results
Workspace. It does not replace the figure's **Title** under **Appearance**.
Without a custom name, VIPP uses a meaningful figure title or derives a label
from the selected plot settings. See [Name a node](edit-graph.md#name-a-node).

In Results Workspace, the figure fits the available preview area while the
settings scroll independently. Use the title-bar **Maximize** button, resize
the window or drag the divider for a
larger preview. This changes only the on-screen view, not the data, saved plot
recipe or exported figure size.

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

### Set grid and axis-label spacing

Under **Appearance**, leave **X axis label interval** and **Y axis label
interval** on **Auto** to let VIPP choose readable spacing. Uncheck **Auto**
and enter a positive interval for evenly spaced numeric labels and matching
grid lines: for example, `100` for area ticks at 100-unit steps or `2` for count
ticks at two-count steps.

This changes the axis markings, not histogram bins, measurements or summary
values. The same saved interval is used in the inspector, plot window,
Results Workspace and exported figures.

- Count axes require whole-number intervals of at least 1.
- The **Compare groups** horizontal axis is categorical, so numeric X
  intervals do not apply. Category label spacing remains automatic.
- Logarithmic axes use **Auto**; switch the corresponding interval to Auto
  before using a log scale. A saved incompatible interval is reported rather
  than silently replaced.
- If a custom interval would make the axis too dense, increase it or use
  Auto. VIPP does not silently substitute a different custom interval.

Missing, nonnumeric and non-finite measurements are not treated as zero;
review the included/excluded
counts. Logarithmic axes cannot show zero or negative values, and report those
exclusions. They do not change the original measurements.

### Choose categories or a numeric axis

**Compare groups** treats every distinct **Group by** value as a separate,
equally spaced category—even when the values are numbers. VIPP never silently
bins or merges those values, or changes your plot type. More than 12 numeric
groups triggers a warning to review this choice.

Read the highlighted warning beside the plot before interpreting it. Warning
text adapts to light/dark themes and wraps to the inspector width, expanding
vertically so the full message remains available.

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

For a reusable descriptive summary table, use
[Statistics](summarize-measurements.md) with explicit object/image/sample
aggregation. Paired/time-course views and object-count/fraction plots are not
included here. Confidence intervals and inferential tests are outside the
0.16 results scope; they are not a promised next phase.
