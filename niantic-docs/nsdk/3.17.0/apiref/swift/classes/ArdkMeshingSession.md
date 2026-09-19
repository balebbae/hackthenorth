---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/ArdkMeshingSession/
title: ArdkMeshingSession
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `ArdkMeshingSession`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public final class ArdkMeshingSession: ArdkSession.IDisposable, ArdkFeatureSession
```

</div>

</div>

A session for real-time 3D mesh generation from AR camera frames.

The meshing feature provides capabilities for processing AR session data and generating a triangle mesh representation of the physical environment in real-time. The mesh is divided into chunks that can be individually queried and updated as the environment is scanned.

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

Configures the meshing feature with the specified settings.

- Attention: If this method is called while meshing is running, the meshing feature will restart with the new configuration, and any mesh data that has been produced will be lost.

- Parameter config: An object that defines the meshing behavior.

- Throws: `ArdkError.invalidArgument` if the configuration is invalid. Check ARDK's C logs for more information.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name   | Description                                  |
|--------|----------------------------------------------|
| config | An object that defines the meshing behavior. |

### `start()`<a href="#start" class="hash-link" aria-label="Direct link to start" title="Direct link to start">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func start()
```

</div>

</div>

Starts the meshing feature.

The feature will begin processing AR frame data and building a mesh according to the currently applied configuration.

### `stop()`<a href="#stop" class="hash-link" aria-label="Direct link to stop" title="Direct link to stop">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func stop()
```

</div>

</div>

Stops the meshing feature.

- Note: This will clear previously generated mesh data.

### `updatedMeshInfos()`<a href="#updatedmeshinfos" class="hash-link" aria-label="Direct link to updatedmeshinfos" title="Direct link to updatedmeshinfos">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func updatedMeshInfos() -> MeshUpdateInfo?
```

</div>

</div>

Gets the ids of all chunks in the current mesh and their update status.

The returned information contains the ids and update status for all chunks currently in the mesh. If a chunk's updated flag is true, the mesh chunk has been updated since the last time its data was read with `meshDataById(id:)`.

To retrieve the data for a specific chunk, call `meshDataById(id:)`.

- Returns: A buffer containing updated mesh chunk ids, nil if there are no chunks.

### `meshDataById(id:)`<a href="#meshdatabyidid" class="hash-link" aria-label="Direct link to meshdatabyidid" title="Direct link to meshdatabyidid">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func meshDataById(id: Int64) -> MeshData?
```

</div>

</div>

Retrieves the mesh data for a specified chunk.

- Note: This method resets the updated flag for the specified chunk. Subsequent calls to `updatedMeshInfos()` will only mark the chunk as updated if its mesh data has changed since the mesh chunk's data was last retrieved.

- Parameter id: The ID of the mesh chunk to retrieve, obtained from `updatedMeshInfos()`.

- Returns: The mesh data for the specified chunk, or `nil` if no chunk with the given ID exists.

#### Parameters<a href="#parameters-1" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| id | The ID of the mesh chunk to retrieve, obtained from `updatedMeshInfos()`. |

### `lastMeshUpdateTime()`<a href="#lastmeshupdatetime" class="hash-link" aria-label="Direct link to lastmeshupdatetime" title="Direct link to lastmeshupdatetime">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func lastMeshUpdateTime() -> UInt64?
```

</div>

</div>

Gets the timestamp of the latest mesh update.

- Returns: The timestamp in milliseconds, or nil if no mesh data has been produced yet.

</div>

</div>
