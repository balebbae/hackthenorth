---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.Occlusion.NsdkOcclusionSubsystem/
title: NsdkOcclusionSubsystem
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Subsystems.Occlusion](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.Occlusion/ "NianticSpatial.NSDK.AR.Subsystems.Occlusion") 

</div>

<div class="api-title">

#  NsdkOcclusionSubsystem

<div class="api-extends">

↳ extends UnityEngine.XR.ARSubsystems.XROcclusionSubsystem

</div>

<div class="api-package">

This subsystem provides implementing functionality for the XROcclusionSubsystem class.s

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">sealed</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">NsdkOcclusionSubsystem</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arsubsystems@4.2/api/UnityEngine.XR.ARSubsystems.XROcclusionSubsystem.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">XROcclusionSubsystem</a></span></span>

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
<td><span id="property-latestextrinsicsmatrix"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">LatestExtrinsicsMatrix</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nullable</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Returns the extrinsics matrix of the most recent depth prediction. This matrix<br />
represents the transformation from the camera to the world space for the image<br />
that was used to create the latest depth image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-latestintrinsicsmatrix"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">LatestIntrinsicsMatrix</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nullable</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Returns the intrinsics matrix of the most recent depth prediction. Contains values<br />
for the camera's focal length and principal point. Converts between 2D image pixel<br />
coordinates and 3D world coordinates relative to the camera.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-targetframerate"></span><span class="ctoken-line"><span class="ctoken class-name">TargetFrameRate</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">uint</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
