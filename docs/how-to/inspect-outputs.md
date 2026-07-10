# Inspect and compare outputs

VIPP has several inspection surfaces. Choose the one that answers the question
rather than treating a thumbnail as evidence for every decision.

| Surface | Good for | Not sufficient for |
| --- | --- | --- |
| Node thumbnail | Rapid whole-graph scan | Fine boundaries, rare failures, or quantitative QC |
| Inspector preview | Selected node at a controlled slice/MIP | Comparing many full-resolution layers |
| Pinned napari layer | Full-resolution comparison and overlay | Recording why a parameter was selected |
| Histogram | Dynamic range and threshold context | Spatial correctness |
| Label-volume histogram | Size-filter cutoff review | Shape or identity correctness |
| Table preview | Columns, rows, units, obvious missingness | Statistical validation of measurements |

## Pin an output in napari

1. Select a node with an image-like output.
2. If it has several outputs, select the intended output port.
3. Choose **Pin selected**.
4. Rename the napari layer if necessary so the operation and parameters remain
   recognizable.

Pin the raw image, a decisive intermediate mask, and the final labels for an
overlay review. Hide or show layers to locate false positives, missed objects,
merged objects, and boundary errors.

## Compare 3D data without hiding failures

A maximum-intensity projection can make a workflow look persuasive while
hiding slice-specific noise or z-merging. Review at least:

- representative `YX` slices at multiple z positions;
- the volume/MIP overview;
- objects near the top and bottom of the stack;
- regions with low signal or high background;
- anisotropic structures when z-spacing differs from x/y pixel size.

Use **Link napari/VIPP sliders** when synchronized slice navigation is useful.
Turn it off when the inspector should remain on a fixed reference slice.

## Review manual results after upstream changes

Manual/cached nodes become stale after a relevant upstream or parameter change.
Select the node and choose **Recalculate**, or use **Calculate all** for all
stale manual nodes. Do not take a screenshot or export a table while its status
indicates a stale cached result.

## Capture review evidence

For a formal analysis, retain representative QC images or screenshots with:

- input/sample identity;
- workflow and VIPP version;
- slice or projection mode;
- visible scale and units where relevant;
- enough context to identify the operation and parameter being reviewed.

Screenshots complement reference masks and quantitative tests; they are not a
replacement for them.
