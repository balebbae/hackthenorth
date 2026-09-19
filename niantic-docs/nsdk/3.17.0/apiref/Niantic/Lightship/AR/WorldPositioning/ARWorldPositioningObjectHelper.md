---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/WorldPositioning/ARWorldPositioningObjectHelper/
title: class ARWorldPositioningObjectHelper
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class ARWorldPositioningObjectHelper

</div>

(Niantic.Lightship.AR.WorldPositioning.ARWorldPositioningObjectHelper)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

[ARWorldPositioningObjectHelper](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/WorldPositioning/ARWorldPositioningObjectHelper/) provides a simple way to position objects using geographic coordinates. When an object is added it will be automatically updated as the accuracy of the WPS data improves.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class ARWorldPositioningObjectHelper: MonoBehaviour {
   public:
   
     enumAltitudeMode;

  
     class WorldPosition;

       // fields
    
      float _altitudeOffset = 0.0f;

     // methods
   
     void AddOrUpdateObject(
         GameObject gameObject,
          double latitude,
          double longitude,
         double altitude,
          Quaternion rotationXYZToEUN
       );
    
     void RemoveObject(GameObject gameObject);
      void RemoveAllObjects();
  };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

[ARWorldPositioningObjectHelper](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/WorldPositioning/ARWorldPositioningObjectHelper/) provides a simple way to position objects using geographic coordinates. When an object is added it will be automatically updated as the accuracy of the WPS data improves.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### AddOrUpdateObject<a href="#AddOrUpdateObject" class="hash-link" aria-label="Direct link to AddOrUpdateObject" title="Direct link to AddOrUpdateObject">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void AddOrUpdateObject(
     GameObject gameObject,
      double latitude,
      double longitude,
     double altitude,
      Quaternion rotationXYZToEUN
   )
```

</div>

</div>

Adds an object using a world geographic position, or updates the position if it has already been added through a previous call to this method. Updating is only rquired for dynamic objects where the world position needs to change. The object will be added to the scene and placed at the corresponding location in the unity scene. If the WPS data becomes more accurate, the object position will be automatically updated.

    **Parameters**:

    `gameObject` - The GameObject to add

    `latitude` - The latitude where the object should be placed

    `longitude` - The longitude where the object should be place

    `altitude` - The altitude where the object should be place

    `rotationXYZToEUN` - The rotation from object coordinates to world East-Up-North coordinates

#### RemoveObject<a href="#RemoveObject" class="hash-link" aria-label="Direct link to RemoveObject" title="Direct link to RemoveObject">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void RemoveObject(GameObject gameObject)
```

</div>

</div>

Removes the object from the scene and stops updating the position based on WPS data. This should only be called for objects which were previously added through a call to AddOrUpdateObject.

    **Parameters**:

    `gameObject` - The object to remove and stop updating

#### RemoveAllObjects<a href="#RemoveAllObjects" class="hash-link" aria-label="Direct link to RemoveAllObjects" title="Direct link to RemoveAllObjects">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void RemoveAllObjects()
```

</div>

</div>

Removes all objects from the scene which were previously added through a call to AddOrUpdateObject. The positions will no longer be updated using WPS data.

</div>

</div>
