---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/WorldPositioning/ARWorldPositioningManager/
title: class ARWorldPositioningManager
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class ARWorldPositioningManager

</div>

(Niantic.Lightship.AR.WorldPositioning.ARWorldPositioningManager)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

The [ARWorldPositioningManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/WorldPositioning/ARWorldPositioningManager/) class controls the XRWorldPositioningSubsystem and provides access to the underlying [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) to world transform from the World Positioning System (WPS).

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class ARWorldPositioningManager: SubsystemLifecycleManager< XRWorldPositioningSubsystem, XRWorldPositioningSubsystemDescriptor, XRWorldPositioningSubsystem.Provider > {
    public:
       // fields
    
      bool IsAvailable => Status == WorldPositioningStatus.Available;
        Action<WorldPositioningStatus> OnStatusChanged;

        // properties
    
     ARWorldPositioningTangentialTransform WorldTransform;
       int??? Framerate;
     bool??? Smoothing;
        bool??? BevEnabled;
       int??? BevFramerate;
      WorldPositioningStatus? Status;
     ARWorldPositioningCameraHelper DefaultCameraHelper;

     // methods
   
     void Update();
    
     WorldPositioningStatus TryGetXRToWorld(
           ref Matrix4x4 arToWorld,
          ref double originLatitude,
          ref double originLongitude,
         ref double originAltitude
     );
    
     void OverrideTransform(ARWorldPositioningTangentialTransform simulatedTransform);
      void EndOverride();

   protected:
        // methods
   
     override void OnDisable();
  };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

The [ARWorldPositioningManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/WorldPositioning/ARWorldPositioningManager/) class controls the XRWorldPositioningSubsystem and provides access to the underlying [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) to world transform from the World Positioning System (WPS).

It is unlikely that an application will need to use the value of WorldTransform directly. For applications requiring only a more accurate/stable version of GPS & compass, the properties on DefaultCameraHelper can be accessed to obtain Latitude, Longitude and Heading values which work similarly to those available through location services.

The transform can also be used to place objects into the [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) View using geographic coordinates. WorldPositioningPositioningHelper provides a more convenient interface for adding objects to the scene and updating their positions as WPS data becomes more accurate.

### Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

#### IsAvailable<a href="#IsAvailable" class="hash-link" aria-label="Direct link to IsAvailable" title="Direct link to IsAvailable">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool IsAvailable => Status == WorldPositioningStatus.Available
```

</div>

</div>

Returns true if World Positioning is available.

#### OnStatusChanged<a href="#OnStatusChanged" class="hash-link" aria-label="Direct link to OnStatusChanged" title="Direct link to OnStatusChanged">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Action<WorldPositioningStatus> OnStatusChanged
```

</div>

</div>

Action that is called when the status changes

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### WorldTransform<a href="#WorldTransform" class="hash-link" aria-label="Direct link to WorldTransform" title="Direct link to WorldTransform">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
ARWorldPositioningTangentialTransform WorldTransform
```

</div>

</div>

The current estimate of the transform between the [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) tracking coordinates and the world geographic coordinate system. This property should only be used when the Status property is Available, otherwise it is undefined.

#### Framerate<a href="#Framerate" class="hash-link" aria-label="Direct link to Framerate" title="Direct link to Framerate">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
int??? Framerate
```

</div>

</div>

Framerate for measurement updates

#### Smoothing<a href="#Smoothing" class="hash-link" aria-label="Direct link to Smoothing" title="Direct link to Smoothing">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool??? Smoothing
```

</div>

</div>

Enable smoothing for World Positioning

#### BevEnabled<a href="#BevEnabled" class="hash-link" aria-label="Direct link to BevEnabled" title="Direct link to BevEnabled">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool??? BevEnabled
```

</div>

</div>

Enable BEV (Bird's Eye View) queries

#### BevFramerate<a href="#BevFramerate" class="hash-link" aria-label="Direct link to BevFramerate" title="Direct link to BevFramerate">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
int??? BevFramerate
```

</div>

</div>

Framerate for BEV queries

#### Status<a href="#Status" class="hash-link" aria-label="Direct link to Status" title="Direct link to Status">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
WorldPositioningStatus? Status
```

</div>

</div>

The Status of the WorldTransform estimate. The WorldTransform is only valid when Status is Available.

#### DefaultCameraHelper<a href="#DefaultCameraHelper" class="hash-link" aria-label="Direct link to DefaultCameraHelper" title="Direct link to DefaultCameraHelper">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
ARWorldPositioningCameraHelper DefaultCameraHelper
```

</div>

</div>

A [ARWorldPositioningCameraHelper](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/WorldPositioning/ARWorldPositioningCameraHelper/) which is automatically generated for the default [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) camera

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### OverrideTransform<a href="#OverrideTransform" class="hash-link" aria-label="Direct link to OverrideTransform" title="Direct link to OverrideTransform">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void OverrideTransform(ARWorldPositioningTangentialTransform simulatedTransform)
```

</div>

</div>

Overrides the World Positioning transform with the value specified. This method allows the developer to simulate different locations. The [ARWorldPositioningEditorControls](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/WorldPositioning/ARWorldPositioningEditorControls/) class can be used to simulate different locations in the Unity editor.

#### EndOverride<a href="#EndOverride" class="hash-link" aria-label="Direct link to EndOverride" title="Direct link to EndOverride">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void EndOverride()
```

</div>

</div>

Stops overriding the World Positioning transform. Use this to switch back to the real transform (on a device) or playback (in the Unity editor)

</div>

</div>
