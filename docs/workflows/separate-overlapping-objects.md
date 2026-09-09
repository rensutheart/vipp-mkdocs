# Separate overlapping objects

Follow one image through segmentation, binary logic and two coloured 3D meshes.
This is a worked synthetic example, not a general method for separating mixed
signals.

!!! note "Unreleased example"
    In nightly, open **Gear menu → Open example → Segmentation & Labels →
    Separate Overlapping Objects**, then **Calculate all**. No external files
    are needed. Six canvas notes follow the saved workflow from left to right.

## Follow the branches

1. **Prepare the image.** The sample contains a rounded object and a curved
   band in one grayscale ZYX image. Background subtraction, rescaling and
   non-local means denoising make their intensity differences easier to use.
2. **Separate the masks.** Compare Otsu on the denoised image with the
   **Gamma 4.247 → Otsu** branch that isolates the rounded object. **XOR**
   retains foreground present in exactly one mask, revealing the curve's
   fragments.
3. **Reconnect the curve.** Clean and dilate the XOR result. The lower
   **Gamma 10 → Rescale → Binary Threshold** branch supplies a cleaned bridge
   through the overlap. **OR** joins these masks.
4. **Finish the masks.** **Gaussian Blur 3D → Otsu → Erosion** refines the
   reconstructed curved band. Compare it with the rounded-object mask across
   Z slices, especially around their overlap.
5. **Inspect the surfaces.** Each **Mask to 3D Mesh** node creates one mesh.
   The two measurement nodes describe them separately. **Combine Meshes**
   retains both objects without geometric union; **Colour Mesh Objects** gives
   them distinct ID colours.

## Interpret and save the result

The authored cutoffs and morphology settings are specific to this sample.
Reconstruction changes boundaries and does not guarantee recovery of the
original shapes or disjoint masks. This is not channel unmixing.

The sample carries **0.45 µm spacing on Z, Y and X**. **Close at image border**
caps surfaces at the volume edges, affecting mesh volume measurements.

Both **Save Image** nodes are disabled, so **Calculate all** writes no files.
Use the inspector's **Save mesh…** action to export a chosen result; see
[mesh inspection and export](mask-to-mesh.md) for OBJ/3MF and unit limitations.
