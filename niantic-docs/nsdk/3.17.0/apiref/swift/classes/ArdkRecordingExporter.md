---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/ArdkRecordingExporter/
title: ArdkRecordingExporter
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `ArdkRecordingExporter`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public final class ArdkRecordingExporter: ArdkSession.IDisposable
```

</div>

</div>

A session for exporting scan recordings to various formats.

`ArdkRecordingExporter` provides capabilities for converting saved scan data into recorderV2 format for use in Unity Playback or activating VPS.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `export(scanDirPath:scanId:userData:exportAsVideo:pollingInterval:timeout:progressCallback:)`<a href="#exportscandirpathscaniduserdataexportasvideopollingintervaltimeoutprogresscallback" class="hash-link" aria-label="Direct link to exportscandirpathscaniduserdataexportasvideopollingintervaltimeoutprogresscallback" title="Direct link to exportscandirpathscaniduserdataexportasvideopollingintervaltimeoutprogresscallback">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func export(
    scanDirPath: String,
    scanId: String,
    userData: [String: Any] = [:],
    exportAsVideo: Bool = true,
    pollingInterval: TimeInterval = 0.1,
    timeout: TimeInterval = 300.0,
    progressCallback: ((Float) -> Void)? = nil
) async throws -> String
```

</div>

</div>

Exports a scan recording asynchronously.

Starts the export process for a scan recording and suspends until the export completes successfully, fails, or times out.

- Parameters:
  - scanPath: The path to the directory containing the raw scan files to export. This is obtained from the return value of`ArdkScanningSession/saveInfo()`. The export will be written to a .tgz file inside this directory.
  - scanId: The unique identifier of the scan to export.
  - userData: Dictionary containing custom metadata to include in the export
  - exportAsVideo: If true, the RGB frames in the scan will be exported as an .mp4 video. If false, they will be individual image files.
  - pollingInterval: Time between progress checks (default: 0.5s).
  - timeout: Maximum duration to wait before failing (default: 5 minutes).
- Returns: The file path to the exported recording.
- Throws:
  - `CancellationError` if the Task running this function was cancelled.
  - `TimeoutError` if the function timed out before it could complete execution.
  - `MeshDownloaderResults.Error` if there was an error specific to the VPS Coverage query.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| scanPath | The path to the directory containing the raw scan files to export. This is obtained from the return value of`ArdkScanningSession/saveInfo()`. The export will be written to a .tgz file inside this directory. |
| scanId | The unique identifier of the scan to export. |
| userData | Dictionary containing custom metadata to include in the export |
| exportAsVideo | If true, the RGB frames in the scan will be exported as an .mp4 video. If false, they will be individual image files. |
| pollingInterval | Time between progress checks (default: 0.5s). |
| timeout | Maximum duration to wait before failing (default: 5 minutes). |

</div>

</div>
