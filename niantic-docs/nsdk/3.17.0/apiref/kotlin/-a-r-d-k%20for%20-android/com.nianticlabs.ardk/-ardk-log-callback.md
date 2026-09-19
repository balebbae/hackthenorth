---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-log-callback/
title: index
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[ArdkLogCallback](https://www.nianticspatial.com/docs/nsdk/3.17.0/)

<div>

# ArdkLogCallback

</div>

fun interface [ArdkLogCallback](https://www.nianticspatial.com/docs/nsdk/3.17.0/)

Functional interface for receiving log messages from ARDK.

This callback is invoked by the native ARDK library to send log messages to the Kotlin/Java layer. The callback receives the log level, message, and optional source location information.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|          |                                                                |
|----------|----------------------------------------------------------------|
| level    | The log level (0=All, 1=Debug, 2=Info, 3=Warn, 4=Error, 5=Off) |
| message  | The log message                                                |
| fileName | Optional source file name where the log was triggered          |
| fileLine | Optional line number in the source file                        |
| funcName | Optional function name where the log was triggered             |

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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-log-callback/on-log/">onLog</a></td>
<td>[androidJvm]<br />
abstract fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-log-callback/on-log/">onLog</a>(level: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a>, message: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>, fileName: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>?, fileLine: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a>, funcName: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>?)</td>
</tr>
</tbody>
</table>

</div>

</div>
