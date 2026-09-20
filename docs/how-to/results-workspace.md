# Explore results in one workspace

Keep measurement tables, descriptive summaries and plots beside their controls
in **Results Workspace**, without replacing your workflow nodes.

!!! info "Unreleased — 0.16 development, after 0.15.0a5"
    Results Workspace brings existing table, Statistics and Plot Results
    tools into one window. It does not add statistical tests or change their
    calculation methods.

## Open the workspace

1. Calculate a table-producing node, such as **Measure Objects**, **Merge
   Tables** or **Table Source**.
2. Select it and choose **Open Results Workspace…** in the inspector.
   You can also open the workspace from **Statistics** or **Plot Results**.
3. Use the selection bar above the tabs: **Workflow → Data source → Statistics
   node → Plot**. Matching blue arrows join all four selectors. Bold headings
   and a subtle border highlight this global connection bar, which stays
   visible in every view.
4. Choose **Data**, **Summary** or **Plots** using the full-width icon tabs.
   Tabs change the view, not the selected source, summary or plot. Controls
   are on the left and the relevant table or figure is on the right.

Use the window's title-bar **Maximize** button for more room. **Restore**
returns it to its previous size; both actions leave the analysis unchanged.

Choose the chain you want to explore:

- **Workflow** lists every open workflow. Selecting one activates its workflow
  tab and lists its table sources. Repeated workflow names include their tab
  number so you can tell them apart. A workflow with no table-producing nodes
  remains selectable and explains why no data sources are available.
- **Data source** identifies an exact table output, including its named port
  when relevant. Filtered and merged tables remain separate choices from
  their upstream measurements.
- **Statistics node** selects a summary connected to that table. Choose
  **None — use input data** to work directly with the selected table instead.
- **Plot** lists only plots directly connected to the selected Statistics
  output, or to the data source when Statistics is **None**. If none exist,
  VIPP shows **No connected plots**, not a plot from another branch.

The relationship caption confirms the selected chain. These selections change
what you browse; they do not edit graph connections. Settings changes,
**+** actions and calculations apply to the selected workflow. The editing
heading identifies the node for the current tab, and **Show node** locates it
in the workflow.

Selectors use descriptive node names instead of relying on numbered labels
such as **Statistics 1**. Table Source uses the dataset title or filename;
Statistics uses the measurements and grouping, adding **Image averages** or
**Sample averages** for those observation levels; Plot Results uses a meaningful
figure title or its plot settings. For example, a summary might read
**3 measurements by Well**, while a plot might read **area distribution**.
These examples depend on the actual selected columns.

