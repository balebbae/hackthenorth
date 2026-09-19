---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.Playback.ScreenOrientationFromPose.GetScreenOrientation/
title: GetScreenOrientation
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Subsystems.Playback](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.Playback/ "NianticSpatial.NSDK.AR.Subsystems.Playback") <span class="api-breadcrumbs-nav">←</span>[ScreenOrientationFromPose](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.Playback.ScreenOrientationFromPose/ "NianticSpatial.NSDK.AR.Subsystems.Playback.ScreenOrientationFromPose") 

</div>

<div class="api-title">

#  GetScreenOrientation

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScreenOrientation.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ScreenOrientation</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">GetScreenOrientation</span><span class="ctoken punctuation">(</span><span class="ctoken keyword">this</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">cameraPose</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Calculates the ScreenOrientation from a camera pose. It is assumed that LandscapeLeft is the natural camera\
orientation, so for example in identity pose. For the edge case screen facing up it will return Portrait and for\
screen facing down it will return PortraitUpsideDown.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

ScreenOrientation in Unity convention

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
<td><span id="external parameter-camerapose"></span><span class="ctoken-line"><span class="ctoken class-name">cameraPose</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span></span></td>
<td><div class="ctoken comment">
The camera pose in Unity coordinate convention
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
