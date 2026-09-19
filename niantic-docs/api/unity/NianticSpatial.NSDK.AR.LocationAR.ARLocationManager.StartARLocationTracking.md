---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.LocationAR.ARLocationManager.StartARLocationTracking/
title: StartARLocationTracking
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.LocationAR](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.LocationAR/ "NianticSpatial.NSDK.AR.LocationAR") <span class="api-breadcrumbs-nav">←</span>[ARLocationManager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.LocationAR.ARLocationManager/ "NianticSpatial.NSDK.AR.LocationAR.ARLocationManager") 

</div>

<div class="api-title">

#  StartARLocationTracking

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">void</span><span class="ctoken plain"> </span><span class="ctoken class-name">StartARLocationTracking</span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Starts tracking locations specified by SetARLocations() or set in Unity Editor

\

\
Content authored as children of the ARLocation will be enabled once the ARLocation becomes tracked.\
This will create digital content in the physical world.

\

\
If no locations were specified in SetARLocations(), requests will be made to attempt to track nearby\
locations. In this case, multiple nearby locations may be targeted and the first one to successfully\
track will be used.

</div>

------------------------------------------------------------------------

</div>

</div>
