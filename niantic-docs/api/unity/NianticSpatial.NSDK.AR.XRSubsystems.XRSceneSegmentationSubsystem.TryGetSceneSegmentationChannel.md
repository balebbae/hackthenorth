---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem.TryGetSceneSegmentationChannel/
title: TryGetSceneSegmentationChannel
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

#  TryGetSceneSegmentationChannel

<div class="api-package">

Get the XRTextureDescriptor for the specified semantic channel.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">bool</span><span class="ctoken plain"> </span><span class="ctoken class-name">TryGetSceneSegmentationChannel</span><span class="ctoken punctuation">(</span><span class="ctoken class-name">[SceneSegmentationChannel](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.SceneSegmentation.SceneSegmentationChannel/ "Represents the different semantic segmentation channels that can be detected....")</span><span class="ctoken plain"> </span><span class="ctoken class-name">channel</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken keyword">out</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arsubsystems@4.2/api/UnityEngine.XR.ARSubsystems.XRTextureDescriptor.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">XRTextureDescriptor</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">sceneSegmentationChannelDescriptor</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken keyword">out</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">samplerMatrix</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nullable</a></span><span class="ctoken punctuation">\<</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arsubsystems@4.2/api/UnityEngine.XR.ARSubsystems.XRCameraParams.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">XRCameraParams</a></span><span class="ctoken punctuation">\></span><span class="ctoken plain"> </span><span class="ctoken class-name">cameraParams</span><span class="ctoken plain"> </span><span class="ctoken punctuation">=</span><span class="ctoken plain"> </span><span class="ctoken plain">null</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Get the XRTextureDescriptor for the specified semantic channel.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

true if the semantic channel texture descriptor is available and is returned. Otherwise,\
false.

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- `NotSupportedException` — Thrown if the implementation does not support semantics channel texture.

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
<td><span id="external parameter-channel"></span><span class="ctoken-line"><span class="ctoken class-name">channel</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.SceneSegmentation.SceneSegmentationChannel/" title="Represents the different semantic segmentation channels that can be detected....">SceneSegmentationChannel</a></span></span></td>
<td><div class="ctoken comment">
The semantics channel to acquire.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-scenesegmentationchanneldescriptor"></span><span class="ctoken-line"><span class="ctoken class-name">sceneSegmentationChannelDescriptor</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arsubsystems@4.2/api/UnityEngine.XR.ARSubsystems.XRTextureDescriptor.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">XRTextureDescriptor</a></span></span></td>
<td><div class="ctoken comment">
The resulting semantic channel texture descriptor, if available.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-samplermatrix"></span><span class="ctoken-line"><span class="ctoken class-name">samplerMatrix</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span></span></td>
<td><div class="ctoken comment">
The matrix that transforms from normalized viewport coordinates to normalized texture coordinates.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-cameraparams"></span><span class="ctoken-line"><span class="ctoken class-name">cameraParams</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nullable</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arsubsystems@4.2/api/UnityEngine.XR.ARSubsystems.XRCameraParams.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">XRCameraParams</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Describes the viewport the texture is to be displayed on.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
