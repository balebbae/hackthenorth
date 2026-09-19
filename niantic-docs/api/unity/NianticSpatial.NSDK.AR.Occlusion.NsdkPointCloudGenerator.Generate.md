---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Occlusion.NsdkPointCloudGenerator.Generate/
title: Generate
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Occlusion](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Occlusion/ "NianticSpatial.NSDK.AR.Occlusion") <span class="api-breadcrumbs-nav">←</span>[NsdkPointCloudGenerator](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Occlusion.NsdkPointCloudGenerator/ "NianticSpatial.NSDK.AR.Occlusion.NsdkPointCloudGenerator") 

</div>

<div class="api-title">

#  Generate

<div class="api-package">

Generate a point cloud from a depth texture using the given intrinsics and extrinsics.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector4</a></span><span class="ctoken punctuation">\[</span><span class="ctoken punctuation">\]</span><span class="ctoken plain"> </span><span class="ctoken class-name">Generate</span><span class="ctoken punctuation">(</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Texture</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">depth</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arsubsystems@4.2/api/UnityEngine.XR.ARSubsystems.XRCameraIntrinsics.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">XRCameraIntrinsics</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">intrinsics</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">extrinsics</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Generate a point cloud from a depth texture using the given intrinsics and extrinsics.

</div>

#### Remarks<a href="#remarks" class="hash-link" aria-label="Direct link to Remarks" title="Direct link to Remarks">​</a>

<div class="ctoken comment">

This is an allocating, blocking call.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

A collection of 3D points generated from the image.

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
<td><span id="external parameter-depth"></span><span class="ctoken-line"><span class="ctoken class-name">depth</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Texture</a></span></span></td>
<td><div class="ctoken comment">
The depth image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-intrinsics"></span><span class="ctoken-line"><span class="ctoken class-name">intrinsics</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arsubsystems@4.2/api/UnityEngine.XR.ARSubsystems.XRCameraIntrinsics.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">XRCameraIntrinsics</a></span></span></td>
<td><div class="ctoken comment">
The camera intrinsic parameters for the depth image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-extrinsics"></span><span class="ctoken-line"><span class="ctoken class-name">extrinsics</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span></span></td>
<td><div class="ctoken comment">
The camera to world transform.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Overload 1<a href="#overload-1" class="hash-link" aria-label="Direct link to Overload 1" title="Direct link to Overload 1">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector4</a></span><span class="ctoken punctuation">\[</span><span class="ctoken punctuation">\]</span><span class="ctoken plain"> </span><span class="ctoken class-name">Generate</span><span class="ctoken punctuation">(</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Texture</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">depth</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">intrinsics</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">extrinsics</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary-1" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Generate a point cloud from a depth texture using the given intrinsics and extrinsics.

</div>

#### Remarks<a href="#remarks-1" class="hash-link" aria-label="Direct link to Remarks" title="Direct link to Remarks">​</a>

<div class="ctoken comment">

This is an allocating, blocking call.

</div>

#### Returns<a href="#returns-1" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

A collection of 3D points generated from the image.

</div>

### Parameters<a href="#parameters-1" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

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
<td><span id="external parameter-depth"></span><span class="ctoken-line"><span class="ctoken class-name">depth</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Texture</a></span></span></td>
<td><div class="ctoken comment">
The depth image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-intrinsics"></span><span class="ctoken-line"><span class="ctoken class-name">intrinsics</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arsubsystems@4.2/api/UnityEngine.XR.ARSubsystems.XRCameraIntrinsics.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">XRCameraIntrinsics</a></span></span></td>
<td><div class="ctoken comment">
The camera intrinsic parameters for the depth image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-extrinsics"></span><span class="ctoken-line"><span class="ctoken class-name">extrinsics</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span></span></td>
<td><div class="ctoken comment">
The camera to world transform.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Overload 2<a href="#overload-2" class="hash-link" aria-label="Direct link to Overload 2" title="Direct link to Overload 2">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">void</span><span class="ctoken plain"> </span><span class="ctoken class-name">Generate</span><span class="ctoken punctuation">(</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Texture</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">depth</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arsubsystems@4.2/api/UnityEngine.XR.ARSubsystems.XRCameraIntrinsics.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">XRCameraIntrinsics</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">intrinsics</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">extrinsics</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken keyword">ref</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector4</a></span><span class="ctoken punctuation">\[</span><span class="ctoken punctuation">\]</span><span class="ctoken plain"> </span><span class="ctoken class-name">result</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary-2" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Generate a point cloud from a depth texture using the given intrinsics and extrinsics.

</div>

#### Remarks<a href="#remarks-2" class="hash-link" aria-label="Direct link to Remarks" title="Direct link to Remarks">​</a>

<div class="ctoken comment">

This is a non-allocating, blocking call.

</div>

### Parameters<a href="#parameters-2" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

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
<td><span id="external parameter-depth"></span><span class="ctoken-line"><span class="ctoken class-name">depth</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Texture</a></span></span></td>
<td><div class="ctoken comment">
The depth image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-intrinsics"></span><span class="ctoken-line"><span class="ctoken class-name">intrinsics</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arsubsystems@4.2/api/UnityEngine.XR.ARSubsystems.XRCameraIntrinsics.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">XRCameraIntrinsics</a></span></span></td>
<td><div class="ctoken comment">
The camera intrinsic parameters for the depth image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-extrinsics"></span><span class="ctoken-line"><span class="ctoken class-name">extrinsics</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span></span></td>
<td><div class="ctoken comment">
The camera to world transform.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Overload 3<a href="#overload-3" class="hash-link" aria-label="Direct link to Overload 3" title="Direct link to Overload 3">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">void</span><span class="ctoken plain"> </span><span class="ctoken class-name">Generate</span><span class="ctoken punctuation">(</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Texture</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">depth</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">intrinsics</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">extrinsics</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken keyword">ref</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector4</a></span><span class="ctoken punctuation">\[</span><span class="ctoken punctuation">\]</span><span class="ctoken plain"> </span><span class="ctoken class-name">result</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary-3" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Generate a point cloud from a depth texture using the given intrinsics and extrinsics.

</div>

#### Remarks<a href="#remarks-3" class="hash-link" aria-label="Direct link to Remarks" title="Direct link to Remarks">​</a>

<div class="ctoken comment">

This is a non-allocating, blocking call.

</div>

### Parameters<a href="#parameters-3" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

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
<td><span id="external parameter-depth"></span><span class="ctoken-line"><span class="ctoken class-name">depth</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Texture</a></span></span></td>
<td><div class="ctoken comment">
The depth image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-intrinsics"></span><span class="ctoken-line"><span class="ctoken class-name">intrinsics</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arsubsystems@4.2/api/UnityEngine.XR.ARSubsystems.XRCameraIntrinsics.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">XRCameraIntrinsics</a></span></span></td>
<td><div class="ctoken comment">
The camera intrinsic parameters for the depth image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-extrinsics"></span><span class="ctoken-line"><span class="ctoken class-name">extrinsics</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span></span></td>
<td><div class="ctoken comment">
The camera to world transform.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
