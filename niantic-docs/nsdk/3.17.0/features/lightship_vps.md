---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/features/lightship_vps/
title: Visual Positioning System (VPS)
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="theme-admonition theme-admonition-warning admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>warning

</div>

<div class="admonitionContent_BuS1">

The Geospatial Browser (GSB), previously used to search and activate VPS locations, has been retired.

Existing applications that already use GSB-based POIs will continue to function. However, it is no longer possible to create new experiences using public POIs from the GSB.

To build new VPS 2.0 experiences, you must scan your own locations using Scaniverse and upgrade to NSDK 4.0.

</div>

</div>

<div>

# Niantic Spatial VPS

</div>

With Niantic Spatial’s Visual Positioning System (VPS) you now have the power to determine a user’s position and orientation with centimeter-level accuracy - in seconds. You can use VPS to create location-based AR experiences that connect the real world with the digital one. Content can be anchored to these locations so they can persist over AR sessions. VPS makes augmented reality feel more relevant to the communities that live within these locations and gives users new reasons to explore the world around them.

## What is VPS?<a href="#what-is-vps" class="hash-link" aria-label="Direct link to What is VPS?" title="Direct link to What is VPS?">​</a>

Niantic Spatial's Visual Positioning System (VPS) is a cloud-based system that allows devices to know where they are relative to Niantic Spatial’s map. By determining the six-degrees-of-freedom pose of a device relative to the map, you can place persistent virtual objects that stay aligned with the real world.

## The VPS Map<a href="#the-vps-map" class="hash-link" aria-label="Direct link to The VPS Map" title="Direct link to The VPS Map">​</a>

The Niantic Spatial VPS map is built using scans submitted by users and is organized by the coverage of the locations in the scans. When enough scans have been submitted for a location, the location becomes "VPS-Activated".

Once enough scans of an area are collected, they are processed to create a map. Connected nodes on that mapped area form spaces, and each of those contribute to a VPS-Activated Location. The highest quality space is used as the default space for that VPS-Activated Location. The default space contains a default anchor, which is provided by the VPS Coverage API as part of the LocalizationTarget. Locations downloaded from the Geospatial Browser contain the mesh and anchor data that can be loaded into your project.

## Anchors<a href="#anchors" class="hash-link" aria-label="Direct link to Anchors" title="Direct link to Anchors">​</a>

Each anchor represents a stable point and orientation in the real world. Anchors can be stored as a payload and resolved across sessions to create persistent virtual objects.

## The Localization Process<a href="#the-localization-process" class="hash-link" aria-label="Direct link to The Localization Process" title="Direct link to The Localization Process">​</a>

Localization is the process of resolving an anchor's position and orientation in a device's local tracking coordinate system. To localize, the user needs to point their device at the real-world location associated with that anchor. The Niantic Spatial SDK then sends the camera frames to the cloud and looks for a match. (If users are having trouble, the VPS Coverage API provides a field to add a hint image for them to look for.)

Because device local tracking is inexact, anchor positions can drift after localizing. To combat this, the SDK offers Location Drift Mitigation features that use a variety of techniques to recompute the correct anchor position.

There are a number of other factors that can also impact localization quality. Moving too fast, darkness or fog, dirty camera lenses, and poor internet connection can all impact the speed and quality of localization. If local tracking fails or jumps suddenly to another place, the anchor will become "Untracked" and the user will need to localize again.

## Creating Location AR Experiences with VPS<a href="#creating-location-ar-experiences-with-vps" class="hash-link" aria-label="Direct link to Creating Location AR Experiences with VPS" title="Direct link to Creating Location AR Experiences with VPS">​</a>

### VPS currently provides these features:<a href="#vps-currently-provides-these-features" class="hash-link" aria-label="Direct link to VPS currently provides these features:" title="Direct link to VPS currently provides these features:">​</a>

- Public Locations are unique or notable, publicly accessible, real-world locations that are VPS-Activated and apps can engage with.
- The VPS Coverage API which lets you discover Public Locations that are VPS-Activated.
- VPS Coverage Areas are geographic regions where users can localize with VPS and show the area around a Public Location where users can localize.
- VPS Localization Targets are real-world images of Public Locations that users can track with their device to localize.
- The Geospatial Browser (Beta) allows you to search, nominate, and find Public Locations across the globe. You can select the location you want to use for your project and [download the associated 3D mesh assets](#downloading-the-3d-mesh-asset-of-a-vps-location).
- Test Scans are VPS locations in your surrounding area to test with using the Niantic App.

### We also provides the following to help you develop your VPS-enabled AR experience:<a href="#we-also-provides-the-following-to-help-you-develop-your-vps-enabled-ar-experience" class="hash-link" aria-label="Direct link to We also provides the following to help you develop your VPS-enabled AR experience:" title="Direct link to We also provides the following to help you develop your VPS-enabled AR experience:">​</a>

The Niantic Scaniverse App allows you to capture and submit scans at Public Locations to improve the coverage of Lightship VPS. You can also use the app to create Private VPS Locations for your own rapid testing and development. Finally, the Scaniverse App can be used to test localization at Public Locations and Private VPS Locations.

A VPS developer portal on lightship.dev that lets you visualize Public Locations and manage Private VPS Locations. Niantic Spatial VPS APIs make requests to the VPS backend, which needs to receive user information such as user location and an ID unique to the user using your app to make the requests. To facilitate this, ARDK provides a User ID data element that’s automatically used in Lightship VPS requests. This User ID is considered private user data, and your app will need to provide privacy policies and guidance for handling private user data, as described in ARDK and Data Privacy.

## Downloading the 3D Mesh Asset of a VPS Location<a href="#downloading-the-3d-mesh-asset-of-a-vps-location" class="hash-link" aria-label="Direct link to Downloading the 3D Mesh Asset of a VPS Location" title="Direct link to Downloading the 3D Mesh Asset of a VPS Location">​</a>

With the Mesh Download API, you can download and create a mesh of any Public Location at runtime, allowing you to dynamically create mesh overlays in AR scenes. This feature makes it easier to test AR experiences by allowing you to check that your mesh lines up with the real world without having to leave the test environment. For example, you can download a stored mesh after localizing to see how far offset your localization is and figure out how it needs to change. Mesh downloading also allows developers to place content in scenes and explore environmental interactions without needing to stop testing and set up each mesh they want to try.

To learn how to do this, see the [Mesh Download How-To](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/mesh_download/).

## Next Steps<a href="#next-steps" class="hash-link" aria-label="Direct link to Next Steps" title="Direct link to Next Steps">​</a>

### Using VPS with the Niantic SDK:<a href="#using-vps-with-the-niantic-sdk" class="hash-link" aria-label="Direct link to Using VPS with the Niantic SDK:" title="Direct link to Using VPS with the Niantic SDK:">​</a>

4.  [Getting Started with VPS](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/adding_vps/)

</div>

</div>
