# Contributor guide

Contributions that improve correctness, scientific clarity, accessibility,
tests, examples, or documentation are welcome. The application and manual are
maintained in separate repositories:

| Repository | Scope |
| --- | --- |
| [`napari-vipp`](https://github.com/rensutheart/napari-vipp) | Application, operation registry, examples, tests, release metadata |
| [`vipp-mkdocs`](https://github.com/rensutheart/vipp-mkdocs) | Public, versioned user manual |

Publication plans, private datasets, ethics material, unpublished results, and
internal screenshot roadmaps do not belong in either public manual page.

## Pick a contribution path

- [Set up a development environment](development-setup.md)
- [Add or change an operation](operations.md)
- [Test and document changes](testing-docs.md)
- [Publish versioned documentation](docs-releases.md)

## Principles

1. **Correctness before breadth.** A smaller validated node is preferable to a
   broad claim with unclear behavior.
2. **Metadata claims are field-specific.** State exactly which axes, scale,
   units, channels, or history are transformed or retained.
3. **Graph examples must be executable.** Core JSON examples use bundled
   deterministic samples and have focused assertions.
4. **UI labels and docs move together.** Search the manual for changed labels,
   defaults, node titles, formats, and version references.
5. **Scientific limitations are user-facing behavior.** Put material caveats
   beside the task, not only in an internal roadmap.

Before opening a pull request, describe the user-visible outcome, tests run,
scientific assumptions, compatibility impact, and documentation changes.
