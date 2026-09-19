---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/TrackingStateReason/
title: enum TrackingStateReason
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# enum TrackingStateReason

</div>

(Niantic.Lightship.AR.XRSubsystems.TrackingStateReason)

Provides further information about the tracking state of an anchor. Query this if the anchor's tracking state is NotTracking

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs

enum TrackingStateReason: UInt32 {
     None             = 0,
       Removed          = 1,
       AnchorTooFar     = 2,
       PermissionDenied = 3,
};
```

</div>

</div>

</div>

</div>
