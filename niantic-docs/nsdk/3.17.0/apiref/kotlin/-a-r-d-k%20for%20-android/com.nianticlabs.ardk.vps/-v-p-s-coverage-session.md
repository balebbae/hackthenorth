---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.vps/-v-p-s-coverage-session/
title: index
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk.vps](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.vps/)/[VPSCoverageSession](https://www.nianticspatial.com/docs/nsdk/3.17.0/)

<div>

# VPSCoverageSession

</div>

\[androidJvm\]\
class [VPSCoverageSession](https://www.nianticspatial.com/docs/nsdk/3.17.0/) : [SessionBase](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-session-base/)\<[VPSCoverageSession](https://www.nianticspatial.com/docs/nsdk/3.17.0/)\>

Creates a VPS Coverage instance for querying coverage information.

VPS Coverage allows you to query which areas have VPS mapping coverage, helping you determine where VPS localization will be available.

## Types<a href="#types" class="hash-link" aria-label="Direct link to Types" title="Direct link to Types">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Name</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.vps/-v-p-s-coverage-session/-companion/">Companion</a></td>
<td>[androidJvm]<br />
object <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.vps/-v-p-s-coverage-session/-companion/">Companion</a></td>
</tr>
</tbody>
</table>

## Functions<a href="#functions" class="hash-link" aria-label="Direct link to Functions" title="Direct link to Functions">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Name</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-session-base/acquire/">acquire</a></td>
<td>[androidJvm]<br />
@<a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.jvm/-synchronized/index.html" target="_blank" rel="noopener noreferrer">Synchronized</a><br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-session-base/acquire/">acquire</a>(): <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/">VPSCoverageSession</a></td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-session-base/close/">close</a></td>
<td>[androidJvm]<br />
@<a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.jvm/-synchronized/index.html" target="_blank" rel="noopener noreferrer">Synchronized</a><br />
open override fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-session-base/close/">close</a>()</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.vps/-v-p-s-coverage-session/get-area-targets/">getAreaTargets</a></td>
<td>[androidJvm]<br />
suspend fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.vps/-v-p-s-coverage-session/get-area-targets/">getAreaTargets</a>(latLng: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-lat-lng/">LatLng</a>, radius: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a>, timeoutMillis: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-long/index.html" target="_blank" rel="noopener noreferrer">Long</a> = TIMEOUT_MS): <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-async-result/">AsyncResult</a>&lt;<a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-array/index.html" target="_blank" rel="noopener noreferrer">Array</a>&lt;<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-area-target/">AreaTarget</a>&gt;, <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-coverage-error/">VpsCoverageError</a>&gt;<br />
Asynchronously retrieves area targets within a specified radius of a geographic location.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.vps/-v-p-s-coverage-session/get-hint-image/">getHintImage</a></td>
<td>[androidJvm]<br />
suspend fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.vps/-v-p-s-coverage-session/get-hint-image/">getHintImage</a>(hintUrl: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>, timeoutMillis: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-long/index.html" target="_blank" rel="noopener noreferrer">Long</a> = TIMEOUT_MS): <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-async-result/">AsyncResult</a>&lt;<a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-byte-array/index.html" target="_blank" rel="noopener noreferrer">ByteArray</a>, <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-coverage-error/">VpsCoverageError</a>&gt;<br />
Asynchronously downloads a hint image from a given URL.</td>
</tr>
</tbody>
</table>

</div>

</div>
