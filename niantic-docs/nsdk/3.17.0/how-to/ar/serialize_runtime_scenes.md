---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/ar/serialize_runtime_scenes/
title: How to Serialize Content Placed at Runtime for Persistence
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Serialize Content Placed at Runtime for Persistence

</div>

This how-to demonstrates:

- Registering prefabs for spawning at runtime
- Storing transform and stateful data for restoring content in a future session
- Updating previously serialized data

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

This how-to uses manually constructed verbose strings to demonstrate serialization in a human-readable format. For proper serialization, we recommend using `[Serializable]` structs with a JSON serializer for a concrete structure or a binary serializer for compact storage.

</div>

</div>

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

You will need a Unity project with Lightship AR enabled. For more information, see [Installing ARDK 3.0](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/).

## Basic Concepts for Serialization of Runtime Content<a href="#basic-concepts-for-serialization-of-runtime-content" class="hash-link" aria-label="Direct link to Basic Concepts for Serialization of Runtime Content" title="Direct link to Basic Concepts for Serialization of Runtime Content">​</a>

As opposed to [Remote Content Authoring](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/real_world_location_ar/), where Unity scenes contain static placed objects in each `ARLocation`, runtime content serialization allows players to place content arbitrarily, then serialize the placed content into a known format so that it can be re-spawned in the future.

To serialize a player-constructed scene, this information is needed:

1.  The root transform that anchors the content (ARLocation, Image Target, etc);
    - This ensures that future deserialized content will be placed in the same location.
2.  All `GameObjects` that the player has placed;
3.  The type and state (transform and color, in this example) of each of these `GameObjects`.

This data is then compacted into a string or binary blob for retrieval the next time a player tracks that same `ARLocation`.

To deserialize the data and reconstruct the scene:

1.  Retrieve and instantiate each `GameObject` from the serialized data;
    - Each `GameObject` is placed under the same root transform (`ARLocation`) so that it appears in the same place.
2.  Apply the stateful data (transform, color, etc.) of each `GameObject`.

A sample scene, "VpsSceneSerialization", is provided to follow along with the scripts in this How-To.

## Registering Prefabs for Serialization<a href="#registering-prefabs-for-serialization" class="hash-link" aria-label="Direct link to Registering Prefabs for Serialization" title="Direct link to Registering Prefabs for Serialization">​</a>

The first problem to solve is gathering a list of all possible Prefabs that players can place. This is necessary to reconstruct the scene in the future.

The script `PersistentObject.cs` allows for finding spawnable Prefabs with a `GetComponent` and identifying each unique Prefab with a `PrefabId`.

Click to expand the PersistentObject class

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using UnityEngine;

public class PersistentObject : MonoBehaviour
{
  [SerializeField]
  private long _prefabId;

  public long PrefabId
  {
      get { return _prefabId; }
      internal set
      {
          _prefabId = value;
      }
  }

  ... // Serialization code
}
```

</div>

</div>

</div>

</div>

In the "VpsSceneSerialization" sample, there are two `PersistentObject` Prefabs, a cube and a sphere, assigned the `PrefabIds` 0 and 1 respectively. These `PersistentObjects` are then registered to a `PersistentObjectManager` to create a complete list of spawnable objects.

<img src="https://www.nianticspatial.com/docs/assets/images/persistent_objects_manager-a727e305cab09d32ae8dd0c764a70999.png" width="600" alt="Persistent Object Manager component" />

Click to expand the PersistentObjectManager class

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using System.Collections.Generic;
using System.Collections.ObjectModel;

public class PersistentObjectManager : MonoBehaviour
{
  [SerializeField]
  private List<PersistentObject> _persistentObjects = new List<PersistentObject>();

  public ReadOnlyCollection<PersistentObject> PersistentObjects => _persistentObjects.AsReadOnly();

  ... // Serialization and validation code
}
```

</div>

</div>

</div>

</div>

## Runtime Content Placement<a href="#runtime-content-placement" class="hash-link" aria-label="Direct link to Runtime Content Placement" title="Direct link to Runtime Content Placement">​</a>

The "VpsSceneSerialization" sample has two scripts; `PersistentContentDemoManager.cs` and `PersistentObjectPlacementBehaviour.cs`. These scripts manage spawning/destroying `Cubes` and `Spheres` whenever the player taps a plane or existing `GameObject`. Each game will have its own rules for spawning and destroying objects, so this How-To will not go into the details of making those scripts.

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Attention

