---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.PlaybackSession.method-run/
title: run
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[PlaybackSession](https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackSession/ "PlaybackSession") 

</div>

<div class="api-title">

#  run

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">override</span><span class="ctoken plain"> </span><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">run</span><span class="ctoken plain">(</span><span class="ctoken plain">\_</span><span class="ctoken plain"> </span><span class="ctoken plain">configuration</span><span class="ctoken plain">: </span><span class="ctoken class-name">ARConfiguration</span><span class="ctoken plain">, </span><span class="ctoken plain">options</span><span class="ctoken plain">: </span><span class="ctoken class-name">ARSession</span><span class="ctoken plain">.</span><span class="ctoken class-name">RunOptions</span><span class="ctoken plain"> = \[\])</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Starts playback. The playback loop runs asynchronously on a background queue; frames are delivered on the main queue.\
Configuration and options are ignored (playback uses the dataset's frame rate and content). Call `pause()` to stop.

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
<td><span id="external parameter-configuration"></span><span class="ctoken-line"><span class="ctoken class-name">configuration</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">ARConfiguration</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-options"></span><span class="ctoken-line"><span class="ctoken class-name">options</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">ARSession</span><span class="ctoken plain">.</span><span class="ctoken class-name">RunOptions</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
