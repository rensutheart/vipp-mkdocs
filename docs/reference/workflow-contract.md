# Workflow and export contract

Use this page when deciding whether an artifact is sufficient to reproduce or
review an analysis.

## Workflow JSON

A saved workflow represents the editable graph. It can include:

- node operation IDs, titles, parameters, and canvas positions;
- connections and output-port hints;
- named tunnels and graph notes;
- selected workflow/UI state such as thumbnail visibility and per-node/output
  display profiles where enabled.

It does **not** embed calculated pixel arrays or tables. It also does not, by
itself, freeze the Python environment, preserve every external source, prove
metadata correctness, or capture the rationale for every choice.

Workflow tabs are independent live sessions, not one multi-workflow file.
**Save workflow…** serializes the active tab only. Other open tabs, their
caches, undo/redo histories, transient viewport, and in-flight state are not
bundled into that JSON.

### Current schema: version 4

A current file identifies itself with:

```json
{
  "type": "napari-vipp-workflow",
  "version": 4
}
```

VIPP 0.13.0a1 accepts schema versions 3 and 4 and rejects versions 1 and 2 with
an explicit error. Schema 4 adds portable authored compute intent under
`execution.compute`, including `cpu`, `auto`, `prefer_gpu`, or `custom` mode
and per-node preferences. It does not store a claim that the same backend will
be available or fastest on another computer.

A schema-3 workflow has no compute contract. It therefore loads with an
explicit **CPU** request, never the new-session Auto default. Saving the reviewed
workflow emits schema 4. This one conservative migration does not relax the
scientific reasons that schemas 1 and 2 remain rejected.

Retain an older workflow unchanged for provenance and use the VIPP environment
that created it when it must be inspected or run. Rebuild the graph in 0.13
from the old graph and methods notes, then compare nodes, connections, dynamic
ports, parameters, sources, metadata, and results on known data. Do not change
the JSON version number by hand.

A schema-3 workflow saved by 0.12 can therefore be reconstructed in 0.13 with
its graph, parameters, connections, and persisted workflow state plus a known
CPU request. This does not mean prior calculated results were embedded or
revalidated. Scientific pixel/table caches, thumbnails, pinned layers, and
runtime execution reports are not serialized in workflow JSON. Recalculate and
validate the graph after upgrading.

Schema-4 per-node preferences are keyed by workflow node ID and validated
before execution. They express an authored preference such as CPU or a GPU
library, not a hidden cast or a stored benchmark result. The execution report,
rather than workflow intent, is the record of the runtime, implementation,
fallback, and environment that actually produced a result.

Legacy development builds may display **Selective** or serialize `selective`
for the policy now named **Custom**. Current builds accept that spelling for
compatibility and write `custom`; the policy behavior is unchanged.

Per-node preferences are active only in Custom. CPU, Auto, and Prefer GPU
preserve them as dormant authored intent so switching modes is lossless. Prefer
GPU considers all reviewed public GPU candidates regardless of CPU speed, but
retains scientific, dtype, parameter, dependency, environment, and memory
admission. It requires visible fallback; an unsupported node receives an
explained ordinary CPU decision.

Alpha compatibility is not guaranteed across future schema or operation
changes. Preserve the original file and exact VIPP version, and test a duplicate
before using it in a consequential analysis.

### Optional Batch workspace attachment

A 0.13.0a1 workflow can carry an optional top-level `batch_config`. The
version-2 attachment contains source bindings, local input/output paths,
patterns, formats, output policy, run settings, and a complete compute request,
including runtime/device and accelerator-memory settings. It contains no source
pixels, calculated arrays, output files, manifests, or item sidecars.

A version-1 batch config had no compute request and loads as explicit CPU. It
saves as version 2 only after validation. VIPP never guesses that an older
collection run intended to use an accelerator.

The attachment is validated against the containing graph when it is saved and
loaded. It is deliberately excluded from the scientific workflow hash: changing
where or how a graph is applied must not create a self-referential hash or imply
that the graph's scientific operations changed. An invalid, unsupported, or
mismatched attachment is not silently applied; VIPP can still load the
scientific graph while reporting that Batch workspace was not restored.

