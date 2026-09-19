---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/-configuration/
title: index
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[ArdkConfiguration](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/)/[Configuration](https://www.nianticspatial.com/docs/nsdk/3.17.0/)

<div>

# Configuration

</div>

\[androidJvm\]\
data class [Configuration](https://www.nianticspatial.com/docs/nsdk/3.17.0/)(val forceDisableCTrace: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = false, val deviceInfo: [ArdkConfiguration.DeviceInfo](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/-device-info/) = DeviceInfo(), val envConfig: [ArdkConfiguration.CloudEnvConfig](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/-cloud-env-config/) = CloudEnvConfig(), val userConfig: [ArdkConfiguration.UserConfig](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/-user-config/) = UserConfig(), val useLidar: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = false, val logCallback: [ArdkLogCallback](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-log-callback/)? = null)

Top-level ARDK configuration container.

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>Configuration</td>
<td>[androidJvm]<br />
constructor(forceDisableCTrace: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = false, deviceInfo: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/-device-info/">ArdkConfiguration.DeviceInfo</a> = DeviceInfo(), envConfig: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/-cloud-env-config/">ArdkConfiguration.CloudEnvConfig</a> = CloudEnvConfig(), userConfig: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/-user-config/">ArdkConfiguration.UserConfig</a> = UserConfig(), useLidar: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = false, logCallback: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-log-callback/">ArdkLogCallback</a>? = null)</td>
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/-configuration/device-info/">deviceInfo</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/-configuration/device-info/">deviceInfo</a>: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/-device-info/">ArdkConfiguration.DeviceInfo</a></td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/-configuration/env-config/">envConfig</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/-configuration/env-config/">envConfig</a>: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/-cloud-env-config/">ArdkConfiguration.CloudEnvConfig</a></td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/-configuration/force-disable-c-trace/">forceDisableCTrace</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/-configuration/force-disable-c-trace/">forceDisableCTrace</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = false</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/-configuration/log-callback/">logCallback</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/-configuration/log-callback/">logCallback</a>: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-log-callback/">ArdkLogCallback</a>? = null</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/-configuration/use-lidar/">useLidar</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/-configuration/use-lidar/">useLidar</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = false</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/-configuration/user-config/">userConfig</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/-configuration/user-config/">userConfig</a>: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-configuration/-user-config/">ArdkConfiguration.UserConfig</a></td>
</tr>
</tbody>
</table>

</div>

</div>