</div>

<div class="admonitionContent_BuS1">

The following line of code implements an important detail - all spawned objects must be children of the `ARLocation` after instantiation! Make sure to do this when building your own application!

</div>

</div>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
// _root is a reference to the ARLocation that is currently tracked
spawned.transform.SetParent(_root.transform, true);
```

</div>

</div>

## Serializing and Storing Spawned Objects<a href="#serializing-and-storing-spawned-objects" class="hash-link" aria-label="Direct link to Serializing and Storing Spawned Objects" title="Direct link to Serializing and Storing Spawned Objects">​</a>

After the player has built their scene and is ready to serialize it for storage, we must create a list of all spawned `GameObjects`. There are several ways to do this, such as holding each `GameObject` in a `List`, or, as this sample does, using a `GetComponent<PersistentObject>` on the root `GameObject`.

Click to expand the updated PersistentObjectManager script

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
public class PersistentObjectManager : MonoBehaviour
{
  [SerializeField]
  private List<PersistentObject> _persistentObjects = new List<PersistentObject>();
  private const char Delimiter = ';';

  private readonly Dictionary<long, PersistentObject> _validObjects =
      new Dictionary<long, PersistentObject>();

  public string SerializeObjectsToString(GameObject rootGo = null)
  {
      var root = rootGo ? rootGo.transform : this.transform;
      var serializedObjects = new List<string>();
      ValidateAndRefreshPersistentObjectList();

      foreach (var child in root)
      {
          var persistentObject = ((Transform)child).GetComponent<PersistentObject>();
          if (persistentObject)
          {
              if (!_validObjects.Keys.ToList().Contains(persistentObject.PrefabId))
              {
                  continue;
              }

              serializedObjects.Add(persistentObject.SerializeObjectToString());
          }
      }

      return string.Join(Delimiter, serializedObjects.ToArray());
  }

  ... // Deserialization and validation code
}
```

</div>

</div>

</div>

</div>

For simplicity, this sample assumes that all Prefabs are children of the same root with no nested Prefabs. A real application may require better tracking and handling of Prefabs in the Hierarchy.

After gathering the `List` of `PersistentObjects`, each `PersistentObject` handles its own serialization into a string. These strings are then joined into a single string representation for storage.

Click to expand the updated PersistentObject script

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
public class PersistentObject : MonoBehaviour
{
  [SerializeField]
  private long _prefabId;

  public long PrefabId
  {
      get { return _prefabId; }
      internal set
      {
          _prefabId = value;
      }
  }

  public virtual string SerializeObjectToString()
  {
      return SimpleObjectToString();
  }

  protected string SimpleObjectToString()
  {
      var stringFormat = $"PrefabId: {_prefabId}, Position: {SerializeVector3(transform.localPosition)}, " +
                          $"Rotation: {SerializeQuaternion(transform.localRotation)}, Scale: {SerializeVector3(transform.localScale)}";

      return stringFormat;
  }

  private string SerializeVector3(Vector3 vector)
  {
      return string.Format("{0},{1},{2}", vector.x, vector.y, vector.z);
  }

  private string SerializeQuaternion(Quaternion quat)
  {
      return string.Format("{0},{1},{2},{3}", quat.x, quat.y, quat.z, quat.w);
  }

  ... // Deserialization code
}
```

</div>

</div>

</div>

</div>

Serialization returns a string that contains the relevant information for reconstructing the scene in a future session. In this example, the string looks like this:

`PrefabId: 0, Position: 0,0,0, Rotation: 0,-0.2323422,0,0.9726341, Scale: 1,1,1; PrefabId: 1, Position: 0,0,-1.689, Rotation: 0,0,0,1, Scale: 1,1,1`

The serialized string can then be stored in a backend or service for future retrieval. In this sample, the string is stored locally in `PlayerPrefs`, indexed by the name of the `ARLocation` Anchor.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
// Serialize the content and store it
var serializedString = PersistentObjectManager.SerializeObjectsToString(_root);

// _locationString is just persistentAnchor.name
PlayerPrefs.SetString(_locationString, serializedString);
```

</div>

</div>

