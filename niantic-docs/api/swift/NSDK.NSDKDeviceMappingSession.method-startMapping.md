---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKDeviceMappingSession.method-startMapping/
title: startMapping
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKDeviceMappingSession](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKDeviceMappingSession/ "NSDKDeviceMappingSession") 

</div>

<div class="api-title">

#  startMapping

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">startMapping</span><span class="ctoken plain">()</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Begin a mapping sequence.\
This begins building an on-device map that can be used for VPS. Map data is accumulated\
in the session's `NSDKMapStorage` while mapping is running. Subscribe to `$latestMapUpdate`\
to retrieve incremental map updates reactively, or call `NSDKMapStorage.mapData()`\
after mapping completes to get the full map.\
- Attention: This method must be called after `start()` and before `stop()`.

</div>

------------------------------------------------------------------------

</div>

</div>
