---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/ArdkMapStorage/
title: ArdkMapStorage
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `ArdkMapStorage`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public final class ArdkMapStorage: ArdkSession.IDisposable
```

</div>

</div>

A storage system for managing device-generated maps.

The map storage feature provides capabilities for capturing, storing, and managing map data from AR sessions. This data can be persisted and used for Visual Positioning System (VPS) localization and map updates.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `mapData()`<a href="#mapdata" class="hash-link" aria-label="Direct link to mapdata" title="Direct link to mapdata">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func mapData() -> ArdkBuffer?
```

</div>

</div>

Gets the complete map data.

This function returns all the map data accumulated during the AR session, serialized as a DeviceMap protobuf. This data can be saved, shared, and/or used for localization.

- Returns: The serialized map data buffer if available, `nil` if no map data exists.

### `mapUpdate()`<a href="#mapupdate" class="hash-link" aria-label="Direct link to mapupdate" title="Direct link to mapupdate">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func mapUpdate() -> ArdkBuffer?
```

</div>

</div>

Gets the latest map update data.

This method returns the incremental map changes (new nodes and edges) that have been added since the last update.

- Returns: The serialized map update if available, `nil` if no updates exist.

### `createRootAnchor()`<a href="#createrootanchor" class="hash-link" aria-label="Direct link to createrootanchor" title="Direct link to createrootanchor">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func createRootAnchor() -> String?
```

</div>

</div>

Creates an anchor on the existing map located at the origin of the current AR session, if possible.

The root anchor represents the origin point of the map coordinate system and can be used with VPS for localization.

- Returns: The payload of the root anchor, encoded as a base64 string if available, `nil` if otherwise.

### `addMap(map:)`<a href="#addmapmap" class="hash-link" aria-label="Direct link to addmapmap" title="Direct link to addmapmap">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func addMap(map: ArdkBuffer) throws
```

</div>

</div>

Adds previously serialized map data to the map storage.

- Parameter map: The serialized map data to add. It should be encoded as a DeviceMap protobuf and can be obtained from `mapData()`, `mapUpdate()`, or `mergeMapUpdate(existingMap:mapUpdate:)`.
- Throws: `ArdkError.invalidArgument`or `ArdkError.nullArgument` indicating a problem with the `map` argument . Check ARDK's C logs for more information.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| map | The serialized map data to add. It should be encoded as a DeviceMap protobuf and can be obtained from `mapData()`, `mapUpdate()`, or `mergeMapUpdate(existingMap:mapUpdate:)`. |

### `clear()`<a href="#clear" class="hash-link" aria-label="Direct link to clear" title="Direct link to clear">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func clear()
```

</div>

</div>

- Note: Must not be called if VPS is running. If called, localization data will be discarded and the session state will be undefined.

### `extractMapMetadata(anchorPayload:map:)`<a href="#extractmapmetadataanchorpayloadmap" class="hash-link" aria-label="Direct link to extractmapmetadataanchorpayloadmap" title="Direct link to extractmapmetadataanchorpayloadmap">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func extractMapMetadata(anchorPayload: String, map: ArdkBuffer) throws -> MapMetadata?
```

</div>

</div>

Extracts metadata from a map relative to a specified anchor.

Render the feature points in the metadata relative to the specified anchor to visualize the map. This is only possible when the anchor is linked directly to the map's node(s), or if the anchor's nodes are reachable to the map's nodes from the currently active transform graph.

- Parameter anchorPayload: The base64-encoded payload of the anchor that the returned points will be relative to.
- Parameter map: The map buffer to extract metadata from.
- Returns: The metadata of the map if successful, `nil` if otherwise.
- Throws: `ArdkError.invalidArgument`or `ArdkError.nullArgument` indicating a problem with either argument. Check ARDK's C logs for more information.

#### Parameters<a href="#parameters-1" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| anchorPayload | The base64-encoded payload of the anchor that the returned points will be relative to. |
| map | The map buffer to extract metadata from. |

### `mergeMapUpdate(existingMap:mapUpdate:)`<a href="#mergemapupdateexistingmapmapupdate" class="hash-link" aria-label="Direct link to mergemapupdateexistingmapmapupdate" title="Direct link to mergemapupdateexistingmapmapupdate">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func mergeMapUpdate(existingMap: ArdkBuffer, mapUpdate: ArdkBuffer) throws -> ArdkBuffer
```

</div>

</div>

Merges a map update into an existing map.

This method combines incremental map updates with a base map to produce a merged map buffer containing the complete map data.

- Parameter existingMap: The existing map to merge the update into.
- Parameter mapUpdate: The map update to merge into the existing map.
- Returns: The merged map buffer
- Throws: `ArdkError` of type `ArdkError.invalidArgument`or `ArdkError.nullArgument` indicating a problem with either argument . Check ARDK's C logs for more information.

#### Parameters<a href="#parameters-2" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name        | Description                                    |
|-------------|------------------------------------------------|
| existingMap | The existing map to merge the update into.     |
| mapUpdate   | The map update to merge into the existing map. |

</div>

</div>
