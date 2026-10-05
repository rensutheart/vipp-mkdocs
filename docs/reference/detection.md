# Template matching and peaks

**Template Match** returns a normalized-correlation score image and a Boolean
valid-support mask. **Find Peaks** returns a table of retained local maxima.
For a worked sequence, see [Detect repeated patterns](../how-to/detect-patterns.md).

!!! info "New in 0.16.0a3"
    This first implementation is CPU-only, fixed-size and fixed-orientation.
    These two single-image nodes add no registration, resampling, segmentation
    or object tracking. For complete time series, use the separate
    [Detect Spots per Frame and Build Tracks](tracking.md) nodes.

## Inputs and score coordinates

Use scalar intensity images with explicit `YX` or `ZYX` axes. Select T and C
before either node: they are not silently squeezed, projected or interpreted
as spatial axes. Search image and template require the same axis order and
sampling; template origin may differ. The template must fit completely inside
the search image.

For source extent `N` and template extent `K`, the score extent is `N - K + 1`
on each spatial axis. Score index `p` represents source center
`p + (K - 1) / 2`. Thus even-sized templates have half-integer centers; no
subpixel fitting is implied. The score image preserves source spacing and shifts
its physical origin by that center offset. No padded border scores are created.

Correlation measures the mean-centered intensity agreement within each complete
template window. Valid values range from `-1` to `1`: a high positive value
means similar local intensity structure, not confidence or probability.
Undefined flat-window correlations are distinguished by **Valid scores**;
connect that mask when finding peaks in a Template Match result.

Connect the two unchanged outputs directly. This version rejects modified,
cropped or recalibrated score/mask pairs rather than reusing stale source
coordinates. A plain external array without the carried template metadata is
an ordinary intensity image, not an asserted template response.

## Find Peaks controls

| Control | Effect |
| --- | --- |
| **Use valid mask** | Restrict candidates to true samples of a Boolean mask on exactly the same grid. Required for Template Match scores. |
| **Minimum value** | Inclusive cutoff: retain candidates with score/intensity at least this value. Default `0.5`. |
| **Minimum separation** | Greedy Euclidean distance suppression, after sorting by descending score. Candidates closer than this distance to a retained peak are removed; equality is allowed. Default `1`. |
| **Separation units** | **Pixels** uses index distance; **Physical (micrometers)** uses calibrated axis spacing. The latter requires compatible physical length units. |
| **Maximum detections** | Maximum retained rows after ordering and suppression. Default `1000`; this is a result cap, not evidence that no more candidates exist. |
| **Border exclusion (score-grid pixels)** | Number of score-image samples excluded from each edge. Default `0`. Template Match already excludes placements that extend outside the source. |

The sliders use fixed practical windows of `-1` to `1`
for **Minimum value**, `0` to `100` for **Minimum separation**, `1` to `10,000`
for **Maximum detections**, and `0` to `100` for **Border exclusion**. Numeric
spinners accept the full valid ranges: enter higher or lower intensity cutoffs,
larger distances, detection caps or border widths directly. Accepted values
outside a slider window remain unchanged when reopening the inspector or
workflow. **Detect Spots per Frame** inherits these windows, with its detection
cap applied per frame; these are tuning windows, not new scientific limits.

Local maxima use the full 3 × 3 neighborhood in 2D or 3 × 3 × 3 neighborhood in
3D. Each connected equal-valued local-maximum plateau contributes its
lexicographically first coordinate. Candidates are ordered by descending score,
then coordinates, before distance suppression. This deterministic choice is not
a fitted biological center. Find Peaks can also process an ordinary intensity/response image; its
`score` column then contains that input value, not normalized correlation.

## Detection table

| Column | Meaning |
| --- | --- |
| `detection_id` | One-based identifier in retained score order; not a segmentation label or tracking identity. |
| `y_index`, `x_index`, and `z_index` in 3D | Coordinates in the source image supplied to Template Match, or the ordinary image supplied to Find Peaks. |
| Corresponding `*_physical` columns | Calibrated coordinates in each source axis's recorded length unit, including the source origin; consult the column units. |
| `score` | Value at the retained maximum. |
| `template_<axis>_start`, `template_<axis>_stop` | Source-index template bounds for matched scores; stop is exclusive. |

