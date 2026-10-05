# Track objects and spots over time

Create a trajectory table from repeated detections or segmented objects, then
review the links against the source series.

!!! info "New in 0.16.0a3"
    **Detect Spots per Frame**, **Build Tracks**, and trajectory review are
    available in this release. They run on the CPU and support one explicit scalar `TYX` or
    `TZYX` series. They do not infer divisions, fusions or biological identity.

## Choose what to follow

| Starting data | Workflow |
| --- | --- |
| Bright spots | Image Source → select one channel → Detect Spots per Frame → Build Tracks |
| Repeated intensity patterns | Time series plus a fixed spatial template → Detect Spots per Frame (**Template match**) → Build Tracks |
| Segmented objects | Per-frame labels → Measure Objects → Build Tracks |

Select one channel upstream; do not remove T. Each XYZ volume is processed as
one frame. If image drift needs correction, explicitly
[register and apply the transforms](register-images.md) before detection or
segmentation. Linking does not automatically correct drift.

1. In **Detect Spots per Frame**, choose **Local peaks** or **Template match**.
   For template matching, connect a fixed `YX`/`ZYX` template with matching spatial
   sampling. Set the minimum value and separation as described in
   [detection controls](../reference/detection.md#find-peaks-controls).
2. Calculate and review detections. **Maximum detections per frame** is a cap,
   not a count estimate. Increase it if any frame is truncated; Build Tracks
   refuses capped observations.
3. Connect the complete table to **Build Tracks**. Set **Maximum displacement /
   frame**, choose pixel or physical distance, and initially leave **Maximum
   missing frames** at zero.
4. Calculate. The two outputs are **Tracked observations** and **Track
   summary**. Use **Display Output** to inspect/export either table.
5. Choose **Review trajectories…** on the node card, or **Review trajectories
   on source…** in the inspector. Select a row or current-frame marker to
   navigate to its T and Z. Sorting the table does not change its identity.

The card shortcut sits beside **Open measurements…** on **Detect
Spots per Frame** and **Build Tracks**. It also appears on **Measure Objects**
and **Measure Objects + Intensity** when their calculated table carries time-series
observations. It opens that node's existing read-only source/table review without
calculating or changing the selected node. See [review availability](../reference/tracking.md#source-review)
if the cached result or source is no longer current.

For labels, use **Measure Objects** or **Measure Objects + Intensity** on the
explicit time series. The original index centroids and label IDs are retained
in the observation table. Label IDs are local to a frame; equal IDs at different
times are not assumed to be the same object. Imported labels must use a supported
label-output route; do not threshold/relabel them merely to preserve their IDs.
The supplied object example explicitly segments its synthetic source, so its
connected-component IDs may change between frames.

## Review gaps and uncertainty

**Maximum missing frames = 1** permits linking across one absent frame. The
distance allowance is multiplied by elapsed frames; it does not predict motion.
Adjacent-frame candidates have priority over older gap candidates.

- Cyan trails join observed positions. Dashed segments span missing frames;
  they are not measured or interpolated intermediate positions.
- Orange trails identify observations with competing feasible links. Inspect
  them; the flag is not a probability and does not catch every possible error.
- Yellow highlights the selected track. In 3D, only links with both endpoints
  on the selected Z plane appear. This is not a projection.

Crossing objects can exchange identities. Increasing the displacement or gap
allowance can create plausible but incorrect links. Check representative
sequences against independent annotations before drawing biological conclusions.

The preview fits the available window. **Trail frames**, time/plane selection,
table sorting and decimal display affect only review. Changed sources or
settings disable the old view; **Refresh view** loads an already calculated
current result and does not start a calculation.

## Try the synthetic examples

Open **2D Spots, Missing Frame and Crossing Review** to inspect isolated
trajectories alongside a crossing pair and an empty frame. Compare the uncertain
crossing, rather than assuming the displayed IDs establish identity. Open
**Anisotropic 3D Object Trajectories** for XYZ objects with unequal spatial
sampling, a missing observation and a later appearance.

See [tracking contracts and output columns](../reference/tracking.md) for units,
linking rules, saved evidence and limitations.
