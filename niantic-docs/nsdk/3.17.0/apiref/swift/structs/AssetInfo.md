---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/AssetInfo/
title: AssetInfo
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `AssetInfo`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct AssetInfo: CustomStringConvertible
```

</div>

</div>

Represents asset information from the Sites Manager service.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `id`<a href="#id" class="hash-link" aria-label="Direct link to id" title="Direct link to id">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let id: String
```

</div>

</div>

Asset identifier.

### `name`<a href="#name" class="hash-link" aria-label="Direct link to name" title="Direct link to name">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let name: String
```

</div>

</div>

Asset name.

### `type`<a href="#type" class="hash-link" aria-label="Direct link to type" title="Direct link to type">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let type: String
```

</div>

</div>

Asset type.

### `siteId`<a href="#siteid" class="hash-link" aria-label="Direct link to siteid" title="Direct link to siteid">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let siteId: String
```

</div>

</div>

Site identifier that owns this asset.

### `pipelineJobId`<a href="#pipelinejobid" class="hash-link" aria-label="Direct link to pipelinejobid" title="Direct link to pipelinejobid">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let pipelineJobId: String?
```

</div>

</div>

Pipeline job identifier (nil if not present).

### `pipelineStatus`<a href="#pipelinestatus" class="hash-link" aria-label="Direct link to pipelinestatus" title="Direct link to pipelinestatus">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let pipelineStatus: String?
```

</div>

</div>

Pipeline job status (nil if not present).

### `vpsAnchorPayload`<a href="#vpsanchorpayload" class="hash-link" aria-label="Direct link to vpsanchorpayload" title="Direct link to vpsanchorpayload">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let vpsAnchorPayload: String?
```

</div>

</div>

VPS anchor payload (nil if not present).

### `meshRootNodeId`<a href="#meshrootnodeid" class="hash-link" aria-label="Direct link to meshrootnodeid" title="Direct link to meshrootnodeid">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let meshRootNodeId: String?
```

</div>

</div>

Mesh root node ID (nil if not present).

### `sourceScanIds`<a href="#sourcescanids" class="hash-link" aria-label="Direct link to sourcescanids" title="Direct link to sourcescanids">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let sourceScanIds: [String]
```

</div>

</div>

Source scan IDs (empty array if none).

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
public init?(fromC cValue: ARDK_SitesManager_AssetInfo)
```

</div>

</div>

</div>

</div>
