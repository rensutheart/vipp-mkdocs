# Axes And Metadata

VIPP carries an image state alongside node outputs. This state records array
shape, axes, units, scale, source identity, channel metadata, and operation
history where available.

## Common Axes

| Axis | Meaning |
| --- | --- |
| `T` | time |
| `C` | channel |
| `Z` | depth |
| `Y` | image row |
| `X` | image column |

Examples:

| Shape label | Meaning |
| --- | --- |
| `YX` | 2D image |
| `ZYX` | 3D z-stack |
| `CZYX` | multichannel z-stack |
| `TCZYX` | time-lapse multichannel z-stack |

## Why Axes Matter

Many operations depend on whether data is processed per slice or as a volume.

Examples:

- `Gaussian Blur` and local threshold nodes may operate per `YX` plane.
- `Gaussian Blur 3D`, connected components, hole filling, and skeleton analysis
  can use true `ZYX` spatial processing.
- `Split Channels` should be used for a semantic channel axis.
- `Split Axis` should be used for time, Z, or non-channel axes.

VIPP distinguishes axes explicitly supplied by a reader or user from axes
inferred from shape. Operations that need scientific meaning can reject an
inferred-only choice rather than guessing. A trailing dimension of length three
or four is not, by itself, evidence of RGB/RGBA; a generic `C` axis remains a
scientific channel axis unless color semantics are declared explicitly.

Since workflow schema 3, affected operations persist `channel_axis`. The value
`-1` means scalar/no-channel data. It does not ask VIPP to detect RGB from
shape.

Workflow schema 4 adds authored compute intent without changing these axis and
metadata semantics. A schema-3 workflow therefore loads into 0.13 with explicit
CPU execution rather than silently applying the new-session Auto policy.

## TIFF page labels at an image source

Some ordinary TIFF files report a page dimension as generic `Q` because the
file does not say what those pages mean. VIPP does not assume that Q is Z for
every TIFF.

The `Image Source` inspector and each Batch workspace source use the same
**Image stack** interpretation control. On an ordinary Image Source, the
conservative default is **Use the file's labels unchanged**. Choose **Pages are
depth slices (Z stack)** only after confirming that a reported `QYX` source is
really a Z stack. The reviewed choice is saved with the workflow.

In a new Batch workspace source, **Image stack** starts at **Automatic
(recommended)**. If one representative reports exactly `QYX` and the workflow
demonstrates that it requires `ZYX`, VIPP visibly selects **Pages are depth
slices (Z stack)** and retries with the same guarded declaration:

```text
QYX -> ZYX
```

Keep that suggestion only when independent acquisition information confirms
that the pages are depth slices. **Use the file's labels unchanged** rejects the
interpretation, and VIPP does not choose it again for that source. Uncommon
reviewed mappings remain under **Something else (advanced)...**.

An axis declaration assigns new semantic names by position. The source side
must match exactly, including rank and order. It does not transpose pixels or
change shape. `Reorder Axes` is separate: it transposes pixels and moves each
complete axis record, but it cannot rename Q to Z.

Scale, unit, and origin stay attached to their existing positions when an axis
is declared. Relabelling Q as Z therefore does not discover a missing Z step or
prove that the saved calibration is correct. Verify **Output Metadata** and use
`Set Pixel Size / Units` before calibration-dependent analysis.

An Image Source declaration and a Batch source declaration use the same parser,
validation, positional relabelling, metadata record, and execution path. The
Automatic suggestion is applied only by the visible Batch GUI. A resolved
choice is saved as the concrete declaration and is reproduced by headless
execution. An unresolved or historic blank value stores no declaration,
reloads as **Use the file's labels unchanged**, and remains strict in headless
runs.

After `QYX -> ZYX`, **Rescale Axes** exposes Z alongside Y and X. Without a
reviewed declaration, a node that only needs a 2D spatial interpretation can
use inferred trailing Y/X and displays that inference; it does not silently
promote Q to Z.

`Composite → RGB` adds explicit authoring modes around that contract.
**Channel axis mode = Auto** resolves the carried explicit channel axis and
shows it read-only; **Manual** enables the axis selector and permits any valid
deliberate choice, including Z even when the metadata also declares C. **RGB
mapping mode = Auto** similarly shows the resolved per-source-channel mapping
read-only, while **Manual** exposes one colour assignment per detected channel.

Manual assignments are Unassigned, Red, Green, Blue, Magenta, Cyan, and Yellow.
Unassigned contributes nothing; composite colours contribute to multiple RGB
planes, and multiple source channels can add to the same plane. The mapping is
not limited to three or four source channels. Auto mode uses declared encoded
RGB/RGBA order where applicable and otherwise blends every fluorescence channel
by carried pseudo-colour, falling back through Blue, Green, Red, Magenta,
Yellow, and Cyan repeatedly.

## Ordered ND2 dimensions in 0.13

For Nikon ND2, VIPP follows the reader's ordered `sizes` mapping only when the
dimension labels and sizes exactly match the returned array shape. This keeps
T, Z, and C controls attached to the dimensions they actually index and fixes
affected cases where a napari slider moved without changing the expected
slice.

An inconsistent mapping is not used to transpose or relabel pixels. VIPP falls
back to conservative shape-based axis inference. That fallback is not itself a
visible uncertainty flag, so manual verification is required: compare the
displayed axis order and shape with acquisition records, move every T/Z/C
control on a representative file, and inspect the resulting channel and slice
before quantitative processing. Do not add `Reorder Axes` merely to make the
controls look familiar unless the stored order is known independently.

## Physical Scale

Scale-aware measurements use pixel size and units when available.

Use `Set Pixel Size / Units` when input calibration is missing or wrong.

Physical scale affects:

- area and volume;
- centroid and bounding-box coordinates;
- skeleton length;
- branch length;
- 3D mesh surface and volume;
- anisotropic projections and rescaling.

## Physical-grid compatibility

Two arrays with the same shape are not necessarily aligned. Multi-image,
image/mask, and image/PSF operations can also require compatible:

- semantic axis names and types;
- sample counts on corresponding axes;
- physical scale and compatible units;
- physical origin/translation.

VIPP validates these fields where the operation requires alignment. It does not
silently register, resample, reorder, reinterpret, or repair an origin to make
inputs fit. Semantic mask broadcasting follows uniquely corresponding axes,
not merely equal dimension sizes. Deconvolution additionally requires image/PSF
sampling compatibility.

Use an explicit, documented preprocessing step outside or inside the graph when
registration or resampling is scientifically justified, then validate its
effect.

## Metadata Is Not Magic

When files lack reliable metadata, VIPP may expose inferred axes but does not
promote that inference to authoritative meaning. Always check metadata before
reporting quantitative physical units or relying on an automatic spatial,
channel, projection, or PSF choice. Malformed/duplicated axes, stale shapes,
non-finite scale/origin, and non-positive calibration are errors rather than
triggers for replacement guesses.
