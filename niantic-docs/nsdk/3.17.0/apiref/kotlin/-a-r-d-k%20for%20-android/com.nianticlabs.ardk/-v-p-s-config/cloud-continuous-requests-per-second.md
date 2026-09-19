---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/cloud-continuous-requests-per-second/
title: cloud-continuous-requests-per-second
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[VPSConfig](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[cloudContinuousRequestsPerSecond](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/cloud-continuous-requests-per-second/)

<div>

# cloudContinuousRequestsPerSecond

</div>

\[androidJvm\]\
val [cloudContinuousRequestsPerSecond](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/cloud-continuous-requests-per-second/): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a> = 0.2f

Defines the number of localization requests per second which are sent to the VPS server after the first successful localization. This is only used if continuous localization is enabled.

This is 0.2f in the default configuration (one request every 5 seconds).

**Default:**`0.2f`**Range:** 0.1f - 1.0f (recommended) **Requires:**[enableContinuousLocalization](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/enable-continuous-localization/) = true

</div>

</div>
