# Crop an image or volume

Use **Crop Stack** to remove borders while keeping time points and channels.
Cropping changes the scientific image; it is not a display zoom.

## Set the margins

1. Connect the image to **Crop Stack** and select the node.
2. Check the axes and physical spacing in **Output Metadata**.
3. Adjust the margins, using the overlay to review the retained region.
4. Release the slider or finish numeric entry to commit the crop.
5. Inspect the cropped output and its updated origin before continuing.

| Controls | Axis affected |
| --- | --- |
| Top / Bottom | Y |
| Left / Right | X |
| Z start / Z end | An explicitly declared Z spatial axis only |

Each opposing pair must leave at least one sample. Time, channels, and other
nonspatial axes remain complete. A `QYX` TIFF does not become a Z stack by shape
alone: first review its [axis declaration](../concepts/axes-and-metadata.md#tiff-page-labels-at-an-image-source).

## Understand the overlay

- The 2D outline is orange on a retained Z plane and red on an excluded plane.
- The 3D view uses a transparent wireframe, not a filled volume.
- Dragging shows a draft; holding the mouse still does not commit it.
- Releasing commits one edit and starts one calculation. One Undo restores the
  margins from before the drag.

VIPP also commits pending margins before calculation, saving, export, batch
start, tab change, or close. Saved workflows therefore use the final visible
crop, not an earlier intermediate slider value.

## Channels and calibration

Crop Stack protects a known channel axis. **Channel axis override** appears
only when axis roles need review or a saved non-negative override needs repair.
It identifies an axis to protect; it never chooses one channel from it.

Spatial scale and units are retained. Each cropped origin moves by
`leading margin × scale`. For example, cropping a `(5, 3, 12, 96, 128)` TCZYX
image by Z `2/1`, Y `4/5`, and X `6/7` produces `(5, 3, 9, 87, 115)`.

Older workflows without Z margins load with both Z margins at zero.

## When the full source will not fit in RAM

For a strictly eligible local OME-Zarr source, VIPP can read only the exact
retained level-0 window. It still verifies the complete source container;
cropping reduces pixel decoding/allocation, not necessarily file-check time.

The source must feed one direct, active Crop Stack, without another branch or
output tunnel. Axes and source identity must be known. Unsupported readers,
bypassed crops, and ambiguous or changed inputs cannot use this shortcut.

When offered, **Add fitted Crop Stack** or **Fit existing Crop Stack** proposes
a centred region based on geometry, chunk sizes, and RAM headroom. It is one
undoable edit—not a content-aware ROI or a scientific recommendation. Review
the region yourself; later operations may still require more memory.

See [memory limits and exact source crops](../reference/cache-memory.md#low-ram-source-crop-repair)
for the supported boundary. The bundled **Responsive Volumetric Crop Acceptance**
workflow provides a small, repeatable example.
