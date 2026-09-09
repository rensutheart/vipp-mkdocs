# Export a reproducibility package

Create a local ZIP containing a readable methods/evidence report and a portable
workflow with its explanatory notes. Review the exact contents before sharing
it with a collaborator or including it in an analysis archive.

!!! note "New in 0.15.0a3"
    This export requires VIPP 0.15.0a3 or newer. It does not
    calculate the graph, upload anything, or include raw images, output images,
    tables, meshes, thumbnails or previews.

## Choose the right evidence

| Start here | What the package describes |
| --- | --- |
| Main toolbar gear → **Workflow actions → Export reproducibility package…** | The current workflow recipe, captured when the review window opens. This is not evidence that the graph was run or its outputs verified. |
| **Batch workflow → Run & results → run report card → Export reproducibility package…** (also **Export package…** in the finished-run footer) | The recorded run's archived workflow, settings and available item evidence—not the graph as edited afterward. The action is enabled after a recorded run, while no run is active. |

Both batch actions open the same review window; neither immediately saves a ZIP.
The package keeps the workflow's explanations, settings, software versions and
run records, but not images, intermediate results or saved outputs. The results
toolbar keeps run-recovery and file-status actions, not package export.

For batch work, keep failed, partial, skipped and cancelled outcomes visible;
the package does not turn them into successful results. If the archived evidence
is incomplete or incompatible, preparation fails rather than substituting the
current graph. Keep the original manifest archives and sidecars separately.

## Prepare, review and export

1. Open the export action for the evidence you want. Initial preparation runs
   in the background, leaving the interface responsive.
2. Review the **Report title** and optional **Notes**. Folder locations are
   hidden automatically. Select **Anonymise filenames** if filenames should
   also be replaced; it is off by default.
3. After changing any of those fields, select **Prepare report** again. The old
   preview and sharing confirmation are invalidated; export waits for the new
   report.
4. Read **Report**, inspect the file inventory and exact text in **Package
   contents**, and check **Privacy & omissions** for removed information,
   substitutions and limitations.
5. Check **I reviewed the report and included files for sharing.** Then select
   **Export package…** and choose a new `.zip` filename. Existing files are not
   overwritten. The ZIP contains the prepared bytes you reviewed; export does
   not regenerate the report from later graph or file changes.

Closing during preparation discards the pending preview. Once ZIP writing has
started, Close becomes available when writing finishes. A cancelled destination
dialog writes nothing.

In the preview, an official release or setup-guide link opens your browser only
when you select it. The `workflow.json` link explains how to export, extract
and open the workflow in VIPP; it does not start an analysis. The preview does
not fetch remote images or other resources.

## Repeat the analysis in VIPP

1. Extract the ZIP and open `report.html`. Start with **How to repeat the
   analysis**; its `workflow.json` link refers to the file beside the report.
2. Review the recorded VIPP version and follow the report's official release
   and installation-guide links, when available. Run versions and the version
   that exported the package are separate records. A development or locally
   modified build may have no matching public installer; ask the author for
   that build's setup information rather than assuming the latest release is
   equivalent.
3. In VIPP, choose **Open workflow** and select the extracted `workflow.json`.
   For a recorded workflow with verification information, choose **Reproduce
   original run** or **Use workflow on new data** when prompted, review the
   version status, then select **Continue to batch setup**.
   If the package contains batch settings, that file carries them together
   with the graph and restores **Batch workflow → Setup**. Review any
   restoration warning before continuing.
   Opening the workflow or viewing an Image Source does not change its saved
   settings; input verification starts when you select **Check batch**.
4. In **Setup**, choose the intended input folder for each collection source
   and a **new output folder**. Select any fixed reference images separately
   in their **Image Source** inspectors; the restored batch settings are
   retained. Review filename patterns, source pairing, image axes, calibration,
   overrides and output settings.
5. Select **Check batch**, review **Items & outputs** and **Overrides**, then
   select **Run** when the checked plan is correct. Checking does not calculate
   images or save processing outputs. Compare the new results with the
   separately supplied reference results and validation evidence.

For a graph-only recipe, reconnect each **Image Source** in the inspector and
review any save destinations before calculating. The package does not include
the images or results you need for either route. Ordinary GUI reuse does not
require editing JSON or copying workflow/configuration hashes.

### Reproduce or use new data

- **Reproduce original run:** use the original inputs. **Check batch** compares
  them with the recorded hashes and image selections. The summary shows how
  many need attention; the **Checks** column identifies affected items. Changed,
  missing or unexpected inputs block Run until resolved.
- **Use workflow on new data:** no match to the original inputs is required.
  VIPP keeps its normal input checks. Saving this reused workflow does not keep
  the original reproduction requirement; export a new recorded batch to create
  a new reference.

