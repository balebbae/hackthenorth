---
source: https://www.nianticspatial.com/docs/nsdk/release_notes/
title: Release Notes
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Release Notes

</div>

## Version 4.1.0<a href="#version-410" class="hash-link" aria-label="Direct link to Version 4.1.0" title="Direct link to Version 4.1.0">​</a>

### Highlights<a href="#highlights" class="hash-link" aria-label="Direct link to Highlights" title="Direct link to Highlights">​</a>

- [Scaniverse now available on Android](#scaniverse-android-support)
- [Meta Quest 3 support restored](#meta-quest-3)
- [iOS simulator support for x86_64](#ios-simulator-support-for-x86_64)
- [New Kotlin wayfinding guide](#kotlin-vps2-sample)
- [Updated Unity version to 6000.0.74f1](#unity-version-update)

### Features/Fixes<a href="#featuresfixes" class="hash-link" aria-label="Direct link to Features/Fixes" title="Direct link to Features/Fixes">​</a>

#### Scaniverse Android support<a href="#scaniverse-android-support" class="hash-link" aria-label="Direct link to Scaniverse Android support" title="Direct link to Scaniverse Android support">​</a>

- Scaniverse is now available on supported Android devices. The new experience enables users to capture scans, upload them, generate assets, and test localization as part of the new enterprise workflow.

#### Meta Quest 3<a href="#meta-quest-3" class="hash-link" aria-label="Direct link to Meta Quest 3" title="Direct link to Meta Quest 3">​</a>

- NSDK version 4.1 restores support for Meta Quest 3.

#### iOS Simulator support for x86_64<a href="#ios-simulator-support-for-x86_64" class="hash-link" aria-label="Direct link to iOS Simulator support for x86_64" title="Direct link to iOS Simulator support for x86_64">​</a>

- Added x86_64 iOS Simulator support to improve simulator-based development.

#### Kotlin VPS2 Sample<a href="#kotlin-vps2-sample" class="hash-link" aria-label="Direct link to Kotlin VPS2 Sample" title="Direct link to Kotlin VPS2 Sample">​</a>

- A new end-to-end <a href="https://github.com/nianticspatial/nsdk-samples-kotlin" target="_blank" rel="noopener noreferrer">Kotlin wayfinding guide</a> demonstrates how to create a wayfinding app using VPS2.

#### Unity version update<a href="#unity-version-update" class="hash-link" aria-label="Direct link to Unity version update" title="Direct link to Unity version update">​</a>

- Updated the supported Unity version to **6000.0.74f1**.

### Known Issues<a href="#known-issues" class="hash-link" aria-label="Direct link to Known Issues" title="Direct link to Known Issues">​</a>

- Meta Quest 3: Force the OpenXR Plugin (`com.unity.xr.openxr`) to version **1.15.1**. Version 1.16.1 is incompatible and will cause issues.
- Importing the NSDK UPM in a project started from Universal 3D template might cause a few build errors reported in the console. Restarting the editor should fix this.
- Playback rendering on Android native may not match live results. Some features, such as occlusion, may not function as expected. Improvements are planned in a future update.
- On iPad Pro running iOS 17 in the Unity External Sample, rotating the device from landscape to portrait may cause a soft lock and screen flickering.

</div>

</div>
