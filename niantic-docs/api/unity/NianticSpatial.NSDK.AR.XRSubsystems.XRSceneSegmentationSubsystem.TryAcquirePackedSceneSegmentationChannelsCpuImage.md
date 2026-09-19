---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem.TryAcquirePackedSceneSegmentationChannelsCpuImage/
title: TryAcquirePackedSceneSegmentationChannelsCpuImage
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.XRSubsystems](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems/ "NianticSpatial.NSDK.AR.XRSubsystems") <span class="api-breadcrumbs-nav">←</span>[XRSceneSegmentationSubsystem](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem/ "NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem") 

</div>

<div class="api-title">

#  TryAcquirePackedSceneSegmentationChannelsCpuImage

<div class="api-package">

Acquire the latest packed semantic channels XRCpuImage.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">bool</span><span class="ctoken plain"> </span><span class="ctoken class-name">TryAcquirePackedSceneSegmentationChannelsCpuImage</span><span class="ctoken punctuation">(</span><span class="ctoken keyword">out</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arsubsystems@4.2/api/UnityEngine.XR.ARSubsystems.XRCpuImage.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">XRCpuImage</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">cpuImage</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken keyword">out</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">samplerMatrix</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nullable</a></span><span class="ctoken punctuation">\<</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arsubsystems@4.2/api/UnityEngine.XR.ARSubsystems.XRCameraParams.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">XRCameraParams</a></span><span class="ctoken punctuation">\></span><span class="ctoken plain"> </span><span class="ctoken class-name">cameraParams</span><span class="ctoken plain"> </span><span class="ctoken punctuation">=</span><span class="ctoken plain"> </span><span class="ctoken plain">null</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Acquire the latest packed semantic channels XRCpuImage.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

Returns `true` if an XRCpuImage was successfully acquired. Returns `false` otherwise.

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
<td><span id="external parameter-cpuimage"></span><span class="ctoken-line"><span class="ctoken class-name">cpuImage</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arsubsystems@4.2/api/UnityEngine.XR.ARSubsystems.XRCpuImage.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">XRCpuImage</a></span></span></td>
<td><div class="ctoken comment">
The resulting XRCpuImage. The XRCpuImage must be disposed by the caller.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-samplermatrix"></span><span class="ctoken-line"><span class="ctoken class-name">samplerMatrix</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span></span></td>
<td><div class="ctoken comment">
The matrix that transforms from normalized viewport coordinates to normalized image coordinates.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-cameraparams"></span><span class="ctoken-line"><span class="ctoken class-name">cameraParams</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nullable</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arsubsystems@4.2/api/UnityEngine.XR.ARSubsystems.XRCameraParams.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">XRCameraParams</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Describes the viewport the image is to be displayed on.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
