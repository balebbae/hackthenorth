---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/ArdkSemanticsSession/
title: ArdkSemanticsSession
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `ArdkSemanticsSession`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public final class ArdkSemanticsSession: ArdkSession.IDisposable, ArdkFeatureSession
```

</div>

</div>

A session for semantic segmentation and environmental understanding.

`ArdkSemanticsSession` provides capabilities for understanding the semantic structure of the environment by classifying pixels into different object categories. This enables applications to make intelligent decisions based on environmental context.

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Semantics features include:

- Real-time semantic segmentation of camera images
- Multiple semantic categories (sky, ground, buildings, people, etc.)
- Confidence maps for semantic classifications
- Packed channel data for efficient processing
- Suppression masks for filtering unwanted areas

## Usage Pattern<a href="#usage-pattern" class="hash-link" aria-label="Direct link to Usage Pattern" title="Direct link to Usage Pattern">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
// Create and configure semantics session
let semanticsSession = ardkSession.createSemanticsSession()
let config = Configuration()
semanticsSession.configure(with: config)
semanticsSession.start()

// Get available semantic channels
let (error, channelNames) = semanticsSession.getChannelNames()
if error == .none, let names = channelNames {
    print("Available channels: \(names)")
}

// Get semantic confidence for a specific channel
let (status, result) = semanticsSession.getLatestConfidence(channelIndex: 0)
if status.isOk(), let semanticResult = result {
    // Process semantic data
    processSemanticData(semanticResult)
}
```

</div>

</div>

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `featureStatus()`<a href="#featurestatus" class="hash-link" aria-label="Direct link to featurestatus" title="Direct link to featurestatus">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func featureStatus() -> ArdkFeatureStatus
```

</div>

</div>

Gets the current status of the Semantics feature.

This method reports any errors or warnings that have occurred within the semantics system. Check this periodically to monitor the health of semantic processing operations.

- Returns: Feature status flags indicating current state and any issues

## Example<a href="#example" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
let status = semanticsSession.getFeatureStatus()
if status.contains(.failed) {
    print("Semantics has encountered an error")
}
```

</div>

</div>

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

Starts the Semantics system.

After starting, Semantics will begin processing incoming frame data for semantic segmentation. The system must be configured before starting.

## Example<a href="#example-1" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
semanticsSession.configure(with: config)
semanticsSession.start()
```

</div>

</div>

### `stop()`<a href="#stop" class="hash-link" aria-label="Direct link to stop" title="Direct link to stop">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func stop()
```

</div>

</div>

Stops the Semantics system.

This halts all semantic processing. The session can be reconfigured and restarted after stopping.

### `channelNames()`<a href="#channelnames" class="hash-link" aria-label="Direct link to channelnames" title="Direct link to channelnames">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func channelNames() -> ArdkAsyncState<[String], AwarenessError>
```

</div>

</div>

Retrieves the names of available semantic channels.

This method returns the list of semantic categories that are available for processing. Channel names can be used to understand what semantic information is available and to select appropriate channels for your application.

### `latestConfidence(channelIndex:)`<a href="#latestconfidencechannelindex" class="hash-link" aria-label="Direct link to latestconfidencechannelindex" title="Direct link to latestconfidencechannelindex">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func latestConfidence(channelIndex: Int) throws -> ArdkAsyncState<SemanticsResult, AwarenessError>
```

</div>

</div>

Retrieves the latest confidence map for a specific semantic channel.

This method returns a confidence map where each pixel value represents the confidence score (0.0-1.0) that the pixel belongs to the specified semantic category. Higher confidence values indicate stronger belief in the semantic classification.

- Parameter channelIndex: The index of the semantic channel to retrieve
- Returns: A tuple containing the operation status and semantic result if successful

