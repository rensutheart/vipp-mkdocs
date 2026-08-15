# Documentation releases

The manual uses `mike` to publish `nightly`, numbered versions, and the
`stable` alias from the `gh-pages` branch.

## Principle

Documentation follows the same risk-based release model as the application:

- inspect pages whose behavior or instructions changed;
- rely on the strict documentation CI build for the whole site;
- publish one timeless release page rather than a sequence of “pending”,
  “now public”, and “stable promoted” status edits; and
- keep workflow run IDs, transient test counts, and duplicated asset hashes in
  machine-readable release evidence rather than prose.

A version-only change does not require recapturing unchanged screenshots,
rechecking every guide, or replaying installer/GPU qualification.

## Automated channels

- A pull request or push to `main` runs `mkdocs build --strict`; pull requests
  retain the rendered site as a short-lived preview artifact.
- A push to `main` deploys the `nightly` manual.
- A manual **Deploy versioned documentation** run publishes a numbered version
  and can move the `stable` alias/default in the same run.

## Iterative alpha

Use one documentation PR and one post-package deployment:

1. Update the release page, current-version installation examples, and only
   the guides affected by the release.
2. Use timeless wording. Link the canonical GitHub release, PyPI page, assets
   actually shipped, and validation boundary; do not say that a tag or
   publication is “pending”. The page is not deployed as a numbered version
   until those links are live.
3. Let the pull-request build validate all navigation and internal links.
   Manually inspect the changed pages and any changed screenshots.
4. Merge the documentation PR before or with the application release.
5. After the GitHub release and PyPI version are public, run **Deploy versioned
   documentation** once with the target version and `make_stable=true` when
   that alpha should be the default manual.
6. Verify the numbered home page, `stable`, and the changed pages. Stop; do not
   create a second evidence-only PR to record the deployment that just ran.

If an alpha should not become the default manual, use `make_stable=false`.

## Release candidate and stable production

An RC receives broader review of installation, upgrade, compatibility, and the
combined user journey. It may first deploy with `make_stable=false` when users
need a preview without changing the default manual.

For a production release, promote an unchanged, reviewed RC snapshot where
possible. Deploy the final numbered version and move `stable` only after the
matching package is public. If production behavior or documentation changes
after the RC, review those changed pages and publish another candidate rather
than silently editing the final snapshot.

Never overwrite an old numbered manual with content for a different software
release. Correct a serious documentation error with a transparent follow-up
commit and redeployment.

## Deployment

```text
gh workflow run docs-deploy.yml \
  --repo rensutheart/vipp-mkdocs \
  --ref main \
  -f version="<version>" \
  -f make_stable=true
```

The workflow executes the equivalent of:

```text
mike deploy --push --update-aliases <version> stable
mike set-default --push stable
```

For a numbered preview without alias promotion, use `make_stable=false`, which
executes `mike deploy --push <version>`.

## Local preview

```text
mike deploy <version> stable
mike deploy nightly
mike serve
```

Do not push the generated `site/` directory; `mike` manages versioned content
in the deployment branch.
