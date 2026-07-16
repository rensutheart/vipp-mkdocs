# Toolbar and settings

Labels below match napari-vipp 0.12.0a1. Controls can collapse into
**Settings** when the window is narrow.

## Workflow toolbar

| Control | Effect |
| --- | --- |
| **New workflow…** | Reset after confirmation to one unbound `Image Source` on an otherwise empty graph. |
| **Open example…** | Open one of 13 bundled templates; ordinary examples configure sample sources, while the batch example creates a safe working copy on request. |
| **Load workflow…** | Open an external or previously saved workflow JSON. |
| **Save workflow…** | Save graph structure, parameters, layout, and selected UI state—not computed arrays. |
| **Export Python…** | Generate a headless script using supported operation and I/O calls. |
| **Batch workspace…** | Open the retained local-collection setup, representative navigator, run progress, final status, and provenance view. |
| **Export OME dataset…** | Save one reference image with associated graph label outputs. |
| **Tunnels…** | Manage named graph outputs and subscribers. |
| **Auto structure graph** | Apply a one-shot source-to-sink layout; undo restores positions. |
| **Focus** | Recover the graph center without changing zoom, selection, layout, cache state, or undo history. |
| **Refresh** | Re-evaluate ordinary automatic graph state. |
| **Calculate all** | Calculate manual nodes that are not current. |
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
| Graph zoom | Scales graph cards; reset returns to 100%. |

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

## Inspector surfaces

Depending on the selected node/output, the inspector can show parameters,
execution state, output metadata/history, output and input histograms, label
volume distribution, colocalization scatter, table preview, auto contrast,
**Pin selected**, and **Save selected output…**.

### Manual execution colors

Manual/cached execution barriers apply to every VIPP operation that uses the
manual policy, including measurements, graph analysis, colocalization, and
deconvolution.

| Graph color | Meaning | Action |
| --- | --- | --- |
| Bright amber | This is the first manual node stopping the branch. It has never been calculated, or its cached result is stale. | Select this node and choose **Calculate** or **Recalculate**, or use **Calculate all**. |
| Dark amber | This downstream result is also stale, but it is waiting for the bright-amber upstream barrier. VIPP retains the last coherent cached branch and does not recalculate this node yet. | Resolve the bright-amber node first; this node will then run or become the next actionable barrier. |

The toolbar **Calculate all** button also turns bright amber while an
uncalculated or stale manual frontier needs attention. It returns to the normal
toolbar style when no such action remains. A node already configured for
**Auto Recalculate** does not trigger this user-action prompt while VIPP is
handling it automatically.

This distinction also applies during background execution. A dark-amber node
does not show a processing spinner until it is actually runnable. Once that
node finishes updating, it returns to its normal current color immediately
while later nodes continue calculating; it does not remain dark amber until the
whole branch finishes. Selecting or pinning that node uses the same newly
completed run-scoped result shown by its card when the active cache policy
retains that node. Low-memory pruning remains in force for other intermediates,
which follow the normal cache-restore behavior when selected. VIPP still
commits the scientific workflow cache only after accepting the complete
background run.

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
and the graph calculation succeeds. See [process a folder](../workflows/batch-processing.md).
