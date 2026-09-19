---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scan-save-error/-companion/from-state/
title: from-state
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[ScanSaveError](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scan-save-error/)/[Companion](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[fromState](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scan-save-error/-companion/from-state/)

<div>

# fromState

</div>

\[androidJvm\]\
fun [fromState](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scan-save-error/-companion/from-state/)(state: [ScanSaveState](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scan-save-state/)): [ScanSaveError](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scan-save-error/)

Converts a non-successful ScanSaveState into the corresponding ScanSaveError.

#### Return<a href="#return" class="hash-link" aria-label="Direct link to Return" title="Direct link to Return">​</a>

The mapped ScanSaveError. Returns UNKNOWN if the state is SAVED or unexpected.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|       |                       |
|-------|-----------------------|
| state | The state to convert. |

</div>

</div>
