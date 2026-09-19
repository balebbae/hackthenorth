---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/extensions/ArdkSession/
title: ArdkSession
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**EXTENSION**

<div>

# `ArdkSession`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
extension ArdkSession
```

</div>

</div>

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `createDepthSession()`<a href="#createdepthsession" class="hash-link" aria-label="Direct link to createdepthsession" title="Direct link to createdepthsession">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func createDepthSession() -> ArdkDepthSession
```

</div>

</div>

### `createDeviceMappingSession()`<a href="#createdevicemappingsession" class="hash-link" aria-label="Direct link to createdevicemappingsession" title="Direct link to createdevicemappingsession">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func createDeviceMappingSession() -> ArdkDeviceMappingSession
```

</div>

</div>

Creates a new Mapping session.

- Returns: A new Device Mapping session attached to this ARDK session

### `createMapStorage()`<a href="#createmapstorage" class="hash-link" aria-label="Direct link to createmapstorage" title="Direct link to createmapstorage">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func createMapStorage() -> ArdkMapStorage
```

</div>

</div>

### `createMeshDownloader()`<a href="#createmeshdownloader" class="hash-link" aria-label="Direct link to createmeshdownloader" title="Direct link to createmeshdownloader">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func createMeshDownloader() -> ArdkMeshDownloader
```

</div>

</div>

Creates a new Mesh Downloader instance.

- Returns: A new `ArdkMeshDownloader` attached to this ARDK session.

### `createMeshingSession()`<a href="#createmeshingsession" class="hash-link" aria-label="Direct link to createmeshingsession" title="Direct link to createmeshingsession">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func createMeshingSession() -> ArdkMeshingSession
```

</div>

</div>

Creates a new Meshing session.

- Returns: A new Meshing session attached to this ARDK session

### `createObjectDetectionSession()`<a href="#createobjectdetectionsession" class="hash-link" aria-label="Direct link to createobjectdetectionsession" title="Direct link to createobjectdetectionsession">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func createObjectDetectionSession() -> ArdkObjectDetectionSession
```

</div>

</div>

### `createRecordingExporter()`<a href="#createrecordingexporter" class="hash-link" aria-label="Direct link to createrecordingexporter" title="Direct link to createrecordingexporter">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func createRecordingExporter() -> ArdkRecordingExporter
```

</div>

</div>

Creates a new Recording Exporter session.

Recording Export enables the conversion and export of saved scan recordings to various formats for external processing or sharing. This session manages the export workflow from scan selection through format conversion and output.

- Returns: A new Recording Exporter session attached to this ARDK session

### `createScanningSession()`<a href="#createscanningsession" class="hash-link" aria-label="Direct link to createscanningsession" title="Direct link to createscanningsession">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func createScanningSession() -> ArdkScanningSession
```

</div>

</div>

Creates a new Scanning session.

- Returns: A new Scanning session attached to this ARDK session

### `createSemanticsSession()`<a href="#createsemanticssession" class="hash-link" aria-label="Direct link to createsemanticssession" title="Direct link to createsemanticssession">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func createSemanticsSession() -> ArdkSemanticsSession
```

</div>

</div>

Creates a new Semantics session.

Semantics enables pixel-level understanding of the environment by classifying objects and surfaces in camera images. This session manages semantic segmentation processing and provides access to semantic understanding results.

- Returns: A new Semantics session attached to this ARDK session

## Example<a href="#example" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
let session = ArdkSession(apiKey: "your-api-key")
let semanticsSession = session.createSemanticsSession()
```

</div>

</div>

### `createSitesSession()`<a href="#createsitessession" class="hash-link" aria-label="Direct link to createsitessession" title="Direct link to createsitessession">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func createSitesSession() -> ArdkSitesSession
```

</div>

</div>

### `createVpsSession()`<a href="#createvpssession" class="hash-link" aria-label="Direct link to createvpssession" title="Direct link to createvpssession">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func createVpsSession() -> ArdkVpsSession
```

</div>

</div>

Creates a new VPS (Visual Positioning System) session.

- Returns: A new VPS session attached to this ARDK session

### `createVpsCoverageSession()`<a href="#createvpscoveragesession" class="hash-link" aria-label="Direct link to createvpscoveragesession" title="Direct link to createvpscoveragesession">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func createVpsCoverageSession() -> ArdkVpsCoverageSession
```

</div>

</div>

Creates a new VPS Coverage session.

- Returns: A new `ArdkVpsCoverageSession` instance attached to this ARDK session.

### `createWpsSession()`<a href="#createwpssession" class="hash-link" aria-label="Direct link to createwpssession" title="Direct link to createwpssession">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func createWpsSession() -> ArdkWpsSession
```

</div>

</div>

Creates a new World Positioning System (WPS) session.

- Returns: A new WPS session attached to this ARDK session

</div>

</div>
