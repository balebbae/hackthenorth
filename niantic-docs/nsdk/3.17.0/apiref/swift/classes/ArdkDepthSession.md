---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/ArdkDepthSession/
title: ArdkDepthSession
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `ArdkDepthSession`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public final class ArdkDepthSession: ArdkSession.IDisposable, ArdkFeatureSession
```

</div>

</div>

Depth feature session for ARDK. Provides control over depth sensing capabilities.

Upon starting the depth session, ARDK will begin processing AR frames to generate depth data. The latest depth data can be retrieved using `latestDepth()`, and `latestImageParams()` provides information to synchronize the depth image with camera frame.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `featureStatus()`<a href="#featurestatus" class="hash-link" aria-label="Direct link to featurestatus" title="Direct link to featurestatus">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func featureStatus() -> ArdkFeatureStatus
```

</div>

</div>

The current feature status of the depth session.

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

Starts the depth session, enabling depth data processing with the current configuration.

### `stop()`<a href="#stop" class="hash-link" aria-label="Direct link to stop" title="Direct link to stop">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func stop()
```

</div>

</div>

Stops the depth session, halting depth data processing.

### `latestDepth()`<a href="#latestdepth" class="hash-link" aria-label="Direct link to latestdepth" title="Direct link to latestdepth">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func latestDepth() -> ArdkAsyncState<DepthResult, AwarenessError>
```

</div>

</div>

Retrieves the latest depth result from the depth session.

- Returns: An `ArdkAsyncState` containing either the latest `DepthResult`, or an `AwarenessError`.

### `latestImageParams()`<a href="#latestimageparams" class="hash-link" aria-label="Direct link to latestimageparams" title="Direct link to latestimageparams">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func latestImageParams() -> ArdkAsyncState<AwarenessImageParams, AwarenessError>
```

</div>

</div>

Retrieves the latest image parameters associated with the depth data.

- Returns: An `ArdkAsyncState` containing either the latest `AwarenessImageParams`, or an `AwarenessError`.

</div>

</div>
