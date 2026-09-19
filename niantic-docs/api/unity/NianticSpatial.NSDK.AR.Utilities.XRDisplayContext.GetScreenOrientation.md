---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.XRDisplayContext.GetScreenOrientation/
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

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Utilities](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities/ "NianticSpatial.NSDK.AR.Utilities") <span class="api-breadcrumbs-nav">←</span>[XRDisplayContext](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.XRDisplayContext/ "NianticSpatial.NSDK.AR.Utilities.XRDisplayContext") 

</div>

<div class="api-title">

#  GetScreenOrientation

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScreenOrientation.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ScreenOrientation</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">GetScreenOrientation</span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

For NSDK, it is important to know the screen orientation in order to know how to rotate the camera\
input image received from the XRCameraSubsystem. The UnityEngine.Screen.orientation property only returns\
ScreenOrientation.Portrait when called in Editor, presumably because there is no rotation offset\
between the camera image and the displayed screen image in Editor. Thus, use this method to get the\
screen orientation value expected by NSDK's APIs, regardless of the active platform.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The corrected screen orientation. When running XR in NSDK's Playback mode, the\
returned value will match the screen orientation recorded in the dataset's current frame. Else, will\
return the UnityEngine.Screen.orientation value.

</div>

------------------------------------------------------------------------

</div>

</div>
