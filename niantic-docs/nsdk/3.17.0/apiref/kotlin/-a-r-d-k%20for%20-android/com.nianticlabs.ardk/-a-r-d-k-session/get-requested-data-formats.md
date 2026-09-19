---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/get-requested-data-formats/
title: get-requested-data-formats
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[ARDKSession](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[getRequestedDataFormats](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/get-requested-data-formats/)

<div>

# getRequestedDataFormats

</div>

\[androidJvm\]\
fun [getRequestedDataFormats](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/get-requested-data-formats/)(): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a>

Gets the data formats that ARDK requires for processing.

This function returns a bitmask indicating which types of input data (camera frames, depth, IMU, etc.) ARDK needs for optimal performance. Use this to configure your data capture pipeline accordingly.

#### Return<a href="#return" class="hash-link" aria-label="Direct link to Return" title="Direct link to Return">​</a>

Bitmask of required data formats as defined in InputDataFlags

#### See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

|  |
|----|
| [ARDKSession.sendFrame](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/send-frame/) |
| create |

</div>

</div>
