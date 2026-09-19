---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mapping/-mapping-storage-session/merge-update/
title: merge-update
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk.mapping](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mapping/)/[MappingStorageSession](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[mergeUpdate](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mapping/-mapping-storage-session/merge-update/)

<div>

# mergeUpdate

</div>

\[androidJvm\]\
fun [mergeUpdate](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mapping/-mapping-storage-session/merge-update/)(existingMap: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-byte-array/index.html" target="_blank" rel="noopener noreferrer">ByteArray</a>, mapUpdate: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-byte-array/index.html" target="_blank" rel="noopener noreferrer">ByteArray</a>): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-byte-array/index.html" target="_blank" rel="noopener noreferrer">ByteArray</a>?

Merge a map update into an existing map.

Combines incremental map updates with existing map data to create an updated complete map dataset.

#### Return<a href="#return" class="hash-link" aria-label="Direct link to Return" title="Direct link to Return">​</a>

The merged map data if successful, or `null` if no merged map data exists.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|             |                                               |
|-------------|-----------------------------------------------|
| existingMap | The existing map to merge the update into     |
| mapUpdate   | The map update to merge into the existing map |

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

|  |  |
|----|----|
| ArdkNullArgumentStatusException | or ArdkInvalidArgumentStatusException indicating a problem with the map argument. Check ARDK's C logs for more information. |

</div>

</div>
