# Time-series detection and tracking

!!! info "New in 0.16.0a3"
    The first tracking implementation is position-only, one-to-one and CPU-only.
    Follow [Track objects and spots](../how-to/track-objects.md) for the workflow.

## Observation input

**Detect Spots per Frame** accepts a materialized, scalar image with explicit
`TYX` or `TZYX` axes. Each frame uses the existing [peak detector](detection.md). Template
mode first calculates normalized correlation against one fixed spatial template;
it does not search rotations or scales. Responses are processed one volume at a
time rather than retained as a full response stack. The source image and output
table still need sufficient memory.

The table carries source-index coordinates, `t_index`, frame-local `detection_id`
or `label_id`, the exact spatial grid, source revision and uniform time sampling.
Every frame has population evidence, including empty frames. Object measurement
tables use `centroid_y`, `centroid_x` (and `centroid_z`) index coordinates; the
linker does not reinterpret historical physical centroid columns.

**Build Tracks** rejects missing/duplicate frame-local identities, malformed
coordinates, mismatched populations and truncated observations. A general CSV
or a merged collection does not by itself establish one calibrated time series.
This version has no arbitrary-table column mapping or irregular timestamps.

## Linking rule

At each frame, surviving tracks last seen in the preceding frame are considered
first. Older tracks are considered in increasing gap order, up to **Maximum
missing frames**. Within each tier, eligible links maximize the number of
one-to-one assignments, then minimize total Euclidean distance. New unmatched
observations begin new tracks. There is no velocity model or interpolation.

The inclusive distance gate is **Maximum displacement / frame** multiplied by
elapsed frames. Physical mode uses all spatial spacings, including anisotropic
Z, converted to micrometers. Pixel mode uses source-index distance, even when
the physical sampling is anisotropic. Known time units produce seconds and
distance/second; without time calibration, duration and speed are in frames
and distance/frame. Unknown non-frame time units are rejected.

**Build Tracks** uses fixed practical slider windows
of `1e-6` to `100` for **Maximum displacement / frame** and `0` to `10` for
**Maximum missing frames**. Numeric spinners still accept each setting's full
valid range; enter larger distances or gap counts directly. Accepted values
outside the slider window remain unchanged when reopening the inspector or
workflow. **Detect Spots per Frame** uses the same
[detection tuning windows](detection.md#find-peaks-controls) as **Find Peaks**,
with the detection cap applied per frame.

Stable frame/ID ordering makes reruns deterministic in the tested environment.
Exact ties are not evidence of biological identity, and cross-version bitwise
equivalence of the assignment backend is not claimed. Competing feasible links
flag affected observations for review, not confidence scoring.

## Outputs

**Tracked observations** retains every input row and adds:

| Field | Meaning |
| --- | --- |
| `track_id` | Persistent ID assigned by this calculation; not a biological identity assertion. |
| `previous_frame` | Prior observed frame in this track; absent for its first observation. |
| `gap_frames` | Missing frames since the previous observation. |
| `displacement`, `speed` | Step distance and distance per elapsed time. First observations have no step value. Consult column units. |
| `review_flag` | Competing feasible links were present for this observation; false does not prove correctness. |

**Track summary** reports `observation_count`, first/last frame, `duration`,
`path_length`, `net_displacement`, `gap_count`, `missing_frame_count` and a track
review flag. Path length sums distances between observed positions, including
straight-line distances over gaps; it cannot recover unobserved motion.
Single-observation tracks have zero duration/path length.

## Source review

**Review trajectories…** appears beside **Open measurements…** on
**Detect Spots per Frame** and **Build Tracks** graph cards. **Measure Objects** and
**Measure Objects + Intensity** show it only when a cached output carries
time-series observation metadata; ordinary static measurement tables do not.
The shortcut opens the same read-only source/table window as the inspector's
**Review trajectories on source…**, for the clicked node rather than the
currently selected node. It does not calculate, change selection or infer links
for unlinked observations.

Review requires current cached observations and their current source series
already resident in memory. It does not reload an unavailable source or
recalculate missing/stale observations. Pending calculation or source changes
block review of the old result. After an explicit calculation, **Refresh view**
can load the new current result without calculating again.

## Persistence and limits

Both outputs use ordinary table display, CSV/TSV export, decimal presentation,
batch execution and generated Python. Batch manifests retain time-series and
linker evidence per source item; keep them with the exact tables. Collected
datasets preserve that item evidence but do not present several series as one
trackable coordinate frame. Track IDs can repeat between separate source items.

Generated Python exposes a node's primary output in its result mapping. To
access the summary independently there, connect **Track summary** to a table
node such as **Select Table Columns** (all columns), or to a separate Batch
Output. The examples include this explicit summary branch.

Annotation/reordering keeps evidence only while protected scientific fields
survive unchanged. Removing or overwriting those fields clears the evidence
explicitly; merging does not invent shared geometry. Cancelled work publishes
no partial table, and source revisions invalidate cached results.

There is no splitting/fusion, lineage editing, GPU linking, deformable tracking,
appearance model, rotation/scale matching or automatic drift correction. Dense
candidate neighborhoods can exceed explicit memory/assignment limits; VIPP
fails with guidance rather than silently sampling or dropping candidates.

Synthetic checks cover 2D/3D known motion, anisotropic scales, empty frames,
gaps, competing links, persistence and stale review. The documented local
development validation was native Windows-only; read the
[release evidence](validation-status.md#0160a3-scope-and-evidence) for the exact
hosted native CI and installed-package routes tested. These checks do not
establish acquired-microscopy accuracy, minimum-dependency support or
large-volume memory/performance; those require separate qualification.

The assignment backend uses SciPy's
[linear sum assignment](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linear_sum_assignment.html).
The distance gate, adjacent-first gap tiers, immutable observation evidence and
review flags are VIPP's additional rules.
