---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.ARUtils.method-isLidarAvailable/
title: isLidarAvailable
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[ARUtils](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-ARUtils/ "ARUtils") 

</div>

<div class="api-title">

#  isLidarAvailable

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">isLidarAvailable</span><span class="ctoken plain">() -\> </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Checks if LiDAR depth is available on the current device.\
LiDAR depth data significantly improves the accuracy of NSDK features\
such as device mapping, scanning, and localization.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

`true` if LiDAR is available and supported, `false` otherwise

</div>

#### Example<a href="#example" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
if ARUtils.isLidarAvailable() {
    print("LiDAR is available - enhanced depth sensing enabled")
    // Configure NSDK to use LiDAR data
    let session = NSDKSession(apiKey: "your-key", useLidar: true)
} else {
    print("LiDAR not available - using alternative depth methods")
    let session = NSDKSession(apiKey: "your-key", useLidar: false)
}
```

</div>

</div>

#### Device Support<a href="#device-support" class="hash-link" aria-label="Direct link to Device Support" title="Direct link to Device Support">​</a>

LiDAR is available on:

- iPad Pro (4th generation and later)
- iPhone 12 Pro and iPhone 12 Pro Max
- iPhone 13 Pro and iPhone 13 Pro Max
- iPhone 14 Pro and iPhone 14 Pro Max
- iPhone 15 Pro and iPhone 15 Pro Max

------------------------------------------------------------------------

</div>

</div>
