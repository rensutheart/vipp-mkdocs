# Supported input and output

VIPP routes interactive sources, selected-output saves, `Save Image`, batch
outputs, and generated scripts through a shared headless I/O layer. Format
support does not imply lossless preservation of every source metadata field.

## Input routes

!!! info "Included microscope readers"
    Native CZI, Leica, ND2 and Olympus readers are now default dependencies for
    plugin and desktop installations; Bio-Formats remains optional. See
    [Reader support in Image Source](../getting-started/reader-support.md).
    This changes installation, not the scientific format guarantees below.

| Source | Behavior in 0.15.0a2 |
| --- | --- |
| Napari layer | Detaches supported NumPy data and metadata into a revision-tracked snapshot; stale results are rejected. |
| Bundled sample | Loads one of 15 deterministic VIPP samples. |
| OME-TIFF | Reads image series and supported semantic axes, scale, channel, and selected acquisition fields from OME metadata. |
| ImageJ TIFF | Reads supported hyperstack axes, XY resolution, z spacing, frame interval, and unit fields where present. |
| Conventional TIFF | Reads TIFF series and infers basic axes where explicit semantic metadata is absent. |
| Nikon ND2 with the included `nd2` reader | Exposes stable items, lazy inspection/data access, decoded-size estimates, calibration, channels, and selected objective metadata in the qualified corpus. |
| Local OME-Zarr 0.4/0.5 | Discovers image/label groups and declared levels/transforms. A sliced lower level can be displayed while analysis remains fixed to level 0; label previews retain label semantics. One strictly eligible sole direct Crop Stack can also read its exact retained level-0 window before materialization. |
| NPY / NPZ | Reads one NPY array or a selected NPZ member; semantic microscopy metadata is not inherent. |
| PNG, JPEG, BMP, GIF, WebP, TGA, PNM | Reads ordinary raster images; animated rasters use a leading time axis. |
| Microscope readers | Qualified corpus routes cover CZI/LSM, ND2, LIF, OIR/OIB/OIF/VSI, and IMS with normalized inspection/read metadata. Native readers are included; the Bio-Formats IMS/VSI route remains optional. Native LIF, CZI, OIR/OIB, and LSM pixels remain eager; broad advertised extensions are not all qualified claims. |

Always inspect the resulting shape, axes, scale, unit, channel mapping, dtype,
and chosen series. Missing fields can be inferred; an inference is not the same
as acquisition metadata.

For an inspectable multi-series TIFF, NPZ, Zarr, microscope container, or
similar source, VIPP records a frozen `SourceItem v1`: stable logical selector,
reader/backend and version, normalized shape/axes/metadata, and exact container
revision. Interactive browsing, collision-safe output names, batch planning,
manifests, and provenance retain that identity. Changed bytes, missing
companions, ambiguous legacy indices, or an unexpected reader topology stop for
review instead of selecting a different image by position.

For every microscope reader, actively move the T, Z, and C controls on a
representative acquisition and verify that the expected content changes. Check
the selected item, reader/backend, calibration, channels, and decoded shape
against acquisition records. A normalized contract cannot prove that a
third-party reader's presentation matches the experiment.

## Source revision contract

File and directory-store sources are identified from their path revision and
bytes before and after inspection/materialization. VIPP owns a read-only array
snapshot pinned until **Refresh**. If the source changes during work, the
result is rejected rather than combining revisions.

Live NumPy-backed napari layers are copied and revision-tokened. Supported data,
metadata, RGB, axes, scale, translation, unit, rotation, shear, and affine
changes invalidate stale work. A live lazy array or transform that cannot be
detached without changing pixels is rejected.

These checks protect one execution boundary; they do not replace an archival
checksum or persistent dataset identifier.

For local multiscale OME-Zarr, a lower-level presentation layer is labelled
`Preview level N - analysis remains full resolution`. The dynamic chooser lists
the declared levels available for that selected image or label. Requested
T/Z/C positions and Y/X region are sliced before preview computation. This
layer never replaces SourceItem analysis level 0, scientific cache data, batch
input, generated execution, or output provenance.

## Export choices

| Format | Use when | Check carefully |
| --- | --- | --- |
| OME-Zarr | Chunked multidimensional image data or an image with associated label outputs | Current export/pyramid scope and downstream reader compatibility |
| OME-TIFF | A portable processed image with supported OME metadata | dtype, axes, scale, and series after reopening |
| ImageJ TIFF | Fiji/ImageJ hyperstack interoperability is required | It cannot safely represent 32-bit integer label IDs |
| TIFF | Broad TIFF compatibility or 32-bit labels are needed | Semantic metadata may be limited compared with OME routes |
| NPY | Exact array/dtype exchange in Python | Axes, scale, units, and channel semantics must be stored separately |
| Ordinary raster | A 2D display image is required | Display-oriented only; not a quantitative stack/archive format |
| CSV / TSV | A table will be analyzed elsewhere | Units, identity columns, missing values, and delimiter handling |
| 3MF | [Mesh objects](../workflows/mask-to-mesh.md) need portable units and display colours | Scientific surfaces, not print-validated solids; physical calibration is required. |
| OBJ | Mesh geometry/object groups are needed, including uncalibrated voxel coordinates | Units, original IDs and colours are in VIPP comments; no standard unit field or material file. |

### Format details

OME-TIFF is the default quick-save format; the OME-Zarr writer defaults to 0.4.
ImageJ TIFF encodes binary masks as `uint8` 0/255. PNG can preserve 16-bit
grayscale values and label IDs up to 65,535; other ordinary raster routes are
8-bit display exports, and JPEG cannot store alpha. Use a scientific image
format when axes, calibration, stacks, or exact label identity matter.

