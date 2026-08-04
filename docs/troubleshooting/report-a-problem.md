# Get help or report a problem

Choose the route that matches what you need. Keeping questions separate from
trackable defects makes both easier to find later.

| Route | Best for |
| --- | --- |
| [GitHub Issues](https://github.com/rensutheart/napari-vipp/issues/new/choose) | Reproducible defects, incorrect documentation, and focused feature requests. Search [existing issues](https://github.com/rensutheart/napari-vipp/issues) first. |
| [GitHub Discussions](https://github.com/rensutheart/napari-vipp/discussions) | Installation help, workflow design questions, ideas, and examples that may help other VIPP users. |
| [image.sc — napari](https://forum.image.sc/tag/napari) | Broader bioimage-analysis and scientific-method questions that benefit from the wider community. Put `napari-vipp` and its version in the title or opening paragraph. |
| [Private security reporting](https://github.com/rensutheart/napari-vipp/security/policy) | A credible vulnerability or sensitive security detail that should not be public. |

If a discussion reveals a reproducible software defect, link it from a focused
GitHub issue. A small reproducible case is more useful than a large private
dataset or an unexplained screenshot.

## Include

- napari-vipp, napari, Python, and operating-system versions;
- whether the build came from PyPI, a tag, or a commit;
- the smallest workflow JSON that reproduces the problem;
- exact steps from a new napari session;
- expected and observed behavior;
- complete traceback as text;
- source shape, axes, dtype, scale/unit, and format;
- whether a bundled sample reproduces it;
- for a numerical problem, a tiny synthetic array and expected invariant.
- for compute/GPU behavior: requested mode, node badge/decision reason, fallback
  policy, provider/device, `vipp-compute-doctor` output, and the relevant
  execution report or redacted provenance sidecar;
- for optimizer behavior: node/provider stage, both progress values, time
  limit, completed/remaining comparisons, and whether exact evidence was reused;
- for ND2 T/Z/C behavior: ordered shape/axes reported by the reader, which
  slider is missing or wrong, and a minimal non-sensitive file when possible.

Get the core versions with:

```text
python -c "import importlib.metadata as m, sys; print(sys.version); print('napari-vipp', m.version('napari-vipp')); print('napari', m.version('napari'))"
```

For an optional CUDA environment also run:

```text
vipp-compute-doctor --track cuda13
```

Review its output before posting: local paths, host/device names, and
environment details can be identifying. Do not attach a full batch manifest or
workflow until source paths and metadata have been redacted.

## Protect data and identities

Do not attach patient/research-participant data, credentials, restricted image
metadata, identifiable paths, or unpublished results. Reproduce with a bundled
sample, crop/synthetic phantom, or a privately shared artifact only after an
appropriate route is agreed.

Review workflow JSON and screenshots: paths, source names, graph notes, metadata
columns, window titles, and recent-file dialogs can reveal sensitive context.

## Security problems

Do not disclose a credible vulnerability in an Issue, Discussion, or image.sc
topic. Follow the application repository's [security
policy](https://github.com/rensutheart/napari-vipp/security/policy) and use its
private reporting route.
