---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.GameViewUtils.GetEditorScreenOrientation/
title: GetEditorScreenOrientation
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Utilities](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities/ "NianticSpatial.NSDK.AR.Utilities") <span class="api-breadcrumbs-nav">←</span>[GameViewUtils](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.GameViewUtils/ "NianticSpatial.NSDK.AR.Utilities.GameViewUtils") 

</div>

<div class="api-title">

#  GetEditorScreenOrientation

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScreenOrientation.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ScreenOrientation</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">GetEditorScreenOrientation</span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Calculates the screen orientation via the game view aspect ratio. Use this method instead of\
UnityEngine.Screen.orientation in Editor, as the latter only returns Portrait in Editor.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The screen orientation. When this method is called in a platform other than the Unity Editor,\
it defaults to return ScreenOrientation.Portrait.

</div>

------------------------------------------------------------------------

</div>

</div>
