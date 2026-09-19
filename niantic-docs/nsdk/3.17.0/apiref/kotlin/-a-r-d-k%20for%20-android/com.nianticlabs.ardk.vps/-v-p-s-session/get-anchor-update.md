---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.vps/-v-p-s-session/get-anchor-update/
title: get-anchor-update
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk.vps](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.vps/)/[VPSSession](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[getAnchorUpdate](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.vps/-v-p-s-session/get-anchor-update/)

<div>

# getAnchorUpdate

</div>

\[androidJvm\]\
fun [getAnchorUpdate](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.vps/-v-p-s-session/get-anchor-update/)(uuid: [UUID](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-u-u-i-d/)): [AnchorUpdate](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-update/)

Gets the latest tracking update for a specified anchor.

Call this regularly to get updated anchor poses as the device moves and VPS refines the localization.

#### Return<a href="#return" class="hash-link" aria-label="Direct link to Return" title="Direct link to Return">​</a>

The anchor update

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|      |                                    |
|------|------------------------------------|
| uuid | The unique identifier of an anchor |

#### See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

|  |
|----|
| [VPSSession.trackAnchor](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.vps/-v-p-s-session/track-anchor/) |
| [AnchorUpdate](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-update/) |

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

|  |  |
|----|----|
|  | `ARDKStatusException` with code `ARDKStatus.invalidArgument` if no anchor with the id `uuid` has been created or added for tracking. Check ARDK's C logs for more information. |

</div>

</div>
