---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/base-path/
title: base-path
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[ScannerConfig](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[basePath](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/base-path/)

<div>

# basePath

</div>

\[androidJvm\]\
var [basePath](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/base-path/): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>?

Optional field to set a base path for writing scan data.

If an absolute path (starting with '/', '', or a drive name) is provided, the directory must be writeable by the application. All other paths will be interpreted as relative to the public application path configured when the NSDK object was created. If left `null`, NSDK uses the public application path which was configured when creating the NSDK object.

**Default:**`null`

</div>

</div>
