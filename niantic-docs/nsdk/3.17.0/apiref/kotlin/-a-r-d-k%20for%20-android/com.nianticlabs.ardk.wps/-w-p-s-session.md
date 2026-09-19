---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.wps/-w-p-s-session/
title: index
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk.wps](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.wps/)/[WPSSession](https://www.nianticspatial.com/docs/nsdk/3.17.0/)

<div>

# WPSSession

</div>

class [WPSSession](https://www.nianticspatial.com/docs/nsdk/3.17.0/) : [SessionBase](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-session-base/)\<[WPSSession](https://www.nianticspatial.com/docs/nsdk/3.17.0/)\>

A session for World Positioning System (WPS) functionality.

WPS provides the 3D position and orientation of the device in geographic coordinates as an alternative to using device GPS and compass heading data. WPS provides greater accuracy and frame-to-frame stability than standard GPS positioning, making it more suitable for AR applications. As the user moves around, WPS maintains the device's position, making it suitable for continuous use over long periods of time and long distances. WPS will work in any location where the phone has a GPS signal, but the accuracy will vary depending on GPS accuracy.

### Usage<a href="#usage" class="hash-link" aria-label="Direct link to Usage" title="Direct link to Usage">​</a>

**1. Acquire the WPS session:**

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
val wpsSession = ardkSession.wps.acquire()
```

</div>

</div>

**2. Configure the session (optional - defaults are usually sufficient):**

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
val config = WPSConfig(
    enableSmoothing = true,
    framerate = 120
)
wpsSession.configure(config)
```

</div>

</div>

**3. Start the session:**

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
wpsSession.start()
```

</div>

</div>

**4. Poll for location updates regularly:**

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
coroutineScope.launch {
    while (trackingStarted) {
        delay(1000) // Update every second

        // Check feature status
        val featureStatus = wpsSession.featureStatus()
        if (!featureStatus.isOk()) {
            println("WPS has encountered an error")
        }

        // Get the latest location estimate
        when (val result = wpsSession.getLatestLocation()) {
            is ARDKResult.Success -> {
                val location = result.value
                println("GPS: ${location.referenceLatitudeDegrees}, ${location.referenceLongitudeDegrees}")
                println("Altitude: ${location.referenceAltitudeMetres} meters")

                // Use the transformation matrix for coordinate conversions
                val worldPosition = location.trackingToRelativeEdn
                // Place AR content using world position
            }
            is ARDKResult.Error -> {
                when (result.code) {
                    WPSError.NOT_INITIALIZED -> println("WPS still initializing...")
                    WPSError.NO_GNSS -> println("No GPS signal available")
                    WPSError.NO_HEADING -> println("No compass data available")
                    WPSError.TRACKING_FAILED -> println("WPS tracking failed")
                    else -> println("WPS error: ${result.code}")
                }
            }
        }
    }
}
```

</div>

</div>

**5. Clean up when done:**

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
wpsSession.stop()
wpsSession.close()
```

</div>

</div>

### Advanced Features<a href="#advanced-features" class="hash-link" aria-label="Direct link to Advanced Features" title="Direct link to Advanced Features">​</a>

**Converting specific poses to geolocations:**

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
val cameraPose = frame.camera.pose
when (val result = wpsSession.getDevicePoseAsGeolocation(cameraPose)) {
    is ARDKResult.Success -> {
        val geolocation = result.value
        println("Pose location: ${geolocation.latitude}, ${geolocation.longitude}")
    }
    is ARDKResult.Error -> {
        println("Could not get geolocation for pose: ${result.code}")
    }
}
```

</div>

</div>

#### See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

|  |
|----|
| [WPSSession.start](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.wps/-w-p-s-session/start/) |
| [WPSSession.stop](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.wps/-w-p-s-session/stop/) |
| [WPSSession.configure](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.wps/-w-p-s-session/configure/) |
| [WPSSession.getLatestLocation](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.wps/-w-p-s-session/get-latest-location/) |
| [WPSSession.getDevicePoseAsGeolocation](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.wps/-w-p-s-session/get-device-pose-as-geolocation/) |

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
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-session-base/acquire/">acquire</a>(): <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/">WPSSession</a></td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-session-base/close/">close</a></td>
<td>[androidJvm]<br />
@<a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.jvm/-synchronized/index.html" target="_blank" rel="noopener noreferrer">Synchronized</a><br />
open override fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-session-base/close/">close</a>()</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.wps/-w-p-s-session/configure/">configure</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.wps/-w-p-s-session/configure/">configure</a>(config: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-w-p-s-config/">WPSConfig</a>)<br />
Configures the session with the specified settings.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.wps/-w-p-s-session/feature-status/">featureStatus</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.wps/-w-p-s-session/feature-status/">featureStatus</a>(): <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-feature-status/">FeatureStatus</a><br />
Reports errors that have occurred within processes running inside this feature.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.wps/-w-p-s-session/get-device-pose-as-geolocation/">getDevicePoseAsGeolocation</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.wps/-w-p-s-session/get-device-pose-as-geolocation/">getDevicePoseAsGeolocation</a>(pose: Pose): <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-result/">ARDKResult</a>&lt;<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-geolocation-data/">GeolocationData</a>, <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-w-p-s-error/">WPSError</a>&gt;<br />
Use WPS to get an estimated geolocation for a pose in AR space.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.wps/-w-p-s-session/get-latest-location/">getLatestLocation</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.wps/-w-p-s-session/get-latest-location/">getLatestLocation</a>(): <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-result/">ARDKResult</a>&lt;<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-w-p-s-location/">WPSLocation</a>, <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-w-p-s-error/">WPSError</a>&gt;<br />
Gets the transform of the latest geolocation estimate.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.wps/-w-p-s-session/start/">start</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.wps/-w-p-s-session/start/">start</a>()<br />
Starts the WPS system.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.wps/-w-p-s-session/stop/">stop</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.wps/-w-p-s-session/stop/">stop</a>()<br />
Stops the WPS system.</td>
</tr>
</tbody>
</table>

</div>

</div>
