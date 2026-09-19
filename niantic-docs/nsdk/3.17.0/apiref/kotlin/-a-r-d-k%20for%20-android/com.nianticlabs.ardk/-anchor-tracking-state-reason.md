---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state-reason/
title: index
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[AnchorTrackingStateReason](https://www.nianticspatial.com/docs/nsdk/3.17.0/)

<div>

# AnchorTrackingStateReason

</div>

\[androidJvm\]\
enum [AnchorTrackingStateReason](https://www.nianticspatial.com/docs/nsdk/3.17.0/) : <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-enum/index.html" target="_blank" rel="noopener noreferrer">Enum</a>\<[AnchorTrackingStateReason](https://www.nianticspatial.com/docs/nsdk/3.17.0/)\>

Provides additional context about why an anchor is in a particular tracking state.

When an anchor is not tracked or has limited tracking, this enum provides specific reasons that can help developers understand and respond to tracking issues.

### Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Tracking state reasons help diagnose why tracking may be failing or limited, enabling applications to provide appropriate user feedback or take corrective actions.

### Example<a href="#example" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
val update = vpsSession.getAnchorUpdate(anchorId)
when (update.trackingStateReason) {
    AnchorTrackingStateReason.INITIALIZING ->
        println("Anchor is still initializing - tracking will improve")
    AnchorTrackingStateReason.PERMISSION_DENIED ->
        println("Tracking failed due to permission issues")
    AnchorTrackingStateReason.FATAL_NETWORK_ERROR ->
        println("Network error preventing tracking")
    else ->
        println("Other tracking issue: ${update.trackingStateReason}")
}
```

</div>

</div>

## Entries<a href="#entries" class="hash-link" aria-label="Direct link to Entries" title="Direct link to Entries">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state-reason/-n-o-n-e/">NONE</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state-reason/-n-o-n-e/">NONE</a><br />
No specific reason for the current tracking state.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state-reason/-i-n-i-t-i-a-l-i-z-i-n-g/">INITIALIZING</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state-reason/-i-n-i-t-i-a-l-i-z-i-n-g/">INITIALIZING</a><br />
The anchor is currently initializing and tracking will improve.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state-reason/-r-e-m-o-v-e-d/">REMOVED</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state-reason/-r-e-m-o-v-e-d/">REMOVED</a><br />
The anchor has been explicitly removed from tracking.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state-reason/-i-n-t-e-r-n-a-l_-e-r-r-o-r/">INTERNAL_ERROR</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state-reason/-i-n-t-e-r-n-a-l_-e-r-r-o-r/">INTERNAL_ERROR</a><br />
An internal error occurred within the tracking system.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state-reason/-p-e-r-m-i-s-s-i-o-n_-d-e-n-i-e-d/">PERMISSION_DENIED</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state-reason/-p-e-r-m-i-s-s-i-o-n_-d-e-n-i-e-d/">PERMISSION_DENIED</a><br />
Tracking failed due to insufficient permissions.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state-reason/-f-a-t-a-l_-n-e-t-w-o-r-k_-e-r-r-o-r/">FATAL_NETWORK_ERROR</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state-reason/-f-a-t-a-l_-n-e-t-w-o-r-k_-e-r-r-o-r/">FATAL_NETWORK_ERROR</a><br />
A fatal network error prevented tracking.</td>
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state-reason/-companion/">Companion</a></td>
<td>[androidJvm]<br />
object <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state-reason/-companion/">Companion</a></td>
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state-reason/entries/">entries</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state-reason/entries/">entries</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.enums/-enum-entries/index.html" target="_blank" rel="noopener noreferrer">EnumEntries</a>&lt;<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/">AnchorTrackingStateReason</a>&gt;<br />
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state-reason/value/">value</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state-reason/value/">value</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a></td>
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state-reason/value-of/">valueOf</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state-reason/value-of/">valueOf</a>(value: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>): <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/">AnchorTrackingStateReason</a><br />
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state-reason/values/">values</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state-reason/values/">values</a>(): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-array/index.html" target="_blank" rel="noopener noreferrer">Array</a>&lt;<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/">AnchorTrackingStateReason</a>&gt;<br />
Returns an array containing the constants of this enum type, in the order they're declared.</td>
</tr>
</tbody>
</table>

</div>

</div>
