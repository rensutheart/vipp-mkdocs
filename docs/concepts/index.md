# Concepts

These pages explain the mental model behind VIPP.

Start with:

- [Graph Workflows](graph-workflows.md)
- [Data Types](data-types.md)
- [Axes And Metadata](axes-and-metadata.md)
- [Inspection Model](inspection-model.md)
- [Examples And Samples](examples-and-samples.md)

VIPP is easiest to use when you treat every graph edge as a scientific object:
an image, mask, label image, table, PSF, or future data type with a specific
meaning.

In 0.13, apply the same distinction to execution: the workflow stores a
portable **CPU / Auto / Prefer GPU / Custom** request, while an accepted run records
the actual CPU/CuPy/cuCIM implementation and any fallback. See
[choose and verify compute](../how-to/choose-compute.md).
