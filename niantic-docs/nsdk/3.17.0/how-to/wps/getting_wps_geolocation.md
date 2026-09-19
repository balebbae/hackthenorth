---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/wps/getting_wps_geolocation/
title: Getting Geolocation with WPS
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Getting Geolocation with WPS

</div>

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

This guide assumes that you’ve already gone through:

- How to set up a basic AR session guide.
- Getting started with WPS guide.

## Accessing Geolocation Estimates<a href="#accessing-geolocation-estimates" class="hash-link" aria-label="Direct link to Accessing Geolocation Estimates" title="Direct link to Accessing Geolocation Estimates">​</a>

Adding the [ARWorldPositioningManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/WorldPositioning/ARWorldPositioningManager/) to the **XROrigin** component in the **Hierarchy** will automatically add an [ARWorldPositioningCameraHelper](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/WorldPositioning/ARWorldPositioningCameraHelper/) to the **Main Camera**. To directly access the more accurate compass and GPS properties provided by WPS, the values are directly exposed through the `CameraHelper`. A sample script accessing these values can be found below:

Click to reveal WPSCompass.cs

<div>

<div class="collapsibleContent_i85q">

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Attention!

</div>

<div class="admonitionContent_BuS1">

Be sure to set the `ARCameraManager` in the **XROrigin** inspector before running!

</div>

</div>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Niantic.Lightship.AR.WorldPositioning;
using UnityEngine.XR.ARFoundation;

public class WPSCompass : MonoBehaviour
{
    [SerializeField] private ARCameraManager _arCameraManager;
    
    private ARWorldPositioningCameraHelper _WPSCameraHelper;

    // Start is called before the first frame update
    void Start()
    {
      _WPSCameraHelper = _arCameraManager.GetComponent<ARWorldPositioningCameraHelper>();
    }

    // Update is called once per frame
    void Update()
    {
        float heading = _WPSCameraHelper.TrueHeading;
        
        double latitude = _WPSCameraHelper.Latitude;
        double longitude = _WPSCameraHelper.Longitude;
        double altitude = _WPSCameraHelper.Altitude;

        Quaternion q = _WPSCameraHelper.RotationCameraRUFToWorldEUN;
    }
}
```

</div>

</div>

The `Latitude`, `Longitude`, `Altitude`, and `TrueHeading` fields provide the estimated geolocation for the device, where `TrueHeading` represents the heading relative to true north. the `RotationCameraRUFToWorldEUN` provides the quaternion for the device's orientation in East-Up-North space (where East is +x axis, Up is +y axis, and North is +z axis).

</div>

</div>

</div>

</div>
