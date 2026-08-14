# Choose and verify CPU or GPU compute

VIPP 0.13.0a7 lets one workflow request **CPU**, **Auto**, **Prefer GPU**, or
**Custom** compute. The request is not the execution record: the node badge
and accepted run provenance say what actually ran.

CPU remains the portable scientific reference. GPU implementations are
considered only inside operation-specific regions that preserve the declared
CPU contract. An unsupported dtype, parameter, shape, dependency, memory
budget, or environment normally produces an explained CPU decision. A forced
Custom GPU choice can instead produce an amber visible fallback or a typed
failure; some invalid or non-fallback-safe calls fail under either policy.

## Choose a pipeline policy

| Mode | Use it when | What to expect |
| --- | --- | --- |
| **Auto** | The recommended, learning new-session default | With no exact compatible history, use reviewed GPU defaults. Accelerated-only history makes the next global Auto run measure CPU once on the same execution surface; a later matching run applies the 1.20x/20-ms gate to the pair. Auto never silently benchmarks multiple implementations. |
| **CPU** | Establishing a portable reference, diagnosing a provider, or requiring host execution | Every calculated operation uses its authoritative CPU implementation. |
| **Prefer GPU** | Placing as much scientifically eligible work on GPU as possible, regardless of speed | Every reviewed public GPU candidate is considered, including providers not admitted to Auto. An eligible GPU is used even when it is only slightly faster, tied, or slower than CPU. Unsupported nodes receive an explained ordinary CPU decision. |
| **Custom** | Using GPU, comparing providers, or authoring reviewed per-node preferences | Implemented nodes expose CPU and one choice per declared GPU library; node and whole-pipeline benchmarking become available. Applying a measured pipeline assignment records Custom preferences. |

**Prefer GPU bypasses only the CPU-versus-GPU speed gate.** Scientific parity,
dtype, parameter, shape, optional dependency, environment, provider, and memory
admission remain mandatory. VIPP never inserts a cast or changes an authored
parameter to place more work on GPU. Developer-hidden implementations remain
excluded unless an advanced request explicitly enables experimental admission;
that does not turn them into public support.

If every eligible GPU candidate has complete comparable timing evidence,
Prefer GPU chooses the fastest GPU. If that evidence is incomplete, it chooses
deterministically by stable implementation ID rather than requiring a CPU-speed
comparison. This stable choice is not a claim that the selected GPU is fastest.

A schema-3 workflow opens in **CPU**, not Auto, because the older file did not
record compute intent. A schema-4 workflow restores its portable request, but
not a promise that the same backend exists or is fastest on another machine.

The toolbar presents the modes in default-first order: **Auto**, **CPU**,
**Prefer GPU**, then **Custom**. Switching to Custom while VIPP is idle does not
discard or relabel a valid calculation. The existing images and actual
CPU/GPU provenance remain visible. If those decisions differ from the saved
Custom choices, VIPP marks the badges and summary as a **previous result**;
the Custom choices take effect when a node preference changes, you calculate,
or you apply a reviewed optimizer proposal.

Compute policy cannot change underneath active work. While a pipeline
calculation, node benchmark, or **Find fastest** analysis is running, the mode
and applicable per-node controls are disabled until normal completion. To
select another policy sooner, use the explicit **Cancel calculation**, **Cancel
benchmark**, or **Cancel analysis** control first. The controls remain locked
while the worker reaches a cooperative checkpoint,
synchronizes, and releases CPU/GPU resources. This guarantees that selecting
CPU cannot leave an earlier GPU calculation or timing comparison running.

## Keep Thumbnail Statistics Separate

The scientific compute policy also establishes safety boundaries for
presentation work, but a thumbnail-statistics backend is not scientific node
provenance. **Settings > Thumbnail statistics** provides local **Auto**,
**CPU**, and **Prefer GPU** control for full-output Stack contrast:

- main compute **CPU** hard-forces presentation CPU and prevents CUDA
  initialization;
- main **Prefer GPU** makes presentation Auto prefer every eligible CuPy
  Percentile histogram;
- main **Auto** and **Custom** leave presentation Auto adaptive; and
- an explicit presentation CPU or Prefer GPU choice otherwise controls new
  statistics results.

