---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/
title: index
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[ARDKStatus](https://www.nianticspatial.com/docs/nsdk/3.17.0/)

<div>

# ARDKStatus

</div>

enum [ARDKStatus](https://www.nianticspatial.com/docs/nsdk/3.17.0/) : <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-enum/index.html" target="_blank" rel="noopener noreferrer">Enum</a>\<[ARDKStatus](https://www.nianticspatial.com/docs/nsdk/3.17.0/)\>

Status codes returned by ARDK operations.

ARDKStatus represents the outcome of ARDK API calls, indicating success or various types of failures. These codes help diagnose issues with ARDK integration and usage.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|       |                                                 |
|-------|-------------------------------------------------|
| value | The underlying integer value of the status code |

#### See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

|  |
|----|
| [ArdkStatusException](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-status-exception/) |

## Entries<a href="#entries" class="hash-link" aria-label="Direct link to Entries" title="Direct link to Entries">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/-s-u-c-c-e-s-s/">SUCCESS</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/-s-u-c-c-e-s-s/">SUCCESS</a><br />
Operation completed successfully</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/-n-u-l-l_-a-r-g-u-m-e-n-t/">NULL_ARGUMENT</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/-n-u-l-l_-a-r-g-u-m-e-n-t/">NULL_ARGUMENT</a><br />
A required argument was null</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/-i-n-v-a-l-i-d_-a-r-g-u-m-e-n-t/">INVALID_ARGUMENT</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/-i-n-v-a-l-i-d_-a-r-g-u-m-e-n-t/">INVALID_ARGUMENT</a><br />
An argument had an invalid value</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/-i-n-v-a-l-i-d_-o-p-e-r-a-t-i-o-n/">INVALID_OPERATION</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/-i-n-v-a-l-i-d_-o-p-e-r-a-t-i-o-n/">INVALID_OPERATION</a><br />
The operation is not valid in the current state</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/-i-n-v-a-l-i-d_-a-r-d-k_-h-a-n-d-l-e/">INVALID_ARDK_HANDLE</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/-i-n-v-a-l-i-d_-a-r-d-k_-h-a-n-d-l-e/">INVALID_ARDK_HANDLE</a><br />
The provided ARDK handle is invalid or destroyed</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/-f-e-a-t-u-r-e_-n-o-t_-i-n-i-t-i-a-l-i-z-e-d/">FEATURE_NOT_INITIALIZED</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/-f-e-a-t-u-r-e_-n-o-t_-i-n-i-t-i-a-l-i-z-e-d/">FEATURE_NOT_INITIALIZED</a><br />
The required feature has not been initialized</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/-f-e-a-t-u-r-e_-a-l-r-e-a-d-y_-i-n-i-t-i-a-l-i-z-e-d/">FEATURE_ALREADY_INITIALIZED</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/-f-e-a-t-u-r-e_-a-l-r-e-a-d-y_-i-n-i-t-i-a-l-i-z-e-d/">FEATURE_ALREADY_INITIALIZED</a><br />
The feature is already initialized</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/-n-o_-d-a-t-a/">NO_DATA</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/-n-o_-d-a-t-a/">NO_DATA</a><br />
DEPRECATED. No data is available for the requested operation</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/-i-n-t-e-r-n-a-l_-e-r-r-o-r/">INTERNAL_ERROR</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/-i-n-t-e-r-n-a-l_-e-r-r-o-r/">INTERNAL_ERROR</a><br />
DEPRECATED.</td>
</tr>
</tbody>
</table>

## Types<a href="#types" class="hash-link" aria-label="Direct link to Types" title="Direct link to Types">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Name</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/-companion/">Companion</a></td>
<td>[androidJvm]<br />
object <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/-companion/">Companion</a></td>
</tr>
</tbody>
</table>

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Name</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/entries/">entries</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/entries/">entries</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.enums/-enum-entries/index.html" target="_blank" rel="noopener noreferrer">EnumEntries</a>&lt;<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/">ARDKStatus</a>&gt;<br />
Returns a representation of an immutable list of all enum entries, in the order they're declared.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-w-p-s-error/-u-n-k-n-o-w-n_-e-r-r-o-r/#-372974862%2FProperties%2F1173183731">name</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-w-p-s-error/-u-n-k-n-o-w-n_-e-r-r-o-r/#-372974862%2FProperties%2F1173183731">name</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a></td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-w-p-s-error/-u-n-k-n-o-w-n_-e-r-r-o-r/#-739389684%2FProperties%2F1173183731">ordinal</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-w-p-s-error/-u-n-k-n-o-w-n_-e-r-r-o-r/#-739389684%2FProperties%2F1173183731">ordinal</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a></td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/value/">value</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/value/">value</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a></td>
</tr>
</tbody>
</table>

## Functions<a href="#functions" class="hash-link" aria-label="Direct link to Functions" title="Direct link to Functions">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Name</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/value-of/">valueOf</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/value-of/">valueOf</a>(value: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>): <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/">ARDKStatus</a><br />
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/values/">values</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/values/">values</a>(): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-array/index.html" target="_blank" rel="noopener noreferrer">Array</a>&lt;<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/">ARDKStatus</a>&gt;<br />
Returns an array containing the constants of this enum type, in the order they're declared.</td>
</tr>
</tbody>
</table>

</div>

</div>
