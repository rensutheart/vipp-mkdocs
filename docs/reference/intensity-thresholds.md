# Intensity and threshold controls

Use this reference when cutoff choice, histogram scope, or numeric precision
could change your analysis. For a first segmentation, start with the
[label-cleanup tutorial](../workflows/segmentation-label-cleanup.md).

## Binary Threshold: cutoff or intensity range

Binary Threshold offers **Foreground: Above / Below / In range / Outside range**.
Older workflows without a saved **Foreground** choice use **Above** and produce
the same mask as before.

Choose **Foreground**, then adjust the slider or drag a histogram guide:

| Choice | Becomes foreground | Useful for |
| --- | --- | --- |
| **Above** (default) | Values strictly greater than the threshold | Bright structures on a darker background |
| **Below** | Values strictly less than the threshold | Dark structures on a brighter background |
| **In range** | `low ≤ value ≤ high` | Keep an intensity band, including its limits |
| **Outside range** | `value < low` or `value > high` | Exclude an intensity band and its limits |

**Above/Below** show one **Threshold** slider; values exactly equal to it stay
background. **In range/Outside range** instead show **Low threshold** and
**High threshold**, with orange and blue histogram guides. The controls keep
low ≤ high. Equal limits select exactly that intensity with In range, or every
other non-NaN value with Outside range.

NaN pixels stay background in all four modes, so Outside range is not simply
an inversion of In range. Loaded or scripted ranges with non-finite or reversed
limits are rejected, not silently corrected.

The cutoff applies throughout the supplied image or volume; it does not fit a
separate cutoff per slice. Declared RGB/RGBA input uses the existing explicit
luminance conversion. The choice is saved and used by batch and Python exports.

With a finite cutoff, positive infinity is foreground only in Above, and
negative infinity only in Below. With finite range limits, both infinities are
outside the range. Automatic threshold nodes use the different
non-finite policy described below.

