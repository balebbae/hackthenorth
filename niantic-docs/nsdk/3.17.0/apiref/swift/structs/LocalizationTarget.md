---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/LocalizationTarget/
title: LocalizationTarget
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `LocalizationTarget`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct LocalizationTarget: CustomStringConvertible
```

</div>

</div>

Represents a real-world point of interest that is a VPS localization target.

VPS localization is more likely to succeed when a localization target is in camera view.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `identifier`<a href="#identifier" class="hash-link" aria-label="Direct link to identifier" title="Direct link to identifier">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let identifier: String
```

</div>

</div>

Unique identifier of this target

### `center`<a href="#center" class="hash-link" aria-label="Direct link to center" title="Direct link to center">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let center: LatLng
```

</div>

</div>

Geolocation coordinates of this target

### `name`<a href="#name" class="hash-link" aria-label="Direct link to name" title="Direct link to name">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let name: String
```

</div>

</div>

Name of this target

### `hintImageUrl`<a href="#hintimageurl" class="hash-link" aria-label="Direct link to hintimageurl" title="Direct link to hintimageurl">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let hintImageUrl: String?
```

</div>

</div>

URL where an image of the target is stored, if available.

This image can be a visual aid for users to help them know what to put in to camera view in order to localize.

### `defaultAnchorPayload`<a href="#defaultanchorpayload" class="hash-link" aria-label="Direct link to defaultanchorpayload" title="Direct link to defaultanchorpayload">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let defaultAnchorPayload: String
```

</div>

</div>

VPS anchor payload that can be used to localize when near this target.

### `description`<a href="#description" class="hash-link" aria-label="Direct link to description" title="Direct link to description">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var description: String
```

</div>

</div>

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `init(fromC:)`<a href="#initfromc" class="hash-link" aria-label="Direct link to initfromc" title="Direct link to initfromc">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public init?(fromC cValue: ARDK_VPSCoverage_LocalizationTarget)
```

</div>

</div>

</div>

</div>
