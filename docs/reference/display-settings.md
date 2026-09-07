# Graph display settings

These controls change graph-card presentation, not image data or analysis results.
They are separate from the main napari viewer's display controls.

In **0.15.0a1**, open **Preview**. In **nightly builds after 0.15.0a1**, the
button is **Display settings**, shortened to **Display** in narrower windows.

## Menu labels

| 0.15.0a1 label | Nightly label |
| --- | --- |
| Mode | Thumbnail view |
| Contrast | Contrast method |
| Range | Contrast based on |
| Colormap | Colour map |
| Detail | Thumbnail resolution |
| Port labels | Input/output labels |

The options below use the nightly wording. **Slice / MIP / Off** in 0.15.0a1
correspond to **Current slice / Maximum-intensity projection (MIP) / Hidden**.
**Percentile / Min-max / Raw** become **Percentile (0.5–99.9%) /
Minimum–maximum / Raw**; these are label changes, not new calculations.

Nightly builds disable **Entire stack** when no available graph preview contains
a stack or series. The view-dependent label describes what is displayed; this
does not change the saved preference for use when a stack becomes available.

## Choose a useful view

- Use **Current slice** for interactive inspection, or **Current image** for 2D.
- Use **Maximum-intensity projection (MIP)** for an overview, not to verify 3D
  connectivity or depth.
- Use **Hidden** when thumbnails are unnecessary or expensive.
- Use **Entire stack** contrast for stable brightness while moving through slices.
- Use current-slice/view contrast for quicker local inspection. Its limits can
  differ between slices; do not read equal brightness as equal intensity.

## Resolution and exact statistics

| Resolution | Backing pixels |
| --- | --- |
| Low | 90 × 55 |
| Standard | 180 × 110 |
| High | 360 × 220 |
| Very high | 720 × 440 |

Resolution changes the retained thumbnail image, not node calculations or
scientific output. The graph card stays the same size; **Very high** retains
four times the backing pixels of **High**, not necessarily more screen pixels.

- **Entire stack** contrast keeps its cached exact limits when resolution changes.
- **Current slice** contrast uses the selected resolution's spatial sample, so
  its display limits may change slightly.
- These are local presentation preferences, not workflow parameters or
  scientific provenance.

### Where to see contrast activity

Select a node and look for **Thumbnail contrast** in its inspector. It shows
**Calculating…**, **CPU · NumPy**, **GPU · CuPy**, amber **CPU fallback**, or red
**Error**. This is separate from the graph card's scientific-compute badge.

Hover the row or thumbnail for scope, resolution, algorithm, byte count,
elapsed time, backend choice, and failure details. Keyboard **What's This**
help and screen readers receive the same information.

The shared toolbar reports the active node, backend, and statistics phase.
**Cancel** takes effect at the next safe boundary; a GPU kernel or exact
NumPy percentile call may need to finish first. No partial contrast limit is
published.

### How the limits are calculated

For Stack Percentile contrast, native `uint8` and `uint16` results use an exact
dtype-aware histogram. CPU and CuPy produce the same display limits, including
the NumPy-linear 0.5th/99.9th-percentile result. Min-max uses an exact native CPU
reduction rather than constructing a histogram. Float and other-dtype
percentiles use the exact NumPy-compatible CPU path in this release. Raw integer
contrast, masks, labels, tables, and other scan-free previews do not launch an
unnecessary statistics scan.

### CPU and GPU choices

- Presentation **Auto** chooses using the full output's dtype and size, not
  thumbnail resolution.
- Presentation **CPU** never initializes CUDA.
- Presentation **Prefer GPU** attempts eligible CuPy histograms and visibly
  falls back to CPU when safe.

The main compute policy takes precedence: **CPU** forces presentation CPU;
**Prefer GPU** biases presentation Auto toward GPU; **Auto** and **Custom**
leave it adaptive. Automatic selection is a heuristic, not a guarantee of the
fastest path on every dataset or machine.

??? info "Automatic-selection and background-work details"

    Before the first successful thumbnail GPU calculation, Auto uses a
    384-MiB crossover for `uint8` and 512 MiB for `uint16`. Both become 32 MiB
    while that path is warm. Data distribution, hardware, CUDA startup,
    residency, and competing work can change which path is faster.

    Small CPU-only batches finish immediately without occupying the toolbar
    progress strip: at most 1 MiB total, eight requests, and eight aggregate
    scalar/channel lanes. Larger work, high-channel data, and GPU paths use a
    cancellable background worker. Inspector status is recorded in either case.

    CPU integer histogram and min-max calculations advance and cancel between
    bounded chunks. Scheduling changes neither the population nor the contrast
    algorithm.

## Port-label layout

**When needed / Always / Never** in nightly builds correspond to
**Ambiguous only / Show all / Hide all** in 0.15.0a1.

Long port names are shortened on the card and retain their full text in a
tooltip. Changing the label mode can make an already tightly packed layout
overlap; VIPP reports the number of overlapping card pairs in its message strip.
Use **Auto Arrange** to make
label-aware space, or move the affected
cards manually. Label visibility is a graph-display choice and never changes
connections or processed data.


## Related settings

**Link napari/VIPP sliders** controls dimension synchronization.
**Save thumbnail visibility in workflows** saves per-node visibility choices.
Both remain in the gear menu; neither changes pixels.

For full-resolution inspection and exported figures, see
[inspect and compare outputs](../how-to/inspect-outputs.md).
