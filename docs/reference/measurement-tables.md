# Measurement tables and units

For graph construction and export, follow the
[object-measurement tutorial](../workflows/object-measurements-tables.md).
Use this reference to check identities, units, and unavailable measurements.

## Table identity

Measurement nodes produce tables, not images. Each table carries ordered
columns, a table kind, row/column counts, a source name where available, and
per-column units where the calculation defines them.

Keep the keys that distinguish observations:

- leading-axis indices, such as `t_index`, `c_index`, and `z_index`;
- object/graph IDs, such as `label_id`, `component_id`, `branch_id`, `node_id`,
  and `edge_id`;
- experimental fields added with **Add Metadata Columns**, such as treatment,
  replicate, and batch.

Equal row counts are not proof that two tables describe the same observations.

## Units through table composition

| Node | Unit handling |
| --- | --- |
| Merge Tables | Preserves units; duplicate names and their units receive matching suffixes. |
| Select Table Columns | Preserves the selected columns' units. |
| Add Metadata Columns | Keeps existing units; new metadata columns are unitless. |
| Summarize Measurements | Propagates numeric units except for count statistics. |

## Object morphology

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

Use **Measure 3D Mesh Morphology** only with true 3D labels and correct Z/Y/X
spacing. It extracts a marching-cubes surface for each object.

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
metrics. Mesh export, preview, and specialist repair are not supplied by this
measurement node.

## Skeleton and association tables

- [Skeleton reference](skeleton-nodes.md): component, branch, graph-node/edge,
  and whole-network outputs.
- [Association reference](association-metrics.md): overlap, nearest-centroid,
  event-region, and object-colocalization outputs.
- [Validation status](validation-status.md): evidence and scientific limits.

Expensive measurement nodes are manual/cached by default. Recalculate stale
results before export; changing table sorting does not recalculate the data.
