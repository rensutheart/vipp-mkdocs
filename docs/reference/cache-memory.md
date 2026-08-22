# Cache And Memory

VIPP is currently an eager interactive workflow builder. Its accepted public
cache uses host NumPy-like in-memory outputs so thumbnails, inspection, pinned
layers, and downstream edits feel immediate. Eligible nodes may use private
device-resident segments during a run, but those values cross a verified host
boundary before they become public results.

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

- Windows uses `GlobalMemoryStatusEx`, reports physical RAM and system commit
  separately, and does not require `os.sysconf`;
- macOS uses `host_statistics64` plus guarded `sysconf` page-size/physical-page
  queries;
- other POSIX systems use guarded `sysconf` page counters.

If a platform API is unavailable, returns an error, or supplies an invalid
value, VIPP reports memory as unavailable rather than crashing or inventing a
number. The value is still an operational estimate, and container/VM limits
can differ from host memory.

Windows `Commit free` is remaining system commit headroom, not merely free
physical RAM or configured page-file capacity. A large allocation can fail
when commit is exhausted while some physical RAM remains. VIPP checks both
reserves before the optional Auto CPU timing comparison; when that evidence run
would be unsafe, Auto retains its reviewed safe assignment and reports the
skip. The missing CPU observation can be collected later.

## Device residency and accelerator memory

The interactive scientific cache remains host-owned. During one accepted run,
eligible adjacent GPU nodes can use a private device-resident segment so VIPP
does not transfer every intermediate back to NumPy. Private device values are
transactional execution state: they are not workflow persistence, public cache
entries, or napari layers, and they must be synchronized and cleaned before a
host result is accepted or published.

Before launching a segment, VIPP applies a conservative, operation-specific
memory model to the device inputs, outputs, simultaneously live intermediates,
library workspace, and uncertainty allowance. A fair process-wide accelerator
lease prevents unrelated VIPP jobs from interleaving on the same runtime/device
while allowing separate device keys to proceed independently.

**Compute setup and memory…** distinguishes host RAM from VRAM on a discrete
NVIDIA GPU. In the bounded M1 Max CPU smoke, VIPP presented host memory once as
system RAM and did not fabricate or add a separate VRAM total. A future Apple
or other accelerator provider that reports unified topology must instead use
one shared CPU/GPU budget row. macOS remains CPU-only in 0.13.0a8.

With **visible** fallback, one complete device segment may retry once on CPU
after a classified runtime OOM, but only after synchronization and proven
cleanup. The accepted badge becomes amber and provenance retains the attempted
segment, memory evidence, exception, cleanup, and retry. **Strict** returns the
typed failure. Availability or eligibility decisions made before device work
are still explained but are not runtime OOM fallbacks.

Cache mode limits retained graph outputs; it cannot cap every NumPy/SciPy or
CuPy/CuPyX temporary. Low-memory mode can therefore coexist with an operation
whose CPU RAM or VRAM workspace is large. Basic GPU measurement nodes also
cross a deliberate host boundary for an exact typed-table finalizer after the
bounded device calculation.

See [choose and verify CPU or GPU compute](../how-to/choose-compute.md) for the
operation regions and fallback workflow.

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
  followed by exact full finite limits calculated in the background; and
- Stack thumbnail contrast reads the complete node output once and caches its
  exact limits independently of the selected render detail. Native `uint8` and
  `uint16` Percentile calculations use a bounded exact histogram on CPU or
  eligible CuPy GPU; Min-max uses an exact native reduction. Float and
  other-dtype percentiles retain the NumPy-compatible CPU path, which may
  allocate full-array conversion or finite-filter temporaries and whose active
  NumPy call may be temporarily non-interruptible. The GPU histogram uploads one
  complete eligible input and allocates a fixed count table; memory admission
  includes both plus conservative overhead.

Slice thumbnail contrast takes the responsiveness tradeoff: it normalizes the
selected detail's spatially sampled current view rather than reading the full
slice. Low/Standard/High/Very High may therefore change Slice display limits
slightly.
This remains presentation-only and never changes a node output.

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
by themselves publish results into the live scientific cache. Normal success
commits the complete accepted result against the same workflow and source
revisions. Cancellation, a newer edit, or a superseding run discards the
overlays and restores the previous coherent cache view.

Failure/OOM handling is provenance-aware. A verified source boundary may be
accepted. A cleanup-failed result may additionally contribute a completed
processing node only when its matching actual-implementation decision is
present; an uncomputed or unreported value never replaces an earlier valid
result. Prior thumbnails and truthful CPU/GPU
badges remain visible for all other nodes, with previous/pending styling when
they do not satisfy current intent. A cleanup failure quarantines further
compute in that process until VIPP is restarted.

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

- pyramid-aware source-level selection beyond the current 90 × 55, 180 × 110,
  360 × 220, and 720 × 440 backing-detail controls. Very High uses four times
  the pixmap memory of High;
- more lazy and chunk-native operations;
- operation capability declarations;
- OME-Zarr pyramid export;
- warnings before eager-only nodes materialize large lazy arrays.
