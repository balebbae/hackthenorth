---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/
title: index
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/)

<div>

# ARDK for Android

</div>

\[androidJvm\]\
ARDK for Android provides a high-level Kotlin interface to Niantic's Augmented Reality Developer Kit. The API follows a consistent pattern where all features require initialization, configuration, and proper lifecycle management.

## Architecture<a href="#architecture" class="hash-link" aria-label="Direct link to Architecture" title="Direct link to Architecture">​</a>

The ARDK Kotlin wrapper provides a high-level interface to Niantic's Augmented Reality Developer Kit. The API follows a consistent pattern where all features require initialization, configuration, and proper lifecycle management.

### Core Concepts<a href="#core-concepts" class="hash-link" aria-label="Direct link to Core Concepts" title="Direct link to Core Concepts">​</a>

**ARDK Handle**: All operations revolve around a long integer handle that represents your ARDK instance. This handle is passed to all API calls and manages the underlying native resources.

**Feature Lifecycle**: Each ARDK feature (VPS, Mapping, Scanner) follows a standardized lifecycle:

- **Create** - Initialize the feature (main thread required)
- **Configure** - Set feature-specific parameters
- **Start** - Begin active operation
- **Stop** - Pause operation while preserving state
- **Destroy** - Clean up resources

**Thread Requirements**: Feature creation and destruction must occur on the main thread due to native manager requirements. Other operations can typically run on background threads.

## Data Flow<a href="#data-flow" class="hash-link" aria-label="Direct link to Data Flow" title="Direct link to Data Flow">​</a>

### Frame Processing<a href="#frame-processing" class="hash-link" aria-label="Direct link to Frame Processing" title="Direct link to Frame Processing">​</a>

ARDK processes camera frames and sensor data in real-time. Applications provide frame data through `FrameData` objects containing:

- Camera images and metadata
- Device sensors (GPS, compass, orientation)
- ARCore tracking data (poses, intrinsics)

The system uses an intelligent data request mechanism - ARDK only requests the sensor data it needs for current operations, optimizing performance and battery usage.

### Result Handling<a href="#result-handling" class="hash-link" aria-label="Direct link to Result Handling" title="Direct link to Result Handling">​</a>

API operations return results through the `ARDKResult<TData, TError>` wrapper, providing type-safe success/error handling:

- **Success**: Contains the requested data
- **Error**: Contains an error code of type `TError` for debugging

## Key Features<a href="#key-features" class="hash-link" aria-label="Direct link to Key Features" title="Direct link to Key Features">​</a>

### VPS (Visual Positioning System)<a href="#vps-visual-positioning-system" class="hash-link" aria-label="Direct link to VPS (Visual Positioning System)" title="Direct link to VPS (Visual Positioning System)">​</a>

Enables precise localization against Niantic's global 3D map. Supports:

- Anchor tracking and management
- Coverage area queries
- Continuous localization for drift correction
- Device map localization (local maps)

### Mapping<a href="#mapping" class="hash-link" aria-label="Direct link to Mapping" title="Direct link to Mapping">​</a>

Creates local 3D maps that can be saved, shared, and used for localization:

- Real-time scanning and mapping
- Map persistence and export
- Integration with VPS for enhanced coverage

### Scanner<a href="#scanner" class="hash-link" aria-label="Direct link to Scanner" title="Direct link to Scanner">​</a>

Provides mesh reconstruction and 3D scanning capabilities:

- Real-time mesh generation
- Scan management and export
- Quality assessment tools

## Integration Patterns<a href="#integration-patterns" class="hash-link" aria-label="Direct link to Integration Patterns" title="Direct link to Integration Patterns">​</a>

### Android Lifecycle<a href="#android-lifecycle" class="hash-link" aria-label="Direct link to Android Lifecycle" title="Direct link to Android Lifecycle">​</a>

ARDK integrates naturally with Android's activity lifecycle:

- **onCreate**: Initialize ARDK and create features
- **onResume**: Start active features
- **onPause**: Stop features while preserving state
- **onDestroy**: Clean up all resources

### ARCore Integration<a href="#arcore-integration" class="hash-link" aria-label="Direct link to ARCore Integration" title="Direct link to ARCore Integration">​</a>

ARDK is designed to work alongside ARCore, leveraging:

- Camera frames and tracking data
- Pose information and calibration
- Device orientation and sensors

