<!-- BEGIN:nextjs-agent-rules -->

# This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` (resolved from this file's directory; in monorepos the `next` package may not be visible from the repo root) before writing any code. Heed deprecation notices.

This block is written and re-added by `next dev` — verify at `node_modules/next/dist/server/lib/generate-agent-files.js`. Removing it from a diff only re-creates the uncommitted change; committing it with your work keeps the tree clean.

<!-- END:nextjs-agent-rules -->

## Project frontend design — required

Before creating or changing frontend designs, read the repository [AGENTS.md](../../AGENTS.md) and the full [FRONTEND_STYLE.md](../../FRONTEND_STYLE.md). Follow that shared design reference for this Next.js application. These project rules supplement the generated Next.js guidance above.

## Conventions in this app

- Design tokens live in `src/app/globals.css` as a Tailwind v4 `@theme` block; shared component classes (`btn-primary`, `card`, `pill`, `input`, `container-page`, …) are `@utility` definitions there. Tailwind v4 cannot `@apply` classes declared in `@layer components`, so add new shared classes as `@utility`.
- Fonts: Inter (`--font-inter`) and Source Serif 4 (`--font-source-serif`) via `next/font/google` in `src/app/layout.tsx`; use `font-sans` / `font-serif`.
- Product name ("Wander") and copy come from `src/lib/brand.ts`. The logo orb lives at `public/brand/wander-mark.png` (rendered by `<LogoMark>`; a copy at `src/app/icon.png` is the favicon/app icon).
- Palette tokens: `wander-blue` (primary), `wander-pink` / `wander-sky` / `wander-navy` (accent cast), `stellar-white` (canvas), `void-black` (text), `sky-tint` / `pink-tint`, `hairline`. The brand gradient is `bg-wander` / `card-brand` and is only for the CTA band and login panel.
- Images: every visual asset is registered in `src/lib/images.ts` with a `src`, size, alt, and a generation prompt. `<ImageSlot>` (server) checks `public/<src>` and renders `next/image` if the file exists, otherwise `<ImagePlaceholder>`. To ship an image, drop the file at the registered path — no code change needed. Client components receive a pre-resolved `imageReady` flag instead of importing `images.server.ts`.
- Routes: `/` landing, `/login` (UI only, submit routes to `/dashboard`), `/dashboard` (worlds browser; live worlds from the volume merged ahead of the samples in `src/lib/worlds.ts`), `/worlds/[id]` (full-viewport Spark splat editor — deliberately outside the dashboard shell), `/api/worlds/[[...path]]` (same-origin proxy to the worlds backend: GET list/manifest/measurements/assets, PUT graph/measurements).

## Worlds, splats and the viewer

- Splats, VPS maps and meshes live on a Modal Volume as `worlds/<id>/world.json` + `worlds/<id>/<version>/scene.spz`. The manifest contract is `shared/contracts/world.schema.json`; its TypeScript mirror is `src/lib/world-manifest.ts` (`WorldManifest`, `validateManifest`, `assetUrl`). Change both together.
- The browser never talks to FastAPI directly. `src/lib/worlds-api.server.ts` (server-only) reads from `WANDER_API_URL` (sending `X-API-Key: $WANDER_API_KEY`) when set, otherwise from `maps/assets/worlds/` at the repo root (`WANDER_ASSETS_DIR` overrides). The route handler `src/app/api/worlds/[[...path]]/route.ts` exposes list / manifest / streamed asset on the Next.js origin; assets are versioned so they are served `immutable`.
- Rendering: `src/components/viewer/SplatViewerEngine.ts` owns Three.js + `@sparkjsdev/spark` (`SparkRenderer`, `SplatMesh`), orbit (`three/addons` OrbitControls) and first-person `WalkControls.ts`, click picking (raycast against the SplatMesh), the stop/edge and measurement overlays, HTML labels, robust camera framing and disposal. React owns the data: `WorldViewer.tsx` holds graph / measurements / selection and pushes them through `useSplatViewer.ts` setters; the engine reports `pick` events back. The engine module is only imported dynamically so nothing WebGL-related runs on the server. UI pieces: `InspectorPanel.tsx` (Stops / Measure / Details tabs), `ViewerOverlays.tsx` (loading / empty / error cards). Tools: Navigate (1), Measure (2), Add stop (3); Esc cancels, Delete removes the selected stop; Save PUTs to `/api/worlds/:id/graph` and `/measurements`. Spark needs Turbopack (the default here); do not switch the build to webpack without the `new URL()` workaround from sparkjsdev/spark-react-nextjs.
- The viewer canvas is the one Wander Navy "dark island" on the page; everything around it stays on the light canvas per FRONTEND_STYLE.md. Graph colours: waypoint = Wander Blue, entrance = Wander Sky, destination = Wander Pink.
- Local dev without the backend: `npm run world:add -- <id> path/to/scene.spz --name "…" --site <nianticSiteId>` copies the export into `maps/assets/worlds/<id>/v1/` and writes `world.json`; the same folder uploads to the volume unchanged. `alignment` in the manifest maps splat coordinates into the VPS frame (the "Flip up axis" toolbar button is a quick visual check for upside-down exports).

## Verification

```bash
npm run lint        # eslint (flat config)
npx tsc --noEmit    # typecheck (run `npx next typegen` first if PageProps/RouteContext types look stale)
npm run build       # next build (Turbopack); marketing/login prerender static, /dashboard* and /api/worlds are dynamic (force-dynamic) by design
npm run image-prompts  # regenerate IMAGE_PROMPTS.md from src/lib/images.ts after editing prompts
```

Env vars are documented in `.env.example`.