Restoring a valid attachment opens Batch workspace and populates its fields. It
does not scan the collection, build a preview, load a representative, or
calculate the graph. **Preview batch** remains optional and **Run batch** always
performs a fresh preflight. Because paths are local configuration, review and
repair them after moving a workflow to another computer.

### Scientific parameters versus inspector state

The workflow saves parameters that can change calculations, including:

- floating-point histogram bins for Otsu, Triangle, Yen, Isodata, and Minimum;
- the threshold scope (`Stack histogram` or `Slice histogram`);
- Minimum's maximum smoothing iterations;
- `Rescale Intensity` cutoff mode plus its percentile or explicit-value fields;
- `Clip` cutoff mode and explicit values;
- `Linear Scale + Offset` values written by Auto Contrast;
- required channel-axis choices for channel-sensitive operations;
- Composite-to-RGB `channel_axis_mode`, `mapping_mode`, ordered per-source
  `channel_colors`, and native-versus-normalized intensity mapping.

Compact histogram chart bins, napari layer contrast limits, provisional display
ranges, and inspector layout do not alter node arrays. They are not substitutes
for the saved scientific parameters. A screenshot can document what was
reviewed, but the workflow JSON is the authoritative editable graph.

In 0.13, compatible VIPP Inspect display profiles are saved independently by
node, output port, and RGB surface. They can include colormap, contrast,
blending, opacity, visibility, gamma, interpolation, and compatible
projection/rendering settings, but remain presentation state: restoring or
resetting one cannot change a cached array, threshold, mask, label image, or
table. Physical layer scale continues to come from image metadata, and
arbitrary napari transforms are not included. The napari camera/dimension view
is also preserved while the same output recalculates in a live session; do not
confuse that view-continuity feature with scientific workflow provenance.

## Generated Python

Python export embeds immutable validated workflow JSON and reconstructs a fresh
pipeline for each call through the same headless executor as VIPP. It preserves
supported `ImageState` through source and save paths and accepts explicit
bindings for every source. Missing, duplicate, and unknown bindings fail.

An export records the exact VIPP version that generated it and refuses a
different runtime. Regenerate and revalidate exported code after every VIPP
upgrade, including 0.12.0a3 to 0.13.0a1. Interactive caches, thumbnails, pinned
layers, and graph layout remain UI state and are not reproduced.

In 0.13, the callable API accepts a complete `compute_request`, a progress
callback, and a cooperative cancellation token. The generated CLI overlays
only explicitly supplied `--compute-mode`, `--fallback-policy`, and repeatable
`--node-preference` values; omitted fields retain the embedded schema-4 request.
It also supports `--progress` and provenance controls. A runtime override does
not mutate the embedded workflow.

The serialized and CLI value for Prefer GPU is `prefer_gpu`. Changing only the
CLI mode to that value defaults the effective fallback to `visible`; explicitly
combining it with `strict` fails request validation. Interactive, batch, and
generated execution use the same selection and provenance contract.

`PipelineResults` exposes the effective compute request, the formal execution
report, per-node compute provenance, and output-bound provenance. A successful
`save_image()` writes an atomic `.vipp-provenance.json` sibling when the caller
supplies the provenance document. The generated CLI enables provenance by
default and exposes `--provenance` / `--no-provenance`. The document identifies
the output node/port and actual implementation, not merely the requested mode.

The generated CLI stages every requested output and sidecar in one private
same-directory publication set, rejects duplicate destinations, verifies
execution cleanup, and commits the set together with rollback for caught commit
failures. Requested provenance sidecars are promoted before their outputs, so
an abrupt process crash can leave an orphan sidecar but not a newly published
output lacking its requested provenance. Failure sidecars distinguish execution
from publication failure. Normal exit is `0`, setup/execution/publication
failure is `2`, and cooperative cancellation is `130`.

