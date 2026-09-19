---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKInputDataFlags.method-remove/
title: remove
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

#  remove

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken plain">@discardableResult</span><span class="ctoken plain"> </span><span class="ctoken keyword">mutating</span><span class="ctoken plain"> </span><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">remove</span><span class="ctoken plain">(</span><span class="ctoken plain">\_</span><span class="ctoken plain"> </span><span class="ctoken plain">member</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword">Self</span><span class="ctoken plain">.</span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/element" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Element</a></span><span class="ctoken plain">) -\> </span><span class="ctoken class-name keyword">Self</span><span class="ctoken plain">.</span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/element" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Element</a></span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Removes the given element and all elements subsumed by it.\
In the following example, the `.priority` shipping option is removed from\
the `options` option set. Attempting to remove the same shipping option\
a second time results in `nil`, because `options` no longer contains\
`.priority` as a member.\
var options: ShippingOptions = \[.secondDay, .priority\]\
let priorityOption = options.remove(.priority)\
print(priorityOption == .priority)\
// Prints "true"\
print(options.remove(.priority))\
// Prints "nil"\
In the next example, the `.express` element is passed to `remove(_:)`.\
Although `.express` is not a member of `options`, `.express` subsumes\
the remaining `.secondDay` element of the option set. Therefore,\
`options` is emptied and the intersection between `.express` and\
`options` is returned.\
let expressOption = options.remove(.express)\
print(expressOption == .express)\
// Prints "false"\
print(expressOption == .secondDay)\
// Prints "true"

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The intersection of `[member]` and the set, if the\
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
<td><span id="external parameter-member"></span><span class="ctoken-line"><span class="ctoken class-name">member</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">Self</span><span class="ctoken plain">.</span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/element" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Element</a></span></span></td>
<td><div class="ctoken comment">
The element of the set to remove.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
