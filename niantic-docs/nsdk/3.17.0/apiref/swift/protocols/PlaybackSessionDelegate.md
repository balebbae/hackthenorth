---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/protocols/PlaybackSessionDelegate/
title: PlaybackSessionDelegate
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**PROTOCOL**

<div>

# `PlaybackSessionDelegate`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public protocol PlaybackSessionDelegate
```

</div>

</div>

Delegate protocol for receiving frame updates during playback.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `session(_:didUpdate:image:)`<a href="#session_didupdateimage" class="hash-link" aria-label="Direct link to session_didupdateimage" title="Direct link to session_didupdateimage">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
func session(_ session: PlaybackSession, didUpdate frame: PlaybackDataset.FrameMetadata, image: CGImage?)
```

</div>

</div>

Called each time a new frame is ready during playback.

This method is called on the playback queue, so any UI updates should be dispatched to the main queue.

- Parameters:
  - session: The playback session that generated the update
  - frame: The metadata for the current frame
  - image: The CGImage for the current frame, or nil if unavailable

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name    | Description                                              |
|---------|----------------------------------------------------------|
| session | The playback session that generated the update           |
| frame   | The metadata for the current frame                       |
| image   | The CGImage for the current frame, or nil if unavailable |

</div>

</div>
