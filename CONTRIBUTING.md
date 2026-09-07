# Writing the VIPP manual

The manual owns public instructions. Keep implementation plans, code-level
contracts, test evidence, and release procedures in napari-vipp; link to those
records when engineering detail is useful. Do not duplicate a user guide there.

## Make the next action clear

- Start with what the page helps the reader do.
- Use numbered steps for procedures and short paragraphs for explanations.
- Use a compact table when comparing choices or defining output fields.
- Give a setting's effect and when to choose it, not just its internal name.
- Keep essential warnings beside the decision. Do not hide scientific caveats
  in a collapsed technical section.
- Put optional formulas, field schemas, and edge cases in focused reference
  pages linked from the tutorial. Long detail is appropriate when precision
  requires it, not as a substitute for organization.
- Link to an existing explanation instead of repeating it in several pages.
- Remove temporary status updates and development history from task guides.
- Keep retired alpha-provider details in release history or a brief linked
  historical note. Avoid repeated migration tables and warnings about obsolete
  installers in current guides unless they address a current user need.

## Match the software

- Verify UI labels, defaults, formats, and limits against the relevant code.
- Mark unreleased behavior explicitly in `nightly`; never imply it shipped in
  a numbered release. Preserve older numbered manuals.
- Distinguish tests, source-aligned compatibility, independent validation,
  and biological validity. Do not strengthen a claim while shortening it.
- Keep executable example JSON and fixture acceptance checks in napari-vipp.
  The manual owns their user-facing walkthroughs and screenshots.

## Check the change

1. Link new pages from `mkdocs.yml` and the relevant topic index/tutorial.
2. Run `python scripts/check_manual.py` and `mkdocs build --strict`.
3. With both checkouts, run
   `python scripts/check_manual.py --application-repo ../napari-vipp`.
4. Inspect changed pages at desktop and narrow widths, including links and
   light/dark readability. Follow the
   [screenshot checklist](docs/developer/testing-docs.md#update-the-manual).
5. Link the related application change in the documentation PR.

The [release procedure](docs/developer/docs-releases.md) controls publication;
a successful local build does not mean the online manual has been updated.
