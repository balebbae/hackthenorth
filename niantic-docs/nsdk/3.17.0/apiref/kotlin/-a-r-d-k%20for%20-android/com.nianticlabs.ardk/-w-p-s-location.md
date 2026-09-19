---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-w-p-s-location/
title: index
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[WPSLocation](https://www.nianticspatial.com/docs/nsdk/3.17.0/)

<div>

# WPSLocation

</div>

\[androidJvm\]\
data class [WPSLocation](https://www.nianticspatial.com/docs/nsdk/3.17.0/)(val referenceLatitudeDegrees: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-double/index.html" target="_blank" rel="noopener noreferrer">Double</a>, val referenceLongitudeDegrees: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-double/index.html" target="_blank" rel="noopener noreferrer">Double</a>, val referenceAltitudeMetres: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-double/index.html" target="_blank" rel="noopener noreferrer">Double</a>, val trackingToRelativeEdn: Pose)

Contains world positioning data from the WPS (World Positioning System).

`WPSLocation` provides global positioning information that combines GPS/GNSS data with visual positioning for enhanced accuracy and reliability.

### Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

WPS location data includes:

- Reference GPS coordinates (latitude, longitude, altitude)
- Transformation matrix for coordinate conversions
- Status information about positioning quality

### Example<a href="#example" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
val result = wpsSession.getLatestLocation()
when (result) {
    is ARDKResult.Success -> {
        val location = result.value
        println("GPS Coordinates: ${location.referenceLatitudeDegrees}, ${location.referenceLongitudeDegrees}")
        println("Altitude: ${location.referenceAltitudeMetres} meters")

        // Use the transformation matrix for coordinate conversions
        val worldPosition = location.trackingToRelativeEdn
        placeARContent(worldPosition)
    }
    is ARDKResult.Error -> {
        println("WPS error: ${result.code}")
    }
}
```

</div>

</div>

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>WPSLocation</td>
<td>[androidJvm]<br />
constructor(referenceLatitudeDegrees: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-double/index.html" target="_blank" rel="noopener noreferrer">Double</a>, referenceLongitudeDegrees: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-double/index.html" target="_blank" rel="noopener noreferrer">Double</a>, referenceAltitudeMetres: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-double/index.html" target="_blank" rel="noopener noreferrer">Double</a>, trackingToRelativeEdn: Pose)</td>
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-w-p-s-location/reference-altitude-metres/">referenceAltitudeMetres</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-w-p-s-location/reference-altitude-metres/">referenceAltitudeMetres</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-double/index.html" target="_blank" rel="noopener noreferrer">Double</a><br />
Reference altitude in meters above sea level.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-w-p-s-location/reference-latitude-degrees/">referenceLatitudeDegrees</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-w-p-s-location/reference-latitude-degrees/">referenceLatitudeDegrees</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-double/index.html" target="_blank" rel="noopener noreferrer">Double</a><br />
Reference latitude in degrees (WGS84 coordinate system).</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-w-p-s-location/reference-longitude-degrees/">referenceLongitudeDegrees</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-w-p-s-location/reference-longitude-degrees/">referenceLongitudeDegrees</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-double/index.html" target="_blank" rel="noopener noreferrer">Double</a><br />
Reference longitude in degrees (WGS84 coordinate system).</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-w-p-s-location/tracking-to-relative-edn/">trackingToRelativeEdn</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-w-p-s-location/tracking-to-relative-edn/">trackingToRelativeEdn</a>: Pose<br />
Transformation matrix from tracking to relative coordinate system.</td>
</tr>
</tbody>
</table>

</div>

</div>
