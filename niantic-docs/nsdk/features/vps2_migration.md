---
source: https://www.nianticspatial.com/docs/nsdk/features/vps2_migration/
title: Migrate from VPS to VPS2
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Migrate from VPS to VPS2

</div>

## What changed in NSDK 4.x<a href="#what-changed-in-nsdk-4x" class="hash-link" aria-label="Direct link to What changed in NSDK 4.x" title="Direct link to What changed in NSDK 4.x">​</a>

This guide is for developers migrating from Unity ARDK 3.x to NSDK 4.x.

In NSDK 4.x, VPS and WPS are unified into a single system called **VPS2**. Instead of using separate APIs for localization and geopositioning, all functionality is now handled through [ARVps2Manager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager/).

This change:

- Replaces separate VPS and WPS APIs with a single unified API.
- Consolidates localization, geoposition, and anchor workflows.
- Simplifies configuration and runtime behavior.

For a full overview of VPS2 capabilities, see the [VPS2 feature page](https://www.nianticspatial.com/docs/nsdk/features/vps2/).

## Migration steps<a href="#migration-steps" class="hash-link" aria-label="Direct link to Migration steps" title="Direct link to Migration steps">​</a>

1.  [Set up Sites in Scaniverse](#set-up-sites-in-scaniverse) - Move location management to Scaniverse before you update Unity-side integration.
2.  [Update core APIs to VPS2](#update-core-apis-to-vps2) - Replace legacy VPS and WPS managers with the unified VPS2 entry point.
3.  [Update device mapping](#update-device-mapping) - Update how you load, convert, and save device maps if your app uses Device Mapping.
4.  [Update geoposition and coordinate conversion](#update-geoposition-and-coordinate-conversion) - Replace legacy AR to geoposition helper APIs with localization-based conversions.
5.  [Replace VPS Coverage API with Sites API](#replace-vps-coverage-api-with-sites-api) - Replace older discovery flows when you need Scaniverse-created Sites.
6.  [Update configuration and events](#update-configuration-and-events) - Update event handling and remove configuration that VPS2 now manages internally.

## Set up Sites in Scaniverse<a href="#set-up-sites-in-scaniverse" class="hash-link" aria-label="Direct link to Set up Sites in Scaniverse" title="Direct link to Set up Sites in Scaniverse">​</a>

Complete this step first if your Unity project depends on locations created, discovered, or activated through the Geospatial Browser (GSB). In NSDK 4.x, Scaniverse is the system of record for creating and managing Sites and their assets.

<div class="theme-admonition theme-admonition-warning admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Geospatial Browser is no longer available

</div>

<div class="admonitionContent_BuS1">

The Geospatial Browser workflows used by older projects are no longer available. Use Scaniverse to create and manage Sites, and use the Sites API to retrieve production anchor payloads. If your project previously used GSB locations or imported location packages, follow the migration steps on this page.

</div>

</div>

Use **Scaniverse** to manage VPS maps and Sites, then update your Unity workflow to use those Sites.

For instructions on creating a Scaniverse account, creating Sites, and managing mapped locations, see [First Localization with NSDK](https://www.nianticspatial.com/docs/nsdk/first_localization/).

If you have saved payloads from VPS locations discovered or activated through GSB, those payloads remain valid and can still be used for localization.

## Update core APIs to VPS2<a href="#update-core-apis-to-vps2" class="hash-link" aria-label="Direct link to Update core APIs to VPS2" title="Direct link to Update core APIs to VPS2">​</a>

Replace your ARDK 3.x VPS and WPS components with the unified VPS2 API before migrating downstream localization and anchor logic. In NSDK 4.x, [ARVps2Manager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager/) is the primary Unity entry point for VPS2 functionality.

In NSDK 4.x, localization, geopositioning, and anchor management are handled through a single VPS2 session.

Use the following table to replace each legacy manager or workflow in your project with its NSDK 4.x equivalent.

| ARDK 3.x | NSDK 4.x | Details |
|----|----|----|
| ARPersistentAnchorManager, ARLocationManager | [ARVps2Manager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager/) | Use VPS2 to manage Site-based localization and anchor tracking |
| ARWorldPositioningManager | [ARVps2Manager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager/) | VPS and WPS functionality are unified under a single manager |
| ARLocation + ARLocationManager + imported GSB location package | [ARVps2Manager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager/) + tracked Site anchor | Retrieve the Site's production anchor payload from Scaniverse or the Sites API, track it with VPS2, and place content relative to the tracked anchor. |

## Update device mapping<a href="#update-device-mapping" class="hash-link" aria-label="Direct link to Update device mapping" title="Direct link to Update device mapping">​</a>

Complete this step if your app uses Device Mapping. The data can still be migrated, but you need to update how you load maps, create anchors, and save map data in NSDK 4.x.

Use the following table to replace each Device Mapping API or data expectation in your migration.

| ARDK 3.x | NSDK 4.x | Details |
|----|----|----|
| ARPersistentAnchorManager | [ARVps2Manager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager/) | Use VPS2 to track anchors with Device Mapping |
| ARDeviceMappingManager | ARDeviceMappingManager | No change |
| ARDeviceMap | Serialized data as `byte[]` | Pass serialized Device Map bytes directly to `DeviceMapAccessController.AddMap()` |
| Multiple anchors in ARDeviceMap | One "root" anchor | Call `DeviceMapAccessController.CreateRootAnchor()` after setting the Device Map to generate the anchor payload |

NSDK 4.x uses a different serialization format than ARDK 3.x, but serialized Device Mapping data from ARDK 3.x can still be migrated. Pass the byte array returned from `ARDeviceMap.Serialize()` to `DeviceMapAccessController.AddMap()`, and NSDK 4.x converts it internally the first time it is loaded.

If you save maps at the end of a session, update that code too. `ARDeviceMappingManager.MapFinalized` now delivers delta data instead of a full map, so call `ARDeviceMappingManager.TryGetMapData()` when you need the complete Device Map byte array.

## Update geoposition and coordinate conversion<a href="#update-geoposition-and-coordinate-conversion" class="hash-link" aria-label="Direct link to Update geoposition and coordinate conversion" title="Direct link to Update geoposition and coordinate conversion">​</a>

In VPS2, anchor updates include geolocation data directly and `TryGetDeviceGeolocation()` replaces pose-based device geolocation. These two changes replace most legacy conversion workflows. `TryGetPose()` remains available as a convenience for converting arbitrary geographic coordinates to AR poses.

Use the following table to replace each legacy conversion helper in your project.

| ARDK 3.x | NSDK 4.x | Details |
|----|----|----|
| ARWorldPositioningObjectHelper | Anchor geolocation data | Attach content to anchors and read geolocation from anchor updates |

\| ARWorldPositioningObjectHelper (arbitrary geo coords) \| [ARVps2Manager.TryGetPose()](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager.TryGetPose/) \| Converts geographic coordinates to AR coordinates and updates the `GameObject` transform \| \| ARWorldPositioningCameraHelper \| [ARVps2Manager.TryGetDeviceGeoLocation()](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager.TryGetDeviceGeolocation/) \| Retrieve the device’s geographic location and heading\|

For most use cases, attach content to VPS2 anchors and read geolocation from anchor updates — no manual coordinate conversion is needed.

If you need to convert arbitrary geographic coordinates to AR poses or retrieve the device's current geolocation independently, see [Geolocate with VPS2](https://www.nianticspatial.com/docs/nsdk/how-to/vps2/getting_vps2_geoposition/).

## Replace VPS Coverage API with Sites API<a href="#replace-vps-coverage-api-with-sites-api" class="hash-link" aria-label="Direct link to Replace VPS Coverage API with Sites API" title="Direct link to Replace VPS Coverage API with Sites API">​</a>

Update this part of your app if you currently query nearby VPS locations or anchor payloads through the VPS Coverage API. This matters because Scaniverse-created Sites are not discoverable through the old GSB-based coverage flow.

Use [Sites API](https://www.nianticspatial.com/docs/nsdk/features/sites/) when you need to query Scaniverse-managed Sites and retrieve the VPS anchor payload data that your app should localize against.

The VPS Coverage API remains available for querying VPS locations and anchors near the user at runtime. However, it only returns locations that were created or activated through GSB. VPS locations created on Scaniverse are not supported. It will be replaced by a unified Sites API in a future release.

With **Scaniverse**, Sites replace the VPS location and test-scan workflows that previously depended on GSB. If your migration includes newly created Sites in Scaniverse, move your discovery logic to Sites-based queries instead of relying on coverage results.

## Update configuration and events<a href="#update-configuration-and-events" class="hash-link" aria-label="Direct link to Update configuration and events" title="Direct link to Update configuration and events">​</a>

Update this code after the core API migration so your runtime behavior still matches user expectations. In VPS2, anchor updates are consolidated and several old configuration properties are no longer set manually.

### Update anchor events<a href="#update-anchor-events" class="hash-link" aria-label="Direct link to Update anchor events" title="Direct link to Update anchor events">​</a>

Use the following table to replace legacy anchor and location tracking event handlers.

| ARDK 3.x | NSDK 4.x | Details |
|----|----|----|
| `arPersistentAnchorStateChanged` event in ARPersistentAnchorManager | `ARVps2Manager.trackablesChanged` event | `trackablesChanged` delivers anchor add, update, and remove events together |
| `locationTrackingStateChanged` event in ARLocationManager | `ARVps2Manager.trackablesChanged` event | Check changed anchors in `trackablesChanged` and inspect whether the tracking state is `Tracked` |

Anchor add, update, and removal remain conceptually consistent with legacy VPS, but tracking quality reporting is different. Anchors can surface coarse poses even when the device is not yet localized to a VPS map.

Handle the tracking state accordingly:

- Treat `Limited` as a coarse pose that is not yet fully tracked against the VPS map.
- Treat `Tracked` as the state where the anchor is tracking against the VPS map.

### Update configuration properties<a href="#update-configuration-properties" class="hash-link" aria-label="Direct link to Update configuration properties" title="Direct link to Update configuration properties">​</a>

Search your project for VPS configuration code and update the remaining properties first, then remove settings that VPS2 now manages internally. This prevents you from carrying forward configuration that no longer has any effect.

Use the following table to replace the remaining configurable properties.

| ARDK 3.x | NSDK 4.x | Details |
|----|----|----|
| Initial Service Request Interval Seconds | Initial Vps Requests Per Second | Unit changed from interval to requests per second |
| Continuous Service Request Interval Seconds | Continuous Vps Requests Per Second | Unit changed from interval to requests per second |

Then remove the following properties from your project because VPS2 always enables them or manages them internally:

- Continuous Localization Enabled (Continuous localization is always enabled in VPS2)
- Temporal Fusion Enabled (Temporal fusion is always enabled in VPS2)
- Interpolation Enabled (Interpolation is always enabled in VPS2)
- Diagnostics Enabled
- Gps Correction For Continuous Localization
- Vps Usage Mode
- Jpeg Compression Quality

Configuration changes are applied immediately at runtime and no longer require restarting subsystems.

</div>

</div>