## Extending PersistentObject to Store More State<a href="#extending-persistentobject-to-store-more-state" class="hash-link" aria-label="Direct link to Extending PersistentObject to Store More State" title="Direct link to Extending PersistentObject to Store More State">​</a>

In the "VpsSceneSerialization" sample, the Cube and Sphere are `ColorfulPersistentObjects` rather than base `PersistentObjects`. We extend the base class here to show serializing more custom stateful data on top of the basic transform.

Click to expand the ColorfulPersistentObject class

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using UnityEngine;

public class ColorfulPersistentObject : PersistentObject
{
  public override string SerializeObjectToString()
  {
      Color color;

      if (!Application.isPlaying)
      {
          // Have to use sharedMaterial in edit mode to not leak materials,
          // this means all gameobjects that share a material (default) will have the same color
          color = GetComponent<Renderer>().sharedMaterial.color;
      }
      else
      {
          color = GetComponent<Renderer>().material.color;
      }

      var colorStr = SerializeColor(color);
      return $"{base.SerializeObjectToString()}, Color: {colorStr}";
  }

  private string SerializeColor(Color color)
  {
      return $"{color.r},{color.g},{color.b},{color.a}";
  }

  ... // Deserialization code
}
```

</div>

</div>

</div>

</div>

This extension adds the `Color` field to each serialized `GameObject` for future restoration. Our sample serialized data string now looks like this:

`PrefabId: 0, Position: 0,0,0, Rotation: 0,-0.2323422,0,0.9726341, Scale: 1,1,1, Color: 1,1,1,1;PrefabId: 1, Position: 0,0,-1.689, Rotation: 0,0,0,1, Scale: 1,1,1, Color: 1,1,1,1`

## Restoring Serialized Content (Deserialization)<a href="#restoring-serialized-content-deserialization" class="hash-link" aria-label="Direct link to Restoring Serialized Content (Deserialization)" title="Direct link to Restoring Serialized Content (Deserialization)">​</a>

The serialized data string is then restored in a future session by `PersistentObjectManager.cs`.

Click to expand the updated PersistentObjectManager script

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text.RegularExpressions;

using UnityEngine;

public class PersistentObjectManager : MonoBehaviour
{
    [SerializeField]
    private List<PersistentObject> _persistentObjects = new List<PersistentObject>();

    public ReadOnlyCollection<PersistentObject> PersistentObjects => _persistentObjects.AsReadOnly();

    private const char Delimiter = ';';
    private const string PrefabIdReg = "PrefabId: (?<pid>\\d*)";
    private Regex _prefabIdRegex = new Regex(PrefabIdReg);

    private readonly Dictionary<long, PersistentObject> _validObjects =
        new Dictionary<long, PersistentObject>();

    ... // Serialization and validation code

    public List<GameObject> DeserializeObjectsFromString(string str, GameObject rootGo = null)
    {
        var spawnedObjects = new List<GameObject>();
        var root = rootGo ? rootGo.transform : this.transform;
        ValidateAndRefreshPersistentObjectList();

        var objs = str.Split(Delimiter);
        foreach (var serializedObj in objs)
        {
            var match = _prefabIdRegex.Match(serializedObj);
            if (!match.Success)
            {
                Debug.LogError("Could not parse out prefab id");
                continue;
            }

            var prefabId = long.Parse(match.Groups["pid"].Value);
            if (!_validObjects.ContainsKey(prefabId))
            {
                Debug.LogError($"Could not find prefab id {prefabId}");
                continue;
            }

            var persistentObject = _validObjects[prefabId];
            var newObject = Instantiate(persistentObject.gameObject, root);
            newObject.GetComponent<PersistentObject>().ApplyStringToObject(serializedObj);
            spawnedObjects.Add(newObject);
        }

        return spawnedObjects;
    }
}
```

</div>

</div>

</div>

</div>

The `DeserializeObjectsFromString` method takes a serialized string, splits it into individual `GameObjects`, then attempts to spawn registered `PersistentObjects` according to the recorded `PrefabIds`. Each `GameObject` string is then passed to the `PersistentObject` (or, in our example, `ColorfulPersistentObject`) for each `GameObject` to handle individually.

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>caution

</div>

<div class="admonitionContent_BuS1">

