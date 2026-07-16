# Report a VIPP analysis

Readers should be able to identify the software, reconstruct the graph, find
the data, and understand which decisions or exclusions were manual.

## Methods checklist

Report:

- napari-vipp version (and commit for nightly/development builds);
- Python and important dependency versions or an environment file;
- workflow JSON and, if used, generated Python;
- input dataset identifiers, acquisition details, series selection, and axes;
- channel mapping, physical scale, and any metadata corrections;
- source checksums/identities and the source revision accepted at calculation;
- for multi-input nodes: how physical-grid alignment, scale, units, and origin
  were established, plus any explicit registration/resampling performed;
- node sequence, decisive parameter values, and 2D/3D handling;
- for automatic thresholds: method, stack/slice scope, and the saved float
  histogram-bin count where applicable; for Minimum, also the maximum smoothing
  iterations;
- for `Rescale Intensity` or `Clip`: percentile/data-range/explicit-value mode
  and its saved cutoffs;
- how non-finite source values were detected, justified, and handled when they
  occurred;
- tuning set, held-out validation set, reference annotation procedure, and
  quantitative metrics;
- manual calculations, exclusions, retries, and QC criteria;
- batch source pairing, naming, output formats, overwrite behavior, workflow and
  config hashes, manifest/run id, item/output statuses, retries, and partial or
  skipped outputs;
- location and license of data, workflows, code, validation artifacts, and
  output tables.

## Suggested concise wording

> Images were processed with napari-vipp 0.12.0a2 using the archived workflow
> JSON [identifier]. The workflow was developed on [development set] and frozen
> before evaluation on [held-out set]. Intermediate masks and labels were
> reviewed using predefined criteria [reference], and [metrics] were calculated
> against [reference annotations/phantoms].

An appropriate threshold detail could read: “The complete `float32` stack was
segmented with Otsu's method using 1,024 histogram bins; all finite pixels were
included and non-finite pixels were assigned to background.” Do not report the
inspector chart's display bins as the algorithm setting.

Adapt the text to what was actually done. Do not state that VIPP guarantees
reproducibility, metadata fidelity, or biological correctness.

## Archive an analysis bundle

Prefer a DOI-backed repository for final artifacts. Include:

```text
analysis/
  README.md
  environment.yml or requirements.txt
  workflow.json
  generated_pipeline.py        # if used
  vipp_batch_config.json        # if batch processing was used
  vipp_batch_manifest.json      # latest finalized run
  batch-manifest-archives/
  batch-item-sidecars/
  inputs-manifest.csv
  validation/
  qc/
  outputs/
```

Use checksums or persistent dataset identifiers when input images cannot be
redistributed. Review paths and metadata for confidential information before
deposit.

For a batch analysis, preserve the exact workflow/config pair and their hashes;
do not archive only the thin runner. Retain partial, skipped, and failed status
evidence as well as successful outputs. Sidecars are a recovery trail and
should be interpreted with the finalized manifest after an interruption.

## Cite VIPP

Use the current record in the application's `CITATION.cff`. Until a software
paper or DOI is available, cite the exact software release and repository URL
in addition to describing the workflow.
