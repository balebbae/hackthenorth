---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mapping/-device-mapping-session/configure/
title: configure
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk.mapping](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mapping/)/[DeviceMappingSession](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[configure](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mapping/-device-mapping-session/configure/)

<div>

# configure

</div>

\[androidJvm\]\
fun [configure](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.mapping/-device-mapping-session/configure/)(config: [DeviceMappingConfig](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-device-mapping-config/))

Configure the session with the specified settings.

Note: It is only valid to call this when the session is stopped. Note: Configuration is asynchronous and can fail later, even if this call does not throw an error. Use featureStatus() to check there are no issues.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|  |  |
|----|----|
| config | An object that defines this session's behavior. Only settings that differ from the defaults will be applied. |

#### See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

|  |
|----|
| [DeviceMappingConfig](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-device-mapping-config/) |

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

|  |  |
|----|----|
|  | `ARDKStatusException` with code `ARDKStatus.invalidArgument` if the configuration is invalid. Check ARDK's C logs for more information. |

</div>

</div>
