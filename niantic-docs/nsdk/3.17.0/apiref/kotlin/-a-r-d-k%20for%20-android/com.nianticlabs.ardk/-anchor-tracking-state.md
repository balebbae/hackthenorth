---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state/
title: index
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[AnchorTrackingState](https://www.nianticspatial.com/docs/nsdk/3.17.0/)

<div>

# AnchorTrackingState

</div>

\[androidJvm\]\
enum [AnchorTrackingState](https://www.nianticspatial.com/docs/nsdk/3.17.0/) : <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-enum/index.html" target="_blank" rel="noopener noreferrer">Enum</a>\<[AnchorTrackingState](https://www.nianticspatial.com/docs/nsdk/3.17.0/)\>

Represents the current tracking state of a VPS anchor.

The tracking state indicates how well the system is able to track an anchor's position and orientation in the current environment. This information is crucial for determining the reliability of anchor pose data.

### Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Tracking states progress from not tracked to fully tracked, with limited tracking representing an intermediate state where tracking is possible but may be less reliable.

### Example<a href="#example" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
val update = vpsSession.getAnchorUpdate(anchorId)
when (update.trackingState) {
    AnchorTrackingState.NOT_TRACKED ->
        println("Anchor is not currently being tracked")
    AnchorTrackingState.LIMITED ->
        println("Anchor tracking is limited - pose may be unreliable")
    AnchorTrackingState.TRACKED ->
        println("Anchor is fully tracked - pose is reliable")
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state/-n-o-t_-t-r-a-c-k-e-d/">NOT_TRACKED</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state/-n-o-t_-t-r-a-c-k-e-d/">NOT_TRACKED</a><br />
The anchor is not currently being tracked.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state/-l-i-m-i-t-e-d/">LIMITED</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state/-l-i-m-i-t-e-d/">LIMITED</a><br />
The anchor is being tracked with limited accuracy.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state/-t-r-a-c-k-e-d/">TRACKED</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state/-t-r-a-c-k-e-d/">TRACKED</a><br />
The anchor is being tracked with full accuracy.</td>
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state/-companion/">Companion</a></td>
<td>[androidJvm]<br />
object <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state/-companion/">Companion</a></td>
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state/entries/">entries</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state/entries/">entries</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.enums/-enum-entries/index.html" target="_blank" rel="noopener noreferrer">EnumEntries</a>&lt;<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/">AnchorTrackingState</a>&gt;<br />
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state/value/">value</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state/value/">value</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a></td>
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state/value-of/">valueOf</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state/value-of/">valueOf</a>(value: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>): <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/">AnchorTrackingState</a><br />
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state/values/">values</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-anchor-tracking-state/values/">values</a>(): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-array/index.html" target="_blank" rel="noopener noreferrer">Array</a>&lt;<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/">AnchorTrackingState</a>&gt;<br />
Returns an array containing the constants of this enum type, in the order they're declared.</td>
</tr>
</tbody>
</table>

</div>

</div>
