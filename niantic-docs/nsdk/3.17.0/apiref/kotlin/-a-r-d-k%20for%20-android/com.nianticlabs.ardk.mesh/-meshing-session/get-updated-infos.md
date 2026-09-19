---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mesh/-meshing-session/get-updated-infos/
title: get-updated-infos
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk.mesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mesh/)/[MeshingSession](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[getUpdatedInfos](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mesh/-meshing-session/get-updated-infos/)

<div>

# getUpdatedInfos

</div>

\[androidJvm\]\
fun [getUpdatedInfos](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mesh/-meshing-session/get-updated-infos/)(): [MeshingUpdateInfo](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-meshing-update-info/)?

Gets the ids of all chunks in the current mesh and their update status.

The returned information contains the IDs and update status for all chunks currently in the mesh. If a chunk's updated flag is true, the mesh chunk has been updated since the last time its data was read with [getData](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mesh/-meshing-session/get-data/).

#### Return<a href="#return" class="hash-link" aria-label="Direct link to Return" title="Direct link to Return">​</a>

Information about all the updated mesh chunks if available, null if there are no chunks.

#### See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

|  |
|----|
| [MeshingSession.getData](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mesh/-meshing-session/get-data/) |
| [MeshingSession.getLastUpdateTime](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mesh/-meshing-session/get-last-update-time/) |

</div>

</div>
