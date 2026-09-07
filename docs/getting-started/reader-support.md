# Open microscope files and check reader support

!!! info "Unreleased — after 0.15.0a1"
    New plugin and desktop installations include the native microscope readers
    below. The **Reader support** section and guided setup described here are
    not present in 0.15.0a1. See the [older installation instructions](installation.md#optional-microscope-readers)
    if you are still using that version.

## What is included?

| File family | Included reader |
| --- | --- |
| TIFF, OME-TIFF and Zeiss LSM | TIFF reader and compression codecs |
| Zeiss CZI | Native CZI reader |
| Leica LIF, LOF and XLIF | Native Leica reader |
| Nikon ND2 | ND2 reader, including legacy compression support |
| Olympus OIF, OIB and OIR | Native Olympus readers |

These readers are standard in the napari plugin and Windows/macOS desktop
installations. You do not need to choose a microscope extra during installation.
Other existing inputs, such as OME-Zarr and ordinary images, remain available.

**Bio-Formats remains optional.** It provides the IMS/VSI route and broader
fallback support. Its current Python package can fetch Java and Bio-Formats
when first used, so that first read may require internet access and extra time.
[Bio-Formats installation details](https://pypi.org/project/bioio-bioformats/).

## Check or fix a reader

1. Select any **Image Source** node, including a newly added node. You do not need
   to open a file or change its source mode.
2. Expand the separate **Reader support** inspector section, marked
   **System information**. It is normally collapsed, outside the image parameters.
3. Read the status beside the format you need. **Reader loads** means the
   dependency/import check passed; it does not validate the selected image.
4. If a package is missing, click **Install [reader]…**. If a reader cannot load,
   retry its check or open **Reader help**.

When an image fails to open, relevant reader actions also appear directly in
Image Source, without requiring you to find a Settings page. Use **Retry opening
this image** after a temporary problem is resolved.

Reader support describes this installation, not a processing setting for the
selected image. The first expansion checks support in the background. Results
are cached for the VIPP session, including while switching nodes. Use **Recheck
reader support** to refresh them explicitly; restarting VIPP starts a new cache.

Format names are bold in the normal text colour. The status beside each name
is **green** when the reader loads, **yellow** when support is missing or needs
an update, and **red** when loading failed. Scroll the inspector to see all
formats and recovery actions.

## Install missing support

1. In the separate setup window, confirm that the displayed environment is the
   VIPP/napari installation you want to fix.
2. Click **Review packages**. This downloads a proposed package set from PyPI;
   it does not install it yet.
3. Review the package list and approve **Install after VIPP / napari closes**.
4. Save your work and close VIPP/napari normally. Close other Python sessions
   using that environment too; leave the setup window open.
5. Wait for the result, then reopen VIPP/napari and retry the image.

Setup only adds missing packages. It does not replace installed scientific
packages, change your images, or automatically close your work. You can close
setup while it is waiting to cancel. Do not reopen VIPP during installation.

If the reader needs different installed dependencies, or the environment is
shared, externally managed or read-only, setup stops. Use the normal
[VIPP update route](updating.md) or ask the environment owner to repair it.
An import check cannot repair a broken native library by itself.

## Before quantitative use

Check representative facility files: selected series, axes, scale and units,
channels, dtype and pixels. Some vendor acquisitions need companion files or
are outside a reader's supported variants. Installing another reader does not
override VIPP's saved source identity or silently accept different axes.

See [input formats and source contracts](../reference/import-export.md) for the
scientific boundaries and [loading problems](../troubleshooting/index.md) for
other causes of a failed import.