Presentation Auto considers native `uint8`/`uint16` Percentile work and uses the
complete output's byte size. Its conservative cold crossover is 384 MiB for
`uint8` or 512 MiB for `uint16`; both become 32 MiB after one successful GPU
histogram. These measured default heuristics are not a universal fastest
guarantee because data distribution, hardware, CUDA startup, residency, and
competing work matter. It does not use Low/Standard/High/Very High backing resolution.
Use **Prefer GPU** as the explicit override. Min-max uses an exact native CPU
reduction. Float and other-dtype percentiles retain the exact NumPy-compatible
CPU calculation. Select a node and read its separate **Thumbnail contrast**
inspector row—**Calculating… / CPU · NumPy / GPU · CuPy / CPU fallback /
Error**—for what happened; the ordinary CPU/CuPy/cuCIM badge remains in the node
title row as the record of what produced the node output.

## A safe practical sequence

1. Run a representative item on **CPU** and inspect the decisive images,
   masks, labels, and tables. Retain this result when CPU/GPU parity matters.
2. Open **Compute setup and memory…**. Read its three short rows—**CUDA and
   GPU**, **Optional cuCIM**, and **VIPP GPU coverage**—then follow the one
   recommended next step. Open **Show advanced details** only when you need the
   scientific stack, device, eligibility, RAM/VRAM, and provider evidence. The
   window can save a privacy-redacted support report; VIPP never executes a
   repair command automatically.
3. Keep **Auto** for normal calculation and read the actual-run summary and
   per-node badges. Auto starts with reviewed safe GPU defaults. Successful,
   fallback-free completed full-pipeline runs—whether CPU, GPU, or mixed—add
   only their wall time to machine-local history. If exact compatible history
   is accelerated-only, the next global Auto run measures CPU once on the same
   execution surface. Once both observations exist, a later matching run uses
   acceleration only when it clears the 1.20x/20-ms gate; otherwise it uses CPU.
   Interactive, batch, and registry-lifecycle timing surfaces are never mixed.
   Auto never silently benchmarks multiple implementations. Before the optional
   CPU comparison, VIPP checks conservative host-memory headroom. On Windows it
   checks both available physical RAM and remaining system commit. If the
   comparison would consume the reserve, Auto keeps the reviewed safe assignment,
   explains the skipped evidence, and can try again on a later compatible run.
4. Switch to **Prefer GPU** when you want every reviewed eligible accelerator
   region without first benchmarking whether it beats CPU. Read the ordinary
   CPU reasons for unsupported nodes; this mixed result is the intended policy.
5. Switch to **Custom** when you want an authored per-node choice or an
   explicit performance measurement. Normal choices are **Auto for this
   node**, **CPU**, and one
   **GPU · library** entry. **Best GPU** appears only when several GPU libraries
   genuinely compete. A loaded exact implementation pin remains visible as an
   advanced compatibility choice until replaced.
6. Benchmark an eligible node for a focused comparison, or choose **Find
   fastest pipeline…** to compare every eligible implementation in the current
   writer-free subgraph. If the displayed result is stale, Find fastest first
   establishes a private current-graph baseline after cancellation cleanup; it
   does not require you to publish an ordinary replacement calculation. Review
   the proposal before applying it;
   accepted winners become Custom per-node preferences. Raw isolated-node
   timings remain separate from Auto's complete-pipeline history, although a
   later successful, fallback-free completed run of the accepted assignment
   can add a compatible full-pipeline observation.
7. Save the workflow only after accepting the portable preferences. For a real
   run, retain the execution report or batch provenance that records the exact
   implementations, environment, fallbacks, memory decisions, and cleanup.

Choosing a backend does not lock it against optimization. Use the separate
optimizer lock only when a node must be excluded from the search. The optimizer
can evaluate a detached manual node without overwriting its live cached result;
it changes no node preference until the final assignment is reviewed and
applied.

## Use a dtype repair only after reviewing it

When `uint8` or `uint16` is the only blocker between a node and a reviewed
finite-`float32` GPU region, the node can show a small **GPU tip**. Select the
node to see the affected input, exact proposed conversion, and memory trade-off.
The tip remains available in Prefer GPU after calculation while that same
blocker is still present.

**Add conversion** inserts an ordinary visible **Convert Dtype** node on that
one input. The proposed `float32` **Preserve** conversion changes storage dtype
without rescaling pixel values, and the graph edit has one-step Undo. Shared
branches remain connected to the original source unless they already use the
affected input path. VIPP revalidates the suggestion before applying it and
does nothing if the input, candidate, or explicit Custom choice changed.

