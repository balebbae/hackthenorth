---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mapping/-mapping-storage-session/create-root-anchor/
title: create-root-anchor
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk.mapping](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mapping/)/[MappingStorageSession](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[createRootAnchor](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mapping/-mapping-storage-session/create-root-anchor/)

<div>

# createRootAnchor

</div>

\[androidJvm\]\
fun [createRootAnchor](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mapping/-mapping-storage-session/create-root-anchor/)(): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>?

Creates an anchor on the existing map located at the origin of the current AR session, if possible.

The root anchor represents the origin point of the map coordinate system and can be used with VPS for localization.

#### Return<a href="#return" class="hash-link" aria-label="Direct link to Return" title="Direct link to Return">​</a>

The base64-encoded anchor payload if successful, or `null` if no anchor payload exists.

</div>

</div>
