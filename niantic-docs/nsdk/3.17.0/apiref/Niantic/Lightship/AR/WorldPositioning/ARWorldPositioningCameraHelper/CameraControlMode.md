---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/WorldPositioning/ARWorldPositioningCameraHelper/CameraControlMode/
title: enum CameraControlMode
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# enum CameraControlMode

</div>

(Niantic.Lightship.AR.WorldPositioning.ARWorldPositioningCameraHelper.CameraControlMode)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

The CameraControlMode represents the adjustment to be applied to the [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) camera before rendering

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs

enum CameraControlMode {
     Default   = 0,
      HeadsDown = 1,
};
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

The CameraControlMode represents the adjustment to be applied to the [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) camera before rendering

Default leaves the camera position unchanged so that it matched the device trackign position

HeadsDown adjusts the camera view so that a downwards 45 degree tilt results in a horizontal view being rendered. This allows the user to hold the device in a more comfortable position during extended gameplay.

</div>

</div>
