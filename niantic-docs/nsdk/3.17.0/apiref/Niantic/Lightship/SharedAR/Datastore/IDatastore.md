---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Datastore/IDatastore/
title: interface IDatastore
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# interface IDatastore

</div>

(Niantic.Lightship.SharedAR.Datastore.IDatastore)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Server-backed data storage that is associated with sessions or rooms. Peers can set, update, and delete Key/Value pairs, and have the server notify all other peers in the session when updates occur.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   interface IDatastore: IDisposable {
     // events
    
     event DatastoreCallback();

       // methods
   
     void SetData(UInt32 requestId, string key, byte[] value);
       void GetData(UInt32 requestId, string key);
     void DeleteData(UInt32 requestId, string key);
  };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Server-backed data storage that is associated with sessions or rooms. Peers can set, update, and delete Key/Value pairs, and have the server notify all other peers in the session when updates occur.

### Events<a href="#events" class="hash-link" aria-label="Direct link to Events" title="Direct link to Events">​</a>

#### DatastoreCallback<a href="#DatastoreCallback" class="hash-link" aria-label="Direct link to DatastoreCallback" title="Direct link to DatastoreCallback">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
event DatastoreCallback()
```

</div>

</div>

Callback to listen to server response or changes This is called either when receiving a response from the own request, or data changed on server side

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### SetData<a href="#SetData" class="hash-link" aria-label="Direct link to SetData" title="Direct link to SetData">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void SetData(UInt32 requestId, string key, byte[] value)
```

</div>

</div>

Set/Add data into the server storage asynchronously

    **Parameters**:

    `requestId` - ID to distinguish to identify th originated request in callback

    `key` - Key of the data

    `value` - Value to set

#### GetData<a href="#GetData" class="hash-link" aria-label="Direct link to GetData" title="Direct link to GetData">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void GetData(UInt32 requestId, string key)
```

</div>

</div>

Get data from the server storage asynchronously

    **Parameters**:

    `requestId` - ID to distinguish to identify th originated request in callback

    `key` - Key of the data

#### DeleteData<a href="#DeleteData" class="hash-link" aria-label="Direct link to DeleteData" title="Direct link to DeleteData">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void DeleteData(UInt32 requestId, string key)
```

</div>

</div>

Delete the key-value pair from the server storage asynchronously

    **Parameters**:

    `requestId` - ID to distinguish to identify th originated request in callback

    `key` - Key of the data to delete

</div>

</div>
