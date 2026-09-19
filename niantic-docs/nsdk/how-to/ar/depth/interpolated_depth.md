---
source: https://www.nianticspatial.com/docs/nsdk/how-to/ar/depth/interpolated_depth/
title: Displaying Interpolated Depth
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Displaying Interpolated Depth

</div>

In the previous tutorial, we learned how to display the **raw environment depth texture** from NSDK using Unity’s AROcclusionManager. That setup visualized the latest depth frame exactly as it was produced, aligned to the viewport through a simple **display matrix.**

In this tutorial, we extend that concept by enabling **depth warping** (also referred to as *interpolation*). This feature allows NSDK to *project* and *re-align* previously inferred depth images to the **current camera pose**, producing smoother and more temporally consistent results — even when new depth frames aren’t yet available.

------------------------------------------------------------------------

## 1. Overview of Warping (Interpolation)<a href="#1-overview-of-warping-interpolation" class="hash-link" aria-label="Direct link to 1. Overview of Warping (Interpolation)" title="Direct link to 1. Overview of Warping (Interpolation)">​</a>

When depth is inferred via NSDK’s neural network, each depth image is tied to the **camera pose** from the frame it was generated for. As the camera moves, NSDK can reproject that depth image forward in time to better match the current view.

<div class="theme-admonition theme-admonition-info admonition_xJq3 alert alert--info">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)</span>info

</div>

<div class="admonitionContent_BuS1">

In the previous tutorial, the transformation was purely **affine** (used `CameraMath.CalculateDisplayMatrix`). In this tutorial, it becomes **projective** — meaning the transformation includes distance-based warping caused by changes in camera position and orientation.

</div>

</div>

------------------------------------------------------------------------

## 2. Adding the NSDK Occlusion Extension<a href="#2-adding-the-nsdk-occlusion-extension" class="hash-link" aria-label="Direct link to 2. Adding the NSDK Occlusion Extension" title="Direct link to 2. Adding the NSDK Occlusion Extension">​</a>

Unlike Unity’s built-in AROcclusionManager, the **NsdkOcclusionExtension** component exposes NSDK-specific depth functionality, including interpolation.

1.  Select your **AR Camera** in the Unity scene.
2.  Add the **NsdkOcclusionExtension** component.
3.  Default settings are usually fine.
    - To *visualize interpolation more clearly*, try setting your **target frame rate** to **1 FPS**. This slows the updates to inference, letting you see how warping adjusts the depth between frames.

------------------------------------------------------------------------

## 3. Modified Script<a href="#3-modified-script" class="hash-link" aria-label="Direct link to 3. Modified Script" title="Direct link to 3. Modified Script">​</a>

### FitDepth.cs<a href="#fitdepthcs" class="hash-link" aria-label="Direct link to FitDepth.cs" title="Direct link to FitDepth.cs">​</a>

This version of the FitDepth component is very similar to the previous one — the key difference is that it uses the **NsdkOcclusionExtension** instead of the **AROcclusionManager**, and applies a combined **display + interpolation matrix.**

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
using NianticSpatial.NSDK.AR.Occlusion;
using UnityEngine.UI;

namespace UnityEngine.XR.ARFoundation.Samples
{
    /// <summary>
    /// This component overlays the environment depth texture to the full screen viewport (interpolated).
    /// </summary>
    public class FitDepth : MonoBehaviour
    {
        [SerializeField]
        private NsdkOcclusionExtension _occlusionExtension;

        [SerializeField]
        private Material _displayMaterial;

        [SerializeField]
        private RawImage _rawImage;

        private static readonly int s_displayMatrixId = Shader.PropertyToID("_DisplayMatrix");

        private void Awake()
        {
            Debug.Assert(_rawImage != null, "no raw image");

            // Assign the display material to the RawImage
            _rawImage.material = _displayMaterial;
            _rawImage.material.SetMatrix(s_displayMatrixId, Matrix4x4.identity);
        }

