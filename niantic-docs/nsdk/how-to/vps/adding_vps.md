---
source: https://www.nianticspatial.com/docs/nsdk/how-to/vps/adding_vps/
title: Getting Started with VPS
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Getting Started with VPS

</div>

When using Unity, the Niantic Spatial Development Kit (NSDK)s package provides a configurable component to help you create and manage your VPS enabled AR experience.

## The AR Location Manager<a href="#the-ar-location-manager" class="hash-link" aria-label="Direct link to The AR Location Manager" title="Direct link to The AR Location Manager">​</a>

The AR Location Manager allows you to easily persist content at Public Locations.

<img src="https://www.nianticspatial.com/docs/assets/images/ARLocationManager-0f7b288115e3331e4890d46b6302fb7a.png" style="width:75.0%" alt="AR Location Manager Component" />

- **Default Anchor GameObject:** This will take a gameObject prefab and instantiate it at the ARLocation’s default anchor position once localized as an easy way to visualize the process.
- **VPS Usage Mode:** Preset configurations for the VPS Manager.

Drift Mitigation Options:

- **Continuous Localization:** Continue to send localization requests after localization. This mitigates drift but consumes more bandwidth. If enabled then you can also use:
  - **Interpolation Enabled:** Interpolates anchors positions instead of snapping them in place.
  - **Temporal Fusion Enabled:** Average/fused multiple localization results to provide a more stable localization.

Performance:

- **JPEG compression Quality:** (Default: 50) 0-100 value, determines the quality of the JPEG image sent to the servers for cloud localization. The lower quality can save more network bandwidth usage. We have benchmarked that 50-90 quality for jpeg compression does not significantly impact the accuracy of the localization results.
- **Initial Service Request Interval Seconds:** Number of seconds between server requests.
- **GPS Correction for Continuous Localization:** If checked, VPS localization will use estimated GPS location from previously localized information instead of device GPS read. Intended for large and poor GPS area localization.

Debugging Options:

- **Diagnostics Enabled:** If checked, VPS localization will run image classification which outputs the probability of each “failure cause” category, for example: image too dark, moving too fast or looking at ground. This feature is GPU intensive and Android devices often struggle and slow down rendering performance.
- **VPS Debugger Enabled:** If checked, NSDK will create a log file with detailed events related to VPS localization. This can be helpful to investigate issues in VPS localization.

VPS Startup Behavior:

- **Auto Track:** If checked, the location manager will automatically try to localize to the AR Location selected.
- **AR Location:** AR Locations available in the scene.
- **Add AR Location:** This will create an AR Location GameObject in the hierarchy which will then show up on the AR Location list. Note that this will not be valid until you assign a location manifest or Payload to it.

## AR Location<a href="#ar-location" class="hash-link" aria-label="Direct link to AR Location" title="Direct link to AR Location">​</a>

The AR Location game object is a representation of a real-life location. In the hierarchy the game object holding this component must be a child of XR Origin, and child objects of the AR Location will be connected to the location and appear relative to it when localization succeeds.

<img src="https://www.nianticspatial.com/docs/assets/images/ARLocation-ce86e7758cf9d7807321b6c98cc2aa6b.png" style="width:75.0%" alt="AR Location Component" />

- **Include Mesh in Build:** if enabled and an AR Location Manifest is assigned, you’ll be able to see the mesh of the location on Editor.
- **AR Location Manifest:** allows you to assign a location mesh (available on the GeoSpatial Browser).
- **Payload:** string blob representing the location.

<div class="theme-admonition theme-admonition-warning admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Legacy Geospatial Browser workflow

</div>

<div class="admonitionContent_BuS1">

The Geospatial Browser is no longer available. These instructions are retained for developers maintaining older `ARLocation` projects. For current projects, manage Sites in <a href="https://scaniverse.nianticspatial.com/" target="_blank" rel="noopener noreferrer">Scaniverse Web</a> and use [VPS2](https://www.nianticspatial.com/docs/nsdk/how-to/vps2/adding_vps2/).

</div>

</div>

</div>

</div>
