---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKMapStorage.method-createRootAnchor/
title: createRootAnchor
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKMapStorage](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKMapStorage/ "NSDKMapStorage") 

</div>

<div class="api-title">

#  createRootAnchor

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">createRootAnchor</span><span class="ctoken plain">() -\> </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Creates an anchor on the existing map located at the origin of the current AR session, if possible.\
The root anchor represents the origin point of the map coordinate system and can be\
used with VPS for localization.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The payload of the root anchor, encoded as a base64 string if available, `nil` if otherwise.

</div>

------------------------------------------------------------------------

</div>

</div>
