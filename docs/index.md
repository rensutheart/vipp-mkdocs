# napari-vipp Documentation

`napari-vipp` is a napari-native visual image processing pipeline system for
bioimage analysis. It lets users build graph workflows, inspect intermediate
outputs, tune parameters, preserve image metadata, produce measurement tables,
and export or batch-run workflows.

!!! warning "Alpha software"
    VIPP is active alpha software. Workflows, node parameters, and file
    compatibility may change between releases. Validate outputs before using
    them for scientific interpretation or publication.

## Use This Site When You Need To

- get VIPP installed and launched;
- understand images, masks, labels, tables, axes, and metadata;
- choose the right node family for a task;
- follow a workflow pattern;
- find an example workflow or synthetic sample;
- troubleshoot performance or memory behavior;
- understand what is validated and what is still experimental.

## Fast Paths

| Need | Start here |
| --- | --- |
| First-time user | [Installation](getting-started/installation.md) |
| Build a simple graph | [First Workflow](getting-started/first-workflow.md) |
| Understand ports and data types | [Data Types](concepts/data-types.md) |
| Segment objects | [Segmentation And Label Cleanup](workflows/segmentation-label-cleanup.md) |
| Measure objects and export tables | [Object Measurements And Tables](workflows/object-measurements-tables.md) |
| Analyze skeleton networks | [Skeleton And Network Analysis](workflows/skeleton-network-analysis.md) |
| Run colocalization analysis | [Colocalization And Association](workflows/colocalization-association.md) |
| Check nodes by family | [Node Index](reference/node-index.md) |
| Find sample data | [Sample Data](reference/sample-data.md) |
| Find workflow JSON files | [Example Workflows](reference/example-workflows.md) |

## Documentation Philosophy

The documentation has two jobs:

1. Help expert users get unstuck quickly.
2. Preserve enough scientific context that workflows remain inspectable and
   reportable.

The future training book can teach bioimage analysis more slowly. This site is
the quick, searchable system manual.

