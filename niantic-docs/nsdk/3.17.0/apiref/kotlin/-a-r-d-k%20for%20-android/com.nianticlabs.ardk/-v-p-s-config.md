---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/
title: index
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[VPSConfig](https://www.nianticspatial.com/docs/nsdk/3.17.0/)

<div>

# VPSConfig

</div>

class [VPSConfig](https://www.nianticspatial.com/docs/nsdk/3.17.0/)(var enableContinuousLocalization: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = false, val cloudInitialRequestsPerSecond: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a> = 1.0f, val cloudContinuousRequestsPerSecond: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a> = 0.2f, val enableTemporalFusion: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = false, val enableInterpolation: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = false, val jpegCompressionQuality: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a> = 50, val enableDeviceMapLocalization: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = false, val enableVPSDebugger: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = false, val enableGpsCorrectionForContinuousLocalization: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = true)

Configuration structure for the VPS session.

VPSConfig allows you to customize VPS behavior including localization frequency, quality settings, and advanced features like temporal fusion. Use this class to optimize VPS performance for your specific use case.

### Usage<a href="#usage" class="hash-link" aria-label="Direct link to Usage" title="Direct link to Usage">​</a>

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
val config = VPSConfig(
    enableContinuousLocalization = true,
    cloudInitialRequestsPerSecond = 2.0f,
    jpegCompressionQuality = 80
)
vpsSession.configure(config)
```

</div>

</div>

#### See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

|  |
|----|
| [VPSSession.configure](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.vps/-v-p-s-session/configure/) |

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>VPSConfig</td>
<td>[androidJvm]<br />
constructor(enableContinuousLocalization: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = false, cloudInitialRequestsPerSecond: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a> = 1.0f, cloudContinuousRequestsPerSecond: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a> = 0.2f, enableTemporalFusion: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = false, enableInterpolation: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = false, jpegCompressionQuality: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a> = 50, enableDeviceMapLocalization: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = false, enableVPSDebugger: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = false, enableGpsCorrectionForContinuousLocalization: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = true)</td>
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/cloud-continuous-requests-per-second/">cloudContinuousRequestsPerSecond</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/cloud-continuous-requests-per-second/">cloudContinuousRequestsPerSecond</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a> = 0.2f<br />
Defines the number of localization requests per second which are sent to the VPS server after the first successful localization. This is only used if continuous localization is enabled.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/cloud-initial-requests-per-second/">cloudInitialRequestsPerSecond</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/cloud-initial-requests-per-second/">cloudInitialRequestsPerSecond</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a> = 1.0f<br />
Defines the number of localization requests per second which are sent to the VPS server prior to the first successful localization.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/enable-continuous-localization/">enableContinuousLocalization</a></td>
<td>[androidJvm]<br />
var <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/enable-continuous-localization/">enableContinuousLocalization</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a><br />
Whether to enable continuous localization.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/enable-device-map-localization/">enableDeviceMapLocalization</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/enable-device-map-localization/">enableDeviceMapLocalization</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = false<br />
Enables localization against device-created maps.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/enable-gps-correction-for-continuous-localization/">enableGpsCorrectionForContinuousLocalization</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/enable-gps-correction-for-continuous-localization/">enableGpsCorrectionForContinuousLocalization</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = true<br />
Whether to enable GPS correction for continuous localization.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/enable-interpolation/">enableInterpolation</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/enable-interpolation/">enableInterpolation</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = false<br />
Whether to enable interpolation.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/enable-temporal-fusion/">enableTemporalFusion</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/enable-temporal-fusion/">enableTemporalFusion</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = false<br />
Whether to enable temporal fusion.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/enable-v-p-s-debugger/">enableVPSDebugger</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/enable-v-p-s-debugger/">enableVPSDebugger</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = false<br />
Enable VPS Debugger.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/jpeg-compression-quality/">jpegCompressionQuality</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-v-p-s-config/jpeg-compression-quality/">jpegCompressionQuality</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a> = 50<br />
Defines the quality of the JPEG compression used for the camera image sent to the VPS server as part of a localization request. Lower values will result in lower bandwidth usage.</td>
</tr>
</tbody>
</table>

</div>

</div>
