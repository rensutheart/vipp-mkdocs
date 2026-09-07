# RACC-like index

Use **RACC Index** or **Masked RACC Index** for an intensity-relationship image,
not as a substitute for a reported metric table. See the
[colocalization tutorial](../workflows/colocalization-association.md) for setup.

## Dependency And Scope Statement

VIPP does not depend on the standalone RACC napari plugin. RACC is not listed
in `pyproject.toml`; the `RACC Index` and `Masked RACC Index` nodes use VIPP's
own implementation in `napari_vipp.core.operations`.

The VIPP RACC node should therefore be described as a VIPP-implemented
RACC-like index rather than as a wrapper around the external RACC plugin. The
standalone RACC plugin remains a separate package for its focused interactive
workflow. If future releases add direct RACC-plugin interoperation or extract a
shared numerical core, that dependency and any relevant license or patent
notices should be documented separately.

The overlap population `C` contains voxels meeting both native channel thresholds
within the selected ROI. See [threshold definitions](colocalization-metrics.md#thresholds-and-positive-sets).

## Calculation

The `RACC Index` and `Masked RACC Index` nodes calculate a scalar image over
the threshold-positive overlap set `C`. Voxels outside `C`, or outside the ROI
for masked analysis, are assigned zero.

The RACC-like calculation requires at least two voxels in `C`. VIPP fits a
positive Deming-style regression line through the overlap intensities:

```text
I2 = slope * I1 + intercept
```

The line is anchored between two points:

- `p0`, where the fitted line intersects the lower threshold boundary defined
  by `T1` and `T2`;
- `p1`, where the line intersects a common display/geometry extent. The extent
  retains the former 255 behavior for 8-bit-like data and expands to the joint
  native maximum when either input exceeds 255.

For every voxel in `C`, VIPP projects the intensity point `(I1, I2)` onto the
line from `p0` to `p1`, producing a fractional position `t`. It also measures
the perpendicular distance from the point to the line, normalized by the same
common extent.

The `include_percentile` parameter defines the high-intensity and distance
population used to scale the output. VIPP calculates:

- `t_max`, the selected quantile of projected positions;
- `pmax = p0 + t_max * (p1 - p0)`;
- `distance_threshold`, the selected quantile of normalized perpendicular
  distances.

The output value for each overlap voxel is then:

```text
value = min(t_to_pmax, 1) - distance_to_line * tan(theta)
```

Values are set to zero when `t_to_pmax <= 0` or when the normalized distance
is greater than `distance_threshold`, and the final result is clipped to
`[0, 1]`. The default output is `float32`; optional `uint8` output scales the
clipped result to `0..255`.

The `theta` parameter therefore controls how strongly off-axis points are
penalized. A larger angle applies a stronger distance penalty. The
`include_percentile` parameter limits the influence of extreme overlap
intensities and distances.

If the overlap set is too small, the regression line is degenerate, no
positive regression slope can be fit, or the percentile-based scale cannot be
calculated, VIPP raises an error instead of returning a misleading index.

Report `theta`, `include_percentile`, thresholds, preprocessing, ROI, spatial
scope, and output dtype. The supplied synthetic examples are regression and
demonstration data, not biological validation.
