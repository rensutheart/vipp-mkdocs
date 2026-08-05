# Performance

## If Updates Feel Slow

Try these in order:

1. Leave `Run all in BG` off initially so adaptive execution can choose between
   immediate and background work. Turn it on if repeated small recomputes still
   make interaction uncomfortable.
2. Set **Thumbnail detail** to **Low (90 × 55)** while authoring a large graph.
3. Switch **Contrast range** from **Stack** to **Slice** when a stable
   whole-volume brightness window is unnecessary.
4. Switch preview mode from `MIP` to `Slice`, or disable thumbnails globally.
5. Turn `Link napari/VIPP sliders` off when you need a fixed reference view.
6. Reduce graph fan-out while tuning upstream nodes.
7. Use `Smart interactive cache` or `Low-memory mode`.
8. Mark expensive intermediates with `Keep output cached`.

If optional CUDA support is installed, also inspect the toolbar's actual-run
summary and node badges. With no exact compatible history, **Auto** uses
reviewed GPU defaults wherever all safety gates pass. Accelerated-only history
makes the next global Auto run measure CPU once on the same execution surface;
once both observations exist, a later matching run applies the 1.20x/20-ms
gate. Auto never silently benchmarks multiple implementations. Use
**Prefer GPU** to use every reviewed eligible accelerator regardless of speed,
or use **Custom** for per-node choices and **Find fastest**. Then use
**Compute setup and memory…** and the badge reason to understand any call-specific
CPU decision or fallback. Do not infer GPU use from the selected mode. For the complete decision sequence and operation matrix, see
[choose and verify CPU or GPU compute](../how-to/choose-compute.md).

## CPU, Auto, Prefer GPU, and Custom compute

- **CPU** runs the authoritative host implementation everywhere.
- **Auto** starts with reviewed GPU defaults. Accelerated-only exact compatible
  history makes the next global Auto run measure CPU once on the same execution
  surface. A later matching run uses acceleration only if it clears the
  1.20x/20-ms gate. Only successful, fallback-free completed full-pipeline wall
  times are retained; interactive, batch, and registry-lifecycle surfaces are
  never mixed. Auto never silently benchmarks multiple implementations.
- **Prefer GPU** uses every scientifically eligible reviewed public GPU
  candidate without requiring it to beat CPU. It still enforces all dtype,
  parameter, dependency, environment, parity, and memory gates, and unsupported
  nodes receive explained ordinary CPU decisions.
- **Custom** exposes per-node library choices plus node and whole-pipeline
  benchmarking. A separate lock preserves an authored choice during **Find
  fastest pipeline…**.

Benchmarking uses the exact current data and validates parity before timing. A
whole-pipeline search can be intentionally expensive because it compares
alternatives whose winner is not known in advance. Its overall bar reports
nodes/search progress; its current-operation bar reports truthful checkpoints
within the active parity, warmup, or timed call. If the time limit is reached,
the result must say which comparisons completed and remain. Exact completed
records can be reused on retry.

Find fastest can establish a private fresh baseline when the current graph or
parameters are newer than the displayed result. If a synchronized GPU
incumbent has enough repeat evidence, it may stop a cooperative CPU warm call
after the CPU has exceeded a confidence-adjusted decision bound. A report such
as `CPU > 10.6 s; stopped early` is a censored lower bound, not an exact timing
and not reusable timing history. Parity and graph-wide transfer costs still
apply. A changed modeled assignment must pass final paired pipeline validation;
when the current assignment wins, its fresh baseline and conservative
comparison evidence are reported without a redundant paired run against itself.

Compute mode and per-node backend controls are disabled during calculation or
benchmarking. They unlock after normal completion. To select another policy
sooner, use the visible cancellation action and wait for synchronization and
cleanup. A failed, canceled, or OOM worker
never replaces earlier processing results with uncomputed or
provenance-unknown values. A verified source boundary may be accepted. Only
when cleanup itself failed may a completed processing node also be accepted,
and then only with matching actual-implementation provenance; all other
outputs, thumbnails, and badges remain coherent.

