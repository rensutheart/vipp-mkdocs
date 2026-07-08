# Segmentation And Label Cleanup

Segmentation workflows usually turn an intensity image into a mask, then into
labels.

## Basic Pattern

```text
Image Source
  -> Extract Channel or Split Channels
  -> optional background correction / denoising
  -> threshold
  -> morphology cleanup
  -> Label Connected Components
  -> label filtering
```

## Recommended First Graph

```text
Image Source
  -> Split Channels
  -> Gaussian Blur
  -> Otsu Threshold
  -> Fill Holes
  -> Remove Small Objects
  -> Label Connected Components
  -> Filter Labels By Volume
```

## Key Nodes

| Step | Common nodes |
| --- | --- |
| Channel selection | `Extract Channel`, `Split Channels` |
| Smoothing | `Gaussian Blur`, `Gaussian Blur 3D`, `Median Filter`, `Non-Local Means` |
| Background | `Rolling-Ball Background`, `Subtract Background` |
| Threshold | `Otsu Threshold`, `Triangle Threshold`, `Li Threshold`, `Yen Threshold`, `Binary Threshold`, local threshold nodes |
| Mask cleanup | `Fill Holes`, `Remove Small Objects`, morphology nodes |
| Label creation | `Label Connected Components`, watershed nodes |
| Label cleanup | `Clear Border Objects`, `Filter Labels By Volume`, `Filter Labels By Property`, `Relabel Sequential` |

## 2D Versus 3D

For z-stacks, decide whether objects should be connected across `Z`.

- Use 2D processing when each `YX` plane should be independent.
- Use 3D processing when the object exists as one `ZYX` volume.
- Use `Auto from axes` only after checking that VIPP has interpreted the axes
  correctly.

## Split Touching Objects

Use watershed when simple connected components merge neighboring objects:

```text
mask
  -> Euclidean Distance Transform
  -> H-Maxima Markers
  -> Marker-Controlled Watershed
  -> Filter Labels By Volume
```

For a compact single-node starting point, use `Auto Watershed From Mask`.

## Reference Workflow

Use:

```text
examples/otsu-red-channel-labels.json
```

This demonstrates red/TRITC-like channel segmentation, mask cleanup, labels,
border clearing, volume filtering, and inspectable outputs.

## What To Check

- Does the mask include the biology of interest?
- Are background/noise structures being labeled as objects?
- Are touching objects merged?
- Are small objects biological or artifacts?
- Are physical units correct before size filtering or measurement?
