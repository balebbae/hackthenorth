---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/enums/ArdkError/
title: ArdkError
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**ENUM**

<div>

# `ArdkError`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public enum ArdkError: Error, Equatable
```

</div>

</div>

Errors thrown by the ARDK API.

`ArdkError` a subset of all the `ARDK_Status`codes returned by the C API, containing just those that can occur in the Swift environment.

## Cases<a href="#cases" class="hash-link" aria-label="Direct link to Cases" title="Direct link to Cases">​</a>

### `nullArgument`<a href="#nullargument" class="hash-link" aria-label="Direct link to nullargument" title="Direct link to nullargument">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case nullArgument
```

</div>

</div>

A null argument was passed where a valid value was required.

This typically indicates an internal error, as the Swift wrapper should prevent null arguments from being passed to the C API.

### `invalidArgument`<a href="#invalidargument" class="hash-link" aria-label="Direct link to invalidargument" title="Direct link to invalidargument">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case invalidArgument
```

</div>

</div>

An invalid argument was provided to the operation.

This occurs when arguments are technically valid (non-null) but contain invalid values, such as out-of-range numbers or malformed data.

### `invalidOperation`<a href="#invalidoperation" class="hash-link" aria-label="Direct link to invalidoperation" title="Direct link to invalidoperation">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case invalidOperation
```

</div>

</div>

The requested operation cannot be performed in the current state.

For example, trying to start a feature that's already running, or attempting to get data before initialization is complete.

### `unknown(msg:)`<a href="#unknownmsg" class="hash-link" aria-label="Direct link to unknownmsg" title="Direct link to unknownmsg">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case unknown(msg: String)
```

</div>

</div>

Indicates an internal malfunction. In a working version of ARDK, an application should never see this result code.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `==(_:_:)`<a href="#__" class="hash-link" aria-label="Direct link to __" title="Direct link to __">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static func ==(lhs: ArdkError, rhs: ArdkError) -> Bool
```

</div>

</div>

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description               |
|------|---------------------------|
| lhs  | A value to compare.       |
| rhs  | Another value to compare. |

</div>

</div>
