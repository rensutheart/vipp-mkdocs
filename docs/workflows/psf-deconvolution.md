# PSF And Deconvolution

!!! warning "Experimental / next-release area"
    PSF generation and Richardson-Lucy deconvolution are implemented in the
    current working tree, but should be documented as experimental unless they
    are included in the release you are using.

PSF-aware restoration workflows use point-spread functions as ordinary graph
images. This makes the PSF inspectable before deconvolution.

## Measured PSF Workflow

```text
Image Source
PSF Image Source
  -> Prepare / Validate PSF
  -> Richardson-Lucy Deconvolution
  -> Richardson-Lucy TV Deconvolution
```

## Generated PSF Workflow

```text
Image Source
  -> Born-Wolf PSF
  -> Prepare / Validate PSF
  -> Richardson-Lucy TV Deconvolution
```

`Born-Wolf PSF` can use image metadata such as pixel size, z-step, channel, and
objective metadata when available.

## Why Prepare The PSF Separately?

`Prepare / Validate PSF` can:

- clip negative values;
- center the peak or centroid;
- normalize the PSF sum;
- force odd shape;
- reject invalid kernels.

Keeping this as a visible node lets users inspect the PSF before running an
expensive restoration.

## Reference Workflows

| Workflow | Purpose |
| --- | --- |
| `synthetic-deconvolution-rl-tv.json` | 2D measured-PSF workflow with ordinary Richardson-Lucy and RL-TV side by side. |
| `synthetic-3d-deconvolution-rl-tv.json` | 3D measured-PSF workflow with ZYX deconvolution. |

## What To Check

- Is the PSF dimensionality compatible with the image processing mode?
- Is the PSF centered and normalized?
- Are pixel sizes and z-step correct?
- Does deconvolution amplify noise or edge artifacts?
- Are iteration count and TV regularization conservative?

## Validation Status

Synthetic workflows and tests exist. Real bead-PSF and microscopy-image
validation should be added before positioning restoration as publication-ready.

