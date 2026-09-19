---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.CameraMath/
title: CameraMath
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Utilities](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities/ "NianticSpatial.NSDK.AR.Utilities") 

</div>

<div class="api-title">

#  CameraMath

<div class="api-package">

A collection of functions used to calculate transformations for AR imaging.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">CameraMath</span></span>

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
<td><span id="method-calculatedisplaymatrix"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.CameraMath.CalculateDisplayMatrix/" title="Returns an affine transformation matrix for converting between normalized image...">CalculateDisplayMatrix</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span></span></td>
<td><div class="ctoken comment">
Returns an affine transformation matrix for converting between normalized image<br />
coordinates and a coordinate space appropriate for rendering the camera image onscreen.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-calculateprojectionmatrix"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.CameraMath.CalculateProjectionMatrix/" title="Returns a transform matrix appropriate for rendering 3D content to match the image...">CalculateProjectionMatrix</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span></span></td>
<td><div class="ctoken comment">
Returns a transform matrix appropriate for rendering 3D content to match the image<br />
captured by the camera, using the specified parameters.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-calculatezbufferparams"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.CameraMath.CalculateZBufferParams/" title="Calculates a ZBufferParams container, similar to the built-in _ZBufferParams...">CalculateZBufferParams</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector4</a></span></span></td>
<td><div class="ctoken comment">
Calculates a ZBufferParams container, similar to the built-in _ZBufferParams<br />
used in shaders, but instead of using the clipping plane distances of the camera,<br />
it will consider the specified near and far values.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-cameratodisplayrotation"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.CameraMath.CameraToDisplayRotation/" title="Browse to CameraToDisplayRotation">CameraToDisplayRotation</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Quaternion</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-displaytocamerarotation"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.CameraMath.DisplayToCameraRotation/" title="Browse to DisplayToCameraRotation">DisplayToCameraRotation</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Quaternion</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
