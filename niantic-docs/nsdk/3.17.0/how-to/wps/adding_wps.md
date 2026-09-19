---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/wps/adding_wps/
title: Getting Started with WPS
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Getting Started with WPS

</div>

## Adding WPS to a Unity Project<a href="#adding-wps-to-a-unity-project" class="hash-link" aria-label="Direct link to Adding WPS to a Unity Project" title="Direct link to Adding WPS to a Unity Project">​</a>

To add WPS to a Unity project:

1.  In the **Hierarchy**, select the `XROrigin`, then, in the **Inspector**, click **Add Component** and add an [ARWorldPositioningObjectHelper](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/WorldPositioning/ARWorldPositioningObjectHelper/) to it. This will also create a [ARWorldPositioningManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/WorldPositioning/ARWorldPositioningManager/) Component.
2.  Still in the **Hierarchy**, expand the `XROrigin` and `Camera Offset` to expose the `Main Camera`, then select it. In the **Inspector**, locate **Clipping Planes** under **Camera** and set the **Far** value to 1000.

This is shown below:

<img src="https://www.nianticspatial.com/docs/assets/images/world_positioning_manager-083dc285e2501c01df633e6a7f8e054f.png" width="400" alt="WPS components in Unity with proper configuration" />

### WPS Parameters<a href="#wps-parameters" class="hash-link" aria-label="Direct link to WPS Parameters" title="Direct link to WPS Parameters">​</a>

Within the `ARWorldPositioningManager` component, `Framerate` describes the target rate at which GPS and Compass measurements are consumed by the algorithm. The default value is set to 120 times per second. The `Smoothing` parameter enables smooth interpolation between transform updates: when the world positioning system updates its estimate from one transform to another, it will smoothly interpolate to the new transform over time instead of instantly teleporting to it. This provides a more natural and visually stable experience, especially when GPS or compass readings update abruptly.

</div>

</div>
