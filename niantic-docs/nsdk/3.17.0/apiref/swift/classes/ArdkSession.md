---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/ArdkSession/
title: ArdkSession
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `ArdkSession`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public final class ArdkSession
```

</div>

</div>

The main entry point for the ARDK (Augmented Reality Development Kit) framework.

`ArdkSession` provides the core functionality for AR applications, managing the lifecycle of ARDK features and serving as a factory for specialized sessions like VPS, WPS, scanning, and mapping. This class handles frame data processing, configuration management, and resource cleanup.

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Use `ArdkSession` to:

- Initialize the ARDK with your API key and configuration
- Send camera frame data for processing
- Create specialized feature sessions (VPS, WPS, Scanning, Mapping)
- Query required input data formats
- Manage the lifecycle of ARDK resources

## Example Usage<a href="#example-usage" class="hash-link" aria-label="Direct link to Example Usage" title="Direct link to Example Usage">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
// Initialize with API key
let session = ArdkSession(apiKey: "your-api-key")

// Create a VPS session for localization
let vpsSession = session.createVpsSession()

// Send frame data during AR session
let status = session.sendFrame(frameData)
```

</div>

</div>

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `nativeHandle`<a href="#nativehandle" class="hash-link" aria-label="Direct link to nativehandle" title="Direct link to nativehandle">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let nativeHandle: ArdkHandle
```

</div>

</div>

The native handle to the underlying ARDK C API instance.

This handle is used internally to communicate with the native ARDK library and should not be modified directly by application code.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `init(apiKey:useLidar:pathConfig:logCallback:)`<a href="#initapikeyuselidarpathconfiglogcallback" class="hash-link" aria-label="Direct link to initapikeyuselidarpathconfiglogcallback" title="Direct link to initapikeyuselidarpathconfiglogcallback">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public convenience init(apiKey: String, useLidar: Bool = true, pathConfig: ArdkPathConfig? = nil, logCallback: ArdkLogCallback? = nil)
```

</div>

</div>

Creates a new ARDK session with the specified API key and configuration.

This is the recommended way to initialize ARDK for most use cases. The session will automatically configure itself with default settings appropriate for AR applications.

- Parameters:
  - apiKey: Your ARDK API key obtained from the developer portal
  - useLidar: Whether to use LiDAR depth data when available (default: true)
  - pathConfig: Optional path configuration for custom file locations
  - logCallback: Optional callback to receive ARDK log messages

## Example<a href="#example" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
let session = ArdkSession(apiKey: "your-api-key")
let sessionWithoutLidar = ArdkSession(apiKey: "your-api-key", useLidar: false)
```

</div>

</div>

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| apiKey | Your ARDK API key obtained from the developer portal |
| useLidar | Whether to use LiDAR depth data when available (default: true) |
| pathConfig | Optional path configuration for custom file locations |
| logCallback | Optional callback to receive ARDK log messages |

### `init(withJson:logCallback:)`<a href="#initwithjsonlogcallback" class="hash-link" aria-label="Direct link to initwithjsonlogcallback" title="Direct link to initwithjsonlogcallback">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public convenience init?(withJson configFilePath: String, logCallback: ArdkLogCallback? = nil)
```

</div>

</div>

Creates a new ARDK session from a JSON configuration file.

Use this initializer for fine-grained control over ARDK configuration or when loading settings from a configuration file.

- Parameters:
  - configFilePath: Path to the JSON configuration file
  - logCallback: Optional callback to receive ARDK log messages
- Returns: A new ARDK session, or `nil` if configuration loading fails

## Example<a href="#example-1" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
if let session = ArdkSession(withJson: "/path/to/config.json") {
    // Session created successfully
} else {
    // Failed to load configuration
}
```

</div>

</div>

#### Parameters<a href="#parameters-1" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name           | Description                                    |
|----------------|------------------------------------------------|
| configFilePath | Path to the JSON configuration file            |
| logCallback    | Optional callback to receive ARDK log messages |

### `init(withConfig:)`<a href="#initwithconfig" class="hash-link" aria-label="Direct link to initwithconfig" title="Direct link to initwithconfig">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public convenience init?(withConfig config: Configuration)
```

</div>

</div>

Creates a new ARDK session with a Configuration object.

Use this initializer for fine-grained control over ARDK configuration

- Parameter config: The configuration object with defined settings
- Returns: A new ARDK session, or `nil` if configuration is invalid

