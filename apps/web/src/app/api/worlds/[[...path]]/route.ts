import { parseGraph, parseMeasurements } from "@/lib/world-manifest";
import {
  getMeasurements,
  getWorld,
  isSafeSegment,
  listWorlds,
  openAsset,
  saveGraph,
  saveMeasurements,
} from "@/lib/worlds-api.server";

/**
 * Same-origin proxy for the worlds stored on the Modal Volume.
 *
 *   GET /api/worlds                         → { worlds: WorldManifest[] }
 *   GET /api/worlds/:id                     → WorldManifest
 *   GET /api/worlds/:id/measurements        → MeasurementsFile
 *   PUT /api/worlds/:id/graph               → WorldManifest (body: NavigationGraph)
 *   PUT /api/worlds/:id/measurements        → MeasurementsFile (body: { measurements })
 *   GET /api/worlds/:id/:version/:file      → streamed asset bytes (e.g. scene.spz)
 *
 * The browser only ever talks to this route; `WANDER_API_URL` and the API key
 * stay on the server. Without an API URL the files live in maps/assets.
 */
export const dynamic = "force-dynamic";

const NO_STORE = { "cache-control": "no-store" };

export async function GET(_req: Request, ctx: RouteContext<"/api/worlds/[[...path]]">) {
  const { path = [] } = await ctx.params;
  if (path.some((s) => !isSafeSegment(s))) return Response.json({ error: "Invalid path" }, { status: 400 });

  try {
    if (path.length === 0) return Response.json({ worlds: await listWorlds() }, { headers: NO_STORE });
    if (path.length === 1) {
      const world = await getWorld(path[0]);
      return world
        ? Response.json(world, { headers: NO_STORE })
        : Response.json({ error: "World not found" }, { status: 404 });
    }
    if (path.length === 2 && path[1] === "measurements") {
      return Response.json({ measurements: await getMeasurements(path[0]) }, { headers: NO_STORE });
    }
    const asset = await openAsset(path);
    return asset ?? Response.json({ error: "Asset not found" }, { status: 404 });
  } catch (err) {
    console.error("[api/worlds]", err);
    return Response.json({ error: "Worlds backend unavailable" }, { status: 502 });
  }
}

export async function PUT(req: Request, ctx: RouteContext<"/api/worlds/[[...path]]">) {
  const { path = [] } = await ctx.params;
  if (path.length !== 2 || path.some((s) => !isSafeSegment(s)))
    return Response.json({ error: "Not found" }, { status: 404 });
  const [id, resource] = path;

  let body: unknown;
  try {
    body = await req.json();
  } catch {
    return Response.json({ error: "Body must be JSON" }, { status: 400 });
  }

  try {
    if (resource === "graph") {
      const graph = parseGraph(body);
      const manifest = await saveGraph(id, graph);
      return manifest
        ? Response.json(manifest, { headers: NO_STORE })
        : Response.json({ error: "World not found" }, { status: 404 });
    }
    if (resource === "measurements") {
      const list = parseMeasurements((body as { measurements?: unknown })?.measurements ?? body);
      const saved = await saveMeasurements(id, list);
      return saved
        ? Response.json(saved, { headers: NO_STORE })
        : Response.json({ error: "World not found" }, { status: 404 });
    }
    return Response.json({ error: "Not found" }, { status: 404 });
  } catch (err) {
    if (err instanceof Error && /^Invalid /.test(err.message))
      return Response.json({ error: err.message }, { status: 400 });
    console.error("[api/worlds]", err);
    return Response.json({ error: "Worlds backend unavailable" }, { status: 502 });
  }
}
