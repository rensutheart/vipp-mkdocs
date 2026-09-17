# Grow regions from seeds

Use numbered seed objects to divide a foreground region into separate objects.
For example, nuclei can seed cell regions in an actin image. The seeds supply
object identity; the image guides boundaries; the mask limits where growth is
allowed.

!!! info "Unreleased"
    **Grow Regions from Seeds — CellProfiler Propagation** is a new CPU node
    documented for nightly development. It is not in 0.15.0a5.
    **Marker-Controlled Watershed** is already available for 2D and 3D data.

## Choose the method

| Need | Method |
| --- | --- |
| The 2D CellProfiler Propagation rule, using appearance and distance from seeds | Grow Regions from Seeds — CellProfiler Propagation |
| Seeded flooding of an elevation image, including a full ZYX volume | Marker-Controlled Watershed |
| Growth by geometric distance without an intensity image | Expand Labels |

These methods can produce different boundaries from the same seeds. Choose the
method before tuning parameters, and validate the result on held-out images.

## Grow 2D regions with CellProfiler Propagation

1. Prepare one scalar **YX** image. For multichannel or volumetric data, use
   **Extract Channel** and **Select Axis Slice** to select the intended channel,
   time point and plane. Confirm that the result has exactly two axes, Y and X.
2. Create a labels image for the seeds, with zero as background and a distinct
   positive integer for each object. Nucleus labels are one possible source.
3. Create a Boolean foreground mask with a threshold or other reviewed
   segmentation. Inspect it: growth cannot cross excluded pixels.
4. Add **Grow Regions from Seeds — CellProfiler Propagation**. Connect the
   intensity image to **Guidance image**, labels to **Seed labels**, and the
   mask to **Foreground mask**.
   All three must share the same shape, axes and physical grid.
5. Start with **Distance regularization** at **0.05**, then click **Calculate**. Higher
   values give pixel distance more influence relative to image appearance.
   Compare the output over the input image using
   [label boundaries](../workflows/segmentation-label-cleanup.md#inspect-label-boundaries).
6. Save the chosen preprocessing, mask and regularization in the workflow.
   Apply those frozen settings to held-out fields before using the labels for
   measurements.

The node keeps seed IDs and returns an `int32` labels image. A seed outside the
mask remains in the output but does not start growth. A disconnected masked
region with no reachable seed stays zero. Inspect both cases when labels seem
missing or extend beyond the foreground.

**Intensity scale matters.** The node does not normalize the image. A setting
of 0.05 on raw uint16 intensities is not equivalent to 0.05 on an image scaled
to 0–1. Make any rescaling an explicit upstream step and save its settings.
The node uses manual/cached execution; recalculate it after changing an input
or parameter.

## Use watershed on a 3D volume

1. Prepare aligned **ZYX** image, marker-label and Boolean mask volumes. Select
   a channel and time point explicitly if the source also contains C or T.
2. Connect all three to **Marker-Controlled Watershed** and select **3D ZYX**
   for its spatial mode. Check the input-axis interpretation before running.
3. Choose the elevation image deliberately. For separating touching objects
   in a mask, use **Euclidean Distance Transform** and **H-Maxima Markers**, then
   set **Image meaning** to **Distance map (invert)**. Use **Elevation image**
   for a supplied elevation whose low values should form basins.
4. Inspect the resulting labels through Z and in orthogonal views. Compare
   object identity and split/merge errors, not only a maximum projection.

The repository's
[`seeded-3d-watershed.json`](https://github.com/rensutheart/napari-vipp/blob/main/examples/seeded-3d-watershed.json)
provides a runnable graph, initially bound to the bundled synthetic volume.
Download and open that workflow, then replace its image source with a reviewed
ZYX volume to try the same steps. Its saved parameters are a validation example,
not established settings for every mitochondrial acquisition.

The existing watershed uses voxel adjacency, and the existing distance
transform uses voxel-index distances. They do not use physical voxel spacing
to adjust those calculations. Calibration is retained for later measurements,
but unequal Z and XY spacing can still affect the segmentation. **Sobel Edges**
operates per YX plane and should not be described as a volumetric gradient.

For exact input rules and the boundary of CellProfiler compatibility, see the
[seeded segmentation reference](../reference/seeded-segmentation.md).
The [validation status](../reference/validation-status.md#unreleased-seeded-segmentation)
separates acquired-volume backend checks from biological validation.
