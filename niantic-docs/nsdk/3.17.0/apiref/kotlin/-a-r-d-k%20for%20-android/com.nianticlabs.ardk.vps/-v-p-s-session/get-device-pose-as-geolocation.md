---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.vps/-v-p-s-session/get-device-pose-as-geolocation/
title: get-device-pose-as-geolocation
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk.vps](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.vps/)/[VPSSession](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[getDevicePoseAsGeolocation](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.vps/-v-p-s-session/get-device-pose-as-geolocation/)

<div>

# getDevicePoseAsGeolocation

</div>

\[androidJvm\]\
fun [getDevicePoseAsGeolocation](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.vps/-v-p-s-session/get-device-pose-as-geolocation/)(pose: Pose): [ARDKResult](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-result/)\<[GeolocationData](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-geolocation-data/), [VpsGraphOperationError](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/)\>

Use VPS to get an estimated geolocation for a pose in AR space.

Requires that the session was configured with `enableGpsCorrectionForContinuousLocalization` enabled and the user be currently localized.

**Note:** Test (private) scans currently don't have GPS data so they cannot be used with this functionality.

#### Return<a href="#return" class="hash-link" aria-label="Direct link to Return" title="Direct link to Return">​</a>

The estimated geolocation, if available, or an error code otherwise.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|      |                                  |
|------|----------------------------------|
| pose | A pose in the device's AR space. |

#### See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

|  |
|----|
| [VPSSession.configure](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.vps/-v-p-s-session/configure/) |

</div>

</div>
