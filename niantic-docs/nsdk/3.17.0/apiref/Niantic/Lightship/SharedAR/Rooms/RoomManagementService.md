---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Rooms/RoomManagementService/
title: class RoomManagementService
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class RoomManagementService

</div>

(Niantic.Lightship.SharedAR.Rooms.RoomManagementService)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

The RoomManagementService provides interface to access Room Management Service backend to create, remove, find [Rooms](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Rooms/). A room is an entity to connect multiple peers through server relayed network.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
class RoomManagementService {
 public:
   
     struct GetOrCreateRoomAsyncTaskResult;

     // methods
   
     static RoomManagementServiceStatus CreateRoom(
          RoomParams roomParams,
          out IRoom outRoom
       );
    
     static void TryReinitializeRoomManagementService();
     static RoomManagementServiceStatus DeleteRoom(string roomId);
        static RoomManagementServiceStatus GetRoom(string roomId, out IRoom outRoom);
 
     static RoomManagementServiceStatus QueryRoomsByName(
            string name,
          out List<IRoom> rooms
       );
    
     static RoomManagementServiceStatus GetAllRooms(out List<IRoom> rooms);
   
     static RoomManagementServiceStatus GetOrCreateRoomForName(
          RoomParams roomParams,
          out IRoom outRoom
       );
    
     static void GetOrCreateRoomAsync(
         string roomName,
          string roomDesc,
          uint roomCapacity,
            GetOrCreateRoomCallback doneCb
        );
    
     static async Task<GetOrCreateRoomAsyncTaskResult> GetOrCreateRoomAsync(
           string roomName,
          string roomDescription,
           uint roomCapacity
       );
    
     delegate void GetOrCreateRoomCallback(
            RoomManagementServiceStatus status,
         string room_id
      );
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

The RoomManagementService provides interface to access Room Management Service backend to create, remove, find [Rooms](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Rooms/). A room is an entity to connect multiple peers through server relayed network.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### CreateRoom<a href="#CreateRoom" class="hash-link" aria-label="Direct link to CreateRoom" title="Direct link to CreateRoom">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static RoomManagementServiceStatus CreateRoom(
      RoomParams roomParams,
      out IRoom outRoom
   )
```

</div>

</div>

Create a new room on the server.

    **Parameters**:

    `roomParams` - Parameters of the room

    `outRoom` - Created room as [IRoom](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Rooms/IRoom/) object. null if failed to create.

    **Returns:**

    Status of the operation

#### DeleteRoom<a href="#DeleteRoom" class="hash-link" aria-label="Direct link to DeleteRoom" title="Direct link to DeleteRoom">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static RoomManagementServiceStatus DeleteRoom(string roomId)
```

</div>

</div>

Delete a room on the server.

    **Parameters**:

    `roomId` - Room ID of the room to delete

    **Returns:**

    Status of the operation

#### GetRoom<a href="#GetRoom" class="hash-link" aria-label="Direct link to GetRoom" title="Direct link to GetRoom">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static RoomManagementServiceStatus GetRoom(string roomId, out IRoom outRoom)
```

</div>

</div>

Get a room by Room ID on the server

    **Parameters**:

    `roomId` - Room ID as a string

    `outRoom` - Found Room object. Null if operation failed or room ID not found\<//param\>

    **Returns:**

    Status of the operation

#### QueryRoomsByName<a href="#QueryRoomsByName" class="hash-link" aria-label="Direct link to QueryRoomsByName" title="Direct link to QueryRoomsByName">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static RoomManagementServiceStatus QueryRoomsByName(
        string name,
      out List<IRoom> rooms
   )
```

</div>

</div>

Query room(s) by name on the server

    **Parameters**:

    `name` - Name of the room to find

    `rooms` - A List of rooms which has matching name

    **Returns:**

    Status of the operation

#### GetAllRooms<a href="#GetAllRooms" class="hash-link" aria-label="Direct link to GetAllRooms" title="Direct link to GetAllRooms">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static RoomManagementServiceStatus GetAllRooms(out List<IRoom> rooms)
```

</div>

</div>

Get all rooms on the server, which was created by this app

    **Parameters**:

    `rooms` - List of rooms available for this app

    **Returns:**

    Status of the operation

#### GetOrCreateRoomForName<a href="#GetOrCreateRoomForName" class="hash-link" aria-label="Direct link to GetOrCreateRoomForName" title="Direct link to GetOrCreateRoomForName">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static RoomManagementServiceStatus GetOrCreateRoomForName(
      RoomParams roomParams,
      out IRoom outRoom
   )
```

</div>

</div>

Get a [IRoom](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Rooms/IRoom/) object that has a given name on the server. If no room found with the name, create a new room using given room parameters

    **Parameters**:

    `roomParams` - Room parameters of the room to get or create

    `outRoom` - [IRoom](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Rooms/IRoom/) object. null if server operarion failed

    **Returns:**

    Status of the operation

#### GetOrCreateRoomAsync<a href="#GetOrCreateRoomAsync" class="hash-link" aria-label="Direct link to GetOrCreateRoomAsync" title="Direct link to GetOrCreateRoomAsync">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static void GetOrCreateRoomAsync(
     string roomName,
      string roomDesc,
      uint roomCapacity,
        GetOrCreateRoomCallback doneCb
    )
```

</div>

</div>

An async implementation of the GetOrCreateRoom request. This function checks to see if any rooms of the name "roomName" exist and if not, it creates the room. Once the function has a valid RoomID from either of these operations, it returns it via the "doneCb". The "doneCb" has two parameters. The first is a response code in case there are service issues, and the second parameter is the room id that was found/created.

    **Parameters**:

    `roomName` - Room name to check for

    `roomDesc` - Room description to use if a room needs to be made

    `roomCapacity` - Room capacity to use if a room needs to be made

    `doneCb` - Callback that the function calls after it errors or receives a valid room id.

#### GetOrCreateRoomAsync<a href="#GetOrCreateRoomAsync" class="hash-link" aria-label="Direct link to GetOrCreateRoomAsync" title="Direct link to GetOrCreateRoomAsync">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static async Task<GetOrCreateRoomAsyncTaskResult> GetOrCreateRoomAsync(
       string roomName,
      string roomDescription,
       uint roomCapacity
   )
```

</div>

</div>

An async implementation of the GetOrCreateRoom request. This function checks to see if any rooms of the name "roomName" exist and if not, it creates the room. This variant returns a Task so it can be `await` -ed by C#'s `async/await` feature. The task is given two results, the status of the request and, if successful, the roomId for the request.

    **Parameters**:

    `roomName` - Room name to check for

    `roomDescription` - Room description to use if a room needs to be made

    `roomCapacity` - Room capacity to use if a room needs to be made

    **Returns:**

    Task with the request status and the roomId on successful requests

</div>

</div>
