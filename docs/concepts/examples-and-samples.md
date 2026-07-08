# Examples And Samples

VIPP needs two different kinds of examples. Keeping them separate prevents the
documentation from becoming confused.

Use this rule of thumb:

- samples are data sources selected in `Image Source > Source = sample`;
- example workflows are runnable graph templates opened with `Open example...`.

## Core System Samples

Core samples ship with the plugin. They should be deterministic, small enough
for tests, and useful for regression checks.

Core samples are appropriate when they:

- validate a feature;
- are used by tests;
- support a checked-in workflow;
- document a stable capability;
- avoid license or privacy problems.

Examples:

- synthetic multichannel volume;
- measurement summary sample with known object counts;
- 3D mesh morphology phantom;
- skeleton network sample;
- colocalization sample;
- synthetic deconvolution image and PSF.

## Core Example Workflows

Core workflows ship with the repository. They should load and run in automated
tests and demonstrate a stable workflow family.

Examples:

- object measurement with intensity;
- table merge and metadata columns;
- 3D mesh morphology;
- skeleton QC;
- colocalization and object association;
- PSF-aware deconvolution.

## Documentation Examples

Documentation examples exist to teach users. They may be lighter, more visual,
or more step-by-step than core tests.

Use documentation examples when:

- a concept needs a simple visual explanation;
- the sample is too tutorial-specific for the plugin;
- the workflow is not stable enough for automated regression;
- screenshots are the main artifact.

Documentation examples can later graduate into core examples if they become
stable and scientifically important.

## Graduation Criteria

A documentation example should become a core system example when it has:

- deterministic input data;
- a checked-in workflow JSON file;
- at least one automated test assertion;
- a row in the example workflow reference;
- clear user-facing purpose;
- stable expected outputs.
