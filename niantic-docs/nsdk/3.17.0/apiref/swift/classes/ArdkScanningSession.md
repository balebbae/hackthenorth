---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/ArdkScanningSession/
title: ArdkScanningSession
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `ArdkScanningSession`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public final class ArdkScanningSession: ArdkSession.IDisposable, ArdkFeatureSession
```

</div>

</div>

A session for 3D scanning and visualization functionality.

The scanning feature provides capabilities for capturing, processing, and exporting 3D scan data from AR sessions. Scans of a location can be processed by the Visual Positioning System's (VPS's) cloud services to enable VPS localization.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `featureStatus()`<a href="#featurestatus" class="hash-link" aria-label="Direct link to featurestatus" title="Direct link to featurestatus">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func featureStatus() -> ArdkFeatureStatus
```

</div>

</div>

Reports errors that have occurred within processes running inside this feature.

Check this periodically to see if any errors have occurred with processes running inside this feature. Once an error has been flagged, it will remain flagged until the culprit process has been run again and completed successfully.

- Returns: Feature status flags for any issues that have occurred

### `configure(with:)`<a href="#configurewith" class="hash-link" aria-label="Direct link to configurewith" title="Direct link to configurewith">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func configure(with config: Configuration) throws
```

</div>

</div>

Configures the session with the specified settings.

- Attention: This method must be called while the session is stopped, or else configuration will fail. In that case, while this function returns without throwing, configuration will still fail asynchronously. Use `featureStatus()` to check that configuration has not failed.
- Parameter config: An object that defines this session's behavior. Only settings that differ from the defaults will be applied.
- Throws: `ArdkError.invalidArgument` if the configuration is invalid. Check ARDK's C logs for more information.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| config | An object that defines this session’s behavior. Only settings that differ from the defaults will be applied. |

### `start()`<a href="#start" class="hash-link" aria-label="Direct link to start" title="Direct link to start">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func start()
```

</div>

</div>

Starts scanning.

"Scanning" here may include up to three processes — recording input AR data, raycasting, and voxelization — depending on how the feature is configured.

Raycasting and voxelization are useful for visualizing scanned areas and providing feedback to the user about their scan.

- SeeAlso: `stop()`
- SeeAlso: `configure(_:)`

### `stop()`<a href="#stop" class="hash-link" aria-label="Direct link to stop" title="Direct link to stop">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func stop()
```

</div>

</div>

Stops scanning and discards any unsaved scan data.

Halts any active scanning while keeping the scanner instance alive. You can restart scanning later by calling `start()`.

- SeeAlso: `start()`

### `recordingInfo()`<a href="#recordinginfo" class="hash-link" aria-label="Direct link to recordinginfo" title="Direct link to recordinginfo">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func recordingInfo() -> RecordingInfo
```

</div>

</div>

Returns information about the current recording.

Call this method **before** `saveCurrentScan()` to ensure that the recording contains frames to save. Otherwise, the save operation may fail.

- Returns: A `RecordingInfo` object containing details about the current recording.
- Throws: An error if the underlying ARDK call fails.
- Note: Make sure to call this method before `saveCurrentScan()` if you plan to save the current scan; otherwise, the save may fail.

### `saveCurrentScan(timeout:pollingInterval:)`<a href="#savecurrentscantimeoutpollinginterval" class="hash-link" aria-label="Direct link to savecurrentscantimeoutpollinginterval" title="Direct link to savecurrentscantimeoutpollinginterval">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func saveCurrentScan(
    timeout: Double = 10.0,
    pollingInterval: TimeInterval = 0.1
) async throws -> SaveInfo
```

</div>

</div>

Stops recording and asynchronously saves the recording to the configured path.

Calling this function will stop the active recording, but `stop` must still be called afterward to completely shut down this session.

- Parameters:
  - timeout: The maximum duration in seconds to wait for the save operation (default is 10 seconds).
  - pollingInterval: The interval in seconds to wait between progress checks (default is 0.1 seconds)
- Returns: Information about the saved scan, including it's id and file location.
- Throws:
  - `CancellationError` if the Task running this function was cancelled.
  - `TimeoutError` if the function timed out before it could complete execution.
  - `ArdkScanningSession.SaveError` if there was an error specific to the save operation.
- SeeAlso:
  - `stop`
  - `configure(with:)`

#### Parameters<a href="#parameters-1" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| timeout | The maximum duration in seconds to wait for the save operation (default is 10 seconds). |
| pollingInterval | The interval in seconds to wait between progress checks (default is 0.1 seconds) |

### `exportArchive(metadata:exportAsVideo:)`<a href="#exportarchivemetadataexportasvideo" class="hash-link" aria-label="Direct link to exportarchivemetadataexportasvideo" title="Direct link to exportarchivemetadataexportasvideo">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func exportArchive(metadata: [String: Any]? = nil, exportAsVideo: Bool = true) throws -> String?
```

