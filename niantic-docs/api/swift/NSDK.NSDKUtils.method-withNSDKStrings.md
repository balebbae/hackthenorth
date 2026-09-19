---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKUtils.method-withNSDKStrings/
title: withNSDKStrings
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKUtils](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKUtils/ "NSDKUtils") 

</div>

<div class="api-title">

#  withNSDKStrings

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">withNSDKStrings</span><span class="ctoken plain">\<</span><span class="ctoken plain">Result</span><span class="ctoken plain">\>(</span><span class="ctoken plain">\_</span><span class="ctoken plain"> </span><span class="ctoken plain">body</span><span class="ctoken plain">: ((</span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">?) -\> </span><span class="ctoken class-name">ARDK_String</span><span class="ctoken plain">) </span><span class="ctoken keyword">throws</span><span class="ctoken plain"> -\> </span><span class="ctoken class-name keyword">Result</span><span class="ctoken plain">) </span><span class="ctoken keyword">rethrows</span><span class="ctoken plain"> -\> </span><span class="ctoken class-name keyword">Result</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Safely manages multiple C string conversions with automatic memory cleanup.\
This function provides a convenient way to work with multiple C strings in a single scope\
while ensuring proper memory management. It automatically allocates memory for C strings\
and cleans up all allocated memory when the scope exits.\
Use this function when you need to have multiple C strings in a single scope and\
the number of nested scopes gets too messy. Otherwise, prefer Swift's built-in\
`String.withCString` for simpler cases.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The result of executing the body closure

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- Any error thrown by the body closure

#### Example<a href="#example" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
let result = NSDKUtils.withNSDKStrings { createString in
    let string1 = createString("Hello")
    let string2 = createString("World")
    let string3 = createString(nil) // Creates empty string
    // Use the NSDK strings with C API calls
    return someCFunction(string1, string2, string3)
}
// Memory is automatically cleaned up here
```

</div>

</div>

#### Memory Management<a href="#memory-management" class="hash-link" aria-label="Direct link to Memory Management" title="Direct link to Memory Management">​</a>

The function automatically:

- Allocates memory for each string using `strdup`

- Tracks all allocated pointers

- Frees all memory when the scope exits (even if an error is thrown)

- Handles nil and empty strings gracefully

  ### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

<table class="api-table">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr class="api-table-row">
<td><span id="external parameter-body"></span><span class="ctoken-line"><span class="ctoken class-name">body</span></span></td>
<td><span class="ctoken-line"><span class="ctoken plain"> ((</span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">?) -&gt; </span><span class="ctoken class-name">ARDK_String</span><span class="ctoken plain">) </span><span class="ctoken keyword">throws</span><span class="ctoken plain"> -&gt; </span><span class="ctoken class-name keyword">Result</span></span></td>
<td><div class="ctoken comment">
A closure that receives a function for creating NSDK strings
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
