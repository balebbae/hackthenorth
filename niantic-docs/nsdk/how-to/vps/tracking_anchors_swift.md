---
source: https://www.nianticspatial.com/docs/nsdk/how-to/vps/tracking_anchors_swift/
title: Localizing and Tracking Anchors with VPS
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Localizing and Tracking Anchors with VPS

</div>

Anchors are persistent spatial reference points that can be tracked across sessions and devices. The `VpsSession` is responsible for managing these anchors and correlating them with their real-world geographic locations.

## **Creating** anchors<a href="#creating-anchors" class="hash-link" aria-label="Direct link to creating-anchors" title="Direct link to creating-anchors">​</a>

The `createAnchor(at:)` method creates a persistent anchor tied to the visual features at the given location. And returns its unique `anchorId` string.

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
let anchorPose = simd_float4x4(/* your transformation matrix */)

do {
    let anchorId = try vpsSession.createAnchor(at: anchorPose)
} catch {
    print("Failed to create anchor: \(error)")
}
```

</div>

</div>

*The transformation matrix here can be assigned to any AR Content you’d want to place.*

## **Getting** anchor payloads<a href="#getting-anchor-payloads" class="hash-link" aria-label="Direct link to getting-anchor-payloads" title="Direct link to getting-anchor-payloads">​</a>

The payload encodes the data needed to localize an anchor across multiple devices or sessions, it is a string blob that can be shared or stored and is only available after the anchor has been tracked and can be obtained from:

1.  The "blob" field in the Geospatial Browser for VPS-activated locations
2.  The `anchorPayload(anchorId:)` method for user-generated anchors

<div class="theme-admonition theme-admonition-warning admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Legacy Geospatial Browser workflow

</div>

<div class="admonitionContent_BuS1">

The Geospatial Browser is no longer available. References to its anchor payload field on this page apply only to payloads already saved from older VPS projects. For current Sites, obtain the production anchor payload from Scaniverse Web or the Sites API and use VPS2.

</div>

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
if let payloadState = vpsSession.anchorPayload(anchorId: anchorId) {
    switch payloadState {
    case .inProgress:
        print("Anchor payload is being generated...")
    case .success(let payload):
        // Payload is available - base64-encoded string
        saveAnchorPayload(payload, for: anchorId)
    default:
        print("Unknown error, default result hit")
    }
} else {
    // No anchor with the given ID was found
    print("Anchor not found")
}
```

</div>

</div>

The `anchorPayload(anchorId:)` returns: An \``AnchorTrackingBound`\` representing the state of the anchor payload request:\
.`inProgress(nil)`: The anchor is not yet tracked, so the payload is not yet available.\
.`success(value)`: The request completed successfully. Contains the base64-encoded payload.\
`nil`: No anchor with id \`anchorId\` was found.

## **Tracking** existing anchors<a href="#tracking-existing-anchors" class="hash-link" aria-label="Direct link to tracking-existing-anchors" title="Direct link to tracking-existing-anchors">​</a>

In order to start localizing you’ll need to track an anchor associated to the vps location you’re trying to localize to.\
The process of localization starts with getting an anchor payload, initializing and sending frame data to the vpsSession, and then start tracking the anchor.

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
do {
    let anchorId = try vpsSession.trackAnchor(payload: anchorPayload)
} catch {
    print("Failed to track anchor: \(error)")
}
```

</div>

</div>

The `trackAnchor(payload:)` returns the unique identifier of the anchor encoded in the payload once tracking has started. Note that successfully getting the id does not mean that the localization has succeeded and for that we need to call update function.

## **Updating** anchors<a href="#updating-anchors" class="hash-link" aria-label="Direct link to updating-anchors" title="Direct link to updating-anchors">​</a>

After tracking an anchor, you’ll need to explicitly poll for updates to get the anchor's state and latest pose and make corrections to any related AR content:

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
// Poll for anchor updates every frame in your update loop
if let update = vpsSession.anchorUpdate(anchorId: anchorId) {
    switch update.trackingState {
        case .tracked:
            // Localized and succesfully tracking the anchor.
        case .notTracked:
           // Handle untracked state (e.g., hide AR content)  
        case .Limited:
            // Tracking is limited or degraded
        default:
            //Default error message, example: "Unknown error, default result hit"
    }
}
```

</div>

</div>

*The `VpsAnchorUpdate` object contains a lot of useful information, see the api reference for more information.*

## **Removing** anchors<a href="#removing-anchors" class="hash-link" aria-label="Direct link to removing-anchors" title="Direct link to removing-anchors">​</a>

Once removed, the anchor will no longer receive updates or consume processing resources.

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
if vpsSession.removeAnchor(withId: anchorId) {
    // if you are keeping local anchor references you'll need to handle those
} else {
    // Failed to remove anchor (may not exist)
}
```

</div>

</div>

This returns true if the anchor was removed, false if otherwise. Keep in mind that you’ll still need to clear content associated with the anchor.\
*Note that this call uses the anchorId and not the payload.*

# VPS Workflow:

A typical VPS workflow involves the following sequence of steps:

1.  **Initialization and Setup**

- Initialize and set up your `ardkSession`.
  - **Note:** Ensure GPS data is included within the `ArdkFrameData`.

2.  **Session Configuration and Start**

- Configure and start the `vpsSession`.

3.  **Anchor Management**

- **Load and Get Payloads:**
  - Retrieve the anchor payload blob of the location you want to localize to.
  - *(Optional)* Load anchor payload(s) from previous sessions.
- **Start Tracking:** Begin the anchor tracking process.
- **Update and Maintain:**
  - Periodically call `anchorUpdate` to check for state or position changes in the anchors.
  - Handle any detected changes.
- **Cleanup and Save:**
  - Remove any anchors that are no longer needed.
  - *(Optional)* Save any anchor payloads you want to be loaded in a subsequent session.

4.  **Finalization**

- End the session and clear all related content.

</div>

</div>
