# First Workflow

This first workflow creates labels from one fluorescence channel, then inspects
and measures those labels.

## Starting Point

Open the bundled sample data:

```text
File > Open Sample > VIPP synthetic microscopy samples
```

The most useful starting sample is:

```text
VIPP synthetic time-lapse multichannel
```

For a smaller first workflow, use:

```text
VIPP synthetic multichannel volume
```

## Screenshot

![First VIPP workflow overview](../assets/screenshots/getting-started/first-workflow-overview.png)

This screenshot shows the checked-in first label-cleanup workflow loaded in
napari. The viewer displays the selected label output, the graph shows
intermediate thumbnails, and the inspector exposes the selected label-filtering
parameters.

## Build The Graph

Create this graph:

```text
Image Source
  -> Split Channels
  -> Gaussian Blur
  -> Otsu Threshold
  -> Fill Holes
  -> Label Connected Components
  -> Measure Objects
```

## What To Inspect

Inspect these outputs before trusting the final table:

- the selected channel after `Split Channels`;
- the blurred image;
- the binary mask after `Otsu Threshold`;
- the cleaned mask after `Fill Holes`;
- the label image after `Label Connected Components`;
- the table preview from `Measure Objects`.

## Why This Workflow Matters

It demonstrates the central VIPP pattern:

1. Create an intermediate output.
2. Inspect it visually.
3. Tune the parameter.
4. Confirm the downstream effect.
5. Save the workflow and outputs.

The same graph can later be adapted for batch output or exported to Python.
