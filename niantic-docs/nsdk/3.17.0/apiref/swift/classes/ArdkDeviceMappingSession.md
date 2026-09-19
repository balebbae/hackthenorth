---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/ArdkDeviceMappingSession/
title: ArdkDeviceMappingSession
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `ArdkDeviceMappingSession`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public final class ArdkDeviceMappingSession: ArdkSession.IDisposable, ArdkFeatureSession
```

</div>

</div>

A session for creating VPS maps from AR data on the local device.

The device mapping feature provides capabilities for locally building persistent maps that can be used for Visual Positioning System (VPS) localization. These maps capture the visual features and spatial structure of an environment.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `featureStatus()`<a href="#featurestatus" class="hash-link" aria-label="Direct link to featurestatus" title="Direct link to featurestatus">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func featureStatus() -> ArdkFeatureStatus
```

</div>

</div>

Reports the current status of the mapping session.

Check this periodically to see if any errors have occurred with processes running inside this feature. Once an error has been flagged, it will remain flagged until the culprit process has been run again and completed successfully.

- Returns: A flag indicating the current status of the mapping session.

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

Starts the mapping session and initializes required processes.

Downloads the mapping algorithm model and prepares the session for mapping operations. Does not begin map building; call `startMapping()` to start building a map.

### `stop()`<a href="#stop" class="hash-link" aria-label="Direct link to stop" title="Direct link to stop">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func stop()
```

</div>

</div>

Stop all mapping processes.

- Note: If mapping is in progress, this will stop mapping.

### `startMapping()`<a href="#startmapping" class="hash-link" aria-label="Direct link to startmapping" title="Direct link to startmapping">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func startMapping()
```

</div>

</div>

Begin a mapping sequence.

This begins building an on-device map that can be used for VPS. Map data is accumulated in `ArdkMapStorage` while mapping is running. Poll `ArdkMapStorage.mapUpdate()` periodically to retrieve incremental map updates, or call `ArdkMapStorage.mapData()` after mapping completes to get the full map.

- Attention: This method must be called after `start()` and before `stop()`.

### `stopMapping()`<a href="#stopmapping" class="hash-link" aria-label="Direct link to stopmapping" title="Direct link to stopmapping">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func stopMapping()
```

</div>

</div>

Stop the current mapping sequence.

This stops adding new frames to the current on-device VPS Map.

</div>

</div>
