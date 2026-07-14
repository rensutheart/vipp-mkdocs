# Process a folder

**Batch workspace...** configures and runs one validated workflow over paired
collections of local files. The interactive graph always represents one item;
preview and execution cover the complete deterministic plan.

!!! important "Representative is not the batch"

    Moving the representative slider swaps every collection-bound `Image
    Source` and calculates one item through the live graph. It does not save
    outputs or run the rest of the collection.

## Recommended sequence

1. Build, tune, and validate the graph on defined development data.
2. Add explicit `Batch Output` nodes for every image, mask, label, RGB result,
   or table to save.
3. Save the workflow.
4. Open **Batch workspace...** and bind each varying `Image Source` to a local
   folder and pattern.
5. Choose an output folder, formats, naming, and existing-file policy.
6. Select **Preview batch**. Review all pairing and collision summaries.
7. Navigate several representatives, including difficult and boundary cases.
8. Save `vipp_batch_config.json` when the plan is intended for replay.
9. Select **Run batch**. If the fresh preflight differs, review the refreshed
   plan and run again only after accepting it.
10. Inspect outputs, final status, validation text, manifest, archive, and item
    sidecars before treating the run as complete.

## Deterministic pairing

VIPP sorts matched paths independently for every bound source and pairs them by
position. Every bound source must match the same number of files.

```text
source A: a_01.npy  a_02.npy  a_03.npy
source B: b_01.npy  b_02.npy  b_03.npy
items:    (a_01,b_01) (a_02,b_02) (a_03,b_03)
```

Directory names and filename similarity do not create biological pairing.
Inspect the preview and retain an independent sample/field map when position is
not sufficient evidence. Time, channel, and Z remain inside each file; 0.12
does not iterate semantic-axis combinations or discover plate/well/field HCS
structure.

The first bound source is the primary source used by default naming. Fixed
file-path Image Sources can remain unbound; napari-layer and bundled-sample
sources must be replaced by collection bindings for a headless batch.

## Mark outputs explicitly

`Batch Output` passes data through during interactive execution and marks one
specific output for batch saving. It can define a tag, subfolder, filename
template, format override, and overwrite choice.

Use clear tags, for example:

```text
labels_cleaned
rl_tv_restored
object_measurements
colocalization_metrics
```

If a graph has no `Batch Output` nodes, VIPP offers a warned compatibility
fallback for terminal graph nodes. An image-like terminal uses the selected
batch image format and a table uses CSV. A terminal with multiple ports is
rejected because the intended port is ambiguous. Add explicit markers before
saving a reproducible configuration.

Enabled `Save Image` nodes are rejected in a batch workflow. Their recompute
side effects are not part of collision-checked batch publication.

## Names and collision policy

Default explicit-output naming is:

```text
{source_stem}__{tag}
```

Templates can use:

- `{batch_id}` and `{batch_index}`;
- `{source_name}` and `{source_stem}`;
- `{primary_source_stem}`;
- `{tag}`, `{node_id}`, and `{node_title}`.

VIPP appends the appropriate extension when the template has no known one.
Preview detects duplicate destinations, paths that already exist, overlap with
inputs, and collisions within the plan before graph execution.

Choose the batch default deliberately:

| Policy | Existing destination |
| --- | --- |
| `Error` | Treat it as a collision that must be resolved before execution. |
| `Skip` | Keep the file unchanged and record the output as skipped. |
| `Overwrite` | Replace the destination and record the new write. |

An explicit overwrite choice on a `Batch Output` node takes precedence over
the batch default.

## Review representatives

After preview, the retained strip above the graph shows `Item N of M`, the
batch ID, paired filenames, Previous/Next buttons, and a full-plan slider. The
table displays a limited row sample for large plans, but its selected-row
preview and the slider control the same complete representative session.

VIPP atomically replaces every collection-bound source path and calculates the
selected item with the ordinary verified source/execution path. Fixed sources
remain fixed. The transient pairing does not change serialized source
parameters or the scientific workflow hash.

The UI distinguishes a requested position from a successfully committed one.
It labels a new representative only after matching source loading and graph
calculation succeed. Rapid slider changes, failed inputs, stale workers, or a
changed graph therefore cannot falsely claim that the requested item is the
one displayed.

