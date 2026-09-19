---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mapping/-mapping-storage-session/get-data/
title: get-data
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk.mapping](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mapping/)/[MappingStorageSession](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[getData](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mapping/-mapping-storage-session/get-data/)

<div>

# getData

</div>

\[androidJvm\]\
fun [getData](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mapping/-mapping-storage-session/get-data/)(): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-byte-array/index.html" target="_blank" rel="noopener noreferrer">ByteArray</a>?

Get the complete map data.

This function returns all the map data accumulated during the AR session, serialized as a DeviceMap protobuf. This data can be saved, shared, and/or used for localization.

#### Return<a href="#return" class="hash-link" aria-label="Direct link to Return" title="Direct link to Return">​</a>

The map data if successful, or `null` if no map data exists.

</div>

</div>
