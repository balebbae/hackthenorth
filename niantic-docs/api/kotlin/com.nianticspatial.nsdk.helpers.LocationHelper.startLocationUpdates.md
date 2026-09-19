---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers.LocationHelper.startLocationUpdates/
title: startLocationUpdates
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.helpers](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers/ "com.nianticspatial.nsdk.helpers") <span class="api-breadcrumbs-nav">←</span>[LocationHelper](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers.LocationHelper/ "com.nianticspatial.nsdk.helpers.LocationHelper") 

</div>

<div class="api-title">

#  startLocationUpdates

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken plain">@</span><span class="ctoken class-name"><a href="https://developer.android.com/reference/android/annotation/SuppressLint" target="_blank" rel="noopener noreferrer" title="Opens an external reference">SuppressLint</a></span><span class="ctoken punctuation">(</span><span class="ctoken plain">"MissingPermission"</span><span class="ctoken punctuation">)</span><span class="ctoken plain"> </span><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">startLocationUpdates</span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Begins receiving GPS updates. Delivers the last known location immediately (if available),\
then streams new fixes at ~5-second intervals via `OnUpdateListener.onLocationUpdate`.\
Requires `ACCESS_FINE_LOCATION``android.Manifest.permission.ACCESS_FINE_LOCATION`; no-op if\
the permission is not granted.

</div>

------------------------------------------------------------------------

</div>

</div>