Representative arrays are cached within a bounded session. Their file
identities stay pinned so a file overwritten after review is rejected on
revisit or Run. Use **Refresh** to accept a new revision deliberately.

## Stale plans and fresh preflight

Changing batch settings or the scientific graph marks the runnable plan stale.
The previous representative pairing remains available and is labelled as
historical, but it is not authorization to run the old plan.

Run always performs a fresh preflight. If sources, files, destinations,
collision states, output declarations, or workflow hash differ from the plan
you reviewed, VIPP refreshes the workspace and stops for review. Select Run
again only after confirming the new plan.

## Save and replay a configuration

**Save config...** writes a versioned `vipp_batch_config.json` containing:

- source-node bindings, folders, and patterns;
- output folder and default image format;
- filename/output declarations and existing-file policy;
- continue-after-failure behavior;
- the required workflow companion and optional runner;
- the canonical scientific workflow hash.

**Load config...** validates it against the current workflow. A hash or resolved
output mismatch fails rather than silently applying stale selections.

The optional `vipp_batch_pipeline.py` is a thin command-line launcher. It
defaults to its sibling config, resolves the recorded workflow, and delegates
to the same headless batch core as the workspace. It is different from
**Export Python...**, whose immutable embedded workflow and primary-source
folder helper serve a different automation use case.

## Execution and publication safety

For each item, VIPP:

1. verifies and materializes every bound source revision;
2. runs the complete graph through the shared headless executor;
3. writes all outputs to private staging paths;
4. reverifies every source identity;
5. promotes staged outputs to final paths one at a time;
6. updates provenance status and checkpoints.

If a source changes before publication, none of that item's outputs are
promoted. A failure during later promotion can leave earlier outputs from the
same item successfully published; the item is recorded as `partial` rather
than hidden. Successful earlier items remain available. With **Continue after
item failures** enabled, later items continue.

Item progress is intentionally item-level. One expensive item can stay at
`running` for a long time while its graph invocation completes.

## Provenance artifacts

A workspace-started run writes the resolved configuration beside its outputs.
Every workspace or headless run writes:

- `vipp_batch_manifest.json` — latest finalized run;
- a run-id manifest archive — preserves prior finalized runs;
- a run-id sidecar directory — per-item/output checkpoints during execution.

The manifest records:

- canonical workflow/config and their hashes;
- VIPP, Python, and relevant runtime package versions;
- each source identity and available metadata;
- every planned output path, format, and collision policy;
- errors and item/output states.

Output states are `pending`, `completed`, `skipped`, or `failed`. Item states
can also be `running` or `partial`. Final summaries count completed, partial,
skipped, and failed items separately.

Sidecars reduce ambiguity after interruption, but there is a small window
between output promotion and checkpoint replacement. They are a recovery trail,
not a multi-file transaction log. Inspect files and sidecars before deciding
what to rerun.

## Deterministic batch demo

Choose **Open example... → Deterministic Batch & Provenance → Open batch
demo...**. Select a writable location; VIPP creates a unique working copy and
does not overwrite an earlier demo.

The bundle contains two NumPy source collections, a workflow, config, thin
runner, exact ground truth, and an empty results folder. The graph initially
shows the first of three paired 8 × 8 fields. Navigate all three pairs, then
select **Run demo batch**.

A successful run produces nine outputs—combined images, overlap labels, and
measurement tables—and validates exact decoded arrays/rows, source identities,
hashes, runtime versions, latest/archive manifests, and three finalized item
sidecars. This is an end-to-end regression fixture for its defined data; it is
not evidence that another assay or naming scheme is valid.

## Before accepting a run

- Pairing and item identifiers match an independent sample map.
- Every intended output has an explicit `Batch Output` marker.
- Representative navigation changes all paired sources together.
- Axes, channels, physical scale, origin, and units are appropriate.
- Output names, formats, subfolders, and collision policy are intentional.
- The fresh preflight matches the reviewed plan.
- Completed/partial/skipped/failed counts match expectations.
- Manifests, archives, sidecars, environment, exclusions, QC, and validation
  evidence are retained with the outputs.
