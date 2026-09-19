---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers.com.nianticspatial.nsdk.helpers.createLiveDataSource/
title: createLiveDataSource
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.helpers](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers/ "com.nianticspatial.nsdk.helpers") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.helpers](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers/#property-com.nianticspatial.nsdk.helpers "com.nianticspatial.nsdk.helpers.com.nianticspatial.nsdk.helpers") 

</div>

<div class="api-title">

#  createLiveDataSource

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">createLiveDataSource</span><span class="ctoken punctuation">(</span><span class="ctoken plain"> </span><span class="ctoken plain">context</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">Context</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">frameProvider</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span><span class="ctoken plain"> </span><span class="ctoken plain">-\></span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://developers.google.com/ar/reference/java/com/google/ar/core/Frame" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Frame</a></span><span class="ctoken plain">?</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">orientationProvider</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span><span class="ctoken plain"> </span><span class="ctoken plain">-\></span><span class="ctoken plain"> </span><span class="ctoken class-name">[Orientation](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Orientation/ "Device orientation when capturing camera frames....")</span><span class="ctoken plain"> </span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[NsdkSessionDataSource](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkSessionDataSource/ "Provides synchronous, pull-based access to the latest available sensor data...")</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Creates a live ARCore data source that manages GPS and compass sensors internally.

\

The returned object implements `DefaultLifecycleObserver` — add it to your lifecycle\
to automatically start/stop sensor listeners.

</div>

------------------------------------------------------------------------

</div>

</div>
