---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/enable-interpolation/
title: enable-interpolation
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[VPSConfig](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[enableInterpolation](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/enable-interpolation/)

<div>

# enableInterpolation

</div>

\[androidJvm\]\
val [enableInterpolation](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/enable-interpolation/): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = false

Whether to enable interpolation.

This will interpolate the position of the anchor over time to provide a smoother result. Anchor updates will be surfaced as sequential smooth updates rather than a single update at the latest localization result.

**Attention:** This is disabled in the default configuration.

**Default:**`false`

</div>

</div>
