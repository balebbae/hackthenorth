---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/enums/ArdkAsyncState/
title: ArdkAsyncState
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**ENUM**

<div>

# `ArdkAsyncState`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public enum ArdkAsyncState<Value, Error: Swift.Error>
```

</div>

</div>

Reports the state of an asynchronous ARDK operation.

## Cases<a href="#cases" class="hash-link" aria-label="Direct link to Cases" title="Direct link to Cases">​</a>

### `notReady`<a href="#notready" class="hash-link" aria-label="Direct link to notready" title="Direct link to notready">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case notReady
```

</div>

</div>

Deprecated – use `inProgress` instead.

### `inProgress(_:)`<a href="#inprogress_" class="hash-link" aria-label="Direct link to inprogress_" title="Direct link to inprogress_">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case inProgress(Value?)
```

</div>

</div>

The asynchronous operation is currently in progress. The associated value may contain a partial result if available.

### `success(_:)`<a href="#success_" class="hash-link" aria-label="Direct link to success_" title="Direct link to success_">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case success(Value)
```

</div>

</div>

The asynchronous operation has completed successfully with a result.

### `failure(_:)`<a href="#failure_" class="hash-link" aria-label="Direct link to failure_" title="Direct link to failure_">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case failure(Error)
```

</div>

</div>

The asynchronous operation has failed with an error.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `isFinished`<a href="#isfinished" class="hash-link" aria-label="Direct link to isfinished" title="Direct link to isfinished">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var isFinished: Bool
```

</div>

</div>

Indicates whether the asynchronous operation has finished

</div>

</div>
