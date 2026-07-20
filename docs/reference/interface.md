# Toolbar and settings

Labels below match napari-vipp 0.12.0a3. Controls can collapse into
**Settings** when the window is narrow.

## Workflow toolbar

| Control | Effect |
| --- | --- |
| **New workflow…** | Reset after confirmation to one unbound `Image Source` on an otherwise empty graph. |
| **Open example…** | Open one of 13 bundled templates; ordinary examples configure sample sources, while the batch example creates a safe working copy on request. |
| **Load workflow…** | Open an external or previously saved workflow JSON. A valid attached batch configuration restores and opens Batch workspace without running a preview. |
| **Save workflow…** | Save graph structure, parameters, layout, and selected UI state—not computed arrays. When a Batch workspace is active, choose whether to attach its versioned configuration to the same workflow JSON. |
| **Batch workspace…** | Open or return to the retained local-collection setup, optional representative preview, run progress, final status, and provenance view. This is the sole Batch workspace entry and is visually separated between workflow loading and the export actions. |
| **Export Python…** | Generate a headless script using supported operation and I/O calls. |
| **Export OME dataset…** | Save one reference image with associated graph label outputs. |
| **Tunnels…** | Manage named graph outputs and subscribers. |
| **Auto structure graph** | Apply a one-shot source-to-sink layout; undo restores positions. |
| **Focus** | Recover the graph center without changing zoom, selection, layout, cache state, or undo history. |
| **Refresh** | Re-evaluate ordinary automatic graph state. |
| **Calculate all** | Calculate manual nodes that are not current. During isolated tuning, first apply the tuned result and release the temporary downstream boundary. |
| **Undo / Redo** | Reverse or restore supported workflow edits. |

## Display settings

| Setting | Choices / meaning |
| --- | --- |
| Preview mode | `Slice`, `MIP`, or `Off` for graph/inspector previews. |
| Thumbnail contrast | Controls thumbnail contrast behavior; it does not alter processed data. |
| Contrast range | Controls how contrast scope is estimated. |
| Monochrome colormap | Changes display of monochrome previews only. |
| Link napari/VIPP sliders | Synchronizes napari dimensions and VIPP preview sliders. |
| Save thumbnail visibility in workflows | Includes per-node thumbnail visibility in workflow UI state. |
| Port labels | `Ambiguous only` (default) labels multi-input or multi-output nodes, `Show all` labels every port, and `Hide all` removes persistent labels. |
| Graph zoom | Scales graph cards; reset returns to 100%. |

Long port names are shortened on the card and retain their full text in a
tooltip. Changing the label mode can make an already tightly packed layout
overlap; VIPP reports the number of overlapping card pairs in the status bar.
Use **Auto structure graph** to make label-aware space, or move the affected
cards manually. Label visibility is a graph-display choice and never changes
connections or processed data.

## Execution and memory settings

| Setting | Meaning |
| --- | --- |
| Run all in BG | Checked: dispatch every graph recompute to background processing. Unchecked: use adaptive execution, keeping small ordinary work immediate while backgrounding known expensive operations and large inputs. |
| Cache mode | Keep all outputs, use Smart interactive cache, or use Low-memory mode. |
| Auto memory guard | Switches away from keep-all and prunes optional outputs if the configured cache share is exceeded. |
| Cache limit | Share of free-or-reclaimable memory used by the keep-all cache before the guard acts. |
| Keep output cached | Per-node request to retain an important result in Smart/Low-memory modes. |
| Auto Recalculate | Re-runs a selected manual node when upstream state changes; use cautiously for expensive work. |

**Cancel** prevents queued reruns and ignores the active result. It asks
cooperative work to stop, but cannot forcibly interrupt every NumPy, SciPy, or
scikit-image call already executing.

The current adaptive large-input boundary is 4,000,000 elements or 32 MiB,
whichever is reached first. This applies even when **Run all in BG** is
unchecked. Exact threshold diagnostics, Auto Contrast, colocalization density,
and generated-layer contrast calculations also leave the user-interface thread
when their inputs are large.

Background execution changes *where* work runs, not the method or the values it
uses. Exact operations still inspect the complete required population. They may
consume CPU time and memory while napari remains responsive.

### Tune one node in isolation

**Tune node in isolation** is available in the selected-node inspector and the
node context menu. The selected node must have a coherent cached result, and no
dirty edit, pipeline calculation, source load, or batch run can be pending or
in flight. Downstream nodes do not all need to have outputs.

While the session is active, parameter edits recalculate the selected node but
pause propagation beyond it. The tuned node is the bright-amber actionable
frontier. Its downstream closure is darker amber and labelled as waiting; those
cards keep their last coherent results when they have them and otherwise remain
unavailable. Neither case may be interpreted as a result of the new parameter
values.

- **Apply and continue** keeps the latest parameters and local result, releases
  the boundary, and resumes calculation from the node's direct descendants.
- **Cancel tuning** restores the parameters, output, and execution state that
  were current when the session began without recalculating the held branch.
- **Calculate all** applies the current tuning result before performing its
  ordinary automatic and manual-node scheduling.

