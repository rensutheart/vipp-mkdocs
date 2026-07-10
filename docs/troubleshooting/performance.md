# Performance

## If Updates Feel Slow

Try these in order:

1. Turn `Run all in BG` off and compare latency.
2. Disable thumbnails globally.
3. Switch preview mode from `MIP` to `Slice`.
4. Turn `Link napari/VIPP sliders` off when you need a fixed reference view.
5. Reduce graph fan-out while tuning upstream nodes.
6. Use `Smart interactive cache` or `Low-memory mode`.
7. Mark expensive intermediates with `Keep output cached`.

## Background Execution

`Run all in BG` controls how many graph recomputes are dispatched to background
processing.

- Off: only known slower operations use background mode.
- On: all recomputes use background mode.

The `Cancel` button cancels queued reruns and asks cooperative operations to
stop. It cannot forcibly interrupt a NumPy, SciPy, or scikit-image call already
inside a work unit.

## Expensive Node Families

Expect heavier computation from:

- 3D filtering;
- rolling-ball or background subtraction;
- rescale axes;
- distance transforms and watershed;
- 3D mesh morphology;
- skeleton graph tables;
- colocalization tables on large volumes;
- deconvolution.

## Batch Runs

Batch runs use low-memory retention internally. Add explicit `Batch Output`
nodes so VIPP keeps and writes only the outputs that matter.

Large OME-Zarr or lazy inputs can still materialize when an eager operation
runs. Cache mode controls retained graph outputs; it cannot remove every
temporary allocation made inside NumPy, SciPy, or scikit-image.
