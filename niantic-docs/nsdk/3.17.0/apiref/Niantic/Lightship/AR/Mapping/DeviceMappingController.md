---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Mapping/DeviceMappingController/
title: class DeviceMappingController
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class DeviceMappingController

</div>

(Niantic.Lightship.AR.Mapping.DeviceMappingController)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Class for rimitive Device mapping operations and configs

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
class DeviceMappingController {
   public:
       // properties
    
     bool TrackingEdgesEnabled;
        DeviceMappingType DeviceMappingType;
        uint TargetFrameRate;
     float SplitterMaxDistanceMeters;
      float SplitterMaxDurationSeconds;
     bool IsMapping;

       // methods
   
     void StartMapping();
      void StopMapping();
   };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Class for rimitive Device mapping operations and configs

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### TrackingEdgesEnabled<a href="#TrackingEdgesEnabled" class="hash-link" aria-label="Direct link to TrackingEdgesEnabled" title="Direct link to TrackingEdgesEnabled">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool TrackingEdgesEnabled
```

</div>

</div>

Config to enable/disable creation of tracking edges during mapping

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### DeviceMappingType<a href="#DeviceMappingType" class="hash-link" aria-label="Direct link to DeviceMappingType" title="Direct link to DeviceMappingType">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
DeviceMappingType DeviceMappingType
```

</div>

</div>

Config to enable/disable use of learned features during mapping

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### TargetFrameRate<a href="#TargetFrameRate" class="hash-link" aria-label="Direct link to TargetFrameRate" title="Direct link to TargetFrameRate">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
uint TargetFrameRate
```

</div>

</div>

Target Framerate to run Mappers. The 0 value indicates maximun framerate

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### SplitterMaxDistanceMeters<a href="#SplitterMaxDistanceMeters" class="hash-link" aria-label="Direct link to SplitterMaxDistanceMeters" title="Direct link to SplitterMaxDistanceMeters">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float SplitterMaxDistanceMeters
```

</div>

</div>

Node Splitter config for Max Distantance Travelled before creating a new map node

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### SplitterMaxDurationSeconds<a href="#SplitterMaxDurationSeconds" class="hash-link" aria-label="Direct link to SplitterMaxDurationSeconds" title="Direct link to SplitterMaxDurationSeconds">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float SplitterMaxDurationSeconds
```

</div>

</div>

Node Splitter config for Max Duration Exceeded before creating a new map node

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### IsMapping<a href="#IsMapping" class="hash-link" aria-label="Direct link to IsMapping" title="Direct link to IsMapping">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool IsMapping
```

</div>

</div>

Status if running mapping or not

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

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

</div>

</div>
