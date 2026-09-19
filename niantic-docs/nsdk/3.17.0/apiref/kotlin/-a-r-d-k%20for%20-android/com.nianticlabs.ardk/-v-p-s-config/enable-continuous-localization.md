---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/enable-continuous-localization/
title: enable-continuous-localization
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[VPSConfig](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[enableContinuousLocalization](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/enable-continuous-localization/)

<div>

# enableContinuousLocalization

</div>

\[androidJvm\]\
var [enableContinuousLocalization](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/enable-continuous-localization/): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a>

Whether to enable continuous localization.

This will continuously send localization requests to the VPS server even after the first successful localization response has been received. These results will help refine the position of the anchor over time. This will also help mitigate AR tracking drift.

**Attention:** This will increase the bandwidth used by the VPS feature.

**Attention:** This will also cause anchored objects to move in the scene as their positions are refined.

**Attention:** This is disabled in the default configuration.

See `cloudContinuousRequestsPerSecond` to define the frequency of the requests.

**Default:**`false`

</div>

</div>
