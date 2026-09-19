---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.SceneSegmentationChannels.method-isStrictSubset/
title: isStrictSubset
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

#  isStrictSubset

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">isStrictSubset</span><span class="ctoken plain">(</span><span class="ctoken plain">of</span><span class="ctoken plain"> </span><span class="ctoken plain">other</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword">Self</span><span class="ctoken plain">) -\> </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Returns a Boolean value that indicates whether this set is a strict\
subset of the given set.\
Set *A* is a strict subset of another set *B* if every member of *A* is\
also a member of *B* and *B* contains at least one element that is not a\
member of *A*.\
let employees: Set = \["Alicia", "Bethany", "Chris", "Diana", "Eric"\]\
let attendees: Set = \["Alicia", "Bethany", "Diana"\]\
print(attendees.isStrictSubset(of: employees))\
// Prints "true"\
// A set is never a strict subset of itself:\
print(attendees.isStrictSubset(of: attendees))\
// Prints "false"

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

`true` if the set is a strict subset of `other`; otherwise,\
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
<td><span id="external parameter-of"></span><span class="ctoken-line"><span class="ctoken class-name">other</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">Self</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