### Data Optimization<a href="#data-optimization" class="hash-link" aria-label="Direct link to Data Optimization" title="Direct link to Data Optimization">​</a>

The API includes built-in optimizations:

- Conditional sensor data collection based on feature needs
- Intelligent frame throttling options
- Bandwidth management for cloud features

## Configuration<a href="#configuration" class="hash-link" aria-label="Direct link to Configuration" title="Direct link to Configuration">​</a>

Each feature supports extensive configuration through dedicated config classes:

- **VPSConfig**: Localization frequency, quality settings, temporal fusion
- **DeviceMappingConfig**: Scan parameters, quality thresholds
- **ScannerConfig**: Mesh generation settings, export options

## Best Practices<a href="#best-practices" class="hash-link" aria-label="Direct link to Best Practices" title="Direct link to Best Practices">​</a>

1.  **Resource Management**: Always pair Create/Destroy calls and follow proper lifecycle patterns
2.  **Error Handling**: Use ARDKResult pattern for robust error management
3.  **Performance**: Leverage GetRequestedDataFormats to provide only needed sensor data
4.  **Threading**: Respect main thread requirements for feature lifecycle operations
5.  **Permissions**: Ensure proper camera, location, and storage permissions before use

## Getting Started<a href="#getting-started" class="hash-link" aria-label="Direct link to Getting Started" title="Direct link to Getting Started">​</a>

### Basic Usage Example<a href="#basic-usage-example" class="hash-link" aria-label="Direct link to Basic Usage Example" title="Direct link to Basic Usage Example">​</a>

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
// Initialize ARDK
val handle = ARDK.Create("your-api-key")

// Create and configure VPS
ARDK.CreateVPS(handle)
val vpsConfig = VPSConfig(enableContinuousLocalization = true)
ARDK.ConfigureVPS(handle, vpsConfig)

// Start VPS
ARDK.StartVPS(handle)

// Send frame data
val frameData = FrameData(System.currentTimeMillis(), frameId++)
// ... populate frame data
ARDK.SendFrame(handle, frameData)

// Track an anchor
val result = ARDK.TrackVPSAnchor(handle, anchorPayload)
when (result) {
    is ARDKResultDeprecated.Success -> {
        val anchorId = result.value
        // Anchor tracked successfully
    }
    is ARDKResultDeprecated.Error -> {
        // Handle error
    }
}

// Clean up
ARDK.StopVPS(handle)
ARDK.DestroyVPS(handle)
ARDK.Destroy(handle)
```

</div>

</div>

For detailed API documentation and complete reference materials, see the API classes and functions below.

## Packages<a href="#packages" class="hash-link" aria-label="Direct link to Packages" title="Direct link to Packages">​</a>

| Name |
|----|
| \[com.nianticlabs.ardk\](-a-r-d-k for -android/com.nianticlabs.ardk/index.mdx) |
| \[com.nianticlabs.ardk.awareness.semantics\](-a-r-d-k for -android/com.nianticlabs.ardk.awareness.semantics/index.mdx) |
| \[com.nianticlabs.ardk.depth\](-a-r-d-k for -android/com.nianticlabs.ardk.depth/index.mdx) |
| \[com.nianticlabs.ardk.mapping\](-a-r-d-k for -android/com.nianticlabs.ardk.mapping/index.mdx) |
| \[com.nianticlabs.ardk.mesh\](-a-r-d-k for -android/com.nianticlabs.ardk.mesh/index.mdx) |
| \[com.nianticlabs.ardk.objectdetection\](-a-r-d-k for -android/com.nianticlabs.ardk.objectdetection/index.mdx) |
| \[com.nianticlabs.ardk.recording\](-a-r-d-k for -android/com.nianticlabs.ardk.recording/index.mdx) |
| \[com.nianticlabs.ardk.scanning\](-a-r-d-k for -android/com.nianticlabs.ardk.scanning/index.mdx) |
| \[com.nianticlabs.ardk.utils\](-a-r-d-k for -android/com.nianticlabs.ardk.utils/index.mdx) |
| \[com.nianticlabs.ardk.vps\](-a-r-d-k for -android/com.nianticlabs.ardk.vps/index.mdx) |
| \[com.nianticlabs.ardk.wps\](-a-r-d-k for -android/com.nianticlabs.ardk.wps/index.mdx) |

</div>

</div>
