---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh/
title: NianticSpatial.NSDK.AR.NavigationMesh
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") 

</div>

<div class="api-title">

#  NavigationMesh

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
<td><span id="class-navmeshmodel"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NavMeshModel/" title="Browse to NavMeshModel">NavMeshModel</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NavMeshModel/" title="Browse to NavMeshModel">NavMeshModel</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdknavmesh"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMesh/" title="This class manages the data structures associated with a navigation mesh (&quot;NsdkNavMesh&quot;)....">NsdkNavMesh</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMesh/" title="This class manages the data structures associated with a navigation mesh (&quot;NsdkNavMesh&quot;)....">NsdkNavMesh</a></span></span></td>
<td><div class="ctoken comment">
This class manages the data structures associated with a navigation mesh ("NsdkNavMesh").<br />
It dynamically builds a 2d grid on the meshes detected in the environment for running navigation algorithms on.<br />
You are able to retrieve a number of properties of the "NsdkNavMesh" from it.<br />
There are also a number of methods to help you place and move NsdkNavMeshAgents on the board.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdknavmeshagent"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMeshAgent/" title="NsdkNavMeshAgent is an example agent implementation that navigates a NsdkNavMesh based on logic programmed here....">NsdkNavMeshAgent</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">MonoBehaviour</a></span></span></td>
<td><div class="ctoken comment">
NsdkNavMeshAgent is an example agent implementation that navigates a NsdkNavMesh based on logic programmed here.<br />
You place this MonoBehaviour on a GameObject to have that GameObject navigate autonomously through your real environment.<br />
You can create new versions of this to change how your creatures navigate the NsdkNavMesh.<br />
For example you may want to use physics/forces or add splines rather than straight lines.<br />
This is a basic example that uses linear interpolation and coroutines.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdknavmeshagentpathrenderer"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMeshAgentPathRenderer/" title="NsdkNavMeshAgentPathRenderer is a debug renderer to show you the path a  NsdkNavMeshAgent is moving along...">NsdkNavMeshAgentPathRenderer</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">MonoBehaviour</a></span></span></td>
<td><div class="ctoken comment">
NsdkNavMeshAgentPathRenderer is a debug renderer to show you the path a NsdkNavMeshAgent is moving along<br />
while navigating the environment. You add it to the NsdkNavMeshAgentGameObject in your scene<br />
and it will draw that agent's current path.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdknavmeshmanager"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMeshManager/" title="NsdkNavMeshManager is a MonoBehaviour that will create a NsdkNavMesh configured according to your settings and manage how it gets updated....">NsdkNavMeshManager</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">MonoBehaviour</a></span></span></td>
<td><div class="ctoken comment">
NsdkNavMeshManager is a MonoBehaviour that will create a NsdkNavMesh configured according to your settings and manage how it gets updated.<br />
You can add this component to a GameObject in your scene to use the NsdkNavMesh features.<br />
You can pass this to any GameObject s that may need the NsdkNavMesh e.g. your agents that handle moving across the board.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdknavmeshrenderer"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMeshRenderer/" title="NsdkNavMeshRenderer is a helper MonoBehaviour which will draw the NsdkNavMesh tiles...">NsdkNavMeshRenderer</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">MonoBehaviour</a></span></span></td>
<td><div class="ctoken comment">
NsdkNavMeshRenderer is a helper MonoBehaviour which will draw the NsdkNavMesh tiles<br />
If you want to draw the NsdkNavMesh in a custom way you can create a similar renderer<br />
e.g. stylize the board as water/snow/sand etc.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-path"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.Path/" title="Browse to Path">Path</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.Path/" title="Browse to Path">Path</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-spatialtree"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.SpatialTree/" title="Browse to SpatialTree">SpatialTree</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.SpatialTree/" title="Browse to SpatialTree">SpatialTree</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-surface"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.Surface/" title="Represents a subset on the grid with cells of approximately the same elevation.">Surface</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.Surface/" title="Represents a subset on the grid with cells of approximately the same elevation.">Surface</a></span></span></td>
<td><div class="ctoken comment">
Represents a subset on the grid with cells of approximately the same elevation.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-utils"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.Utils/" title="Browse to Utils">Utils</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.Utils/" title="Browse to Utils">Utils</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Structs<a href="#structs" class="hash-link" aria-label="Direct link to Structs" title="Direct link to Structs">​</a>

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
<td><span id="struct-agentconfiguration"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.AgentConfiguration/" title="Browse to AgentConfiguration">AgentConfiguration</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-bounds"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.Bounds/" title="Specifies an area in a top-down 2D grid using a square.">Bounds</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">IEquatable</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.Bounds/" title="Specifies an area in a top-down 2D grid using a square.">Bounds</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Specifies an area in a top-down 2D grid using a square.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-gridnode"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.GridNode/" title="Encloses data for grid elements used during scanning for walkable areas.">GridNode</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">IEquatable</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.GridNode/" title="Encloses data for grid elements used during scanning for walkable areas.">GridNode</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Encloses data for grid elements used during scanning for walkable areas.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-modelsettings"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.ModelSettings/" title="The ModelSettings struct provides a configuration for how NsdkNavMesh scans the real environment and creates a navigable space....">ModelSettings</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span></td>
<td><div class="ctoken comment">
The ModelSettings struct provides a configuration for how NsdkNavMesh scans the real environment and creates a navigable space.<br />
An instance of ModelSettings is created by the NsdkNavMeshManager using the parameters specified by the user in the Inspector,<br />
and that instance is subsequently used to create a NsdkNavMesh that is configured this way.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-waypoint"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.Waypoint/" title="Browse to Waypoint">Waypoint</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Enums<a href="#enums" class="hash-link" aria-label="Direct link to Enums" title="Direct link to Enums">​</a>

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
<td><span id="enum-agentnavigationstate"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMeshAgent.AgentNavigationState/" title="Browse to AgentNavigationState">AgentNavigationState</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMeshAgent.AgentNavigationState/" title="Browse to AgentNavigationState">AgentNavigationState</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-movementtype"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.Waypoint.MovementType/" title="The type of movement of a waypoint">MovementType</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.Waypoint.MovementType/" title="The type of movement of a waypoint">MovementType</a></span></span></td>
<td><div class="ctoken comment">
The type of movement of a waypoint
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-pathfindingbehaviour"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.PathFindingBehaviour/" title="Browse to PathFindingBehaviour">PathFindingBehaviour</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.PathFindingBehaviour/" title="Browse to PathFindingBehaviour">PathFindingBehaviour</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-status"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.Path.Status/" title="Browse to Status">Status</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.Path.Status/" title="Browse to Status">Status</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
