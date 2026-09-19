---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-depth-config/
title: index
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[DepthConfig](https://www.nianticspatial.com/docs/nsdk/3.17.0/)

<div>

# DepthConfig

</div>

class [DepthConfig](https://www.nianticspatial.com/docs/nsdk/3.17.0/)(var framerate: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a> = 0, var featureMode: [AwarenessFeatureMode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-awareness-feature-mode/) = AwarenessFeatureMode.UNSPECIFIED)

Configuration parameters for ARDK's Depth System.

## Basic Usage<a href="#basic-usage" class="hash-link" aria-label="Direct link to Basic Usage" title="Direct link to Basic Usage">​</a>

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
val config = DepthConfig(
    framerate = 120
    featureMode = AwarenessFeatureMode.SMOOTH,
)
ARDK.ConfigureDepth(handle, config)
```

</div>

</div>

#### See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

|                     |
|---------------------|
| ARDK.ConfigureDepth |
| ARDK.CreateDepth    |

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>DepthConfig</td>
<td>[androidJvm]<br />
constructor(framerate: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a> = 0, featureMode: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-awareness-feature-mode/">AwarenessFeatureMode</a> = AwarenessFeatureMode.UNSPECIFIED)</td>
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-depth-config/feature-mode/">featureMode</a></td>
<td>[androidJvm]<br />
var <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-depth-config/feature-mode/">featureMode</a>: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-awareness-feature-mode/">AwarenessFeatureMode</a><br />
Specify mode to internally select model for depth estimation. Each model selects a model that has different performance and quality characteristics.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-depth-config/framerate/">framerate</a></td>
<td>[androidJvm]<br />
var <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-depth-config/framerate/">framerate</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a><br />
Framerate which the Depth system takes in input. Depth is an expensive system so keeping framerate lower is recommended,</td>
</tr>
</tbody>
</table>

</div>

</div>
