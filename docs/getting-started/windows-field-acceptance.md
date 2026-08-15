# Try the VIPP Windows installer

Use this checklist when someone asks you to test the tagged VIPP `0.13.0a7`
installer on Windows. You do not need Python knowledge. Check only what you
actually tried; leave everything else as **not run**.

!!! warning "Use the exact public tagged installer"
    The official public installer SHA-256 is
    `b62c715152447c4b1f8db878996b776ef2bfb0cdc6656df72d3ec94e7818c12f`,
    and a fresh download from the public release matched it. Use this checklist
    only with the exact `v0.13.0a7` GitHub asset and checksum identified by
    [release verification](../releases/0.13.0a7.md#release-verification). Do not
    use an untagged build or a similarly named file from another site.

    A display-independent production-backend install, repair, scientific
    smoke, and uninstall does not count as a pass for the downloaded
    installer's visible setup window or operator experience.

Start with the normal [Windows installation instructions](installation.md).
If you have a suitable NVIDIA GPU and were asked to test acceleration, also use
the [Windows CUDA and cuCIM instructions](windows-cuda.md).

!!! important "What to expect from unusual paths"
    Windows supplies canonical Local App Data through
    `SHGetKnownFolderPath(FOLDERID_LocalAppData)`. Managed setup accepts only
    `VIPP\environments\cpu` or `VIPP\environments\cuda13` beneath it; custom
    managed roots are rejected. The fixed CPU root supports spaces and
    non-ASCII characters. CUDA supports spaces but requires the complete
    canonical path to be ASCII. If it is not, one-click CUDA should be
    unavailable before download and setup should offer CPU.

!!! warning "Keep private information private"
    Do not post your Windows username, computer name, local paths, unpublished
    images, support reports, or screenshots publicly. Send the completed notes
    only to the person who invited you to test. Review the privacy-redacted
    Compute Doctor support report before sharing it.

## Before installing

Record these facts without including your account or computer name:

- Windows version:
- Standard or administrator account:
- Does the account path contain a space? yes / no / unsure
- Does it contain a non-ASCII character? yes / no / unsure
- GPU model, if testing CUDA:
- Start time:

Download the installer and checksum file only from the official `v0.13.0a7`
entry on the
[VIPP releases page](https://github.com/rensutheart/napari-vipp/releases).
The filename should be
`VIPP-Setup-0.13.0a7-Windows-x86_64-UNSIGNED.exe`. In PowerShell, run:

```powershell
Get-FileHash -Algorithm SHA256 `
  .\VIPP-Setup-0.13.0a7-Windows-x86_64-UNSIGNED.exe
```

Compare all 64 characters with the installer line in
`SHA256SUMS-Windows-0.13.0a7.txt`. Stop and delete the file if they differ. This
alpha is intentionally unsigned, so **Unknown publisher** is expected; an
antivirus threat warning is not expected and must not be bypassed.

## The short test

- [ ] The installer opened and its recommended choice made sense without
      needing to understand Python or CUDA packages.
- [ ] Installation finished and created the expected VIPP shortcut or
      shortcuts.
- [ ] **VIPP** or **VIPP Automatic** opened successfully.
- [ ] I opened a bundled example, calculated it, and saw a sensible result.
- [ ] I saved the workflow, closed it, reopened it, and calculated it again.
- [ ] I ran a small batch and could find its outputs.
- [ ] Compute Doctor showed short, understandable results and one next action.
- [ ] I could tell whether the calculation actually used CPU or GPU.

What was confusing or did not work:

## Extra CUDA check

Complete this only if the installer offered the NVIDIA CUDA route.

- [ ] The CUDA installation location exactly matched canonical Local App Data
      plus `VIPP\environments\cuda13`; spaces did not prevent setup.
- [ ] Supplying any other managed root was rejected before resolution or
      download; setup did not expose a custom-location chooser.
- [ ] If canonical Local App Data contained a non-ASCII character, one-click
      CUDA was unavailable and setup offered the fixed CPU route instead.
- [ ] Selecting an expert existing CUDA environment remained a separate
      non-mutating review and never suggested moving, editing, or adopting it.
- [ ] For an installer-owned CUDA copy under a non-ASCII root, setup separately
      reported any recovery from a prior interrupted transaction; after that
      recovery, the newly blocked selection performed no new mutation. Setup
      opened Installed apps for ownership-bound removal; it did not offer a
      second or custom managed CUDA copy or an in-place/fallback migration.
- [ ] **VIPP Automatic**, **VIPP CPU**, and **VIPP Prefer GPU** all opened.
- [ ] Compute Doctor separately showed **CUDA and GPU**, **Optional cuCIM**,
      and **VIPP GPU coverage**.
- [ ] At least one reviewed operation showed that it actually ran on GPU.
- [ ] A CPU-selected or unsupported step explained its CPU fallback and still
      produced the expected result.
- [ ] The same small workflow completed with Automatic and CPU-only shortcuts.
- [ ] **Portable GPU Segmentation Bridge** completed in Prefer GPU and CPU,
      retained four final objects, and showed an explanation for any CPU step.
- [ ] If a node showed a dtype-only **GPU tip**, **Add conversion** inserted one
      visible Convert Dtype node in the expected place and Undo removed it.
- [ ] A relevant GPU tip remained visible after a Prefer GPU calculation.
- [ ] **Find fastest** kept grouped results readable and inspectable, including
      when it could not choose a winner.

If you were specifically asked to test optional cuCIM:

- [ ] I verified the official cuCIM ZIP against the a7 checksum file.
- [ ] I used **Extract All** before running **Install VIPP cuCIM.cmd**.
- [ ] The helper built cuCIM locally for this VIPP CUDA environment.
- [ ] Compute Doctor changed only the optional cuCIM and genuinely enabled
      coverage results.

What was confusing or did not work:

## Repair, rollback, and removal

Only perform interruption or network-failure tests on a computer where the
previous working installation and research data are safely preserved.

- [ ] Rerunning the same installer offered a clear repair choice and the
      repaired installation still worked.
- [ ] If updating, the previous working version remained usable until the new
      version passed its checks.
- [ ] For an installer-owned CUDA copy already under a non-ASCII root, any
      prior-transaction recovery was recorded separately and the newly blocked
      selection caused no new mutation, with clear fixed-root/CPU guidance.
- [ ] If setup was cancelled, it reached a clear end state and did not present
      a half-created installation as ready.
- [ ] If the network failed, setup explained what to do and preserved the
      previous working installation.
- [ ] Retrying after restoring the network completed successfully.
- [ ] Uninstall removed VIPP-owned shortcuts and files without removing
      unrelated data or another separate CPU/CUDA VIPP installation.

What was confusing or did not work:

## Final result

- CPU fresh installation: pass / fail / not run
- CUDA fresh installation: pass / fail / not run
- Spaces path: pass / fail / not run
- CPU non-ASCII path: pass / fail / not run
- CUDA non-ASCII-path guidance: pass / fail / not run
- Cancellation rollback: pass / fail / not run
- Network-failure rollback: pass / fail / not run
- Repair/update/uninstall: pass / fail / not run
- Novice first workflow: pass / fail / not run
- Finish time:
- Overall: ready for my use / still has a problem
- Most important remaining problem:

Automated tests, an older development installer, WSL, or a different VIPP
version do not count as a pass for this downloaded `0.13.0a7` installer.