Operation type and current settings remain available alongside the name or
in its tooltip. If names match, VIPP adds source context and, when necessary,
a short stable identifier. Use **Show node**, then the inspector's **Name**
field or the node's **Rename…** action to give it your own description. See
[Name a node](edit-graph.md#name-a-node) for automatic naming, reset and
save behavior. A custom plot-node name is independent of the exported
figure's title.

For multiple sources, first [merge matching
measurements](../workflows/object-measurements-tables.md) or [collect batch
measurements](collect-measurement-results.md). Merging adds fields for matching
objects; collection brings observations from several images into one dataset.
Browsing another workflow does not copy its data, combine tables or create
connections between workflows.

## Review the data

In **Data**, search rows and choose which columns to show. These controls only
change what you see: they do not exclude observations from a summary or plot.
Use **Select all** or **Select none** above **Visible columns** to show or hide
all columns at once, then select the individual columns you want.
Export uses the complete table, not just the visible search results or columns.
For a saved column selection used downstream, use **Select Table Columns** in
the workflow.

## Build a summary

Select a **Statistics node** in the top bar, or use **+** beside it to add an
ordinary Statistics node connected to the selected data
source. Then open **Summary**. Choose
measurements, groups, observation level and statistics on the left; review
the updated table and **Result overview** on the right. The overview separates
objects used/excluded from image or sample averages summarized, for each
measurement across all groups. Enable **Show all fields** to see per-group
inclusion counts and calculation settings;
table export includes them whether or not they are currently visible.

Object values, image averages and sample averages have different meanings.
See [Summarize measurements](summarize-measurements.md) for identity fields,
weighting and missing-value choices. Counts and units stay with the result.

## Choose what the plot uses

Choose **Plot** in the top bar, then open **Plots**. The **+** beside **Plot**
creates a normal Plot Results node connected to the selected Statistics
output, or to **Data source** when Statistics is **None — use input data**.
Opening a tab never creates a node or selects a different branch.

To deliberately reconnect an existing plot, expand **Change plot input…** in
the plot controls and choose its new input:

| Source | What the connected rows represent |
| --- | --- |
| **Original measurements** | Rows from the workspace's source table. For an object table, these are individual objects; **Mean per image** can explicitly reduce them to image means. |
| **Summary table** | Rows already calculated by the selected Statistics node, often one row per group. Choose a summary column such as a mean to plot it. |

The blue-bordered input card stays visible above the figure. Its header
identifies the input; click the header or the outlined cyan chevron at its
right edge to expand **Input details**. The body starts collapsed and explains
the source, what each plotted value represents and the counts. **Original
measurements** means the workspace's connected source, not earlier raw rows.
When that source is already a summary, the input selector calls it **Input
summary table**.

Choosing a summary in **Change plot input** connects the plot to that
Statistics node and uses each summary row directly, rather than averaging it
again by image. Review
the measurement and group fields after changing sources: a column available
in the original table might not exist in the summary. VIPP does not guess an
equivalent measurement.

For a new plot of a summary table, first choose **Measurement** (and both axes
for **Scatter**). VIPP waits for these choices before calculating the plot;
the setup prompt is not a failed analysis. It never picks a summary statistic
on your behalf. Once configured, changes update the plot automatically.

!!! warning "A summary does not contain the original observations"
    Two treatment means are two summary values, not all the original objects
    or independent samples. Selecting a mean column does not automatically
    add its SD as error bars or recover the underlying distribution.

The plotting controls are the same as [Plot Results](plot-measurement-results.md),
including **Appearance** and automatic/custom numeric-axis intervals.

Messages beside the plot distinguish guidance from problems:

- **Grey analysis notes** explain interpretation: summary rows are not
  original objects, and SD is not automatically an error bar.
- **Orange cautions** flag issues to review, such as excluded rows, values
  excluded by log scales, display sampling, many numeric categories or no
  eligible values.
- **Red errors** mean the plot could not be calculated. They remain visible
  until the problem is addressed.

Analysis notes appear by default. Dismiss them after reading, and use the
compact **Analysis notes** indicator to reopen them. Notes return when input
data, analysis choices (including grouping, averaging or log scales), or
warning text changes. Switching tabs,
resizing and appearance-only edits do not reopen them. Dismissal applies only
to that plot in this workspace window; calculations, exports, inspector and
separate plot-window warnings are unchanged. Errors, setup prompts and
out-of-date status remain visible and cannot be dismissed this way.

The figure fits the available preview area, including its axes. Maximize or
resize the window, or drag the divider to give it more room; the settings scroll
independently. Resizing the preview does not change the measurements, saved
plot recipe or export dimensions. Set the exported figure's width and height
in **Export figure…**.

## Keep, export and close

- The **+** actions add normal Statistics or Plot Results nodes. Opening the
  workspace or switching its tabs does not create nodes.
- Changes edit the selected node immediately and are shared with its
  inspector and existing plot window. **Show node** locates it in the graph.
  It hides (rather than closes) the workspace and centers the node; reopening
  **Results Workspace** from the inspector retains your view and selections.
  It targets the exact node shown in the editing heading and is disabled when
  there is no selected node, such as a summary with no connected plot.
  Different summary/plot nodes keep independent settings.
- Save each edited workflow to keep its nodes, connections and settings.
  Closing the workspace does not discard edits.
- Table export saves the complete current table as **CSV/TSV**, including
  summary counts and method fields. Excel export remains available in the
  separate batch collection window.
- Figure export uses **Export figure…** for sized PNG/TIFF/SVG/PDF output.
  A stale or calculating result is not exportable as a current result.

Changing results settings reuses current upstream measurements. If the
measurement table itself is stale, recalculate that source before treating
the summary or plot as current. The activity area remains in place while
updates are prepared, so the controls do not jump.
