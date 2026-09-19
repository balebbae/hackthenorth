---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKVps2Session.method-anchorUpdate/
title: anchorUpdate
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKVps2Session](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKVps2Session/ "NSDKVps2Session") 

</div>

<div class="api-title">

#  anchorUpdate

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">anchorUpdate</span><span class="ctoken plain">(</span><span class="ctoken plain">anchorId</span><span class="ctoken plain">: </span><span class="ctoken class-name">NSDKVpsAnchorId</span><span class="ctoken plain">) -\> </span><span class="ctoken class-name">[VpsAnchorUpdate](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-VpsAnchorUpdate/ "Contains the latest tracking information for a VPS anchor....")</span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Gets the latest tracking update for a specified anchor.\
Call this for one-shot queries. For ongoing per-frame updates, subscribe to\
`anchorUpdated` instead.\
- Precondition: `anchorId` must be exactly 32 characters long.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The latest anchor update, or `nil` if the anchor ID is not recognized.

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
<td><span id="external parameter-anchorid"></span><span class="ctoken-line"><span class="ctoken class-name">anchorId</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">NSDKVpsAnchorId</span></span></td>
<td><div class="ctoken comment">
The unique identifier of a tracked anchor.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
