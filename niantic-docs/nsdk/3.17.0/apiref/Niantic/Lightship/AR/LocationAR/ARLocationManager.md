---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/LocationAR/ARLocationManager/
title: class ARLocationManager
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class ARLocationManager

</div>

(Niantic.Lightship.AR.LocationAR.ARLocationManager)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

The [ARLocationManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/LocationAR/ARLocationManager/) is used to track ARLocations. ARLocations tie digital content to the physical world. When you start tracking an [ARLocation](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/LocationAR/ARLocation/), and aim your phone's camera at the physical location, the digital content that you child to the [ARLocation](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/LocationAR/ARLocation/) will appear in the physical world.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class ARLocationManager: Niantic.Lightship.AR.PersistentAnchors.ARPersistentAnchorManager {
 public:
       // fields
    
      ARLocation[] ARLocations => GetComponentsInChildren<ARLocation>(true);
       bool AutoTrack => _autoTrack;

      // properties
    
     int MaxLocationTrackingCount;

     // events
    
     event locationTrackingStateChanged();

        // methods
   
     void SetARLocations(params ARLocation[] arLocations);
        void StartTracking();
     void StopTracking();
      void TryUpdateTracking();

 protected:
        // methods
   
     override void OnEnable();
       virtual override void Start();
        override void OnDisable();
  };
```

</div>

</div>

## Inherited Members<a href="#inherited-members" class="hash-link" aria-label="Direct link to Inherited Members" title="Direct link to Inherited Members">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
public:
   // properties

    float InterpolationTimeSeconds;
   bool ContinuousLocalizationEnabled;
   bool InterpolationEnabled;
    bool TemporalFusionEnabled;
   int JpegCompressionQuality;
   bool TransformUpdateSmoothingEnabled;
 float InitialServiceRequestIntervalSeconds;
   float ContinuousServiceRequestIntervalSeconds;
    bool DiagnosticsEnabled;
  bool VpsDebuggerEnabled;
  bool GpsCorrectionForContinuousLocalization;
  float DeviceMappingLocalizationRequestIntervalSeconds;
    bool CloudLocalizationEnabled;
    bool DeviceMappingLocalizationEnabled;
    DeviceMappingType DeviceMappingType;
    bool DeviceMapDownloadEnabled;

    // events

    event arPersistentAnchorStateChanged();
  event DebugInfoUpdated();
    event VpsDebuggerEvent();

    // methods

   VpsGraphOperationError TryGetDevicePoseAsGeolocation(
     Pose pose,
      out double latitude,
        out double longitude,
       out double altitude,
        out double verticalAccuracy,
        out double horizontalAccuracy,
      out double heading
    );

    async Task RestartSubsystemAsync();
   IEnumerator RestartSubsystemAsyncCoroutine();
   bool GetVpsSessionId(out string vpsSessionId);

 bool TryCreateAnchor(
       Pose anchorLocalPose,
       out ARPersistentAnchor arPersistentAnchor
   );

    bool TryTrackAnchor(
        ARPersistentAnchorPayload payload,
      out ARPersistentAnchor arPersistentAnchor
   );

    void DestroyAnchor(ARPersistentAnchor arPersistentAnchor);
```

</div>

</div>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
protected:
    // fields

     override string gameObjectName => "Persistent Anchor";

 // methods

   override GameObject GetPrefab();
  override void OnEnable();
   override void OnBeforeStart();
  virtual void Start();
   override void OnDisable();
  override void OnDestroy();

  override void OnTrackablesChanged(
        List<ARPersistentAnchor> added,
     List<ARPersistentAnchor> updated,
       List<ARPersistentAnchor> removed
  );
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

The [ARLocationManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/LocationAR/ARLocationManager/) is used to track ARLocations. ARLocations tie digital content to the physical world. When you start tracking an [ARLocation](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/LocationAR/ARLocation/), and aim your phone's camera at the physical location, the digital content that you child to the [ARLocation](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/LocationAR/ARLocation/) will appear in the physical world.

### Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

#### ARLocations<a href="#ARLocations" class="hash-link" aria-label="Direct link to ARLocations" title="Direct link to ARLocations">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
ARLocation[] ARLocations => GetComponentsInChildren<ARLocation>(true)
```

</div>

</div>

Gets all of the ARLocations childed to the [ARLocationManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/LocationAR/ARLocationManager/).

#### AutoTrack<a href="#AutoTrack" class="hash-link" aria-label="Direct link to AutoTrack" title="Direct link to AutoTrack">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool AutoTrack => _autoTrack
```

</div>

</div>

Whether or not to automatically start tracking the selected [ARLocation](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/LocationAR/ARLocation/). If true, the location that is currently enabled will be automatically tracked on Start.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### MaxLocationTrackingCount<a href="#MaxLocationTrackingCount" class="hash-link" aria-label="Direct link to MaxLocationTrackingCount" title="Direct link to MaxLocationTrackingCount">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
int MaxLocationTrackingCount
```

</div>

</div>

Maximum number of locations that will be tracked by StartTracking. MaxLocationTrackingCount is always 1. Future versions of [ARDK](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/ARDK/) may support tracking more than one location at a time, but currently only one location at a time can be tracked.

### Events<a href="#events" class="hash-link" aria-label="Direct link to Events" title="Direct link to Events">​</a>

#### locationTrackingStateChanged<a href="#locationTrackingStateChanged" class="hash-link" aria-label="Direct link to locationTrackingStateChanged" title="Direct link to locationTrackingStateChanged">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
event locationTrackingStateChanged()
```

</div>

</div>

Called when the location tracking state has changed.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### SetARLocations<a href="#SetARLocations" class="hash-link" aria-label="Direct link to SetARLocations" title="Direct link to SetARLocations">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void SetARLocations(params ARLocation[] arLocations)
```

</div>

</div>

Selects the [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) Locations to try to track when [StartTracking()](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/LocationAR/ARLocationManager/#StartTracking) is called. At most one of these locations will actually be tracked.

    **Parameters**:

    `arLocations` - The locations to try to track.

#### StartTracking<a href="#StartTracking" class="hash-link" aria-label="Direct link to StartTracking" title="Direct link to StartTracking">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void StartTracking()
```

</div>

</div>

Starts tracking locations specified by [SetARLocations()](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/LocationAR/ARLocationManager/#SetARLocations).

Currently only one location can be tracked at a time. In the future, the number of locations tracked will be limited to MaxAnchorTrackingCount.

Content authored as children of the [ARLocation](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/LocationAR/ARLocation/) will be enabled once the [ARLocation](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/LocationAR/ARLocation/) becomes tracked. This will create digital content in the physical world.

If no locations were specified in [SetARLocations()](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/LocationAR/ARLocationManager/#SetARLocations), requests will be made to attempt to track nearby locations. In this case, multiple nearby locations may be targeted and the first one to successfully track will be used.

#### StopTracking<a href="#StopTracking" class="hash-link" aria-label="Direct link to StopTracking" title="Direct link to StopTracking">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void StopTracking()
```

</div>

</div>

Stops tracking the currently tracked location. This must be called before switching to a new location.

.. note::

Anchors are destroyed asynchronously, so there needs to be a small delay after calling [StopTracking()](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/LocationAR/ARLocationManager/#StopTracking) before calling [StartTracking()](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/LocationAR/ARLocationManager/#StartTracking).

#### TryUpdateTracking<a href="#TryUpdateTracking" class="hash-link" aria-label="Direct link to TryUpdateTracking" title="Direct link to TryUpdateTracking">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void TryUpdateTracking()
```

</div>

</div>

Tries to refresh the tracking of the currently tracked anchors.

</div>

</div>
