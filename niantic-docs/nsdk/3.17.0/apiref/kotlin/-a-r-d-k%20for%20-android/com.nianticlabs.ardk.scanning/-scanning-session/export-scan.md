---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.scanning/-scanning-session/export-scan/
title: export-scan
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk.scanning](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.scanning/)/[ScanningSession](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[exportScan](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.scanning/-scanning-session/export-scan/)

<div>

# exportScan

</div>

\[androidJvm\]\
fun [exportScan](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.scanning/-scanning-session/export-scan/)(jsonMetadata: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>?, exportAsVideo: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html" target="_blank" rel="noopener noreferrer">Boolean</a> = true): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html" target="_blank" rel="noopener noreferrer">String</a>?

Exports the scan data as an archive file.

This method processes the saved scan data and exports it to a standard archive format that can be used with external 3D processing tools or Niantic's VPS map.

Note: This function is blocking and may take a while to execute. See RecordingExporter for a non-blocking option.

#### Return<a href="#return" class="hash-link" aria-label="Direct link to Return" title="Direct link to Return">​</a>

The path of the archive file, if the export was successful, nil if otherwise. Export failure indicates something was wrong with the saved scan.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|  |  |
|----|----|
| jsonMetadata | Optional JSON object string to be included in the as metadata. |
| exportAsVideo | If true, the RGB frames in the scan will be exported as an .mp4 video. If false, they will be individual image files. |

#### See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

|                                    |
|------------------------------------|
| ScanningSession.saveCurrentScan    |
| ScanningSession.getCurrentSaveInfo |

</div>

</div>
