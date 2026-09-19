---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.awareness.semantics/-semantics-session/latest-packed-channel/
title: latest-packed-channel
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk.awareness.semantics](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.awareness.semantics/)/[SemanticsSession](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[latestPackedChannel](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.awareness.semantics/-semantics-session/latest-packed-channel/)

<div>

# latestPackedChannel

</div>

\[androidJvm\]\
fun [latestPackedChannel](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.awareness.semantics/-semantics-session/latest-packed-channel/)(): [ARDKResult](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-a-r-d-k-result/)\<[SemanticsResult](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.awareness.semantics/-semantics-result/), [AwarenessStatus](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-awareness-status/)\>

Gets the latest packed channel semantics data.

This retrieves the most recent packed channel data for semantic classification of the current frame.

#### Return<a href="#return" class="hash-link" aria-label="Direct link to Return" title="Direct link to Return">​</a>

ARDKResult containing packed channel data if successful, or error information

#### See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

|  |
|----|
| [SemanticsSession.channelNames](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.awareness.semantics/-semantics-session/channel-names/) |
| [SemanticsSession.latestConfidence](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.awareness.semantics/-semantics-session/latest-confidence/) |
| [SemanticsSession.latestSuppressionMask](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.awareness.semantics/-semantics-session/latest-suppression-mask/) |

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

|  |  |
|----|----|
| [ArdkStatusException](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-ardk-status-exception/) | if there was an internal error |

</div>

</div>
