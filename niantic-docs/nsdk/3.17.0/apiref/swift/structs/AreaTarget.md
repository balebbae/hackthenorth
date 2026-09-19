---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/AreaTarget/
title: AreaTarget
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `AreaTarget`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct AreaTarget: CustomStringConvertible
```

</div>

</div>

Contains a `CoverageArea` and its associated `LocalizationTarget`.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `coverageArea`<a href="#coveragearea" class="hash-link" aria-label="Direct link to coveragearea" title="Direct link to coveragearea">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let coverageArea: CoverageArea
```

</div>

</div>

The geographic area where the `localizationTarget` can be used for VPS operations.

### `localizationTarget`<a href="#localizationtarget" class="hash-link" aria-label="Direct link to localizationtarget" title="Direct link to localizationtarget">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let localizationTarget: LocalizationTarget
```

</div>

</div>

The localization target located within the `coverageArea`

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
public init?(fromC cValue: ARDK_VPSCoverage_AreaTarget)
```

</div>

</div>

</div>

</div>
