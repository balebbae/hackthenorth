---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/enums/VpsAnchorUpdate.AnchorTrackingStateReason/
title: VpsAnchorUpdate.AnchorTrackingStateReason
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**ENUM**

<div>

# `VpsAnchorUpdate.AnchorTrackingStateReason`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
enum AnchorTrackingStateReason
```

</div>

</div>

Provides additional context about why an anchor is in a particular tracking state.

When an anchor is not tracked or has limited tracking, this enum provides specific reasons that can help developers understand and respond to tracking issues.

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Tracking state reasons help diagnose why tracking may be failing or limited, enabling applications to provide appropriate user feedback or take corrective actions.

## Example Usage<a href="#example-usage" class="hash-link" aria-label="Direct link to Example Usage" title="Direct link to Example Usage">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
let (status, update) = vpsSession.getAnchorUpdate(anchorId: anchorId)
if status.isOk() {
    switch update.trackingStateReason {
    case .initializing:
        print("Anchor is still initializing - tracking will improve")
    case .permissionDenied:
        print("Tracking failed due to permission issues")
    case .fatalNetworkError:
        print("Network error preventing tracking")
    default:
        print("Other tracking issue: \(update.trackingStateReason)")
    }
}
```

</div>

</div>

## Cases<a href="#cases" class="hash-link" aria-label="Direct link to Cases" title="Direct link to Cases">​</a>

### `none`<a href="#none" class="hash-link" aria-label="Direct link to none" title="Direct link to none">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case none
```

</div>

</div>

No specific reason for the current tracking state.

This is the default state when tracking is working normally or when no specific reason has been identified for tracking issues.

### `initializing`<a href="#initializing" class="hash-link" aria-label="Direct link to initializing" title="Direct link to initializing">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case initializing
```

</div>

</div>

The anchor is currently initializing and tracking will improve.

This reason indicates that the system is still processing the anchor's visual features and tracking quality should improve over time.

### `removed`<a href="#removed" class="hash-link" aria-label="Direct link to removed" title="Direct link to removed">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case removed
```

</div>

</div>

The anchor has been explicitly removed from tracking.

This reason indicates that the anchor was removed via `removeAnchor(withId:)` and is no longer being tracked by the system.

### `internalError`<a href="#internalerror" class="hash-link" aria-label="Direct link to internalerror" title="Direct link to internalerror">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case internalError
```

</div>

</div>

An internal error occurred within the tracking system.

This reason indicates a system-level error that prevented normal tracking. The application should check the VPS feature status for more details.

### `permissionDenied`<a href="#permissiondenied" class="hash-link" aria-label="Direct link to permissiondenied" title="Direct link to permissiondenied">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case permissionDenied
```

</div>

</div>

Tracking failed due to insufficient permissions.

This reason indicates that the anchor target requested is not accessible by the current authenticated user. Check that the API key or authentication token has the necessary permissions and organization access.

### `fatalNetworkError`<a href="#fatalnetworkerror" class="hash-link" aria-label="Direct link to fatalnetworkerror" title="Direct link to fatalnetworkerror">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case fatalNetworkError
```

</div>

</div>

A fatal network error prevented tracking.

This reason indicates that network connectivity issues are preventing the VPS system from functioning properly.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `isError`<a href="#iserror" class="hash-link" aria-label="Direct link to iserror" title="Direct link to iserror">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var isError: Bool
```

</div>

</div>

</div>

</div>
