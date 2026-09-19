---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKUtils/
title: NSDKUtils
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") 

</div>

<div class="api-title">

#  NSDKUtils

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">struct</span><span class="ctoken plain"> </span><span class="ctoken class-name">NSDKUtils</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Utility functions for NSDK string management and memory handling. `NSDKUtils` provides helper methods for safely managing C string conversions and memory allocation when working with the NSDK C API.

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

The utilities in this struct help manage the complexity of converting between Swift strings and C strings while ensuring proper memory cleanup and avoiding memory leaks.

------------------------------------------------------------------------

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

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
<td><span id="method-withnsdkstrings"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKUtils.method-withNSDKStrings/" title="Safely manages multiple C string conversions with automatic memory cleanup....">withNSDKStrings</a></span><span class="ctoken plain">&lt;</span><span class="ctoken plain">Result</span><span class="ctoken plain">&gt;(</span><span class="ctoken plain">_</span><span class="ctoken plain"> </span><span class="ctoken plain">body</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">Result</span></span></td>
<td><div class="ctoken comment">
Safely manages multiple C string conversions with automatic memory cleanup.<br />
This function provides a convenient way to work with multiple C strings in a single scope<br />
while ensuring proper memory management. It automatically allocates memory for C strings<br />
and cleans up all allocated memory when the scope exits.<br />
Use this function when you need to have multiple C strings in a single scope and<br />
the number of nested scopes gets too messy. Otherwise, prefer Swift's built-in<br />
<code>String.withCString</code> for simpler cases.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
