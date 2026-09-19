---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/
title: index
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[ARDKSession](https://www.nianticspatial.com/docs/nsdk/3.17.0/)

<div>

# ARDKSession

</div>

class [ARDKSession](https://www.nianticspatial.com/docs/nsdk/3.17.0/) : <a href="https://developer.android.com/reference/kotlin/java/io/Closeable.html" target="_blank" rel="noopener noreferrer">Closeable</a>

Creates a new ARDK instance with the provided API key.

This is the primary entry point for initializing ARDK functionality. You must call this before using any other ARDK features.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|  |  |
|----|----|
| apiKey | Your Niantic API key for authentication. Get this from the Niantic developer portal. |

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

|  |  |
|----|----|
| <a href="https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html" target="_blank" rel="noopener noreferrer">IllegalStateException</a> | if native libraries failed to load |

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>ARDKSession</td>
<td>[androidJvm]<br />
constructor(apiKey: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>, useLidar: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = true, pathConfig: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-path-config/">PathConfig</a>? = null, logCallback: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-log-callback/">ArdkLogCallback</a>? = null)constructor(accessToken: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>, refreshToken: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>, useLidar: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = true, pathConfig: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-path-config/">PathConfig</a>? = null, logCallback: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-log-callback/">ArdkLogCallback</a>? = null)<br />
Convenience constructor to initialize ARDK with auth tokens instead of an API key. Tokens will be forwarded to native for validation and persistence.<br />
constructor(configFilePath: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>, logCallback: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-log-callback/">ArdkLogCallback</a>? = null)<br />
Creates a new ARDK instance from a JSON configuration file. Throws IllegalStateException if initialization fails.<br />
constructor(config: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/-configuration/">ArdkConfiguration.Configuration</a>, pathConfig: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-path-config/">PathConfig</a>? = null)<br />
Creates a new ARDK instance from a programmatic configuration object. Throws IllegalStateException if initialization fails.</td>
</tr>
</tbody>
</table>

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/depth-session/">depthSession</a></td>
<td>[androidJvm]<br />
lateinit var <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/depth-session/">depthSession</a>: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.depth/-depth-session/">DepthSession</a></td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/mapping/">mapping</a></td>
<td>[androidJvm]<br />
lateinit var <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/mapping/">mapping</a>: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mapping/-device-mapping-session/">DeviceMappingSession</a></td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/map-store/">mapStore</a></td>
<td>[androidJvm]<br />
lateinit var <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/map-store/">mapStore</a>: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mapping/-mapping-storage-session/">MappingStorageSession</a></td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/mesh-download/">meshDownload</a></td>
<td>[androidJvm]<br />
lateinit var <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/mesh-download/">meshDownload</a>: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mesh/-mesh-downloader-session/">MeshDownloaderSession</a></td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/meshing-session/">meshingSession</a></td>
<td>[androidJvm]<br />
lateinit var <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/meshing-session/">meshingSession</a>: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mesh/-meshing-session/">MeshingSession</a></td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/object-detection/">objectDetection</a></td>
<td>[androidJvm]<br />
lateinit var <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/object-detection/">objectDetection</a>: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-object-detection-session/">ObjectDetectionSession</a></td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/recording-exporter/">recordingExporter</a></td>
<td>[androidJvm]<br />
lateinit var <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/recording-exporter/">recordingExporter</a>: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.recording/-recording-exporter/">RecordingExporter</a></td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/scanning/">scanning</a></td>
<td>[androidJvm]<br />
lateinit var <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/scanning/">scanning</a>: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.scanning/-scanning-session/">ScanningSession</a></td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/semantics/">semantics</a></td>
<td>[androidJvm]<br />
lateinit var <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/semantics/">semantics</a>: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.awareness.semantics/-semantics-session/">SemanticsSession</a></td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/vps/">vps</a></td>
<td>[androidJvm]<br />
lateinit var <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/vps/">vps</a>: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.vps/-v-p-s-session/">VPSSession</a></td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/vps-coverage/">vpsCoverage</a></td>
<td>[androidJvm]<br />
lateinit var <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/vps-coverage/">vpsCoverage</a>: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.vps/-v-p-s-coverage-session/">VPSCoverageSession</a></td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/wps/">wps</a></td>
<td>[androidJvm]<br />
lateinit var <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/wps/">wps</a>: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.wps/-w-p-s-session/">WPSSession</a></td>
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/close/">close</a></td>
<td>[androidJvm]<br />
open override fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/close/">close</a>()<br />
Destroys an ARDK instance and any remaining opened feature sessions and frees associated resources.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/get-requested-data-formats/">getRequestedDataFormats</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/get-requested-data-formats/">getRequestedDataFormats</a>(): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a><br />
Gets the data formats that ARDK requires for processing.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/get-version/">getVersion</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/get-version/">getVersion</a>(): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a><br />
Returns the ARDK version string from the native library.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/send-frame/">sendFrame</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/send-frame/">sendFrame</a>(frameData: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-frame-data/">FrameData</a>)</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/set-access-token/">setAccessToken</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/set-access-token/">setAccessToken</a>(token: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>)<br />
Set the access token at runtime. Invalid/empty tokens are ignored by native.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/set-refresh-token/">setRefreshToken</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-session/set-refresh-token/">setRefreshToken</a>(token: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>)<br />
Set the refresh token at runtime. Invalid/empty tokens are ignored by native.</td>
</tr>
</tbody>
</table>

</div>

</div>
