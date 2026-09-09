# Create, colour and export 3D mesh objects

Turn segmented volumes into separate coloured surfaces, inspect them in napari,
and export their geometry without losing object identity.

The **3D Meshes** category sits beside **Morphology**. Its nodes are manual/
cached by default and run on CPU. **Measure 3D Mesh Morphology** remains under
**Measurements** and also accepts their mesh outputs.

## Create the surfaces

For an end-to-end segmentation-to-mesh example, see
[Separate overlapping objects](separate-overlapping-objects.md).

To try a ready-made workflow, open **Open example → 3D Meshes →
Mesh Objects, Colours & Refinement**, then **Calculate all**. It uses a bundled
five-object sample, Turbo colours by triangle count, two smoothing iterations
at strength 1, and a target of 10% of triangles kept at aggressiveness 4.
Colour, Smooth and Simplify have **Auto Recalculate** enabled in this example.
These are saved sample-specific choices, not recommended settings for every
specimen. Compare upstream geometry and measurements before accepting the
refined result. Calculating the example does not save output files.

!!! note "Unreleased example consolidation"
    Nightly keeps the saved interactive workflow under the original example
    name. The two mesh-object examples shipped in 0.15.0a2 are now one;
    its saved parameters and layout are unchanged.

1. Prepare a **Boolean mask** or **integer labels**. Select one channel/time
   point upstream: the input needs exactly three explicit spatial axes, Z/Y/X,
   with at least two voxels each. A 2D mask is not extruded into invented depth.
2. Check calibration with **Set Pixel Size / Units** before extracting a mesh.
   Physical units are required for 3MF export.
3. Choose the object grouping:

    | Node and choice | Result |
    | --- | --- |
    | **Mask to 3D Mesh → Objects: Single object** | All foreground, including disconnected pieces, has one ID. This preserves existing workflows. |
    | **Mask to 3D Mesh → Objects: Connected objects** | Each face-connected foreground component gets its own ID and colour. Cavities remain part of their foreground object. |
    | **Labels to 3D Mesh** | Each positive label keeps its ID and gets a colour. Zero is background; disconnected regions with the same label remain one object. |

4. Choose **Image border**:

    - **Close at image border** adds background outside the volume. It closes
      cut objects, assuming they end there; it does not recover missing biology.
    - **Leave open at image border** makes no outside-background assumption.
      Border-touching objects can have open surfaces.

5. Click **Calculate**, then select or pin the result to inspect it in napari's
   **3D Surface** viewer. The graph card shows object, vertex and triangle
   counts instead of an image thumbnail. Mesh and table cards have no thumbnail
   placeholder, including while bypassed or before their first calculation.

Extraction uses full-resolution Lewiner marching cubes, level 0.5 and step 1,
without smoothing or repair. Empty masks have no surface; an entirely filled
volume with open borders has no internal interface. Large volumes need substantial
memory, and cancellation waits for the current extraction call to finish.

## Colour by identity or measurement

Add **Colour Mesh Objects** after extraction:

- **Colour by → Object ID** gives repeatable categorical colours.
- **Volume**, **Surface area**, **Sphericity** or **Triangle count** colours each
  object from its current geometry. Choose **Viridis**, **Plasma**, **Magma** or
  **Turbo** for the gradient. Unavailable measurements are grey.

Measurement colours span the finite minimum and maximum in this mesh collection;
they are not a fixed scale shared between different samples. Equal values use the
middle of the gradient. The node changes colours, not triangles, and does not
accept a separate measurement table in this version.

## Combine, split or select objects

| Node | What to do | Important distinction |
| --- | --- | --- |
| **Combine Meshes** | Set **Input meshes** from 2–16 and connect each mesh. | Retains separate objects, colours and physical positions. Compatible units convert to the first input's frame; incompatible calibration is rejected. No alignment, vertex welding or geometric union occurs. |
| **Split Mesh Objects** | Connect an existing mesh with disconnected pieces. | Gives edge-connected surface pieces separate IDs. Touching at a vertex alone does not join pieces. |
| **Filter Mesh Objects** | Choose **Measure**, **Minimum**, **Maximum** and **Keep objects**. | Select by Volume, Surface area, Sphericity, Triangle count or Object ID. **In range** includes both bounds; **Outside range** excludes them. Missing measurements are excluded in both modes. |

Splitting a hollow object separates its disconnected inner cavity wall too.
Prefer **Connected objects** during mask extraction when you want a hollow
foreground object to keep its walls together.

Filtering retains the kept IDs and colours. Combining preserves IDs unless they
collide, then assigns new IDs and records the original identities. Split parts
retain their parent identity in metadata. These are object-management operations,
not a method for registering different acquisitions.

### Choose filter limits from the input distribution

**Filter Mesh Objects** shows a histogram of the **input** objects for the
selected **Measure**, before filtering. Measurements run in the background
from the cached input mesh and use the same current-geometry calculation as
the filter. Calculate the upstream mesh first if no cached input is available.

Hover over a bin to see its measurement range and object count. Drag the linked
minimum/maximum markers or edit **Minimum** and **Maximum** to choose the bounds.
The plotted span follows the finite input measurements, so a distant bound such
as the default maximum of `1e12` does not flatten the distribution. Logarithmic
display changes only the plot, not measurements, bounds or filtering.
Unavailable values, including volume from open or invalid surfaces, are excluded
from the histogram and reported; they are also excluded by either filter mode.

