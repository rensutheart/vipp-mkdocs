# Summarize measurements

Use **Statistics** to summarize object measurements at the object, image or
declared-sample level, while keeping counts, exclusions and units visible.

!!! info "New in 0.16.0a1"
    **Statistics** expands **Summarize Measurements**. New nodes use the
    descriptive recipe below. Older saved summaries retain their previous
    calculations until you explicitly upgrade them. No inferential tests,
    p-values, significance labels or confidence intervals are included.

## Start with a measurement table

1. Connect a calculated measurement table to **Statistics**, under
   **Measurements → Tables**. A single image is enough; a batch collection is
   optional.
2. Review **Auto-select measurements**, or switch it off and
   choose the **Measurements** you need. Under **Group results by**, leave
   **None** for one overall summary or choose a field such as treatment.
3. Set **Each observation represents** using the table below. For image/sample
   averages, select the relevant **Image identity column** and **Sample
   identity column**. Under **Statistics to report**, choose the reductions.
4. Set **Missing or invalid measurements** to **Exclude and report** or
   **Stop and review**. Never interpret an excluded measurement as zero.
5. Calculate and inspect the result table. Check the counts and status fields
   alongside the values before exporting or plotting.

Choose **Open Results Workspace…** to keep these controls beside the updating
summary table, with **Data** and **Plots** in the same window. It edits this
same Statistics node, not a separate recipe. See
[Explore results in one workspace](results-workspace.md).

The initial selection is count, mean and sample SD over objects. You can also
choose median, lower/upper quartiles, IQR, minimum, maximum and sum. The
[Statistics reference](../reference/statistics.md) defines each method and
explains empty groups and undefined results.

Hover over a field or choice for its explanation. **Auto-select measurements**
tracks eligible numeric measurement columns as the upstream table changes.
It excludes recognized identities/metadata and the chosen grouping and
identity fields. It neither creates measurements nor converts text to numbers.

Use **Select all** to keep the currently eligible measurement names as a fixed
manual selection, or **Select none** to clear it and choose a smaller set.
Both turn off **Auto-select measurements**; neither selects fields marked
**not automatic**. An empty selection cannot be calculated: choose at least
one measurement first. These actions affect the analysis, unlike the
Results Workspace Data tab's visible-column controls. They work identically
in the inspector and Results Workspace.

The controls are divided into **Measurements**, **Grouping**, **Observation
unit** and **Statistics to report**. The short note below the missing-value
choice explains the selected policy; hover for the full details. Sample SD
still needs at least two valid observations at the chosen level.

## Choose groups

**Group results by** calculates a separate summary for each distinct value of
one column. For example, choosing `condition` separates control and treatment.
**None** combines all eligible rows into one summary.

Check **Group by several columns** to reveal the grouping checklist. Select,
for example, `condition` and `timepoint` to summarize each distinct combination:
control at time 0, control at time 1, treatment at time 0, and so on. Merely
opening the checklist keeps the current grouping until you change a selection.
Unchecking **Group by several columns** returns to **None** (no grouping), not
the previous single-column choice.

## Choose what is being summarized

| Level | What enters the final summary | When unequal counts matter |
| --- | --- | --- |
| Objects | Every eligible measurement row | An image with more objects contributes more values. |
| Image averages | One arithmetic mean per contributing image | Each image mean has equal weight, regardless of object count. |
| Sample averages, Equal images | One mean of image means per sample | Images have equal weight within each sample. |
| Sample averages, Equal objects | One pooled object mean per sample | Images with more eligible objects have more weight within that sample. |

The sample setting **Within each sample, weight** selects **Equal images** or
**Equal objects**. Both modes give each contributing sample mean equal weight in the final
summary. For example, one image with measurements `2, 4` and another with
measurement `12` have an equal-image mean of `7.5`, but a pooled-object mean of
`6`. Neither weighting is universally correct: choose the quantity you intend
to describe and keep that choice with the result.

### Choose image and sample identities

- **Image identity column:** all object rows from the same image must have the
  same ID, and different images must have different IDs across the collection.
  For example, every object from field `image_01` shares that image ID.
  Object labels such as `label_id` identify objects, not images.
- **Sample identity column:** use the same ID for images from the same declared
  experimental sample, such as an animal or culture. For example, `image_01`
  and `image_02` can both belong to sample `animal_01`. Choose this mapping from
  your experimental design; VIPP does not infer it from filenames or prove that
  samples are independent.

An identity marked **optional counts** only adds image/sample counts; it does
not change the averaging level or weighting. Switching the observation level
clears identity choices that are no longer used; review the visible fields
after switching.

Image averages require one group per image; sample averages require one group
per sample (and, with equal-image weighting, one group per image). Objects may
belong to different categories within one image. Conflicting image-to-sample
assignments are always errors, not silently split populations.

An image with no eligible measurement contributes no mean and no invented
zero. For a collected batch, review empty, failed and excluded images in the
[collection review](collect-measurement-results.md), not just in the summary.

## Keep and use the result

Save the workflow to keep selected columns, level, weighting and exclusion
policy. The output is an ordinary table: each measurement has separate
statistic and count columns, with its own units. Method fields and a saved
recipe are included so a result is not detached from its averaging rule.

The inspector keeps the short summary separate from the full evidence:

- **Result overview** reports the number of summary rows and a compact
  inclusion breakdown for each measurement, totalled across all groups.
  Compare objects used/excluded with the number of observations summarized:
  at image/sample level, those observations are averages, not individual
  objects. The full table keeps the per-group details.
- The compact Results preview shows group values, **valid n** and selected
  statistics.
- **Open in window** and **Export CSV/TSV…** include the complete table, with
  exclusion reasons, image/sample counts where supplied, and the saved recipe.

Connect the output to
[Plot Results](plot-measurement-results.md) to plot selected result columns;
remember that these rows already represent summaries, not the original
objects. The separate batch collector's Excel export does not make ordinary
Statistics table export an Excel exporter.

## Existing summaries

Opening an older workflow keeps its legacy summary behavior, including a
sample SD of zero for a singleton. Review the legacy notice and choose
**Upgrade to descriptive Statistics** only when you intend to adopt the new
rules. The upgrade can be undone. Version 2 reports
singleton sample SD as undefined, distinguishes exclusion reasons and uses
the selected aggregation level. Save a copy of a consequential workflow before
changing its analysis recipe.

These are descriptive results. Object counts, image counts and declared
sample counts are not interchangeable evidence of biological replication.
