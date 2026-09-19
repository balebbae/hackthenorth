---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/
title: index
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[VpsGraphOperationError](https://www.nianticspatial.com/docs/nsdk/3.17.0/)

<div>

# VpsGraphOperationError

</div>

\[androidJvm\]\
enum [VpsGraphOperationError](https://www.nianticspatial.com/docs/nsdk/3.17.0/) : <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-enum/index.html" target="_blank" rel="noopener noreferrer">Enum</a>\<[VpsGraphOperationError](https://www.nianticspatial.com/docs/nsdk/3.17.0/)\> , [ErrorCodeProvider](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-error-code-provider/)

Error codes for VPS graph operations.

These errors can occur during VPS operations that query the internal graph structure, such as converting device poses to geolocations. Each error provides specific information about why the operation failed.

## Entries<a href="#entries" class="hash-link" aria-label="Direct link to Entries" title="Direct link to Entries">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/-n-o-n-e/">NONE</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/-n-o-n-e/">NONE</a><br />
No error occurred - the operation completed successfully.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/-n-o-t_-i-n-i-t-i-a-l-i-z-e-d/">NOT_INITIALIZED</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/-n-o-t_-i-n-i-t-i-a-l-i-z-e-d/">NOT_INITIALIZED</a><br />
The VPS system has not been initialized yet.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/-n-o-t_-l-o-c-a-l-i-z-e-d/">NOT_LOCALIZED</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/-n-o-t_-l-o-c-a-l-i-z-e-d/">NOT_LOCALIZED</a><br />
The device has not successfully localized to a VPS location.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/-n-o_-t-r-a-n-s-f-o-r-m_-t-o_-t-r-a-c-k-i-n-g_-n-o-d-e/">NO_TRANSFORM_TO_TRACKING_NODE</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/-n-o_-t-r-a-n-s-f-o-r-m_-t-o_-t-r-a-c-k-i-n-g_-n-o-d-e/">NO_TRANSFORM_TO_TRACKING_NODE</a><br />
No transform path exists between the requested node and the tracking node.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/-t-a-r-g-e-t_-n-o-d-e_-n-o-t_-f-o-u-n-d/">TARGET_NODE_NOT_FOUND</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/-t-a-r-g-e-t_-n-o-d-e_-n-o-t_-f-o-u-n-d/">TARGET_NODE_NOT_FOUND</a><br />
The requested target node was not found in the VPS graph.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/-n-o_-g-e-o-r-e-f-e-r-e-n-c-e_-d-a-t-a/">NO_GEOREFERENCE_DATA</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/-n-o_-g-e-o-r-e-f-e-r-e-n-c-e_-d-a-t-a/">NO_GEOREFERENCE_DATA</a><br />
The VPS location does not have GPS georeference data.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/-u-n-k-n-o-w-n_-e-r-r-o-r/">UNKNOWN_ERROR</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/-u-n-k-n-o-w-n_-e-r-r-o-r/">UNKNOWN_ERROR</a><br />
An unknown error occurred during the operation.</td>
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/-companion/">Companion</a></td>
<td>[androidJvm]<br />
object <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/-companion/">Companion</a> : <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-error-factory/">ErrorFactory</a>&lt;<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/">VpsGraphOperationError</a>&gt;</td>
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/entries/">entries</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/entries/">entries</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.enums/-enum-entries/index.html" target="_blank" rel="noopener noreferrer">EnumEntries</a>&lt;<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/">VpsGraphOperationError</a>&gt;<br />
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/value/">value</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/value/">value</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a></td>
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/value-of/">valueOf</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/value-of/">valueOf</a>(value: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>): <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/">VpsGraphOperationError</a><br />
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/values/">values</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-vps-graph-operation-error/values/">values</a>(): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-array/index.html" target="_blank" rel="noopener noreferrer">Array</a>&lt;<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/">VpsGraphOperationError</a>&gt;<br />
Returns an array containing the constants of this enum type, in the order they're declared.</td>
</tr>
</tbody>
</table>

</div>

</div>
