---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/protocols/ArdkFeatureSession/
title: ArdkFeatureSession
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**PROTOCOL**

<div>

# `ArdkFeatureSession`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public protocol ArdkFeatureSession
```

</div>

</div>

A protocol that defines the common lifecycle and configuration interface for ARDK feature sessions.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `featureStatus()`<a href="#featurestatus" class="hash-link" aria-label="Direct link to featurestatus" title="Direct link to featurestatus">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
func featureStatus() -> ArdkFeatureStatus
```

</div>

</div>

Gets the current status of the feature.

This method reports any errors or warnings that have occurred within the feature system. Check this periodically to monitor the health of operations. Once an error is flagged, it will remain flagged until the problematic process runs again and completes successfully.

- Returns: Feature status flags indicating current state and any issues

### `configure(with:)`<a href="#configurewith" class="hash-link" aria-label="Direct link to configurewith" title="Direct link to configurewith">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
func configure(with config: Configuration) throws
```

</div>

</div>

### `start()`<a href="#start" class="hash-link" aria-label="Direct link to start" title="Direct link to start">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
func start()
```

</div>

</div>

Starts the feature session.

After starting, the session will begin processing incoming frame data according to its configured behavior. The session must be configured before starting.

### `stop()`<a href="#stop" class="hash-link" aria-label="Direct link to stop" title="Direct link to stop">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
func stop()
```

</div>

</div>

Stops the feature session.

This halts all processing. The session can be reconfigured and restarted after stopping.

</div>

</div>
