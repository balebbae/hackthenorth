---
source: https://www.nianticspatial.com/docs/nsdk/features/vps2/
title: Visual Positioning System 2 (VPS2)
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Niantic Spatial VPS2

</div>

Niantic Spatial’s Visual Positioning System 2 (VPS2) helps an app estimate where the device is in the world, and place content at a stable position inside a mapped Site.

VPS2 combines device sensors, visual data, and cloud services to estimate location and place content. When a processed VPS map is available, VPS2 can also provide map-relative localization for that Site.

## Core concepts<a href="#core-concepts" class="hash-link" aria-label="Direct link to Core concepts" title="Direct link to Core concepts">​</a>

- **Geoposition**: Latitude, longitude, and altitude in a global coordinate system.
- **Heading**: Heading relative to geographic north.
- **Map-relative pose**: A full six-degree of freedom (6DOF) pose—position (x, y, z) and orientation (roll, pitch, yaw) expressed in the coordinate frame of a VPS map.
- **Coarse localization**: Global geoposition and heading without requiring a VPS map.
- **Precise localization**: Map-relative pose resolved against a VPS map.

## Localization modes<a href="#localization-modes" class="hash-link" aria-label="Direct link to Localization modes" title="Direct link to Localization modes">​</a>

VPS2 operates in two distinct modes, **Coarse** and **Precise**, depending on what data is available in the moment to estimate the device’s real-world position and heading.

### Coarse localization<a href="#coarse-localization" class="hash-link" aria-label="Direct link to Coarse localization" title="Direct link to Coarse localization">​</a>

Coarse localization provides a global geoposition (latitude/longitude/altitude) and heading. Notably, it:

- Works globally
- Does not require a VPS map
- Provides stable global alignment suitable for large-scale AR experiences

It operates through two methods:

**Local Sensor Fusion**

Formerly known as WPS (World Positioning System), this method fuses GPS and magnetometer data with device AR tracking locally on the device. It improves frame-to-frame stability beyond raw GPS and compass readings and is available globally without any cloud dependency.

**Cloud-based Geopositioning**

When enabled, VPS2 sends camera imagery to the cloud to compute an improved geoposition and heading. This can provide greater accuracy than local sensor fusion alone. Improvements are most apparent in dense urban environments, where multipath effects and signal obstruction frequently degrade GPS accuracy. Enable this via the `Universal Localization Enabled` configuration option.

**Network requirements:** VPS2 typically requires approximately four cloud localization requests per second during initialization to establish a stable initial geoposition and heading.

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Attention

</div>

<div class="admonitionContent_BuS1">

**Cold start**

In some regions, the first cloud geopositioning response may take 60 seconds or longer. Until this initial cloud response is received, global geoposition accuracy mirrors standard device GPS. This delay applies only to cloud-based coarse geopositioning. It does not affect VPS map localization once a VPS map is available and localization is attempted.

</div>

</div>

### Precise localization<a href="#precise-localization" class="hash-link" aria-label="Direct link to Precise localization" title="Direct link to Precise localization">​</a>

In areas where a VPS Site is available and has been fully processed from a Scaniverse capture, VPS2 can localize the device to that Site. When this succeeds, your app can place content at a stable position inside that Site.

VPS2 represents that stable position as a six-degree-of-freedom pose for the Site's default anchor in the device's local coordinate frame. Virtual objects placed relative to that anchor can be used in persistent and shared AR experiences. VPS2 handles the conversions between AR space, map space, and global coordinates.

Precise localization enables:

- High-precision AR content placement
- Persistent and shared anchors
- Stable alignment to mapped real-world environments

Additionally, when localized to a VPS map, VPS2 will often improve global geoposition and heading accuracy. However, improvements to absolute geoposition are not guaranteed, particularly for smaller maps.

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

Precise localization requires that your application has access to the Site. It does not start automatically. To start it, track one of the Site's anchors, such as the default anchor.

</div>

</div>

## Check device status and anchor status<a href="#check-device-status-and-anchor-status" class="hash-link" aria-label="Direct link to Check device status and anchor status" title="Direct link to Check device status and anchor status">​</a>

VPS2 reports device status and the status of each anchor you track. Do not use one as a substitute for the other. They are as follows:

| Status | API type | Values | Source | Question it answers |
|----|----|----|----|----|
| **Device localization** | `Vps2TrackingState` | `unavailable`, `coarse`, `precise` | VPS2 geoposition (GPS + cloud) | "How well does the device know where it is in the world?" |
| **Anchor tracking** | `VpsAnchorUpdate.AnchorTrackingState` | `notTracked`, `limited`, `tracked` | Per-anchor updates from the session's `anchorUpdated` stream | "Is this anchor ready for reliable content placement?" |

