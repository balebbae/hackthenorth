---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-status-exception/
title: index
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[ArdkStatusException](https://www.nianticspatial.com/docs/nsdk/3.17.0/)

<div>

# ArdkStatusException

</div>

open class [ArdkStatusException](https://www.nianticspatial.com/docs/nsdk/3.17.0/)(val status: [ARDKStatus](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/), message: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>? = null) : <a href="https://developer.android.com/reference/kotlin/java/lang/Exception.html" target="_blank" rel="noopener noreferrer">Exception</a>

Base class for all ARDK-specific exceptions originating from the native layer.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|         |                                                 |
|---------|-------------------------------------------------|
| status  | The ARDKStatus code that caused this exception. |
| message | An optional descriptive message.                |

#### Inheritors<a href="#inheritors" class="hash-link" aria-label="Direct link to Inheritors" title="Direct link to Inheritors">​</a>

|  |
|----|
| [ArdkNullArgumentStatusException](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-null-argument-status-exception/) |
| [ArdkInvalidArgumentStatusException](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-invalid-argument-status-exception/) |
| [ArdkInvalidOperationStatusException](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-invalid-operation-status-exception/) |
| [ArdkInvalidHandleStatusException](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-invalid-handle-status-exception/) |
| [ArdkFeatureNotInitializedStatusException](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-feature-not-initialized-status-exception/) |
| [ArdkFeatureAlreadyInitializedStatusException](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-feature-already-initialized-status-exception/) |

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>ArdkStatusException</td>
<td>[androidJvm]<br />
constructor(status: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/">ARDKStatus</a>, message: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>? = null)</td>
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-unknown-status-exception/#-654012527%2FProperties%2F1173183731">cause</a></td>
<td>[androidJvm]<br />
open val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-unknown-status-exception/#-654012527%2FProperties%2F1173183731">cause</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html" target="_blank" rel="noopener noreferrer">Throwable</a>?</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-unknown-status-exception/#1824300659%2FProperties%2F1173183731">message</a></td>
<td>[androidJvm]<br />
open val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-unknown-status-exception/#1824300659%2FProperties%2F1173183731">message</a>: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>?</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-status-exception/status/">status</a></td>
<td>[androidJvm]<br />
val <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-status-exception/status/">status</a>: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-status/">ARDKStatus</a></td>
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-unknown-status-exception/#282858770%2FFunctions%2F1173183731">addSuppressed</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-unknown-status-exception/#282858770%2FFunctions%2F1173183731">addSuppressed</a>(p0: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html" target="_blank" rel="noopener noreferrer">Throwable</a>)</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-unknown-status-exception/#-1102069925%2FFunctions%2F1173183731">fillInStackTrace</a></td>
<td>[androidJvm]<br />
open fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-unknown-status-exception/#-1102069925%2FFunctions%2F1173183731">fillInStackTrace</a>(): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html" target="_blank" rel="noopener noreferrer">Throwable</a></td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-unknown-status-exception/#1043865560%2FFunctions%2F1173183731">getLocalizedMessage</a></td>
<td>[androidJvm]<br />
open fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-unknown-status-exception/#1043865560%2FFunctions%2F1173183731">getLocalizedMessage</a>(): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a></td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-unknown-status-exception/#2050903719%2FFunctions%2F1173183731">getStackTrace</a></td>
<td>[androidJvm]<br />
open fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-unknown-status-exception/#2050903719%2FFunctions%2F1173183731">getStackTrace</a>(): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-array/index.html" target="_blank" rel="noopener noreferrer">Array</a>&lt;<a href="https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html" target="_blank" rel="noopener noreferrer">StackTraceElement</a>&gt;</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-unknown-status-exception/#672492560%2FFunctions%2F1173183731">getSuppressed</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-unknown-status-exception/#672492560%2FFunctions%2F1173183731">getSuppressed</a>(): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-array/index.html" target="_blank" rel="noopener noreferrer">Array</a>&lt;<a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html" target="_blank" rel="noopener noreferrer">Throwable</a>&gt;</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-unknown-status-exception/#-418225042%2FFunctions%2F1173183731">initCause</a></td>
<td>[androidJvm]<br />
open fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-unknown-status-exception/#-418225042%2FFunctions%2F1173183731">initCause</a>(p0: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html" target="_blank" rel="noopener noreferrer">Throwable</a>): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html" target="_blank" rel="noopener noreferrer">Throwable</a></td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-unknown-status-exception/#-1769529168%2FFunctions%2F1173183731">printStackTrace</a></td>
<td>[androidJvm]<br />
open fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-unknown-status-exception/#-1769529168%2FFunctions%2F1173183731">printStackTrace</a>()<br />
open fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-unknown-status-exception/#1841853697%2FFunctions%2F1173183731">printStackTrace</a>(p0: <a href="https://developer.android.com/reference/kotlin/java/io/PrintStream.html" target="_blank" rel="noopener noreferrer">PrintStream</a>)<br />
open fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-unknown-status-exception/#1175535278%2FFunctions%2F1173183731">printStackTrace</a>(p0: <a href="https://developer.android.com/reference/kotlin/java/io/PrintWriter.html" target="_blank" rel="noopener noreferrer">PrintWriter</a>)</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-unknown-status-exception/#2135801318%2FFunctions%2F1173183731">setStackTrace</a></td>
<td>[androidJvm]<br />
open fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-unknown-status-exception/#2135801318%2FFunctions%2F1173183731">setStackTrace</a>(p0: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-array/index.html" target="_blank" rel="noopener noreferrer">Array</a>&lt;<a href="https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html" target="_blank" rel="noopener noreferrer">StackTraceElement</a>&gt;)</td>
</tr>
</tbody>
</table>

</div>

</div>
