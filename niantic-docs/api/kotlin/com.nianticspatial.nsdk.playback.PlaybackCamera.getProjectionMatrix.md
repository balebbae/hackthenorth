---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackCamera.getProjectionMatrix/
title: getProjectionMatrix
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.playback](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback/ "com.nianticspatial.nsdk.playback") <span class="api-breadcrumbs-nav">←</span>[PlaybackCamera](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackCamera/ "com.nianticspatial.nsdk.playback.PlaybackCamera") 

</div>

<div class="api-title">

#  getProjectionMatrix

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">getProjectionMatrix</span><span class="ctoken punctuation">(</span><span class="ctoken plain"> </span><span class="ctoken plain">zNear</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">zFar</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">viewportWidth</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">viewportHeight</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">deviceDisplayOrientation</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[Orientation](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Orientation/ "Device orientation when capturing camera frames....")</span><span class="ctoken plain">?</span><span class="ctoken plain"> </span><span class="ctoken plain">=</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">null</span><span class="ctoken plain"> </span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">FloatArray</a></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

OpenGL-style projection matrix (column-major) from intrinsics for the given viewport and near/far.\
Use with `getViewMatrix` to render 3D content aligned with the playback camera.

</div>

------------------------------------------------------------------------

</div>

</div>
