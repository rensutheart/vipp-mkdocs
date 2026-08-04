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

The Batch workspace and any active run belong to the workflow tab that started
them. Other tabs remain editable while the background run proceeds, and all
progress/completion returns to the origin tab. VIPP blocks closing that origin,
starting a second batch, or exiting the application until execution finishes or
cooperative cancellation completes and final state is persisted.

## Recommended sequence

1. Build, tune, and validate the graph on defined development data.
2. Add explicit `Batch Output` nodes for every image, mask, label, RGB result,
   or table to save.
3. Open **Batch workspace...** and bind each varying `Image Source` to a local
   folder and pattern.
4. Choose the intended toolbar compute request. New work defaults to Auto,
   which remains CPU in ordinary 0.13.0a1 batch execution because no local
   timing evidence is attached. Choose CPU for an explicit portable reference
   or Selective for reviewed CPU/GPU per-node preferences.
5. Choose an output folder, formats, naming, existing-file policy, fallback
   policy, device, and accelerator-memory settings.
6. Optionally select **Preview batch** to review pairing and collision summaries.
7. When previewing, navigate several representatives, including difficult and
   boundary cases.
8. Save the workflow and choose **Yes** to attach the Batch workspace, or use
   **Save config...** when a separate headless-replay configuration is needed.
9. Select **Run batch**. It performs its own plan-only preflight and starts
   directly when no reviewed plan is current. If a displayed plan changed
   unexpectedly, review the refreshed plan and run again only after accepting it.
10. Inspect outputs, final status, validation text, manifest, archive, item
    sidecars, configured/effective compute requests, actual node
    implementations, fallbacks, and cleanup evidence before treating the run as
    complete.

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
not sufficient evidence. Time, channel, and Z remain inside each file; 0.13
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

Choose **Leave batch mode** when the tab should return to ordinary single-image
work. It discards the retained representative source overrides but does not
delete collection files, outputs, or saved configurations. The action is
unavailable during an active run.

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
- complete compute mode, per-node preferences, fallback policy,
  runtime/device selection, and accelerator memory limits;
- the required workflow companion and optional runner;
- the canonical scientific workflow hash.

Batch config schema 2 stores this compute request. A version-1 config had no
compute fields and loads as explicit CPU. Loading a config does not silently
replace the toolbar request; it retains its saved request until the user changes
a toolbar compute setting, at which point the current complete toolbar request
is used for the next preview, save, or run.

**Load config...** validates it against the current workflow. A hash or resolved
output mismatch fails rather than silently applying stale selections.

The optional `vipp_batch_pipeline.py` is a thin command-line launcher. It
defaults to its sibling config, resolves the recorded workflow, and delegates
to the same headless batch core as the workspace. It is different from
**Export Python...**, whose immutable embedded workflow and primary-source
folder helper serve a different automation use case.

The runner uses the config request by default. Its CLI can overlay explicitly
supplied `--compute-mode`, `--fallback-policy`, and repeatable
`--node-preference NODE_ID=PREFERENCE` options without mutating the saved
config. Use `--progress` to print both overall-item and current-operation
updates. Exit code `0` means no recorded failures, `1` means a finalized batch
contains failures, `2` means setup/execution failed before a normal result, and
`130` means cooperative cancellation.

Run the saved request with:

```text
python vipp_batch_pipeline.py --progress
```

Override only a deliberate difference from the saved config, for example:

```text
python vipp_batch_pipeline.py --progress --compute-mode selective --fallback-policy visible --node-preference gaussian_blur_1=library:cupyx --node-preference otsu_threshold_1=cpu
```

Node IDs come from the reviewed workflow/config. Stable preferences include
`auto`, `cpu`, `best_gpu`, `library:<library-id>`, and
`implementation:<implementation-id>`. Prefer a library choice for portability;
an exact implementation pin can be unavailable on another computer.

## Execution and publication safety

For each item, VIPP:

1. verifies and materializes every bound source revision;
2. runs the complete graph through the shared headless executor;
3. writes all outputs to private staging paths;
4. reverifies every source identity;
5. synchronizes and verifies accelerator cleanup when device work occurred;
6. promotes staged outputs to final paths one at a time;
7. updates provenance status and checkpoints.

If a source changes before publication, none of that item's outputs are
promoted. A failure during later promotion can leave earlier outputs from the
same item successfully published; the item is recorded as `partial` rather
than hidden. Successful earlier items remain available. With **Continue after
item failures** enabled, later items continue.

Batch displays two progress levels. **Overall** reports the item number, batch
ID, and final item status. **Current operation** reports the containing item,
node/operation, completed checkpoint, total checkpoints, and message. A
monolithic NumPy, SciPy, CuPy, cuCIM, or writer call can still remain at one
percentage until it returns because VIPP does not invent internal progress.

**Cancel** requests cooperative cancellation between nodes, device segments,
iterative/tiled checkpoints, output staging, source verification, and items.
The active operation may finish its current atomic library call first. On the
normal cancellation path, the active item and its unpublished outputs become
`cancelled`, later unstarted items become `skipped`, manifest/archive/checkpoint
evidence is finalized, and the runner exits `130`. Once the short multi-output
promotion boundary begins, VIPP completes it to avoid an avoidable partial set.

This provider-neutral progress/cancellation path received a bounded M1 Max CPU
smoke in addition to focused cancellation tests. See
[validation status](../reference/validation-status.md) for the exact evidence
boundary; it is not an Apple GPU claim.

With **visible** fallback, a complete transactional GPU segment can be retried
once on CPU only after a classified, retryable OOM and proven GPU cleanup.
**Strict** returns the typed memory failure. Other device errors are not silently
renamed or retried. Each later item is replanned independently.

## Provenance artifacts

A workspace-started run writes the resolved configuration beside its outputs.
Every workspace or headless run writes:

- `vipp_batch_manifest.json` — latest finalized run;
- a run-id manifest archive — preserves prior finalized runs;
- a run-id sidecar directory — per-item/output checkpoints during execution.

The version-2 manifest records:

- canonical workflow/config and their hashes;
- VIPP, Python, and relevant runtime package versions;
- each source identity and available metadata;
- every planned output path, format, and collision policy;
- errors and item/output states;
- the configured and effective compute requests, whether a CLI/UI override was
  used, and their fingerprints;
- for every calculated item, the formal execution document and digest with
  actual CPU/CuPy/cuCIM decisions, implementation IDs/versions, memory
  estimates, fallbacks, outcome, and cleanup; and
- an execution-provenance digest on every published output record that links it
  to that exact item execution.

Output states are `pending`, `completed`, `skipped`, `cancelled`, or `failed`.
Item states can also be `running` or `partial`. Final summaries count completed,
partial, skipped, cancelled, and failed items separately.

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
- The configured and effective compute requests match the intended run, and
  the version-2 manifest and item execution provenance explain the actual CPU,
  GPU, and fallback decisions. Interactive node badges describe the last
  accepted interactive calculation, not every detached batch item.
- Completed/partial/skipped/cancelled/failed counts match expectations.
- Manifests, archives, sidecars, environment, exclusions, QC, and validation
  evidence are retained with the outputs.
