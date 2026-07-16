# Cache And Memory

VIPP is currently an eager interactive workflow builder. Most nodes calculate
NumPy-like in-memory outputs so thumbnails, inspection, pinned layers, and
downstream edits feel immediate.

## Cache Modes

| Mode | Intended use |
| --- | --- |
| Keep all node outputs cached | Default graph design and rapid inspection. |
| Smart interactive cache | Larger graphs where repeated inspection matters but RAM is limited. |
| Low-memory mode | Memory-constrained work and batch-like runs. |

Batch collection runs use low-memory retention internally.

Calculated **manual-node** results are retained in every interactive cache mode.
That includes an expensive Richardson-Lucy deconvolution several hops upstream
from the node currently being edited. A downstream Composite → RGB mapping edit
therefore invalidates the composite and its descendants without discarding the
manual result that feeds it.

When a stale manual node blocks a branch, VIPP also temporarily retains every
dark-amber downstream result that already exists as one coherent cached
snapshot. A waiting node with no previous result remains unavailable. Smart
and Low-memory modes do not prune existing results from that waiting branch.
Recalculating the bright-amber barrier replaces the snapshot in dependency
order, after which the normal cache policy applies again.

The same retention rule protects existing results in a branch held by **Tune
node in isolation**. Starting isolation requires a coherent cached result for
the selected node and no pending or in-flight pipeline, source-load, or batch
work; it does not require every descendant to have an output. After the first
parameter edit, the tuned root is bright amber and its descendants remain
darker amber until **Apply and continue**, **Calculate all**, or **Cancel
tuning** releases the temporary boundary. Descendants without a previous
result remain unavailable while they wait. The boundary and restore snapshot
are transient and are not serialized.

Automatic upstream nodes are likewise not invalidated by an unrelated
downstream edit, but Smart/Low-memory mode may intentionally prune their cached
arrays. VIPP recomputes a pruned automatic intermediate when needed. Mark a
specific automatic node **Keep output cached** when it must survive that policy.

## Memory Guard

When keep-all mode uses too much reclaimable memory, VIPP can automatically
switch to Smart interactive cache, prune nonessential outputs, refresh the UI,
and warn the user.

The cache estimate is practical, not a full Python heap profile.

The cache-status display obtains available/total physical memory through an
operating-system-specific path:

- Windows uses `GlobalMemoryStatusEx` and does not require `os.sysconf`;
- macOS uses `host_statistics64` plus guarded `sysconf` page-size/physical-page
  queries;
- other POSIX systems use guarded `sysconf` page counters.

If a platform API is unavailable, returns an error, or supplies an invalid
value, VIPP reports memory as unavailable rather than crashing or inventing a
number. The value is still an operational estimate, and container/VM limits
can differ from host memory.

## Per-Node Keep Cached

Use `Keep output cached` for important intermediates such as:

- expensive background correction;
- a rescaled reference image;
- a manual measurement table;
- a segmentation mask feeding many branches.

This setting affects cache retention only. It does not force a node to
calculate.

## Exact Statistics Without Freezing The Interface

VIPP separates memory-bounded calculation from scientific approximation.
Automatic threshold histograms and inspector histograms visit the complete
required data in bounded chunks. The chunks limit temporary memory; they do not
sample or discard pixels.

When an input reaches 4,000,000 elements or 32 MiB, adaptive execution normally
moves image-sized work off the user-interface thread. Known expensive
operations can move earlier. Checking **Run all in BG** forces all graph
recomputes into background execution; leaving it unchecked keeps this adaptive
policy.

Several inspector calculations follow the same principle:

- automatic-threshold guides use the complete finite population and the node's
  saved method parameters;
- histogram displays count every finite value, then group the counts into a
  compact number of chart bins;
- colocalization density, ROI counts, and colocalized counts include every ROI
  voxel;
- Auto Contrast calculates exact full-input finite percentiles;
- large inspect and pinned layers use an immediate provisional display range,
  followed by exact full finite limits calculated in the background.

The provisional layer range is display-only. It does not make the node output
or downstream analysis provisional.

## Progressive Display, Atomic Scientific Cache

During a background graph run, each completed node can update its card state and
sampled thumbnail immediately while later nodes continue. If the selected cache
mode already retains that node, the same run-scoped payload can also update its
inspection layer, pinned layer, table preview, and metadata. Smart and
Low-memory modes do not retain an otherwise prunable full-volume intermediate
merely to provide this progress display.

These updates are presentation overlays owned by the active run. They do not
partially publish results into the live scientific cache. VIPP commits the
workflow outputs and execution states only after the complete result is
accepted against the same workflow and source revisions. Cancellation,
failure, a newer edit, or a superseding run discards the overlays and restores
the previous coherent cache view.

This distinction matters when monitoring a long pipeline: a newly grey/current
card and thumbnail mean that node completed in the active run, but the workflow
as a whole is not committed until the run finishes successfully.

!!! note "Background does not mean free"

    Exact work still reads the complete required input and can consume CPU,
    memory bandwidth, and operation-specific temporary memory. Background
    execution keeps napari responsive; it does not turn an eager operation into
    a lazy or lower-cost one.

## Large-Data Direction

Future large-data work should add:

- preview-resolution controls;
- more lazy and chunk-native operations;
- operation capability declarations;
- OME-Zarr pyramid export;
- warnings before eager-only nodes materialize large lazy arrays.