## Example<a href="#example-2" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
// Get confidence for "sky" channel (assuming it's at index 0)
let (status, result) = semanticsSession.getLatestConfidence(channelIndex: 0)
if status.isOk(), let semanticResult = result {
    print("Sky confidence image size: \(semanticResult.image?.width ?? 0) x \(semanticResult.image?.height ?? 0)")

    // Process confidence data
    if let image = semanticResult.image {
        processConfidenceMap(image, forChannel: "sky")
    }
}
```

</div>

</div>

## Confidence Interpretation<a href="#confidence-interpretation" class="hash-link" aria-label="Direct link to Confidence Interpretation" title="Direct link to Confidence Interpretation">​</a>

Confidence values range from 0.0 to 1.0:

- **0.0**: Definitely not the specified semantic category
- **0.5**: Uncertain classification
- **1.0**: Definitely the specified semantic category

Use confidence thresholds to filter results based on your application's needs.

#### Parameters<a href="#parameters-1" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name         | Description                                   |
|--------------|-----------------------------------------------|
| channelIndex | The index of the semantic channel to retrieve |

### `latestPackedChannels()`<a href="#latestpackedchannels" class="hash-link" aria-label="Direct link to latestpackedchannels" title="Direct link to latestpackedchannels">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func latestPackedChannels() -> ArdkAsyncState<SemanticsResult, AwarenessError>
```

</div>

</div>

Retrieves the latest packed semantic channels data.

This method returns a multi-channel image where each channel represents a different semantic category. Packed channels provide an efficient way to access multiple semantic classifications in a single image, reducing the need for multiple API calls.

- Returns: A tuple containing the operation status and semantic result if successful

## Example<a href="#example-3" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
let (status, result) = semanticsSession.getLatestPackedChannels()
if status.isOk(), let semanticResult = result {
    print("Packed channels image size: \(semanticResult.image?.width ?? 0) x \(semanticResult.image?.height ?? 0)")

    // Process packed semantic data
    if let image = semanticResult.image {
        processPackedSemanticChannels(image)
    }
}
```

</div>

</div>

## Packed Channels Format<a href="#packed-channels-format" class="hash-link" aria-label="Direct link to Packed Channels Format" title="Direct link to Packed Channels Format">​</a>

The packed channels image contains multiple semantic categories encoded as separate channels in a single image. Each channel corresponds to a semantic category, and pixel values represent classification confidence or probability scores.

## Performance Benefits<a href="#performance-benefits" class="hash-link" aria-label="Direct link to Performance Benefits" title="Direct link to Performance Benefits">​</a>

Using packed channels is more efficient than calling `getLatestConfidence` multiple times, as it reduces the number of API calls and data transfers required.

### `latestSuppressionMask()`<a href="#latestsuppressionmask" class="hash-link" aria-label="Direct link to latestsuppressionmask" title="Direct link to latestsuppressionmask">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func latestSuppressionMask() -> ArdkAsyncState<SemanticsResult, AwarenessError>
```

</div>

</div>

Retrieves the latest suppression mask for semantic processing.

This method returns a binary mask indicating areas that should be ignored or suppressed during semantic processing. Suppression masks are useful for filtering out regions that are not relevant for semantic understanding, such as areas with poor image quality.

- Returns: A tuple containing the operation status and semantic result if successful

## Example<a href="#example-4" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
let (status, result) = semanticsSession.getLatestSuppressionMask()
if status.isOk(), let semanticResult = result {
    print("Suppression mask image size: \(semanticResult.image?.width ?? 0) x \(semanticResult.image?.height ?? 0)")

    // Apply suppression mask to filter semantic results
    if let mask = semanticResult.image {
        applySuppressionMask(mask, toSemanticResults: otherResults)
    }
}
```

</div>

</div>

## Suppression Mask Usage<a href="#suppression-mask-usage" class="hash-link" aria-label="Direct link to Suppression Mask Usage" title="Direct link to Suppression Mask Usage">​</a>

Suppression masks are typically binary images where:

- **0**: Areas to be suppressed (ignored in semantic processing)
- **1**: Areas to be processed normally

Use suppression masks to improve semantic processing quality by excluding problematic regions from analysis.

### `latestImageParams()`<a href="#latestimageparams" class="hash-link" aria-label="Direct link to latestimageparams" title="Direct link to latestimageparams">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func latestImageParams() -> ArdkAsyncState<AwarenessImageParams, AwarenessError>
```

</div>

</div>

Retrieves the latest camera intrinsic parameters for semantic processing.

This method returns the camera intrinsic parameters that were used during semantic processing. These parameters are essential for coordinate transformations between image coordinates and 3D world coordinates.

- Returns: A tuple containing the operation status and intrinsics result

</div>

</div>
