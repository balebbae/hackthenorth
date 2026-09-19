---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/ImageMath/
title: ImageMath
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `ImageMath`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct ImageMath
```

</div>

</div>

Provides affine transformation utilities for image processing.

All affine matrices returned by this class operate in **normalized coordinates**, where image space is mapped to the \[0, 1\] range in both axes with origin at top-left.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `reprojection(aspect:fovRadians:zNear:zFar:referenceView:targetView:backProjectionDistance:)`<a href="#reprojectionaspectfovradiansznearzfarreferenceviewtargetviewbackprojectiondistance" class="hash-link" aria-label="Direct link to reprojectionaspectfovradiansznearzfarreferenceviewtargetviewbackprojectiondistance" title="Direct link to reprojectionaspectfovradiansznearzfarreferenceviewtargetviewbackprojectiondistance">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static func reprojection(aspect: Float, fovRadians: Float, zNear: Float, zFar: Float,
                                referenceView: matrix_float4x4, targetView: matrix_float4x4, backProjectionDistance: Float = 0.9
) -> matrix_float3x3
```

</div>

</div>

Returns a 3×3 homography matrix as `matrix_float3x3` that reprojects image coordinates from a reference camera view into a target camera view. The image coordinates are expected to be normalized \[0..1\].

- Parameters:
  - aspect: The aspect ratio of the image (width / height).
  - fovRadians: The vertical field of view in radians.
  - zNear: Near clipping plane distance.
  - zFar: Far clipping plane distance.
  - referenceView: The reference camera view.
  - targetView: The target camera view.
  - backProjectionDistance: Depth at which to reproject, normalized between clipping planes near (0) and far (1). Recommended: 0.9.
- Returns: A 3×3 homography matrix in column-major order.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| aspect | The aspect ratio of the image (width / height). |
| fovRadians | The vertical field of view in radians. |
| zNear | Near clipping plane distance. |
| zFar | Far clipping plane distance. |
| referenceView | The reference camera view. |
| targetView | The target camera view. |
| backProjectionDistance | Depth at which to reproject, normalized between clipping planes near (0) and far (1). Recommended: 0.9. |

### `displayTransform(for:viewportSize:imageSize:)`<a href="#displaytransformforviewportsizeimagesize" class="hash-link" aria-label="Direct link to displaytransformforviewportsizeimagesize" title="Direct link to displaytransformforviewportsizeimagesize">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static func displayTransform(for orientation: UIInterfaceOrientation,
                                    viewportSize: CGSize,
                                    imageSize: CGSize) -> CGAffineTransform
```

</div>

</div>

Returns an affine transform that maps normalized image coordinates into a coordinate space suitable for rendering the camera image in the given viewport and orientation.

This method replicates ARKit’s `displayTransform(for:viewportSize:)` by computing a transform that accounts for the camera image’s aspect ratio, the device’s interface orientation, and the desired viewport size.

- Parameters:
  - orientation: The current interface orientation of the device’s UI.
  - viewportSize: The size of the viewport in which the image will be rendered.
  - imageSize: The dimensions of the camera image.
- Returns: A `CGAffineTransform` that converts normalized image coordinates (with origin at top-left, ranging from 0.0 to 1.0) into the coordinate space of the viewport, accounting for orientation and aspect ratio.

#### Parameters<a href="#parameters-1" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| orientation | The current interface orientation of the device’s UI. |
| viewportSize | The size of the viewport in which the image will be rendered. |
| imageSize | The dimensions of the camera image. |

### `viewRotation(fromOrientation:toOrientation:)`<a href="#viewrotationfromorientationtoorientation" class="hash-link" aria-label="Direct link to viewrotationfromorientationtoorientation" title="Direct link to viewrotationfromorientationtoorientation">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static func viewRotation(fromOrientation: UIInterfaceOrientation, toOrientation: UIInterfaceOrientation) -> CGAffineTransform
```

</div>

</div>

Returns an affine transform that rotates between two interface orientations around the center.

This method models UI rotation (opposite to physical device rotation). For example, rotating from `.landscapeRight` to `.portrait` results in a counter-clockwise transform.

- Parameters:
  - fromOrientation: The starting interface orientation.
  - toOrientation: The target interface orientation.
- Returns: A `CGAffineTransform` representing the rotation.

#### Parameters<a href="#parameters-2" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name            | Description                         |
|-----------------|-------------------------------------|
| fromOrientation | The starting interface orientation. |
| toOrientation   | The target interface orientation.   |

