---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.TextureUtils.method-createOrUpdateTexture/
title: createOrUpdateTexture
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[TextureUtils](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-TextureUtils/ "TextureUtils") 

</div>

<div class="api-title">

#  createOrUpdateTexture

<div class="api-package">

Creates or updates a Metal texture using a `NSDKImage`.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken plain">@discardableResult</span><span class="ctoken plain"> </span><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">createOrUpdateTexture</span><span class="ctoken plain">(</span><span class="ctoken plain">from</span><span class="ctoken plain"> </span><span class="ctoken plain">image</span><span class="ctoken plain">: </span><span class="ctoken class-name">[NSDKImage](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKImage/ "Provides a view into the data buffer of an image output by the NSDK....")</span><span class="ctoken plain">?, </span><span class="ctoken plain">texture</span><span class="ctoken plain">: </span><span class="ctoken keyword">inout</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//metal/MTLTexture" target="_blank" rel="noopener noreferrer" title="Opens an external reference">MTLTexture</a></span><span class="ctoken plain">?, </span><span class="ctoken plain">device</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//metal/MTLDevice" target="_blank" rel="noopener noreferrer" title="Opens an external reference">MTLDevice</a></span><span class="ctoken plain">) -\> </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Creates or updates a Metal texture using a `NSDKImage`.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

`true` if the texture was allocated or updated this call.

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
<td><span id="external parameter-from"></span><span class="ctoken-line"><span class="ctoken class-name">image</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKImage/" title="Provides a view into the data buffer of an image output by the NSDK....">NSDKImage</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-texture"></span><span class="ctoken-line"><span class="ctoken class-name">texture</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//metal/MTLTexture" target="_blank" rel="noopener noreferrer" title="Opens an external reference">MTLTexture</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
An existing Metal texture to update, or <code>nil</code> to create a new one.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-device"></span><span class="ctoken-line"><span class="ctoken class-name">device</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//metal/MTLDevice" target="_blank" rel="noopener noreferrer" title="Opens an external reference">MTLDevice</a></span></span></td>
<td><div class="ctoken comment">
The Metal device used to allocate textures.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
