# Service handoffs: localization, semantics, knowledge and voice

Status: current backend contracts plus explicitly marked proposals. This document does not implement Niantic, native clients, audio streaming, or scene segmentation ingestion. Existing wire formats are in [backend.md](backend.md); component schemas are in [backend.schema.json](backend.schema.json).

## What runs today

| Component | Current responsibility | Status |
| --- | --- | --- |
| Local FastAPI / Uvicorn | Session state, HTTP, navigation and assistant WebSockets, agent tool execution, A* | Implemented; localhost demos use this |
| Modal | Host that same FastAPI application for remote devices with HTTPS/WSS | Deployment definition exists; no deployment verified in this task |
| Elasticsearch | Building documents, semantic map entities, historical events; BM25 + dense + RRF; ES\|QL | Implemented; user reported successful seed and place retrieval |
| OpenAI Responses API | Text reasoning, function tools, contextual replies and destination actions | Implemented; live location/place tool calls observed |
| OpenAI embeddings API | Document/query vectors, called through Elasticsearch's OpenAI inference service | Configured as `htn-openai-embeddings`, 1024 dimensions |
| Niantic client | Localization and optional supported perception features | Client-owned; not implemented in backend |
| OpenAI audio / Realtime | Streaming microphone/speech interaction | Not implemented |

AWS ElastiCache, Redis and a separate cache service are not used. Current pose, route and conversation history stay in process memory. Elasticsearch stores searchable knowledge/history, not the authoritative live pose. Modal currently specifies one container because session state is not shared between workers. Restarts/redeployments lose sessions.

## Localization owner: required for the first real-device navigation demo

Deliver these artifacts to the backend owner before replacing simulator poses:

1. Exact SDK product, version, platform, enabled features and a recorded localization result with credentials removed. Confirm the APIs actually available on the target iPhone/build; do not infer feature parity from Unity documentation.
2. The Niantic Site/map/anchor IDs and their mapping to our graph's `site_id` and `coordinate_frame`. Include a map revision identifier. The backend currently loads one graph via `GRAPH_PATH`; the simulator graph is `demo_building`. A different site requires a corresponding graph/configuration.
3. The coordinate alignment from SDK/AR coordinates to graph coordinates: origin, scale, axes, handedness, units, transform direction and matrix convention. Provide a transform or already converted sample poses. The client performs conversion; the backend currently performs none. Verify against at least two known positions and a known facing direction in the real site. Distinguish the pose of an anchor in AR space from the pose of the device in map space.
4. A localization-state mapping showing when the client will set `localized=true/false`. With VPS2, inspect the tracked Site anchor as well as device status; coarse global position alone is not sufficient for our mapped indoor route. Send loss immediately. Do not assume a numerical confidence exists; use null if absent.
5. Validated real waypoints, walkable edges and destination annotations, including accessibility evidence and disconnected/blocked segments. A splat/mesh or VPS localization does not automatically provide a routing graph. Backend owner integrates graph files under `maps/navigation/` and indexes entities.

### Implemented pose transport

Create a session with `POST /sessions` and the configured graph `site_id`. Share the returned `session_id` between the localization client, destination selector and voice client. Send to `WS /ws/sessions/{session_id}`:

```json
{
  "type": "pose_update",
  "pose": {
    "x": 0.0,
    "y": 0.0,
    "z": 0.0,
    "heading": 0.0,
    "localized": true,
    "timestamp": 1789819200,
    "localization": {
      "provider": "niantic_spatial",
      "coordinate_frame": "site",
      "map_id": "REPLACE_WITH_REAL_MAP_ID",
      "confidence": null,
      "tracking_status": "REPLACE_WITH_ACTUAL_STATUS",
      "provider_metadata": {
        "sdk_version": "REPLACE_WITH_ACTUAL_VERSION",
        "site_id": "REPLACE_WITH_NIANTIC_SITE_ID",
        "anchor_id": "REPLACE_WITH_REAL_ANCHOR_ID",
        "map_revision": "REPLACE_WITH_MAP_REVISION"
      }
    }
  }
}
```

