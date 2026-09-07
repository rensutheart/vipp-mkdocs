# Channel and axis controls

Start with [axes and metadata](../concepts/axes-and-metadata.md) to establish what
each dimension means. These controls make deliberate changes; they do not
infer biological channel identity from dimension length.

## Choose the operation

| Need | Node |
| --- | --- |
| One scalar channel | Extract Channel |
| Separate graph outputs for every semantic channel | Split Channels |
| Separate time points, Z slices, or another non-channel axis | Split Axis |
| A channel-last RGB image | Composite → RGB |
| Resize spatial dimensions | Rescale Axes |
| Supply missing acquisition facts | Set Microscope Metadata |

## Composite → RGB

Axis choice and colour assignment are independent:

| Control | Auto | Manual |
| --- | --- | --- |
| Channel axis mode | Uses the explicit carried channel axis; the resolved choice is read-only. | Lets you choose a valid axis deliberately, including Z; the choice is recorded. |
| RGB mapping mode | Shows the resolved mapping from encoded RGB/RGBA or fluorescence pseudo-colours. | Exposes one saved colour choice per detected source channel. |

Missing or ambiguous channel semantics are errors in Auto, not an invitation
to guess from a trailing dimension of length three or four.

Manual colours are **Unassigned**, **Red**, **Green**, **Blue**, **Magenta**,
**Cyan**, and **Yellow**. Composite colours contribute to multiple RGB planes;
multiple channels can add to the same plane. Unassigned contributes nothing.
There is no three- or four-source-channel limit.

Auto mapping:

- preserves declared RGB/RGBA order and ignores alpha;
- blends all fluorescence channels using their carried pseudo-colours;
- falls back to Blue, Green, Red, Magenta, Yellow, Cyan, repeating as needed;
- copies one scalar channel into all three RGB planes.

**Intensity mapping** is a separate scientific choice:

- **Preserve numeric values** keeps native scale without normalization or
  clipping and rejects unsafe precision/overflow cases.
- **Per-channel 1st–99th percentile (lossy)** normalizes channels independently
  and clips additive mixtures to `[0, 1]`.

Changing the mapping invalidates this node and its descendants, not unchanged
upstream manual results. Smart/Low-memory cache modes may still prune automatic
intermediates under their normal retention policy.

## Which Split Channels output is inspected?

When exactly one distinct output is connected, that channel drives the split
node's thumbnail, inspect/pinned layer, histogram, metadata, dimensions, and
**Save selected output…**. Several consumers of the same port still count as one.

With no connected output, or several different outputs in use, these surfaces
use the saved **Thumbnail channel**. This presentation choice neither rewires
the graph nor changes the arrays delivered downstream.

## Rescale Axes with inferred names

Unique inferred X/Y axes may be resized after reviewing the inspector's amber
warning. A real X/Y size change records that plane as explicit; a no-op does not
change confidence. Other inferred axes retain their metadata.

This does not infer depth. A `QYX` image keeps Q unchanged until you explicitly
establish that Q means Z. An inferred Z axis must likewise be declared before
a nontrivial Z resize. Interactive, exported, and batch execution use the same
rule.

## Set Microscope Metadata

This pass-through node supplies up to three channel emission wavelengths,
objective numerical aperture, and immersion refractive index. Zero means
**leave the carried value unchanged**, not erase it.

Channels 2/3 require an explicit channel axis and a matching channel count.
Values travel with the image and its history without changing pixels. This is
separate from **Set Pixel Size / Units**, which supplies spatial calibration.
