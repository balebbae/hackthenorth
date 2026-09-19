---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/far-depth/
title: far-depth
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[ScannerConfig](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[farDepth](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/far-depth/)

<div>

# farDepth

</div>

\[androidJvm\]\
var [farDepth](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/far-depth/): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a>

Far depth plane for scan depth range, in meters.

This parameter controls the farthest distance at which depth data will be integrated. Objects farther than this distance will not be visible in visualization or reconstruction. This does not affect the range of the recorded depth frames. If set to `0.0`, this is configured to 5.0 m in the default configuration. Values greater than 5.0 m are not recommended. Must be greater than [nearDepth](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/near-depth/), or set to `0` to use the default range.

**Default:**`0.0f` (defaults to 5.0 m)

</div>

</div>
