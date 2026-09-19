---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.SceneSegmentationChannels.method-contains/
title: contains
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[SceneSegmentationChannels](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-SceneSegmentationChannels/ "SceneSegmentationChannels") 

</div>

<div class="api-title">

#  contains

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">contains</span><span class="ctoken plain">(</span><span class="ctoken plain">\_</span><span class="ctoken plain"> </span><span class="ctoken plain">member</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword">Self</span><span class="ctoken plain">) -\> </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Returns a Boolean value that indicates whether a given element is a\
member of the option set.\
This example uses the `contains(_:)` method to check whether next-day\
shipping is in the `availableOptions` instance.\
let availableOptions = ShippingOptions.express\
if availableOptions.contains(.nextDay) {\
print("Next day shipping available")\
}\
// Prints "Next day shipping available"

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

`true` if the option set contains `member`; otherwise,\
`false`.

</div>

### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

<table class="api-table">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr class="api-table-row">
<td><span id="external parameter-member"></span><span class="ctoken-line"><span class="ctoken class-name">member</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">Self</span></span></td>
<td><div class="ctoken comment">
The element to look for in the option set.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
