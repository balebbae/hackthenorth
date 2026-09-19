---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/extensions/CGRect/
title: CGRect
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**EXTENSION**

<div>

# `CGRect`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
extension CGRect
```

</div>

</div>

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `applyingAffineTransform(containerSize:viewSize:transform:)`<a href="#applyingaffinetransformcontainersizeviewsizetransform" class="hash-link" aria-label="Direct link to applyingaffinetransformcontainersizeviewsizetransform" title="Direct link to applyingaffinetransformcontainersizeviewsizetransform">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func applyingAffineTransform(containerSize: CGSize, viewSize: CGSize, transform: CGAffineTransform) -> CGRect
```

</div>

</div>

Transforms a rectangle from the container coordinate space to view by applying a given affine transform to its corner points.

- Parameters:
  - containerSize: The size of the original container coordinate space.
  - viewSize: The size of the target view coordinate space.
  - transform: The affine transform to apply (expected to operate on normalized coordinates).
- Returns: A new rectangle transformed into the view coordinate space.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| containerSize | The size of the original container coordinate space. |
| viewSize | The size of the target view coordinate space. |
| transform | The affine transform to apply (expected to operate on normalized coordinates). |

### `applyingReprojection(containerSize:transform:)`<a href="#applyingreprojectioncontainersizetransform" class="hash-link" aria-label="Direct link to applyingreprojectioncontainersizetransform" title="Direct link to applyingreprojectioncontainersizetransform">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func applyingReprojection(containerSize: CGSize, transform: simd_float3x3) -> CGRect
```

</div>

</div>

Applies a 3x3 homography (reprojection) to this rectangle and returns the resulting bounding box in a specified container coordinate space.

- Parameters:
  - containerSize: The size of the container coordinate space. Coordinates are assumed to be relative to this space (e.g., image or view size) when applying the homography.
  - transform: The 3x3 homography matrix that maps points from the source coordinate space to the target coordinate space.
- Returns: A new CGRect representing the transformed rectangle.

#### Parameters<a href="#parameters-1" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| containerSize | The size of the container coordinate space. Coordinates are assumed to be relative to this space (e.g., image or view size) when applying the homography. |
| transform | The 3x3 homography matrix that maps points from the source coordinate space to the target coordinate space. |

</div>

</div>
