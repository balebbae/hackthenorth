---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.class-VoxelBuffer/
title: VoxelBuffer
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") 

</div>

<div class="api-title">

#  VoxelBuffer

<div class="api-package">

A read-only container for the voxel buffer information generated during scanning.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">VoxelBuffer</span></span>

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
<td><span id="property-colors"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">colors</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/unsafemutablebufferpointer" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UnsafeMutableBufferPointer</a></span><span class="ctoken plain">&lt;</span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/uint8" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UInt8</a></span><span class="ctoken plain">&gt;</span></span></td>
<td><div class="ctoken comment">
The colors of the voxels.<br />
Array of 4 bytes per voxel.<br />
- Attention: These pointers are valid as long as this class does not go out of scope.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-normals"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">normals</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/unsafemutablebufferpointer" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UnsafeMutableBufferPointer</a></span><span class="ctoken plain">&lt;</span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken plain">&gt;</span></span></td>
<td><div class="ctoken comment">
The normals of the voxels.<br />
Array of 3 floats per voxel.<br />
- Attention: These pointers are valid as long as this class does not go out of scope.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-positions"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">positions</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/unsafemutablebufferpointer" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UnsafeMutableBufferPointer</a></span><span class="ctoken plain">&lt;</span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken plain">&gt;</span></span></td>
<td><div class="ctoken comment">
The positions of the voxels.<br />
Array of 3 floats per voxel.<br />
- Attention: These pointers are valid as long as this class does not go out of scope.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-voxelsize"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">voxelSize</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
The size of the voxels.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
