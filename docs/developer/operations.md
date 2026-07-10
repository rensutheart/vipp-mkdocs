# Add or change an operation

An operation is more than a numerical function. A complete contribution aligns
the headless implementation, registry contract, graph behavior, metadata,
interactive inspection, export, examples, and tests.

## Design first

Specify:

- scientific purpose and evidence for the method;
- input and output semantic types;
- axis and 2D/3D behavior;
- dtype/range behavior and empty/degenerate cases;
- metadata fields preserved, changed, inferred, or dropped;
- execution policy (`auto` or `manual`) and cancellation/progress needs;
- expected memory scaling;
- parameters, defaults, bounds, units, and invalid combinations.

Avoid adding a near-duplicate operation only to expand the node count. Prefer a
clear focused node when a selector would hide materially different methods or
parameter meanings.

## Implementation checklist

1. Add or revise the headless operation under `napari_vipp.core`.
2. Register an `OperationSpec` with a stable ID, title, category, typed ports,
   parameters, execution policy, and stack-processing note.
3. Define static or dynamic outputs explicitly; test saved-workflow restoration
   when the number of ports depends on runtime data.
4. Transform `ImageState` or `TableState` deliberately.
5. Keep Python export and batch execution aligned with interactive semantics, or
   reject unsupported graphs with a clear error.
6. Add focused operation, pipeline, persistence, export, and UI tests in
   proportion to risk.
7. Add a deterministic sample/example only when it teaches or validates a
   stable capability.
8. Update the node reference, workflow guides, validation status, and release
   notes.

## Scientific tests

Test invariants with simple truth: uniform images, single objects, known
geometries, explicit axes/scale, empty masks, boundary-touching objects, and
small arrays. Numerical equality to the same underlying library call is useful
but not independent validation of the scientific claim.

For multi-input operations test shape/axis incompatibility and port ordering.
For tables test identity columns, units, missing values, and merge behavior—not
only that a table object was returned.
