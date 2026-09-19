---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/ArdkSemanticsSession.Configuration/
title: ArdkSemanticsSession.Configuration
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `ArdkSemanticsSession.Configuration`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
struct Configuration
```

</div>

</div>

Configuration structure for the semantics session.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `framerate`<a href="#framerate" class="hash-link" aria-label="Direct link to framerate" title="Direct link to framerate">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var framerate: UInt32
```

</div>

</div>

The desired frame rate for semantics processing.

### `mode`<a href="#mode" class="hash-link" aria-label="Direct link to mode" title="Direct link to mode">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var mode: SemanticsMode
```

</div>

</div>

The desired semantics mode.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `init(framerate:mode:)`<a href="#initframeratemode" class="hash-link" aria-label="Direct link to initframeratemode" title="Direct link to initframeratemode">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public init(framerate: UInt32 = 0, mode: SemanticsMode = .unspecified)
```

</div>

</div>

### `convertToC()`<a href="#converttoc" class="hash-link" aria-label="Direct link to converttoc" title="Direct link to converttoc">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func convertToC() -> ARDK_Semantics_Config
```

</div>

</div>

</div>

</div>
