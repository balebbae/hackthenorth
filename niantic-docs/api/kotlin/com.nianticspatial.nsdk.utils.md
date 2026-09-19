---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils/
title: com.nianticspatial.nsdk.utils
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") 

</div>

<div class="api-title">

#  utils

</div>

------------------------------------------------------------------------

## Classes<a href="#classes" class="hash-link" aria-label="Direct link to Classes" title="Direct link to Classes">​</a>

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
<td><span id="class-flowpollingmanager"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.FlowPollingManager/" title="Manages Flow-based polling for session updates with automatic subscriber tracking...">FlowPollingManager</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.FlowPollingManager/" title="Manages Flow-based polling for session updates with automatic subscriber tracking...">FlowPollingManager</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name">T</span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Manages Flow-based polling for session updates with automatic subscriber tracking<br />
and frame deduplication.<br />
This class abstracts the common pattern of:<br />
- Creating a MutableSharedFlow<br />
- Tracking active subscribers<br />
- Starting/stopping polling coroutines based on subscriber count<br />
- Deduplicating updates by frame ID or timestamp
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
