---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/CoverageArea/
title: CoverageArea
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `CoverageArea`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct CoverageArea: CustomStringConvertible
```

</div>

</div>

Represents a geographic area where VPS localization is possible

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `shape`<a href="#shape" class="hash-link" aria-label="Direct link to shape" title="Direct link to shape">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let shape: [LatLng]
```

</div>

</div>

Points describing a polygon outline of the area.

### `centroid`<a href="#centroid" class="hash-link" aria-label="Direct link to centroid" title="Direct link to centroid">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let centroid: LatLng
```

</div>

</div>

Centroid of the polygon described in `shape`.

### `localizationTargetIdentifiers`<a href="#localizationtargetidentifiers" class="hash-link" aria-label="Direct link to localizationtargetidentifiers" title="Direct link to localizationtargetidentifiers">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let localizationTargetIdentifiers: [String]
```

</div>

</div>

Identifiers of all the localization targets within the coverage area.

### `localizability`<a href="#localizability" class="hash-link" aria-label="Direct link to localizability" title="Direct link to localizability">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let localizability: Localizability
```

</div>

</div>

Quality of VPS coverage in the area.

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
public init?(fromC cValue: ARDK_VPSCoverage_CoverageArea)
```

</div>

</div>

</div>

</div>
