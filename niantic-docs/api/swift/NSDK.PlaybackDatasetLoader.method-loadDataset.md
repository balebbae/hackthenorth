---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.PlaybackDatasetLoader.method-loadDataset/
title: loadDataset
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[PlaybackDatasetLoader](https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackDatasetLoader/ "PlaybackDatasetLoader") 

</div>

<div class="api-title">

#  loadDataset

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">loadDataset</span><span class="ctoken plain">() -\> </span><span class="ctoken class-name">[PlaybackDataset](https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackDataset/ "A dataset loaded from a capture JSON file containing frame metadata....")</span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Loads a dataset from the data source.\
This method only loads the capture JSON metadata upfront. Frame images and depth data\
are loaded on-demand when requested, reducing memory pressure for large datasets.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

A `PlaybackDataset` configured for on-demand loading, or `nil` if loading fails

</div>

------------------------------------------------------------------------

</div>

</div>
