# Validation Status

This page separates evidence-backed claims from planned or future claims.

## Evidence-Backed Now

Current evidence includes:

- automated tests for graph behavior, workflow persistence, preview, export,
  operations, widget behavior, I/O, and example workflows;
- deterministic synthetic samples;
- checked-in workflow JSON files;
- analytical phantom validation for calibrated object and mesh morphology;
- method documentation and tests for colocalization calculations;
- table outputs and CSV/TSV saving;
- workflow JSON and Python export.

The calibrated morphology validation report currently records:

```text
28 checks
28 passed
Status: PASS
```

## Strong Claims To Avoid Until Further Validation

Do not claim yet:

- broad usability superiority over other tools;
- numerical equivalence to Fiji, CellProfiler, scikit-image, or other packages
  across a broad benchmark corpus;
- scalability to very large whole-slide or HCS data;
- complete OME metadata fidelity;
- biological validity of a segmentation or measurement workflow;
- user-study evidence beyond pilot observations.

## Planned Validation Packs

High-value future validation reports:

- watershed and touching-object separation;
- colocalization deterministic overlap scenarios;
- object association, nearest distance, and event localization;
- skeleton/network topology and branch-length checks;
- OME-TIFF and OME-Zarr round trips;
- real PSF/deconvolution examples;
- real microscope file import metadata checks.

## Publication Use

Use this page to decide what can be stated in a paper, documentation page, or
release note. If a claim is not evidence-backed, label it as planned,
experimental, or future work.

