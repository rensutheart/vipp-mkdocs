# Workflow and export contract

Use this page when deciding whether an artifact is sufficient to reproduce or
review an analysis.

## Workflow JSON

A saved workflow represents the editable graph. It can include:

- node operation IDs, titles, parameters, and canvas positions;
- connections and output-port hints;
- named tunnels and graph notes;
- selected workflow/UI state such as thumbnail visibility where enabled.

It does **not** embed calculated pixel arrays or tables. It also does not, by
itself, freeze the Python environment, preserve every external source, prove
metadata correctness, or capture the rationale for every choice.

### Current schema: version 3

A current file identifies itself with:

```json
{
  "type": "napari-vipp-workflow",
  "version": 3
}
```

VIPP 0.12.0a1 accepts schema version 3 and rejects versions 1 and 2 with an
explicit error. There is no automatic migration path. This prevents an old file
from being silently reinterpreted with invented threshold, cutoff, channel-axis,
color, or intensity-mapping choices.

Retain an older workflow unchanged for provenance and use the VIPP environment
that created it when it must be inspected or run. Rebuild the graph in 0.12
from the old graph and methods notes, then compare nodes, connections, dynamic
ports, parameters, sources, metadata, and results on known data. Do not change
the JSON version number by hand.

Alpha compatibility is not guaranteed across future schema or operation
changes. Preserve the original file and exact VIPP version, and test a duplicate
before using it in a consequential analysis.

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

## Generated Python

Python export embeds immutable validated workflow JSON and reconstructs a fresh
pipeline for each call through the same headless executor as VIPP. It preserves
supported `ImageState` through source and save paths and accepts explicit
bindings for every source. Missing, duplicate, and unknown bindings fail.

An export records the exact VIPP version that generated it and refuses a
different runtime. Regenerate and revalidate exported code after an upgrade.
Interactive caches, thumbnails, pinned layers, and graph layout remain UI
state and are not reproduced.

## Batch artifacts

A batch run uses a versioned `vipp_batch_config.json` that records collection
bindings, output policy, resolved output declarations, the workflow companion,
and the canonical workflow hash. Preview and execution share one deterministic
sorted positional pairing and output planner. A fresh preflight must still match
the reviewed plan before execution.

Each run writes a latest manifest, a run-id archive, and item sidecars recording
software versions, source identities/metadata, hashes, planned outputs,
policies, errors, and status. Output promotion is atomic per file after all
sources for an item are reverified. These artifacts improve auditability but do
not form one transaction across every output and sidecar; inspect the recovery
trail after an interruption.

See [process a folder](../workflows/batch-processing.md) for the complete user
contract.

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
