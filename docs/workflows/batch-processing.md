# Process a folder

The sole **Batch workspace...** button in the main toolbar configures and runs
one validated workflow over paired collections of local files. It is visually
separated between **Load workflow...** and the export actions because it opens
a retained working setup rather than exporting an artifact. The interactive
graph always represents one item; preview and execution cover the complete
deterministic plan.

!!! important "Representative is not the batch"

    Moving the representative slider swaps every collection-bound `Image
    Source` and calculates one item through the live graph. It does not save
    outputs or run the rest of the collection.

## Recommended sequence

1. Build, tune, and validate the graph on defined development data.
2. Add explicit `Batch Output` nodes for every image, mask, label, RGB result,
   or table to save.
3. Open **Batch workspace...** and bind each varying `Image Source` to a local
   folder and pattern.
4. Choose an output folder, formats, naming, and existing-file policy.
5. Optionally select **Preview batch** to review pairing and collision summaries.
6. When previewing, navigate several representatives, including difficult and
   boundary cases.
7. Save the workflow and choose **Yes** to attach the Batch workspace, or use
   **Save config...** when a separate headless-replay configuration is needed.
8. Select **Run batch**. It performs its own plan-only preflight and starts
   directly when no reviewed plan is current. If a displayed plan changed
   unexpectedly, review the refreshed plan and run again only after accepting it.
9. Inspect outputs, final status, validation text, manifest, archive, and item
    sidecars before treating the run as complete.

After the first source folder is bound, VIPP suggests its `output` subdirectory
as the destination. Amber means that this is an unconfirmed suggestion, not an
invalid path. Review it before running or previewing the batch. Focusing,
clicking, editing, or choosing the output folder confirms it and restores the
normal text colour; later source-folder changes then leave it unchanged. For
multiple sources, the suggestion follows the first bound (primary) source.

!!! caution "Recursive input patterns"

    If a pattern searches subdirectories, such as `**/*.tif`, choose an output
    folder outside the input tree. Otherwise, files from an earlier run could
    match the next input search.

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

When every resolved output for an item already exists under `Skip`, VIPP records
that no-op without loading the source pixels or calculating the graph. If an
item has a mixture of existing and missing outputs, it still calculates once so
the missing outputs can be produced correctly.

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
again only after confirming the new plan. When there is no current reviewed
plan - for example, immediately after loading a config or deliberately editing
a setting - the same Run click uses the fresh plan and starts execution. It does
not calculate a graph representative first; **Preview batch** remains optional.

## Save and replay a configuration

When Batch workspace is active, **Save workflow...** offers three choices:

- **Yes** attaches the current versioned batch configuration to the workflow
  JSON. It records collection bindings, local input/output paths, patterns,
  formats, and run policies, but no source pixels, calculated results, or batch
  outputs.
- **No** saves an ordinary graph-only workflow.
- **Cancel** does not save a file.

Loading a workflow with a valid attachment restores and opens Batch workspace
with its fields populated. VIPP does not preview the plan, read a
representative, or calculate the graph as part of that batch restore. Use
optional **Preview batch** for inspection, or choose **Run batch** to perform a
fresh preflight and start the full run. An invalid or mismatched attachment is
not silently applied; the scientific workflow can still load while VIPP
reports that the Batch workspace was not restored.

For command-line replay or when workflow and automation settings should remain
separate, use **Save config...**. It writes a standalone versioned
`vipp_batch_config.json` containing:

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

VIPP retries transient Windows and cloud-sync locks during atomic replacement.
If a final per-item sidecar still cannot be written, the authoritative run
manifest records that item as partial; **Continue after item failures** controls
whether later items run. Failure to finalize the run manifest itself remains a
run-level error because VIPP must not report success without durable provenance.

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