Make sure the list and contents of the `_persistentObjects` List stay consistent between serialization and deserialization! Otherwise, nonsense objects may spawn instead. When making a full game, we recommend using a versioning scheme to ensure that the List stays consistent between operations.

</div>

</div>

Click to reveal the updated ColorfulPersistentObject deserialization script

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using System.Text.RegularExpressions;

using UnityEngine;

public class ColorfulPersistentObject : PersistentObject
{
    private const string ColourReg = "Color: (?<color>.*,.*,.*,.*)";
    private static Regex _colourRegex = new Regex(ColourReg);

    ... // Serialization code

    public override void ApplyStringToObject(string str)
    {
        base.ApplyStringToObject(str);

        var match = _colourRegex.Match(str);
        if (!match.Success)
        {
            Debug.Log("No match");
            return;
        }

        var colorString = match.Groups["color"].Value;
        var color = DeserializeColor(colorString);
        ApplyColorToObject(color);
    }

    public void ApplyColorToObject(Color color)
    {
        Material mat;
        if (!Application.isPlaying)
        {
            // Have to use sharedMaterial in edit mode to not leak materials
            mat = GetComponent<Renderer>().sharedMaterial;
        }
        else
        {
            mat = GetComponent<Renderer>().material;
        }

        mat.color = color;
    }

    private Color DeserializeColor(string str)
    {
        // Deserialize a color from a string
        var split = str.Split(',');
        return new Color(float.Parse(split[0]), float.Parse(split[1]), float.Parse(split[2]),
            float.Parse(split[3]));
    }
}
```

</div>

</div>

</div>

</div>

The extension `ColorfulPersistentObject` handles the Color portion of the serialized string, then hands the rest to the base `PersistentObject` class to handle the transform data. This is inefficient, so let's clean it up:

Click to reveal the optimized PersistentObject script

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using System.Text.RegularExpressions;

using UnityEngine;

public class PersistentObject : MonoBehaviour
{
    [SerializeField]
    private long _prefabId;

    public long PrefabId
    {
        get { return _prefabId; }
        internal set
        {
            _prefabId = value;
        }
    }

    private static string regStr =
        "PrefabId: (?<pid>\\d*), Position: (?<pos>.*,.*,.*), Rotation: (?<rot>.*,.*,.*,.*), Scale: (?<scale>.*,.*,.*)";
    private static Regex regex = new Regex(regStr);

    public virtual void ApplyStringToObject(string str)
    {
        // Parse the string and apply it to the object
        SimpleApplyStringToObject(str);
    }

    protected void SimpleApplyStringToObject(string str)
    {
        var match = regex.Match(str);
        if (!match.Success)
        {
            Debug.Log("No match");
            return;
        }

        var prefabId = match.Groups["pid"].Value;
        var position = match.Groups["pos"].Value;
        var rotation = match.Groups["rot"].Value;
        var scale = match.Groups["scale"].Value;

        _prefabId = long.Parse(prefabId);
        transform.localPosition = DeserializeVector3(position);
        transform.localRotation = DeserializeQuaternion(rotation);
        transform.localScale = DeserializeVector3(scale);
    }

    private Vector3 DeserializeVector3(string str)
    {
        var split = str.Split(',');
        return new Vector3(float.Parse(split[0]), float.Parse(split[1]), float.Parse(split[2]));
    }

    private Quaternion DeserializeQuaternion(string str)
    {
        var split = str.Split(',');
        return new Quaternion(float.Parse(split[0]), float.Parse(split[1]), float.Parse(split[2]), float.Parse(split[3]));
    }
}
```

</div>

</div>

</div>

</div>

## Updating Serialized Data<a href="#updating-serialized-data" class="hash-link" aria-label="Direct link to Updating Serialized Data" title="Direct link to Updating Serialized Data">​</a>

To update serialized data, restore the data, allow players to modify the scene (delete `GameObjects`, move them, etc.), and then reserialize and overwrite the previously stored data. (For very large scenes, constantly reading and rewriting the entire scene is inefficient, so we recommend an incremental update system.)

## More Information<a href="#more-information" class="hash-link" aria-label="Direct link to More Information" title="Direct link to More Information">​</a>

For more information on using Location AR, see [Creating Location AR Experiences with VPS](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/lightship_vps/).

</div>

</div>