To decide whether content attached to a Site anchor is reliably placed, read the anchor's tracking state, not the device's `Vps2TrackingState` because these two statuses can change independently. For example, the device can report `precise` geoposition while a given anchor is still `limited` or `notTracked`. If your app shows a placement status such as `Localizing` or `Localized`, base its status on the anchor update, not on the device tracking state.

<div class="theme-admonition theme-admonition-warning admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>warning

</div>

<div class="admonitionContent_BuS1">

A device state of `coarse` or `precise` does not mean a Site anchor is ready for placement. Your app must track an anchor before VPS2 can place content at that Site. See [Anchors](#anchors) and [Place virtual content with VPS2](https://www.nianticspatial.com/docs/nsdk/how-to/vps2/placing_virtual_content/).

</div>

</div>

## Geo-alignment and absolute accuracy<a href="#geo-alignment-and-absolute-accuracy" class="hash-link" aria-label="Direct link to Geo-alignment and absolute accuracy" title="Direct link to Geo-alignment and absolute accuracy">​</a>

Each VPS map is aligned to geographic coordinates during processing. This alignment determines how map-relative poses convert to global latitude, longitude, altitude, and heading.

In the Scaniverse Web, you can manually adjust maps with the Georeference tool to better align the VPS map with geographic imagery. This adjustment affects global geoposition accuracy but does not change local map-relative accuracy. The following points are **important**:

- Satellite imagery is not guaranteed to be accurate and may be outdated.
- Satellite images typically show rooftops, which may occlude or obscure ground-level geometry.
- Indoor scans cannot always be precisely aligned to overhead imagery.
- Tall buildings and shadows can reduce visual clarity in satellite imagery.
- **Rotation accuracy is critical.** Small rotational misalignment between the VPS map and geographic north can produce increasing positional error as distance from the map origin increases. Positional offset remains constant, but rotational error is magnified as users move farther from the map center.

Global geoposition accuracy depends heavily on how precisely the VPS map is aligned to the real-world geographic coordinate system.

Applications should rely on:

- **Map-relative pose** for high-precision AR alignment.
- **Geoposition accuracy values** returned by the localization to evaluate global alignment reliability.

## Anchors<a href="#anchors" class="hash-link" aria-label="Direct link to Anchors" title="Direct link to Anchors">​</a>

An anchor represents a persistent real-world pose used to attach virtual content.

Anchor accuracy depends on the anchor's own tracking state, delivered as a `VpsAnchorUpdate.AnchorTrackingState` through the session's `anchorUpdated` updates:

- **`notTracked`**: The anchor is not currently being tracked; its pose is not usable.
- **`limited`**: The device is not localized to a VPS map. The anchor pose is estimated using coarse localization and will not be as accurate or as stable in comparison to a `tracked` state.
- **`tracked`**: The device is localized to a VPS map. The anchor pose provides stable map-relative alignment — this is the state to wait for before relying on placed content.

An anchor may transition between these states as map localization is gained or lost. These anchor tracking states let your app adapt its user interface based on how reliable the anchor pose is. Anchor tracking state is separate from the device's `Vps2TrackingState` — see [Check device status and anchor status](#check-device-status-and-anchor-status).

Anchor updates also include geolocation data directly, so you can access the anchor's geographic coordinates without performing a separate conversion.

## How VPS2 fits together<a href="#how-vps2-fits-together" class="hash-link" aria-label="Direct link to How VPS2 fits together" title="Direct link to How VPS2 fits together">​</a>

1.  The device runs local AR tracking.
2.  VPS2 establishes a global geoposition and heading (`Coarse`).
3.  If the app tracks a Site anchor and that Site has a processed VPS map, VPS2 can localize to that map.
4.  Anchors provide a pose and geolocation, resolved relative to either:
    - The global geoposition (`Limited`), or
    - The VPS map (`Tracked`).
5.  The device's current geolocation and heading are available via VPS2 at any time, with variable accuracy depending on VPS2's current tracking state.

VPS2 reports errors through `LocalizationError` when a localization request fails.

## Best practices<a href="#best-practices" class="hash-link" aria-label="Direct link to Best practices" title="Direct link to Best practices">​</a>

**Camera orientation:** Hold the device upright at approximately eye level, pointing toward visually distinctive features. Avoid low-texture surfaces, ground-only views, or sky.

## Next steps<a href="#next-steps" class="hash-link" aria-label="Direct link to Next steps" title="Direct link to Next steps">​</a>

**End-to-end guide:**

- [First localization with NSDK](https://www.nianticspatial.com/docs/nsdk/first_localization/)

**Using VPS2 with the Niantic SDK:**

- [Get started with VPS2](https://www.nianticspatial.com/docs/nsdk/how-to/vps2/adding_vps2/)
- [Use geoposition with VPS2](https://www.nianticspatial.com/docs/nsdk/how-to/vps2/getting_vps2_geoposition/)
- [Place virtual content with VPS2](https://www.nianticspatial.com/docs/nsdk/how-to/vps2/placing_virtual_content/)

</div>

</div>
