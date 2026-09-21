# Measurement tables and units

For graph construction and export, follow the
[object-measurement tutorial](../workflows/object-measurements-tables.md).
Use this reference to check identities, units, and unavailable measurements.

## Table identity

Measurement nodes produce tables, not images. Each table carries ordered
columns, a table kind, row/column counts, a source name where available, and
per-column units where the calculation defines them.

[Results Workspace](../how-to/results-workspace.md) combines table
viewing, Statistics controls and Plot Results without a new table type. Search
and visible columns affect only the view; exports retain the complete current
table. Plot inputs explicitly distinguish the source measurements from a
selected summary table.

Keep the keys that distinguish observations:

- leading-axis indices, such as `t_index`, `c_index`, and `z_index`;
- object/graph IDs, such as `label_id`, `mesh_id`, `component_id`, `branch_id`, `node_id`,
  and `edge_id`;
- experimental fields added with **Add Metadata Columns**, such as treatment,
  replicate, and batch.

Equal row counts are not proof that two tables describe the same observations.

## Decimal places in table views

!!! info "New in 0.16.0a1"
    Results Workspace tables and separate result-table windows provide
    **Increase Decimal** and **Decrease Decimal** controls for easier reading.

Floating-point values initially show **3 decimal places**. Use the controls to
show more or fewer places, from **0 to 15**, throughout the current table view.
Hover over a cell to inspect its full original value. Integers, Boolean values,
text, missing values and non-finite values such as `NaN` are not reformatted.

This is a display preference, not a measurement-accuracy setting. It does not
round the stored values or change calculations, sorting, searching or exports:
those still use the original full-precision data. Values that look identical
after display rounding can therefore sort differently.

The choice survives table refreshes in the current view. It is not saved as a
workflow setting or shared with other table views.

## Units through table composition

| Node | Unit handling |
| --- | --- |
| Merge Tables | Preserves units; duplicate names and their units receive matching suffixes. |
| Select Table Columns | Preserves the selected columns' units. |
| Add Metadata Columns | Keeps existing units; new metadata columns are unitless. |
| Summarize Measurements | Propagates numeric units except for count statistics. |

In 0.16.0a1, **Statistics** expands Summarize
Measurements with explicit object/image/sample levels and counts. It retains
each measurement's units in separate result columns. Old recipes retain their
calculations until explicitly upgraded. See
[Summarize measurements](../how-to/summarize-measurements.md) and the
[method/count reference](statistics.md).

## Collected batch tables

!!! info "New in 0.16.0a1"
    [Batch measurement collection](../how-to/collect-measurement-results.md)
    exports CSV/TSV or an Excel workbook directly. Saving a typed
    `.vipp-results.json` dataset and opening it through **Table Source** are
    separate, optional steps. Ordinary workflow JSON keeps only the external
    dataset reference and its hash, not the collected rows.

The collector checks recorded output contents, column types and units before
appending rows. It does not silently mix incompatible tables or convert pixels
to physical units. Existing annotation and local object-ID columns are
preserved alongside their image/source identity.

The item inventory distinguishes a valid zero-row table from a missing,
changed, unsupported or failed output, and retains deliberate exclusions.
Zero-row images add no artificial object. Historical CSV/TSV files without
typed output records are not imported by guessing; a new, explicitly requested
batch run is needed to produce collectable records.

Excel includes **Measurements**, **Image summary** and **About this
collection** sheets: rows, per-image outcomes/annotations, and units/run
information respectively. CSV/TSV offers an optional `-image-summary`
companion, selected by default, to keep empty and excluded images visible.
These exports do not rerun measurements. Keep the native VIPP dataset for a
typed round trip; **Table Source → Export table…** remains CSV/TSV-only.

## Object morphology

In 0.16.0a1, connect a measurement table directly to
**Plot Results** to explore individual points, histograms, cumulative
distributions or scatter plots. A single labelled image is sufficient; batch
collection is optional. See [Plot measurement results](../how-to/plot-measurement-results.md)
for image means, exclusions and figure export.

**Measure Objects** returns one row per label object. Basic fields include ID,
pixel/voxel area or volume, centroid, bounding box, equivalent diameter, extent,
and Euler number. Optional groups add shape, axis/inertia, derived ratios,
2D boundary descriptors, and 2D moments.

With calibration, supported physical columns include:

- area/volume, centroid, and bounding-box coordinates;
- equivalent diameter, bounding/fill size, and maximum Feret diameter;
- major/minor axis lengths, bounding-box side lengths, and inertia eigenvalues.

Physical perimeter, Crofton perimeter, and perimeter-to-area ratio are available
for isotropic 2D pixels. For anisotropic 2D pixels these physical perimeter
columns remain `NaN`; VIPP does not apply a misleading single scale factor.

**Measure Objects + Intensity** takes matching **Labels** and **Intensity image**
inputs and adds per-object mean, minimum, maximum, sum, and standard deviation.

## 3D mesh morphology

With true 3D labels and correct Z/Y/X spacing, **Measure 3D Mesh Morphology**
extracts a marching-cubes surface for each object.

| Field group | Outputs |
| --- | --- |
| Size | `voxel_count`, `voxel_volume_physical`, `mesh_volume_physical`, `mesh_surface_area_physical` |
| Shape | `surface_area_to_volume`, equivalent-sphere radius/diameter, `sphericity`, physical extents and extent ratios |
| Optional convex hull | Hull volume/area, `solidity_3d`, `surface_area_to_convex_hull_area` |
| Diagnostics | `mesh_status`, `mesh_error` |

Tiny or invalid objects remain as rows with `NaN` mesh metrics and an
explanatory status. Check those fields before summarizing results.

Segmentation, voxel spacing, and surface approximation all affect these
measurements. Very small or flat objects may not support stable mesh or hull
metrics. Mesh viewing/export belongs to the separate
[3D Meshes nodes](../workflows/mask-to-mesh.md); specialist repair is not supplied.

<span id="existing-mesh-objects-nightly"></span>

### Existing mesh objects

The mesh input measures current geometry directly, with one row per explicit
object. It never remeshes, rejoins disconnected shells, or infers voxel counts.

| Field | Meaning |
| --- | --- |
| `mesh_id` | Stable mesh object identity, not a row number. Label extraction retains source label IDs. |
| `vertex_count`, `triangle_count` | Counts in that mesh object. |
| `watertight` | Edge/orientation checks passed; not a general self-intersection or print-validity certificate. |
| `mesh_status`, `mesh_error` | Explain empty or invalid geometry and unavailable metrics. |

Physical metrics use compatible units converted to the mesh X-axis unit;
uncalibrated data remains in voxel-coordinate units. Open, degenerate,
non-manifold or inconsistently wound surfaces keep area/extents where defined,
but volume-derived fields are `NaN`. Smoothing and simplification can change
measurements, even when the object ID stays the same.

Filtering retains IDs; combining remaps collisions, and splitting assigns IDs
to additional parts. Keep source/parent IDs from mesh metadata when tracing
those changes. Do not join pre- and post-operation tables by row position.

## Skeleton and association tables

- [Skeleton reference](skeleton-nodes.md): component, branch, graph-node/edge,
  and whole-network outputs.
- [Association reference](association-metrics.md): overlap, nearest-centroid,
  event-region, and object-colocalization outputs.
- [Validation status](validation-status.md): evidence and scientific limits.

Expensive measurement nodes are manual/cached by default. Recalculate stale
results before export; changing table sorting does not recalculate the data.
