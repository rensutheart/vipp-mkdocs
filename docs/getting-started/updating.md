# Check for updates

Use the version badge in VIPP 0.15.0a2 to check release notes and update guidance. Older releases can use [GitHub releases](https://github.com/rensutheart/napari-vipp/releases) directly.

## Notice an update without an interruption

VIPP checks GitHub quietly, at most once a day. A highlighted version badge
with an **↑** means a newer release was found. Nothing opens automatically,
and no installer or package is downloaded or installed automatically.

- **Click the badge** to open **VIPP updates**.
- **Right-click → Release notes on GitHub** opens notes for your installed version.
- **Right-click → Check for updates…** checks now and shows the result.

The dialog offers notes for the latest eligible release. Offline or rate-limit
errors stay in this dialog; they do not interrupt image processing. Cached
release information can remain visible when GitHub is unavailable.

On narrower windows or with larger fonts, the download buttons stack vertically;
the dialog scrolls without hiding its **Check for updates** and **Close** buttons.

## Update safely

1. Read the release notes and save your workflows.
2. For an installer-managed application, use **Download installer** and
   **Download checksums** when offered. Both open official GitHub assets in
   your browser. Verify the download using the
   [Windows](installation.md#verify-the-download-and-pass-the-windows-warning)
   or [macOS](macos.md) instructions.
3. Finish or safely stop processing, then close VIPP/napari.
4. Run setup and review the installation options. Keep the intended Windows
   CPU/GPU installation; an installer may create a separate installation
   instead of updating a pip/conda environment or source checkout.
5. Reopen VIPP and confirm the version badge. Test a saved workflow before
   resuming a large batch.

No matching installer? Follow the [installation guide](installation.md) for
your platform/environment. The dialog never runs pip inside a live session
or executes a downloaded installer for you.

## Choose what to check

- **Check automatically once a day** can be turned off; manual checks remain available.
- **Include pre-release versions** includes alpha, beta and release candidates.
  It starts enabled for prerelease installations and disabled for final releases.

Managed/offline deployments can set `VIPP_DISABLE_UPDATE_CHECKS=1` to suppress
automatic checks. An explicit manual check still contacts GitHub.

Checks send no images, workflows, file paths, installed version or hardware
inventory. GitHub still receives ordinary connection information, such as
your IP address, when serving the public release list.
