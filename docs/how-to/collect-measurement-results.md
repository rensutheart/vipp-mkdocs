# Collect measurements from a batch

Bring saved measurements from many images into one table, then export them to
CSV, TSV or Excel without reprocessing the images. Continuing in a VIPP results
workflow is optional.

!!! info "New in 0.16.0a1"
    Collection combines and exports saved measurements. It does not calculate
    plots or statistical tests; use connected results nodes for descriptive
    summaries and figures.

## Collect and review

1. Finish a [batch run](../workflows/batch-processing.md) that saves a measurement
   table through **Batch Output**. Keep its run records beside the outputs.
2. In **Batch workflow → Run & results**, choose **Collect measurement results…**
   and select the table output to collect. For example, collect the object
   measurements across all images, rather than mixing them with skeleton branches
   or a summary table.
3. Review the item list. VIPP checks that saved files match their recorded
   contents and that their columns, value types and units are compatible.
   Read the reported reasons for any unusable result.
4. Add missing **condition**, **sample** or **replicate** annotations where useful.
   Select several items to apply the same annotation together. Existing
   annotations are retained; collection does not change the measurement values.
5. Review any exclusions explicitly, then choose **Export results…** and select
   CSV, TSV or Excel. You do not need to save a VIPP collection or open another
   workflow first. The review stays open after export.

**A failed or missing result is not an image with zero objects.** A verified
table with no rows remains in the collection's item inventory, but contributes
no invented object row. Changed, missing, unsupported, failed and excluded
results remain distinguishable, so a smaller collected table cannot silently
look like a complete experiment.

!!! warning "Older runs may need to be repeated"
    Older CSV/TSV outputs may lack the recorded value types needed for safe
    collection. VIPP will explain this rather than guessing whether, for
    example, `001` is a sample name or the number 1. To collect those results,
    deliberately rerun the analysis with a VIPP build that records the required
    information. Opening the collection review never reruns images for you.

## Choose an export

- **CSV or TSV:** one measurement table for other analysis software. The
  optional **image summary** companion is selected by default; keep it to
  preserve each image's outcome, annotations and inclusion decision, including
  images with no measurement rows. It uses the same filename with
  `-image-summary` before the extension, for example
  `nuclei-image-summary.csv` beside `nuclei.csv`.
- **Excel (`.xlsx`):** one workbook with **Measurements**, **Image summary** and
  **About this collection** sheets. The image summary is always present; About
  this collection explains the measurement units and records run information.

The image summary is an inventory, not a new statistical analysis. An empty
valid result and an excluded or failed image remain different outcomes. If
you omit the CSV/TSV companion, the measurement rows alone cannot show all
images that contributed no rows.

CSV/TSV does not store VIPP's column types or units, and spreadsheet apps may
reinterpret identifiers such as `001`. Check import settings before analysing
those files. The Excel workbook keeps text as text and records units, but
spreadsheet number precision still applies. Save the native VIPP collection
as well when exact values and their original types must be retained.

## Optionally continue in VIPP

Choose **Save VIPP collection…** separately to keep a reusable
**`.vipp-results.json`** dataset, such as
`nuclei-measurements.vipp-results.json`. It preserves VIPP's typed measurements,
units and complete collection records for reopening; CSV/TSV and Excel are
exports for use elsewhere, not replacements for this native dataset.

**Open VIPP collection in a results workflow** is unchecked by default. Select it
before saving only if you want a new VIPP results workflow. Saving without it
does not open another workflow, and the collection review stays open.

**Table Source** provides the saved measurement rows to the ordinary table
tools:

- **Select Table Columns** keeps the fields you need, including identity keys.
- **Add Metadata Columns** adds further constant annotations.
- **Summarize Measurements** calculates its existing grouped summaries.

In the Table Source inspector, **Review collection…** shows the saved item
inventory read-only, including empty results and exclusions. **Choose
measurement dataset…** lets you select a saved dataset to use in that node.
Its ordinary **Export table…** action exports just the node's table as CSV or
TSV. For the Excel workbook or the image-summary companion, use **Export
results…** in the batch collection review instead.

Collection appends observations from different images. **Merge Tables** has a
different job: joining columns that describe matching observations. Neither
equal row counts nor repeated local object numbers prove a match. Keep the
source/image identifiers so object 1 in one image is not confused with object
1 in another.

Choose sample and replicate names to reflect the experiment—for example, an
animal, culture or independent experiment. Several images from one sample do
not automatically become independent replicates. Adding these labels does not
itself establish which statistical comparisons are appropriate.

## Save, move or share

The `.vipp-results.json` file contains measurements, units, reviewed
annotations and an inventory of included and omitted results with their run
records. **It contains no input images, masks, mesh geometry or previews.**
Review source names and annotations before sharing; they can contain private
information.

Save the results workflow separately. Its JSON references the dataset's path
and recorded hash; it does not embed the table. Keep the dataset with the
workflow when moving or sharing them. VIPP reports a missing or changed dataset
instead of silently accepting different measurements. Opening a collection
does not require recalculating the source images.

A [reproducibility package](export-reproducibility-package.md) still excludes
result files. Share this measurement dataset separately if you want the
recipient to inspect it. For column identities and units, see
[Measurement tables and units](../reference/measurement-tables.md).

**Python export is not yet available for Table Source workflows.** Use VIPP
to reopen and calculate the saved results workflow. A reproducibility package
explains this limitation and omits the Python runner for these workflows;
ordinary image-workflow exports are unchanged.
