---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKStatus/
title: NSDKStatus
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk/ "com.nianticspatial.nsdk") 

</div>

<div class="api-title">

#  NSDKStatus

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">enum</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">NSDKStatus</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Status codes returned by NSDK operations. NSDKStatus represents the outcome of NSDK API calls, indicating success or various types of failures. These codes help diagnose issues with NSDK integration and usage.

## See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

- NsdkStatusException

------------------------------------------------------------------------

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

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
<td><span id="property-value"></span><span class="ctoken-line"><span class="ctoken class-name keyword">value</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Cases<a href="#cases" class="hash-link" aria-label="Direct link to Cases" title="Direct link to Cases">​</a>

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
<td><span id="case-feature_already_initialized"></span><span class="ctoken-line"><span class="ctoken class-name">FEATURE_ALREADY_INITIALIZED</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">FEATURE_ALREADY_INITIALIZED</span></span></td>
<td><div class="ctoken comment">
The feature is already initialized
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-feature_not_initialized"></span><span class="ctoken-line"><span class="ctoken class-name">FEATURE_NOT_INITIALIZED</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">FEATURE_NOT_INITIALIZED</span></span></td>
<td><div class="ctoken comment">
The required feature has not been initialized
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-internal_error"></span><span class="ctoken-line api-obsolete"><span class="ctoken class-name">INTERNAL_ERROR</span></span></td>
<td><span class="ctoken-line api-obsolete"><span class="ctoken class-name">INTERNAL_ERROR</span></span></td>
<td><div class="ctoken comment">
DEPRECATED.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-invalid_argument"></span><span class="ctoken-line"><span class="ctoken class-name">INVALID_ARGUMENT</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">INVALID_ARGUMENT</span></span></td>
<td><div class="ctoken comment">
An argument had an invalid value
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-invalid_nsdk_handle"></span><span class="ctoken-line"><span class="ctoken class-name">INVALID_NSDK_HANDLE</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">INVALID_NSDK_HANDLE</span></span></td>
<td><div class="ctoken comment">
The provided NSDK handle is invalid or destroyed
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-invalid_operation"></span><span class="ctoken-line"><span class="ctoken class-name">INVALID_OPERATION</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">INVALID_OPERATION</span></span></td>
<td><div class="ctoken comment">
The operation is not valid in the current state
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-no_data"></span><span class="ctoken-line api-obsolete"><span class="ctoken class-name">NO_DATA</span></span></td>
<td><span class="ctoken-line api-obsolete"><span class="ctoken class-name">NO_DATA</span></span></td>
<td><div class="ctoken comment">
DEPRECATED. No data is available for the requested operation
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-null_argument"></span><span class="ctoken-line"><span class="ctoken class-name">NULL_ARGUMENT</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">NULL_ARGUMENT</span></span></td>
<td><div class="ctoken comment">
A required argument was null
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-success"></span><span class="ctoken-line"><span class="ctoken class-name">SUCCESS</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">SUCCESS</span></span></td>
<td><div class="ctoken comment">
Operation completed successfully
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
