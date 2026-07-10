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
- node sequence, decisive parameter values, and 2D/3D handling;
- tuning set, held-out validation set, reference annotation procedure, and
  quantitative metrics;
- manual calculations, exclusions, retries, and QC criteria;
- batch source pairing, naming, output formats, and overwrite behavior;
- location and license of data, workflows, code, validation artifacts, and
  output tables.

## Suggested concise wording

> Images were processed with napari-vipp 0.11.0a1 using the archived workflow
> JSON [identifier]. The workflow was developed on [development set] and frozen
> before evaluation on [held-out set]. Intermediate masks and labels were
> reviewed using predefined criteria [reference], and [metrics] were calculated
> against [reference annotations/phantoms].

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
  inputs-manifest.csv
  validation/
  qc/
  outputs/
```

Use checksums or persistent dataset identifiers when input images cannot be
redistributed. Review paths and metadata for confidential information before
deposit.

## Cite VIPP

Use the current record in the application's `CITATION.cff`. Until a software
paper or DOI is available, cite the exact software release and repository URL
in addition to describing the workflow.
