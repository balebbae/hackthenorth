---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session.getPose/
title: getPose
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.vps2](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2/ "com.nianticspatial.nsdk.vps2") <span class="api-breadcrumbs-nav">←</span>[Vps2Session](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session/ "com.nianticspatial.nsdk.vps2.Vps2Session") 

</div>

<div class="api-title">

#  getPose

<div class="api-package">

Convert a geolocation to an AR pose using a localization snapshot.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">getPose</span><span class="ctoken punctuation">(</span><span class="ctoken plain">localization</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[Vps2Localization](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Localization/ "Spatial mapping between the device's AR coordinate space and real-world...")</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">location</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[GeolocationData](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.GeolocationData/ "Browse to GeolocationData")</span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://developers.google.com/ar/reference/java/com/google/ar/core/Pose" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Pose</a></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Convert a geolocation to an AR pose using a localization snapshot.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The AR pose corresponding to the given `location`.

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- `NsdkInvalidOperationStatusException` — if the current localization tracking state is `VPS2TrackingState.UNAVAILABLE`.

------------------------------------------------------------------------

## Overload<a href="#overload" class="hash-link" aria-label="Direct link to Overload" title="Direct link to Overload">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">getPose</span><span class="ctoken punctuation">(</span><span class="ctoken plain">localization</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[Vps2Localization](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Localization/ "Spatial mapping between the device's AR coordinate space and real-world...")</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">location</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">Location</span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://developers.google.com/ar/reference/java/com/google/ar/core/Pose" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Pose</a></span></span>

</div>

#### Summary<a href="#summary-1" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Convert an Android `Location` to an AR pose using a localization snapshot.

</div>

#### Returns<a href="#returns-1" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The AR pose corresponding to the given `location`.

</div>

#### Throws<a href="#throws-1" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- `NsdkInvalidOperationStatusException` — if the current localization tracking state is `VPS2TrackingState.UNAVAILABLE`.

------------------------------------------------------------------------

</div>

</div>
