---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-lat-lng/
title: index
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[LatLng](https://www.nianticspatial.com/docs/nsdk/3.17.0/)

<div>

# LatLng

</div>

data class [LatLng](https://www.nianticspatial.com/docs/nsdk/3.17.0/)(val lat: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-double/index.html" target="_blank" rel="noopener noreferrer">Double</a>, val lng: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-double/index.html" target="_blank" rel="noopener noreferrer">Double</a>)

Geographic coordinates representing latitude and longitude.

LatLng is used throughout ARDK for specifying geographic locations, particularly for VPS coverage queries and area-based operations.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|     |                                                |
|-----|------------------------------------------------|
| lat | Latitude in decimal degrees (-90.0 to 90.0)    |
| lng | Longitude in decimal degrees (-180.0 to 180.0) |

#### See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

|                                       |
|---------------------------------------|
| VPSCoverageSession.requestAreas       |
| VPSCoverageSession.requestAreaTargets |

#### Samples<a href="#samples" class="hash-link" aria-label="Direct link to Samples" title="Direct link to Samples">​</a>

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>LatLng</td>
<td>[androidJvm]<br />
constructor(lat: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a>, lng: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a>)<br />
Creates LatLng from float coordinates.<br />
constructor(lat: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-double/index.html" target="_blank" rel="noopener noreferrer">Double</a>, lng: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-double/index.html" target="_blank" rel="noopener noreferrer">Double</a>)</td>
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-lat-lng/lat/">lat</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-lat-lng/lat/">lat</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-double/index.html" target="_blank" rel="noopener noreferrer">Double</a></td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-lat-lng/lng/">lng</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-lat-lng/lng/">lng</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-double/index.html" target="_blank" rel="noopener noreferrer">Double</a></td>
</tr>
</tbody>
</table>

</div>

</div>
