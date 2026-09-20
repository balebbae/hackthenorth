# hackthenorth

HTN Navigation Assistant — **Wander**, a wearable indoor navigation assistant for blind and low-vision users. Four LiDAR iPhones (chest, back, left, right) sense the surroundings; a FastAPI backend on Modal owns routing, sessions and the OpenAI agent; a Next.js companion app lets a helper pick destinations on a Gaussian-splat view of the building.

## Architecture

![Wander system architecture: front iPhone coordinates obstacle cues, Niantic localization, speech and peer haptics; FastAPI worlds API on Modal owns routing, sessions, agent tools and the voice bridge; Next.js companion app reaches the backend through a server-side proxy.](docs/architecture/wander-architecture.png)

Three cooperating layers, each with a single owner:

| Layer | Runs on | Owns |
| --- | --- | --- |
| Local obstacle guidance | Front phone (`apps/ios`) | ARKit LiDAR depth → `ObstacleDetector` → speech/haptic cues. Never waits on the network; urgent stop cues interrupt route narration. Fans haptic pulses to the side/back phones over MultipeerConnectivity. |
| Localization + routing | Niantic VPS on the phone, `services/backend` on Modal | Phone posts poses/fixes to `/worlds/{id}/localize`; backend routes over the `world.json` navigation graph (Dijkstra), tracks session progress, off-route and arrival, and serves progress cues back. Geometry, not the LLM, is authoritative for movement commands. |
| AI interaction | `services/backend` → OpenAI | Responses-API agent answers grounded questions and acts only through validated tools (`resolve_destination`, `set_destination`, `get_navigation_state`, …). GPT Live voice is bridged server-side so API keys never reach the phone. |

Cross-cutting: `shared/contracts/` defines the world manifest, navigation graph and API schemas; worlds (`world.json`, `scene.spz`, notes, sessions) live on the `wander-worlds` Modal Volume; the browser only talks to FastAPI through the Next.js `/api/*` proxy. The backend intentionally runs as one container because session state and WebSocket subscribers are process-local. Optional Modal GPU workers provide self-hosted hloc/COLMAP localization and scene annotation.

Diagram source: [`docs/architecture/wander-architecture.html`](docs/architecture/wander-architecture.html) (also exported as [SVG](docs/architecture/wander-architecture.svg)).

## Layout

```text
htn/
├── apps/
│   ├── web/                     # Next.js companion web app
│   │   ├── src/
│   │   │   └── app/             # App Router pages, layouts, and global styles
│   │   └── public/              # Static web assets
│   └── ios/                     # Swift iPhone app, shared across device roles
│       ├── App/                # App entry point and composition
│       ├── Features/           # Navigation, obstacle cues, voice interaction
│       ├── Services/           # ARKit, Shepherd, Niantic SDK, networking, speech
│       └── Resources/          # Native app assets
├── services/
│   └── backend/                # Python / FastAPI backend
│       ├── app/
│       │   ├── api/            # HTTP endpoints and WebSocket connections
│       │   ├── routing/        # Waypoint routing and navigation progress
│       │   └── integrations/   # OpenAI and other external service clients
│       └── deployment/         # Modal deployment configuration
├── shared/
│   └── contracts/              # Message schemas shared by the apps and backend
├── maps/
│   ├── navigation/             # Waypoints, destinations, graph and alignment data
│   └── assets/                 # Local exported splats and meshes (ignored by Git)
└── docs/                       # Architecture, setup notes, and demo plan
```

## Team ownership

| Area | Owner |
| --- | --- |
| iPhone app, obstacle sensing, and speech | iOS developer |
| Mapping, Niantic localization, and map alignment | Localization developer |
| FastAPI, routing, and Modal deployment | Backend developer |
| Next.js companion app and splat viewer | Web developer |

The iOS and localization developers share one native app. Agree on the camera/AR session boundary before implementation. Message contracts and map coordinates are shared team responsibilities.

## Notes

- The web app uses Next.js with the App Router, TypeScript, Tailwind CSS, and ESLint. Run npm run dev from apps/web to start it.
- The first MVP uses the chest phone; the same iOS app can later support left, right, and back device roles.
- Niantic localization runs through the phone SDK. Modal hosts the custom backend.
- Exported map assets belong in `maps/assets/`; navigation metadata belongs in `maps/navigation/`.
- Worlds are stored on a Modal Volume as `worlds/<id>/world.json` + `worlds/<id>/<version>/scene.spz` (contract in `shared/contracts/`). The web app renders them with Spark/Three.js at `/worlds/<id>` (measure distances, tag stops, save the graph back), reading through FastAPI when `WANDER_API_URL` is set or from `maps/assets/worlds/` locally (`npm run world:add` in `apps/web` registers an export).
- Per-area docs: `apps/ios/README.md`, `apps/web/README.md`, `services/backend/WORLDS_MIGRATION.md`, `shared/contracts/README.md`, `shared/contracts/service-handoffs.md`.
