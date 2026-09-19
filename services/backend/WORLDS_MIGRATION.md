# Main-branch world contract migration

Contract source: origin/main at 881e103b59d69f7f2aa449d39dbc30d32b0a842d.
The six contract files from that revision are copied unchanged into shared/contracts.

## Deployment changes

GitHub Actions: `.github/workflows/deploy-modal.yml` tests every push to main and
then deploys both Modal apps to the `main` Modal environment. It also supports
manual runs from GitHub Actions on main. Configure repository Actions secrets
`MODAL_TOKEN_ID` and `MODAL_TOKEN_SECRET` for the workspace containing htn-backend.
Application credentials remain in that existing Modal secret; CI does not replace
it or require a checked-in .env. Deployments are serialized and require passing
backend tests. The two app deployments are sequential, not an atomic rollout.

Shortcut from the activated virtual environment at the repository root:
`python -m services.backend.scripts.deploy`. This replaces the htn-backend secret
from the local .env (excluding local path overrides), deploys both apps, and saves
the detected web endpoint as WANDER_BACKEND_URL. It generates WANDER_API_KEY only
when missing. Existing Modal authentication and installed dependencies are required.

Import a scan with `python -m services.backend.scripts.scan_pipeline`.
Default inputs are artifacts/test-building/v1/scene.spz and walkthrough.mp4
in the same folder. Optional --world, --version, --splat and --video override these.
This reads the URL/key from .env, uploads assets, runs annotation, downloads frames,
and prepares review.json under artifacts/test-building/v1. After verified waypoint
placement/review, rerun with `--world test-building --publish` to publish, index,
and issue a sample agent query. A measured navigation graph remains required for
publication; the video is not automatically registered to the splat.

1. Set a team secret `WANDER_API_KEY` in services/backend/.env and in the existing
   Modal `htn-backend` secret. Use the same value in the web proxy and phone.
2. Install updated dependencies: `python -m pip install -r services/backend/requirements.txt`.
3. Deploy: `python -m modal deploy -m services.backend.deployment.modal_app`.
4. The app mounts the `wander-worlds` Volume at `/data` and reads
   `worlds/<id>/world.json` there. Local development defaults to maps/assets.
   Do not put a Windows WANDER_DATA_ROOT into the Modal secret; use `/data` remotely.
5. Import/create worlds through the API. Existing legacy demo graph settings do
   not automatically populate the Volume. No real assets are bundled.

All HTTP requests, including /health, now require `X-API-Key`. Authentication fails
closed if WANDER_API_KEY is empty. WebSockets use the same header; the dashboard
socket also accepts the contract's `?key=` fallback. Prefer a server-side proxy
to avoid exposing the key in browser URLs. The Live voice endpoint additionally
retains its first-message VOICE_ACCESS_TOKEN check.

```powershell
# In the current shell, set the same team key that you configured in Modal:
$headers = @{ 'X-API-Key' = $env:WANDER_API_KEY }
Invoke-RestMethod "$baseUrl/health" -Headers $headers
Invoke-RestMethod "$baseUrl/worlds" -Headers $headers
```

## Implemented canonical API

- World create/list/get/patch/delete, with schema validation and per-world locks.
- Navigation graph and measurement persistence; graph reads never use a stale cache.
- Raw streamed immutable asset uploads, 2 GiB default cap; downloads include length,
  ETag and immutable cache headers. PATCH version discovers the version's splat
  and optional mesh.glb/thumbnail.png/vps-map.bin; ambiguous splats are rejected.
- Persistent navigation sessions, destination updates, pose updates and ending.
- Weighted Dijkstra routing, directed edges, avoidance, edge snapping, turns.
- Localization site/device checks, timestamp ordering, quaternion validation.
- Off-route detection above 3 m and rerouting after 5 seconds; arrival below 1.5 m;
  tracking loss pauses cues. Session events on the dashboard WebSocket.
