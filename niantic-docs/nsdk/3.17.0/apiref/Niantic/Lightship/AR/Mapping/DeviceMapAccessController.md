---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Mapping/DeviceMapAccessController/
title: class DeviceMapAccessController
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class DeviceMapAccessController

</div>

(Niantic.Lightship.AR.Mapping.DeviceMapAccessController)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Class to access primitive device map data and configs

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
class DeviceMapAccessController {
 public:
       // properties
    
     DeviceMapAccessController Instance;
     OutputEdgeType OutputEdgeType;

      // methods
   
     void ClearDeviceMap();
        void StartUploadingMaps();
        void StopUploadingMaps();
     void StartDownloadingMaps();
      void StopDownloadingMaps();
       void StartGettingGraphData();
     void StopGettingGraphData();
      bool MarkMapNodeForUpload(TrackableId mapId);
      bool HasMapNodeBeenUploaded(TrackableId mapId);
        void AddMapNode(byte[] dataBytes);
       void AddSubGraph(byte[] dataBytes);
      bool GetMapNodeIds(out TrackableId[] mapIds);
    
     bool GetSubGraphIds(
            out TrackableId[] subgraphIds,
            OutputEdgeType outputEdgeType = OutputEdgeType.All
       );
    
     bool GetMapNodes(TrackableId[] mapIds, out MapNode[] maps);
     bool GetSubGraphs(TrackableId[] subgraphIds, out MapSubGraph[] blobs);
  
     bool GetLatestUpdates(
          out MapNode[] mapNodes,
           out MapSubGraph[] subGraphs,
          OutputEdgeType outputEdgeType = OutputEdgeType.All
       );
    
     bool CreateAnchorFromMapNode(
           MapNode map,
            Matrix4x4 pose,
         out byte[] anchorPayload
      );
    
     bool MergeSubGraphs(
            MapSubGraph[] subgraphs,
            bool onlyKeepLatestEdges,
         out MapSubGraph mergedSubgraph
      );
    
