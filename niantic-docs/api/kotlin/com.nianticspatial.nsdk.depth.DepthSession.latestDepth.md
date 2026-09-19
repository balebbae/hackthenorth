---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.depth.DepthSession.latestDepth/
title: latestDepth
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.depth](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.depth/ "com.nianticspatial.nsdk.depth") <span class="api-breadcrumbs-nav">←</span>[DepthSession](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.depth.DepthSession/ "com.nianticspatial.nsdk.depth.DepthSession") 

</div>

<div class="api-title">

#  latestDepth

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">latestDepth</span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[NSDKResult](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKResult/ "ResultDeprecated wrapper for NSDK operations that can succeed or fail....")</span><span class="ctoken punctuation">\<</span><span class="ctoken class-name">[DepthBuffer](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.DepthBuffer/ "Depth result from ARDK's Depth System after computing disparity.")</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name">[AwarenessStatus](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessStatus/ "Browse to AwarenessStatus")</span><span class="ctoken punctuation">\></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Get the latest output from the depth feature

\

This retrieves the latest depth buffer represented as an image, along side other\
relevant information such as the camera pose, intrinsics, and min max disparity.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

Result containing depth buffer if successful, or error information

</div>

------------------------------------------------------------------------

</div>

</div>
