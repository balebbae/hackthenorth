---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.CameraIntrinsics.getFocalLength/
title: getFocalLength
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk/ "com.nianticspatial.nsdk") <span class="api-breadcrumbs-nav">←</span>[CameraIntrinsics](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.CameraIntrinsics/ "com.nianticspatial.nsdk.CameraIntrinsics") 

</div>

<div class="api-title">

#  getFocalLength

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">open</span><span class="ctoken plain"> </span><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">getFocalLength</span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">FloatArray</a></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Returns the camera's focal length in pixels.

\

The focal length is conventionally represented in pixels. For a detailed explanation, please\
see\
<a href="https://ksimek.github.io/2013/08/13/intrinsic" target="_blank" rel="noopener noreferrer">Disecting the Camera Matrix, Part 3: The Intrinsic Matrix</a>.\
Pixels-to-meters conversion can use `SENSOR_INFO_PHYSICAL_SIZE` and\
`SENSOR_INFO_PIXEL_ARRAY_SIZE` in the Android Characteristics API.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

a `float[2]` containing the focal length. The order of values is {fx, fy}.

</div>

------------------------------------------------------------------------

## Overload<a href="#overload" class="hash-link" aria-label="Direct link to Overload" title="Direct link to Overload">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">open</span><span class="ctoken plain"> </span><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">getFocalLength</span><span class="ctoken punctuation">(</span><span class="ctoken plain">focalLength</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">FloatArray</a></span><span class="ctoken plain">?</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">offset</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary-1" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Returns the camera's focal length in pixels.

\

The focal length is conventionally represented in pixels. For a detailed explanation, please\
see\
<a href="https://ksimek.github.io/2013/08/13/intrinsic" target="_blank" rel="noopener noreferrer">Disecting the Camera Matrix, Part 3: The Intrinsic Matrix</a>.\
Pixels-to-meters conversion can use `SENSOR_INFO_PHYSICAL_SIZE` and\
`SENSOR_INFO_PIXEL_ARRAY_SIZE` in the Android Characteristics API.

</div>

------------------------------------------------------------------------

</div>

</div>
