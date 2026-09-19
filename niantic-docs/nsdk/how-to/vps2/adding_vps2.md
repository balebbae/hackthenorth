---
source: https://www.nianticspatial.com/docs/nsdk/how-to/vps2/adding_vps2/
title: Get started with VPS2
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Get started with VPS2

</div>

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

This guide assumes that you have already completed:

- [Set up the Niantic SDK for Unity](https://www.nianticspatial.com/docs/nsdk/setup/#set-up-the-niantic-sdk-for-unity)
- [Authorization](https://www.nianticspatial.com/docs/nsdk/auth_getting_started/)

## Adding VPS2 to your projects<a href="#adding-vps2-to-your-projects" class="hash-link" aria-label="Direct link to Adding VPS2 to your projects" title="Direct link to Adding VPS2 to your projects">​</a>

The Niantic Spatial Unity SDK (NSDK) uses AR Foundation as the interface for exposing its features. Adding VPS2 is therefore similar to adding other AR Foundation components.

#### ARVps2Manager<a href="#arvps2manager" class="hash-link" aria-label="Direct link to ARVps2Manager" title="Direct link to ARVps2Manager">​</a>

`ARVps2Manager` is a <a href="https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/manual/architecture/managers.html#trackables-and-trackable-managers" target="_blank" rel="noopener noreferrer">trackable manager</a> that manages georeferenced anchors. An anchor represents a real-world pose that the device maintains over time. With VPS2, anchors can be persisted and shared across AR sessions.

The manager can also convert between local AR poses and global geopositions (and vice versa).

<img src="https://www.nianticspatial.com/docs/assets/images/vps2_manager-d7cbe07c538eef5f568020ff231d97e9.png" style="width:75.0%" alt="AR VPS2 Manager Component" />

#### Configuration Fields<a href="#configuration-fields" class="hash-link" aria-label="Direct link to Configuration Fields" title="Direct link to Configuration Fields">​</a>

- **Universal Localization Enabled:** This field enables Cloud-based Geopositioning. When active, VPS2 sends AR sensor data and camera imagery to the server to calculate the device’s absolute geographic coordinates and heading. This method can improve geoposition accuracy beyond local sensor fusion but requires a network connection. If disabled, the system relies exclusively on local sensor fusion.

  - **Universal Localization Requests per Second:** (Default: 1) Frequency of cloud geopositioning requests.

- **VPS Map Localization Enabled:** When active, the system localizes the device against VPS maps to achieve “precise” localization.

  - **Initial Requests per Second:** (Default: 1.0) Server request frequency prior to the first successful VPS map localization. (For example, 1.0 = 1 request per second.)
  - **Continuous Requests per Second:** (Default: 0.2) Server request frequency after the initial localization. (For example, 0.2 = 1 request every 5 seconds.)

- **Geolocation Smoothing Enabled:** Enables interpolation between localization updates. This minimizes “snapping” or visual jumps during abrupt GPS or compass recalibrations, ensuring a stable AR experience.

## Starting and Stopping VPS2<a href="#starting-and-stopping-vps2" class="hash-link" aria-label="Direct link to Starting and Stopping VPS2" title="Direct link to Starting and Stopping VPS2">​</a>

VPS2 starts and stops according to the Unity component lifecycle. When started, the system begins collecting sensor data required for localization. Coarse positioning estimates are typically available within a few seconds after the AR session begins running.

When stopped, all anchor state is reset.

Configuration changes to `ARVps2Manager` are applied only when the component starts and cannot be modified while it is running.

</div>

</div>