These are elementwise comparisons, preserving 2D, 3D, and leading time/channel
axes and returning a Boolean mask without changing the input. The CPU path
uses NumPy's [inclusive](https://numpy.org/doc/stable/reference/generated/numpy.greater_equal.html)
and [strict](https://numpy.org/doc/stable/reference/generated/numpy.less.html)
comparison rules; the supported scalar float32 CuPy path follows the same rules.

## Automatic Threshold Histograms

Otsu, Triangle, Yen, Isodata, and Minimum calculate their cutoff from every
finite pixel in the selected scope. VIPP does not silently sample a large image
or substitute a lower-resolution preview.

`Stack histogram` fits one cutoff to
the complete stack; `Slice histogram` fits each processed YX plane separately.
For encoded RGB/RGBA input, select its declared channel axis to reduce colour to
luminance first. `-1` is scalar mode for data without encoded-colour semantics;
VIPP rejects that setting when the input metadata explicitly declares an
RGB/RGBA axis instead of producing a misleading component-wise mask.

The histogram resolution follows the input dtype:

| Input | Threshold histogram |
| --- | --- |
| Boolean | Already a binary segmentation, so VIPP preserves it unchanged instead of fitting another threshold. The inspector uses 0.5 only as a conventional dividing marker. |
| Integer | One bin per native integer level between the finite minimum and maximum. `Float histogram bins` is ignored. |
| Floating point | The explicit `Float histogram bins` value, from 2 to 65,536; default 256. |

An integer range wider than 65,536 levels is rejected rather than silently
rebinned. Add `Convert Dtype` or `Rescale Intensity` when such data should be
compressed intentionally. `Float histogram bins` is saved in workflow JSON
because changing it can change a floating-point threshold.

Li Threshold instead
uses all finite raw values directly and therefore has no bin control. For
integer Li inputs, VIPP preserves exact native offsets but rejects a relative
intensity span wider than 2^53, which cannot be represented faithfully by Li's
float64 iteration; convert or rescale deliberately in that exceptional case.

### Minimum Threshold

`Minimum Threshold` is intended for roughly bimodal data, such as a background
peak and a foreground peak. “Minimum” means the lowest valley between those two
histogram peaks, not the minimum image intensity. The node repeatedly applies a
three-bin moving average to the exact histogram—never to the image pixels—and
marks values strictly above the valley as foreground.

The
`Histogram smoothing pass limit` is only a convergence safety limit. Smoothing
stops once fewer than three peaks remain, and calculation succeeds only when
exactly two remain. Raising an already sufficient limit therefore does not
change the result. If two peaks cannot be found within the declared limit, the
node reports the failure; it does not silently substitute another threshold.

### ImageJ Default compatibility

`ImageJ Default Threshold (8-bit)` is a separate, experimental source-aligned
node targeting ImageJ 1.54p for scalar uint8, uint16, and float32 inputs. It
converts each trailing YX plane independently with source-derived 8-bit
ScaleConversions behavior, then applies ImageJ's modified IsoData (`Default`)
AutoThresholder. The method is fixed, so newly authored nodes do not show a
method dropdown.

Existing workflows saved with the former ImageJ `Triangle`
choice retain that source-derived calculation as fixed legacy compatibility;
it is not interchangeable with VIPP's generic `Triangle Threshold`, whose
conversion and histogram contract differs. Independent ImageJ-generated golden
parity is pending.

Bool handling, other floating dtypes, and RGB/RGBA luma
reduction are VIPP extensions and are not claimed as ImageJ-exact. NaNs become
zero during plane conversion; infinite float values are rejected explicitly
instead of preserving ImageJ's collapsed all-zero plane. The node does not
change the scientific contract of VIPP's generic Triangle or Isodata nodes.

### Non-finite data and histogram interaction

For the generic global threshold nodes, NaN, positive infinity, and negative
infinity are excluded from cutoff fitting and become background in the
resulting mask. Large calculations use bounded chunks and background workers
to control memory and keep the interface responsive; chunking does not change
which pixels contribute. An empty input or an input with no finite pixels
reports an error instead of inventing a cutoff.

For manual guides, dragging a Binary Threshold, either Hysteresis guide, either
Rescale cutoff, or an explicit Clamp Intensity cutoff reuses the already
calculated input
distribution. Dragging a percentile-derived Rescale guide switches `Input
cutoffs` to `Explicit values`, preserving the untouched guide and making the
dragged intensity an exact saved cutoff. Only the guide moves immediately and
the node output is queued for recalculation; VIPP does not rescan unchanged
input pixels.

The output histogram still refreshes after that output changes,
as it should. Parameters that change a computed guide, such as floating-point
histogram bins, refresh that guide independently while retaining the displayed
counts. A replacement connected input array, a different slice, or a different
histogram scope still calculates a new distribution because the inspected
population has genuinely changed.

All numeric nodes in **Intensity & Contrast** show both the connected input
histogram and the selected output histogram. The input view has the same exact
slice/stack and log-display controls for Linear Scale + Offset, Gamma
Correction, Rescale Intensity, Normalize, and Clamp Intensity. Rescale Intensity
and Clamp Intensity additionally show their cutoff guides; the other three
input histograms are read-only
context for judging the transformation.

## Rescale Intensity Cutoffs

Low and high input controls cannot cross. Rescale allows equal input cutoffs;
Normalize's percentile limits must remain distinct. Rescale also keeps
**Output min ≤ Output max**; use **Invert intensity** to reverse the mapping.

Normally, the low input cutoff maps to **Output min** and the high cutoff to
**Output max**. With **Invert intensity** checked, these destinations reverse:
dark values become bright and bright values become dark, within the same output
bounds. The checkbox defaults to off and is saved for batch runs and Python
exports. Editing either bound never moves the other one.

Equal output bounds produce a constant numeric image. Equal input cutoffs fill
Output min normally, or Output max when inverted. Boolean masks keep their
True/False values normally; inversion swaps True and False, without rescaling
them to the numeric output bounds. Other inputs retain their dtype; NaNs remain
NaN for distinct input cutoffs, and infinities map to the corresponding endpoints.

Older workflows with reversed output bounds need a one-time correction: enter
the smaller value as Output min, the larger as Output max, then check
Invert intensity if the reversed mapping was intentional. VIPP leaves the
saved values untouched and reports this guidance instead of guessing.

`Rescale Intensity` makes the cutoff source explicit:

| `Input cutoffs` | Behavior |
| --- | --- |
| `Percentiles (exact)` | Default for new nodes. `Low percentile` and `High percentile` are calculated from every finite input value; the value fields do not override them. |
| `Explicit values` | `Low value` and `High value` are used directly; the percentile fields do not override them. |

There is no size-dependent percentile sample. Large percentile calculations are
backgrounded but still use all finite values, with cutoff and voxel-rescaling
phases shown in the pipeline progress area. Interior percentiles such as 99.9
still require an exact order statistic over the volume; 0 and 100 use the exact
finite minimum and maximum directly. Rescaling itself uses bounded work chunks
without changing the requested arithmetic. The selected mode is saved in
workflow JSON. Dragging either histogram cutoff is a manual intensity edit, so
a node in percentile mode changes to `Explicit values` before the dragged
cutoff is saved.

### Clamp Intensity

`Clamp Intensity` uses the same explicit-mode principle. New nodes default to
**Full data range**, which leaves the input range unchanged until explicit bounds are
chosen; **Explicit values** applies `Minimum` and `Maximum`. Values below or above those
bounds are set to the nearest bound; values inside the interval are unchanged.
Clamping does not set a positive lower tail to zero and is not background
removal.

### Integer precision and limits

Integer data retains native-level meaning in both nodes. Integer percentiles
are calculated from exact order statistics, including the fractional
interpolation between neighbouring ranked levels, and Rescale performs its
arithmetic after subtracting a native integer origin. This preserves adjacent
int64/uint64 values even near their dtype limits. Integer Clamp Intensity uses
whole-number bounds and clamps without a float conversion; use `Convert Dtype`
first when a fractional clipping bound is scientifically intended.

When the connected image has a non-boolean integer dtype, the Clamp Intensity
minimum/maximum, Rescale output minimum/maximum, and Mask Image outside-value
controls switch to whole-number steps and integer entry. Floating-point and
boolean inputs retain fractional entry because those operation contracts permit
it.

If an older workflow already contains a fractional or out-of-range value
that is invalid for its current integer input, VIPP preserves and labels that
saved value instead of silently changing the workflow; its correction control
accepts only valid whole numbers and becomes the normal integer control after
the value is corrected. Exceptionally wide integer dtypes use a zero-decimal
wide-range entry so Qt's 32-bit spinner cannot overflow.

Rescaling still needs floating-point ratio arithmetic. An active integer input
or output interval wider than 2^53 levels is therefore rejected because
float64 cannot distinguish every level in that interval. Also, the GUI's
floating-point spin boxes cannot identify adjacent absolute values above 2^53.
For those exceptional wide-integer datasets, use exact integer literals in an
exported/workflow definition, use percentile cutoffs, or deliberately convert
the dtype. int64/uint64 Rescale outputs default safely to `0..1` instead of an
imprecise float representation of the full dtype maximum.

The input-histogram slice/stack selector changes the distribution drawn for
inspection. A percentile-mode Rescale marker and a data-range Clamp marker still
describe the complete connected input, because that is the data those node
modes actually process.
