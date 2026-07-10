# Documentation releases

The manual uses `mike` to publish several versions to the `gh-pages` branch.
GitHub Pages must be configured once to deploy from that branch at `/`.

## Automated channels

- A pull request or push to `main` runs `mkdocs build --strict`; pull requests
  retain the rendered `site/` as a seven-day preview artifact.
- A push to `main` deploys the **nightly** manual.
- A manual **Deploy versioned documentation** run publishes a numbered release
  and can move the **stable** alias/default.

The deployment job uses the exact versions in `requirements.txt` and the full
Git history needed by the revision-date plugin.

## Publish a release

Before moving `stable`:

1. Check out the manual content that matches the application release.
2. Update all explicit version facts, install commands, counts, examples,
   validation status, and compatibility notes.
3. Replace screenshots with captures from the same release.
4. Run `mkdocs build --strict` and visually review key pages.
5. In GitHub Actions, run **Deploy versioned documentation** with a version such
   as `0.11.0a1` and `make_stable=true`.
6. Open the public site, select both the numbered release and `stable`, then
   verify installation, search, code highlighting, redirects, and images.

The workflow executes the equivalent of:

```text
mike deploy --push --update-aliases 0.11.0a1 stable
mike set-default --push stable
```

Never overwrite an old numbered manual with content for a different software
release. Correct a serious documentation error with a transparent follow-up and
record it in the repository history.

## Preview versioned output locally

```text
mike deploy 0.11.0a1 stable
mike deploy nightly
mike serve
```

Do not push the generated `site/` directory; `mike` manages versioned content in
the deployment branch.
