---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKInputDataFlags.method-subtract/
title: subtract
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

#  subtract

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">mutating</span><span class="ctoken plain"> </span><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">subtract</span><span class="ctoken plain">(</span><span class="ctoken plain">\_</span><span class="ctoken plain"> </span><span class="ctoken plain">other</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword">Self</span><span class="ctoken plain">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Removes the elements of the given set from this set.\
In the following example, the elements of the `employees` set that are\
also members of the `neighbors` set are removed. In particular, the\
names `"Bethany"` and `"Eric"` are removed from `employees`.\
var employees: Set = \["Alicia", "Bethany", "Chris", "Diana", "Eric"\]\
let neighbors: Set = \["Bethany", "Eric", "Forlani", "Greta"\]\
employees.subtract(neighbors)\
print(employees)\
// Prints "\["Diana", "Chris", "Alicia"\]"

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
