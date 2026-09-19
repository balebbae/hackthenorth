---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.SceneSegmentationChannels.method-insert/
title: insert
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

#  insert

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken plain">@discardableResult</span><span class="ctoken plain"> </span><span class="ctoken keyword">mutating</span><span class="ctoken plain"> </span><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">insert</span><span class="ctoken plain">(</span><span class="ctoken plain">\_</span><span class="ctoken plain"> </span><span class="ctoken plain">newMember</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword">Self</span><span class="ctoken plain">.</span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/element" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Element</a></span><span class="ctoken plain">) -\> (inserted</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span><span class="ctoken plain">, memberAfterInsert</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword">Self</span><span class="ctoken plain">.</span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/element" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Element</a></span><span class="ctoken plain">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Adds the given element to the option set if it is not already a member.\
In the following example, the `.secondDay` shipping option is added to\
the `freeOptions` option set if `purchasePrice` is greater than 50.0. For\
the `ShippingOptions` declaration, see the `OptionSet` protocol\
discussion.\
let purchasePrice = 87.55\
var freeOptions: ShippingOptions = \[.standard, .priority\]\
if purchasePrice \> 50 {\
freeOptions.insert(.secondDay)\
}\
print(freeOptions.contains(.secondDay))\
// Prints "true"

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

`(true, newMember)` if `newMember` was not contained in\
`self`. Otherwise, returns `(false, oldMember)`, where `oldMember` is\
the member of the set equal to `newMember`.

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
<td><span id="external parameter-newmember"></span><span class="ctoken-line"><span class="ctoken class-name">newMember</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">Self</span><span class="ctoken plain">.</span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/element" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Element</a></span></span></td>
<td><div class="ctoken comment">
The element to insert.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
