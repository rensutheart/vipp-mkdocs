# Install VIPP on macOS

VIPP 0.15.0a1 provides separate offline packages for Apple Silicon and Intel
Macs. The package includes Python, napari, Qt, and VIPP, so the normal install
does not require Terminal or a separately installed Python.

The macOS package is CPU-only, supports macOS 13 or newer, installs for the
current user, and needs approximately 3 GB of free disk space.

## Choose the correct package

Open **Apple menu → About This Mac**, then choose the matching download from
the [official v0.15.0a1 release](https://github.com/rensutheart/napari-vipp/releases/tag/v0.15.0a1):

- **Apple Silicon** — the Mac reports a chip such as Apple M1, M2, M3, or M4:
  download `VIPP-0.15.0a1-macOS-arm64-UNSIGNED.pkg` and
  `SHA256SUMS-macOS-arm64-0.15.0a1.txt`.
- **Intel** — the Mac reports an Intel processor: download
  `VIPP-0.15.0a1-macOS-x86_64-UNSIGNED.pkg` and
  `SHA256SUMS-macOS-x86_64-0.15.0a1.txt`.

Do not use a package from another site or change architectures to work around
an installation error. These are native, architecture-specific packages, not
one Universal 2 package.

## Verify the download

This alpha is explicitly unsigned and not notarized. Verify its SHA-256 before
approving macOS's warning. If you are comfortable using Terminal, open it in
the download folder and run the command for your architecture:

=== "Apple Silicon"

    ```bash
    shasum -a 256 VIPP-0.15.0a1-macOS-arm64-UNSIGNED.pkg
    ```

=== "Intel"

    ```bash
    shasum -a 256 VIPP-0.15.0a1-macOS-x86_64-UNSIGNED.pkg
    ```

Compare all 64 characters with the line for the PKG in the matching
`SHA256SUMS-macOS-*.txt` file. Stop and delete the package if they differ.
Terminal is only used here as an optional checksum tool; it is not needed to
install or run VIPP.

## Install and pass the macOS warning

1. Double-click the verified `-UNSIGNED.pkg`.
2. If macOS says the developer cannot be verified, choose **Done**.
3. Open **System Settings → Privacy & Security**.
4. Under **Security**, find the blocked VIPP package, choose **Open Anyway**,
   and confirm the exact package name.
5. Approve the Installer prompt and let installation finish.

Never disable Gatekeeper globally or remove quarantine from unrelated files.
A managed work or school Mac may not offer **Open Anyway**; ask its
administrator or use the [advanced manual route](installation.md#linux-and-advanced-manual-installation)
instead of weakening security settings.

## Open VIPP

The package creates:

- a private managed environment at `~/Library/vipp`; and
- the application `~/Applications/VIPP.app`.

Open your user **Applications** folder and double-click **VIPP**. First launch
may take longer while napari loads. macOS remains CPU-only in this alpha.

The package does not alter the system Python or shell startup files. It is a
PKG rather than a DMG because the PKG already performs the installation and
creates the application.

## Update or remove this alpha

There is no graphical updater or uninstaller in 0.15.0a1. Unless a later
release explicitly documents a supported in-place update, remove both
installer-owned paths before reinstalling:

```text
~/Applications/VIPP.app
~/Library/vipp
```

Move only those two paths to Trash. They contain the managed application and
environment; your research images and saved workflows should live elsewhere.
