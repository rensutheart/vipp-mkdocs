# Build your first workflow

In this exercise you will create a short segmentation graph from an empty
canvas. It uses bundled data, so unexpected results are easier to diagnose.

## 1. Start clean

Choose **New workflow…** and confirm the reset. VIPP keeps one unbound
`Image Source` on the otherwise empty canvas. Select that source (do not add a
second one) and set:

| Setting | Value |
| --- | --- |
| Source | `sample` |
| Sample | `VIPP synthetic multichannel volume` |

Wait for the source thumbnail and metadata to appear.

## 2. Add and connect nodes

Search the node library and add these operations:

```text
Image Source → Extract Channel → Gaussian Blur → Otsu Threshold
             → Fill Holes → Label Connected Components
```

Drag from an output port to a compatible input port. Typed ports prevent many
invalid connections; they do not detect scientifically inappropriate choices.

Set `Extract Channel` to the red channel. If channel names are available,
prefer the semantic name; otherwise verify the index visually.

## 3. Tune while looking upstream and downstream

Select `Gaussian Blur`. Change its scale gradually and compare:

- small puncta in the extracted channel;
- speckle in the smoothed image;
- foreground retained by `Otsu Threshold`;
- object merging after connected components.

Restore a conservative value before continuing. There is no universally
correct blur or threshold: tune against the structures your assay intends to
measure.

## 4. Add a measurement branch

Add `Measure Objects` and connect the labels to it:

```text
Label Connected Components → Measure Objects
```

Select the measurement node and choose **Calculate**. Check the row count,
column names, units, and whether leading axes are represented as expected.

## 5. Save an inspectable checkpoint

Choose **Save workflow…** and use a name that communicates its purpose and
release, for example:

```text
nuclei-segmentation-vipp-0.12.0a2.json
```

Also record:

- the input dataset or acquisition family used for tuning;
- any manual exclusions;
- expected axes and physical units;
- one or more reference images used to judge the result.

Workflow JSON is necessary but not sufficient provenance. See the
[workflow contract](../reference/workflow-contract.md) for what it does and
does not preserve.

## 6. Test that the workflow reopens

Create a new workflow, then load the saved JSON. Confirm the source, graph,
parameters, and connections before relying on the file as an analysis record.

Next, learn how to [use your own images](own-data.md) without assuming that the
same parameters will transfer unchanged.
