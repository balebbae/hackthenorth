---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Settings.PrivacyData/
title: PrivacyData
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Settings](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Settings/ "NianticSpatial.NSDK.AR.Settings") 

</div>

<div class="api-title">

#  PrivacyData

<div class="api-package">

This class contains all the data required for data management requests.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">partial</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">PrivacyData</span></span>

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
<td><span id="property-clientid"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">ClientId</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
This is the device Id used to identify any device. In case there is no userId, the clientId can be provided<br />
for your GDPR data requests.<br />
If you are an NSDK developer, clientId is Unity's SystemInfo.deviceUniqueIdentifier.<br />
For your game users, it is a random Guid. In case of no userId, you have to record it.<br />
It changes if the ios/android app is uninstalled and reinstalled. It remains the same over app upgrades
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
