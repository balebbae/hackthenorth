---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSceneSegmentationSession.method-start/
title: start
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

#  start

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">start</span><span class="ctoken plain">()</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Starts the Scene Segmentation system.\
After starting, Scene Segmentation will begin processing incoming frame data for semantic segmentation.\
The system must be configured before starting.

</div>

#### Example<a href="#example" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
sceneSegmentationSession.configure(with: config)
sceneSegmentationSession.start()
```

</div>

</div>

------------------------------------------------------------------------

</div>

</div>
