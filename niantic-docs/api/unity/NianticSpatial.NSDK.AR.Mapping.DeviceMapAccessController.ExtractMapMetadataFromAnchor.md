---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Mapping.DeviceMapAccessController.ExtractMapMetadataFromAnchor/
title: ExtractMapMetadataFromAnchor
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Mapping](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Mapping/ "NianticSpatial.NSDK.AR.Mapping") <span class="api-breadcrumbs-nav">←</span>[DeviceMapAccessController](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Mapping.DeviceMapAccessController/ "NianticSpatial.NSDK.AR.Mapping.DeviceMapAccessController") 

</div>

<div class="api-title">

#  ExtractMapMetadataFromAnchor

<div class="api-package">

Extract the metadata from a map relative to an anchor on the map.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">bool</span><span class="ctoken plain"> </span><span class="ctoken class-name">ExtractMapMetadataFromAnchor</span><span class="ctoken punctuation">(</span><span class="ctoken class-name keyword">string</span><span class="ctoken plain"> </span><span class="ctoken class-name">anchorPayload</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">byte</span><span class="ctoken punctuation">\[</span><span class="ctoken punctuation">\]</span><span class="ctoken plain"> </span><span class="ctoken class-name">mapData</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken keyword">out</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector3</a></span><span class="ctoken punctuation">\[</span><span class="ctoken punctuation">\]</span><span class="ctoken plain"> </span><span class="ctoken class-name">points</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken keyword">out</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">float</span><span class="ctoken punctuation">\[</span><span class="ctoken punctuation">\]</span><span class="ctoken plain"> </span><span class="ctoken class-name">errors</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Extract the metadata from a map relative to an anchor on the map.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

True if successful, false otherwise.

</div>

<div class="theme-admonition theme-admonition-info admonition_xJq3 alert alert--info">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)</span>Notice

</div>

<div class="admonitionContent_BuS1">

This is an experimental feature, and is subject to breaking changes or deprecation without notice

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
<td><span id="external parameter-anchorpayload"></span><span class="ctoken-line"><span class="ctoken class-name">anchorPayload</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
The anchor payload as a byte array. The returned map metadata<br />
will be relative to this anchor.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-mapdata"></span><span class="ctoken-line"><span class="ctoken class-name">mapData</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">byte</span><span class="ctoken punctuation">[</span><span class="ctoken punctuation">]</span></span></td>
<td><div class="ctoken comment">
The map to extract the metadata from.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-points"></span><span class="ctoken-line"><span class="ctoken class-name">points</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector3</a></span><span class="ctoken punctuation">[</span><span class="ctoken punctuation">]</span></span></td>
<td><div class="ctoken comment">
The positions of the feature points in the map.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-errors"></span><span class="ctoken-line"><span class="ctoken class-name">errors</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span><span class="ctoken punctuation">[</span><span class="ctoken punctuation">]</span></span></td>
<td><div class="ctoken comment">
The error metric for each of the points in the map.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
