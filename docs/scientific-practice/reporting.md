# Report a VIPP analysis

Readers should be able to identify the software, reconstruct the graph, find
the data, and understand which decisions or exclusions were manual.

## Methods checklist

Report:

- napari-vipp version (and commit for nightly/development builds);
- exact GPU model and compute capability, NVIDIA driver, CUDA driver/runtime
  and toolkit-package versions, and compiler/JIT-relevant provider versions
  whenever acceleration was used;
- Python and important dependency versions or an environment file;
- workflow JSON and, if used, generated Python;
- authored compute mode and per-node preferences, plus the actual CPU/CuPy/
  cuCIM implementation IDs/versions, environment fingerprint, fallback/OOM
  records, and cleanup outcome from execution provenance;
- any explicit optimizer locks, exact-workload benchmark/assignment used, and
  whether a time limit left alternatives unmeasured;
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
- every explicit dtype conversion and its preserve/rescale policy, especially
  when it enabled a floating-point GPU region;
- for colocalization: native intensity units, threshold mode/values, ROI,
  canonical Pearson/Manders column names, `coloc_semantics`, and
  `coloc_validation_status`;
- how non-finite source values were detected, justified, and handled when they
  occurred;
- tuning set, held-out validation set, reference annotation procedure, and
  quantitative metrics;
- manual calculations, exclusions, retries, and QC criteria;
- batch source pairing, naming, output formats, overwrite behavior, workflow and
  config/effective-request hashes, manifest/run id, item execution digests,
  cancellation, item/output statuses, retries, and partial, skipped, cancelled,
  or failed outputs;
- location and license of data, workflows, code, validation artifacts, and
  output tables.

## Suggested concise wording

> Images were processed with napari-vipp 0.13.0a5 using the archived workflow
> JSON [identifier]. The workflow was developed on [development set] and frozen
> before evaluation on [held-out set]. Intermediate masks and labels were
> reviewed using predefined criteria [reference], and [metrics] were calculated
> against [reference annotations/phantoms].

For an accelerated run, add wording such as: “The saved workflow requested
Prefer GPU compute. The archived execution report records CuPy implementation
`[ID/version]` on `[device/environment]` for `[nodes]`, CPU for `[nodes]`, and
`[no fallbacks / classified fallback details]`.” Do not report “GPU analysis”
from toolbar intent alone.

Compatible GPU models can produce minor floating-point differences because of
hardware, driver, compiler-path, or reduction-order changes. Report the exact
environment, preserve the execution report, and state how the accelerated
result was compared with the CPU reference on representative data. Bitwise
contracts remain bitwise where the implementation explicitly promises them.

If Custom was used, also report the authored per-node choices or applied
optimizer assignment. Prefer GPU means accelerator placement regardless of
speed; it is not a claim that GPU was faster.

If a generated CLI wrote outputs, retain whether provenance was enabled and the
atomic sibling sidecars. For batch, retain the finalized version-3 manifest and
execution digests rather than reconstructing implementation choices from card
badges or screenshots. When a source-axis declaration was used, report the raw
axes, effective axes, and how the interpretation was verified.

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
