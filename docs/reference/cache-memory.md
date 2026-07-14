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
