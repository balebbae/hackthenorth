---
source: https://www.nianticspatial.com/docs/nsdk/how-to/ar/query_semantics_real_objects/
title: How to Query Scene Segmentation and Highlight Semantic Channels
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Query Scene Segmentation and Highlight Semantic Channels

</div>

<img src="https://www.nianticspatial.com/docs/assets/images/semantics_query_playback-58817d3855cde60712c2f313656486b5.gif" style="width:100.0%" alt="Viewing semantic information in an AR app with playback" />

This how-to covers:

- Querying scene segmentation to detect what is on-screen at a point the player touches;
- Highlighting a specific semantic channel based on the last point the player touched;
- Available APIs for querying semantic information.

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

You will need a Unity project with NSDK installed and a set-up basic AR scene. For more information, see [Set up the Niantic SDK for Unity](https://www.nianticspatial.com/docs/nsdk/setup/#set-up-the-niantic-sdk-for-unity) and [Set up a basic AR scene](https://www.nianticspatial.com/docs/nsdk/setup/#set-up-a-basic-ar-scene).

## Steps<a href="#steps" class="hash-link" aria-label="Direct link to Steps" title="Direct link to Steps">​</a>

### Adding UI Elements<a href="#adding-ui-elements" class="hash-link" aria-label="Direct link to Adding UI Elements" title="Direct link to Adding UI Elements">​</a>

Before implementing the script that handles semantic querying, we need to prepare the UI elements that will display semantic information to the user. For this example, we will create a text field to display the semantic channel name and a `RawImage` to handle shader output.

To create the UI elements:

1.  In the **Hierarchy**, right-click in your AR scene, then mouse over **UI** and select **Raw Image** to add a `RawImage` to the scene.
2.  Repeat this process, but select **Text-TextMeshPro** to add a text field. If a TMP Importer pop-up appears, click **Import TMP Essentials** to finish adding the text field.
3.  Select the text field in the **Hierarchy**, then, in the **Inspector**, set its position to (0, 0, 0).
4.  In the **Rect Transform** menu in the **Inspector**, click the square in the top-left corner to open the **Anchor Presets** menu. Hold Shift and click the center option to anchor the text in the middle of the screen.

<img src="https://www.nianticspatial.com/docs/assets/images/text_transform-acef39269a79a0b778394596a6a230e0.png" width="417" alt="An image of the Unity UI highlighting the Center Transform button" />

5.  Select the `RawImage`, then open the **Anchor Presets** menu again. Hold the Option key (Alt on Windows) and select the bottom-right square to place the `RawImage` in the correct spot and stretch it to cover the entire screen.

<img src="https://www.nianticspatial.com/docs/assets/images/anchor_presets_stretch-11b09df550e1759d4368e090634f8478.png" width="417" alt="An image of the Unity UI highlighting the Stretch option in the Anchor Presets menu" />

### Adding the Semantic Segmentation Manager<a href="#adding-the-semantic-segmentation-manager" class="hash-link" aria-label="Direct link to Adding the Semantic Segmentation Manager" title="Direct link to Adding the Semantic Segmentation Manager">​</a>

The Semantic Segmentation Manager provides access to the Semantics subsystem and serves semantic predictions that other parts of your code can access. (For more detailed information, see the [Scene Segmentation Features page](https://www.nianticspatial.com/docs/nsdk/features/semantics/).)

To add a Semantic Segmentation Manager to your scene:

1.  Right-click in the **Hierarchy** window, then select **Create Empty** to add an empty `GameObject` to the scene. Name it **Segmentation Manager**.
2.  Select the new `GameObject`, then, in the **Inspector** window, click **Add Component**, search for "AR Semantic Segmentation Manager", and select it to add it as a Component.

<img src="https://www.nianticspatial.com/docs/assets/images/manager-7993b004e5a4cd250d2f4dbe24cfa974.png" width="417" alt="An example of a game object containing the scene segmentation segmentation manager" />

### Adding the Alignment Shader<a href="#adding-the-alignment-shader" class="hash-link" aria-label="Direct link to Adding the Alignment Shader" title="Direct link to Adding the Alignment Shader">​</a>

To make sure our semantic information aligns properly on-screen, we need to use the display matrix and rotate the buffer returned by the camera. Using an overlay shader, we can get the display transform from the **ARCameraManager** frame update event and use it to transform the UVs into the correct screen space. Then, we render the semantic information into the `RawImage` we made earlier and display it to the user.

To create the shader:

1.  Create a shader and material:
    1.  In the **Project** window, open the **Assets** directory.
    2.  Right-click in the **Assets** directory, then mouse over **Create** and select **Unlit Shader** from the **Shader** menu. Name it **SemanticShader**.
    3.  Repeat this process, but select **Material** from the **Create** menu to create a new material. Name it **SemanticMaterial**, then drag and drop **SemanticShader** onto the new Material to associate them.
2.  Add the shader code:
    1.  Select **SemanticShader** from the **Assets** directory, then, in the **Inspector** window, click **Open** to edit the shader code.
    2.  Replace the default shader with the alignment shader code.

Click to expand the alignment shader code

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Shader "Unlit/SemanticShader"
{
    Properties
    {
        _MainTex ("_MainTex", 2D) = "white" {}
        _SemanticTex ("_SemanticTex", 2D) = "red" {}
        _Color ("_Color", Color) = (1,1,1,1)
    }
    SubShader
    {
        Tags {"Queue"="Transparent" "IgnoreProjector"="True" "RenderType"="Transparent"}
        Blend SrcAlpha OneMinusSrcAlpha
        // No culling or depth
        Cull Off ZWrite Off ZTest Always
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
                float3 texcoord : TEXCOORD1;
                float4 vertex : SV_POSITION;

            };

            float4x4 _SemanticMat;

            v2f vert (appdata v)
            {
                v2f o;
                o.vertex = UnityObjectToClipPos(v.vertex);
                o.uv = v.uv;

                //we need to adjust our image to the correct rotation and aspect.
                o.texcoord = mul(_SemanticMat, float4(v.uv, 1.0f, 1.0f)).xyz;
                
                return o;
            }

            sampler2D _MainTex;
            sampler2D _SemanticTex;
            fixed4 _Color;

            fixed4 frag (v2f i) : SV_Target
            {
                //convert coordinate space
                float2 semanticUV = float2(i.texcoord.x / i.texcoord.z, i.texcoord.y / i.texcoord.z);
                
                float4 semanticCol = tex2D(_SemanticTex, semanticUV);
                return float4(_Color.r,_Color.g,_Color.b,semanticCol.r*_Color.a);
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

3.  Set up the material properties:
    1.  Once you replace the shader code, the material will populate with properties. To access them, select **SemanticMaterial** from the **Assets** directory, then look in the **Inspector** window.
    2.  Click the color swatch to the right of the **Color** property in the **Inspector** to set the material color and alpha. Set the alpha value to `128` (roughly 50%) to make sure the semantic color filter is translucent enough to see the real-world object beneath it. The color is up to you!

<img src="https://www.nianticspatial.com/docs/assets/images/semantics_overlay_material-7aed5f6ce748d7a500f8484bc913f056.png" width="400" alt="The material inspector" />

### Creating the Query Script<a href="#creating-the-query-script" class="hash-link" aria-label="Direct link to Creating the Query Script" title="Direct link to Creating the Query Script">​</a>

To get semantic information when the player touches the screen, we need a script that queries the Semantic Segmentation Manager and displays the information when the player touches an area.

To create the query script:

1.  Make the script file and add it to the Segmentation Manager:
    1.  In the **Project** window, select the **Assets** directory, then right-click inside the window, mouse over **Create**, and select **C# Script**. Name the new script **SemanticQuerying**.
    2.  In the **Hierarchy**, select the **Segmentation Manager** `GameObject`, then, in the **Inspector** window, click **Add Component**. Search for "script", then select **New Script** and choose the **SemanticQuerying** script.
2.  Add code to the script:
    1.  Double-click the **SemanticQuerying** script in the **Assets** directory to open it in a text editor, then copy the following script into it. (See the [Appendix](#appendix-how-does-the-query-script-work) for details on how each part of the script works.)

Click to reveal the SemanticQuerying script

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using NianticSpatial.NSDK.AR.Semantics;
using TMPro;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.XR.ARFoundation;

public class SemanticQuerying : MonoBehaviour
{
    public ARCameraManager _cameraMan;
    public ARSemanticSegmentationManager _semanticMan;

    public TMP_Text _text;
    public RawImage _image;
    public Material _material;

    private string _channel = "ground";

    void OnEnable()
    {
        _cameraMan.frameReceived += OnCameraFrameUpdate;
    }

    private void OnDisable()
    {
        _cameraMan.frameReceived -= OnCameraFrameUpdate;
    }

    private void OnCameraFrameUpdate(ARCameraFrameEventArgs args)
    {
        if (!_semanticMan.subsystem.running)
        {
            return;
        }

        //get the semantic texture
        Matrix4x4 mat = Matrix4x4.identity;
        var texture = _semanticMan.GetSemanticChannelTexture(_channel, out mat);

        if (texture)
        {
            //the texture needs to be aligned to the screen so get the display matrix
            //and use a shader that will rotate/scale things.
            _image.material = _material;
            _image.material.SetTexture("_SemanticTex", texture);
            _image.material.SetMatrix("_SemanticMat", mat);
        }
    }

    private float _timer = 0.0f;

    void Update()
    {
        if (!_semanticMan.subsystem.running)
        {
            return;
        }

        //Unity Editor vs On Device
        if (Input.GetMouseButtonDown(0) || (Input.touches.Length > 0))
        {
            var pos = Input.mousePosition;

            if (pos.x > 0 && pos.x < Screen.width)
            {
                if (pos.y > 0 && pos.y < Screen.height)
                {
                    _timer += Time.deltaTime;
                    if (_timer > 0.05f)
                    {
                        var list = _semanticMan.GetChannelNamesAt((int)pos.x, (int)pos.y);

                        if (list.Count > 0)
                        {
                            _channel = list[0];
                            _text.text = _channel;
                        }
                        else
                        {
                            _text.text = "?";
                        }

                        _timer = 0.0f;
                    }
                }
            }
        }
    }
}
```

</div>

</div>

</div>

</div>

## Assigning Script Variables<a href="#assigning-script-variables" class="hash-link" aria-label="Direct link to Assigning Script Variables" title="Direct link to Assigning Script Variables">​</a>

Before the script can run, we need to assign its variables in Unity so that the script and UI elements can talk to each other.

To assign the variables:

1.  In the **Hierarchy**, select the **Segmentation Manager** `GameObject`.
2.  In the **Inspector** window, assign the variables in the `SemanticQuerying` script Component by dragging and dropping each item to its respective field:
    1.  The scene's `MainCamera` to the **Camera Man** field;
    2.  The `SegmentationManager` object to the **Segmentation Man** field;
    3.  The `Text-TMP` object to the **Text** field;
    4.  The `RawImage` object to the **Image** field;
    5.  `SemanticMaterial` from the **Assets** directory to the **Material** field.

<img src="https://www.nianticspatial.com/docs/assets/images/querying_script-a2badd487bb9fec326b26b0c40832416.png" width="417" alt="the Semantic Querying script after assigning the script variables" />

## Build and Test<a href="#build-and-test" class="hash-link" aria-label="Direct link to Build and Test" title="Direct link to Build and Test">​</a>

Once you have added the script and populated it with code, you can now test using a playback dataset. For instructions on setting up your editor to play back a recorded dataset in the Unity editor, see [How to Setup Playback](https://www.nianticspatial.com/docs/nsdk/how-to/playback/setting_up_playback/#1--download-or-create-a-recording-to-use-for-playback). If using <a href="https://github.com/nianticspatial/nsdk-samples-csharp/releases/download/3.1.0/Relic_PlaybackDataset.tgz" target="_blank" rel="noopener noreferrer">this Playback dataset from the NSDK Github</a>, your output should look something like this:

<img src="https://www.nianticspatial.com/docs/assets/images/semantics_query_playback-58817d3855cde60712c2f313656486b5.gif" style="width:30.0%" alt="Viewing semantic information in an AR app" />

You can also now build to device and test in a real-world environment:

<img src="https://www.nianticspatial.com/docs/assets/images/semantics_query-1daad5c3ff7c147860f9a3170a8b1939.gif" style="width:30.0%" alt="Viewing semantic information in an AR app" />

## Appendix: How Does the Query Script Work?<a href="#appendix-how-does-the-query-script-work" class="hash-link" aria-label="Direct link to Appendix: How Does the Query Script Work?" title="Direct link to Appendix: How Does the Query Script Work?">​</a>

### What's On The Screen?<a href="#whats-on-the-screen" class="hash-link" aria-label="Direct link to What&#39;s On The Screen?" title="Direct link to What&#39;s On The Screen?">​</a>

The core of the querying script checks on each frame if the user is touching or clicking. After making sure the touch/click is legal by checking the position and amount of frames it took, we get the semantic channel at the point the user chose and show the result using a text box.

Click here to reveal the channel names snippet

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using NianticSpatial.NSDK.AR.Semantics;
using TMPro;
using UnityEngine;

public class SemanticQuerying : MonoBehaviour
{
    public ARSemanticSegmentationManager _semanticMan;
    public TMP_Text _text;

    void Update()
    {
        if (!_semanticMan.subsystem.running)
        {
            return;
        }

        //Unity Editor vs On Device
        if (Input.GetMouseButtonDown(0) || (Input.touches.Length > 0))
        {
            var pos = Input.mousePosition;

            if (pos.x > 0 && pos.x < Screen.width)
            {
                if (pos.y > 0 && pos.y < Screen.height)
                {
                    _timer += Time.deltaTime;
                    if (_timer > 0.05f)
                    {
                        var list = _semanticMan.GetChannelNamesAt((int)pos.x, (int)pos.y);

                        if (list.Count > 0)
                        {
                            _channel = list[0];
                            _text.text = _channel;
                        }
                        else
                        {
                            _text.text = "?";
                        }

                        _timer = 0.0f;
                    }
                }
            }
        }
    }
}
```

</div>

</div>

</div>

</div>

### Highlighting the Semantic Class<a href="#highlighting-the-semantic-class" class="hash-link" aria-label="Direct link to Highlighting the Semantic Class" title="Direct link to Highlighting the Semantic Class">​</a>

Using `GetSemanticChannelTexture`, we can get the texture for the semantic channel we're looking at and output the results to the `RawImage` UI element. Because this function outputs a `Matrix4x4` texture, we then transform it in the shader, as explained in [Adding the Alignment Shader](#adding-the-alignment-shader).

Click to reveal the texture output snippet

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using NianticSpatial.NSDK.AR.Semantics;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

public class SemanticQuerying : MonoBehaviour
{
    public ARSemanticSegmentationManager _semanticMan;
    public TMP_Text _text;
    public RawImage _image;

    void Update()
    {
        if (!_semanticMan.subsystem.running)
        {
            return;
        }

        var list = _semanticMan.GetChannelNamesAt(Screen.width / 2, Screen.height / 2);
        _text.text="";
        foreach (var i in list)
            _text.text += i;

        //this will highlight the class it found
        if (list.Count > 0)
        {
            //just show the first one.
            _image.texture = _semanticMan.GetSemanticChannelTexture(list[0], out Matrix4x4 mat);
        }
    }
}
```

</div>

</div>

</div>

</div>

</div>

</div>
