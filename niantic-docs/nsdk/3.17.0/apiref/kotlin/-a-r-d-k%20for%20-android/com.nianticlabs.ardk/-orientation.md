---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/
title: index
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[Orientation](https://www.nianticspatial.com/docs/nsdk/3.17.0/)

<div>

# Orientation

</div>

enum [Orientation](https://www.nianticspatial.com/docs/nsdk/3.17.0/) : <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-enum/index.html" target="_blank" rel="noopener noreferrer">Enum</a>\<[Orientation](https://www.nianticspatial.com/docs/nsdk/3.17.0/)\>

Device orientation when capturing camera frames.

Orientation affects how ARDK interprets camera data and poses. Ensure the correct orientation is set in [FrameData.screenOrientation](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-frame-data/screen-orientation/) for accurate tracking and localization.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|       |                                                 |
|-------|-------------------------------------------------|
| value | The underlying integer value of the orientation |

#### See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

|  |
|----|
| [FrameData.screenOrientation](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-frame-data/screen-orientation/) |

## Entries<a href="#entries" class="hash-link" aria-label="Direct link to Entries" title="Direct link to Entries">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/-u-n-k-n-o-w-n/">UNKNOWN</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/-u-n-k-n-o-w-n/">UNKNOWN</a><br />
Orientation is unknown or not yet determined</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/-p-o-r-t-r-a-i-t/">PORTRAIT</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/-p-o-r-t-r-a-i-t/">PORTRAIT</a><br />
Device held upright in portrait mode</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/-p-o-r-t-r-a-i-t_-u-p-s-i-d-e_-d-o-w-n/">PORTRAIT_UPSIDE_DOWN</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/-p-o-r-t-r-a-i-t_-u-p-s-i-d-e_-d-o-w-n/">PORTRAIT_UPSIDE_DOWN</a><br />
Device held upside-down in portrait mode</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/-l-a-n-d-s-c-a-p-e_-r-i-g-h-t/">LANDSCAPE_RIGHT</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/-l-a-n-d-s-c-a-p-e_-r-i-g-h-t/">LANDSCAPE_RIGHT</a><br />
Device rotated 90° clockwise from portrait (landscape)</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/-l-a-n-d-s-c-a-p-e_-l-e-f-t/">LANDSCAPE_LEFT</a></td>
<td>[androidJvm]<br />
<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/-l-a-n-d-s-c-a-p-e_-l-e-f-t/">LANDSCAPE_LEFT</a><br />
Device rotated 90° counter-clockwise from portrait (landscape)</td>
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/-companion/">Companion</a></td>
<td>[androidJvm]<br />
object <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/-companion/">Companion</a></td>
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/entries/">entries</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/entries/">entries</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.enums/-enum-entries/index.html" target="_blank" rel="noopener noreferrer">EnumEntries</a>&lt;<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/">Orientation</a>&gt;<br />
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/value-of/">valueOf</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/value-of/">valueOf</a>(value: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>): <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/">Orientation</a><br />
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/values/">values</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/values/">values</a>(): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-array/index.html" target="_blank" rel="noopener noreferrer">Array</a>&lt;<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/">Orientation</a>&gt;<br />
Returns an array containing the constants of this enum type, in the order they're declared.</td>
</tr>
</tbody>
</table>

</div>

</div>
