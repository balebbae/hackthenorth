---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKDepthSession.method-configure/
title: configure
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKDepthSession](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKDepthSession/ "NSDKDepthSession") 

</div>

<div class="api-title">

#  configure

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">configure</span><span class="ctoken plain">(</span><span class="ctoken plain">with</span><span class="ctoken plain"> </span><span class="ctoken plain">config</span><span class="ctoken plain">: </span><span class="ctoken class-name">[Configuration](https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKDepthSession.struct-Configuration/ "The type of configuration used by this session")</span><span class="ctoken plain">) </span><span class="ctoken keyword">throws</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Configures the session with the specified settings.\
- Attention: This method must be called while the session is stopped,\
or else configuration will fail. In that case, while this function returns without\
throwing, configuration will still fail asynchronously. Use `featureStatus()`\
to check that configuration has not failed.

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- `NSDKError.invalidArgument` if the configuration is invalid. Check NSDK's C logs for more information.

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
<td><span id="external parameter-with"></span><span class="ctoken-line"><span class="ctoken class-name">config</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKDepthSession.struct-Configuration/" title="The type of configuration used by this session">Configuration</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
