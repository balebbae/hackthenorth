---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationManager.GetChannelNamesAt/
title: GetChannelNamesAt
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.SceneSegmentation](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation/ "NianticSpatial.NSDK.AR.SceneSegmentation") <span class="api-breadcrumbs-nav">←</span>[ARSceneSegmentationManager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationManager/ "NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationManager") 

</div>

<div class="api-title">

#  GetChannelNamesAt

<div class="api-package">

Returns an array of channel names that are present for the specified pixel onscreen (for display purposes).

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">List</a></span><span class="ctoken punctuation">\<</span><span class="ctoken class-name keyword">string</span><span class="ctoken punctuation">\></span><span class="ctoken plain"> </span><span class="ctoken class-name">GetChannelNamesAt</span><span class="ctoken punctuation">(</span><span class="ctoken class-name keyword">int</span><span class="ctoken plain"> </span><span class="ctoken class-name">viewportX</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">int</span><span class="ctoken plain"> </span><span class="ctoken class-name">viewportY</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nullable</a></span><span class="ctoken punctuation">\<</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arsubsystems@4.2/api/UnityEngine.XR.ARSubsystems.XRCameraParams.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">XRCameraParams</a></span><span class="ctoken punctuation">\></span><span class="ctoken plain"> </span><span class="ctoken class-name">cameraParams</span><span class="ctoken plain"> </span><span class="ctoken punctuation">=</span><span class="ctoken plain"> </span><span class="ctoken plain">null</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Returns an array of channel names that are present for the specified pixel onscreen (for display purposes).

</div>

#### Remarks<a href="#remarks" class="hash-link" aria-label="Direct link to Remarks" title="Direct link to Remarks">​</a>

<div class="ctoken comment">

This query allocates garbage.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

An array of channel names present for the pixel.

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
<td><span id="external parameter-viewportx"></span><span class="ctoken-line"><span class="ctoken class-name">viewportX</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
Horizontal coordinate in viewport space.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-viewporty"></span><span class="ctoken-line"><span class="ctoken class-name">viewportY</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
Vertical coordinate in viewport space.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-cameraparams"></span><span class="ctoken-line"><span class="ctoken class-name">cameraParams</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nullable</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arsubsystems@4.2/api/UnityEngine.XR.ARSubsystems.XRCameraParams.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">XRCameraParams</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Params of the viewport to sample with. Defaults to current screen dimensions if null.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
