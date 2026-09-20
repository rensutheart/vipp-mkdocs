# Reproduce the statistics-paper compartments

Build the supplied CellProfiler nuclei/cell/cytoplasm analysis in VIPP, then
compare measurements on identified image fields. The workflow follows
[Marcotti and colleagues' statistics paper](https://doi.org/10.1242/jcs.264367)
and its executable author pipeline. Its scientific target is a per-cell
relative nuclear-localisation measurement.

!!! info "Unreleased"
    This workflow uses new CellProfiler profile nodes documented for nightly
    development. They are not available in 0.15.0a5.

!!! warning "Keep the comparison target explicit"
    Agreement with the original CellProfiler 4.2.6 runtime on the same inputs
    checks VIPP's implementation. Reproducing the paper's exported measurements
    also requires matching the authors' original image pixels and cohort.
    Current acquired-image reruns do not yet establish full published-result
    equality. Preserve discrepancies instead of tuning settings to conceal them.

## Prepare the three stains

Use a nuclear stain, Actin and the protein being measured. Keep the protein
image unsmoothed for measurement. Select a single **YX** plane from each input
and verify matching physical grids.

| Dataset | Nuclear stain | Cell guidance | Measured protein |
| --- | --- | --- | --- |
| IDR0139 | DNA / DAPI, acquisition **A01** | Actin, **A03** | Fascin, **A02** |
| IDR0028 | Hoechst, TIFF frame **0** | Actin, frame **2** | YAP/TAZ, frame **3** |

IDR0139's filename suffix **C04** belongs to Actin A03; C03 belongs to a
separate NuclearActin A04 stain. Use the acquisition mapping above. IDR0028's
four TIFF frames are stain channels, even when a reader describes them as four
time frames. Review axes explicitly before selecting planes.

Add **Convert Dtype**, choose **float32**, and preserve the input intensity
values. Follow it with **Rescale Intensity**: choose explicit **Values**, input
limits **0** and **65535**, output limits **0** and **1**, with inversion
disabled. This conversion matches CellProfiler's float32 division across the
full uint16 range. You can apply it to a multichannel stack before extracting
stains. Do not stretch each image's observed range or use display contrast as
the scientific normalization. Retain the raw input files.

## Connect the compartment stages

1. Add **Smooth — CellProfiler Gaussian** to the nuclear image and a second
   instance to Actin. Set **Artifact diameter (pixels)** to **2** for both.
2. Connect smoothed nuclear intensity to **Segment Nuclei — CellProfiler
   Shape**. Keep **Minimum diameter (pixels): 15**, **Maximum diameter
   (pixels): 50** and **Threshold smoothing scale: 1.3488**. Click
   **Calculate**. Inspect both **Retained nuclei** and **Before filtering**.
3. Connect smoothed Actin to **Threshold — CellProfiler Minimum Cross-Entropy**.
   Keep **Threshold smoothing scale: 0**. Inspect the Boolean foreground mask.
4. Add **Prepare Seeds — CellProfiler Propagation**. Connect the nuclear
   **Before filtering** output to its matching port and **Retained nuclei** to
   its matching port. The output intentionally includes excluded border nuclei
   while neighbouring cells compete for pixels.
5. Add **Grow Regions from Seeds — CellProfiler Propagation**. Connect smoothed
   Actin to **Guidance image**, prepared seeds to **Seed labels** and the Actin
   threshold mask to **Foreground mask**. Keep **Distance regularization:
   0.05**, then click **Calculate**.
6. Connect those grown labels and **Retained nuclei** to **Finish Cell Regions
   — CellProfiler**. Keep **Fill labelled holes** enabled. This removes regions
   belonging solely to excluded border nuclei and restores accepted nucleus IDs.
7. Connect the finished cells and retained nuclei to **Extract Cytoplasm —
   CellProfiler**. Keep **Shrink nuclei before subtraction** enabled. The
   nuclear outline remains in the cytoplasm by design.
8. Overlay nuclei, cells and cytoplasm on their source images. Inspect touching
   nuclei, image borders, unassigned regions and small objects. Save the frozen
   workflow before processing the rest of the cohort.

Generic Gaussian, threshold, watershed and subtraction nodes have different
edge or object-handling rules. For this reproduction, use the named profile
stages; see the [numerical reference](../reference/cellprofiler-compartments.md).

## Measure and preserve cell identity

Use **Measure Objects + Intensity** to obtain the unsmoothed protein's mean
intensity in **Retained nuclei** and in the **Cytoplasm** output. Export the
tables with the object label and complete source identity, keeping dataset,
plate, well and field. Label 1 in one image is unrelated to label 1 in another
image. See [measurement tables](object-measurements-tables.md) for table and
CSV handling.

The [reproduction companion](https://github.com/rensutheart/napari-vipp/blob/main/scripts/reproduce_statistics_paper.py)
joins the exported means and calculates
`nuclear_mean / (nuclear_mean + cytoplasm_mean)` for each paired cell.
Image processing runs through the VIPP graph; ratios and statistics use
companion Python postprocessing, as in the original paper.
Use the same policy for missing values and zero denominators in both
implementations; do not silently replace them with zero. The authors' selected
reference tables contain finite ratios without such exclusions.

For descriptive exploration inside VIPP, connect the compartment measurement
tables to **Statistics** or **Plot Results**, or open
[Results Workspace](../how-to/results-workspace.md) from a table node. Collect
saved batch tables through [Collect measurement results](../how-to/collect-measurement-results.md)
before comparing images. Choose the observation level deliberately: objects,
image averages and declared-sample averages answer different questions. These
tools do not reproduce the authors' downstream subsampling or inferential
analysis; the companion remains the reference for that part of the workflow.

The main IDR0139 comparison uses wells **J05**, **O02**, **E22** and **L08** on
plate 1093711385, with four fields per well. The larger selected cohort contains
ten wells. IDR0028 uses twelve selected wells across plates 1A, 2A and 2B, with
28 fields per well. The authors' selected-well tables and notebooks define the
cohort; a few example fields cannot reproduce a whole-well result.

## Compare in stages

First compare image identity, scaling, threshold masks, object counts, paired
object positions and compartment means. Then compare per-cell ratios and
well-level summaries. Preserve cell-to-well and well-to-plate relationships
when reproducing the authors' subsampling and replicate plots.

Keep three conclusions separate: agreement with the reference implementation,
agreement with the published measurements, and biological validity. A
successful segmentation comparison does not establish an independent
experimental replicate or validate the statistical inference.

The authors' [pinned code and data instructions](https://github.com/FrancisCrickInstitute/Enhancing-Reproducibility/tree/a81d20c9393485e57395cd4a1be9e7ff83c7f11d)
provide the downstream statistical notebooks. See
[validation status](../reference/validation-status.md#unreleased-cellprofiler-compartment-profile)
for the current evidence and unresolved source differences.

For an interface-only example, open **Exhaustive Inspector Showcase** and
inspect its **CellProfiler compartment profile** lane. It uses an existing
synthetic image for both nuclear and cell guidance to exercise the controls;
it is not a paper-data reproduction.
