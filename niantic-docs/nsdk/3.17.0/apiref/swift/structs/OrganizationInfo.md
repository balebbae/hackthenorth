---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/OrganizationInfo/
title: OrganizationInfo
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `OrganizationInfo`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct OrganizationInfo: CustomStringConvertible
```

</div>

</div>

Represents organization information from the Sites Manager service.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `id`<a href="#id" class="hash-link" aria-label="Direct link to id" title="Direct link to id">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let id: String
```

</div>

</div>

Organization identifier.

### `name`<a href="#name" class="hash-link" aria-label="Direct link to name" title="Direct link to name">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let name: String
```

</div>

</div>

Organization name.

### `status`<a href="#status" class="hash-link" aria-label="Direct link to status" title="Direct link to status">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let status: String
```

</div>

</div>

Organization status.

### `createdTimestamp`<a href="#createdtimestamp" class="hash-link" aria-label="Direct link to createdtimestamp" title="Direct link to createdtimestamp">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let createdTimestamp: Int64
```

</div>

</div>

Timestamp when the organization was created (Unix timestamp in seconds).

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
public init?(fromC cValue: ARDK_SitesManager_OrganizationInfo)
```

</div>

</div>

</div>

</div>
