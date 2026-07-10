# Test and document changes

## Test in layers

Run the smallest relevant test while developing, then the required repository
checks before handoff:

```text
python -m npe2 validate src/napari_vipp/napari.yaml
python -m ruff check .
python -m pytest
```

High-risk changes need more than a happy-path unit test. Consider:

- invalid/empty/minimal inputs;
- 2D, 3D, leading axes, and anisotropic scale;
- dynamic and multi-output persistence;
- manual-node stale/current transitions;
- generated Python compiling and running;
- I/O round trips for supported fields and dtypes;
- cancellation, memory retention, and repeated UI actions;
- bundled examples reopening and satisfying a meaningful invariant.

Prefer a small parameterized test over many near-identical cases. Keep an
end-to-end UI test only when it protects behavior that cannot be established at
a lower layer.

## Update the manual

Write for the user's task first. Put exact lists and settings in reference;
explain scientific decisions in the task page where they occur. Qualify claims
about validation, metadata, scalability, batch provenance, and compatibility.

For UI images:

- use bundled synthetic or clearly licensed public data;
- use the dark napari theme and the documented release;
- show VIPP undocked and large for workflow context;
- crop to the relevant graph portion for a concept or control;
- include the napari viewer for high-resolution/3D scientific inspection;
- remove paths, private metadata, tooltips, clipping, and transient state;
- write alt text and a caption that tells the reader what to notice.

Run `mkdocs build --strict` and inspect both light and dark manual themes at
desktop and narrow widths. Follow links from the page, not only search results.

## Keep reference counts honest

The node and example counts are release facts. When the registries change,
regenerate/compare the public lists and update counts in the same change. Do not
claim a parameter-level generated reference unless the build actually checks it
against the registry.