This button edits the authored workflow; calculation itself still never casts
silently. Review downstream thresholds, memory, output dtype, and scientific
meaning before accepting it. A visible conversion can remain resident with
eligible downstream GPU work, but eligibility is not proof that conversion is
appropriate for the analysis.

## Read benchmark progress honestly

Whole-pipeline optimization shows two progress streams:

- **Overall pipeline** tracks completed node/provider comparisons and final
  assignment validation.
- **Current operation** tracks truthful checkpoints inside the active parity,
  cold-call, warmup, or timed call.

A single NumPy, SciPy, CuPy, CuPyX, or cuCIM call can remain at one percentage
until it returns because VIPP cannot observe a scientifically safe subdivision.
A reached time limit means planned comparisons remain; it does **not** prove
that the current assignment is optimal. The result identifies completed and
remaining work, and complete records for the exact workload and environment
can be reused on retry. Editing data, parameters, code/policy identity, or the
relevant environment invalidates reuse.

A completed comparison remains inspectable when the speed evidence is too
close to recommend a winner. The result groups one heading per workflow node
with a separate row for every tested CPU, CuPy-family, or cuCIM implementation.
The compact columns show total execution time, scientific agreement, and the
outcome; expanded details separate resident compute, transfers, **First run**
cost, memory, and evidence provenance. An inconclusive outcome leaves
the authored assignment unchanged. It is not a GPU eligibility failure.

When a synchronized GPU candidate has enough repeated measurements to be a
reliable incumbent, the optimizer may stop a cooperative CPU warm call once its
elapsed time exceeds the incumbent's one-sided confidence bound plus a material
margin. The dialog reports a censored lower bound such as **CPU > 10.6 s;
stopped early**, not an exact CPU timing. Censored results are not reused as
timing-history samples. Scientific parity is checked independently, required
CPU/GPU transfers remain in the whole-graph model, and a changed modeled
assignment must pass final paired end-to-end validation before it can be
offered. When the already-current assignment wins, VIPP reports its fresh
baseline, parity, and conservative exact-or-censored comparison evidence; it
does not claim a redundant paired comparison against itself. GPU candidates are not
discarded from a one-off transfer-inclusive duration because a resident
pipeline can amortize those transfers.

Current node benchmarking requires resolved ordered inputs, one output, and no
writer side effect. Whole-pipeline optimization operates within one supported
accelerator runtime and the calculated writer-free graph frontier. Unsupported
nodes remain CPU candidates; manual barriers do not justify benchmarking an
unrunnable descendant.

<a id="gpu-regions-in-0130a1"></a>
<a id="gpu-regions-in-0130a7"></a>

## GPU regions in 0.13.0a7

The table is a readable summary, not a substitute for the executable policy.
VIPP's eligibility explanation is authoritative for the exact call.

