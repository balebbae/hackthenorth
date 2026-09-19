---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.class-SceneSegmentationResult/
title: SceneSegmentationResult
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") 

</div>

<div class="api-title">

#  SceneSegmentationResult

<div class="api-extends">

↳ inherits from [AwarenessImageResult](https://www.nianticspatial.com/docs/api/swift/NSDK.class-AwarenessImageResult/ "AwarenessImageResult") 

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">SceneSegmentationResult</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Contains semantic segmentation results from the NSDK scene segmentation processing system. `SceneSegmentationResult` provides semantic understanding of the environment by classifying pixels in camera images into different object categories (e.g., sky, ground, buildings, people, vehicles). This enables applications to understand the scene structure and make intelligent decisions based on environmental context.

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Semantic segmentation results include:

- **Confidence maps**: Per-pixel confidence scores for semantic classifications
- **Packed channels**: Multiple semantic categories encoded in a single image
- **Suppression masks**: Masks indicating areas to be ignored or suppressed
- **Metadata**: Frame information, timestamps, and error status

## Example Usage<a href="#example-usage" class="hash-link" aria-label="Direct link to Example Usage" title="Direct link to Example Usage">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
// Get confidence for a specific semantic channel
let (status, confidenceResult) = sceneSegmentationSession.getLatestConfidence(channelIndex: 0)
if status.isOk(), let result = confidenceResult {
    print("Confidence image size: \(result.image?.width ?? 0) x \(result.image?.height ?? 0)")
    print("Frame ID: \(result.frameId)")
    print("Timestamp: \(result.timestampMs)")
    // Process confidence data for semantic understanding
    processSemanticConfidence(result)
}
// Get packed semantic channels
let (status, packedResult) = sceneSegmentationSession.getLatestPackedChannels()
if status.isOk(), let result = packedResult {
    // Process packed semantic data
    processPackedSceneSegmentation(result)
}
```

</div>

</div>

------------------------------------------------------------------------

</div>

</div>
