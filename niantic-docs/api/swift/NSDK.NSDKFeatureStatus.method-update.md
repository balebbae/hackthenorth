---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKFeatureStatus.method-update/
title: update
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKFeatureStatus](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKFeatureStatus/ "NSDKFeatureStatus") 

</div>

<div class="api-title">

#  update

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken plain">@discardableResult</span><span class="ctoken plain"> </span><span class="ctoken keyword">mutating</span><span class="ctoken plain"> </span><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">update</span><span class="ctoken plain">(</span><span class="ctoken plain">with</span><span class="ctoken plain"> </span><span class="ctoken plain">newMember</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword">Self</span><span class="ctoken plain">.</span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/element" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Element</a></span><span class="ctoken plain">) -\> </span><span class="ctoken class-name keyword">Self</span><span class="ctoken plain">.</span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/element" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Element</a></span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Inserts the given element into the set.\
If `newMember` is not contained in the set but subsumes current members\
of the set, the subsumed members are returned.\
var options: ShippingOptions = \[.secondDay, .priority\]\
let replaced = options.update(with: .express)\
print(replaced == .secondDay)\
// Prints "true"

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The intersection of `[newMember]` and the set if the\
intersection was nonempty; otherwise, `nil`.

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
<td><span id="external parameter-with"></span><span class="ctoken-line"><span class="ctoken class-name">newMember</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">Self</span><span class="ctoken plain">.</span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/element" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Element</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