Replace every placeholder, coordinate and timestamp with actual client values. Metadata keys above are our suggested names, not claims about the Niantic SDK's output schema. Position is metres, +Y up; heading 0=+Z, 90=+X, 180=-Z, 270=-X, not automatically magnetic/geographic north. Timestamp is UTC Unix seconds. Optional pitch/roll are unused by current routing; clients must agree on their convention before relying on them.

For the controlled demo, begin with approximately 2–5 pose messages/second (a project recommendation, not a Niantic sampling requirement), and send localization transitions immediately. Continue updates while the assistant thinks. Backend rejects out-of-order/stale poses, suspends instructions on localization loss, and requires a fresh pose within 3m of a waypoint before routing. Client must also expire instructions on disconnect/staleness; no proactive server expiry notification exists.

Map IDs and revision metadata are carried but not checked against an allowlist today; the client must use the agreed mapping. A map switch, AR reset or realignment invalidates the previous alignment: mark unlocalized and establish the correct graph/session before resuming. Per-frame raw segmentation buffers, camera frames and SDK secrets are not pose metadata.

## What Niantic semantics can and cannot establish

Official NSDK documentation describes pixel-level scene segmentation and semantic channels; the Swift API reference also lists scene-segmentation types. Actual supported channel names and capabilities must be confirmed on the installed SDK/platform at runtime. These are model observations, not guaranteed object identities or building facts.

Do not equate a semantic surface class with a named room, a working elevator, a wheelchair-accessible route, a verified obstacle distance or a clear path. Named places and accessibility facts come from validated map annotations and building documents. Distances need an actual supported depth/geometry source with known units and alignment. Localization and segmentation are separate inputs.

### Sensor owner: supported obstacle transport now

Send `obstacle` on the navigation WebSocket using the existing contract:

```json
{"type":"obstacle","direction":"front","distance_m":1.2,"description":"Observed obstruction","timestamp":1789819200}
```

Use a real current timestamp and measured distance, or `distance_m:null` if unknown. Direction must be relative to the user's facing direction; a side/rear-mounted camera must be transformed by the sensor owner before labeling front/left/right/back. Backend accepts the label without a geometric transformation. Agree on device mounting/calibration with the localization owner. Backend has one most-recent observation per direction and a 5-second expiry; it does not fuse multiple devices or infer clearance when an observation disappears.

The client handles immediate obstacle cues locally, before network or LLM round trips. Backend distributes observations, includes fresh obstacle state in agent context, and indexes historical obstacle events. An obstacle report does not automatically alter graph edges or trigger rerouting.

### Proposed scene-observation handoff — NOT accepted by current endpoints

For richer environmental explanations, the perception owner should provide sample observations with:

| Field | Required meaning |
| --- | --- |
| `observation_id`, `session_id`, `site_id` | Stable deduplication ID and session/site binding |
| `captured_at`, `expires_at` | UTC time of measurement and a source-appropriate freshness limit |
| `provider`, `sdk_version`, `device_id`, `sensor_id` | Source and device provenance |
| `observation_type` | Separate `segmentation`, `object_detection`, `ocr`, `depth` etc.; do not label one as another |
| `label`, `confidence` | Runtime label plus source score/null; segmentation coverage is not confidence |
| `coordinate_frame`, `map_id`, `map_revision`, `pose_timestamp` | Alignment and synchronization, or explicit unlocalized status |
| `direction`, `distance_m`, `distance_source` | Calibrated user-relative direction and measured range/null; never infer range from a label |
| `position` | Optional measured map-space position; null when alignment/depth is unavailable |
| `source_reference` | Optional retained frame/event reference under an agreed access and retention policy |

This proposal needs backend models, validation, ingestion transport, bounded live-state storage, deduplication and event indexing before clients send it. Do not send `scene_observation` to current WebSockets; it will be rejected. Do not stuff rich observations into `provider_metadata` or static building documents to simulate live perception. Once implemented, fresh observations belong in application context; useful historical summaries belong in Elasticsearch with timestamps and source IDs. Historical search must never be treated as current collision evidence.

## Building-data / mapping owner

Provide real directory text, room labels/aliases, accessibility guides, signage transcriptions and source documents, plus human-validated destination IDs tied to graph waypoint IDs. Include provenance, revision/date and permission to use the data. Flag uncertain or outdated claims (for example, operating status of an elevator).

