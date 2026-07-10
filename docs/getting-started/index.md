# Start here

You do not need to write code to use VIPP. Start by opening a complete workflow
on synthetic data, learn how to inspect each stage, and only then build or adapt
a graph.

## A 20-minute route through the manual

| Time | Activity | Outcome |
| --- | --- | --- |
| 5 min | [Install](installation.md) and [launch](launching.md) | VIPP opens inside napari. |
| 5 min | [Tour a finished workflow](example-tour.md) | You can select nodes, inspect outputs, and identify a manual node. |
| 7 min | [Build a small workflow](build-workflow.md) | You can add, connect, tune, and save nodes. |
| 3 min | [Switch to your data](own-data.md) | You understand source choices and the checks required after transfer. |

!!! tip "Learn on the bundled data first"
    Bundled samples are deterministic, small, and free of privacy or licensing
    concerns. If a tutorial behaves differently from the manual on a bundled
    sample, check the [documentation version](../reference/versioning.md) before
    debugging your microscope file.

## What you should understand before batch processing

You are ready to run a folder only when you can:

- tell an image, mask, label image, and table apart;
- confirm the axes and physical scale of an input;
- inspect the mask and labels—not only the final table;
- explain the parameters that materially change the result;
- identify representative images that were not used for tuning;
- save a workflow and reopen it in the same VIPP release.

If any of those are unfamiliar, the [concepts](../concepts/index.md) and
[scientific-practice](../scientific-practice/index.md) sections provide the
necessary background without assuming Python knowledge.
