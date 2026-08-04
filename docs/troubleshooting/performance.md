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

If optional CUDA support is installed, also inspect the toolbar's actual-run
summary and node badges. In ordinary 0.13.0a1 execution, **Auto** does not carry
local timing evidence and therefore resolves fresh candidates to CPU. Use
**Prefer GPU** to use every reviewed eligible accelerator regardless of speed,
or use **Selective** for per-node choices and **Find fastest**. Then use
**Compute setup and memory…** and the badge reason to understand any call-specific
CPU decision or fallback. Do not infer GPU use from the selected mode. For the complete decision sequence and operation matrix, see
[choose and verify CPU or GPU compute](../how-to/choose-compute.md).

## CPU, Auto, Prefer GPU, and Selective compute

- **CPU** runs the authoritative host implementation everywhere.
- **Auto** is conservative and never benchmarks implicitly. Standard 0.13.0a1
  execution supplies no performance evidence, so fresh Auto calls stay on CPU;
  the API can accept validated evidence explicitly.
- **Prefer GPU** uses every scientifically eligible reviewed public GPU
  candidate without requiring it to beat CPU. It still enforces all dtype,
  parameter, dependency, environment, parity, and memory gates, and unsupported
  nodes receive explained ordinary CPU decisions.
- **Selective** exposes per-node library choices plus node and whole-pipeline
  benchmarking. A separate lock preserves an authored choice during **Find
  fastest pipeline…**.

Benchmarking uses the exact current data and validates parity before timing. A
whole-pipeline search can be intentionally expensive because it compares
alternatives whose winner is not known in advance. Its overall bar reports
nodes/search progress; its current-operation bar reports truthful checkpoints
within the active parity, warmup, or timed call. If the time limit is reached,
the result must say which comparisons completed and remain. Exact completed
records can be reused on retry.

Do not change dtype only to win a benchmark unless that conversion is a
scientifically intended workflow step. Some GPU kernels, especially filtering
and deconvolution, gain much more on `float32` than on native `uint16`, and a
particular native-integer GPU path may be ineligible because it cannot preserve
the CPU result. If conversion is appropriate for the analysis, add and report
an explicit `Convert Dtype` node; VIPP never synthesizes one for the optimizer.

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

The same rule applies to CuPy/cuCIM calls and file writers. GPU progress is
published only after stream synchronization at a declared checkpoint, so a
monolithic plane/volume can appear stationary until that call finishes. This
is an honest boundary, not a stalled percentage. Cooperative cancellation then
waits for synchronization and cleanup before output publication.

## GPU memory and fallback

VIPP evaluates an operation-specific conservative device-memory estimate
before launching a GPU segment. **Compute setup and memory…** reports separate
VRAM on a discrete NVIDIA device; the CPU/cache indicator reports host RAM.
The bounded M1 Max CPU smoke showed system RAM once with no fabricated separate
VRAM. A future unified-memory accelerator provider must report one shared
CPU/GPU budget rather than adding RAM and nominal VRAM as though independent.

With visible fallback, one complete device segment can retry on CPU after a
classified runtime OOM only after the GPU attempt synchronizes and cleans up.
The badge turns amber and the execution report retains the attempted segment,
required/available memory where known, exception, cleanup, and CPU retry result.
Prefer GPU requires this visible policy. Strict selective fallback returns the
typed failure. Other GPU faults are not silently treated as OOM.

## Switching Between Node Results

When the same logical node/output recalculates, VIPP keeps its compatible
active **Inspect** layer and swaps only the data reference. The reference is a
non-writeable view of the exact node pixels; no full-volume image copy is made.
Its compatible per-output display profile and napari camera, displayed
dimensions, slice positions, zoom, translation, and rotation are preserved, so
isolated tuning stays focused on the same region. Pinned layers are separate
viewer artifacts and do not receive this saved per-output profile behavior.

Switching to a different logical output restores that output's own remembered
profile or initializes safe defaults. Presentation settings do not leak from
one scientific result into another. Use the inspector reset-to-defaults action
to clear a selected output's saved style. Stale contrast workers are invalidated
when their output context changes.

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
