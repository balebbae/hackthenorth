---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mesh/-meshing-session/configure/
title: configure
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk.mesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mesh/)/[MeshingSession](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[configure](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mesh/-meshing-session/configure/)

<div>

# configure

</div>

\[androidJvm\]\
fun [configure](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mesh/-meshing-session/configure/)(config: [MeshingConfig](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-meshing-config/))

Configures the meshing feature with the specified settings.

Note: If this method is called while meshing is running, the meshing feature will restart with the new configuration, and any mesh data that has been produced will be lost.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|        |                                              |
|--------|----------------------------------------------|
| config | An object that defines the meshing behavior. |

#### See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

|  |
|----|
| [MeshingConfig](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-meshing-config/) |

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

|  |  |
|----|----|
|  | `ARDKStatusException` with code `ARDKStatus.invalidArgument` if the configuration is invalid. Check ARDK's C logs for more information. |

</div>

</div>
