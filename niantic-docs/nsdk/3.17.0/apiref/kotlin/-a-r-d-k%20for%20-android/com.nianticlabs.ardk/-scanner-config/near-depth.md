---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/near-depth/
title: near-depth
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[ScannerConfig](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[nearDepth](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/near-depth/)

<div>

# nearDepth

</div>

\[androidJvm\]\
var [nearDepth](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/near-depth/): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a>

Near depth plane for scan depth range, in meters.

This parameter controls the closest distance at which depth data will be integrated. Objects closer than this distance will not be visible in visualization or reconstruction. This does not affect the range of the recorded depth frames. If set to `-1.0`, this is configured to 0.02 m in the default configuration. Must be greater than or equal to 0 and less than [farDepth](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/far-depth/), or set to `-1.0` to use the default range.

**Default:**`0.02f`

</div>

</div>
