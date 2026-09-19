---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/ARUtils/
title: ARUtils
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `ARUtils`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct ARUtils
```

</div>

</div>

Utility functions for AR and device capability detection.

`ARUtils` provides helper methods for detecting device capabilities and AR features that are relevant to ARDK functionality.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `isLidarAvailable()`<a href="#islidaravailable" class="hash-link" aria-label="Direct link to islidaravailable" title="Direct link to islidaravailable">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static func isLidarAvailable() -> Bool
```

</div>

</div>

Checks if LiDAR depth is available on the current device.

LiDAR depth data significantly improves the accuracy of ARDK features such as device mapping, scanning, and localization.

- Returns: `true` if LiDAR is available and supported, `false` otherwise

## Example<a href="#example" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
if ARUtils.isLidarAvailable() {
    print("LiDAR is available - enhanced depth sensing enabled")
    // Configure ARDK to use LiDAR data
    let session = ArdkSession(apiKey: "your-key", useLidar: true)
} else {
    print("LiDAR not available - using alternative depth methods")
    let session = ArdkSession(apiKey: "your-key", useLidar: false)
}
```

</div>

</div>

## Device Support<a href="#device-support" class="hash-link" aria-label="Direct link to Device Support" title="Direct link to Device Support">​</a>

LiDAR is available on:

- iPad Pro (4th generation and later)
- iPhone 12 Pro and iPhone 12 Pro Max
- iPhone 13 Pro and iPhone 13 Pro Max
- iPhone 14 Pro and iPhone 14 Pro Max
- iPhone 15 Pro and iPhone 15 Pro Max

</div>

</div>