## Example<a href="#example-2" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
let config = Configuration()
// Configure settings...
if let session = ArdkSession(withConfig: config) {
    // Session created successfully
}
```

</div>

</div>

#### Parameters<a href="#parameters-2" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name   | Description                                    |
|--------|------------------------------------------------|
| config | The configuration object with defined settings |

### `init(accessToken:refreshToken:useLidar:pathConfig:logCallback:)`<a href="#initaccesstokenrefreshtokenuselidarpathconfiglogcallback" class="hash-link" aria-label="Direct link to initaccesstokenrefreshtokenuselidarpathconfiglogcallback" title="Direct link to initaccesstokenrefreshtokenuselidarpathconfiglogcallback">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public convenience init(accessToken: String, refreshToken: String, useLidar: Bool = true, pathConfig: ArdkPathConfig? = nil, logCallback: ArdkLogCallback? = nil)
```

</div>

</div>

Convenience initializer that accepts access and refresh tokens instead of an API key. Tokens are sanitized and passed to native AuthManagerApi immediately via creation call.

### `deinit`<a href="#deinit" class="hash-link" aria-label="Direct link to deinit" title="Direct link to deinit">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
deinit
```

</div>

</div>

### `sendFrame(_:)`<a href="#sendframe_" class="hash-link" aria-label="Direct link to sendframe_" title="Direct link to sendframe_">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func sendFrame(_ frameData: ArdkFrameData)
```

</div>

</div>

Sends a frame of data to ARDK for processing.

Call this method for each frame captured from an AR session. This will push the captured frame data into ARDK's native components for processing by active features.

- Parameter frameData: The frame data captured from the AR session

#### Parameters<a href="#parameters-3" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name      | Description                                 |
|-----------|---------------------------------------------|
| frameData | The frame data captured from the AR session |

### `requestedDataInputs()`<a href="#requesteddatainputs" class="hash-link" aria-label="Direct link to requesteddatainputs" title="Direct link to requesteddatainputs">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func requestedDataInputs() -> ArdkInputDataFlags
```

</div>

</div>

Get the current set of input data types that are required by ARDK's native components.

Use this method to determine what data should be included in frames sent to `sendFrame(_:)`. The required data formats may change based on currently active features and their states.

- Returns: Flags indicating which data types are currently required

## Example<a href="#example-3" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
let requiredInputs = session.requestedDataInputs()
if requiredInputs.contains(.camera) {
    // Include camera data in frame
}
if requiredInputs.contains(.depth) {
    // Include depth data in frame
}
```

</div>

</div>

### `setStdoutLogLevel(logLevel:)`<a href="#setstdoutloglevelloglevel" class="hash-link" aria-label="Direct link to setstdoutloglevelloglevel" title="Direct link to setstdoutloglevelloglevel">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func setStdoutLogLevel(logLevel: ArdkLogLevel)
```

</div>

</div>

Sets the log level for standard output logging.

- Parameter logLevel: The desired log level for standard output

#### Parameters<a href="#parameters-4" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name     | Description                               |
|----------|-------------------------------------------|
| logLevel | The desired log level for standard output |

### `setFileLogLevel(logLevel:)`<a href="#setfileloglevelloglevel" class="hash-link" aria-label="Direct link to setfileloglevelloglevel" title="Direct link to setfileloglevelloglevel">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func setFileLogLevel(logLevel: ArdkLogLevel)
```

</div>

</div>

Sets the log level for file logging.

- Parameter logLevel: The desired log level for file logging

#### Parameters<a href="#parameters-5" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name     | Description                            |
|----------|----------------------------------------|
| logLevel | The desired log level for file logging |

### `setCallbackLogLevel(logLevel:)`<a href="#setcallbackloglevelloglevel" class="hash-link" aria-label="Direct link to setcallbackloglevelloglevel" title="Direct link to setcallbackloglevelloglevel">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func setCallbackLogLevel(logLevel: ArdkLogLevel)
```

</div>

</div>

Sets the log level for callback logging.

- Parameter logLevel: The desired log level for callback logging

#### Parameters<a href="#parameters-6" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name     | Description                                |
|----------|--------------------------------------------|
| logLevel | The desired log level for callback logging |

### `version()`<a href="#version" class="hash-link" aria-label="Direct link to version" title="Direct link to version">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static func version() -> String
```

</div>

</div>

Retrieves the ARDK version string.

### `setAccessToken(_:)`<a href="#setaccesstoken_" class="hash-link" aria-label="Direct link to setaccesstoken_" title="Direct link to setaccesstoken_">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func setAccessToken(_ token: String)
```

</div>

</div>

Sets the access token on native (routed through AuthManagerApi via C-ABI). Empty or whitespace-only tokens are ignored by native.

### `setRefreshToken(_:)`<a href="#setrefreshtoken_" class="hash-link" aria-label="Direct link to setrefreshtoken_" title="Direct link to setrefreshtoken_">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func setRefreshToken(_ token: String)
```

</div>

</div>

Sets the refresh token on native (routed through AuthManagerApi via C-ABI). Empty or whitespace-only tokens are ignored by native.

</div>

</div>
