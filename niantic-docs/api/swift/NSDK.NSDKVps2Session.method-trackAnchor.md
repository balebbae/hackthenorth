---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKVps2Session.method-trackAnchor/
title: trackAnchor
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

#  trackAnchor

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">trackAnchor</span><span class="ctoken plain">(</span><span class="ctoken plain">payload</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">) </span><span class="ctoken keyword">throws</span><span class="ctoken plain"> -\> </span><span class="ctoken class-name">NSDKVpsAnchorId</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Requests to start tracking an anchor specified by a payload.\
A VPS payload contains all the data needed to localize at a VPS-activated location.\
A default payload for a VPS-activated location can be obtained from the "blob" field\
in the details view of an entry in the Geospatial Browser, or via\
`anchorPayload(anchorId:)` for user-generated anchors.\
The returned anchor ID is automatically polled each frame via `update()`, and updates\
are published on `anchorUpdated`.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The unique identifier of the anchor encoded in the payload.

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- `NSDKError.invalidArgument` if the payload is not valid.

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
<td><span id="external parameter-payload"></span><span class="ctoken-line"><span class="ctoken class-name">payload</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span></span></td>
<td><div class="ctoken comment">
Base64-encoded anchor payload.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
