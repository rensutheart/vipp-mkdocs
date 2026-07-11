# VIPP — Visual Image Processing Platform

**A visual workflow platform for reproducible bioimage analysis.**

This repository contains the public, searchable manual for VIPP, the **Visual
Image Processing Platform**, distributed for napari as
[`napari-vipp`](https://github.com/rensutheart/napari-vipp). The manual is
separate from the application repository so documentation releases and the
software release cycle can be managed independently.

## Preview locally

```powershell
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install -r requirements.txt
mkdocs serve
```

On macOS or Linux, activate with `source .venv/bin/activate`. Open the local URL
printed by MkDocs. A production-equivalent check is:

```text
mkdocs build --strict
```

## Versions

The site uses [mike](https://github.com/jimporter/mike):

- **stable** points to the manual for the current supported release;
- **nightly** is rebuilt from the documentation `main` branch;
- release-numbered snapshots remain available for older workflows.

See `docs/developer/docs-releases.md` for the deployment procedure. Publication
plans, manuscripts, private datasets, and internal screenshot roadmaps do not
belong in this repository.

## Licensing

The manual's original prose and screenshots are licensed under [Creative
Commons Attribution 4.0 International](LICENSE.md). The napari-vipp application
and source-code excerpts from it remain separately licensed under the [BSD
3-Clause License](https://github.com/rensutheart/napari-vipp/blob/main/LICENSE).
See the manual's [licence and reuse guide](docs/reference/license.md) for scope
and an attribution example.

## Support

- Use [GitHub Issues](https://github.com/rensutheart/napari-vipp/issues) for
  reproducible defects, documentation errors, and focused feature requests.
- Use [GitHub Discussions](https://github.com/rensutheart/napari-vipp/discussions)
  for installation help, workflow questions, ideas, and reusable examples.
- Use the [napari category on image.sc](https://forum.image.sc/tag/napari) for
  broader bioimage-analysis and method questions.

The [support guide](docs/troubleshooting/report-a-problem.md) explains what to
include and how to avoid disclosing restricted data.

## Privacy

The site configures no audience analytics or marketing trackers, uses system
fonts, and bundles externally referenced theme assets at build time. See the
[privacy page](docs/reference/privacy.md) for browser and hosting details.
