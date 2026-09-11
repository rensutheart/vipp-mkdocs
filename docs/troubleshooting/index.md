# Troubleshooting

Start with the earliest stage that differs from expectation. Changing the final
measurement rarely fixes a wrong channel, axis interpretation, threshold mask,
or label image.

| Symptom | Start here |
| --- | --- |
| Wrong objects, counts, channels, units, or stale tables | [Common problems](common-pitfalls.md) |
| Slow interaction or high RAM use | [Performance and memory](performance.md) |
| Auto/Prefer GPU/Custom uses CPU, GPU setup fails, or optimizer progress pauses | [Choose and verify CPU or GPU compute](../how-to/choose-compute.md) |
| Installation/plugin discovery problem | [Install VIPP](../getting-started/installation.md) |
| Question, reproducible bug, or missing behavior | [Get help or report a problem](report-a-problem.md) |

Before debugging your own file, open the matching bundled example. If the
example works, compare source type, axes, scale, dtype, channel mapping, shape,
and release version. If the example fails, capture the exact error and version
without changing multiple settings at once.

## A result appears, but its display reports a problem

**Unreleased (after 0.15.0a4):** a short **Result calculated** warning means
the calculation finished, but the napari view could not fully update. Reselect
the node to retry its display. You do not need to recalculate the mesh just to
clear the message.

Use **Details…** to view and copy the technical message, or **Dismiss** to hide
the warning without changing results or node errors. If it returns, include
those details and your VIPP version when [reporting the problem](report-a-problem.md).
