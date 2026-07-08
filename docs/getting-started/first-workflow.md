# First Workflow

This first workflow creates cleaned labels from one fluorescence channel. Once
the labels look reasonable, they can be measured in the next workflow step.

## Starting Point

Open the runnable example from the VIPP toolbar:

```text
Open example... > Segmentation & Labels > Red-Channel Label Cleanup
```

This loads the checked-in label-cleanup workflow and sets its `Image Source`
node to the bundled sample:

```text
VIPP synthetic multichannel volume
```

The sample channels are ordered blue, green, red. This example explicitly uses
the red/TRITC-like channel.

Napari's `File > Open Sample` menu is not required for this workflow. Use it
only when you want to inspect raw sample layers directly in the napari layer
list.

## Choose Or Change The Source

Select `Image Source` in the graph and choose the data in the inspector. Set
`Source` to `napari layer`, `file path`, or `sample`. The napari layer dropdown
is shown only when `Source` is `napari layer`; sample and file sources use their
own controls.

For example workflows, `Source` is usually `sample`. You can switch it later to
`napari layer` or `file path` when applying the workflow to your own data.

## Screenshot

![First VIPP workflow overview](../assets/screenshots/getting-started/first-workflow-overview.png)

This screenshot shows the checked-in first label-cleanup workflow loaded in
VIPP as a detached, maximized window. The node library is hidden, the graph is
zoomed out to show the full workflow, the preview mode is set to `MIP`, and the
inspector exposes the selected label-filtering parameters.

## Build The Graph

Create this graph:

```text
Image Source
  -> Split Channels
  -> Gaussian Blur
  -> Otsu Threshold
  -> Fill Holes
  -> Label Connected Components
  -> Clear Border Objects
  -> Filter Labels By Volume
```

Natural next step:

```text
Filter Labels By Volume
  -> Measure Objects
```

## What To Inspect

Inspect these outputs before trusting the final table:

- the red channel after `Split Channels`;
- the blurred image;
- the binary mask after `Otsu Threshold`;
- the cleaned mask after `Fill Holes`;
- the label image after `Label Connected Components`;
- the border-cleared labels and the volume-filtered labels;
- the table preview after adding `Measure Objects`.

## Why This Workflow Matters

It demonstrates the central VIPP pattern:

1. Create an intermediate output.
2. Inspect it visually.
3. Tune the parameter.
4. Confirm the downstream effect.
5. Save the workflow and outputs.

The same graph can later be adapted for batch output or exported to Python.
