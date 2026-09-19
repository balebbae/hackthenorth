---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/ar/depth/display_depth/
title: Displaying Depth
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Displaying Depth

</div>

This tutorial explains how to visualize the **environment depth texture** provided by NSDK using Unity’s UI system. This can be useful for debugging or validating that depth data aligns correctly with the camera view.

------------------------------------------------------------------------

## 1. Overview<a href="#1-overview" class="hash-link" aria-label="Direct link to 1. Overview" title="Direct link to 1. Overview">​</a>

The goal is to overlay the current **environment depth texture** across the screen using a RawImage UI element and a simple unlit shader. The FitDepth component handles the logic for fetching the depth texture and computing the appropriate transformation matrix, while the **DepthFit** shader maps metric depth values into a visible color gradient.

------------------------------------------------------------------------

## 2. Scene Setup<a href="#2-scene-setup" class="hash-link" aria-label="Direct link to 2. Scene Setup" title="Direct link to 2. Scene Setup">​</a>

1.  **Add the AR Occlusion Manager**

    - Select your **AR Camera** object in the scene.
    - Add the **AROcclusionManager** component.
    - Configure the desired **Environment Depth Mode** (*Medium, Best, or Fastest*).

2.  **Add a UI Raw Image**

    - Go to **GameObject → UI → Raw Image.**
    - This creates a Canvas with a RawImage.
    - Stretch the RawImage to cover the entire screen.

3.  **Create the Display Material**

    - In the Project window, create a new **Material** and assign it the shader **Unlit/DepthFit** (defined below).
    - Name it something like `DepthFitMaterial`.
    - You’ll assign this material to the FitDepth component later.

------------------------------------------------------------------------

## 3. The FitDepth Component<a href="#3-the-fitdepth-component" class="hash-link" aria-label="Direct link to 3. The FitDepth Component" title="Direct link to 3. The FitDepth Component">​</a>

Create a new script called **FitDepth.cs** and add the following code:

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.XR.ARFoundation;

using UnityEngine;
using UnityEngine.UI;
using UnityEngine.XR.ARFoundation;

public class FitDepth : MonoBehaviour
{
    [SerializeField] private AROcclusionManager _occlusionManager;
    [SerializeField] private Material _displayMaterial;
    [SerializeField] private RawImage _rawImage;

    private static readonly int s_displayMatrixId = Shader.PropertyToID("_DisplayMatrix");

    private void Awake()
    {
        Debug.Assert(_rawImage != null, "no raw image");

        // Assign the display material to the RawImage
        _rawImage.material = _displayMaterial;

        // Optionally reset the display matrix
        _rawImage.material.SetMatrix(s_displayMatrixId, Matrix4x4.identity);
    }

    private void Update()
    {
        // Get the latest environment depth texture
        var environmentDepthTexture = _occlusionManager.environmentDepthTexture;
        if (environmentDepthTexture == null)
            return;

        // Compute the display matrix to align the depth image with the current viewport
        var displayMatrix = CameraMath.CalculateDisplayMatrix(
            environmentDepthTexture.width,
            environmentDepthTexture.height,
            Screen.width,
            Screen.height,
            XRDisplayContext.GetScreenOrientation()
        );

        // Assign the depth texture to the RawImage
        _rawImage.texture = environmentDepthTexture;

        // Update the display matrix in the shader
        _rawImage.material.SetMatrix(s_displayMatrixId, displayMatrix);
    }
}
```

</div>

</div>

Attach this component to a GameObject (e.g., the Canvas), then assign:

- Occlusion Manager: your AROcclusionManager
- Display Material: your new DepthFitMaterial
- Raw Image: the fullscreen RawImage element

**How It Works**

- The AROcclusionManager provides the latest environment depth texture each frame.
- The **CameraMath.CalculateDisplayMatrix** function computes a display matrix that aligns the texture with the current viewport, accounting for orientation and aspect ratio differences.
- This matrix is passed to the shader as \_DisplayMatrix, ensuring the depth map lines up with the camera feed.
- The **Raw Image** component displays the texture using the assigned material, updating in real-time as new depth frames arrive.

------------------------------------------------------------------------

## 4. The DepthFit Shader<a href="#4-the-depthfit-shader" class="hash-link" aria-label="Direct link to 4. The DepthFit Shader" title="Direct link to 4. The DepthFit Shader">​</a>

Create a new shader in Unity (right-click → *Create → Shader → Unlit Shader*) and replace its contents with:

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
                float2 uv : TEXCOORD0;
                float4 vertex : SV_POSITION;
            };

            sampler2D _MainTex;
            float4 _MainTex_ST;

            // Display transform matrix
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

                // Transform UVs to match the current viewport orientation
                o.uv = mul(_DisplayMatrix, float4(v.uv, 1.0f, 1.0f)).xy;
                return o;
            }

            fixed4 frag (v2f i) : SV_Target
            {
                // Sample the metric depth texture
                fixed depth = tex2D(_MainTex, i.uv).r;

                // Map depth range (in meters) to a color
                const float minDistance = 0;
                const float maxDistance = 8;
                half lerpFactor = (depth - minDistance) / (maxDistance - minDistance);

                // Encode depth as hue in HSV space for visualization
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

**How the Shader Works** The **DepthFit** shader is a simple unlit shader designed to visualize the depth map as color.

- **\_DisplayMatrix:** Provided by the FitDepth script, this matrix aligns the depth texture to the current screen orientation and aspect ratio. It ensures that what you see corresponds spatially to the AR camera view.
- **Vertex Stage (vert):** Each vertex’s UV coordinates are transformed by \_DisplayMatrix to correct for orientation and scaling before being passed to the fragment shader.
- **Fragment Stage (frag):**
  - Samples the depth texture (in meters).
  - Normalizes depth between minDistance and maxDistance.
  - Converts the normalized depth into an HSV hue value, mapping near values to warmer colors and far values to cooler ones.
  - Converts HSV to RGB for final display.

You can adjust the minDistance and maxDistance values to tune the visible range for your environment.

## 5. Result<a href="#5-result" class="hash-link" aria-label="Direct link to 5. Result" title="Direct link to 5. Result">​</a>

When running the scene, you’ll see a full-screen depth visualization overlaid on your display. Nearby objects will appear in warm colors (e.g., red/yellow), while distant objects shift toward cool colors (e.g., blue). The image will automatically align with the AR camera orientation and update in real time.

</div>

</div>
