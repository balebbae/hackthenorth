---
source: https://www.nianticspatial.com/docs/nsdk/how-to/vps/tooling/lightship_scaniverse/
title: Scaniverse for Lightship
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Scaniverse for Lightship

</div>

We are currently running a beta of Scaniverse for Niantic Developers, which seamlessly integrates the Geospatial Browser (GSB) with the award-winning scanning experience in Scaniverse. This significantly streamlines developer workflows around browsing the map, adding locations, and of course scanning:

<div class="theme-admonition theme-admonition-warning admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Legacy Geospatial Browser workflow

</div>

<div class="admonitionContent_BuS1">

The Geospatial Browser and its Scaniverse integration are no longer available. These instructions are retained as a reference for older VPS projects. For current projects, create and manage Sites in <a href="https://scaniverse.nianticspatial.com/" target="_blank" rel="noopener noreferrer">Scaniverse Web</a>.

</div>

</div>

- We’ve made the Geospatial Browser (GSB) mobile-friendly so that it can be effectively used within Scaniverse to browse the map, inspect locations, add locations, and request VPS activation
- We’ve replaced the Wayfarer App login flow with a simple QR code that links Scaniverse with your Lightship account
- We have adopted Scaniverse’s existing UI to power creation and uploading of scans
- We’ve enabled testing localization at VPS-activated locations within Scaniverse
- We’ve integrated our latest improvements to map filtering to make it easier than ever to find the location(s) you are looking for

## Linking Scaniverse with the Geospatial Browser (GSB)<a href="#linking-scaniverse-with-the-geospatial-browser" class="hash-link" aria-label="Direct link to Linking Scaniverse with the Geospatial Browser (GSB)" title="Direct link to Linking Scaniverse with the Geospatial Browser (GSB)">​</a>

Install Scaniverse from the <a href="https://apps.apple.com/us/app/scaniverse-3d-scanner/id1541433223" target="_blank" rel="noopener noreferrer">iOS App Store</a> or <a href="https://play.google.com/store/apps/details?id=com.nianticlabs.scaniverse" target="_blank" rel="noopener noreferrer">Google Play Store</a>.

1.  Log in to your Lightship account on your desktop. Open the **Geospatial Browser (GSB)**, select any location on the map, and then select **View Details**. In the bottom right corner of the location details card, press **Generate QR Code**. A QR code will be displayed.

<img src="https://www.nianticspatial.com/docs/assets/images/scaniverse1-26c301b718d037f0639946a2f9d14a4a.png" style="width:30.0%" alt="Indicating the QR Code" />

2.  Open the Camera app on your phone, then scan the QR code and open the Scaniverse link that appears. This will link Scaniverse with your Lightship developer account.
3.  When prompted, allow Scaniverse to use your current location.
4.  Once you have linked Scaniverse to GSB, you will be able to return to the GSB screen at any time by tapping the **GSB button** in the bottom ribbon of the Scaniverse app. Note that you may unlink Scaniverse from GSB at any time by going to the **Settings** menu and toggling off the **Niantic Developer Mode** option.

<img src="https://www.nianticspatial.com/docs/assets/images/scaniverse3-6f86787d5a5fd32842e2f5606853af0a.png" style="width:30.0%" alt="Indicating the GSB Button" />

All of the scans you have taken outside of Niantic Developer Mode will remain accessible when linking/unlinking Scaniverse with GSB.

## Browsing the Geospatial Browser Map in Scaniverse<a href="#browsing-the-gsb-map-in-scaniverse" class="hash-link" aria-label="Direct link to Browsing the Geospatial Browser Map in Scaniverse" title="Direct link to Browsing the Geospatial Browser Map in Scaniverse">​</a>

1.  Tapping on the **Person** icon will allow you to select your Workspace.
2.  The **Upload** button lets you select location scans to upload. Only scans taken in Niantic Developer Mode (using the **Add Scans** or **Test Scan** options) can be uploaded to Niantic for VPS development purposes.
3.  The **Plus** button lets you create new locations and test scans.
4.  The **Layers** button toggles the satellite view of the map.
5.  The **Reticle** button centers the map on your location.
6.  Tapping the **Compass** button returns the map to its default orientation.
7.  The **Controls** button lets you filter visible map locations based on their size, category, or activation status.
8.  The **Magnifying Glass** button lets you to search the map.

<img src="https://www.nianticspatial.com/docs/assets/images/scaniverse4-2189be273b56eeec7c46224ed4a163b9.jpg" style="width:30.0%" alt="The GSB Map Layout" />

