# Troubleshooting

Start with the earliest stage that differs from expectation. Changing the final
measurement rarely fixes a wrong channel, axis interpretation, threshold mask,
or label image.

| Symptom | Start here |
| --- | --- |
| Wrong objects, counts, channels, units, or stale tables | [Common problems](common-pitfalls.md) |
| Slow interaction or high RAM use | [Performance and memory](performance.md) |
| Installation/plugin discovery problem | [Install VIPP](../getting-started/installation.md) |
| Reproducible bug or missing behavior | [Report a problem](report-a-problem.md) |

Before debugging your own file, open the matching bundled example. If the
example works, compare source type, axes, scale, dtype, channel mapping, shape,
and release version. If the example fails, capture the exact error and version
without changing multiple settings at once.
