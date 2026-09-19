---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/WorldPositioning/ARWorldPositioningObjectHelper/AltitudeMode/
title: enum AltitudeMode
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# enum AltitudeMode

</div>

(Niantic.Lightship.AR.WorldPositioning.ARWorldPositioningObjectHelper.AltitudeMode)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

The altitude above sea level is often inaccurate and the floor height unknown. The AltitudeMode provides the option to use a different system for representing altitude/height.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs

enum AltitudeMode {
      SEA_LEVEL       = 0,
        TRACKING        = 1,
        CAMERA          = 2,
        CAMERA_AVERAGED = 3,
};
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

The altitude above sea level is often inaccurate and the floor height unknown. The AltitudeMode provides the option to use a different system for representing altitude/height.

SEA_LEVELThe standard WGS84 altitude above sea-level. This option is only recommended for use when working with map data where the altitude is known.

TRACKINGUses the y coordinate of the [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) tracking coordinate system. This is recommended if content is generated using runtime estimates of the ground position, which will usually be in [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) tracking coordinates.

CAMERAPositions content relative the height of the camera. This can be used for navigation arrows or similar visual indicators.

CAMERA_AVERAGEDSimilar to CAMERA but uses the average camera height to provide a stable relative position while behaving intuitevely if the user moves the device up and down momentarily. This method is recommended for most applications.

</div>

</div>
