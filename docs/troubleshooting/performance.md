# Performance

## If Updates Feel Slow

Try these in order:

1. Leave `Run all in BG` off initially so adaptive execution can choose between
   immediate and background work. Turn it on if repeated small recomputes still
   make interaction uncomfortable.
2. Disable thumbnails globally.
3. Switch preview mode from `MIP` to `Slice`.
4. Turn `Link napari/VIPP sliders` off when you need a fixed reference view.
5. Reduce graph fan-out while tuning upstream nodes.
6. Use `Smart interactive cache` or `Low-memory mode`.
7. Mark expensive intermediates with `Keep output cached`.

## Background Execution

`Run all in BG` controls whether background execution is forced or adaptive.

- Off: small ordinary work can run immediately; known expensive operations and
  inputs of at least 4,000,000 elements or 32 MiB run in the background.
- On: all graph recomputes use background mode.

The same large-input policy protects exact inspector work such as automatic
threshold guides, histogram summaries, colocalization density, Auto Contrast,
and generated-layer display ranges. The UI may show a calculating state before
the exact result appears.

Moving a calculation to the background does not sample the image or change its
numerical method. A complete-data calculation can still take time and compete
for memory bandwidth.

Completed nodes publish a run-scoped card state and sampled thumbnail while the
rest of a background run continues. A retained selected or pinned result can
update from the same active-run payload. This progress is deliberately
separate from the live scientific cache, which is committed only after the
whole run is accepted; cancelling or superseding the run restores the previous
coherent view.

Exact interior percentiles require one native-dtype working buffer for the
order-statistic selection. The common integer `0..100` percentile pair uses
exact extrema without that buffer. Integer Rescale maps the output in bounded
chunks, while integer Clip stays in the native dtype and avoids a whole-image
float temporary.

The `Cancel` button cancels queued reruns and asks cooperative operations to
stop. It cannot forcibly interrupt a NumPy, SciPy, or scikit-image call already
inside a work unit.

## Switching Between Node Results

For compatible napari `Image` presentations, VIPP keeps the same generated
inspect or pin layer and swaps only its data reference. The reference is a
non-writeable view of the exact node pixels; no full-volume image copy is made
for the switch. VIPP explicitly resets colormap, blending, contrast, scale, and
display metadata so presentation settings from the previous result do not
carry over. Stale contrast workers are invalidated when the selection changes.

A genuine class or layout change still needs replacement. Examples include an
`Image` versus a label-ID `Labels` layer and incompatible RGB layouts. A
Boolean mask pinned as a `Labels` overlay requires a uint8 presentation copy;
that conversion is limited to the class-changing display path and does not
replace the original node output used by downstream calculations or saving.

Card thumbnails are rendered at display resolution. Their downsampling and
contrast work affect visualization only, never the scientific array. This is
why thumbnails can update quickly without changing the exact data produced by
the operation.

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