An empty table is a valid no-detection result, not a zero-valued point. The
coordinate overlay is an inspection aid; it does not change the scientific
table or create fake label images. Use the existing [table and plotting
tools](../how-to/plot-measurement-results.md) for descriptive review.

Result metadata records the candidate count, the accepted count after distance
suppression, the returned count after the cap, and whether truncation occurred.
Keep this context when comparing counts; a capped table is not the full count.

## Inspect detections on the source

The **Detection review** section opens **Inspect detections on source…** with
the original search image (or direct intensity input), a sortable table and
read-only markers. Selecting a marker or row identifies the same `detection_id`
even after table sorting. **Export CSV/TSV…** saves the table; markers are not
editable points or segmentation labels.

For ZYX data, **Z plane (zero-based)** is an explicit single-plane selector.
Fractional Z centers display on the nearest plane, with exact halves rounded
up; row selection navigates there and retains the exact coordinates. No
projection or subpixel fit is performed. **Refresh view** only reloads an already
calculated result. Stale or changed source/results hide the overlay and disable
identity/export actions until a current calculation is available.

## Save and collect detection results

Batch CSV/TSV outputs retain each image's `DetectionMetadata` in the run
manifest, including its settings, exact candidate and accepted-before-cap
counts, returned count and truncation flag. Keep the manifest with the table:
a detached CSV/TSV is an ordinary table, not the complete detection provenance.

[Collect measurement results…](../how-to/collect-measurement-results.md) and saved
`.vipp-results.json` collections retain this metadata for each source item,
including valid empty results. The combined table intentionally has no single
image's overlay coordinate frame: rows from different images must not be
displayed as though they belonged to one source image.

To reuse **Match scores** and **Valid scores**, save the two outputs separately
as **TIFF**, **OME-TIFF**, or **OME-Zarr 0.4/0.5**, then reopen both through VIPP's
readers and reconnect the matching mask. These routes retain exact `float64`
scores, Boolean validity, the calibrated center grid and the paired template
metadata. **ImageJ TIFF** refuses tagged outputs instead of casting them.
For a ZYX score grid with only one Z plane, both TIFF routes refuse the write
because their reader would squeeze Z; use **OME-Zarr** to preserve its rank.
Do not use plain NPY or raster exports for provenance-preserving score reuse;
an array without its template metadata is only an ordinary intensity image.

## Limits and evidence

Inputs are not modified. Ambiguous axes, incompatible calibration, non-finite
values (even outside a supplied mask), complex data, extended-precision floats,
integers outside the exactly representable `±2^53` range and a constant template
are rejected. Computation uses `float64` with numerical
centering/scaling intrinsic to normalized correlation, recorded in history;
there is no dtype-range normalization or intensity clipping. A constant search
image is accepted but has no valid correlation windows. Flat search windows
cannot provide defined correlation. No rotation search, scale search or
automatic repair is performed.

Numerically difficult windows use direct mean-centered correlation instead of
the fast calculation, preserving the same full population and score definition.
Extreme intensity ranges can therefore be slower. Remaining unstable results
fail visibly; only floating-point roundoff at the `-1`/`1` score endpoints is
clipped. Cancellation is checked between native calculations, not inside an FFT;
cancelled work does not publish a partial result.

Matching evaluates the complete in-memory image on the CPU. Memory admission
can reject an oversized request; crop the scientific search region explicitly
when justified. VIPP does not silently downsample or search only a subset.

The two bundled examples plant patterns with seeded noise independently of the
matching algorithm, record known centers, and include nearby, border and absent
cases. They are regression checks, not evidence of accuracy on an assay.
Inspect false positives and false negatives on representative independent data.

Normalized correlation and its full-template-window interpretation are described
in the [scikit-image template matching reference](https://scikit-image.org/docs/stable/api/skimage.feature.html#skimage.feature.match_template).
VIPP's calibrated center coordinates, validity mask and deterministic separation
rules are additional contracts described above.
