# Launch VIPP

## Open the napari widget

Activate the environment used for installation and run:

```text
napari
```

In napari, choose:

```text
Plugins → VIPP Workflow (napari-vipp)
```

The VIPP dock widget has three main regions:

| Region | What it is for |
| --- | --- |
| Node library | Search or browse operations, then add them to the graph. |
| Graph canvas | Connect and arrange the visible analysis. |
| Inspector | Edit the selected node, calculate manual nodes, and inspect output metadata, images, histograms, or tables. |

The top toolbar opens examples and workflows, saves or exports the graph,
starts batch processing, and exposes display/execution settings.

## Open a bundled example

Choose **Open example…** in the VIPP toolbar. The chooser groups complete graph
templates by task and configures their `Image Source` nodes to use matching
bundled samples.

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
