---
source: https://www.nianticspatial.com/docs/nsdk/how-to/ar/depth/display_depth/
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

    - Right click in your heirarchy window **UI → Raw Image.**
    - This creates a Canvas with a RawImage.
    - Stretch the RawImage to cover the entire screen.

3.  **Create the Display Material and Shader**

    - Right-click in the Project window → *Create → Shader → Unlit Shader*, name it `DepthFit`, and replace its contents with the code below.
    - Right-click in the Project window → *Create → Material*, name it something like `DepthFitMaterial`, and assign it the shader **Unlit/DepthFit** by dragging the shader on to the material.
    - You’ll assign this material to the FitDepth component later.

DepthFit Shader

<div>

<div class="collapsibleContent_i85q">

<div class="language-hlsl codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` hlsl
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
                half hue = lerp(-0.15h, 0.70h, saturate(lerpFactor));
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

</div>

</div>

------------------------------------------------------------------------

## 3. The FitDepth Component<a href="#3-the-fitdepth-component" class="hash-link" aria-label="Direct link to 3. The FitDepth Component" title="Direct link to 3. The FitDepth Component">​</a>

Create a new script called **FitDepth.cs** and add the following code:

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
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

        // Reset the display matrix
        _rawImage.material.SetMatrix(s_displayMatrixId, Matrix4x4.identity);
    }

    private void Update()
    {
        // Get the latest environment depth texture
        var environmentDepthTexture = _occlusionManager.environmentDepthTexture;
        if (environmentDepthTexture == null)
            return;

        // Assign the depth texture to the RawImage
        environmentDepthTexture.wrapMode = TextureWrapMode.Clamp;
        _rawImage.texture = environmentDepthTexture;

        // Compute and apply the display matrix to align depth with the current viewport
        _rawImage.material.SetMatrix(s_displayMatrixId, CalculateDisplayMatrix(
            environmentDepthTexture.width,
            environmentDepthTexture.height,
            Screen.width,
            Screen.height,
            Screen.orientation
        ));
    }

    // Computes a UV transform matrix that rotates and scales the depth texture
    // to match the current screen orientation and aspect ratio.
    private static Matrix4x4 CalculateDisplayMatrix(
        int imageWidth, int imageHeight,
        int screenWidth, int screenHeight,
        ScreenOrientation orientation)
    {
        bool rotate = orientation == ScreenOrientation.Portrait
                   || orientation == ScreenOrientation.PortraitUpsideDown;

        float iw = rotate ? imageHeight : imageWidth;
        float ih = rotate ? imageWidth  : imageHeight;
        float screenAspect = (float)screenWidth / screenHeight;
        float imageAspect  = iw / ih;
        float scale = screenAspect / imageAspect;

        float scaleX = scale < 1f ? 1f : 1f / scale;
        float scaleY = scale < 1f ? -scale : -1f;

        float angle = orientation switch
        {
            ScreenOrientation.Portrait           =>  90f,
            ScreenOrientation.PortraitUpsideDown => -90f,
            ScreenOrientation.LandscapeRight     => 180f,
            _                                    =>   0f,
        };

        return Matrix4x4.Translate(new Vector3(0.5f, 0.5f, 0f))
             * Matrix4x4.Scale(new Vector3(scaleX, scaleY, 1f))
             * Matrix4x4.Rotate(Quaternion.Euler(0f, 0f, angle))
             * Matrix4x4.Translate(new Vector3(-0.5f, -0.5f, 0f));
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

- The `AROcclusionManager` provides the latest environment depth texture each frame.
- `CalculateDisplayMatrix` computes a UV transform matrix using `Screen.orientation` and the texture/screen aspect ratios, rotating and scaling the UVs so the depth image aligns with the camera feed.
- This matrix is passed to the shader as `_DisplayMatrix`, ensuring the depth map lines up correctly regardless of device orientation.
- The **Raw Image** component displays the texture using the assigned material, updating in real-time as new depth frames arrive.
- The **DepthFit** shader visualizes the depth map as color. In the vertex stage, UVs are transformed by `_DisplayMatrix` to correct for orientation and aspect ratio. In the fragment stage, the metric depth value is normalized between `minDistance` and `maxDistance`, mapped to an HSV hue (warm colors for near, cool for far), and converted to RGB. You can adjust `minDistance` and `maxDistance` to tune the visible range for your environment.

## 4. Result<a href="#4-result" class="hash-link" aria-label="Direct link to 4. Result" title="Direct link to 4. Result">​</a>

When running the scene, you’ll see a full-screen depth visualization overlaid on your display. Nearby objects will appear in warm colors (e.g., red/yellow), while distant objects shift toward cool colors (e.g., blue). The image will automatically align with the AR camera orientation and update in real time.

</div>

</div>
