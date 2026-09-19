---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKInputDataFlags.method-union/
title: union
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKInputDataFlags](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKInputDataFlags/ "NSDKInputDataFlags") 

</div>

<div class="api-title">

#  union

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">union</span><span class="ctoken plain">(</span><span class="ctoken plain">\_</span><span class="ctoken plain"> </span><span class="ctoken plain">other</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword">Self</span><span class="ctoken plain">) -\> </span><span class="ctoken class-name keyword">Self</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Returns a new option set of the elements contained in this set, in the\
given set, or in both.\
This example uses the `union(_:)` method to add two more shipping options\
to the default set.\
let defaultShipping = ShippingOptions.standard\
let memberShipping = defaultShipping.union(\[.secondDay, .priority\])\
print(memberShipping.contains(.priority))\
// Prints "true"

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

A new option set made up of the elements contained in this\
set, in `other`, or in both.

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
An option set.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
