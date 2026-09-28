# Detect repeated patterns

Locate repeated structures with **Template Match**, then turn score peaks into
a coordinate table with **Find Peaks**. This detects locations; it does not
segment object boundaries or create labels.

!!! info "Unreleased after 0.16.0a2"
    These CPU-only nodes and two examples are available in the development
    version. Matching uses one fixed template size and orientation.

## Start with a known-answer example

Choose **Open example…** from the workflow actions menu, then open
**Detection & Peaks**:

| Example | Expected result at the saved settings |
| --- | --- |
| **Repeated 2D Pattern Detection** | Five asymmetric patterns, including two centers 12 pixels apart. |
| **Anisotropic 3D Pattern Detection** | Four volumetric patterns; a nearby pair is 6.4 micrometres apart. |

Use **Calculate all**, then inspect **Find Peaks**. Both examples explicitly
select timepoint `1` and the **Repeated pattern** channel (`1`), crop one complete
template, connect the valid-support mask, and plot retained scores. The other
channel is independent noise; the other timepoint has a different arrangement.
Canvas notes give the known center coordinates. A clipped border copy and a
deliberately absent site should not appear in the detection table.

## Build the detection branch

1. Check the source axes, pixel/voxel spacing and units. Use **Select Axis Slice**
   for the intended timepoint and **Extract Channel** for the intended channel.
   The resulting image must have explicit `YX` or `ZYX` axes.
2. Branch that selected image into **Crop Stack**. Crop tightly around one
   complete, distinctive example of the desired pattern. Keep Z for a 3D
   template; a projection is a different scientific input.
3. Connect the selected full image to **Template Match → Search image** and the
   cropped image to **Template image**. The template may have a different origin but
   must have matching sampling, spatial rank and axis order.
4. Calculate and inspect **Match scores** and **Valid scores**. The score map is
   smaller than the source and is calibrated at template centers, not at the
   top-left template corner.
5. Under Template Match's **Next step**, choose **Add Find Peaks**. This connects
   both outputs and enables **Use valid mask**, without calculating. **Show Find
   Peaks** selects an existing continuation. Set **Minimum value** and
   **Minimum separation** deliberately. Choose physical distance when unequal
   voxel spacing matters.
6. Calculate and inspect the detection table. Under **Detection review**, choose
   **Inspect detections on source…** for the read-only coordinate overlay. Review
   detections throughout Z, including faint, nearby and border structures.
   Connect the table to **Plot Results** to explore `score`, or export the table
   through the existing results controls.

Click a table row or marker to identify the same detection. In 3D, use **Z plane
(zero-based)**; the overlay shows one plane, not a projection. **Refresh view**
loads an already calculated result and does not calculate the workflow. If the
source or result changes, recalculate before interpreting the overlay.

Raise the score cutoff to remove weaker matches; lower it only while reviewing
false detections. Raising minimum separation can suppress real nearby objects.
The 2D example changes from five to four detections at `13` pixels; the 3D
example changes from four to three at `7` micrometres.

!!! warning "A high correlation is not a probability"
    The template's own location is included when it comes from the search image.
    Its near-one score is not independent validation. Patterns with changed
    scale, orientation, shape or contrast may be missed, while unrelated
    structures may match. Validate choices against independent representative
    annotations, not only the bundled synthetic examples.

See [Template matching and peaks](../reference/detection.md) for exact distance,
border, tie, numeric and table-coordinate rules.
