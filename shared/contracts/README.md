# Shared contracts

Schemas shared by the Next.js web app, the iOS app (Niantic Lightship SDK + ARKit), and the FastAPI backend on Modal.

| File | What it defines |
| --- | --- |
| [`worlds-api.openapi.yaml`](worlds-api.openapi.yaml) | The Modal FastAPI service: worlds + assets on the Volume, graph/measurement persistence, Niantic localization, routing, live sessions (REST + WebSocket). Start here if you are building the backend. |
| [`world.schema.json`](world.schema.json) | `worlds/<id>/world.json` — a world's manifest: Niantic site id, asset version, splat path, navigation graph, alignment. |
| [`notes.schema.json`](notes.schema.json) | `worlds/<id>/notes.json` — notes pinned to the scan (title, location, description, position). |
| [`measurements.schema.json`](measurements.schema.json) | `worlds/<id>/measurements.json` — distances measured in the web viewer. |
| [`navigation.schema.json`](navigation.schema.json) | Messages between phone ⇄ backend ⇄ dashboard: `LocalizationUpdate`, `RouteRequest/Response`, `PoseUpdate`, `ProgressUpdate`, `SessionEvent`, `VpsSiteStatus`. |
| [`examples/`](examples/) | Sample documents. |

TypeScript mirrors live in `apps/web/src/lib/world-manifest.ts`. Generate Swift models for the iOS app from the JSON schemas (e.g. quicktype) rather than hand-writing them.

## Storage layout on the Modal Volume

Assets are organised by world and version. Versions are immutable: re-exporting a scan creates `v2`, it never overwrites `v1`.

```text
worlds/
└── demo-building/
    ├── world.json           # manifest (schema above) — source of truth for the navigation graph
    ├── notes.json           # notes pinned in the web viewer (optional)
    ├── measurements.json    # web-viewer measurements (optional)
    └── v1/
        ├── scene.spz        # Gaussian splat exported from Scaniverse
        ├── thumbnail.png    # optional 16:10 preview
        ├── mesh.glb         # optional collision / occlusion mesh
        └── vps-map.bin      # optional VPS map export for the phone
sessions/
└── <sessionId>.json         # navigation session state (a Modal Dict works too)
```

`world.json` records the Niantic VPS site id, the active asset `version`, the splat path, the `navigationGraph` used for routing, and the `alignment` that maps splat coordinates into the shared world frame. The web viewer applies `alignment` to the splat and draws the graph on top, so the displayed world is the one the phone localises against. Notes and measurements made in the viewer autosave with `PUT /worlds/{id}/notes` and `PUT /worlds/{id}/measurements`; the graph itself is edited through `PUT /worlds/{id}/graph`.

## Upload flow (web → backend)

The dashboard's **New world / Import splat** dialog and the viewer's **Upload splat** button run:

1. `POST /worlds` `{ id, name, space?, nianticSiteId?, splatFilename }` → draft manifest (skipped for existing worlds).
2. `PUT /worlds/{id}/{version}/scene.spz` with the raw bytes, streamed through the Next.js proxy (`PUT /api/worlds/...`) so the browser never sees the API key. A `409` (file already at that version) makes the web app retry at the next version.
3. `PATCH /worlds/{id}` `{ version?, assets?, status }` to point the manifest at the new file and flip `draft → processing` (or `aligned` when a Niantic site id is set).

Files stream end-to-end; nothing is held in memory. Note the Next.js proxy must run somewhere without a small request-body cap (Node host, container, `next start`) — Vercel serverless functions cap bodies at ~4.5 MB, which is far below a splat. If that becomes the deployment target, add a signed-URL upload endpoint to this contract and have the browser PUT to the backend directly.

## Frames

- **Splat frame** — raw coordinates in `scene.spz`, as exported.
- **World frame** — where routing happens. `alignment` maps splat → world: `p_world = rotation · (scale · p_splat) + position`. When a world is published to Niantic, the world frame *is* the VPS site frame (`alignment.frame: "niantic-vps"`), so poses coming from the Lightship SDK need no further transform.
- `navigationGraph.frame` says which of the two the node positions use (`world` by default). Measurements are always in the world frame.

## Backend responsibilities (Modal)

1. **Volume as the DB.** All reads/writes go through the API; nothing else mounts the volume. Writes to `world.json` are read-modify-write with a per-world lock; assets are write-once per version.
2. **Auth.** Every request carries `X-API-Key` (below).
3. **Niantic SDK bridge.** The SDK runs on the phone. The backend receives its localization results (`POST /worlds/{id}/localize`), checks the `nianticSiteId` matches the world, re-expresses poses in the world frame, and exposes site status (`GET /worlds/{id}/vps`). If a Lightship API key is configured, it also asks Niantic whether the location is activated.
4. **Routing.** Dijkstra over the graph; turn instructions from leg headings; off-route / arrival detection on every `POST /sessions/{id}/pose`; live `SessionEvent`s over `/ws/sessions/{id}` for the dashboard.
5. **CPU only.** Rendering happens in the browser.

## Authentication — API key

Every request carries a shared secret in the `X-API-Key` header:

```http
GET /worlds/demo-building HTTP/1.1
X-API-Key: <WANDER_API_KEY>
```

- The backend reads the expected value from the `WANDER_API_KEY` environment variable (a Modal Secret) and compares with a constant-time check (`secrets.compare_digest`). Missing or wrong key → `401 {"detail": "invalid api key"}`.
- The Next.js proxy sends the header from its own `WANDER_API_KEY` env var; the key never reaches the browser. The phone sends it directly.
- One key for the whole team is fine for the hackathon. Rotate by changing the secret on both sides.

## Rules

- `id`, `version`, and `filename` match `^[A-Za-z0-9][A-Za-z0-9._-]*$` (no dotfiles, no `..`); reject anything else with `400` so nothing can escape `worlds/`.
- Asset downloads set `Content-Length` and `Cache-Control: public, max-age=31536000, immutable`.
- `PUT /worlds/{id}/graph` must validate: unique node ids, every edge references a node, `kind` ∈ {waypoint, entrance, destination}.

## Local development without the backend

Leave `WANDER_API_URL` unset and the web app reads and writes the same `worlds/…` layout under `maps/assets/` (git-ignored). Use `npm run world:add` in `apps/web` to register a Scaniverse export; notes and measurements saved in the viewer land in `maps/assets/worlds/<id>/notes.json` and `measurements.json`, ready to upload with `modal volume put`.
