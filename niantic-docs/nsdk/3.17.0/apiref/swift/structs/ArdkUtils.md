---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/ArdkUtils/
title: ArdkUtils
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `ArdkUtils`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct ArdkUtils
```

</div>

</div>

Utility functions for ARDK string management and memory handling.

`ArdkUtils` provides helper methods for safely managing C string conversions and memory allocation when working with the ARDK C API.

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

The utilities in this struct help manage the complexity of converting between Swift strings and C strings while ensuring proper memory cleanup and avoiding memory leaks.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `withArdkStrings(_:)`<a href="#withardkstrings_" class="hash-link" aria-label="Direct link to withardkstrings_" title="Direct link to withardkstrings_">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static func withArdkStrings\<Result\>(
    _ body: ((String?) -> ARDK_String) throws -> Result
) rethrows -> Result
```

</div>

</div>

Safely manages multiple C string conversions with automatic memory cleanup.

This function provides a convenient way to work with multiple C strings in a single scope while ensuring proper memory management. It automatically allocates memory for C strings and cleans up all allocated memory when the scope exits.

Use this function when you need to have multiple C strings in a single scope and the number of nested scopes gets too messy. Otherwise, prefer Swift's built-in `String.withCString` for simpler cases.

- Parameter body: A closure that receives a function for creating ARDK strings
- Returns: The result of executing the body closure
- Throws: Any error thrown by the body closure

## Example<a href="#example" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
let result = ArdkUtils.withArdkStrings { createString in
    let string1 = createString("Hello")
    let string2 = createString("World")
    let string3 = createString(nil) // Creates empty string
    
    // Use the ARDK strings with C API calls
    return someCFunction(string1, string2, string3)
}
// Memory is automatically cleaned up here
```

</div>

</div>

## Memory Management<a href="#memory-management" class="hash-link" aria-label="Direct link to Memory Management" title="Direct link to Memory Management">​</a>

The function automatically:

- Allocates memory for each string using `strdup`
- Tracks all allocated pointers
- Frees all memory when the scope exits (even if an error is thrown)
- Handles nil and empty strings gracefully

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description                                                  |
|------|--------------------------------------------------------------|
| body | A closure that receives a function for creating ARDK strings |

</div>

</div>
