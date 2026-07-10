# Report a problem

Search existing [napari-vipp issues](https://github.com/rensutheart/napari-vipp/issues)
before opening a new report. A small reproducible case is more useful than a
large private dataset or an unexplained screenshot.

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

Get the core versions with:

```text
python -c "import importlib.metadata as m, sys; print(sys.version); print('napari-vipp', m.version('napari-vipp')); print('napari', m.version('napari'))"
```

## Protect data and identities

Do not attach patient/research-participant data, credentials, restricted image
metadata, identifiable paths, or unpublished results. Reproduce with a bundled
sample, crop/synthetic phantom, or a privately shared artifact only after an
appropriate route is agreed.

Review workflow JSON and screenshots: paths, source names, graph notes, metadata
columns, window titles, and recent-file dialogs can reveal sensitive context.

## Security problems

Do not disclose a credible vulnerability in a public issue before checking the
application repository's security policy. Use its private reporting route where
available.
