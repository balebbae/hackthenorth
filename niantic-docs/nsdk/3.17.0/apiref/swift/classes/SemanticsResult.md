---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/SemanticsResult/
title: SemanticsResult
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `SemanticsResult`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public class SemanticsResult: AwarenessImageResult
```

</div>

</div>

Contains semantic segmentation results from the ARDK semantics processing system.

`SemanticsResult` provides semantic understanding of the environment by classifying pixels in camera images into different object categories (e.g., sky, ground, buildings, people, vehicles). This enables applications to understand the scene structure and make intelligent decisions based on environmental context.

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
let (status, confidenceResult) = semanticsSession.getLatestConfidence(channelIndex: 0)
if status.isOk(), let result = confidenceResult {
    print("Confidence image size: \(result.image?.width ?? 0) x \(result.image?.height ?? 0)")
    print("Frame ID: \(result.frameId)")
    print("Timestamp: \(result.timestampMs)")
    
    // Process confidence data for semantic understanding
    processSemanticConfidence(result)
}

// Get packed semantic channels
let (status, packedResult) = semanticsSession.getLatestPackedChannels()
if status.isOk(), let result = packedResult {
    // Process packed semantic data
    processPackedSemantics(result)
}
```

</div>

</div>

</div>

</div>
