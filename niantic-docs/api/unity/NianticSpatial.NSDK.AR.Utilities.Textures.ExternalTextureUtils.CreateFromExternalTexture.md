---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Textures.ExternalTextureUtils.CreateFromExternalTexture/
title: CreateFromExternalTexture
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Utilities.Textures](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Textures/ "NianticSpatial.NSDK.AR.Utilities.Textures") <span class="api-breadcrumbs-nav">←</span>[ExternalTextureUtils](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Textures.ExternalTextureUtils/ "NianticSpatial.NSDK.AR.Utilities.Textures.ExternalTextureUtils") 

</div>

<div class="api-title">

#  CreateFromExternalTexture

<div class="api-package">

Creates a new Texture2D object from the provided external texture.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Texture2D</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">CreateFromExternalTexture</span><span class="ctoken punctuation">(</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Texture2D</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">externalTexture</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nullable</a></span><span class="ctoken punctuation">\<</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TextureFormat</a></span><span class="ctoken punctuation">\></span><span class="ctoken plain"> </span><span class="ctoken class-name">outputFormat</span><span class="ctoken plain"> </span><span class="ctoken punctuation">=</span><span class="ctoken plain"> </span><span class="ctoken plain">null</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Creates a new Texture2D object from the provided external texture.

</div>

#### Remarks<a href="#remarks" class="hash-link" aria-label="Direct link to Remarks" title="Direct link to Remarks">​</a>

<div class="ctoken comment">

Avoid using in production code, since this function involves a CPU readback and is slow.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The Texture2D object created from the external texture.

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
<td><span id="external parameter-externaltexture"></span><span class="ctoken-line"><span class="ctoken class-name">externalTexture</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Texture2D</a></span></span></td>
<td><div class="ctoken comment">
The source external/native texture to copy from.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-outputformat"></span><span class="ctoken-line"><span class="ctoken class-name">outputFormat</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nullable</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TextureFormat</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Optional. The desired output texture format. If null, the format of the external texture will be used.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
