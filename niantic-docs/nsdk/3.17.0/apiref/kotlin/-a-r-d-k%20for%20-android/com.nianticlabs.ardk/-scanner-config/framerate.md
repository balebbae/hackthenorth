---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/framerate/
title: framerate
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[ScannerConfig](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[framerate](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/framerate/)

<div>

# framerate

</div>

\[androidJvm\]\
var [framerate](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/framerate/): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a>

Target FPS for recording and visualization processes.

The target framerate is the cap for how often the feature will process new input frames. The actual framerate may differ. If set to `0`, this defaults to 30 FPS. The recording FPS cannot exceed the rate at which frames are delivered to the scanning session.

**Note:** Recording NSDK depth with [useArdkDepthsIfPlatformUnavailable](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/use-ardk-depths-if-platform-unavailable/) can result in a lower recording FPS than the target framerate.

**Default:**`0` (defaults to 30 FPS)

</div>

</div>