If you checked the wrong folder, choose the original inputs in **Setup** and
select **Check batch** again. A successful check replaces the earlier mismatch
result. **Run** checks for subsequent changes before processing; no hash
exception is needed for corrected, matching inputs.

The compact banner keeps its actions to the right of the status text. Select
**Check details…** for the input result, matched/needs-attention totals,
any issues and the VIPP version status, including an accepted version difference.
**Review batch inputs** opens all rows in **Items & outputs**; **Review affected
inputs** shows only items needing attention and clears any search. For a version
or setup problem, **Review batch setup** returns to **Setup**. These buttons only
change views: they do not recheck files, approve exceptions or start Run.

The opening dialog groups the two choices and shows whether the original and
installed VIPP versions match. For reproduction, a different or unknown version
needs explicit acknowledgement. The nearby release and installation links help
you obtain the original version; they open a web page, not an automatic download
or installation. An accepted difference stays visible and is recorded; input
checks still apply. For new data, the version notice does not block the analysis.

After a fully successful reproduction with matching VIPP versions, the green
**Run complete · Original inputs verified** banner describes the completed run.
It does not authorise another run: select **Check batch** again before running
again. Changing input folders or batch settings clears the completed-run badge.
Cancelled, partial or failed runs, and runs with an accepted version difference,
do not receive this green completion state.

Matching hashes confirm the same input files, not identical analysis results.
Software dependencies, hardware and settings also matter. Older packages, and
runs without sufficient recorded input information, may lack this verification;
export a fresh package from the original recorded run where available.

Check the newly discovered samples, including series within multi-image files.
The portable settings do not reuse the old frozen input inventory as proof
about files on your computer. Scientific overrides remain tied to their source
content and logical item; changed data or selectors need review. Individual
overwrite permissions from the original run are not transferred. Review any
existing-output decisions afresh.

Fixed reference images need individual **Image Source** relinking; they are not
silently converted into folder collections. Missing fixed-reference files do
not discard the restored Setup, but **Check batch** still requires all sources
to be valid before Run. Live-layer and sample inputs also
need their intended data supplied separately. If VIPP cannot restore a source
or its Batch Setup, stop and use the author's source-selection/setup notes to
review the recipe before running. Do not substitute another series or image
merely to make the check pass.

The ZIP contains no installer and does not set up an environment automatically.
Use the official software links deliberately; opening or exporting the package
does not install software. A matching VIPP version alone does not establish
matching readers, dependencies, hardware or results.

### Python is an advanced alternative

Use the supplied runners only when you need headless execution. `README.md`
describes their setup and limitations; their `--help` output lists the exact
arguments. For a recorded batch, use `batch-runner.py` with its batch
configuration so batch overrides are retained. `runner.py` embeds the ordinary
graph as an independent copy without those batch overrides. The Python
route is not required to repeat the analysis through VIPP.

## What is included

The inventory is specific to the selected recipe or run. Core files include:

- `report.html`: the self-contained report, readable offline after extracting
  the ZIP;
- `workflow.json`: the portable workflow and its explanatory notes, including
  portable Batch Setup when batch settings are available;
- `README.md`: GUI-first repeat steps, scope and limitations;
- `runner.py`: the generated VIPP runner for advanced headless use;
- `environment.json`: available run/export version summaries;
- `report.json`: structured report details, omissions and changes;
- `SHA256SUMS.json`: exact-byte checksums for the other package members.

Packages with batch settings also include `batch-config.json` and
`batch-runner.py`. The standalone settings match the attachment in
`workflow.json`; they are provided for advanced use, not a required separate
GUI import. A recorded batch package additionally contains sanitized evidence
views, which are **not the original run receipts**.
Recorded source/output identities are reported without reopening the image or
result files to verify them again.

The version summary is not an environment lockfile, installer or bundled Python
environment. Checksums identify exported bytes; they do not authenticate an
author or establish scientific correctness.

## Review privacy and reuse limits

Folder removal and filename anonymisation do not guarantee anonymity. Scientific
labels, node titles and explanatory notes may still identify people or samples.
Workflow notes are kept, with the same folder hiding and optional filename
anonymisation as other shared text. Read those notes and inspect the included
files before sharing. Nothing is sent to an external service by preparation or
export.

The package is **not resumable run state**, a complete data archive, or a promise
of identical output on another computer. Follow the repeat steps above and
validate the result for your data. Keep the original evidence for
[verified batch resume](../workflows/batch-processing.md#resume-an-interrupted-run).

For a publication archive, add the separately reviewed data, results, validation
and manual-decision context required by the
[reporting checklist](../scientific-practice/reporting.md).
