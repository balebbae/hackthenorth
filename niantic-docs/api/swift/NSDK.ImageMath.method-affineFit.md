---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.ImageMath.method-affineFit/
title: affineFit
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[ImageMath](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-ImageMath/ "ImageMath") 

</div>

<div class="api-title">

#  affineFit

<div class="api-package">

Returns an affine transformation that maps normalized coordinates in the source frame to normalized coordinates in the target frame.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">affineFit</span><span class="ctoken plain">(</span><span class="ctoken plain">source</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGSize" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGSize</a></span><span class="ctoken plain">, </span><span class="ctoken plain">sourceOrientation</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//uikit/UIInterfaceOrientation" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UIInterfaceOrientation</a></span><span class="ctoken plain">, </span><span class="ctoken plain">target</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGSize" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGSize</a></span><span class="ctoken plain">, </span><span class="ctoken plain">targetOrientation</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//uikit/UIInterfaceOrientation" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UIInterfaceOrientation</a></span><span class="ctoken plain">) -\> </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGAffineTransform" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGAffineTransform</a></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Returns an affine transformation that maps normalized coordinates in the source frame to normalized coordinates in the target frame.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

An affine transformation matrix that fits the source into the target.

</div>

<div class="theme-admonition theme-admonition-info admonition_xJq3 alert alert--info">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)</span>Notice

</div>

<div class="admonitionContent_BuS1">

Note: In portrait, this function aligns the top and bottom edges to the target.

</div>

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
<td><span id="external parameter-source"></span><span class="ctoken-line"><span class="ctoken class-name">source</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGSize" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGSize</a></span></span></td>
<td><div class="ctoken comment">
The size of the source container.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-sourceorientation"></span><span class="ctoken-line"><span class="ctoken class-name">sourceOrientation</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//uikit/UIInterfaceOrientation" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UIInterfaceOrientation</a></span></span></td>
<td><div class="ctoken comment">
The orientation of the source container.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-target"></span><span class="ctoken-line"><span class="ctoken class-name">target</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGSize" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGSize</a></span></span></td>
<td><div class="ctoken comment">
The size of the target container.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-targetorientation"></span><span class="ctoken-line"><span class="ctoken class-name">targetOrientation</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//uikit/UIInterfaceOrientation" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UIInterfaceOrientation</a></span></span></td>
<td><div class="ctoken comment">
The orientation of the target container.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
