---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/xr_settings/
title: Niantic SDK Settings
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Niantic SDK Settings

</div>

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

You will need a Unity project with NSDK enabled. For more information, see [Setting up an AR Project](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/).

To navigate to **Niantic Lightship SDK Settings**, select **Lightship** \> **Settings** from the top menu bar.

## SDK Status Indicators<a href="#sdk-status-indicators" class="hash-link" aria-label="Direct link to SDK Status Indicators" title="Direct link to SDK Status Indicators">​</a>

At the top of the Settings window, there are three indicators which show whether NSDK is enabled for development in the editor, Android deployment, and iOS deployment. If the plug-in is not enabled for a specific platform, the corresponding indicator will become a button leading to the **Project Validation** window where you can see more details and enable Lightship SDK.

<img src="https://www.nianticspatial.com/docs/assets/images/sdk_status_indicators-cf6bdd27bd8e00d031f65e085da0c032.png" width="600" alt="SDK Status Indicators" />

## Credentials<a href="#credentials" class="hash-link" aria-label="Direct link to Credentials" title="Direct link to Credentials">​</a>

The **Get API Key** button links directly to the Projects page on the lightship.dev website which will redirect you to scaniverse.nianticspatial.com. There, you can copy an existing key from your account or create a new one for free. Use the text field in Lightship Settings to add your API key from your Developer Account.

<img src="https://www.nianticspatial.com/docs/assets/images/sdk_credentials-5a2391462db6f1513f31c706bbd0f10e.png" width="600" alt="SDK Credentials" />

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

An API key is required to build your Unity project. It is also required to develop with certain features within the Unity Editor, such as [Niantic Spatial VPS](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/lightship_vps/).

</div>

</div>

## Feature Toggles<a href="#feature-toggles" class="hash-link" aria-label="Direct link to Feature Toggles" title="Direct link to Feature Toggles">​</a>

These settings allow you to enable and disable individual NSDK features in your project.

<img src="https://www.nianticspatial.com/docs/assets/images/sdk_features-7ac56f5b72df76b0f73606490024c610.png" width="600" alt="SDK Feature Toggles" />

For more on each feature, see their documentation pages:

- [Depth](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/depth/)
- [Scene Segmentation](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/semantics/)
- [Meshing](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/meshing/)
- [Persistent Anchors](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/lightship_vps/)
- [Object Detection](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/object_detection/)

### Prefer LiDAR If Available<a href="#prefer-lidar-if-available" class="hash-link" aria-label="Direct link to Prefer LiDAR If Available" title="Direct link to Prefer LiDAR If Available">​</a>

When the depth toggle is enabled, the depth information returned by the ARFoundation API will come from NSDK's depth prediction algorithms. This option overrides that information and replaces it with depth data received directly from the mobile device's lidar sensor (if it has one).

## Playback<a href="#playback" class="hash-link" aria-label="Direct link to Playback" title="Direct link to Playback">​</a>

This section contains controls for configuring Playback. For more information on this feature, see the [Playback feature page](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/playback/).

For developers who want to use playback during development but use a live camera feed when deployed, NSDK provides two sets of Playback settings; one for the Unity Editor, the other for physical devices.

<img src="https://www.nianticspatial.com/docs/assets/images/sdk_playback-c08b334c656e4931916ad51e336f1bf4.png" width="600" alt="SDK Playback Settings" />

### Dataset Path<a href="#dataset-path" class="hash-link" aria-label="Direct link to Dataset Path" title="Direct link to Dataset Path">​</a>

Use the **Browse** button to select a dataset on your computer. The path must be to a directory that contains a `capture.json` file. It can exist anywhere in your file system, not just within the Unity project folder.

### Run Manually<a href="#run-manually" class="hash-link" aria-label="Direct link to Run Manually" title="Direct link to Run Manually">​</a>

For debugging purposes, it may be useful to step through a recording one frame at a time. When this setting is enabled, your simulated camera feed will start before the first frame on a blank screen. From there, press the space bar to advance the recording one frame at a time.

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

If using Playback on device, use a two-finger tap instead of space bar to step through the frames.

</div>

</div>

### Loop Infinitely<a href="#loop-infinitely" class="hash-link" aria-label="Direct link to Loop Infinitely" title="Direct link to Loop Infinitely">​</a>

Enabling this makes the dataset loop forever to facilitate sessions that last longer than the recording. To prevent instantaneous teleportation from the end to the start, the recording will play back in reverse until it reaches the beginning, then play forwards again.

## Logging<a href="#logging" class="hash-link" aria-label="Direct link to Logging" title="Direct link to Logging">​</a>

For debugging purposes, you may want more or less visibility from NSDK logs. We recommend leaving these settings on **Warn**, **Error**, or **Off** to prevent noisiness in the console.

<img src="https://www.nianticspatial.com/docs/assets/images/sdk_logging-56bbe06543a0fa8fb0ac9b2597a4a6d6.png" width="600" alt="SDK Logging Settings" />

## Simulation<a href="#simulation" class="hash-link" aria-label="Direct link to Simulation" title="Direct link to Simulation">​</a>

The bottom section of the Settings window is relevant only when **Lightship Simulation** is enabled. For more information, see the [Simulation feature page](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/simulation/).

<img src="https://www.nianticspatial.com/docs/assets/images/sdk_simulation-eef8584292b48d099099ff1113d5d36f.png" width="600" alt="SDK Simulation Settings" />

Like the main SDK status indicators, the first section of the Simulation settings shows whether the **Niantic Lightship Simulation** loader is enabled. If it is not, the indicator will link to the **XR Plug-in Management** window where it can be turned on.

### Z-Buffer Depth<a href="#z-buffer-depth" class="hash-link" aria-label="Direct link to Z-Buffer Depth" title="Direct link to Z-Buffer Depth">​</a>

Using Simulation enables you to develop in-editor with all of the NSDK prediction algorithms running in realtime on the simulated frames. However, depth prediction may struggle with simpler environments, or you may want to more closely emulate the behavior on a lidar-equipped device. Enabling **Z-Buffer Depth** allows you to work with the "true" or "perfect" depth data of objects in the environment relative to the simulated device.

### Persistent Anchors<a href="#persistent-anchors" class="hash-link" aria-label="Direct link to Persistent Anchors" title="Direct link to Persistent Anchors">​</a>

When using Simulation with VPS, **Simulation Persistent Anchors** makes development easier by replacing the live **Persistent Anchors** system with a mock one that behaves in a predetermined way.

<img src="https://www.nianticspatial.com/docs/assets/images/sdk_simulation_vps_params-9683b87699ff97d4469f59a3eb10768d.png" width="600" alt="SDK Simulation Persistent Anchor Parameters" />

Use the **Simulation Persistent Anchor Parameters** to dictate how a mock localization attempt should resolve. Simulation can be configured to localize within a specified amount of time, track with a random offset, or surface a failure to help simulate real-world scenarios.

See [Simulation Settings](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/unity/simulation_mocking/#lightship-simulation-settings) for more information.

</div>

</div>