### `deviceRotation(fromOrientation:toOrientation:)`<a href="#devicerotationfromorientationtoorientation" class="hash-link" aria-label="Direct link to devicerotationfromorientationtoorientation" title="Direct link to devicerotationfromorientationtoorientation">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static func deviceRotation(fromOrientation: UIInterfaceOrientation, toOrientation: UIInterfaceOrientation) -> CGAffineTransform
```

</div>

</div>

Returns an affine transform that rotates between two interface orientations around the center.

This method models physical device rotation. For example, rotating from `.landscapeRight` to `.portrait` results in a clockwise transform.

- Parameters:
  - fromOrientation: The starting interface orientation.
  - toOrientation: The target interface orientation.
- Returns: A `CGAffineTransform` representing the rotation.

#### Parameters<a href="#parameters-3" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name            | Description                         |
|-----------------|-------------------------------------|
| fromOrientation | The starting interface orientation. |
| toOrientation   | The target interface orientation.   |

### `affineCrop(source:target:)`<a href="#affinecropsourcetarget" class="hash-link" aria-label="Direct link to affinecropsourcetarget" title="Direct link to affinecropsourcetarget">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static func affineCrop(source: CGSize, target: CGSize) -> CGAffineTransform
```

</div>

</div>

Returns an affine transformation that crops the source size to match the aspect ratio of the target size.

- Parameters:
  - source: The size of the source container.
  - target: The size of the target container.
- Returns: An affine transformation matrix that crops the source to fit the target aspect ratio.

#### Parameters<a href="#parameters-4" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name   | Description                       |
|--------|-----------------------------------|
| source | The size of the source container. |
| target | The size of the target container. |

### `affineFit(source:sourceOrientation:target:targetOrientation:)`<a href="#affinefitsourcesourceorientationtargettargetorientation" class="hash-link" aria-label="Direct link to affinefitsourcesourceorientationtargettargetorientation" title="Direct link to affinefitsourcesourceorientationtargettargetorientation">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static func affineFit(source: CGSize, sourceOrientation: UIInterfaceOrientation,
                             target: CGSize, targetOrientation: UIInterfaceOrientation) -> CGAffineTransform
```

</div>

</div>

Returns an affine transformation that maps normalized coordinates in the source frame to normalized coordinates in the target frame.

- Note: In portrait, this function aligns the top and bottom edges to the target.

- Parameters:

  - source: The size of the source container.
  - sourceOrientation: The orientation of the source container.
  - target: The size of the target container.
  - targetOrientation: The orientation of the target container.

- Returns: An affine transformation matrix that fits the source into the target.

#### Parameters<a href="#parameters-5" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name              | Description                              |
|-------------------|------------------------------------------|
| source            | The size of the source container.        |
| sourceOrientation | The orientation of the source container. |
| target            | The size of the target container.        |
| targetOrientation | The orientation of the target container. |

### `affineRotation(radians:)`<a href="#affinerotationradians" class="hash-link" aria-label="Direct link to affinerotationradians" title="Direct link to affinerotationradians">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static func affineRotation(radians: Float) -> CGAffineTransform
```

</div>

</div>

Returns an (u, v) -\> (u', v') transformation that represents a 2D affine rotation.

### `affineTranslation(tx:ty:)`<a href="#affinetranslationtxty" class="hash-link" aria-label="Direct link to affinetranslationtxty" title="Direct link to affinetranslationtxty">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static func affineTranslation(tx: Float, ty: Float) -> CGAffineTransform
```

</div>

</div>

Returns an (u, v) -\> (u', v') transformation that represents a 2D affine translation.

### `affineScaling(sx:sy:)`<a href="#affinescalingsxsy" class="hash-link" aria-label="Direct link to affinescalingsxsy" title="Direct link to affinescalingsxsy">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static func affineScaling(sx: Float, sy: Float) -> CGAffineTransform
```

</div>

</div>

Returns an (u, v) -\> (u', v') transformation that represents a 2D affine scaling.

### `affineInvertHorizontal()`<a href="#affineinverthorizontal" class="hash-link" aria-label="Direct link to affineinverthorizontal" title="Direct link to affineinverthorizontal">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static func affineInvertHorizontal() -> CGAffineTransform
```

</div>

</div>

Returns an (u, v) -\> (u', v') transformation that represents a horizontal mirroring, i.e. (u, v) -\> (1 - u, v).

### `affineInvertVertical()`<a href="#affineinvertvertical" class="hash-link" aria-label="Direct link to affineinvertvertical" title="Direct link to affineinvertvertical">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static func affineInvertVertical() -> CGAffineTransform
```

</div>

</div>

Returns an (u, v) -\> (u', v') transformation that represents a vertical mirroring, i.e. (u, v) -\> (u, 1 - v).

</div>

</div>