The horizontal axis and filter bounds use the measurement's units. Volume is in
the mesh's X-axis unit cubed and surface area in that unit squared: an X axis in
`nm` gives `nm^3`/`nm^2`, and one in `mm` gives `mm^3`/`mm^2`. Compatible Z/Y units
are converted to X units; non-micrometer units do **not** fall back to voxels.
Without spatial units, these are geometric `voxel^3`/`voxel^2`, still using the
declared axis scales—not a count of foreground mask voxels. VIPP does not assume
a micrometer calibration. Sphericity is a dimensionless ratio; triangle count
and object ID are counts and identifiers, respectively.

## Smooth or reduce triangles

Keep the original mesh on an upstream branch for comparison. Both refinement
nodes return new geometry and retain object IDs and colours; neither overwrites
the input or promises unchanged shape, volume or measurements.

| Node | Starting settings | Effect |
| --- | --- | --- |
| **Smooth Mesh** | **Iterations: 10**, **Strength: 0.5** | Taubin-style smoothing in calibrated coordinates. More iterations or strength change the surface more. Strength 0 leaves geometry unchanged. |
| **Simplify Mesh** | **Triangles to keep (%): 50**, **Aggressiveness: 7** | Approximate quadric-error reduction per object/component. The percentage is what to **keep**, not remove; 100 leaves geometry unchanged. Higher aggressiveness favours faster reduction over fidelity. |

**Strength** controls smoothing per iteration, from **0 to 1** in **0.01** steps.
Start at **0.5**; higher values smooth more strongly. It is not a percentage of
volume reduction. Hover over the control for a reminder.

**Simplify Mesh** accepts fractional percentages (down to **0.01%**) and
aggressiveness in **0.1** steps; neither is restricted to whole numbers.

**Keep open boundaries fixed** is on by default for both. Locked boundaries and
small components can prevent reaching the requested triangle count. Review the
actual result, then recalculate measurements from that branch.

Invalid edges, duplicate/degenerate triangles and detected collapses are rejected
rather than repaired. These checks are not a complete topology or self-intersection
guarantee. Simplification may finish its current component before cancellation.

If refinement fails, the message identifies the object and whether the defect
was in the **input** or the **new result**:

- **Invalid input:** inspect the upstream mesh or regenerate it from the mask/
  labels. Changing refinement settings does not repair an existing defect.
- **Invalid simplified result:** increase **Triangles to keep (%)**, or try lower
  **Aggressiveness**. A valid slider value is not a guarantee for every geometry;
  there is no universal safe minimum percentage.
- **Invalid smoothed result:** reduce **Strength** or **Iterations**.

No new mesh is returned on failure. VIPP does not automatically delete duplicate
faces, since that can change surface validity and measurements. Any older cached
output remains stale until a successful calculation.

## Measure the current geometry

Connect any mesh result to
[Measure 3D Mesh Morphology](object-measurements-tables.md#3d-mesh-morphology)
and click **Calculate**. It produces one row per mesh object, keyed by `mesh_id`,
without running marching cubes again. An already-cached mesh can be measured
with **CPU**, **Auto** or **Prefer GPU** selected; this path remains CPU work.

Open or invalid surfaces have unavailable volume-derived measurements. Check
`mesh_status` and `mesh_error` before comparing objects or using a volume filter.

## Save the mesh

Select **Save mesh…** in the inspector:

| Format | Preserves | Check in the receiving application |
| --- | --- | --- |
| **3MF** | Physical units, separate named objects and display colours in one file; original IDs and calibration in metadata. | Objects are exported as scientific **surfaces**, not certified printable solids. Colour is display colour, not a printer-material assignment. |
| **Wavefront OBJ** | Triangle geometry and separate object groups; IDs, colours and calibration in VIPP comments. | OBJ has no standard unit field, and this export does not write a material file. Other readers may ignore the metadata and colours. |

Both use calibrated **XYZ** coordinates and retain relative positions—no printing
scale, centring or packing is applied. For uncalibrated data, choose OBJ to retain
voxel coordinates or correct calibration upstream and recalculate before 3MF.

For automatic saving during interactive calculation, connect **Save Image**:
it accepts images or meshes. Set a **Path** ending in `.obj` or
`.3mf`, choose **auto** or the matching format, and set **Auto-save on update**
to **on**. **Overwrite: no** protects an existing file. The mesh passes through
unchanged for downstream processing.

For batch work, use **Batch Output** instead and select **3mf** or **obj**.
**batch default** remains OBJ for existing workflows. Generated Python exports
support both formats. See [mesh export details](../reference/import-export.md#mesh-export)
for unit conversion and format limits.

Both nodes list formats for their connected input: mesh formats for meshes,
image formats for images, and CSV/TSV for batch tables. If reconnecting makes a
saved format incompatible, choose a replacement explicitly. Check the **Path**
as well; VIPP will not write image pixels into an old mesh filename.

## Methods

- [scikit-image marching cubes](https://scikit-image.org/docs/stable/api/skimage.measure.html#skimage.measure.marching_cubes)
- [Taubin's surface-smoothing method](https://doi.org/10.1145/218380.218473)
- [fast-simplification's quadric-error implementation](https://github.com/pyvista/fast-simplification)
