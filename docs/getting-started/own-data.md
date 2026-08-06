# Use your own images

An `Image Source` can read a napari layer, a local file or store, or a bundled
sample. Changing the source is easy; establishing that the workflow remains
valid is the important part.

## Choose a source route

| Route | Best for | Important limitation |
| --- | --- | --- |
| `napari layer` | Images already opened, cropped, or registered in napari | The workflow depends on a layer being present and correctly selected; unsupported live/lazy transforms can be rejected. |
| `file path` | A repeatable local file input | Moving, renaming, or replacing the file changes/breaks the source identity. |
| `sample` | Tutorials, regression checks, and demonstrations | Synthetic data does not establish performance on your assay. |
| Local OME-Zarr store | Chunked multidimensional data | Many operations are eager and can still materialize large arrays. |

Select `Image Source`, set **Source**, and then use the control specific to that
route. The napari layer chooser is only shown for `napari layer`. The Image
Source card's live subtitle shows the current layer, sample, file, or collection
representative; hover the card for the complete binding when the subtitle is
elided.

## Understand the source revision

During one interactive revision, VIPP does not repeatedly read an uncontrolled
moving target. A local file or directory store is identified before and after
inspection/materialization, detached into an owned read-only snapshot, and
pinned until **Refresh**. A revision changed during calculation is rejected.

NumPy-backed napari layers are also copied with a revision token. Data,
metadata, RGB, axis, scale, translation, unit, rotation, shear, and affine
events invalidate stale work. VIPP rejects live data or transforms that cannot
be frozen without changing pixels.

**Refresh** is the explicit instruction to accept the current source revision.
Record an external checksum or repository identifier for long-term provenance;
the workflow stores a source parameter/path, not the image bytes.

## Check metadata before processing

Confirm at minimum:

- array shape and semantic axes (`T`, `C`, `Z`, `Y`, `X`);
- channel order and names;
- pixel size, z-step, and unit;
- whether the data is intensity, RGB, a binary mask, or labels;
- whether the reader selected the intended image/series.

For a multi-input node, also confirm that corresponding axes describe the same
physical grid. Equal shape does not prove equal scale, units, origin, or axis
meaning. VIPP rejects detected mismatches rather than resampling silently.

Use `Reorder Axes` only when you understand the actual stored order. Use
`Set Pixel Size / Units` to repair missing or known-wrong calibration, and
record where the corrected values came from.

For an ordinary TIFF batch that reports generic `QYX`, use the source's
**Image stack** chooser instead of trying to rename Q with `Reorder Axes`.
VIPP can visibly suggest **Pages are depth slices (Z stack)** only when the
workflow demonstrates a `ZYX` requirement. Keep it only after confirming the
page meaning, and verify Z spacing separately.

For Nikon ND2, 0.13 follows the reader's ordered dimension mapping when its
labels and sizes exactly match the returned array. This fixes affected T/Z/C
sliders and keeps napari and VIPP slice selection aligned. Still verify the
displayed axis order, array shape, channel choice, and movement of every T, Z,
and C control on a representative file. An inconsistent reader mapping is not
trusted; VIPP falls back conservatively rather than reordering pixels from a
malformed declaration.

## Transfer a workflow deliberately

Do not judge transfer only from the final object count. On representative
images from the new acquisition family:

1. Inspect raw channel quality and background.
2. Inspect every threshold or segmentation boundary.
3. Check objects at image edges and across z.
4. Compare against independent reference annotations or agreed QC examples.
5. Retune only on a defined tuning subset.
6. Evaluate the frozen workflow on held-out images.

Changes in objective, exposure, stain, detector, bit depth, sampling, tissue,
or preprocessing can invalidate parameters that worked previously.

When moving from 0.12.0a3 to 0.13.0a1, keep the original schema-3 file and open
a duplicate. It loads with explicit CPU intent; inspect graph structure,
sources, axes, parameters, dynamic ports, and decisive outputs before saving
the duplicate as schema 4. Rebuild schema-1/2 workflows deliberately; changing
only the JSON version is unsafe. See
[versions and compatibility](../reference/versioning.md#move-from-0120a3-to-0130a1).

## Protect sensitive data

Workflow JSON may contain local paths, source names, graph notes, or metadata
values. Review it before sharing publicly. Do not use patient identifiers,
restricted paths, or unpublished biological conclusions in screenshots,
examples, notes, or metadata columns.

Continue to [segmentation](../workflows/segmentation-label-cleanup.md),
[measurements](../workflows/object-measurements-tables.md), or the
[scientific-practice checklist](../scientific-practice/index.md).
