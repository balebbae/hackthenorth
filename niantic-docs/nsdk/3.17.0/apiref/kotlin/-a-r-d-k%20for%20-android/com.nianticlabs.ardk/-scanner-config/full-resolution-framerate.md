---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/full-resolution-framerate/
title: full-resolution-framerate
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[ScannerConfig](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[fullResolutionFramerate](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/full-resolution-framerate/)

<div>

# fullResolutionFramerate

</div>

\[androidJvm\]\
var [fullResolutionFramerate](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/full-resolution-framerate/): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a>

Target FPS for full resolution frame recording.

The target framerate for recording full resolution frames when [enableFullResolution](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/enable-full-resolution/) is `true`. The actual framerate for full-resolution frames may differ from the target framerate.

**Note:** Recording NSDK depth with [useArdkDepthsIfPlatformUnavailable](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/use-ardk-depths-if-platform-unavailable/) can result in a lower recording FPS than the target framerate.

**Default:**`0` (defaults to 2 FPS)

</div>

</div>
