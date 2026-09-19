---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.FlowPollingManager/
title: FlowPollingManager
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.utils](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils/ "com.nianticspatial.nsdk.utils") 

</div>

<div class="api-title">

#  FlowPollingManager

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">FlowPollingManager</span><span class="ctoken punctuation">\<</span><span class="ctoken class-name">T</span><span class="ctoken punctuation">\></span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Manages Flow-based polling for session updates with automatic subscriber tracking and frame deduplication. This class abstracts the common pattern of:

- Creating a MutableSharedFlow
- Tracking active subscribers
- Starting/stopping polling coroutines based on subscriber count
- Deduplicating updates by frame ID or timestamp

------------------------------------------------------------------------

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

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
<td><span id="property-flow"></span><span class="ctoken-line"><span class="ctoken class-name">flow</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/kotlinx.coroutines.flow.-flow" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Flow</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name">T</span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Public Flow that automatically manages polling lifecycle.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Functions<a href="#functions" class="hash-link" aria-label="Direct link to Functions" title="Direct link to Functions">​</a>

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
<td><span id="function-destroy"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.FlowPollingManager.destroy/" title="Cleans up resources. Should be called when the session is destroyed.">destroy</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Cleans up resources. Should be called when the session is destroyed.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
