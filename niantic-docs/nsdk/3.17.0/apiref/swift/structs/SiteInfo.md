---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/SiteInfo/
title: SiteInfo
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `SiteInfo`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct SiteInfo: CustomStringConvertible
```

</div>

</div>

Represents site information from the Sites Manager service.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `id`<a href="#id" class="hash-link" aria-label="Direct link to id" title="Direct link to id">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let id: String
```

</div>

</div>

Site identifier.

### `name`<a href="#name" class="hash-link" aria-label="Direct link to name" title="Direct link to name">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let name: String
```

</div>

</div>

Site name.

### `status`<a href="#status" class="hash-link" aria-label="Direct link to status" title="Direct link to status">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let status: String
```

</div>

</div>

Site status.

### `organizationId`<a href="#organizationid" class="hash-link" aria-label="Direct link to organizationid" title="Direct link to organizationid">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let organizationId: String
```

</div>

</div>

Organization identifier that owns this site.

### `latitude`<a href="#latitude" class="hash-link" aria-label="Direct link to latitude" title="Direct link to latitude">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let latitude: Double
```

</div>

</div>

Latitude coordinate (valid if hasLocation is true).

### `longitude`<a href="#longitude" class="hash-link" aria-label="Direct link to longitude" title="Direct link to longitude">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let longitude: Double
```

</div>

</div>

Longitude coordinate (valid if hasLocation is true).

### `hasLocation`<a href="#haslocation" class="hash-link" aria-label="Direct link to haslocation" title="Direct link to haslocation">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let hasLocation: Bool
```

</div>

</div>

Indicates whether latitude and longitude are valid.

### `parentSiteId`<a href="#parentsiteid" class="hash-link" aria-label="Direct link to parentsiteid" title="Direct link to parentsiteid">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let parentSiteId: String?
```

</div>

</div>

Parent site identifier (nil if no parent site).

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
public init?(fromC cValue: ARDK_SitesManager_SiteInfo)
```

</div>

</div>

</div>

</div>
