---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/features/depth/
title: Niantic Spatial Depth
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Niantic Spatial Depth

</div>

## Understanding Depth in Augmented Reality<a href="#understanding-depth-in-augmented-reality" class="hash-link" aria-label="Direct link to Understanding Depth in Augmented Reality" title="Direct link to Understanding Depth in Augmented Reality">​</a>

Depth refers to the distance between the camera and the objects in a scene — essentially, how far away each pixel is from the viewer’s perspective. In augmented reality (AR), depth information is critical for enabling digital content to blend seamlessly with the real world. By understanding the geometry of a scene, AR applications can accurately place virtual objects behind, in front of, or on top of real-world surfaces. This creates realistic interactions such as proper occlusion, lighting effects, and physical collisions. Depth data also enhances spatial understanding, allowing experiences like environmental mapping and dynamic object placement to feel more natural and immersive.

## Depth in NSDK<a href="#depth-in-nsdk" class="hash-link" aria-label="Direct link to Depth in NSDK" title="Direct link to Depth in NSDK">​</a>

The Niantic Spatial SDK (NSDK) provides depth information to applications through two complementary methods. When supported and configured, NSDK directly uses the device’s LiDAR sensor to capture high-quality depth data. On devices without LiDAR, or when it is unavailable, NSDK infers depth from the camera feed using its built-in neural network, which is downloaded to the device on demand.

Depth images are delivered as **CPU-accessible buffers**, typically at a lower resolution than the camera images to balance performance and memory usage. Each pixel in a depth image represents a metric distance (in meters) from the camera to the corresponding point in the real world, and the image format is **32-bit floating point (float32)**.

Like camera images, depth data is stored in an **orientation-agnostic layout**, meaning it must be mapped to the current viewport resolution and orientation using a **display transformation matrix**. This transformation ensures that depth values align correctly with the visual content in the scene. On some platforms, NSDK performs this mapping automatically, simplifying integration for developers

In addition, NSDK provides a **temporal warping feature** to enhance temporal consistency between frames. Each inferred depth image is associated with the **world-space camera pose** corresponding to the AR image used during inference. NSDK includes utility functions that compute an **interpolation matrix**, which transforms normalized image coordinates to make the depth image appear as if it were captured from the current camera pose. For efficiency, the **display matrix** and the **interpolation (warp) matrix** can be combined, allowing the depth image to be **sampled only once** when rendering or processing.

</div>

</div>
