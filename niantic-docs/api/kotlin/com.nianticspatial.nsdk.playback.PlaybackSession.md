---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackSession/
title: PlaybackSession
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.playback](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback/ "com.nianticspatial.nsdk.playback") 

</div>

<div class="api-title">

#  PlaybackSession

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">PlaybackSession</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Runs a timed loop over a \[PlaybackDataset\], loading one frame per tick and notifying a listener. Use \[play\] to begin playback and \[pause\] to stop; the loop wraps to frame 0 at end. Call \[setOnFrameListener\] before \[play\] to receive each \[PlaybackFrame\]; the listener may be invoked from a background thread (post to main in the sample if needed).

------------------------------------------------------------------------

## Functions<a href="#functions" class="hash-link" aria-label="Direct link to Functions" title="Direct link to Functions">​</a>

<table class="api-table">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr class="api-table-row">
<td><span id="function-clearonframelistener"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackSession.clearOnFrameListener/" title="Clears the frame listener.">clearOnFrameListener</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Clears the frame listener.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-currentframeindex"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackSession.currentFrameIndex/" title="Current frame index (0 until [dataset][PlaybackDataset].frameCount).">currentFrameIndex</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment">
Current frame index (0 until [dataset][PlaybackDataset].frameCount).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-currentplaybackframe"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackSession.currentPlaybackFrame/" title="Last frame delivered to the listener; null before any frame or after [pause].">currentPlaybackFrame</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackFrame/" title="One frame of playback: metadata, camera representation, optional image and depth....">PlaybackFrame</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Last frame delivered to the listener; null before any frame or after [pause].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-dispose"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackSession.dispose/" title="Stops playback and releases all held references. Call from the owning component&#39;s teardown...">dispose</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Stops playback and releases all held references. Call from the owning component's teardown<br />
(e.g. [androidx.lifecycle.ViewModel.onCleared] or [android.app.Activity.onDestroy]) to<br />
prevent the listener lambda from retaining a reference to a destroyed component.<br />
After dispose, this session should not be reused.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-hasdepth"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackSession.hasDepth/" title="Delegates to [PlaybackDataset.hasDepth].">hasDepth</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Boolean</a></span></span></td>
<td><div class="ctoken comment">
Delegates to [PlaybackDataset.hasDepth].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-isplaying"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackSession.isPlaying/" title="True when the session has been started and not yet paused.">isPlaying</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Boolean</a></span></span></td>
<td><div class="ctoken comment">
True when the session has been started and not yet paused.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-pause"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackSession.pause/" title="Stops the playback loop. Current index is preserved so [play] resumes from the next frame.">pause</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Stops the playback loop. Current index is preserved so [play] resumes from the next frame.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-play"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackSession.play/" title="Starts the playback loop on a background thread. Delivers frames every [PlaybackDataset.frameInterval] seconds;...">play</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Starts the playback loop on a background thread. Delivers frames every [PlaybackDataset.frameInterval] seconds;<br />
at end of dataset wraps to index 0. No-op if already playing.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-seektostart"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackSession.seekToStart/" title="Resets playback to the first frame. Call before [play] to begin from the beginning; safe to call while paused.">seekToStart</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Resets playback to the first frame. Call before [play] to begin from the beginning; safe to call while paused.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-setonframelistener"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackSession.setOnFrameListener/" title="Sets the callback invoked for each loaded frame. Call before [play].">setOnFrameListener</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Sets the callback invoked for each loaded frame. Call before [play].
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
