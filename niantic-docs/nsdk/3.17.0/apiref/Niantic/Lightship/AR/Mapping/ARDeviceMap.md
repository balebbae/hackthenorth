---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Mapping/ARDeviceMap/
title: class ARDeviceMap
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class ARDeviceMap

</div>

(Niantic.Lightship.AR.Mapping.ARDeviceMap)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

[ARDeviceMap](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Mapping/ARDeviceMap/) encapsulates device map data generated from mapping process, and provides to serialize/deserialize device map for persistent or sharing purpose.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
class ARDeviceMap {
   public:
   
     struct SerializableDeviceMap;
      struct SerializeableDeviceMapGraph;
        struct SerializeableDeviceMapNode;

     // properties
    
     List<SerializeableDeviceMapNode> DeviceMapNodes;
        SerializeableDeviceMapGraph DeviceMapGraph;
     int DefaultAnchorIndex;

       // methods
   
     ARDeviceMap();
 
     void AddDeviceMapNode(
          ulong subId1,
         ulong subId2,
         byte[] mapData,
           byte[] anchorPayload,
         string mapType
      );
    
     bool HasMapNode(TrackableId mapId);
        void SetDeviceMapGraph(byte[] graphData);
        virtual byte[] Serialize();
     byte[] GetAnchorPayload();
        bool HasValidMap();
       static ARDeviceMap CreateFromSerializedData(byte[] serializedDeviceMap);

 protected:
        // fields
    
      List<SerializeableDeviceMapNode> _deviceMapNodes = new();
         SerializeableDeviceMapGraph _deviceMapGraph = new();
      int _defaultAnchorIndex = 0;
       HashSet<TrackableId> _addedMapIds = new HashSet<TrackableId>();
   };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

[ARDeviceMap](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Mapping/ARDeviceMap/) encapsulates device map data generated from mapping process, and provides to serialize/deserialize device map for persistent or sharing purpose.

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### DeviceMapNodes<a href="#DeviceMapNodes" class="hash-link" aria-label="Direct link to DeviceMapNodes" title="Direct link to DeviceMapNodes">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
List<SerializeableDeviceMapNode> DeviceMapNodes
```

</div>

</div>

Get a list of SerializeableDeviceMapNode, either mapped on the device or deserialized

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### DeviceMapGraph<a href="#DeviceMapGraph" class="hash-link" aria-label="Direct link to DeviceMapGraph" title="Direct link to DeviceMapGraph">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
SerializeableDeviceMapGraph DeviceMapGraph
```

</div>

</div>

Get a SerializeableDeviceMapGraph in this device map

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### AddDeviceMapNode<a href="#AddDeviceMapNode" class="hash-link" aria-label="Direct link to AddDeviceMapNode" title="Direct link to AddDeviceMapNode">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void AddDeviceMapNode(
      ulong subId1,
     ulong subId2,
     byte[] mapData,
       byte[] anchorPayload,
     string mapType
  )
```

</div>

</div>

Add a device map node. This method is meant to be called by [ARDeviceMappingManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Mapping/ARDeviceMappingManager/) when a device map is generated.

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

    **Parameters**:

    `subId1` -

    `subId2` -

    `mapData` -

    `anchorPayload` -

#### HasMapNode<a href="#HasMapNode" class="hash-link" aria-label="Direct link to HasMapNode" title="Direct link to HasMapNode">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool HasMapNode(TrackableId mapId)
```

</div>

</div>

Checks if map has node by id

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

    **Parameters**:

    `mapId` -

#### SetDeviceMapGraph<a href="#SetDeviceMapGraph" class="hash-link" aria-label="Direct link to SetDeviceMapGraph" title="Direct link to SetDeviceMapGraph">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void SetDeviceMapGraph(byte[] graphData)
```

</div>

</div>

Set graph blob data. This method is meant to be called by [ARDeviceMappingManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Mapping/ARDeviceMappingManager/) when a device map and graph is generated.

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

    **Parameters**:

    `graphData` -

#### Serialize<a href="#Serialize" class="hash-link" aria-label="Direct link to Serialize" title="Direct link to Serialize">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual byte[] Serialize()
```

</div>

</div>

Get serialized device map

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

    **Returns:**

    Serailized device map as byte array

#### GetAnchorPayload<a href="#GetAnchorPayload" class="hash-link" aria-label="Direct link to GetAnchorPayload" title="Direct link to GetAnchorPayload">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
byte[] GetAnchorPayload()
```

</div>

</div>

Get the anchor payload of this device map

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

    **Returns:**

    Persistent anchor payload as byte array

#### HasValidMap<a href="#HasValidMap" class="hash-link" aria-label="Direct link to HasValidMap" title="Direct link to HasValidMap">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool HasValidMap()
```

</div>

</div>

Check if this [ARDeviceMap](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Mapping/ARDeviceMap/) has valid device map data. In case not having valid map data, this ARDviceMap should not be used for serialization

    **Returns:**

    True if it has valid device map data. Otherwise false.

#### CreateFromSerializedData<a href="#CreateFromSerializedData" class="hash-link" aria-label="Direct link to CreateFromSerializedData" title="Direct link to CreateFromSerializedData">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static ARDeviceMap CreateFromSerializedData(byte[] serializedDeviceMap)
```

</div>

</div>

Create an instance of [ARDeviceMap](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Mapping/ARDeviceMap/) from serialized device map data

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

    **Parameters**:

    `serializedDeviceMap` - Serialized device map as byte array

    **Returns:**

    An instance of [ARDeviceMap](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Mapping/ARDeviceMap/)

</div>

</div>
