# Choose 2D or 3D

Dimensionality changes object identity, topology, morphology, distance, and
computation time. Choose it from the scientific object and acquisition—not from
which setting produces a preferred count.

## Decision guide

| Question | Prefer 2D / per-slice | Prefer true 3D |
| --- | --- | --- |
| What is acquired? | Independent fields or sections | A sampled volume of the same structures |
| What defines one object? | Identity should not cross slices | Identity may extend through z |
| Is z sampling adequate? | Sparse/irregular or effectively independent | Calibrated and sufficient for the target scale |
| What is reported? | Planar area, per-section count | Volume, 3D surface, spatial topology, 3D distance |
| Main risk | Double-counting one structure across slices | Joining unrelated structures across z |

## Verify axes and calibration

For a nominal `ZYX` volume, confirm that `Z` is actually depth and that z-step,
x/y pixel size, and units refer to the same physical space. Anisotropic pixels
are common and affect distance, surface, rescaling, and visual interpretation.

Do not repair axes or scale by trial and error. Use acquisition records or a
known calibration source, then document the correction with
`Set Pixel Size / Units` or `Reorder Axes`.

## Keep processing dimensionality consistent

A mixed workflow can be valid—for example, per-slice denoising followed by 3D
connected components—but each switch needs a reason. Inspect the operation's
spatial processing setting and its metadata note. Confirm that:

- local thresholds use the intended neighborhood;
- hole filling and morphology connect the intended dimensions;
- labels represent the intended object identity;
- skeleton/network analysis uses appropriate connectivity;
- the PSF dimensionality matches the deconvolution mode.

## Report it

State the input axes, spatial sampling, processing dimensionality for decisive
steps, and whether leading time/channel axes were processed independently.
