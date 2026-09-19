---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSessionDataSource.method-latestCameraSample/
title: latestCameraSample
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKSessionDataSource](https://www.nianticspatial.com/docs/api/swift/NSDK.interface-NSDKSessionDataSource/ "NSDKSessionDataSource") 

</div>

<div class="api-title">

#  latestCameraSample

<div class="api-package">

Returns the most recent camera sample, if available.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">latestCameraSample</span><span class="ctoken plain">() -\> (image</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreVideo/CVPixelBuffer" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CVPixelBuffer</a></span><span class="ctoken plain">, intrinsics</span><span class="ctoken plain">: </span><span class="ctoken class-name">NSDKCameraIntrinsics</span><span class="ctoken plain">, pose</span><span class="ctoken plain">: </span><span class="ctoken class-name">NSDKCameraExtrinsics</span><span class="ctoken plain">, orientation</span><span class="ctoken plain">: </span><span class="ctoken class-name">[NSDKScreenOrientation](https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKScreenOrientation/ "Represents the screen orientation in the NSDK layer.")</span><span class="ctoken plain">, timestamp</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/uint64" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UInt64</a></span><span class="ctoken plain">)?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Returns the most recent camera sample, if available.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

A tuple containing:\
- image: A retained `CVPixelBuffer` representing the captured image.\
- intrinsics: Camera intrinsic parameters for the image.\
- pose: The pose (extrinsics) of the camera associated with the image.\
- orientation: The device orientation of the camera associated with the image.\
- timestamp: Camera timestamp in milliseconds.

</div>

------------------------------------------------------------------------

</div>

</div>
