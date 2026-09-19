---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/use-ardk-depths-if-platform-unavailable/
title: use-ardk-depths-if-platform-unavailable
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[ScannerConfig](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[useArdkDepthsIfPlatformUnavailable](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/use-ardk-depths-if-platform-unavailable/)

<div>

# useArdkDepthsIfPlatformUnavailable

</div>

\[androidJvm\]\
var [useArdkDepthsIfPlatformUnavailable](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/use-ardk-depths-if-platform-unavailable/): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a>

Whether to use and record NSDK's estimated depths, if platform depths are unavailable.

Depths are recorded as part of the scan data, and are also required to generate voxels or raycast visualization images. If NSDK was configured to use platform depths, this value is ignored, and depths are expected to come through the scanning session. Otherwise:

- When `true`, NSDK will generate estimated depths for use by the scanning feature
- When `false`, the scanning feature will not be able to generate voxels or raycast visualization images, but will still be able to record other scan data.

**Attention:** If NSDK depth is being recorded because [useArdkDepthsIfPlatformUnavailable](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/use-ardk-depths-if-platform-unavailable/) is `true` and lidar is unavailable, the recording FPS will be limited to the update rate of the depth feature, which defaults to 10 FPS. To change the update rate of the depth feature, set [DepthConfig.framerate](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-depth-config/framerate/) to match [framerate](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/framerate/).

**Default:**`false`

</div>

</div>
