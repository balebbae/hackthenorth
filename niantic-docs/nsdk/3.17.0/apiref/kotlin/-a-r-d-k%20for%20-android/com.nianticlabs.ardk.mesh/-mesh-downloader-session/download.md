---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mesh/-mesh-downloader-session/download/
title: download
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk.mesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mesh/)/[MeshDownloaderSession](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[download](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mesh/-mesh-downloader-session/download/)

<div>

# download

</div>

\[androidJvm\]\
suspend fun [download](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mesh/-mesh-downloader-session/download/)(payload: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>, getTexture: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a>, maxDownloadSizeKb: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a>? = null, timeoutMillis: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-long/index.html" target="_blank" rel="noopener noreferrer">Long</a> = TIMEOUT_MS): [AsyncResult](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-async-result/)\<<a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-array/index.html" target="_blank" rel="noopener noreferrer">Array</a>\<[MeshDownloaderData](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-mesh-downloader-data/)\>, [MeshDownloaderError](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-mesh-downloader-error/)\>

Asynchronously downloads a mesh for a given location payload.

This function suspends execution until the download operation is complete, has failed, or has timed out.

#### Return<a href="#return" class="hash-link" aria-label="Direct link to Return" title="Direct link to Return">​</a>

An [AsyncResult](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-async-result/) which will be either [AsyncResult.Success](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-async-result/-success/) containing the mesh data, [AsyncResult.Error](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-async-result/-error/) detailing the failure reason, or [AsyncResult.Timeout](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-async-result/-timeout/) indicating a timeout in the download process.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|  |  |
|----|----|
| payload | The VPS anchor payload string for the desired location. |
| getTexture | If true, the response will include the mesh textures. If false, image data and UVs will be empty, and a color field will be added to each vertex in the mesh. |
| maxDownloadSizeKb | (Optional) Sets a maximum size for the meshes to be downloaded, in kilobytes. Meshes above this size will not be downloaded. The default value, `null`, does not set a size limit. |
| timeoutMillis | The maximum time in milliseconds to wait for the download to complete. |

</div>

</div>
