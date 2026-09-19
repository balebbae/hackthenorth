---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSceneSegmentationSession.method-featureStatus/
title: featureStatus
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKSceneSegmentationSession](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKSceneSegmentationSession/ "NSDKSceneSegmentationSession") 

</div>

<div class="api-title">

#  featureStatus

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">featureStatus</span><span class="ctoken plain">() -\> </span><span class="ctoken class-name">[NSDKFeatureStatus](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKFeatureStatus/ "Status flags for NSDK features indicating their current operational state....")</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Gets the current status of the Scene Segmentation feature.\
This method reports any errors or warnings that have occurred within the scene segmentation system.\
Check this periodically to monitor the health of semantic processing operations.\
Once an error is flagged, it will remain flagged until the problematic process runs again\
and completes successfully.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

Feature status flags indicating current state and any issues

</div>

#### Example<a href="#example" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
let status = sceneSegmentationSession.featureStatus()
if status.contains(.failed) {
    print("Scene Segmentation has encountered an error")
}
```

</div>

</div>

------------------------------------------------------------------------

</div>

</div>
