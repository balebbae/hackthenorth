# Backend contracts v0.1

Ownership: clients provide observations and localization; backend computes routes and instructions. No Niantic, ARKit, speech, computer-vision or frontend implementation is included. Python models live in `services/backend/app/models.py`. Machine-readable component schemas are in `backend.schema.json`; HTTP OpenAPI is served at `/openapi.json` (`/docs` for interactive documentation).

See [service-handoffs.md](service-handoffs.md) for the localization, map alignment, sensor, building-data, voice and deployment inputs needed from teammates. That document explicitly separates implemented messages from proposed semantic/audio extensions.

## Coordinates and localization

All positions are metres in the site's navigation graph coordinate frame. Y is vertical. Heading is degrees clockwise viewed from above: 0 = +Z, 90 = +X, 180 = -Z, 270 = -X. Heading must be in [0,360), coordinates finite. `timestamp` is UTC Unix seconds, not milliseconds. Clients must align coordinates before sending them; backend does not transform camera/local AR coordinates.

```json
{"x":0,"y":0,"z":0,"heading":0,"localized":true,"timestamp":1789819200,"localization":{"provider":"unknown","coordinate_frame":"site","map_id":null,"confidence":null,"tracking_status":null,"provider_metadata":{}}}
```

The sample timestamp must be replaced with the current time. Reject updates older than 15 seconds, more than 5 seconds in the future, or not newer than the preceding pose. Snapshots treat localization as stale after 15 seconds. Clients must independently expire old instructions when no updates arrive; the server does not proactively publish expiry messages. An unlocalized update suspends instructions; reacquisition resumes route progression. Navigation starts only with fresh localization within 3 metres of a waypoint.

Optional `pitch` and `roll` describe orientation in degrees supplied by the client; only heading is used for routing. `localization.provider_metadata` isolates arbitrary provider data. Providers may supply map IDs, tracking status and confidence without any Niantic-specific SDK dependency. Coordinate frame must match the graph. `AgentContextBuilder.localization_context` accepts separately configured operator descriptions of provider semantics, anchors and alignment; these are dynamic application context, not permanent prompt text. Confidence is reported, not interpreted by an invented provider-specific threshold.

## Sessions and HTTP

Create with `POST /sessions` body `{"site_id":"demo_building"}` (or `{}`). Save `session_id` from the 201 response. Multiple clients use the same ID to observe one navigation session. `GET /sessions/{id}` returns a snapshot; unknown IDs return 404. IDs are ephemeral, process-local demo capabilities, not authenticated accounts. Only `demo_building` is loaded by default.

`GET /destinations` returns `{site_id,destinations:[...]}`. Each destination has `id,name,entity_type,waypoint_id,description,aliases,tags,floor`; it refers to a graph waypoint. `POST /sessions/{id}/destination` body `{"destination_id":"east_elevator","accessible_only":true}` validates the ID and runs A*. `accessible_only` defaults true, excluding non-accessible edges. Setting a destination replaces the active route only after successful routing. No route returns 422 without discarding a previous route.

`GET /health` reports process liveness, not provider readiness. `GET /elastic/status` reports configuration, connectivity and lost historical writes. `POST /assistant/query` takes `{session_id,text}` (1–8000 characters). `POST /knowledge/documents` takes `{site_id,id,title,text}`; `POST /knowledge/upload` is multipart with `site_id`, `document_id`, and `file` (UTF-8 `.md`/`.txt` or text PDF, up to 5 MiB). External service failure is 503 for ingestion; assistant failures return an explicit unavailable answer. Validation errors are 422.

## Navigation WebSocket

Connect `WS /ws/sessions/{session_id}`. The server immediately sends a `session_state`. Every message is a JSON object with `type`. Unknown/malformed messages return `{type:"error",message:"..."}` without ending a valid session. Unknown sessions close with 1008. Client navigation messages are capped at 64 KiB.

Incoming messages:

```json
{"type":"hello"}
{"type":"pose_update","pose":{"x":0,"y":0,"z":0,"heading":0,"localized":true,"timestamp":1789819200}}
{"type":"set_destination","destination_id":"east_elevator","accessible_only":true}
{"type":"obstacle","direction":"front","distance_m":1.2,"description":"chair observed","timestamp":1789819200}
```

Obstacle direction: `front|left|right|back`, distance optional/null and nonnegative. Observations expire after 5 seconds; timestamps outside a 5-second window and non-increasing timestamps per direction are rejected. Null means unknown, never clear. Client handles immediate collision warnings independently and prioritizes them above conversational speech; backend broadcasts before historical indexing and does not route around obstacles.

Outgoing messages:

| Type | Fields beyond `type` |
| --- | --- |
| `session_state` | `session_id,site_id,pose,localization,navigation,obstacle_state` |
| `pose_update` | `pose` |
| `route_update` | Navigation fields below |
| `navigation_instruction` | Navigation fields below |
| `obstacle` | `direction,distance_m,description,timestamp` |
| `error` | `message` |

Navigation fields: `destination_id,route` (waypoint IDs), `route_index,next_waypoint_id,instruction,distance_remaining_m`. Instruction is `continue|turn_left|turn_right|turn_around|arrived|null`. A null instruction means no usable current guidance. Arrival/progression radius is 0.65 metres; turns use a 25-degree straight threshold and 150-degree turnaround threshold. Messages after a pose: `pose_update`, then `navigation_instruction`. After destination selection (HTTP, WS or agent): `route_update`, then `navigation_instruction`, broadcast to every navigation subscriber.

## Assistant WebSocket and provenance

Connect `WS /ws/sessions/{session_id}/assistant`; send:

```json
{"type":"assistant_message","text":"Take me to the elevator."}
```

Response:

```json
{"type":"assistant_response","text":"Navigating to the East Elevator.","sources":[{"type":"map_entity","id":"east_elevator"}],"actions":[{"type":"set_destination","destination_id":"east_elevator","accessible_only":true}],"tool_calls":[]}
```

Assistant messages capped at 16 KiB. `tool_calls` contains debug traces in this MVP; hide these in spoken UX. `sources` is the actual evidence available from tools and retained conversation turns, not a claim-by-claim citation map. Source types: `map_entity`, `building_knowledge` (chunk ID), `live_event`. `actions` contains only successfully executed actions in this turn. Inspect actions and navigation state, not answer wording, to determine whether navigation started. A later provider failure does not undo a successful action.

The core `BuildingAgentService.query(session_id,text)` is the future voice boundary. A speech adapter transcribes audio, calls it, then speaks `text`, respecting immediate obstacle priority. No audio codec, voice transport or microphone implementation is required now.

## Demo restrictions

Use a controlled demo network. There is no authentication/authorization, durable state, session TTL, production rate limiting, dynamic obstacle avoidance or multi-worker session sharing. Do not expose this as a production accessibility or collision-avoidance service. Teammates must agree on site alignment, localization freshness, observed obstacles, heading convention and session identity before connecting real devices.