Cleanup failure is different from ordinary cancellation or visible fallback:
the accelerator runtime cannot be proven safe. VIPP disables calculation,
policy changes and policy-changing undo/redo, node benchmarking, **Find
fastest**, and new batch starts until the application is restarted. It also
requests cancellation of other compute already running in the process; wait
for those workers to acknowledge cancellation before closing their dialogs.

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

## Thumbnail Work After A Pipeline Finishes

A completed scientific pipeline can be followed by Stack contrast work for its
node-card thumbnails. This is a separate presentation calculation: it does not
mean a node is recalculating or that its CPU/CuPy/cuCIM provenance changed.

Use the controls independently:

- **Thumbnail detail** chooses Low (90 × 55), Standard (180 × 110), or High
  (360 × 220) backing detail for the fixed card viewport. High can improve
  HiDPI display or downsampling but does not guarantee a larger on-screen card.
  Low redraws faster, but it does not reduce the amount of data inspected by
  Stack contrast.
- **Contrast range: Stack** reads each complete result once, caches exact
  resolution-independent limits, and keeps brightness stable while T/Z/C
  changes. **Slice** uses CPU-local normalization of the selected detail's
  spatially sampled current view and avoids the full-output scan. Its limits may
  therefore change slightly between Low, Standard, and High.
- **Settings > Thumbnail statistics** chooses Auto, CPU, or Prefer GPU for this
  display-only Stack work.

Native `uint8` and `uint16` Stack Percentile calculations use exact dtype-aware
histograms instead of sorting a float copy; Min-max uses an exact native CPU
reduction.
Auto sends eligible cold Percentile work to GPU at 384 MiB for `uint8` or
512 MiB for `uint16`, then at 32 MiB once the histogram path is warm. These
thresholds use the complete output's native bytes and dtype, not thumbnail
detail. They are conservative measured heuristics, not universal fastest
guarantees: data distribution, hardware, CUDA startup, residency, and competing
work can move the crossover. Float and other-dtype percentiles retain the exact
NumPy-compatible CPU path. Forcing main compute to CPU also hard-forces these
statistics to CPU; main Prefer GPU is the explicit override and makes
presentation Auto prefer an eligible GPU.

CPU-only micro-workloads (at most 1 MiB total and no more than eight requests
or aggregate channel lanes) finish inline to avoid worker-queue overhead and
usually do not show toolbar progress. Larger, high-channel, and GPU work remains
background and cancellable. A missing progress flash for a tiny result therefore
does not mean statistics were skipped; confirm the completed Stats chip.

Read the small card chip—not the scientific badge—to see pending **Stats…**,
**Stats · CPU**, **Stats · GPU**, **Stats · CPU fallback**, or
**Stats · error**. Hover it for the algorithm, processed bytes, elapsed time,
reason, crossover, fallback, and failure. Toolbar progress names the active
node/backend/phase. CPU integer histogram and min-max paths advance and cancel
between bounded chunks. An active GPU kernel/synchronization or float/other-dtype
NumPy percentile may have a non-interruptible inner pass; VIPP identifies the
phase and applies `Cancel` at the next cooperative boundary. Cancellation
retains provisional thumbnails and already cached exact limits; it cannot claim
a partial result as complete.

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
Prefer GPU requires this visible policy. Strict Custom fallback returns the
typed failure. Other GPU faults are not silently treated as OOM.

On Windows, physical RAM and system commit are separate limits. VIPP reports
both and preflights the optional Auto CPU timing comparison against both
reserves. If headroom is unsafe, Auto keeps its reviewed safe assignment and
explains that the CPU evidence was skipped; this does not mean the existing
assignment was newly benchmarked or proved optimal.

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

Card thumbnails are rendered at the selected Low, Standard, or High detail.
Their downsampling and contrast work affect visualization only, never the
scientific array. Stack contrast can still read the complete output even when
Low detail is selected; use Slice when that scan is not wanted.

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
