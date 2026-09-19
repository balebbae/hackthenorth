---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/UserInfo/
title: UserInfo
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `UserInfo`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct UserInfo: CustomStringConvertible
```

</div>

</div>

Represents user information from the Sites Manager service.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `id`<a href="#id" class="hash-link" aria-label="Direct link to id" title="Direct link to id">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let id: String
```

</div>

</div>

User identifier.

### `firstName`<a href="#firstname" class="hash-link" aria-label="Direct link to firstname" title="Direct link to firstname">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let firstName: String
```

</div>

</div>

User's first name.

### `lastName`<a href="#lastname" class="hash-link" aria-label="Direct link to lastname" title="Direct link to lastname">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let lastName: String
```

</div>

</div>

User's last name.

### `email`<a href="#email" class="hash-link" aria-label="Direct link to email" title="Direct link to email">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let email: String
```

</div>

</div>

User's email address.

### `status`<a href="#status" class="hash-link" aria-label="Direct link to status" title="Direct link to status">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let status: String
```

</div>

</div>

User status.

### `createdTimestamp`<a href="#createdtimestamp" class="hash-link" aria-label="Direct link to createdtimestamp" title="Direct link to createdtimestamp">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let createdTimestamp: Int64
```

</div>

</div>

Timestamp when the user was created (Unix timestamp in seconds).

### `organizationId`<a href="#organizationid" class="hash-link" aria-label="Direct link to organizationid" title="Direct link to organizationid">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let organizationId: String?
```

</div>

</div>

Organization identifier (nil if user doesn't belong to an organization).

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
public init?(fromC cValue: ARDK_SitesManager_UserInfo)
```

</div>

</div>

</div>

</div>
