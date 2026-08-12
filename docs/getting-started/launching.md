# Launch VIPP

## Use the installed shortcut on Windows

The Windows installer creates launchers for the managed installation:

- a CPU installation provides **VIPP**;
- a CUDA installation provides **VIPP Automatic**, **VIPP CPU**, and
  **VIPP Prefer GPU**.

Begin with **VIPP Automatic** after a CUDA installation. Startup shows the VIPP
brand, real progress milestones, elapsed time, and retained diagnostics. A
Prefer-GPU session requests every scientifically and operationally eligible GPU
implementation, but operations outside the reviewed region still use CPU with
an explanation.

## Open the napari widget

Activate the environment used for installation and run:

```text
napari
```

In napari, choose:

```text
Plugins → VIPP Workflow (napari-vipp)
```

The VIPP dock widget has a workflow tab bar and three main work regions:

| Region | What it is for |
| --- | --- |
| Workflow tabs | Keep several independent graphs, results, caches, histories, inspectors, paths, and Batch workspaces open. Switching tabs restores state without scientific recalculation. |
| Node library | Search or browse operations, then add them to the graph. |
| Graph canvas | Connect and arrange the visible analysis. |
| Inspector | Edit the selected node, calculate manual nodes, and inspect output metadata, images, histograms, or tables. |

The top toolbar opens examples and workflows, saves or exports the graph,
starts batch processing, and exposes display/execution settings. Its
**CPU / Auto / Prefer GPU / Custom** control is the authored compute request; new sessions
default to Auto. After calculation, the toolbar summary and compact node badges
show what actually ran. Auto uses exact compatible complete-pipeline timing
history when both CPU and accelerated observations exist; without history it
uses reviewed safe GPU defaults. Accelerated-only history makes the next global
Auto run measure CPU once on the same execution surface. Auto never silently
benchmarks multiple implementations.
Use **Prefer GPU** when every reviewed eligible accelerator
should run regardless of speed. Use a reviewed Custom
choice or apply a **Find fastest** proposal for per-node control and measurement.

VIPP's severity-aware message strip reports graph, workflow, and compute
feedback. Napari's own bottom status bar reports viewer coordinates and layer
information; the two surfaces have different owners and purposes.

## Open a bundled example

Choose **Open example…** in the VIPP toolbar. The chooser opens a new workflow
tab, groups complete graph templates by task, and configures their `Image
Source` nodes to use matching bundled samples.

For a first visit choose:

```text
Segmentation & Labels → Red-Channel Label Cleanup
```

This route does not require an external file or a layer opened through napari's
sample menu.

## Give the graph enough space

For a long workflow, drag the **VIPP Workflow** dock title bar out of napari (or
double-click the title bar) and maximize the floating window. Hide the node
library after adding nodes and keep the inspector visible while tuning. Use
graph zoom for overview; use napari layers for full-resolution image comparison.

## If VIPP is missing from the Plugins menu

Check that napari is running from the same environment into which VIPP was
installed:

```text
python -c "import sys; print(sys.executable)"
python -c "import napari_vipp; print(napari_vipp.__file__)"
```

If either command uses a different environment, close napari, activate the
correct environment, and launch it again. See [report a problem](../troubleshooting/report-a-problem.md)
if the plugin is installed but still not discovered.

## Maintainer launch scripts

Repository scripts such as `scripts/launch_vipp_sample.py` and
`scripts/launch_vipp_intensity_workflow.py --list` are for development,
screenshots, and repeatable review. End users should normally use
**Open example…** or **Load workflow…** inside VIPP.
