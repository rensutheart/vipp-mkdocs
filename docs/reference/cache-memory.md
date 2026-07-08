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

## Per-Node Keep Cached

Use `Keep output cached` for important intermediates such as:

- expensive background correction;
- a rescaled reference image;
- a manual measurement table;
- a segmentation mask feeding many branches.

This setting affects cache retention only. It does not force a node to
calculate.

## Large-Data Direction

Future large-data work should add:

- preview-resolution controls;
- sampled histograms;
- operation capability declarations;
- OME-Zarr pyramid export;
- warnings before eager-only nodes materialize large lazy arrays.