Generated CLI progress is operation-level. The saved batch runner additionally
has an overall-item stream because it owns a collection plan. Generated inputs
carry supplied `ImageDataset`/`SourcePayload` identity and metadata; exact
source-byte reverification before publication is a durable saved-batch
guarantee, not a promise for every arbitrary generated-Python array caller.

## Batch artifacts

A batch run uses either a standalone version-2 `vipp_batch_config.json` or the
equivalent validated configuration attached to a workflow. It records
collection bindings, output policy, resolved output declarations, the workflow
companion, canonical workflow hash, and configured compute request. Preview and
execution share one deterministic sorted positional pairing and output planner.
Run always performs a fresh plan-only preflight. A new or deliberately edited
plan can start in the same click without calculating a representative; an
unexpectedly changed plan that was already reviewed stops for confirmation.

The effective request follows explicit precedence: a new Batch workspace
captures the current toolbar request; a loaded config retains its own request;
changing a toolbar compute setting after load replaces that request for the
next preview/save/run; and CLI arguments overlay only fields actually supplied.
Unknown node IDs or malformed preferences fail before output artifacts are
produced.

Each run writes a latest version-2 manifest, a run-id archive, and item
sidecars recording software versions, source identities/metadata, hashes,
planned outputs, policies, errors, and status. The manifest also records the
configured/effective requests, whether a run override was used, request/config
fingerprints, and an execution document plus digest for every calculated item.
Each published output links to that exact item execution. Output promotion is
atomic per file after all sources and accelerator cleanup for an item are
verified. These artifacts improve auditability but do not form one transaction
across every output and sidecar; inspect the recovery trail after an
interruption.

An item whose resolved `Skip` destinations all exist is finalized without
loading source pixels or calculating the graph. Atomic artifact replacement
retries short-lived access failures. If a final item sidecar still cannot be
written, that item is partial and **Continue after item failures** controls
whether later items run; final run-manifest persistence remains mandatory.

See [process a folder](../workflows/batch-processing.md) for the complete user
contract.

## Fallback, progress, and cancellation

Every execution report records the requested policy and actual decision for
each completed computed node, including pruned intermediates. The record
includes runtime, array domain, implementation library/ID/version, parity and
cache-equivalence policy, preference, decision reason, benchmark digest, memory
estimate, environment fingerprint, classified fallbacks, outcome, and cleanup
evidence. A custom implementation whose versioned identity is incomplete is
recorded honestly as incomplete rather than presented as exact reproduction.

**Visible** fallback permits one CPU retry of a complete transactional device
segment only after a classified, retryable runtime OOM. VIPP synchronizes and
cleans the GPU attempt first. **Strict** returns the typed memory failure;
unrelated device defects are not renamed as OOM or silently retried. Eligibility
or availability decisions made before device work remain visible in node
decisions and fallback summaries.

Batch exposes overall-item and current-operation progress. The saved runner
prints both with `--progress`; generated workflow CLI prints operation-level
progress. Cancellation is cooperative between nodes, device segments,
iterative/tiled checkpoints, staging, verification, and items. A monolithic
library call or writer can delay the next update because VIPP does not invent
internal progress. On normal cancellation the active item is recorded as
cancelled, later unstarted items as skipped, provenance is finalized, and CLI
returns `130`.

## Metadata boundary

VIPP carries an `ImageState` with supported axes, scale, units, source/channel
fields, and operation history where available. Individual operations transform
or preserve compatible fields. Readers, generic arrays, third-party formats,
or generated Python can have less information.

Never infer “metadata preserving” to mean bit-for-bit round-trip fidelity of
all acquisition metadata. Verify the fields your analysis needs.

## Stable-source and grid boundary

Workflow JSON records source parameters but does not embed source bytes. During
one interactive source revision, VIPP pins an owned read-only snapshot and
rejects a file/store or live-layer revision that changes during work. **Refresh**
is the explicit boundary for accepting a new revision.

For multi-input operations, matching array shape is insufficient. VIPP also
checks semantic axes, sample counts, scale, compatible units, and origin. It
does not silently resample, register, reorder, or reinterpret inputs. Archive
source identities and calibration evidence with the workflow.