For additional readers, see [optional format packages](../getting-started/installation.md).

<span id="mesh-export-nightly"></span>

### Mesh export

**Save Image** also accepts mesh inputs, with **auto**, **obj** and **3mf** format
choices. **Auto** follows `.obj`/`.3mf` in the path (OBJ when no suffix is given).
**Batch Output** offers **batch default**, **obj** and **3mf** for meshes. Their
menus switch to image formats for image inputs; batch tables get CSV/TSV.
Incompatible saved choices are flagged rather than silently changed. Auto-saving
**Save Image** nodes remain prohibited in batch runs; use **Batch Output** there.

Both formats retain object placement and export calibrated XYZ coordinates with
outward winding preserved. Export does not register, weld, unite, smooth, repair
or scale a specimen for printing. Batch **batch default** stays OBJ; choose
**3mf** explicitly when required.

**3MF** stores separate objects in one assembly, retaining their relative
positions. Micrometre, millimetre, centimetre and metre coordinates use native
3MF units. Compatible mixed units are converted; nanometres, picometres and
angstroms use microns. Missing, pixel-only or incompatible physical units are
rejected instead of being interpreted as millimetres.

Display colours use 8-bit sRGB/RGBA. Per-object VIPP metadata also retains the
original floating-point RGBA, names, IDs, source/parent IDs and source
calibration/history. Receiving software may ignore custom metadata or alpha.

The [3MF Core specification](https://github.com/3MFConsortium/spec_core/blob/master/3MF%20Core%20Specification.md)
permits open geometry with the **surface** object type used here. This is not
a claim of watertightness, print readiness or printer-material colour matching.
Representative open/closed two-object outputs were checked against the
Consortium's Core XSD; that checks document structure, not biological validity
or every receiving application's behaviour. Reopen a representative export in
your intended software before a large batch.

**OBJ** stores separate object groups. Units, colours and provenance are comments
rather than portable material/unit declarations; no `.mtl` file is generated.
Confirm import units manually, or use 3MF for standard display colours and units.

## OME analysis dataset

**Export OME dataset...** writes one reference image and graph label outputs into
one local `.ome.zarr` store:

```text
/
  s0
  labels/
    label_output_name/
      s0
```

Use it when label outputs should remain associated with a reference image. For
a standalone label image, use TIFF/OME-TIFF or provide an image-linked OME-Zarr
dataset; the command is not a general project archiver. This UI action
serializes accepted cached values. It does not rerun the graph through the
shared executor or create an exact compute-provenance sidecar.

## Current limitations

- Lower-level presentation preview and exact source-window reads are limited to
  local OME-Zarr 0.4/0.5. Exact level-0 pushdown requires one direct,
  non-bypassed Crop Stack with explicit compatible axes; other paths still
  materialize the complete selected image when memory preflight permits it.
- Remote stores, IMS pyramid preview, plate/well/field browsing, and general
  operation-level lazy/chunked execution are planned, not current.
- Native LIF, CZI, OIR, OIB, and LSM pixels remain eager. Large eager readers
  can receive decoded-memory preflight but not invented chunk progress.
- Only supported metadata fields propagate through compatible operations and
  writers; complete source metadata fidelity is not claimed.
- Reopen representative outputs in the intended downstream software before a
  large run.
- Same-shape inputs can still be scientifically misregistered even when their
  declared grids match. VIPP validates declared axes/calibration; it does not
  infer biological correspondence or perform registration.
- Local batch processing pairs sorted source items by position. It expands
  inspectable multi-series containers, but selected semantic-axis iteration,
  remote collection input, and plate/well/field HCS traversal remain outside
  0.15.0a2.

## Execution provenance for saved outputs

The interactive **Save selected output...** action writes the selected cached
result directly. It does not rerun the graph or write exact execution
provenance, so it is not a complete analysis archive. Generated Python/CLI can
instead write an atomic `.vipp-provenance.json` sibling that binds the output
node/port to the effective compute request, actual CPU/CuPy
implementation, environment, fallback records, outcome, and cleanup evidence.
Failed or cancelled single-output publication attempts a failure sidecar at
the requested destination name.

Batch uses its authoritative version-5 manifest instead of duplicating one
sidecar per output. Every published output record carries an execution digest
link to that item's complete execution document. Successfully read sources
include canonical SourceItem/revision evidence, raw/effective axes, and any
declaration; requested/effective per-sample overrides and their workflow hashes
are also retained. Preserve the manifest, archive, item checkpoints,
workflow/config pair, and source identities with the files.

A generated standalone output remains private until execution cleanup and its
requested staged publication checks are established. The generated local
`load_image()` path hashes the exact source before reading and verifies it after
materialization; arbitrary `ImageDataset`, `SourcePayload`, and raw-array inputs
are only as strong as the identity and stability the caller supplies. The
generated folder helper privately stages and rollback-protects each requested
output/sidecar set in one destination directory. Saved batch execution
additionally reverifies source bytes immediately before promoting an item's
outputs and supplies multi-source planning, checkpoints, and a manifest. OOM
fallback is recorded rather than hidden, and a cleanup or publication failure
prevents a newly calculated output from being presented as successfully
published.

## Multi-input grid safety

Operations that combine arrays validate more than shape: axis meaning, sample
counts, scale, compatible units, and origin must satisfy the operation's grid
contract. Masks broadcast by unique semantic correspondence, not coincident
sizes. Image/PSF pairs require compatible spatial sampling. VIPP does not
silently resample, register, reorder, or repair a transform.

For what workflow and Python export preserve, see the
[workflow and export contract](workflow-contract.md).
