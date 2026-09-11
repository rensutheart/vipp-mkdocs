# Check for updates

Use the version badge to check release notes and update guidance. Older
releases can use [GitHub releases](https://github.com/rensutheart/napari-vipp/releases)
directly.

## Notice an update without an interruption

A highlighted version badge with an **↑** means a newer eligible release was
found. Checking does not download an installer, start setup, or interrupt
image processing.

!!! note "Unreleased after 0.15.0a4"
    With automatic checking enabled, VIPP checks quietly on **every launch**,
    even if an earlier session checked that day. A session left open continues
    to check periodically. The released 0.15.0a4 behavior checks at most once a
    day across sessions.

- **Click the badge** to open **VIPP updates**.
- **Right-click → Release notes on GitHub** opens notes for your installed version.
- **Right-click → Check for updates…** checks now and shows the result.

On narrower windows or with larger fonts, the download buttons stack vertically;
the dialog scrolls without hiding its check and **Close** buttons. The check
button is **Check again** in the unreleased dialog (**Check for updates** in
released 0.15.0a4).

## Read the check result

**Unreleased after 0.15.0a4:** the dialog distinguishes the latest check from
the release information it already knows.

| What you see | What it means |
| --- | --- |
| A successful fresh check | GitHub answered the latest request. The result reflects the chosen prerelease preference. |
| A failed check | VIPP could not establish the current result. This does **not** mean the installed version is up to date. |
| Cached release information | Notes from an earlier successful check remain available; they are not proof that the latest request succeeded. |

Connection, DNS, proxy, verified-HTTPS, timeout, GitHub access and request-limit
failures have different explanations. Follow the reported guidance, retry
when appropriate, or use the official release page. Do not disable HTTPS
verification or security software to make a check succeed. Failure does not
interrupt calculations or change the installation.

## Download and open a Windows update

!!! note "Unreleased after 0.15.0a4 — managed desktop installations only"
    **Download & open update** is offered only when VIPP can verify that the
    running Windows desktop app is the active installation recorded by its
    managed installer. It does not select a nearby or retired environment.

1. Read the release notes and save your workflows.
2. Complete a successful fresh check, then choose **Download & open update**.
   A cached result alone does not enable this action. VIPP downloads the
   matching official installer and checksum, shows progress, and verifies the installer's
   **SHA-256** before opening it. A failed download, checksum mismatch, or
   changed installation ownership prevents the handoff.
3. Review the existing guided installer. VIPP passes the current installation
   folder and CPU/CUDA track; setup still requires your review and approval.
   Opening setup is **not** confirmation that an update was installed.
4. Finish or safely stop processing and save work before restarting VIPP.
   The updater does not quit VIPP, install in
   the live environment, or restart the application automatically. Your current
   session remains unchanged by the download-and-open action.
5. After completing the guided update, reopen VIPP, confirm the version badge,
   and test a saved workflow before resuming a large batch.

Checksum verification does not add a digital signature to an unsigned alpha.
Follow the normal [Windows warning guidance](installation.md#verify-the-download-and-pass-the-windows-warning).

## Browser and manual update routes

In released 0.15.0a4, **Download installer** and **Download checksums** open
official GitHub assets in your browser. This route also remains available for
macOS and environments that cannot use the unreleased managed-Windows action.

The unreleased dialog calls these buttons **Download in browser** and
**Checksums**. For a managed Windows installation, expand **Other download
options** to show them.

Verify the download using the [Windows](installation.md#verify-the-download-and-pass-the-windows-warning)
or [macOS](macos.md) instructions, save your work, close VIPP/napari, then open
setup yourself. Keep the intended installation and compute track.

Pip, conda and source environments require their [manual installation route](installation.md).
The updater never runs pip inside a live session or silently converts one of
these environments into an installer-managed copy. If no matching official
installer is offered, use the release notes and platform instructions.

## Choose what to check

- **Check for updates on startup** is the unreleased automatic-check setting;
  turn it off to keep only manual checks. Checks also continue periodically
  during a long session. In released 0.15.0a4 the setting is
  **Check automatically once a day**.
- **Include pre-release versions** includes alpha, beta and release candidates.
  It starts enabled for prerelease installations and disabled for final releases.

Managed/offline deployments can set `VIPP_DISABLE_UPDATE_CHECKS=1` to suppress
automatic checks. An explicit manual check still contacts GitHub.

Checks send no images, workflows, file paths, installed version or hardware
inventory. GitHub still receives ordinary connection information, such as
your IP address, when serving the public release list.

The unreleased **Download & open update** action additionally contacts the
official GitHub asset service to fetch the installer and checksum. It does not
upload your workflows or send the managed installation folder to GitHub.
