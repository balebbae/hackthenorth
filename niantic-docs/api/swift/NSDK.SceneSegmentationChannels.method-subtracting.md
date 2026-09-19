---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.SceneSegmentationChannels.method-subtracting/
title: subtracting
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

#  subtracting

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">subtracting</span><span class="ctoken plain">(</span><span class="ctoken plain">\_</span><span class="ctoken plain"> </span><span class="ctoken plain">other</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword">Self</span><span class="ctoken plain">) -\> </span><span class="ctoken class-name keyword">Self</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Returns a new set containing the elements of this set that do not occur\
in the given set.\
In the following example, the `nonNeighbors` set is made up of the\
elements of the `employees` set that are not elements of `neighbors`:\
let employees: Set = \["Alicia", "Bethany", "Chris", "Diana", "Eric"\]\
let neighbors: Set = \["Bethany", "Eric", "Forlani", "Greta"\]\
let nonNeighbors = employees.subtracting(neighbors)\
print(nonNeighbors)\
// Prints "\["Diana", "Chris", "Alicia"\]"

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

A new set.

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
<td><span id="external parameter-other"></span><span class="ctoken-line"><span class="ctoken class-name">other</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">Self</span></span></td>
<td><div class="ctoken comment">
A set of the same type as the current set.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
