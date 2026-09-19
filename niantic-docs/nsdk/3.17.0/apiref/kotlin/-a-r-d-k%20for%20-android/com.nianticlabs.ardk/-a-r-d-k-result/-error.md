---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-result/-error/
title: index
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[ARDKResult](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-result/)/[Error](https://www.nianticspatial.com/docs/nsdk/3.17.0/)

<div>

# Error

</div>

data class [Error](https://www.nianticspatial.com/docs/nsdk/3.17.0/)\<out [TData](https://www.nianticspatial.com/docs/nsdk/3.17.0/), out [TError](https://www.nianticspatial.com/docs/nsdk/3.17.0/) : [ErrorCodeProvider](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-error-code-provider/)\>(val code: [TError](https://www.nianticspatial.com/docs/nsdk/3.17.0/)) : [ARDKResult](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-result/)\<[TData](https://www.nianticspatial.com/docs/nsdk/3.17.0/), [TError](https://www.nianticspatial.com/docs/nsdk/3.17.0/)\>

Represents a failed outcome, where the requested data was not available.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|      |                                                  |
|------|--------------------------------------------------|
| code | The error status code indicating what went wrong |

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>Error</td>
<td>[androidJvm]<br />
constructor(code: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a>, factory: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-error-factory/">ErrorFactory</a>&lt;<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/">TError</a>&gt;)constructor(code: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/">TError</a>)</td>
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-result/-error/code/">code</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-result/-error/code/">code</a>: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/">TError</a></td>
</tr>
</tbody>
</table>

</div>

</div>
