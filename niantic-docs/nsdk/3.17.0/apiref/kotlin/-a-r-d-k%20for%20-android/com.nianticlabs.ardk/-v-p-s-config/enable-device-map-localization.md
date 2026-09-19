---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/enable-device-map-localization/
title: enable-device-map-localization
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[VPSConfig](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[enableDeviceMapLocalization](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/enable-device-map-localization/)

<div>

# enableDeviceMapLocalization

</div>

\[androidJvm\]\
val [enableDeviceMapLocalization](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/enable-device-map-localization/): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = false

Enables localization against device-created maps.

When enabled, VPS will attempt to localize against maps created locally by the mapping feature in addition to Niantic's cloud maps. This enables localization in areas without cloud VPS coverage.

**Default:**`false`**Requires:** Mapping feature to have created a local map

#### See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

|                                    |
|------------------------------------|
| DeviceMappingSession.createMapping |

</div>

</div>
