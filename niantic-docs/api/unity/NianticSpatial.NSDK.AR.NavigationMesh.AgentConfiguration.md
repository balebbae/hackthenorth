---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.AgentConfiguration/
title: AgentConfiguration
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.NavigationMesh](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh/ "NianticSpatial.NSDK.AR.NavigationMesh") 

</div>

<div class="api-title">

#  AgentConfiguration

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken keyword">struct</span><span class="ctoken plain"> </span><span class="ctoken class-name">AgentConfiguration</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span>

------------------------------------------------------------------------

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name">AgentConfiguration</span><span class="ctoken punctuation">(</span><span class="ctoken class-name keyword">int</span><span class="ctoken plain"> </span><span class="ctoken class-name">jumpPenalty</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">float</span><span class="ctoken plain"> </span><span class="ctoken class-name">jumpDistance</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name">[PathFindingBehaviour](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.PathFindingBehaviour/ "Browse to PathFindingBehaviour")</span><span class="ctoken plain"> </span><span class="ctoken class-name">behaviour</span><span class="ctoken punctuation">)</span></span>

</div>

------------------------------------------------------------------------

## Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

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
<td><span id="field-behaviour"></span><span class="ctoken-line"><span class="ctoken class-name">Behaviour</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.PathFindingBehaviour/" title="Browse to PathFindingBehaviour">PathFindingBehaviour</a></span></span></td>
<td><div class="ctoken comment">
Determines how the agent should behave when its destination is on a foreign surface.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-jumpdistance"></span><span class="ctoken-line"><span class="ctoken class-name">JumpDistance</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
The maximum distance an agent can jump in meters.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-jumppenalty"></span><span class="ctoken-line"><span class="ctoken class-name">JumpPenalty</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
Determines the cost of jumping.<br />
@discussion<br />
Being off-surface includes steps taken at the jumping off point<br />
and steps taken mid-jump.<br />
If there is a 1 cell block between the start and the destination,<br />
assuming going around takes ~3 points, then jumping over with no<br />
penalty will cost 2 points, jumping over with 1 penalty will cost<br />
3 points, and so on... If there is a gap between the two surfaces,<br />
the cost of jumping will aggregate with each step until the agent<br />
lands on a surface.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

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
<td><span id="method-createjumpingagent"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.AgentConfiguration.CreateJumpingAgent/" title="Browse to CreateJumpingAgent">CreateJumpingAgent</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">AgentConfiguration</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-createsimpleagent"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.AgentConfiguration.CreateSimpleAgent/" title="Browse to CreateSimpleAgent">CreateSimpleAgent</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">AgentConfiguration</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
