---
source: https://www.nianticspatial.com/docs/scaniverse/techniques/
title: Scan Techniques for Scaniverse
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="theme-admonition theme-admonition-info admonition_xJq3 alert alert--info">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)</span><a href="https://lightship.dev/signin" target="_blank" rel="noopener noreferrer">Lightship.dev</a> has been decommissioned.

</div>

<div class="admonitionContent_BuS1">

If you previously used Lightship.dev, log in to <a href="https://scaniverse.nianticspatial.com" target="_blank" rel="noopener noreferrer">scaniverse.nianticspatial.com</a>, and select **Migrate a Lightship account** to create a new account and access your projects. For more information, see the [Migration guide](https://www.nianticspatial.com/docs/scaniverse/migration_guide/).

</div>

</div>

<div>

# Scaniverse scan techniques

</div>

Scans capture the data Scaniverse uses to create assets for localization. Accurate scans make localization more reliable. Incomplete or inconsistent scans can cause gaps or tracking issues.

For best practices on capturing high-fidelity mesh and splat data, see this <a href="https://nianticspatial.com/videos/scaniverse-scanning-tips" target="_blank" rel="noopener noreferrer">video</a>.

This guide shows you how to plan and capture high-quality scans using your phone, including:

- How to prepare and organize your Site.
- Techniques and patterns for capturing spaces.
- Indoor, outdoor, and mixed environments.
- How to review coverage and decide where to add scans.

For 360 camera setup and capture workflows, see the [360 camera scanning guide](https://www.nianticspatial.com/docs/scaniverse/360camera/).

This guide does not cover:

- Asset processing or internal calculations.
- Debugging uploads that failed.
- VPS deployment or configuration.
- Advanced asset tuning.

You can use the <a href="https://scaniverse.nianticspatial.com" target="_blank" rel="noopener noreferrer">Scaniverse Web</a> to inspect assets and review playback sessions. Reviewing your assets helps you identify gaps to add or replace scans.

------------------------------------------------------------------------

## How Scanning Works<a href="#how-scanning-works" class="hash-link" aria-label="Direct link to How Scanning Works" title="Direct link to How Scanning Works">​</a>

Scans capture the data that Scaniverse uses to create assets. High-quality scans improve localization speed and alignment stability. Incomplete or inconsistent scans can cause localization to take longer, fail in certain areas, or appear unstable as you move through the space.

When you scan with your device, you capture:

- High- and low-resolution images.
- Device position and orientation in 3D space.
- Depth information if your device has LiDAR.

Scaniverse uses the scans to generate Assets including:

- **Meshes** - 3D geometry for spatial alignment and use with VPS.
- **Splats** - dense visual representations of a space.

Each generated Asset Version defines a spatial coordinate system for the Site. During localization, the device’s position and orientation are computed within that coordinate system, allowing digital content to align consistently with the real-world environment.

The recommended number of scans and patterns depend on your Site type. See the following [Recommended scan patterns](#recommended-scan-patterns) section for full guidance.

<img src="https://www.nianticspatial.com/docs/assets/images/technique_07-54aeb7342a1cddfbd2ec14d7628383b9.png" width="600" alt="A bad scan contains few visually distinct features while a good scan provides recognizable details." />

------------------------------------------------------------------------

## Plan your scan<a href="#plan-your-scan" class="hash-link" aria-label="Direct link to Plan your scan" title="Direct link to Plan your scan">​</a>

Planning helps you choose scanning patterns, cover all areas, and decide if multiple scans are needed. Over time, this step becomes quick on site.

### Create a Site<a href="#create-a-site" class="hash-link" aria-label="Direct link to Create a Site" title="Direct link to Create a Site">​</a>

A Site organizes all scans for a location, tracks coverage, and reduces repeated scanning, making asset activation easier.

To create a Site:

1.  Open <a href="https://scaniverse.nianticspatial.com" target="_blank" rel="noopener noreferrer">Scaniverse Web</a> in a desktop or laptop browser for faster setup and easier navigation.
2.  Select **+ Create Site**.
3.  Enter a clear, descriptive, and unique Site name.
4.  Select **Confirm**.

------------------------------------------------------------------------

### Prepare Your Device<a href="#prepare-your-device" class="hash-link" aria-label="Direct link to Prepare Your Device" title="Direct link to Prepare Your Device">​</a>

Good device preparation helps ensure reliable scans. Before you start:

- Fully charge your device.
- Bring one or more power banks for extended sessions or large areas.
- Close unnecessary background apps.
- Charge your device if it drops below 50% during a session. Avoid power-saving mode, which can reduce scan quality.

------------------------------------------------------------------------

### Survey the space<a href="#survey-the-space" class="hash-link" aria-label="Direct link to Survey the space" title="Direct link to Survey the space">​</a>

Survey the space before scanning using the following recommendations:

- View maps, satellite imagery, or floor plans to understand the space.
- Identify boundaries, transitions, and points of interest.
- Plan scan start and end points.

------------------------------------------------------------------------

## Core scanning techniques<a href="#core-scanning-techniques" class="hash-link" aria-label="Direct link to Core scanning techniques" title="Direct link to Core scanning techniques">​</a>

Follow these principles to ensure good scanning results:

- Move your device steadily. Avoid sudden movements to prevent blur or position tracking loss.
- Keep a continuous motion, even if very slow.
- Maintain **overlap** with previous views of the same features.
- Capture **multiple angles and distances**.
- Focus on areas with distinct visual features.

Scans can fail if the system cannot connect sequential views. Each scan lasts up to five minutes, but you can capture multiple scans per Site as needed.

**Follow on-device guidance**

Scaniverse provides live meshing feedback while scanning to indicate if the system is successfully capturing the scene.

If meshing becomes sparse or unstable, mesh visuals may appear:

- Patchy or incomplete mesh on the device screen.
- Missing sections in some areas.
- Wobbly or disappearing mesh while moving slowly.

If meshing becomes unstable, do the following:

- Slow down your movement.
- Reorient the camera toward previously scanned features.
- Increase overlap with earlier views.

------------------------------------------------------------------------

**Capture multiple angles and distances**

Capture each area from several viewpoints to help the system reconstruct 3D geometry.

For each object or region:

- Move the device laterally from side to side.
- Change the height and tilt.
- Vary distance from the object or area.
- Keep the camera moving continuously.

Capturing multiple viewpoints lets the system match overlapping features from different perspectives, improving localization accuracy.

<img src="https://www.nianticspatial.com/docs/assets/images/technique_01-949dc38b5698f2eae8f7e8877cba4142.png" style="width:100%;max-width:600px" alt="Phone moves side to side, up/down, and closer/far from table, lamp, and sofa." /> <img src="https://www.nianticspatial.com/docs/assets/images/technique_06-745951744e0b84a6059d7ef44f4f4f70.png" style="width:100%;max-width:600px" alt="Phone moves side to side, up/down, and closer/far from machines, books, and devices." />

------------------------------------------------------------------------

**Ensure sufficient overlap within and between scans** Within a single scan:

- Keep previously captured features in view to help the system align frames accurately.

Across multiple scans in the same Site:

- Ensure successive scans share visible features with earlier scans.
- Overlap at boundaries, doorways, and transitions to connect multiple scans into a single, consistent 3D representation.

**Focus on coverage, not duration**

Recording for the full five-minute limit does not automatically improve results. Scan quality depends on overlap, viewpoint diversity, and clear visual features rather than recording length. A shorter scan with strong coverage is more reliable than a longer scan with gaps or weak overlap.

------------------------------------------------------------------------

**Minimize problematic conditions**

Certain surfaces and motion can reduce scan quality. When scanning, minimize:

- **Repetitive surfaces** including blank walls, and identical tiles.
- **Featureless areas** including empty ceilings or floors.
- **Reflective or transparent surfaces** such as mirrors, and glass.
- **Moving objects** including doors, people, and vehicles.

If you cannot avoid capturing moving objects, keep them out of the center of the camera view and focus on capturing stable, static features.

<img src="https://www.nianticspatial.com/docs/assets/images/technique_05-f39196fe08c62df2c0b50f8dd63036d1.png" style="width:100%;max-width:70%" alt="Four well-scanned areas showing a bookcase, chair, plant, and bench with objects, each captured clearly." /> <img src="https://www.nianticspatial.com/docs/assets/images/technique_02-314e2fe4573eae79e7c6a42461505608.png" style="width:100%;max-width:70%" alt="Four problematic scans showing a featureless wall with door, mirror, walking person, and reflective glass blocks." />

**Consider lighting variation when planning scans**

In most cases, you do not need to scan the same area at multiple times of day. Localization typically works well even when lighting conditions differ between scanning and use.

Capture additional scans under different lighting conditions only when:

- End users are expected to localize in significantly different lighting environments.
- The environment changes noticeably between those conditions, such as:
  - Strong directional sunlight creating harsh shadows.
  - Large shifts in ambient brightness, for example day versus night.

If lighting conditions are relatively consistent, or changes are minor, a single well-captured scan is typically sufficient.

------------------------------------------------------------------------

## Recommended scan patterns<a href="#recommended-scan-patterns" class="hash-link" aria-label="Direct link to Recommended scan patterns" title="Direct link to Recommended scan patterns">​</a>

Following a scanning pattern helps you capture complete coverage efficiently and reduces gaps. Choose a pattern based on the type and size of your Site.

Details for each pattern follow the table:

| Site Type | Suggested Pattern | Notes |
|----|----|----|
| Single Room | Overview Scan | Walk the perimeter and capture ceiling, floor, and corners. Add detail scans where needed. |
| Object or Landmark | Orbit | Move around the object at varying distances and angles. |
| Multiple Connected Rooms | Overview per room | Ensure overlap through doorways and transitions. |
| Large Outdoor Area | Perimeter + Lattice/Grid | Start with a perimeter loop, then fill interior coverage with a grid or crisscross passes. |
| Indoor + Outdoor Combined Site | Separate scans per zone | Pause at thresholds and ensure shared features are visible at transitions. |

You can combine patterns for complex Sites or when different areas require different approaches. Following these guidelines ensures scans connect properly, providing accurate localization and complete 3D coverage.

### Overview scan<a href="#overview-scan" class="hash-link" aria-label="Direct link to Overview scan" title="Direct link to Overview scan">​</a>

An overview scan provides a base localization layer for a room or enclosed space.

To perform an overview scan:

1.  Stand near the perimeter of the room.
2.  Walk along the perimeter while keeping the camera pointed towards the interior.
3.  Move at a steady pace without stopping.
4.  Complete the space in three passes:
    1.  Hold the device level to capture **mid-level** features such as walls and furniture.
    2.  Tilt the device **upwards** to capture the ceiling.
    3.  Tilt the device **downwards** to capture the floor.

During each pass, keep previously captured features visible in the frame so the system can connect the views.

Large rooms may require more than one overview scan to fully cover the space.

<img src="https://www.nianticspatial.com/docs/assets/images/technique_03-fc61f65537e862860f0b700468ba719d.png" style="width:80%" alt="Phone moving in a circular path around an object, plus views tilted up, level, and down toward the center." />

### Orbit pattern<a href="#orbit-pattern" class="hash-link" aria-label="Direct link to Orbit pattern" title="Direct link to Orbit pattern">​</a>

Use an orbit pattern when scanning a single object or point of interest such as furniture, statues, or monuments.

How to perform an orbit scan:

1.  Stand a short distance from the object.
2.  Walk around it in a circular path.
3.  Keep the object centered in the frame as you move.
4.  Maintain a consistent distance while circling.

Avoid stepping straight toward or away from the object repeatedly. Instead, move laterally around it to capture continuous side-to-side variation in perspective.

For larger objects, complete more than one circle at different distances to capture additional context and background features.

<img src="https://www.nianticspatial.com/docs/assets/images/technique_04-cfa55af65b7a26ce62fe6d5af19c929e.png" style="width:80%" alt="Camera moving in a circular path around stacked boxes in a room while pointing toward the center." />

------------------------------------------------------------------------

### Perimeter loop pattern<a href="#perimeter-loop-pattern" class="hash-link" aria-label="Direct link to Perimeter loop pattern" title="Direct link to Perimeter loop pattern">​</a>

Use a perimeter loop pattern for large outdoor spaces or long boundary areas such as courtyards, plazas, or building exteriors.

How to perform a perimeter loop scan:

1.  Walk along the outer boundary of the area.
2.  Keep the camera pointed inward toward the space.
3.  Move steadily while sweeping the device slightly left and right.
4.  Keep boundary features visible in the frame as you progress.

For stronger coverage, complete one pass clockwise and another counterclockwise. Opposite directions increase viewpoint diversity and improve alignment across the Site.

------------------------------------------------------------------------

### Lattice grid pattern<a href="#lattice-grid-pattern" class="hash-link" aria-label="Direct link to Lattice grid pattern" title="Direct link to Lattice grid pattern">​</a>

Use a lattice grid pattern for large continuous areas after completing perimeter coverage.

How to perform a lattice grid pattern:

1.  Complete one or more perimeter loop scans around the boundary.
2.  Walk straight passes across the interior of the area.
3.  After each pass, shift sideways and walk a parallel pass in the opposite direction.
4.  Continue until the entire interior is covered.
5.  Keep previously captured boundary features visible when entering and exiting each pass.

Interior passes should overlap both the perimeter coverage and adjacent passes to maintain alignment across the Site.

<img src="https://www.nianticspatial.com/docs/assets/images/technique_08-e88f4325c740c02be0073181942c21e4.png" style="width:80%" alt="Large outdoor park with trees and benches, dotted perimeter path connecting device positions at each corner." />

Use the table below to choose the most effective scanning pattern for your Site type. Each pattern shows the recommended approach and key notes for capturing complete coverage.

| Site Type | Recommended Pattern | Notes |
|----|----|----|
| Single enclosed space | Overview Scan | Perform an overview scan using three passes to capture ceiling, floor, and mid-level surfaces. |
| Object or landmark | Orbit | Move around the object at varying distances and angles to capture all sides. |
| Long boundary or room sequence | Perimeter Loop | Walk the boundary while capturing features along the edges, include multiple passes if needed. |
| Large open area | Perimeter + Lattice | First perform a perimeter loop, then cover interior with crisscross paths to maintain overlap. |
| Indoor + Outdoor Combined Site | Separate scans per zone | Pause at thresholds, ensure features from both areas are visible for smooth alignment. |

------------------------------------------------------------------------

## Use Cases<a href="#use-cases" class="hash-link" aria-label="Direct link to Use Cases" title="Direct link to Use Cases">​</a>

### Indoor<a href="#indoor" class="hash-link" aria-label="Direct link to Indoor" title="Direct link to Indoor">​</a>

**Single Rooms**

A single room is an enclosed space where you can capture all surfaces and objects in one session as follows:

1.  Perform an overview scan to obtain full coverage of the room.
2.  Scan important objects or areas more carefully to capture extra detail.
3.  Start and end focused scans from views captured in the overview.
4.  Include ceilings, floors, corners, and transitions in all scans.

**Multiple Rooms**

Multiple rooms are a series of connected spaces where scans should maintain overlap between rooms as follows:

1.  Scan doorways and hallways thoroughly. These areas act as structural connectors between rooms, and weak coverage here can cause unstable alignment between spaces.
2.  Ensure each room scan overlaps with visible features in neighboring rooms.
3.  Avoid scanning rooms in isolation.

**Multiple Floors**

Multiple floors are vertical spaces where you need to capture shared features across levels as follows:

1.  Scan staircases completely. Stairways connect vertical spaces, and insufficient coverage can cause misalignment between floors.
2.  Keep shared features visible between floors.
3.  Move slowly when changing elevation to preserve scan accuracy.

------------------------------------------------------------------------

### Outdoor<a href="#outdoor" class="hash-link" aria-label="Direct link to Outdoor" title="Direct link to Outdoor">​</a>

**Specific point of interest**

A specific outdoor Site or point of interest is a distinct object or area where you need detailed coverage as follows:

1.  Perform orbit scans at varying distances and angles around the object.
2.  Include surrounding context to help with localization.
3.  Avoid capturing only tight close-ups without wider references.

**Large continuous outdoor areas**

A large continuous outdoor area is a broad open space that requires multiple passes to ensure complete coverage as follows:

1.  Perform a perimeter scan clockwise around the area.
2.  Perform a perimeter scan counterclockwise to improve coverage and alignment.
3.  Add interior passes in a lattice or grid pattern to fill gaps.
4.  Break down the Site into smaller sections if the area is too large for one scan. Ensure strong overlap at boundaries so the sections connect consistently. Extremely large continuous coverage can reduce alignment stability and make gaps harder to diagnose.

------------------------------------------------------------------------

### Mixed<a href="#mixed" class="hash-link" aria-label="Direct link to Mixed" title="Direct link to Mixed">​</a>

An indoor and outdoor combination Site contains connected indoor and outdoor areas where scans need to align across environments as follows:

1.  Pause briefly at thresholds such as doors or entrances. These transition zones connect separate environments, so ensure features from both sides remain visible to maintain consistent alignment.
2.  Ensure features from both indoor and outdoor areas are visible at transitions.
3.  Adjust scanning pace for lighting changes, moving slower in darker areas.
4.  Maintain overlap with previous scans to connect multiple zones into a consistent 3D representation.

------------------------------------------------------------------------

</div>

</div>
