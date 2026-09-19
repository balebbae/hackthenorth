---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/ArdkFeatureStatus/
title: ArdkFeatureStatus
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `ArdkFeatureStatus`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct ArdkFeatureStatus: OptionSet, CustomStringConvertible, @unchecked Sendable
```

</div>

</div>

Status flags for ARDK features indicating their current operational state.

`ArdkFeatureStatus` is an option set that represents various status conditions for ARDK features like VPS, WPS, scanning, and mapping. Multiple status flags can be active simultaneously to provide detailed status information.

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Use this to monitor the health and state of ARDK features:

- Check for errors that need attention
- Monitor initialization progress
- Verify configuration and API key validity
- Ensure features are ready for operation

## Example Usage<a href="#example-usage" class="hash-link" aria-label="Direct link to Example Usage" title="Direct link to Example Usage">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
let status = vpsSession.getFeatureStatus()
if status.contains(.badApiKey) {
    print("Invalid API key - check your credentials")
} else if status.contains(.configurationFailed) {
    print("Feature configuration failed")
} else if status.contains(.initializing) {
    print("Feature is still initializing...")
} else if status == .ok {
    print("Feature is ready and operational")
}
```

</div>

</div>

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `rawValue`<a href="#rawvalue" class="hash-link" aria-label="Direct link to rawvalue" title="Direct link to rawvalue">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let rawValue: UInt32
```

</div>

</div>

The raw value representing the status flags.

### `ok`<a href="#ok" class="hash-link" aria-label="Direct link to ok" title="Direct link to ok">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static let ok = ArdkFeatureStatus([])
```

</div>

</div>

Feature is operating normally with no issues.

This represents the ideal state where the feature is ready and functional.

### `notused1`<a href="#notused1" class="hash-link" aria-label="Direct link to notused1" title="Direct link to notused1">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static let notused1 = ArdkFeatureStatus(fromC: ARDK_FeatureStatus_NullArdkHandle)
```

</div>

</div>

Reserved status flag (not used in current implementation).

### `notused2`<a href="#notused2" class="hash-link" aria-label="Direct link to notused2" title="Direct link to notused2">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static let notused2 = ArdkFeatureStatus(fromC: ARDK_FeatureStatus_DoesNotExist)
```

</div>

</div>

Reserved status flag (not used in current implementation).

### `configurationFailed`<a href="#configurationfailed" class="hash-link" aria-label="Direct link to configurationfailed" title="Direct link to configurationfailed">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static let configurationFailed = ArdkFeatureStatus(fromC: ARDK_FeatureStatus_ConfigurationFailed)
```

</div>

</div>

Feature configuration failed.

This indicates that the feature could not be configured with the provided settings. Check configuration parameters and try reconfiguring the feature.

### `badApiKey`<a href="#badapikey" class="hash-link" aria-label="Direct link to badapikey" title="Direct link to badapikey">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static let badApiKey = ArdkFeatureStatus(fromC: ARDK_FeatureStatus_BadApiKey)
```

</div>

</div>

Invalid or expired API key.

The provided API key is not valid or has expired. Verify your API key and ensure it has the necessary permissions for the requested features.

### `description`<a href="#description" class="hash-link" aria-label="Direct link to description" title="Direct link to description">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var description: String
```

</div>

</div>

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `init(rawValue:)`<a href="#initrawvalue" class="hash-link" aria-label="Direct link to initrawvalue" title="Direct link to initrawvalue">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public init(rawValue: UInt32)
```

</div>

</div>

Creates a feature status with the specified raw value.

- Parameter rawValue: The raw status value from the underlying C API

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name     | Description                                    |
|----------|------------------------------------------------|
| rawValue | The raw status value from the underlying C API |

### `init(fromC:)`<a href="#initfromc" class="hash-link" aria-label="Direct link to initfromc" title="Direct link to initfromc">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public init(fromC: ARDK_FeatureStatus)
```

</div>

</div>

Creates a feature status from a C API status value.

- Parameter fromC: The status value from the underlying C API

#### Parameters<a href="#parameters-1" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name  | Description                                |
|-------|--------------------------------------------|
| fromC | The status value from the underlying C API |

### `isOk()`<a href="#isok" class="hash-link" aria-label="Direct link to isok" title="Direct link to isok">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func isOk() -> Bool
```

</div>

</div>

</div>

</div>