     void ExtractMapMetaData(
            byte[] mapBlob,
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

Class to access primitive device map data and configs

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### OutputEdgeType<a href="#OutputEdgeType" class="hash-link" aria-label="Direct link to OutputEdgeType" title="Direct link to OutputEdgeType">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
OutputEdgeType OutputEdgeType
```

</div>

</div>

Specifies what type of edges will be output by [GetSubGraphs()](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Mapping/DeviceMapAccessController/#GetSubGraphs) When set, this config takes in effect immediately

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### ClearDeviceMap<a href="#ClearDeviceMap" class="hash-link" aria-label="Direct link to ClearDeviceMap" title="Direct link to ClearDeviceMap">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void ClearDeviceMap()
```

</div>

</div>

Clear map/graph node locally registered in the localizer

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### StartUploadingMaps<a href="#StartUploadingMaps" class="hash-link" aria-label="Direct link to StartUploadingMaps" title="Direct link to StartUploadingMaps">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void StartUploadingMaps()
```

</div>

</div>

Starts uploading new maps generated from this call-on

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### StopUploadingMaps<a href="#StopUploadingMaps" class="hash-link" aria-label="Direct link to StopUploadingMaps" title="Direct link to StopUploadingMaps">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void StopUploadingMaps()
```

</div>

</div>

Stops uploading maps

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### StartDownloadingMaps<a href="#StartDownloadingMaps" class="hash-link" aria-label="Direct link to StartDownloadingMaps" title="Direct link to StartDownloadingMaps">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void StartDownloadingMaps()
```

</div>

</div>

Starts downloading maps around to localize

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### StopDownloadingMaps<a href="#StopDownloadingMaps" class="hash-link" aria-label="Direct link to StopDownloadingMaps" title="Direct link to StopDownloadingMaps">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void StopDownloadingMaps()
```

</div>

</div>

Stops downloading maps

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### StartGettingGraphData<a href="#StartGettingGraphData" class="hash-link" aria-label="Direct link to StartGettingGraphData" title="Direct link to StartGettingGraphData">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void StartGettingGraphData()
```

</div>

</div>

Starts getting cloud graph

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### StopGettingGraphData<a href="#StopGettingGraphData" class="hash-link" aria-label="Direct link to StopGettingGraphData" title="Direct link to StopGettingGraphData">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void StopGettingGraphData()
```

</div>

</div>

Stops getting cloud graph

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### MarkMapNodeForUpload<a href="#MarkMapNodeForUpload" class="hash-link" aria-label="Direct link to MarkMapNodeForUpload" title="Direct link to MarkMapNodeForUpload">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool MarkMapNodeForUpload(TrackableId mapId)
```

</div>

</div>

Marks map node for upload. Downloads are triggered by StartUploadingMaps. Returns false if op fails early.

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### HasMapNodeBeenUploaded<a href="#HasMapNodeBeenUploaded" class="hash-link" aria-label="Direct link to HasMapNodeBeenUploaded" title="Direct link to HasMapNodeBeenUploaded">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool HasMapNodeBeenUploaded(TrackableId mapId)
```

</div>

</div>

Checks if map node was uploaded

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### AddMapNode<a href="#AddMapNode" class="hash-link" aria-label="Direct link to AddMapNode" title="Direct link to AddMapNode">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void AddMapNode(byte[] dataBytes)
```

</div>

</div>

Add a map node to the localizer

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

    **Parameters**:

    `dataBytes` - map node blob data as a byte array

#### AddSubGraph<a href="#AddSubGraph" class="hash-link" aria-label="Direct link to AddSubGraph" title="Direct link to AddSubGraph">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void AddSubGraph(byte[] dataBytes)
```

</div>

</div>

Add graph(s) to the localizer

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

    **Parameters**:

    `dataBytes` - graph blob data as a byte array

#### GetMapNodeIds<a href="#GetMapNodeIds" class="hash-link" aria-label="Direct link to GetMapNodeIds" title="Direct link to GetMapNodeIds">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool GetMapNodeIds(out TrackableId[] mapIds)
```

</div>

</div>

Get a list of current map nodes in the native map storage

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

    **Parameters**:

    `mapIds` - an array of map ids

    **Returns:**

    True if any ids generated. False if no map has been generated so far

#### GetSubGraphIds<a href="#GetSubGraphIds" class="hash-link" aria-label="Direct link to GetSubGraphIds" title="Direct link to GetSubGraphIds">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool GetSubGraphIds(
        out TrackableId[] subgraphIds,
        OutputEdgeType outputEdgeType = OutputEdgeType.All
   )
```

</div>

</div>

Get a list of current map nodes in the native map storage

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

    **Parameters**:

    `subgraphIds` - an array of map ids

    `outputEdgeType` - specify what type of edges will be output

    **Returns:**

    True if any ids generated. False if no map has been generated so far

#### GetMapNodes<a href="#GetMapNodes" class="hash-link" aria-label="Direct link to GetMapNodes" title="Direct link to GetMapNodes">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool GetMapNodes(TrackableId[] mapIds, out MapNode[] maps)
```

</div>

</div>

Get the map data generated

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

    **Parameters**:

    `maps` - an array of map data

    **Returns:**

    True if any maps generated. False if no map has been generated so far

#### GetSubGraphs<a href="#GetSubGraphs" class="hash-link" aria-label="Direct link to GetSubGraphs" title="Direct link to GetSubGraphs">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool GetSubGraphs(TrackableId[] subgraphIds, out MapSubGraph[] blobs)
```

</div>

</div>

Get graph data of map nodes

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

    **Parameters**:

    `blobs` - an array of graphs

    **Returns:**

    True if any graph generated. False if no graph has been generated so far

#### CreateAnchorFromMapNode<a href="#CreateAnchorFromMapNode" class="hash-link" aria-label="Direct link to CreateAnchorFromMapNode" title="Direct link to CreateAnchorFromMapNode">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool CreateAnchorFromMapNode(
       MapNode map,
        Matrix4x4 pose,
     out byte[] anchorPayload
  )
```

</div>

</div>

Generates Anchor (as payload) from MapNode

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

    **Parameters**:

    `map` - A map node, device map

    `pose` - A local pose of the anchor to create

    `anchorPayload` - anchor payload as byte array

    **Returns:**

    True if byte array representing the anchor that can be wrapped by namespace [Niantic.Lightship.AR.PersistentAnchors](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/PersistentAnchors/)

#### MergeSubGraphs<a href="#MergeSubGraphs" class="hash-link" aria-label="Direct link to MergeSubGraphs" title="Direct link to MergeSubGraphs">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool MergeSubGraphs(
        MapSubGraph[] subgraphs,
        bool onlyKeepLatestEdges,
     out MapSubGraph mergedSubgraph
  )
```

</div>

</div>

Merges Map Subgraphs

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

    **Parameters**:

    `subgraphs` - Array of subgraphs to merge

    `onlyKeepLatestEdges` - If true, it only keeps latest edge between two given nodes

    `mergedSubgraph` - Output merged subgraph

    **Returns:**

    True if merge succeeded

#### ExtractMapMetaData<a href="#ExtractMapMetaData" class="hash-link" aria-label="Direct link to ExtractMapMetaData" title="Direct link to ExtractMapMetaData">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void ExtractMapMetaData(
        byte[] mapBlob,
       out Vector3[] points,
     out float[] errors,
     out Vector3 center,
       out string mapType
    )
```

</div>

</div>

Extract map metadata from the map blob data

    **Parameters**:

    `mapBlob` - map blob data as byte array

    `points` - feature points relative to the map center

    `errors` - error of each points

    `center` - map center in the mapping coordinate system

    `mapType` - indicate type of the map data

</div>

</div>
