# Workflow and export contract

Use this page when deciding whether an artifact is sufficient to reproduce or
review an analysis.

## Workflow JSON

A saved workflow represents the editable graph. It can include:

- node operation IDs, titles, parameters, and canvas positions;
- connections and output-port hints;
- named tunnels and graph notes;
- selected workflow/UI state such as thumbnail visibility where enabled.

It does **not** embed calculated pixel arrays or tables. It also does not, by
itself, freeze the Python environment, preserve every external source, prove
metadata correctness, or capture the rationale for every choice.

Alpha compatibility is not guaranteed across releases. Preserve the original
file and the exact VIPP version. Test migrated copies before use.

## Generated Python

Python export translates a supported acyclic graph into direct calls to
napari-vipp's headless operations and I/O helpers. It is intended as readable
automation scaffolding and a reviewable operation sequence.

Generated code does not reproduce interactive caches, thumbnails, pinned
layers, graph layout, or the full runtime image-state behavior of the widget.
Review source bindings, output paths, dynamic outputs, dependency versions,
and generated code before a production run.

## Batch artifacts

A batch run can write the workflow JSON and generated pipeline script alongside
outputs. Input sources are matched and previewed in the dialog; multi-source
collections are paired by sorted position and must have equal counts.

The current release does not claim a complete saved batch configuration or
per-item provenance manifest. Retain your own input manifest, pairing rules,
checksums, exclusions, and run log for consequential analyses.

## Metadata boundary

VIPP carries an `ImageState` with supported axes, scale, units, source/channel
fields, and operation history where available. Individual operations transform
or preserve compatible fields. Readers, generic arrays, third-party formats,
or generated Python can have less information.

Never infer “metadata preserving” to mean bit-for-bit round-trip fidelity of
all acquisition metadata. Verify the fields your analysis needs.