| Operation | GPU library | Broad admitted data/shape | Important first-region limits and common CPU decisions |
| --- | --- | --- | --- |
| Rolling-Ball Background | cuCIM | `uint8`, `uint16`, or `float32`; 2D slice-wise or 3D | Radius 1–500 in 2D and 1–50 in 3D. Other dtypes/radii use CPU. The declared float32 parity region is not finite-only. |
| Subtract Background | cuCIM | `uint8`, `uint16`, or `float32`; 2D slice-wise or 3D | Same reviewed radius limits as Rolling-Ball. The declared float32 parity region is not finite-only. |
| Extract Channel | CuPy | Explicit channel axis | Prefer GPU keeps a host-entry extraction on CPU so only the selected channel is uploaded. An explicit Custom GPU choice can expose a resident allocation-sharing view. Ambiguous axes use CPU or fail rather than being guessed. |
| Convert Dtype | CuPy | `uint8` or `uint16` to `float32` | Exact **Preserve** mode only: pixel values are not rescaled. Other dtype/mode combinations use CPU. |
| Median Filter | CuPyX | `uint8`, `uint16`, or finite `float32` with complete facts proving no negative zero; independent `YX` planes | Canonical odd footprint 1–51; unsupported float facts or footprint use CPU. |
| Gaussian Blur | CuPyX | finite `float32`; independent `YX` planes | Sigma 0–12. Native integer and `float64` Gaussian calls remain CPU. |
| Gaussian Blur 3D | CuPyX | finite `float32`; resolved `ZYX` volumes | Each spatial sigma 0–12. Native integer and `float64` calls remain CPU. |
| Richardson-Lucy Deconvolution | CuPy/CuPyX | finite `float32` Image and PSF; 2D or 3D | Odd PSF extents, default-safe options, authored `filter_epsilon` from `1e-12` through `1e-6`, and 1–100 iterations. The v2 backend-agreement gate does not validate restoration quality. |
| Richardson-Lucy TV Deconvolution | CuPy/CuPyX | finite `float32` Image and PSF; 2D or 3D | Lambda zero inherits ordinary RL's expanded region. Positive TV retains the shipped tuple (`lambda=0.002`, TV epsilon `1e-6`, filter epsilon `1e-12`, denominator floor `0.05`) at 10 or 25 iterations. |
| Canny Edges | CuPy/CuPyX | Boolean, `uint8`, or `uint16`; independent `YX` planes | Sigma 0–12 and finite ordered quantile thresholds. Floating-point input remains CPU in this exact-mask region. |
| Otsu Threshold | CuPy/CuPyX | Boolean, signed/unsigned integers, and `float16`/`float32`/`float64` | Integer occupied span must be at most 65,536 levels; wide integers and per-slice cases need sufficient exact facts. Float histograms use 2–65,536 saved bins. |
| Binary Threshold | CuPy | scalar finite `float32` images | Uses the exact authored finite threshold and returns a resident Boolean mask. Unsupported dtype/channel semantics use CPU; VIPP does not round or replace the threshold. |
| Sigma Filter | CuPy | native-endian `uint8`, `uint16`, or finite `float32`; independent `YX` planes | Radius 0.5–10 and reviewed finite value/parameter facts. ROI/mask behavior is outside version 1. |
| Remove Small Objects | CuPyX | Boolean mask; resolved 2D or 3D | Face or Full connectivity. Integer-label cleanup remains CPU. |
| Fill Holes | CuPyX | Boolean mask; resolved 2D or 3D | Face or Full connectivity with `Maximum hole size = 0` (fill every enclosed hole). Positive bounded-hole-size cleanup remains CPU. |
| Label Connected Components | CuPyX | Boolean mask; resolved 2D or 3D | Preserves exact deterministic `int32` label numbering. Numeric masks and oversized 2D/3D blocks use CPU. In non-CPU planning, a Boolean call not resolved as 2D or 3D is a typed preflight failure in this alpha. |
| Measure Objects | cuCIM | native-endian, non-negative `int32` labels; 2D or 3D | Basic measurement schema only. Extended shape, axis, boundary, moment, and derived-ratio groups remain CPU. |
| Measure Objects + Intensity | cuCIM | the same labels plus native-endian Boolean, `uint8`, `uint16`, or finite `float32` intensity | Matching shapes and the basic table schema are required; extended columns or unsupported intensity data use CPU. |

Canny and Otsu retain the CPU node's explicitly declared RGB/RGBA BT.601 luma
handling where the underlying dtype/profile is admitted. An ambiguous or
invalid channel axis remains on the CPU/error path rather than being guessed.

VIPP never inserts a cast while calculating. If `uint8`/`uint16` dtype is the
only blocker, it may offer the reviewed **Add conversion** graph edit described
above. Otherwise add **Convert Dtype** yourself. In both cases, review its mode,
inspect downstream thresholds/writers, and report it. Conversion can unlock
larger GPU gains across filtering, deconvolution, and segmentation, but it
changes the authored data representation. Never convert only to make a
benchmark look faster.

## Installation and platform boundary

The `gpu-cuda13` extra installs the pinned CuPy/CuPyX CUDA track. It does not
include the separately reviewed cuCIM build used by the background and basic
measurement candidates, so those nodes normally remain CPU after a standard
public GPU install. Windows users can optionally build the pinned cuCIM 26.6.0
source locally and approve it with its generated manifest; see the
[Windows CUDA and cuCIM guide](../getting-started/windows-cuda.md).

Public admission requires native Windows, CPython 3.12, the pinned CUDA 13.2
runtime and scientific/provider stack, driver API 13.3 or newer, and a probed
NVIDIA CUDA device with compute capability 7.5 or newer. The GPU model is
recorded in provenance rather than used as an allowlist. Auto, Prefer GPU, and
Custom use the same device gate; each operation still has its own exact
workload, memory, dependency, and cleanup requirements. The Linux CUDA command
is useful for qualification/development but the current public policy resolves
Linux GPU candidates to CPU. CUDA has no macOS path.