Only one node can be isolated at a time. A graph, layout, note, workflow-load,
undo/redo, or other history-backed edit first commits the current tuning result,
so cancellation cannot cross graph revisions. The isolation boundary and its
restoration snapshot are transient session state; they are not written to
workflow JSON.

## Inspector surfaces

Depending on the selected node/output, the inspector can show parameters,
execution state, output metadata/history, output and input histograms, label
volume distribution, colocalization scatter, table preview, auto contrast,
**Pin selected**, and **Save selected output…**.

### Numeric parameter entry

Numeric spinners accept direct keyboard entry as well as their step buttons and
paired sliders. Floating-point fields accept decimal points or commas and
scientific notation such as `2e-4`; sufficiently small non-zero values are also
displayed in scientific notation. A slider is an exploration window, not
necessarily the full valid entry range. Right-click a numeric field and choose
**Reset to default** to restore that operation's declared default.

### Manual execution colors

Manual/cached execution barriers apply to every VIPP operation that uses the
manual policy, including measurements, graph analysis, colocalization, and
deconvolution.

| Graph color | Meaning | Action |
| --- | --- | --- |
| Bright amber | This is the first manual node stopping the branch. It has never been calculated, or its cached result is stale. | Select this node and choose **Calculate** or **Recalculate**, or use **Calculate all**. |
| Dark amber | This downstream node is also stale, but it is waiting for the bright-amber upstream barrier. VIPP retains its last coherent cached result when one exists; otherwise it remains unavailable. | Resolve the bright-amber node first; this node will then run or become the next actionable barrier. |

![Two bright-amber deconvolution frontiers, darker-amber waiting descendants, and the amber Calculate all control](../assets/screenshots/workflows/manual-execution-frontier.png)

*The two deconvolution branches are actionable. Rescale Intensity and Otsu
Threshold wait behind the selected RL-TV branch and are not the source of the
problem.*

The toolbar **Calculate all** button also turns bright amber while an
uncalculated or stale manual frontier needs attention. It returns to the normal
toolbar style when no such action remains. A node already configured for
**Auto Recalculate** does not trigger this user-action prompt while VIPP is
handling it automatically.

This distinction also applies during background execution. A dark-amber node
does not show a processing spinner until it is actually runnable. Once that
node finishes updating, it returns to its normal current color immediately
while later nodes continue calculating; it does not remain dark amber until the
whole branch finishes. Every completed card receives a run-scoped execution
state and sampled thumbnail. Selecting, pinning, or inspecting tables and
metadata uses the same newly completed run-scoped payload when the active cache
policy already retains that node. Low-memory pruning remains in force for other
intermediates, which follow the normal cache-restore behavior when selected.
VIPP still commits the scientific workflow cache only after accepting the
complete background run. Cancelling, superseding, or editing during a run
discards these temporary presentation updates and restores the last coherent
cache view.

### Generated napari layers

When two inspected results have compatible napari `Image` presentation, VIPP
reuses the existing layer object and replaces only its data reference. The new
reference exposes the exact underlying pixels as a non-writeable view; VIPP
also resets colormap, blending, contrast, scale, and related display metadata
so settings from the previous node cannot leak into the next view. This makes
switching between compatible image-sized nodes largely independent of volume
size.

VIPP replaces the layer for a genuine presentation-class change, such as
`Image` to `Labels`, or for an incompatible RGB layout. A Boolean mask pinned
as a napari `Labels` overlay requires a uint8 presentation copy. That conversion
is limited to the class-changing display path and is not written back to the
node output: the scientific cache, saved output, and downstream calculations
retain the original exact array.

## Auto Contrast Versus Display Contrast

**Auto Contrast** appears for `Linear Scale + Offset`. It calculates exact
full-input finite percentiles from the chosen saturation setting and writes the
resulting `alpha` and `beta` into the node. It therefore changes workflow data.

The contrast limits on inspect and pinned napari layers are display-only. Large
layers can briefly use an explicit provisional dtype range while VIPP obtains
the exact full finite range in the background. A manual napari contrast edit
made during that calculation is preserved. Neither the provisional nor final
layer contrast changes downstream arrays, masks, thresholds, or measurements.

The histogram panel is also a display summary. It counts every finite value,
but its chart bins are independent of a floating-point automatic-threshold
node's saved **Float histogram bins** parameter.

## Draggable histogram guides

Input-histogram markers for Binary Threshold, Hysteresis Threshold, explicit
Rescale Intensity/Clip cutoffs, and supported colocalization thresholds are
editable by dragging. A pointer click without movement does not change the
parameter.

Rescale Intensity has two draggable guides. Moving a percentile-derived guide
switches the node to **Explicit values**, preserves the other exact cutoff, and
queues interactive recalculation. This is a scientific parameter edit: save
the workflow after accepting it. VIPP reuses unchanged input counts while a
manual marker moves and refreshes the output histogram after the output changes.

## Batch representative strip

After a successful batch preview, a persistent strip above the graph exposes
Previous/Next, a full-plan slider, item position, batch ID, and every paired
filename. It calculates one representative only and never saves batch outputs.
The requested item is labelled as current only after all matching sources load
and the graph calculation succeeds. The strip does not duplicate the main
**Batch workspace…** action; use the sole toolbar button to reopen the retained
workspace. See [process a folder](../workflows/batch-processing.md).
