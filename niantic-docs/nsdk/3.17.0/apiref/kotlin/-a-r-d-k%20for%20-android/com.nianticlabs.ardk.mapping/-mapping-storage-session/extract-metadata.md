---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mapping/-mapping-storage-session/extract-metadata/
title: extract-metadata
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk.mapping](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mapping/)/[MappingStorageSession](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[extractMetadata](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mapping/-mapping-storage-session/extract-metadata/)

<div>

# extractMetadata

</div>

\[androidJvm\]\
fun [extractMetadata](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mapping/-mapping-storage-session/extract-metadata/)(anchorPayload: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>, map: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-byte-array/index.html" target="_blank" rel="noopener noreferrer">ByteArray</a>): [MapMetadata](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-map-metadata/)?

Extract the metadata from a map relative to a specified anchor.

Render the feature points in the metadata relative to the specified anchor to visualize the map. This is only possible when the anchor is linked directly to the map's node(s), or if the anchor's nodes are reachable to the map's nodes from the currently active transform graph.

#### Return<a href="#return" class="hash-link" aria-label="Direct link to Return" title="Direct link to Return">​</a>

The extracted metadata if successful, or `null` if no metadata exists.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|  |  |
|----|----|
| anchorPayload | The base64-encoded payload of the anchor that the returned points will be relative to. |
| map | The map buffer to extract metadata from. It should be encoded as a DeviceMap protobuf. |

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

|  |  |
|----|----|
| ArdkNullArgumentStatusException | or ArdkInvalidArgumentStatusException indicating a problem with the either argument. Check ARDK's C logs for more information. |

</div>

</div>
