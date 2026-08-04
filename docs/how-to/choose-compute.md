# Choose and verify CPU or GPU compute

VIPP 0.13.0a1 lets one workflow request **CPU**, **Auto**, **Prefer GPU**, or
**Selective** compute. The request is not the execution record: the node badge
and accepted run provenance say what actually ran.

CPU remains the portable scientific reference. GPU implementations are
considered only inside operation-specific regions that preserve the declared
CPU contract. An unsupported dtype, parameter, shape, dependency, memory
budget, or environment normally produces an explained CPU decision. A forced
Selective GPU choice can instead produce an amber visible fallback or a typed
failure; some invalid or non-fallback-safe calls fail under either policy.

## Choose a pipeline policy

| Mode | Use it when | What to expect |
| --- | --- | --- |
| **CPU** | Establishing a portable reference, diagnosing a provider, or requiring host execution | Every calculated operation uses its authoritative CPU implementation. |
| **Auto** | A conservative, portable new-session default | Auto never benchmarks during calculation. Ordinary interactive, saved-batch, and generated runs in this alpha do not attach local performance evidence, so their fresh Auto candidates resolve to CPU. Programmatic callers can supply validated evidence explicitly. |
| **Prefer GPU** | Placing as much scientifically eligible work on GPU as possible, regardless of speed | Every reviewed public GPU candidate is considered, including providers not admitted to Auto. An eligible GPU is used even when it is only slightly faster, tied, or slower than CPU. Unsupported nodes receive an explained ordinary CPU decision. |
| **Selective** | Using GPU, comparing providers, or authoring reviewed per-node preferences | Implemented nodes expose CPU and one choice per declared GPU library; node and whole-pipeline benchmarking become available. Applying a measured pipeline assignment records Selective preferences. |

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

## A safe practical sequence

1. Run a representative item on **CPU** and inspect the decisive images,
   masks, labels, and tables. Retain this result when CPU/GPU parity matters.
2. Open **Compute setup and memory…**. Check the installed scientific stack,
   device, eligibility reason, host RAM, and separate VRAM where applicable.
   Copy the proposed fresh-environment command if setup is incomplete; VIPP
   never executes it automatically.
3. Keep **Auto** for a conservative calculation and read the actual-run summary
   and per-node badges. In the normal 0.13.0a1 interfaces, Auto has no attached
   local timing evidence and therefore resolves fresh candidates to CPU; that
   CPU result is an ordinary decision, not a fallback.
4. Switch to **Prefer GPU** when you want every reviewed eligible accelerator
   region without first benchmarking whether it beats CPU. Read the ordinary
   CPU reasons for unsupported nodes; this mixed result is the intended policy.
5. Switch to **Selective** when you want an authored per-node choice or an
   explicit performance measurement. Normal choices are **Follow pipeline
   policy**, **CPU**, and one
   **GPU · library** entry. **Best GPU** appears only when several GPU libraries
   genuinely compete. A loaded exact implementation pin remains visible as an
   advanced compatibility choice until replaced.
6. Benchmark an eligible node for a focused comparison, or choose **Find
   fastest pipeline…** to compare every eligible implementation in the current
   calculated, writer-free subgraph. Review the proposal before applying it;
   accepted winners become Selective per-node preferences, not an invisible or
   permanent Auto cache.
7. Save the workflow only after accepting the portable preferences. For a real
   run, retain the execution report or batch provenance that records the exact
   implementations, environment, fallbacks, memory decisions, and cleanup.

Choosing a backend does not lock it against optimization. Use the separate
optimizer lock only when a node must be excluded from the search. The optimizer
can evaluate a detached manual node without overwriting its live cached result;
it changes no node preference until the final assignment is reviewed and
applied.

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

Current node benchmarking requires resolved ordered inputs, one output, and no
writer side effect. Whole-pipeline optimization operates within one supported
accelerator runtime and the calculated writer-free graph frontier. Unsupported
nodes remain CPU candidates; manual barriers do not justify benchmarking an
unrunnable descendant.

## GPU regions in 0.13.0a1

The table is a readable summary, not a substitute for the executable policy.
VIPP's eligibility explanation is authoritative for the exact call.