</div>

</div>

Exports the scan data as an archive file.

This method processes the saved scan data and exports it to a standard archive format that can be used with external 3D processing tools or Niantic's VPS map.

- Note: This function is blocking and may take a while to execute. See `ArdkRecordingExporter` for a non-blocking alternative.

- Precondition: Argument `metadata` must be a valid JSON object string.

- Parameter metadata: Metadata dictionary to include with the export. Can be left empty.

- Parameter exportAsVideo: If true, the RGB frames in the scan will be exported as an .mp4 video. If false, they will be individual image files.

- Returns: The path of the archive file, if the export was successful, `nil` if otherwise. Export failure indicates something was wrong with the saved scan.

- Throws:

  - `ArdkError.invalidOperation` if the scanning session did not have a saved scan to export.

#### Parameters<a href="#parameters-2" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| metadata | Metadata dictionary to include with the export. Can be left empty. |
| exportAsVideo | If true, the RGB frames in the scan will be exported as an .mp4 video. If false, they will be individual image files. |

### `exportSplitArchive(metadata:maxFramesPerArchive:exportAsVideo:)`<a href="#exportsplitarchivemetadatamaxframesperarchiveexportasvideo" class="hash-link" aria-label="Direct link to exportsplitarchivemetadatamaxframesperarchiveexportasvideo" title="Direct link to exportsplitarchivemetadatamaxframesperarchiveexportasvideo">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func exportSplitArchive(metadata: [String: Any]? = nil, maxFramesPerArchive: Int, exportAsVideo: Bool = true) throws -> [String]?
```

</div>

</div>

Exports the scan data as multiple archive files.

This method processes the saved scan data and exports it to multiple archive files based on the maxFramesPerArchive parameter. Each archive will contain at most maxFramesPerArchive frames.

- Note: This function is blocking and may take a while to execute.

- Precondition: Argument `metadata` must be a valid JSON object string.

- Parameter metadata: Metadata dictionary to include with the export. Can be left empty.

- Parameter maxFramesPerArchive: Maximum number of frames per archive file.

- Parameter exportAsVideo: If true, the RGB frames in the scan will be exported as an .mp4 video. If false, they will be individual image files.

- Returns: An array of paths to the archive files, if the export was successful, `nil` if otherwise. Export failure indicates something was wrong with the saved scan.

- Throws:

  - `ArdkError.invalidOperation` if the scanning session did not have a saved scan to export.

#### Parameters<a href="#parameters-3" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| metadata | Metadata dictionary to include with the export. Can be left empty. |
| maxFramesPerArchive | Maximum number of frames per archive file. |
| exportAsVideo | If true, the RGB frames in the scan will be exported as an .mp4 video. If false, they will be individual image files. |

### `raycastBuffer()`<a href="#raycastbuffer" class="hash-link" aria-label="Direct link to raycastbuffer" title="Direct link to raycastbuffer">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func raycastBuffer() ->  RaycastBuffer?
```

</div>

</div>

Get the most recently computed raycast buffers.

Once the session has been started and all the requested data has been sent through the ArdkSession, a buffer should become available after a brief computation period.

- Precondition: Raycast visualization must have been enabled in the configuration.
- Returns: The most recently computed raycast buffers if available, nil if not.

### `computeVoxels()`<a href="#computevoxels" class="hash-link" aria-label="Direct link to computevoxels" title="Direct link to computevoxels">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func computeVoxels()
```

</div>

</div>

Compute the voxelization of the scanned scene.

Processing is asynchronous. Call this function and then call `getVoxelBuffer()` to retrieve voxel data.

- Precondition: Voxel visualization must have been enabled in the configuration.

### `voxelBuffer()`<a href="#voxelbuffer" class="hash-link" aria-label="Direct link to voxelbuffer" title="Direct link to voxelbuffer">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func voxelBuffer() -> VoxelBuffer?
```

</div>

</div>

Get the most recently computed voxel data.

Once the session has been started and all the requested data has been sent through the ArdkSession, a new buffer should become available after a brief computation period after `computeVoxels()` has been called.

- Precondition: Voxel visualization must have been enabled in the configuration.
- Returns: The most recently computed voxel data if available, nil if not.

</div>

</div>
