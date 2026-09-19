---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/ArdkMeshDownloader/
title: ArdkMeshDownloader
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `ArdkMeshDownloader`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public final class ArdkMeshDownloader: ArdkSession.IDisposable
```

</div>

</div>

A session-scoped utility for downloading mesh geometry associated with VPS locations.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `requestLocationMesh(payload:getTexture:maxDownloadSize:timeout:pollingInterval:)`<a href="#requestlocationmeshpayloadgettexturemaxdownloadsizetimeoutpollinginterval" class="hash-link" aria-label="Direct link to requestlocationmeshpayloadgettexturemaxdownloadsizetimeoutpollinginterval" title="Direct link to requestlocationmeshpayloadgettexturemaxdownloadsizetimeoutpollinginterval">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func requestLocationMesh(
    payload: String,
    getTexture: Bool,
    maxDownloadSize: UInt32? = nil,
    timeout: TimeInterval = 300.0,
    pollingInterval: TimeInterval = 0.5
) async throws -> MeshDownloaderResults
```

</div>

</div>

Requests all meshes for a VPS location identified by an anchor payload.

Initiates a network request to download all meshes associated with the given VPS location. The call suspends until the operation completes successfully, fails, or times out.

The method automatically polls for completion and returns a `MeshDownloaderResults` object containing the downloaded geometry data.

- Parameters:
  - payload: The VPS anchor payload string identifying the target location. This can be obtained from the `blob` field in Geospatial Browser, or the `default_anchor` field of the VPS Coverage API’s `LocalizationTarget`.
  - getTexture: If `true`, the response includes mesh texture data; if `false`, the image and UV buffers are empty. Instead, a color field (rgb) will be provided for each vertex.
  - maxDownloadSize: The optional maximum size (in kilobytes) for meshes to be downloaded. Meshes larger than this limit are skipped. A value of `nil` means no size limit.
  - timeout: The maximum duration to wait for completion (default: 300 seconds).
  - pollingInterval: The interval between status checks (default: 0.5 seconds).
- Returns: A `MeshDownloaderResults` object containing the downloaded mesh data.
- Throws:
  - `CancellationError` if the Task running this function was cancelled.
  - `TimeoutError` if the function timed out before it could complete execution.
  - `ArdkError` if there was an error with one or more of the arguments. Check ARDK's C logs for more information.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| payload | The VPS anchor payload string identifying the target location. This can be obtained from the `blob` field in Geospatial Browser, or the `default_anchor` field of the VPS Coverage API’s `LocalizationTarget`. |
| getTexture | If `true`, the response includes mesh texture data; if `false`, the image and UV buffers are empty. Instead, a color field (rgb) will be provided for each vertex. |
| maxDownloadSize | The optional maximum size (in kilobytes) for meshes to be downloaded. Meshes larger than this limit are skipped. A value of `nil` means no size limit. |
| timeout | The maximum duration to wait for completion (default: 300 seconds). |
| pollingInterval | The interval between status checks (default: 0.5 seconds). |

</div>

</div>
