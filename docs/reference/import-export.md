# Supported input and output

VIPP routes interactive sources, selected-output saves, `Save Image`, batch
outputs, and generated scripts through a shared headless I/O layer. Format
support does not imply lossless preservation of every source metadata field.

## Input routes

| Source | Behavior in 0.13.0a5 |
| --- | --- |
| Napari layer | Detaches supported NumPy data and metadata into a revision-tracked snapshot; stale results are rejected. |
| Bundled sample | Loads one of 13 deterministic VIPP samples. |
| OME-TIFF | Reads image series and supported semantic axes, scale, channel, and selected acquisition fields from OME metadata. |
| ImageJ TIFF | Reads supported hyperstack axes, XY resolution, z spacing, frame interval, and unit fields where present. |
| Conventional TIFF | Reads TIFF series and infers basic axes where explicit semantic metadata is absent. |
| Nikon ND2 with the optional `nd2` reader | Uses the reader's ordered dimension mapping when labels/sizes exactly match the returned shape, keeping T/Z/C navigation aligned; malformed mappings fall back conservatively. |
| Local OME-Zarr 0.4/0.5 | Discovers supported image/label groups and reads analysis level 0; label groups are marked as labels. |
| NPY / NPZ | Reads one NPY array or a selected NPZ member; semantic microscopy metadata is not inherent. |
| PNG, JPEG, BMP, GIF, WebP, TGA, PNM | Reads ordinary raster images; animated rasters use a leading time axis. |
| Optional microscope readers | Uses an installed format-specific/BioIO route and normalizes fields the reader exposes. Coverage varies by format. |

Always inspect the resulting shape, axes, scale, unit, channel mapping, dtype,
and chosen series. Missing fields can be inferred; an inference is not the same
as acquisition metadata.

For ND2, actively move the T, Z, and C sliders on a representative acquisition
and verify that the expected content changes. Ordered-axis normalization fixes
the affected 0.12 behavior, but it cannot prove that a third-party reader's
metadata or selected series matches the experiment.

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

## OME analysis dataset

**Export OME dataset…** writes one reference image and graph label outputs into
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

- Analysis reads use OME-Zarr level 0; preview-level/pyramid selection is not
  exposed.
- Plate/well/field browsing and remote URI input are planned, not current.
- Lazy OME-Zarr arrays may materialize when an eager operation executes.
- Only supported metadata fields propagate through compatible operations and
  writers; complete source metadata fidelity is not claimed.
- Reopen representative outputs in the intended downstream software before a
  large run.
- Same-shape inputs can still be scientifically misregistered even when their
  declared grids match. VIPP validates declared axes/calibration; it does not
  infer biological correspondence or perform registration.
- Local batch processing pairs sorted file collections by position. Semantic
  axis iteration, remote collection input, and plate/well/field HCS traversal
  are outside 0.13.0a5.

## Execution provenance for saved outputs

The interactive **Save selected output…** action writes the selected cached
result directly. It does not rerun the graph or write exact execution
provenance, so it is not a complete analysis archive. Generated Python/CLI can
instead write an atomic `.vipp-provenance.json` sibling that binds the output
node/port to the effective compute request, actual CPU/CuPy/cuCIM
implementation, environment, fallback records, outcome, and cleanup evidence.
Failed or cancelled single-output publication attempts a failure sidecar at
the requested destination name.

Batch uses its authoritative version-3 manifest instead of duplicating one
sidecar per output. Every published output record carries an execution digest
link to that item's complete execution document. Successfully read source
records include their raw axes, effective axes, and applied declaration. The
embedded config preserves an intended declaration even when an item was skipped
or failed before source reading. Preserve the manifest, archive, item
checkpoints, workflow/config pair, and source identities with the files.

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
