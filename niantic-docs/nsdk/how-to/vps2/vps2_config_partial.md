---
source: https://www.nianticspatial.com/docs/nsdk/how-to/vps2/vps2_config_partial/
title: vps2_config_partial
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# vps2_config_partial

</div>

#### Configuration Fields<a href="#configuration-fields" class="hash-link" aria-label="Direct link to Configuration Fields" title="Direct link to Configuration Fields">​</a>

- **Universal Localization Enabled:** This field enables Cloud-based Geopositioning. When active, VPS2 sends AR sensor data and camera imagery to the server to calculate the device’s absolute geographic coordinates and heading. This method can improve geoposition accuracy beyond local sensor fusion but requires a network connection. If disabled, the system relies exclusively on local sensor fusion.

  - **Universal Localization Requests per Second:** (Default: 1) Frequency of cloud geopositioning requests.

- **VPS Map Localization Enabled:** When active, the system localizes the device against VPS maps to achieve “precise” localization.

  - **Initial Requests per Second:** (Default: 1.0) Server request frequency prior to the first successful VPS map localization. (For example, 1.0 = 1 request per second.)
  - **Continuous Requests per Second:** (Default: 0.2) Server request frequency after the initial localization. (For example, 0.2 = 1 request every 5 seconds.)

- **Geolocation Smoothing Enabled:** Enables interpolation between localization updates. This minimizes “snapping” or visual jumps during abrupt GPS or compass recalibrations, ensuring a stable AR experience.

</div>

</div>