Existing upload interfaces:

- `POST /knowledge/documents`: `{site_id,id,title,text}`. Use stable IDs for revisions. Current schema has no arbitrary metadata field; preserve date/source details in the supplied title/text until structured metadata is added.
- `POST /knowledge/upload`: multipart `site_id`, `document_id`, `file`; UTF-8 text/Markdown or text PDF, maximum 5 MiB. No OCR.
- Graph/entity changes: coordinate through backend-owned graph data and seeding; there is no runtime map-upload or entity-mutation HTTP API.

The conversational agent retrieves relevant document chunks and map entities on demand. It does not receive the entire index with each request. Site filtering and backend source IDs preserve the connection to evidence. Existing mock building documents must not be presented as real-site knowledge.

## Voice owner: usable interface now, audio work still pending

For an initial voice UX, the native client can transcribe user speech and send its final transcript to either `POST /assistant/query` (`session_id,text`) or `WS /ws/sessions/{session_id}/assistant` (`type:assistant_message,text`). Speak the returned `text` using the chosen speech layer. Neither transcription nor speech synthesis is implemented by this backend. The assistant WebSocket currently returns one complete text response; it is not an audio or token-streaming connection.

The backend automatically supplies fresh session context to OpenAI on each tool-loop iteration and retrieves indexed information when tools request it. Keep the navigation WebSocket active independently of speech. A successful `actions` entry and route update, not model wording alone, confirm a destination change. Null location means unavailable; clients should not speak invented camera or movement instructions.

For a future OpenAI Realtime voice integration, agree on microphone format, transport, turn detection, interruption/cancellation, utterance IDs, session binding and duplicate-action prevention. It will require a separate backend voice adapter and authentication/session setup; there is no `/realtime` or ephemeral-token endpoint today. Reuse the existing context builder and validated tool dispatcher; do not create a second independent routing authority. Do not assume the configured GPT text model is also the chosen audio model.

Immediate obstacle/navigation warnings interrupt conversational playback. Re-evaluate freshness before speaking delayed physical guidance. Current text requests have no cancellation protocol or durable idempotency key, so the client must not blindly retry an action-bearing utterance on timeout. Inspect session navigation state and ask/clarify before resubmission. Realtime audio must not put long-lived OpenAI or Elastic service keys on the phone.

## Deployment / operations owner

For a real-device demo, provide reachable backend HTTPS/WSS URLs (Modal or an agreed local-network server), a shared session identifier, and service credentials through backend environment/Modal secrets. `127.0.0.1` on the phone means the phone itself, not the development PC. Deploy the current FastAPI app using `services/backend/deployment/modal_app.py`; configure the `htn-backend` secret. Current endpoints are not authenticated; add client/session authorization before a public deployment handling real users.

The backend needs OpenAI and Elasticsearch credentials and the configured embedding endpoint ID. It does not currently need a Niantic API key: the localization owner configures client SDK access according to that SDK's requirements. A future server-to-server Niantic map-fetch integration would require a separate documented credential/permission contract; none exists today.

## Integration acceptance checklist

- Client and backend agree on the same real map revision and destination IDs.
- Known physical positions/headings match graph coordinates; coarse/untracked input cannot masquerade as mapped localization.
- Walk a known test route under supervision; verify waypoint progression, arrival, localization loss and recovery.
- Disconnect the network and confirm local obstacle cues remain available and remote instructions expire.
- Ask a building question and inspect actual source IDs; select a destination and verify the route action.
- Verify obstacle history is timestamped/session-scoped and never described as proof of a presently clear path.
- Confirm unsupported semantic/audio messages are not being treated as implemented interfaces.

## Official capability references

- [Niantic VPS2 and separate anchor/device tracking](https://nianticspatial.com/docs/nsdk/features/vps2/)
- [Niantic scene segmentation](https://nianticspatial.com/docs/nsdk/features/semantics/)
- [Niantic Swift API reference](https://www.nianticspatial.com/docs/api/swift/NSDK/)
- [OpenAI Realtime API](https://developers.openai.com/api/docs/guides/realtime)
