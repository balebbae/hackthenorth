---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/enums/VpsAnchorUpdate.AnchorTrackingState/
title: VpsAnchorUpdate.AnchorTrackingState
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**ENUM**

<div>

# `VpsAnchorUpdate.AnchorTrackingState`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
enum AnchorTrackingState
```

</div>

</div>

Represents the current tracking state of a VPS anchor.

The tracking state indicates how well the system is able to track an anchor's position and orientation in the current environment. This information is crucial for determining the reliability of anchor pose data.

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Tracking states progress from not tracked to fully tracked, with limited tracking representing an intermediate state where tracking is possible but may be less reliable.

## Example Usage<a href="#example-usage" class="hash-link" aria-label="Direct link to Example Usage" title="Direct link to Example Usage">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
let (status, update) = vpsSession.getAnchorUpdate(anchorId: anchorId)
if status.isOk() {
    switch update.trackingState {
    case .notTracked:
        print("Anchor is not currently being tracked")
    case .limited:
        print("Anchor tracking is limited - pose may be unreliable")
    case .tracked:
        print("Anchor is fully tracked - pose is reliable")
    }
}
```

</div>

</div>

## Cases<a href="#cases" class="hash-link" aria-label="Direct link to Cases" title="Direct link to Cases">​</a>

### `notTracked`<a href="#nottracked" class="hash-link" aria-label="Direct link to nottracked" title="Direct link to nottracked">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case notTracked
```

</div>

</div>

The anchor is not currently being tracked.

This state indicates that the system cannot determine the anchor's position and orientation. This may occur when the device is not in the mapped area or when visual features are insufficient for tracking.

### `limited`<a href="#limited" class="hash-link" aria-label="Direct link to limited" title="Direct link to limited">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case limited
```

</div>

</div>

The anchor is being tracked with limited accuracy.

In this state, the system can provide pose estimates but they may be less reliable than fully tracked anchors. This often occurs during initialization or when visual conditions are challenging.

### `tracked`<a href="#tracked" class="hash-link" aria-label="Direct link to tracked" title="Direct link to tracked">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case tracked
```

</div>

</div>

The anchor is being tracked with full accuracy.

This is the optimal tracking state where the system can provide reliable pose estimates for the anchor. The anchor's position and orientation should be considered accurate for AR applications.

</div>

</div>
