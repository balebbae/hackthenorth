# HTN Navigation Assistant

The web app is scaffolded with Next.js, TypeScript, Tailwind CSS, and ESLint. The remaining directories are placeholders; application features have not been implemented.

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
- Empty folders contain `.gitkeep` placeholders so they can be tracked by Git.
- The web app contains the create-next-app starter and npm dependencies. No Xcode project, backend implementation, or deployment code has been added.
