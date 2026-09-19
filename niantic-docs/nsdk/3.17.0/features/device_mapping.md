---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/features/device_mapping/
title: Device Mapping
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Device Mapping

</div>

## What is Device Mapping?<a href="#what-is-device-mapping" class="hash-link" aria-label="Direct link to What is Device Mapping?" title="Direct link to What is Device Mapping?">​</a>

Device Mapping is a system that scans and tracks real-world objects, allowing you to place content in alignment with the real world. On the surface, it is functionally similar to [VPS](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/lightship_vps/), but the Device Mapping system does all of its processing on the device and does not require a network connection to localize. Instead, Device Mapping provides scanned maps as serializable objects that a client device can distribute to others, which can then deserialize and recreate the scanned map. Multiple devices can share a map without relying on Niantic VPS servers, which allows for immediate multiplayer experiences anywhere, even with no previous VPS-Activated location. See the **DeviceMappingColocalization** demo scene for sample usage of Device Mapping and sharing over Niantic Spatial Platform's Shared AR library.

For a better idea of how Device Mapping works, compare it to VPS:

|  | VPS | Device Mapping |
|----|----|----|
| Where can you use it? | VPS-Activated Locations Only | Anywhere |
| How is the map built? | Using scans from many users at different times | A single scan |
| Do you need to scan a local map before localizing? | No | Yes |
| Do you need to communicate with Niantic VPS Servers? | Yes | No |
| Where does the map data live? | Niantic servers | Your device |
| Localization robustness? | Consistent because it generates the map from multiple scans | Robustness depends on the quality of the single scan |
| How to access associated visual data? | Download mesh from the internet | Extract point cloud from device map data |

## Limitations<a href="#limitations" class="hash-link" aria-label="Direct link to Limitations" title="Direct link to Limitations">​</a>

Device Mapping is subject to some of the same localization limitations as VPS, such as:

- Visual conditions (lighting, weather, time of day) changing between mapping and localization
- Mapped areas with few distinguishing features (such as grassy fields or indoor areas with little difference in color)
- Scans taken from a limited viewing angle

Without the robustness of generating the map from multiple scans, Device Mapping may perform worse than VPS if these limitations come into play. If your multiplayer experience depends on an area that changes regularly or lacks distinguishing features, consider using VPS instead.

</div>

</div>
