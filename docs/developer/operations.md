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

## Add a CPU/GPU vertical slice

An accelerated function is not complete merely because it imports or runs on a
GPU. For each public region:

1. Keep the established CPU operation, defaults, axes, dtype, boundary,
   rounding, overflow, and error behavior authoritative.
2. Declare a stable implementation/library/runtime identity and versioned
   parameter, workload, parity, memory, boundary, precision, progress, and
   cancellation policy IDs.
3. Keep optional provider imports lazy so CPU-only plugin discovery, workflow
   loading, and execution remain safe without CUDA packages.
4. Derive eligibility from detached exact workload facts. Reject unsupported
   dtypes, shapes, parameters, and environments visibly; never synthesize a cast
   or alter an authored parameter to pass admission.
5. Define residency and every host boundary, including ordered inputs,
   multi-output behavior, and any exact typed host-table finalizer.
6. Bound device memory conservatively and classify runtime OOM separately from
   availability, eligibility, parity, and other device faults.
7. Report only synchronized progress checkpoints; make cancellation
   cooperative at those boundaries and prove cleanup after success, rejection,
   cancellation, error, OOM, and benchmarking.
8. Carry exact implementation, environment, decision, fallback, memory, and
   cleanup provenance through interactive, batch, generated Python/CLI, and
   export execution.
9. Promote only the reviewed region as a public provider/Selective choice.
   Auto additionally requires explicit validated performance evidence; standard
   0.13.0a1 execution does not synthesize or persist that evidence. Broader CPU
   behavior remains first-class and must not be described as a failed GPU
   feature.

## Scientific tests

Test invariants with simple truth: uniform images, single objects, known
geometries, explicit axes/scale, empty masks, boundary-touching objects, and
small arrays. Numerical equality to the same underlying library call is useful
but not independent validation of the scientific claim.

For multi-input operations test shape/axis incompatibility and port ordering.
For tables test identity columns, units, missing values, and merge behavior—not
only that a table object was returned.
