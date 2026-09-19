---
source: https://www.nianticspatial.com/docs/scaniverse/360camera/
title: 360 Camera Scanning Guide
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Scan with a 360 camera

</div>

This guide explains how to capture high-quality 360 scans with Scaniverse, from preparing the scene and configuring your camera to capturing, uploading, and processing scans into meshes and Gaussian splats. It also covers supported cameras, recommended capture techniques, and troubleshooting common issues.

Scaniverse supports **360 video files only**, including `.insv` and equirectangular `.mp4`. Still panoramic images (`.jpg`, `.png`, etc.) are not supported.

### Workflow<a href="#workflow" class="hash-link" aria-label="Direct link to Workflow" title="Direct link to Workflow">​</a>

A typical 360 camera workflow includes the following steps:

1.  [Choose a supported 360 camera](#supported-cameras-and-video-formats).
2.  [Configure your camera](#scene-setup):
    1.  If you're capturing outdoors, set your exposure to **Auto**.
    2.  If you're indoors, set the shutter speed to **1/500** and ISO to **Auto**.
3.  [Capture the scan](#capture-a-scan) by walking the perimeter, then filling the interior with overlapping passes.
4.  Transfer your video to a desktop computer using an SD card, USB cable, or other supported method.
5.  [Upload your scan](#upload-scan) to <a href="https://scaniverse.nianticspatial.com/signin" target="_blank" rel="noopener noreferrer">Scaniverse Web</a>.
6.  [Process and download](#process-and-download) the resulting asset.

------------------------------------------------------------------------

## Table of contents<a href="#table-of-contents" class="hash-link" aria-label="Direct link to Table of contents" title="Direct link to Table of contents">​</a>

Follow the guide from start to finish, or use the following table of contents to navigate directly to a specific step in the workflow.

- [Overview](#overview) - Learn when to use a 360 camera and how it differs from mobile capture.
- [Requirements](#requirements) - Review the supported hardware, software, and account requirements.
- [Supported cameras and video formats](#supported-cameras-and-video-formats) - Find supported cameras and learn which file formats can be uploaded directly.
- [Scene setup](#scene-setup) - Prepare the environment, optimize lighting, and set up metric scale calibration.
- [Capture a scan](#capture-a-scan) - Configure your camera and follow recommended capture techniques.
- [Upload and process scans](#upload-and-process-scans) - Prepare files, upload your scan, and generate assets.
- [Troubleshooting and FAQ](#troubleshooting-and-faq) - Resolve common issues and find answers to frequently asked questions.

------------------------------------------------------------------------

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

A 360 camera captures the entire environment at once using two lenses that each record slightly more than 180°. The camera stitches these feeds together so you can view the full surroundings in every direction simultaneously as shown in the following video:

A 360 camera is:

- **Efficient:** Capturing an environment with a 360 camera is roughly three times faster than using a mobile phone.
- **Immersive:** The camera captures the entire environment—floor to ceiling—at once, producing 3D assets that feel complete and immersive.
- **Easy to use:** The camera sees in all directions simultaneously, which significantly reduces the chance of leaving holes or blind spots in your scan.
- **Ideal for large areas:** The combination of speed and full-environment capture makes 360 cameras especially well suited for digitizing large spaces such as marinas, parks, and large indoor facilities.
- **Limited in duration:** Plus supports up to 5-minute videos, and Pro supports up to 10-minute videos for 360 camera uploads.

### Requirements<a href="#requirements" class="hash-link" aria-label="Direct link to Requirements" title="Direct link to Requirements">​</a>

- A [supported 360 camera](#supported-cameras-and-video-formats).
- A desktop computer for uploading your scan.
- A Pro or Plus Scaniverse account with available credits.

### Supported cameras and video formats<a href="#supported-cameras-and-video-formats" class="hash-link" aria-label="Direct link to Supported cameras and video formats" title="Direct link to Supported cameras and video formats">​</a>

Scaniverse supports 360 video uploads in two formats, depending on your camera.

| Camera type | Upload format | Preparation required |
|----|----|----|
| Insta360 X5, X4 Air, or X4 | Raw `.insv` | Upload directly from the SD card. No stitching or conversion required. |
| Other 360 cameras | Stitched equirectangular `.mp4` | Export the video from the camera manufacturer's desktop software before uploading. |

Commonly used cameras that use the `.mp4` workflow include:

- Insta360 X3 and One RS 1-inch 360
- Ricoh Theta X and Theta Z1
- GoPro Max 2
- DJI Osmo 360
- 360 drones such as Antigravity A1 and DJI Avata 360

<div class="theme-admonition theme-admonition-tip admonition_xJq3 alert alert--success">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)</span>tip

</div>

<div class="admonitionContent_BuS1">

Insta360 cameras record both `.INSV` and `.LRV` files. Upload the original `.INSV` files. The `.LRV` files are low-resolution preview files and are not used for processing.

</div>

</div>

------------------------------------------------------------------------

## Scene setup<a href="#scene-setup" class="hash-link" aria-label="Direct link to Scene setup" title="Direct link to Scene setup">​</a>

Prepare the scene before capturing by optimizing lighting, minimizing moving people, and setting up optional metric scale calibration.

### Environment and lighting<a href="#environment-and-lighting" class="hash-link" aria-label="Direct link to Environment and lighting" title="Direct link to Environment and lighting">​</a>

- Capture in well-lit, evenly lit environments whenever possible.
- Avoid strong shadows, direct sunlight, and rapidly changing lighting conditions.
- Good lighting produces sharper frames and improves reconstruction quality.

### People in the scene<a href="#people-in-the-scene" class="hash-link" aria-label="Direct link to People in the scene" title="Direct link to People in the scene">​</a>

For best results, capture the scene when it is empty.

If people are present:

- People who remain stationary may appear as incomplete or distorted geometry in the final reconstruction.
- People who are moving are more likely to be removed during processing.

### Metric scale calibration<a href="#metric-scale-calibration" class="hash-link" aria-label="Direct link to Metric scale calibration" title="Direct link to Metric scale calibration">​</a>

To enable real-world scale:

1.  Download the calibration board <a href="https://www.nianticspatial.com/docs/calibration/US%20Letter.pdf" download="US Letter.pdf">US Letter</a> \| <a href="https://www.nianticspatial.com/docs/calibration/A4.pdf" download="A4.pdf">A4</a> and print it at 100% scale.
2.  Place the board flat on the floor where you will begin scanning.
3.  Start recording with one 360 camera lens positioned 30–50 cm from the board.
4.  Slowly circle the 360 camera around the board while keeping the board clearly visible and in focus for the first 30 seconds.
5.  Continue scanning the environment as usual.

The following video demonstrates how to capture the calibration board:

The following image shows how to start recording with the calibration board visible to the camera:

<img src="https://www.nianticspatial.com/docs/assets/images/metric_calibration-5d0e332c3555e9e4d2f757d64d1ab03a.jpeg" style="width:80%;max-width:400px" alt="The metric calibration board should be placed in view of the 360 camera in the beginning of the scan." />

Scaniverse automatically detects the calibration board and applies 1:1 scaling during processing.

## Capture a scan<a href="#capture-a-scan" class="hash-link" aria-label="Direct link to Capture a scan" title="Direct link to Capture a scan">​</a>

This section explains how to capture a scan using a 360 camera. Focus on stable movement, complete coverage, and consistent camera setup.

### Camera and equipment setup<a href="#camera-and-equipment-setup" class="hash-link" aria-label="Direct link to Camera and equipment setup" title="Direct link to Camera and equipment setup">​</a>

Configure your camera before capturing. The following recommended settings are based on the Insta360 X5 but apply broadly to other supported 360 cameras.

**GPS capture**

Capture GPS data whenever your 360 camera supports it so that the scan retains its real-world location and movement path for geographic alignment and identification. Insta360 X4 and X5 cameras do not have built-in GPS, so a recording started with the 360 camera's shutter button does not include GPS data. To capture GPS data with the Insta360 app:

1.  Enable location services on your mobile device and allow the Insta360 app to access your location.
2.  Turn on the Insta360 camera and connect it to the Insta360 app.
3.  Tap the camera icon at the bottom of the Insta360 app to open the live preview.
4.  In the live preview, tap the vertical three-dot icon (`⋮`) in the upper-right corner of your mobile device's screen and turn on **GPS**.
5.  Start recording from the Insta360 app.
6.  Keep the app open, the mobile device's screen on, and the Insta360 camera connected during the capture.
7.  Stop recording from the Insta360 app.

For more information, see <a href="https://onlinemanual.insta360.com/app/en-us/operation-tutorial/stats-dashboard/dashboard-collection#how-to-add-stats" target="_blank" rel="noopener noreferrer">Insta360's instructions for recording GPS data with a phone</a>. To capture GPS data with a compatible remote instead, see <a href="https://onlinemanual.insta360.com/gpspreviewremote/en-us/camera/basicuse" target="_blank" rel="noopener noreferrer">Insta360's GPS remote instructions</a>.

**Camera settings**

- Resolution: 8K
- Frame rate: 30 fps, or 25 fps in PAL (EU) regions
- Adaptive tone: Off
- Video encoding: H.265
- Color: Standard
- Sharpness: Medium
- Bitrate: High
- Anti-flicker: Auto

**Exposure**

- **Indoor:** Set shutter speed to 1/500 and ISO to Auto. The following video shows how to open exposure settings and set 1/500:

- **Outdoor:** Set both shutter speed and ISO to Auto.\
  The following video shows how to use Auto mode:

**Equipment setup**

- Use the invisible selfie stick supplied with your camera whenever possible.

- Extend the selfie stick to maintain consistent coverage while minimizing your presence in the capture:

  - **Indoor spaces:** Extend to roughly two-thirds of its full length.
  - **Outdoor spaces:** Extend to its full length.

- Hold the selfie stick slightly away from your body so the camera has a clear view of the environment while minimizing your appearance in the scan. The following image shows the recommended selfie stick positions: extended to two-thirds length for indoor capture (left) and fully extended for outdoor capture (right).

  <div style="display:flex;gap:16px;justify-content:flex-start">

  <img src="https://www.nianticspatial.com/docs/assets/images/indoor_selfie_stick-f31389e8565d0692e48f0b365c906e90.png" style="width:40%" alt="Indoor selfie stick extension" /><img src="https://www.nianticspatial.com/docs/assets/images/outdoor_selfie_stick-b79105ce4cf0c5e997dfd440a6dd544a.png" style="width:40%" alt="Outdoor selfie stick extension" />

  </div>

- Orient the camera so the lenses face left and right relative to your direction of travel, not forward and backward.

  The following image shows the orientation of the camera lenses as perpendicular to the direction of movement towards and away from the viewer:

  <img src="https://www.nianticspatial.com/docs/assets/images/camera_orientation-95d4de7aba80e9bb2fc26eea6e9f73f9.jpeg" style="width:80%;max-width:400px" alt="Orient the camera so that the camera lenses face to the right and left to the direction of travel." />

------------------------------------------------------------------------

### Plan your capture<a href="#plan-your-capture" class="hash-link" aria-label="Direct link to Plan your capture" title="Direct link to Plan your capture">​</a>

High-quality captures depend on smooth movement, consistent camera positioning, and complete scene coverage. The following techniques describe how to move through an environment to maximize reconstruction quality while minimizing alignment errors and artifacts:

#### Planning strategies<a href="#planning-strategies" class="hash-link" aria-label="Direct link to Planning strategies" title="Direct link to Planning strategies">​</a>

**Divide large spaces**

Divide large spaces into logical quadrants or sections and scan one section at a time rather than trying to capture the entire area at once. Complete coverage of one section before moving to the next, ensuring adjacent sections overlap. As you move between sections, capture overlapping views that connect both sections to help maintain alignment throughout the reconstruction.

**Cross-grid open areas (Optional)**

For large, open spaces or when the highest reconstruction quality is required, repeat the lattice grid in a perpendicular direction. For example, north-south followed by east-west. Cross-gridding improves coverage and can reduce alignment errors.

**Close the loop**

Toward the end of your scan, briefly point the camera back at a previously scanned landmark to reinforce alignment across the entire reconstruction. Always finish your scan by returning to the same location that you started.

#### Movement<a href="#movement" class="hash-link" aria-label="Direct link to Movement" title="Direct link to Movement">​</a>

**The wave pattern**

Use a gentle sinusoidal wave pattern as you move the camera, rather than keeping it at a constant height. This captures ceilings, upper walls, floors, and furniture in a single pass, improving coverage without requiring additional passes.

**Sinusoidal motion**

- Walk at a slow and steady pace.
- Slow down when capturing using a sinusoidal wave pattern.
- In darker areas, slow down to a crawl pace. A 1/500 shutter speed requires more light, and slower movement is the only way to prevent motion blur.
- Avoid jerks, bouncing, or rapid turns.

#### Distance<a href="#distance" class="hash-link" aria-label="Direct link to Distance" title="Direct link to Distance">​</a>

- Maintain a minimum distance of 30 cm or 12 inches from all surfaces.
- Avoid placing the camera into tight spaces or directly beneath furniture, or other overhangs unless you are intentionally capturing additional detail.
- Avoid placing objects across the stitch line between the two lenses, which can cause warping, blind spots, or artifacts in the final asset.

#### Coverage<a href="#coverage" class="hash-link" aria-label="Direct link to Coverage" title="Direct link to Coverage">​</a>

Capture the entire environment with consistent overlap and as few gaps as possible. Adapt your scanning pattern to the geometry of the scene to maintain continuous coverage.

- Overlap adjacent passes.
- Avoid isolated regions that aren’t connected to the rest of the scan.

------------------------------------------------------------------------

## Upload and process scans<a href="#upload-and-process-scans" class="hash-link" aria-label="Direct link to Upload and process scans" title="Direct link to Upload and process scans">​</a>

After capturing a scan, transfer your files to a desktop computer and upload them to <a href="https://scaniverse.nianticspatial.com/signin" target="_blank" rel="noopener noreferrer">Scaniverse Web</a> for processing. This section covers how to [prepare your files](#prepare-files), [upload them](#upload-scan), and [process and download](#process-and-download) the resulting assets.

### Prepare files<a href="#prepare-files" class="hash-link" aria-label="Direct link to Prepare files" title="Direct link to Prepare files">​</a>

Before uploading, transfer your 360 capture files to a desktop computer. Connect the camera to your computer using a USB-C cable or remove the microSD card. If connecting the camera directly, select **File Transfer Mode** when prompted so it appears as an external drive. Scaniverse processes 360 data through Scaniverse Web, so all uploads and processing must be done in a desktop browser.

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

360 processing runs exclusively through Scaniverse Web on a desktop browser, not the mobile app.

</div>

</div>

If you are using an Insta360 X5, X4 Air, or X4, you can upload raw `.insv` files directly without additional preparation. For all other cameras, you must first convert your footage into a stitched `.mp4` file.

**Pre-processing**

To prepare stitched footage for upload:

1.  **Trim:** Remove unnecessary portions of the video to reduce file size and processing time.
2.  **Enable direction lock:** When exporting to `.mp4`, enable direction lock to preserve spatial consistency and gyroscope orientation.
3.  **Export:** Export the stitched file as an `.mp4` using H.264 or H.265 encoding. Insta360 users can optionally use Insta360 Studio to preview raw .INSV recordings before uploading. If using an Insta360 X5, X4 Air, or X4, upload the original .INSV files rather than exporting a stitched .mp4.

### Upload scan<a href="#upload-scan" class="hash-link" aria-label="Direct link to Upload scan" title="Direct link to Upload scan">​</a>

After preparing your file, upload it to Scaniverse Web to begin processing. You can generate a mesh or Gaussian splat from a 360 camera scan.

1.  Log in to your <a href="https://scaniverse.nianticspatial.com/" target="_blank" rel="noopener noreferrer">Scaniverse Web account</a> using a desktop browser.
2.  Upload your scan file:
    - **Insta360 X5, X4 Air, or X4:** Upload the raw `.insv` file directly from your local drive or SD card.
    - **Other cameras:** Upload the stitched `.mp4` file exported from your camera’s desktop software.
3.  Start the upload to begin cloud processing.

Processing begins automatically after the upload completes.

### Process and download<a href="#process-and-download" class="hash-link" aria-label="Direct link to Process and download" title="Direct link to Process and download">​</a>

After your 360 scan upload finishes, you can generate one or more asset types from that capture. In this step, select the 360 scan, choose whether to generate a splat, a mesh, or both, review the estimated duration and credit cost, and then download the finished asset in the format you need.

**Asset types**

- **Splat:** Best for visual quality and scene preview. Usually takes longer to generate.
- **Mesh:** Best for geometry-based 3D workflows and exports.

After your upload completes, generate assets as follows:

1.  Select the Site that contains the scan you want to process.
2.  Select **Generate assets**.
3.  Enter an Asset name.
4.  Under **Choose your scan type**, select **360 scan**.
5.  Select the uploaded 360 scan from the list. A preview and scan details appear on the right.
6.  Under **Choose what assets you want generated**, select one or both of the following:
    - **Splat**
    - **Mesh**
7.  Review the **Capture duration** and **Credits required** summary at the bottom of the window.
8.  Select **Generate**.

During processing, Scaniverse extracts frames from your video and reconstructs the scene. The 360 scan flow generates assets from a single 360 capture. Processing time depends on file size, complexity, and which asset types you selected.

**Video length limits**

- **Free plan**: 360 camera asset generation is not available.
- **Plus plan**: uploads are limited to videos up to 5 minutes.
- **Pro plan**: uploads are limited to videos up to 10 minutes.

Capture each site as a single continuous recording whenever possible. If your recording exceeds your account's supported upload duration, split it into shorter recordings before uploading.

**View assets**

Once processing is complete, you can inspect the generated mesh or splat directly in Scaniverse Web.

**Supported output formats**

Download the generated asset in the following formats:

- **Splat:** `.ply`, `.spz`, `.usdz`
- **Mesh:** `.glb`, `.usdz`

------------------------------------------------------------------------

## Troubleshooting and FAQ<a href="#troubleshooting-and-faq" class="hash-link" aria-label="Direct link to Troubleshooting and FAQ" title="Direct link to Troubleshooting and FAQ">​</a>

This section covers common issues and frequently asked questions when capturing and processing 360 scans.

**Blurry splats**\
Use a shutter speed of 1/500 for indoor environments to reduce motion blur.

**Drifting or warped environments**\
If you used the `.mp4` workflow, verify that direction lock was enabled during export.

**Avoid overscanning** Avoid repeatedly scanning the same area. You can pass through an area twice to connect different parts of a scan, but excessive rescanning can introduce SfM (structure from motion) or small alignment errors that reduce the sharpness of the final reconstruction.

**Handling large files**\
If your capture exceeds your account tier’s video length limit, trim the footage into smaller segments using your camera’s desktop software before uploading.

**Can I upload a 360 panoramic image (`.jpg`, `.png`, etc.)?**\
No. Scaniverse supports only 360 **video** files: raw `.insv` files from Insta360 X5, X4 Air, and X4, or stitched equirectangular `.mp4` files from other cameras. Still panoramic images are not supported.

**Can I upload 360 videos via the mobile app?**\
No. Uploading and processing 360 video files is only supported via Scaniverse Web on a desktop browser.

**Can I generate a mesh from a 360 camera scan?** Yes. In the **Generate assets** flow, choose **Mesh** instead of **Gaussian splat**.

**Can I export a 360 scan as USDZ?** Yes. Supported 360 splats and meshes can be downloaded as a combined **USDZ** file from Scaniverse Web.

**How can I produce a splat that can be used for 3D measurements?**\
Print the calibration board <a href="https://www.nianticspatial.com/docs/calibration/US%20Letter.pdf" download="US Letter.pdf">US Letter</a> \| <a href="https://www.nianticspatial.com/docs/calibration/A4.pdf" download="A4.pdf">A4</a> and circle it with your camera at the start of your recording. Scaniverse automatically scales the resulting asset to real-world 1:1 metric measurements.

**Can I use a 360 drone?**\
Yes, you can use 360 videos from 360 drones such as the Antigravity A1 and DJI Avata 360.

**Do I need desktop software to process my files?**

- **No, if you have an Insta360 X5, X4 Air, or X4.** Scaniverse Web natively supports raw `.insv` files from these models. No additional software is required.
- **Yes, if you use any other camera.** Use the manufacturer’s desktop software to stitch your footage into an `.mp4` with direction lock enabled before uploading to Scaniverse Web.

</div>

</div>