Selecting a location on the map will bring up a **Preview** screen. Tap the preview for more details. If you’ve selected a VPS-activated location, you can tap the **Test VPS** button to verify that localization works. To scan a location, tap its **Add Scans** button. You must be near the location for the Add Scans option to be available.

<img src="https://www.nianticspatial.com/docs/assets/images/scaniverse5-7445fb6c5edd56a9fdc06b871aa3ad7a.png" style="width:30.0%" alt="The GSB Map Preview Layout" />

## Creating and Uploading Scans<a href="#creating-and-uploading-scans" class="hash-link" aria-label="Direct link to Creating and Uploading Scans" title="Direct link to Creating and Uploading Scans">​</a>

To create and upload a scan:

1.  The **Record** button is used to start and stop the scanning process.
2.  The **Pause** button can be used to temporarily suspend the scanning process if desired.
3.  The **Time** display indicates the duration of the current scan. A minimum length of 15 seconds is required for a scan to be viable for upload for VPS development purposes. A scan length of 30-60 seconds is ideal (scans in excess of 60 seconds are split into multiple pieces for processing purposes).

<img src="https://www.nianticspatial.com/docs/assets/images/scaniverse6-81f97d40622d2c7f73bb008ec58f5a14.png" style="width:30.0%" alt="The GSB Scan Creation interface" />

When you have completed a scan, you will be able to inspect a **Preview Mesh** of the scene that you captured. If you are happy with your scan, you can upload it immediately by pressing the **Upload Scan** button or do it later over WiFi by tapping **Upload Later**. If you are not happy with your scan, you can discard it by pressing the **Delete** button.

<div class="theme-admonition theme-admonition-tip admonition_xJq3 alert alert--success">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)</span>Important!

</div>

<div class="admonitionContent_BuS1">

Because uploading can use a significant amount of data, we recommend waiting until you have WiFi access to upload your scans.

</div>

</div>

## Scanning Technique<a href="#scanning-technique" class="hash-link" aria-label="Direct link to Scanning Technique" title="Direct link to Scanning Technique">​</a>

Scanned VPS-activated locations should be no larger than a 10-meter diameter around the location. For example, a typical statue would work as a VPS-activated Location, but an entire building will not. We recommend sticking with smaller areas to start (e.g. a desk, statue, or mural). Before scanning, be aware of your surroundings and ensure you have the right to access the location you are scanning.

To scan an area with proper technique:

1.  Check the area to be scanned and the surroundings of the scanned object to determine if there are any obstacles and to select a scanning route. Make sure to plan the route you intend to use for scanning before starting the procedure.
2.  Make sure your camera is in focus. Camera shake can negatively affect 3D reconstruction. Keep your phone as close to your side as possible to avoid blurring. Walk around the object you are scanning instead of standing in one location and moving your phone.
3.  Walk at a slow and natural stroll pace. Move yourself slowly and smoothly during scanning. Sudden changes of direction are a definite no-no. Move slowly and smoothly with your feet on the ground. If you are scanning in a darker setting, it’s even more important to move slowly and smoothly. Move the phone with you while you are moving.
4.  VPS Location should always be the focal point. In order for us to build the map, it's important to focus on the VPS Location and capture the full 360° orbit of it. If it is not safe or not possible to get 360° coverage, capture as much as you can.
5.  Vary your distance/angles (0-10m or 0-35ft). In order for the 3D map to work well in different scenarios, it’s important that we capture the environment around the Location and have a variety of different scans. Vary your distance and angles while scanning the Location.

Video of recommended VPS Location scanning technique:

<div class="iframe">

<div id="player">

</div>

<div class="player-unavailable">

# An error occurred.

<div class="submessage">

Unable to execute JavaScript.

</div>

</div>

</div>

## Things to avoid while scanning<a href="#things-to-avoid-while-scanning" class="hash-link" aria-label="Direct link to Things to avoid while scanning" title="Direct link to Things to avoid while scanning">​</a>

Consider these guidelines while scanning:

1.  Avoid scanning while the surroundings are not safe, e.g. in the middle of the road, or in a playground with children.
2.  Avoid scanning while the Location is too far away (\>10m or 35ft) or too big to focus your camera on.
3.  It is important to keep the Location as your focal point at all times.
4.  Avoid pointing your phone at very bright objects, such as fluorescent lights or the sun.
5.  Avoid not moving or moving too fast while scanning. Abrupt motions will cause offsets in the reconstruction.
6.  If your phone gets hot, let it cool down before scanning. If the temperature of the device rises too high, the performance of the device will be greatly reduced, which will negatively affect the scan.
7.  Avoid uploading any scans that look incomplete or not representative of what you're trying to scan.
8.  Avoid scanning when it’s too dark/there is insufficient lighting

</div>

</div>
