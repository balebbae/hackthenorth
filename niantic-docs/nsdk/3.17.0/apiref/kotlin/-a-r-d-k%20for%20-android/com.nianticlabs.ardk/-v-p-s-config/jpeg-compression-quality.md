---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/jpeg-compression-quality/
title: jpeg-compression-quality
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[VPSConfig](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[jpegCompressionQuality](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/jpeg-compression-quality/)

<div>

# jpegCompressionQuality

</div>

\[androidJvm\]\
val [jpegCompressionQuality](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/jpeg-compression-quality/): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a> = 50

Defines the quality of the JPEG compression used for the camera image sent to the VPS server as part of a localization request. Lower values will result in lower bandwidth usage.

We have benchmarked that 50-90 quality for jpeg compression does not significantly impact the accuracy of the localization results.

This is 70 in the default configuration.

**Default:**`70`**Range:** 1 (lowest quality) - 100 (highest quality) **Recommended:** 50-90 for good balance of quality and bandwidth

</div>

</div>
