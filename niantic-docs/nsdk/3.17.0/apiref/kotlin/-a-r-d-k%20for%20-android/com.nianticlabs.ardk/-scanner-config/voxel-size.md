---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/voxel-size/
title: voxel-size
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[ScannerConfig](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[voxelSize](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/voxel-size/)

<div>

# voxelSize

</div>

\[androidJvm\]\
var [voxelSize](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-scanner-config/voxel-size/): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a>

Minimum size of voxels for the voxel visualization, in meters.

This parameter controls the resolution of the voxel grid used for voxel visualization. Smaller values result in higher resolution but require more memory and computation. Larger values result in lower resolution but are more efficient. The actual voxel size may become larger due to memory constraints, so this is only a minimum value.

**Default:**`0.0f` (defaults to 0.01 m)

</div>

</div>
