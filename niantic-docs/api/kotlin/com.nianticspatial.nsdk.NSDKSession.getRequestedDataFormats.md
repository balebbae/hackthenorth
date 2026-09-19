---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKSession.getRequestedDataFormats/
title: getRequestedDataFormats
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk/ "com.nianticspatial.nsdk") <span class="api-breadcrumbs-nav">←</span>[NSDKSession](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKSession/ "com.nianticspatial.nsdk.NSDKSession") 

</div>

<div class="api-title">

#  getRequestedDataFormats

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">getRequestedDataFormats</span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Gets the data formats that NSDK requires for processing.

\

This function returns a bitmask indicating which types of input data\
(camera frames, depth, IMU, etc.) NSDK needs for optimal performance.\
Use this to configure your data capture pipeline accordingly.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

Bitmask of required data formats as defined in InputDataFlags

</div>

#### See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

- sendFrame
- create

------------------------------------------------------------------------

</div>

</div>
