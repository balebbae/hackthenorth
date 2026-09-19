---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/features/world_pose/
title: World Pose System (WPS)
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# World Pose System (WPS)

</div>

## What is WPS?<a href="#what-is-wps" class="hash-link" aria-label="Direct link to What is WPS?" title="Direct link to What is WPS?">​</a>

The World Pose System (WPS) provides the 3D position and orientation of the phone in geographic coordinates as an alternative to using device GPS and compass heading data. WPS leverages device AR tracking data to provide greater frame-to-frame stability than relying on GPS and compass alone, making it more suitable for AR applications. As the user moves around, WPS continuously maintains the device's position and orientation, improving stability and accuracy over long periods of time and long distances.

WPS will work in any location where the phone has a GPS signal, but positional accuracy will vary depending on GPS accuracy.

## What can WPS be used for?<a href="#what-can-wps-be-used-for" class="hash-link" aria-label="Direct link to What can WPS be used for?" title="Direct link to What can WPS be used for?">​</a>

Any application that uses GPS, compass heading, and camera data for maintaining geographic positioning and orientation can be improved by the increased stability and accuracy that WPS provides. WPS is especially well-suited for powering world-scale AR experiences, such as AR navigation between geographic coordinates, or viewing and interacting with geo-anchored AR content.

To see some of the WPS use cases in action, try out the [Sample Project](https://www.nianticspatial.com/docs/nsdk/3.17.0/sample_projects/).

The improvements to orientation stability granted by WPS can be seen in the image below.

<img src="https://www.nianticspatial.com/docs/assets/images/world_positioning_compass-ee70771dbe638adcd9d02a14e986f5c6.gif" width="350" alt="Side-by-Side showing world pose against the device compass" />

## How does the World Pose System work?<a href="#how-does-the-world-pose-system-work" class="hash-link" aria-label="Direct link to How does the World Pose System work?" title="Direct link to How does the World Pose System work?">​</a>

WPS combines GPS, compass heading, and ARKit/ARCore tracking data from the session to produce a more accurate and stable result. WPS requires the camera to be enabled for the ARKit/ARCore tracking, but the camera view doesn’t need to be visible to the user.

## WPS FAQ<a href="#wps-faq" class="hash-link" aria-label="Direct link to WPS FAQ" title="Direct link to WPS FAQ">​</a>

### Why use WPS instead of the device GPS and compass heading?<a href="#why-use-wps-instead-of-the-device-gps-and-compass-heading" class="hash-link" aria-label="Direct link to Why use WPS instead of the device GPS and compass heading?" title="Direct link to Why use WPS instead of the device GPS and compass heading?">​</a>

WPS provides a more stable and accurate compass heading and latitude/longitude position than is available from standard platform APIs. It fuses GPS and compass data with AR tracking and camera frame data, making it more suitable for use cases that require frame-to-frame stability, such as rendering world-anchored virtual content. It also provides a consistent API across all supported platforms, along with helper utilities to simplify working with geographic data and device-specific GPS considerations.

### Under what conditions will WPS not work at all?<a href="#under-what-conditions-will-wps-not-work-at-all" class="hash-link" aria-label="Direct link to Under what conditions will WPS not work at all?" title="Direct link to Under what conditions will WPS not work at all?">​</a>

WPS will fail when there is no GPS signal or when the AR tracking cannot work reliably. GPS will usually be unavailable when the device is underground or inside some buildings. AR tracking will often fail in darkness, in moving vehicles, and when the user obscures the camera. Avoiding these situations will ensure that apps work reliably.

### How much data does WPS transfer?<a href="#how-much-data-does-wps-transfer" class="hash-link" aria-label="Direct link to How much data does WPS transfer?" title="Direct link to How much data does WPS transfer?">​</a>

WPS processes all data locally on the device. Any data that WPS transfers is for telemetry purposes only.

### How will WPS impact device performance and battery life?<a href="#how-will-wps-impact-device-performance-and-battery-life" class="hash-link" aria-label="Direct link to How will WPS impact device performance and battery life?" title="Direct link to How will WPS impact device performance and battery life?">​</a>

WPS uses approximately 10% of one CPU thread and should not have a significant impact on any application that is already using ARKit/ARCore. Its battery consumption is comparable to that of the screen and 3D rendering, so it is suitable for long sessions.

### How accurate is WPS?<a href="#how-accurate-is-wps" class="hash-link" aria-label="Direct link to How accurate is WPS?" title="Direct link to How accurate is WPS?">​</a>

Orientation Accuracy: The orientation accuracy of WPS depends on the quality of the device’s magnetometer, as well as local conditions that may affect compass readings, but it is consistently more accurate than raw magnetometer readings, offering a more stable experience. In benchmark studies we conducted across more than 50 primarily urban and suburban scenes, WPS has a median and 90th percentile orientation accuracy of 3 degrees/11 degrees, compared to 5 degrees/24 degrees for the device compass.

Positional Accuracy: Likewise, the positional accuracy of WPS depends on the quality of the GPS signal. WPS has a median and 90th percentile positional accuracy of 4 meters/11 meters, compared to 5 meters/16 meters for the device compass.

</div>

</div>