- OpenAI assistant/Live requests can use these session IDs. The agent reads the
  current world and routes through the canonical service.

The single-container deployment is intentional: per-world/session locks and
WebSocket subscribers are process-local. Session JSON survives redeploy, whereas
assistant conversation history does not. Do not increase max_containers or run
multiple Uvicorn workers until distributed locking/broadcasts are added. The
annotation worker uses its own separate htn-annotations Volume.

## Contract ambiguities and explicit limitations

- `alignment` is splat-to-world. When alignment.frame is niantic-vps, SDK VPS poses
  already occupy the world frame and are NOT transformed again. Splat graph nodes
  are transformed. Other target frames are rejected for /localize because no
  VPS-to-world transform is defined by the contract.
- A /worlds/{id}/route request has no session ID in the contract, so omitting
  `from` cannot identify a user's position. It returns 400; use the session
  destination endpoint to route from that session's pose.
- The world schema has no edge accessibility fields. Canonical REST routing is
  ordinary connectivity routing, not certified step-free routing. The assistant
  refuses accessible_only=true rather than label an unverified route accessible.
- GET /vps exposes map availability and the latest successful phone fix. It
  currently reports localizable=false (activation unverified); no Niantic server
  activation lookup is implemented, and there is no 60-second activation cache.
  A server activation endpoint/auth/response contract must be confirmed with the
  Niantic owner. Neither a VPS export nor a past fix proves current activation.
- Canonical session routes persist across graph edits; the next pose detects the
  changed graph and recomputes the route. New route requests see edits immediately.
- Asset uploads do not trigger semantic annotation. The existing batch workflow
  remains explicit. Manifest writes are atomic; multi-file annotation evidence
  plus manifest publication is serialized but is not a transactional database.

## Annotation integration

Use the world ID (for example demo-building) as `--site`, and its active asset
version (for example v1) as `--revision`. Supply the downloaded world.json as
`--graph` to prepare-review and publish. The review hash binds the full manifest.

```powershell
python -m services.backend.scripts.annotate_scan prepare-review --batch artifacts/candidates.json --graph artifacts/world.json --output artifacts/review.json
# Edit review.json, then:
python -m services.backend.scripts.annotate_scan publish --batch artifacts/candidates.json --reviews artifacts/review.json --graph artifacts/world.json --revision v1 --output artifacts/published.world.json --api-url https://YOUR-BACKEND.modal.run --index
```

Two backend extensions support this flow:

- PUT /worlds/{id}/annotations accepts `{batch, review}` and checks the current
  manifest hash under the world lock. It stores detailed evidence separately in
  annotations.json and adds schema-compliant destination nodes at reviewed
  approach waypoints. It converts splat-frame graphs into world coordinates.
- POST /worlds/{id}/index indexes current nodes plus annotation descriptions in
  Elasticsearch. This calls OpenAI embeddings and incurs API usage. Re-index
  after viewer edits to refresh semantic search. Removed IDs are filtered against
  the current graph, even if old Elastic documents remain.

Download a fresh world.json before reviewing again after any world edit. Existing
legacy Graph JSON publication still works, but is only for /legacy navigation.

## Legacy compatibility

Old snake_case demo session REST routes moved to `/legacy/sessions/...`.
Old writable navigation WS moved to `/ws/legacy/sessions/{id}`. The canonical
`/ws/sessions/{id}` is push-only except `{type: ping}` and emits SessionEvent.
Assistant text/voice WS and /assistant/query remain at their existing paths and
accept either session family. Legacy /destinations still lists the old demo graph;
canonical clients obtain destinations from world.navigationGraph.nodes.

Canonical headings are 0=-Z clockwise; legacy poses retain 0=+Z. The assistant
adapter marks its internal legacy heading convention explicitly. Do not mix the
wire formats. The new shared main contracts take precedence over older handoff
documents and demo instructions elsewhere in this branch.