        private void Update()
        {
            // Get the latest depth texture
            var environmentDepthTexture = _occlusionExtension.DepthTexture;
            if (environmentDepthTexture == null)
                return;

            // This transformation combines both the display and interpolation matrices.
            var imageTransform = _occlusionExtension.DepthTransform;

            // Assign and update
            _rawImage.texture = environmentDepthTexture;
            _rawImage.material.SetMatrix(s_displayMatrixId, imageTransform);
        }
    }
}
```

</div>

</div>

<div class="theme-admonition theme-admonition-info admonition_xJq3 alert alert--info">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)</span>info

</div>

<div class="admonitionContent_BuS1">

**Key difference from the previous version:** Instead of computing the display matrix manually with `CameraMath.CalculateDisplayMatrix`, this version retrieves a **combined projective transform** (DepthTransform) directly from **NsdkOcclusionExtension**.

</div>

</div>

------------------------------------------------------------------------

## 4. Modified Shader<a href="#4-modified-shader" class="hash-link" aria-label="Direct link to 4. Modified Shader" title="Direct link to 4. Modified Shader">​</a>

### DepthFit<a href="#depthfit" class="hash-link" aria-label="Direct link to DepthFit" title="Direct link to DepthFit">​</a>

The shader logic remains mostly the same as before, with one crucial change: Because the new \_DisplayMatrix now includes a **projective transformation**, the UV coordinates must be divided by z to correctly convert from homogeneous space back to 2D texture space.

<div class="language-text codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` text
Shader "Unlit/DepthFit"
{
    Properties
    {
        _MainTex ("Texture", 2D) = "white" {}
    }
    SubShader
    {
        Tags { "RenderType"="Opaque" }
        LOD 100

        Pass
        {
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag

            #include "UnityCG.cginc"

            struct appdata
            {
                float4 vertex : POSITION;
                float2 uv : TEXCOORD0;
            };

            struct v2f
            {
                float3 uv : TEXCOORD0;
                float4 vertex : SV_POSITION;
            };

            sampler2D _MainTex;
            float4 _MainTex_ST;

            // Combined display + interpolation transform
            float4x4 _DisplayMatrix;

            // Convert HSV to RGB
            half4 HSVtoRGB(half3 arg1)
            {
                half4 K = half4(1.0h, 2.0h / 3.0h, 1.0h / 3.0h, 3.0h);
                half3 P = abs(frac(arg1.xxx + K.xyz) * 6.0h - K.www);
                half3 rgb = arg1.z * lerp(K.xxx, saturate(P - K.xxx), arg1.y);
                return half4(rgb, 1.0h);
            }

            v2f vert (appdata v)
            {
                v2f o;
                o.vertex = UnityObjectToClipPos(v.vertex);

                // Apply projective transformation to UVs
                o.uv = mul(_DisplayMatrix, float4(v.uv, 1.0f, 1.0f)).xyz;
                return o;
            }

            fixed4 frag (v2f i) : SV_Target
            {
                // Convert from homogeneous coordinates to screen-space UVs
                float2 uv = float2(i.uv.x / i.uv.z, i.uv.y / i.uv.z);

                // Sample the metric depth texture
                fixed depth = tex2D(_MainTex, uv).r;

                // Map depth range to color
                const float minDistance = 0;
                const float maxDistance = 8;
                half lerpFactor = (depth - minDistance) / (maxDistance - minDistance);
                half hue = lerp(0.70h, -0.15h, saturate(lerpFactor));
                if (hue < 0.0h) hue += 1.0h;

                half3 hsv = half3(hue, 0.9h, 0.6h);
                return HSVtoRGB(hsv);
            }
            ENDCG
        }
    }
}
```

</div>

</div>

------------------------------------------------------------------------

## 5. How it Works<a href="#5-how-it-works" class="hash-link" aria-label="Direct link to 5. How it Works" title="Direct link to 5. How it Works">​</a>

- The NsdkOcclusionExtension provides:
  - DepthTexture: the latest available depth frame.-
  - DepthTransform: a combined **display + interpolation matrix** that handles both screen alignment and motion-based reprojection.
  - The **shader** applies this transform per-vertex to reproject UVs based on the current camera pose.
  - During fragment shading, the **division by z** converts from homogeneous coordinates to normalized UVs — this step is essential because interpolation introduces projective distortion.
  - The **resulting image** “warps” to stay visually consistent with the camera’s perspective, even if the depth data was inferred from a slightly earlier frame.

------------------------------------------------------------------------

## 6. Result<a href="#6-result" class="hash-link" aria-label="Direct link to 6. Result" title="Direct link to 6. Result">​</a>

When you press Play, you’ll see the environment depth overlaid on the screen — but this time, it stays spatially aligned with the world even as the camera moves between frames. Lowering the frame rate (e.g., to 1 FPS) makes the interpolation effect especially visible: the depth map “warps” smoothly to follow the camera, even when a new inference hasn’t yet been produced.

</div>

</div>
