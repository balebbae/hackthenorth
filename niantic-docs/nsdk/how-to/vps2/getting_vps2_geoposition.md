---
source: https://www.nianticspatial.com/docs/nsdk/how-to/vps2/getting_vps2_geoposition/
title: Geolocate with VPS2
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Geolocate with VPS2

</div>

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

This guide assumes that you have already completed:

- [Get started with VPS2](https://www.nianticspatial.com/docs/nsdk/how-to/vps2/adding_vps2/)

### Device geolocation<a href="#device-geolocation" class="hash-link" aria-label="Direct link to Device geolocation" title="Direct link to Device geolocation">​</a>

Retrieve the device's current geographic coordinates independently of any anchor. The heading mode parameter controls how heading is computed:

- Camera Direction: Heading from the camera's forward axis. Best when the device is held upright in portrait or landscape orientation.
- Device Top: Heading from the top edge of the screen. Best when the device is face-up or for compass-style widgets.

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
if (vps2Manager.TryGetDeviceGeolocation(out var geolocation, HeadingMode.CameraDirection)) {
  // ...
}
```

</div>

</div>

#### Accuracy<a href="#accuracy" class="hash-link" aria-label="Direct link to Accuracy" title="Direct link to Accuracy">​</a>

The geolocation object contains a tracking state that can be `Unavailable`, `Coarse`, or `Precise`. These are broad categories describing the quality of VPS2's georeference estimate. Applications should rely on reported accuracy values rather than assuming centimeter-level global alignment.

Each estimate also includes accuracy values that represent margin-of-error estimates. Accuracy may vary across conversions performed with the same localization when using different input poses or locations.

- **Horizontal accuracy** (meters)
- **Vertical accuracy** (meters)
- **Heading / rotation accuracy** (degrees)

## Anchor geolocation<a href="#anchor-geolocation" class="hash-link" aria-label="Direct link to Anchor geolocation" title="Direct link to Anchor geolocation">​</a>

VPS2 anchor updates include geolocation data when it is available. Reading geolocation data directly from anchor updates is the most direct way to position anchors on a map.

Geolocation data is available for anchors in either `.limited` or `.tracked` tracking states, and will not change once it becomes available after a brief initialization period.

The guide for [placing virtual content with VPS2](https://www.nianticspatial.com/docs/nsdk/how-to/vps2/placing_virtual_content/) provides detailed steps on how to utilize VPS2 anchors. Following on this page is a simplified version covering just the APIs for getting geolocation.

Each frame, read the anchor's geolocation from its update:

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
if (anchor.trackingState == TrackingState.Tracking) {
    var geo = anchor.geolocation;
    if (geo.HasValue) {
        // Access geo.Value.Latitude, geo.Value.Longitude, geo.Value.Heading
    }
}
```

</div>

</div>

#### Accuracy<a href="#accuracy-1" class="hash-link" aria-label="Direct link to Accuracy" title="Direct link to Accuracy">​</a>

The accuracy of an anchor's geolocation depends on multiple factors, including the quality of GPS readings when the map the anchor is part of was created, and what algorithm was used to align the map. Currently, manually aligning the map in the Scaniverse Portal is how to obtain the most accurate anchor geolocations.

</div>

</div>
