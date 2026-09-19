---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Mapping/ARDeviceMappingManager/
title: class ARDeviceMappingManager
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class ARDeviceMappingManager

</div>

(Niantic.Lightship.AR.Mapping.ARDeviceMappingManager)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

[ARDeviceMappingManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Mapping/ARDeviceMappingManager/) can be used to generate device map and set the device map to track

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class ARDeviceMappingManager: MonoBehaviour {
   public:
       // properties
    
     DeviceMapAccessController DeviceMapAccessController;
        DeviceMappingController DeviceMappingController;
        ARDeviceMap ARDeviceMap;
        uint MappingTargetFrameRate;
      float MappingSplitterMaxDistanceMeters;
       float MappingSplitterMaxDurationSeconds;
      bool MapUploadEnabled;
        bool IsMappingInProgress;

     // events
    
     event DeviceMapUpdated();
        event DeviceMapFinalized();

      // methods
   
     IEnumerator RestartModuleAsyncCoroutine();
      void StartMapping();
      void StopMapping();
       void SetDeviceMap(ARDeviceMap arDeviceMap);
    
     void ExtractMapMetadata(
            out Vector3[] points,
         out float[] errors,
         out Vector3 center,
           out string mapType
        );
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

[ARDeviceMappingManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Mapping/ARDeviceMappingManager/) can be used to generate device map and set the device map to track

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### DeviceMapAccessController<a href="#DeviceMapAccessController" class="hash-link" aria-label="Direct link to DeviceMapAccessController" title="Direct link to DeviceMapAccessController">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
DeviceMapAccessController DeviceMapAccessController
```

</div>

</div>

Get [DeviceMapAccessController](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Mapping/DeviceMapAccessController/), which provides primitive access to the device map and related info

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### DeviceMappingController<a href="#DeviceMappingController" class="hash-link" aria-label="Direct link to DeviceMappingController" title="Direct link to DeviceMappingController">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
DeviceMappingController DeviceMappingController
```

</div>

</div>

Get [DeviceMappingController](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Mapping/DeviceMappingController/), which provides primitive API for device mapping

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### ARDeviceMap<a href="#ARDeviceMap" class="hash-link" aria-label="Direct link to ARDeviceMap" title="Direct link to ARDeviceMap">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
ARDeviceMap ARDeviceMap
```

</div>

</div>

Get the [ARDeviceMap](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Mapping/ARDeviceMap/) object in this manager

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### MappingTargetFrameRate<a href="#MappingTargetFrameRate" class="hash-link" aria-label="Direct link to MappingTargetFrameRate" title="Direct link to MappingTargetFrameRate">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
uint MappingTargetFrameRate
```

</div>

</div>

Property access for mapping speed

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### MappingSplitterMaxDistanceMeters<a href="#MappingSplitterMaxDistanceMeters" class="hash-link" aria-label="Direct link to MappingSplitterMaxDistanceMeters" title="Direct link to MappingSplitterMaxDistanceMeters">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float MappingSplitterMaxDistanceMeters
```

</div>

</div>

Property access for map splitting criteria by distance

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### MappingSplitterMaxDurationSeconds<a href="#MappingSplitterMaxDurationSeconds" class="hash-link" aria-label="Direct link to MappingSplitterMaxDurationSeconds" title="Direct link to MappingSplitterMaxDurationSeconds">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float MappingSplitterMaxDurationSeconds
```

</div>

</div>

Property access for map splitting criteria by time

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### MapUploadEnabled<a href="#MapUploadEnabled" class="hash-link" aria-label="Direct link to MapUploadEnabled" title="Direct link to MapUploadEnabled">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool MapUploadEnabled
```

</div>

</div>

Property access for whether map upload will be enabled during mapping Set this property before [StartMapping()](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Mapping/ARDeviceMappingManager/#StartMapping)

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### IsMappingInProgress<a href="#IsMappingInProgress" class="hash-link" aria-label="Direct link to IsMappingInProgress" title="Direct link to IsMappingInProgress">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool IsMappingInProgress
```

</div>

</div>

A state if mapping is in progress or not. True is mapping is ongoing. Becomes false after calling [StopMapping()](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Mapping/ARDeviceMappingManager/#StopMapping)

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

### Events<a href="#events" class="hash-link" aria-label="Direct link to Events" title="Direct link to Events">​</a>

#### DeviceMapUpdated<a href="#DeviceMapUpdated" class="hash-link" aria-label="Direct link to DeviceMapUpdated" title="Direct link to DeviceMapUpdated">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
event DeviceMapUpdated()
```

</div>

</div>

An event when device map data has been updated

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### DeviceMapFinalized<a href="#DeviceMapFinalized" class="hash-link" aria-label="Direct link to DeviceMapFinalized" title="Direct link to DeviceMapFinalized">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
event DeviceMapFinalized()
```

</div>

</div>

An event when device map is finalized and ready to save

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### RestartModuleAsyncCoroutine<a href="#RestartModuleAsyncCoroutine" class="hash-link" aria-label="Direct link to RestartModuleAsyncCoroutine" title="Direct link to RestartModuleAsyncCoroutine">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
IEnumerator RestartModuleAsyncCoroutine()
```

</div>

</div>

Asynchronously restarts the underlying module with the current configuration.

#### StartMapping<a href="#StartMapping" class="hash-link" aria-label="Direct link to StartMapping" title="Direct link to StartMapping">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void StartMapping()
```

</div>

</div>

Start map generation

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### StopMapping<a href="#StopMapping" class="hash-link" aria-label="Direct link to StopMapping" title="Direct link to StopMapping">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void StopMapping()
```

</div>

</div>

Stop map generation

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### SetDeviceMap<a href="#SetDeviceMap" class="hash-link" aria-label="Direct link to SetDeviceMap" title="Direct link to SetDeviceMap">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void SetDeviceMap(ARDeviceMap arDeviceMap)
```

</div>

</div>

Set a Device Map to track. Use when loading a serialized device map and track it.

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

    **Parameters**:

    `arDeviceMap` - [ARDeviceMap](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Mapping/ARDeviceMap/) to track

#### ExtractMapMetadata<a href="#ExtractMapMetadata" class="hash-link" aria-label="Direct link to ExtractMapMetadata" title="Direct link to ExtractMapMetadata">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void ExtractMapMetadata(
        out Vector3[] points,
     out float[] errors,
     out Vector3 center,
       out string mapType
    )
```

</div>

</div>

Extract map metadata from the currently set device map. Could be used for debugging and/or visual user feedback where map is

    **Parameters**:

    `points` - feature points coordinates relative to the anchor/map center

    `errors` - estimated errors of each points. Smaller error points could be more significant feature points

    `center` - center point coordinates in the mapped coordinate system

</div>

</div>
