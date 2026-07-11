# Toolbar and settings

Labels below match napari-vipp 0.11.0a2. Controls can collapse into
**Settings** when the window is narrow.

## Workflow toolbar

| Control | Effect |
| --- | --- |
| **New workflow…** | Reset after confirmation to one unbound `Image Source` on an otherwise empty graph. |
| **Open example…** | Open one of 12 bundled templates with sample sources configured. |
| **Load workflow…** | Open an external or previously saved workflow JSON. |
| **Save workflow…** | Save graph structure, parameters, layout, and selected UI state—not computed arrays. |
| **Export Python…** | Generate a headless script using supported operation and I/O calls. |
| **Run batch…** | Preview and execute the current graph over local collections. |
| **Export OME dataset…** | Save one reference image with associated graph label outputs. |
| **Tunnels…** | Manage named graph outputs and subscribers. |
| **Auto structure graph** | Apply a one-shot source-to-sink layout; undo restores positions. |
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
| Run all in background | Dispatches all recomputes to background processing; when off, only known slower operations use it. |
| Cache mode | Keep all outputs, use Smart interactive cache, or use Low-memory mode. |
| Auto memory guard | Switches away from keep-all and prunes optional outputs if the configured cache share is exceeded. |
| Cache limit | Share of free-or-reclaimable memory used by the keep-all cache before the guard acts. |
| Keep output cached | Per-node request to retain an important result in Smart/Low-memory modes. |
| Auto Recalculate | Re-runs a selected manual node when upstream state changes; use cautiously for expensive work. |

**Cancel** prevents queued reruns and ignores the active result. It asks
cooperative work to stop, but cannot forcibly interrupt every NumPy, SciPy, or
scikit-image call already executing.

## Inspector surfaces

Depending on the selected node/output, the inspector can show parameters,
execution state, output metadata/history, output and input histograms, label
volume distribution, colocalization scatter, table preview, auto contrast,
**Pin selected**, and **Save selected output…**.