Hardware, driver, compiler, and reduction-order differences can produce minor
floating-point variation across otherwise compatible GPUs within a provider's
declared tolerance. Record the GPU model, compute capability, driver, CUDA
stack, Python and scientific-package versions, actual implementation IDs, and
execution report. Validate consequential work against the CPU reference before
combining results from different environments.

See [installation](../getting-started/installation.md) for commands and
[validation status](../reference/validation-status.md) for the evidence and
remaining platform gaps.

## Memory, fallback, progress, and cancellation

VIPP keeps eligible adjacent operations in a private device-resident segment,
then crosses to host memory only at a planned boundary. Before launch it applies
an operation-specific conservative memory estimate. Host cache limits do not
cap every temporary CPU or GPU workspace.

**Prefer GPU always requires visible fallback.** A strict Prefer-GPU request is
invalid because the policy means GPU wherever possible and CPU everywhere else.
An unsupported node is an explained ordinary CPU planning decision, not an
attempted-device fallback.

For a forced Custom GPU choice, **visible** fallback turns a fallback-safe
availability or eligibility rejection into an amber CPU decision; **Strict**
returns a typed preflight failure. A rejection explicitly marked unsafe to
fall back fails under either setting. Global **Auto** and **Auto for this node**
in Custom use ordinary explained CPU decisions for fallback-safe preflight
rejections.

At runtime, **visible** fallback may retry one complete device segment once on
CPU after a classified OOM, but only after synchronization and proven GPU
cleanup. Its badge becomes amber and provenance keeps the failed attempt and
CPU retry. **Strict** returns the typed failure. Preflight CPU decisions are not
mislabeled as runtime OOM.

Cancellation is cooperative between nodes, resident segments, iterations,
tiles/planes, and publication stages. An opaque call can finish its current
atomic work before responding. A result is not accepted or published until
required synchronization and cleanup succeed.

A failed or OOM interactive attempt never replaces an earlier processing result
with an uncomputed or provenance-unknown value. VIPP may accept a verified
source boundary. If cleanup itself failed, VIPP may additionally accept a
completed processing node, but only when matching actual-implementation
provenance is available for its badge and report. All
other affected nodes retain prior valid outputs, thumbnails, and badges and
remain pending. Cancellation retains the prior coherent result.

If accelerator cleanup fails during a calculation, node benchmark, **Find
fastest**, or collection batch, VIPP cannot prove the runtime safe to reuse. It
requests cancellation of every other active compute owner and disables new
calculation, policy changes (including policy-changing undo/redo),
benchmark/optimizer work, and batch starts for that process. Newly measured
**Find fastest** evidence from the unsafe analysis is rolled back. If that
record-level rollback cannot be written, VIPP writes a durable poison marker
first and moves the complete local timing store to an `.unsafe-*` quarantine
filename under its cross-process lock. A restart resolves the marker or refuses
to open the active store; if the marker itself could not be written, the alert
names the file that must be moved manually. Preserve the error/provenance record
and restart VIPP; ordinary visible CPU fallback is allowed only after cleanup
succeeds.

## Keep interactive and durable execution aligned

Interactive calculation, saved batch runners, and generated Python/CLI use the
same execution service. Interactive **Save selected output…** and **Export OME
dataset…** serialize accepted cached values instead; they do not rerun the graph
or create exact compute-provenance sidecars. Preserve:

- the schema-4 workflow and complete compute request;
- for batch, the version-3 config, finalized manifest/archive, and item
  sidecars;
- for generated outputs, requested `.vipp-provenance.json` sidecars;
- the actual implementation IDs/versions and environment fingerprint; and
- CPU decisions, classified fallbacks/OOM, cancellation, and cleanup outcome.

Workflow schema 4, batch config schema 3, saved runners, and generated CLIs use
the stable value `prefer_gpu`. Saved per-node preferences remain present but
dormant outside Custom; switching back to Custom reactivates them.
`Benchmark node…` and **Find fastest pipeline…** are Custom-only. A CLI mode
override to `prefer_gpu` uses visible fallback when no fallback override is
given, while an explicit strict combination is rejected before calculation.
Every surface records the effective request and exact actual implementations in
the same execution provenance.

The saved batch runner is the production collection route. The generated
program's simple folder helper hashes each local primary source before reading,
verifies it after materialization, and privately stages and transactionally
commits each requested output/sidecar set. It does not provide multi-source
pairing, collision planning, a final source recheck immediately before
publication, checkpoints, a durable manifest, or replay/resume.