| Operation | GPU library | Broad admitted data/shape | Important first-region limits and common CPU decisions |
| --- | --- | --- | --- |
| Rolling-Ball Background | cuCIM | `uint8`, `uint16`, or `float32`; 2D slice-wise or 3D | Radius 1–500 in 2D and 1–50 in 3D. Other dtypes/radii use CPU. The declared float32 parity region is not finite-only. |
| Subtract Background | cuCIM | `uint8`, `uint16`, or `float32`; 2D slice-wise or 3D | Same reviewed radius limits as Rolling-Ball. The declared float32 parity region is not finite-only. |
| Median Filter | CuPyX | `uint8`, `uint16`, or finite `float32` with complete facts proving no negative zero; independent `YX` planes | Canonical odd footprint 1–51; unsupported float facts or footprint use CPU. |
| Gaussian Blur | CuPyX | finite `float32`; independent `YX` planes | Sigma 0–12. Native integer and `float64` Gaussian calls remain CPU. |
| Gaussian Blur 3D | CuPyX | finite `float32`; resolved `ZYX` volumes | Each spatial sigma 0–12. Native integer and `float64` calls remain CPU. |
| Richardson-Lucy Deconvolution | CuPy/CuPyX | finite `float32` Image and PSF; 2D or 3D | Odd PSF extents, default-safe options, `filter_epsilon=1e-8`, and 1–25 iterations. The CPU default epsilon remains CPU. |
| Richardson-Lucy TV Deconvolution | CuPy/CuPyX | finite `float32` Image and PSF; 2D or 3D | Lambda zero inherits ordinary RL. Positive TV admits the shipped tuple (`lambda=0.002`, TV epsilon `1e-6`, filter epsilon `1e-12`, denominator floor `0.05`) at 10 or 25 iterations. |
| Canny Edges | CuPy/CuPyX | Boolean, `uint8`, or `uint16`; independent `YX` planes | Sigma 0–12 and finite ordered quantile thresholds. Floating-point input remains CPU in this exact-mask region. |
| Otsu Threshold | CuPy/CuPyX | Boolean, signed/unsigned integers, and `float16`/`float32`/`float64` | Integer occupied span must be at most 65,536 levels; wide integers and per-slice cases need sufficient exact facts. Float histograms use 2–65,536 saved bins. |
| Sigma Filter | CuPy | native-endian `uint8`, `uint16`, or finite `float32`; independent `YX` planes | Radius 0.5–10 and reviewed finite value/parameter facts. ROI/mask behavior is outside version 1. |
| Label Connected Components | CuPyX | Boolean mask; resolved 2D or 3D | Preserves exact deterministic `int32` label numbering. Numeric masks and oversized 2D/3D blocks use CPU. In non-CPU planning, a Boolean call not resolved as 2D or 3D is a typed preflight failure in this alpha. |
| Measure Objects | cuCIM | native-endian, non-negative `int32` labels; 2D or 3D | Basic measurement schema only. Extended shape, axis, boundary, moment, and derived-ratio groups remain CPU. |
| Measure Objects + Intensity | cuCIM | the same labels plus native-endian Boolean, `uint8`, `uint16`, or finite `float32` intensity | Matching shapes and the basic table schema are required; extended columns or unsupported intensity data use CPU. |

Canny and Otsu retain the CPU node's explicitly declared RGB/RGBA BT.601 luma
handling where the underlying dtype/profile is admitted. An ambiguous or
invalid channel axis remains on the CPU/error path rather than being guessed.

VIPP never inserts a cast to enter this table. If converting an image or PSF to
`float32` is scientifically appropriate, add an explicit `Convert Dtype` node,
review its scaling mode, inspect downstream thresholds/writers, and report it.
This can unlock much larger GPU gains for Gaussian and deconvolution workloads,
but it also changes the authored data representation. Never convert only to
make a benchmark look faster.

## Installation and platform boundary

The `gpu-cuda13` extra installs the pinned CuPy/CuPyX CUDA track. It does not
include the separately reviewed cuCIM build used by the background and basic
measurement candidates, so those nodes normally remain CPU after a standard
public GPU install.

Public admission in this alpha is deliberately narrower than installability:
the recorded gate is one native-Windows CPython 3.12, CUDA 13, RTX 5090 stack.
The Linux CUDA command is useful for qualification/development but the current
public policy still resolves Linux GPU candidates to CPU. CUDA has no macOS
path. CPU launch/basic processing, provider-neutral batch progress/cancellation,
and single-budget RAM presentation received a bounded M1 Max smoke, but Apple
Metal/MPS/MLX acceleration remains a future study.

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

For a forced Selective GPU choice, **visible** fallback turns a fallback-safe
availability or eligibility rejection into an amber CPU decision; **Strict**
returns a typed preflight failure. A rejection explicitly marked unsafe to
fall back fails under either setting. Auto and **Follow pipeline policy** use
ordinary explained CPU decisions for fallback-safe preflight rejections.

At runtime, **visible** fallback may retry one complete device segment once on
CPU after a classified OOM, but only after synchronization and proven GPU
cleanup. Its badge becomes amber and provenance keeps the failed attempt and
CPU retry. **Strict** returns the typed failure. Preflight CPU decisions are not
mislabeled as runtime OOM.

Cancellation is cooperative between nodes, resident segments, iterations,
tiles/planes, and publication stages. An opaque call can finish its current
atomic work before responding. A result is not accepted or published until
required synchronization and cleanup succeed.

## Keep interactive and durable execution aligned

Interactive calculation, saved batch runners, and generated Python/CLI use the
same execution service. Interactive **Save selected output…** and **Export OME
dataset…** serialize accepted cached values instead; they do not rerun the graph
or create exact compute-provenance sidecars. Preserve:

- the schema-4 workflow and complete compute request;
- for batch, the version-2 config, finalized manifest/archive, and item
  sidecars;
- for generated outputs, requested `.vipp-provenance.json` sidecars;
- the actual implementation IDs/versions and environment fingerprint; and
- CPU decisions, classified fallbacks/OOM, cancellation, and cleanup outcome.

Workflow schema 4, batch config schema 2, saved runners, and generated CLIs use
the stable value `prefer_gpu`. Saved per-node preferences remain present but
dormant outside Selective; switching back to Selective reactivates them.
`Benchmark node…` and **Find fastest pipeline…** are Selective-only. A CLI mode
override to `prefer_gpu` uses visible fallback when no fallback override is
given, while an explicit strict combination is rejected before calculation.
Every surface records the effective request and exact actual implementations in
the same execution provenance.

The saved batch runner is the production collection route. The generated
program's simple folder helper does not provide its pairing, collision plan,
source verification, checkpoints, or durable manifest.
