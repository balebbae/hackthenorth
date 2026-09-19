import "server-only";
import { createReadStream } from "node:fs";
import { mkdir, readdir, readFile, stat, writeFile } from "node:fs/promises";
import { extname, join, resolve } from "node:path";
import { Readable } from "node:stream";
import {
  MEASUREMENTS_SCHEMA,
  parseManifest,
  parseMeasurements,
  type Measurement,
  type MeasurementsFile,
  type NavigationGraph,
  type WorldManifest,
} from "./world-manifest";

/**
 * Data access for worlds stored on the Modal Volume.
 *
 * - With `WANDER_API_URL` set, every call goes to the FastAPI service that
 *   fronts the volume (see shared/contracts/README.md for the endpoints).
 * - Without it, the same `worlds/<id>/...` layout is read from a local
 *   directory (default `maps/assets` at the repo root, git-ignored) so the
 *   viewer works offline with Scaniverse exports copied by hand.
 */

const API_URL = process.env.WANDER_API_URL?.replace(/\/+$/, "");
const API_KEY = process.env.WANDER_API_KEY;
// Dev-only fallback outside the app dir; tell Turbopack not to trace it into the server bundle.
const ASSETS_DIR = resolve(
  /*turbopackIgnore: true*/ process.env.WANDER_ASSETS_DIR ?? join(process.cwd(), "../../maps/assets"),
);

const SEGMENT_RE = /^[A-Za-z0-9][A-Za-z0-9._-]*$/;

export const worldsSource = API_URL ? ("api" as const) : ("local" as const);

/** Reject anything that could escape `worlds/` (dotfiles, `..`, separators). */
export function isSafeSegment(s: string): boolean {
  return SEGMENT_RE.test(s);
}

const MIME: Record<string, string> = {
  ".spz": "application/octet-stream",
  ".ply": "application/octet-stream",
  ".splat": "application/octet-stream",
  ".ksplat": "application/octet-stream",
  ".sog": "application/octet-stream",
  ".rad": "application/octet-stream",
  ".glb": "model/gltf-binary",
  ".gltf": "model/gltf+json",
  ".obj": "text/plain",
  ".json": "application/json",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".webp": "image/webp",
  ".bin": "application/octet-stream",
};

/** Shared-secret auth per shared/contracts/README.md; the key never leaves the server. */
function apiHeaders(): HeadersInit {
  return API_KEY ? { "X-API-Key": API_KEY } : {};
}

export async function listWorlds(): Promise<WorldManifest[]> {
  if (API_URL) {
    const res = await fetch(`${API_URL}/worlds`, { headers: apiHeaders(), cache: "no-store" });
    if (!res.ok) throw apiError(res.status);
    const body: unknown = await res.json();
    const list = Array.isArray(body)
      ? body
      : ((body as { worlds?: unknown[] })?.worlds ?? []);
    return list.flatMap((m) => safeParse(m));
  }

  const root = join(ASSETS_DIR, "worlds");
  let dirs: string[];
  try {
    dirs = (await readdir(root, { withFileTypes: true }))
      .filter((d) => d.isDirectory() && isSafeSegment(d.name))
      .map((d) => d.name);
  } catch {
    return [];
  }
  const manifests = await Promise.all(dirs.map((id) => readLocalManifest(id)));
  return manifests
    .filter((m): m is WorldManifest => m !== null)
    .sort((a, b) => (b.updatedAt ?? "").localeCompare(a.updatedAt ?? "") || a.name.localeCompare(b.name));
}

export async function getWorld(id: string): Promise<WorldManifest | null> {
  if (!isSafeSegment(id)) return null;
  if (API_URL) {
    const res = await fetch(`${API_URL}/worlds/${encodeURIComponent(id)}`, {
      headers: apiHeaders(),
      cache: "no-store",
    });
    if (res.status === 404) return null;
    if (!res.ok) throw apiError(res.status);
    return parseManifest(await res.json());
  }
  return readLocalManifest(id);
}

/**
 * Open a versioned asset (`worlds/<id>/<version>/<file>`) as a streaming
 * Response, ready to be returned from a route handler. `null` when missing.
 */
export async function openAsset(segments: string[]): Promise<Response | null> {
  if (segments.length < 2 || !segments.every(isSafeSegment)) return null;
  const file = segments[segments.length - 1];

  if (API_URL) {
    const url = `${API_URL}/worlds/${segments.map(encodeURIComponent).join("/")}`;
    const upstream = await fetch(url, { headers: apiHeaders(), cache: "no-store" });
    if (upstream.status === 404) return null;
    if (!upstream.ok || !upstream.body) throw apiError(upstream.status);
    const headers = new Headers();
    for (const h of ["content-type", "content-length", "etag", "last-modified", "accept-ranges"]) {
      const v = upstream.headers.get(h);
      if (v) headers.set(h, v);
    }
    if (!headers.has("content-type")) headers.set("content-type", mimeFor(file));
    headers.set("cache-control", "public, max-age=31536000, immutable");
    return new Response(upstream.body, { status: 200, headers });
  }

  const path = join(ASSETS_DIR, "worlds", ...segments);
  let size: number;
  try {
    const s = await stat(path);
    if (!s.isFile()) return null;
    size = s.size;
  } catch {
    return null;
  }
  const stream = Readable.toWeb(createReadStream(path)) as ReadableStream<Uint8Array>;
  return new Response(stream, {
    status: 200,
    headers: {
      "content-type": mimeFor(file),
      "content-length": String(size),
      "cache-control": "public, max-age=31536000, immutable",
    },
  });
}

/** Replace the world's navigation graph (stops + edges tagged in the viewer). Returns the updated manifest. */
export async function saveGraph(id: string, graph: NavigationGraph): Promise<WorldManifest | null> {
  if (!isSafeSegment(id)) return null;
  if (API_URL) {
    const res = await fetch(`${API_URL}/worlds/${encodeURIComponent(id)}/graph`, {
      method: "PUT",
      headers: { ...apiHeaders(), "content-type": "application/json" },
      body: JSON.stringify(graph),
      cache: "no-store",
    });
    if (res.status === 404) return null;
    if (!res.ok) throw apiError(res.status);
    return parseManifest(await res.json());
  }
  const manifest = await readLocalManifest(id);
  if (!manifest) return null;
  const next: WorldManifest = { ...manifest, navigationGraph: graph, updatedAt: new Date().toISOString() };
  await writeFile(join(ASSETS_DIR, "worlds", id, "world.json"), `${JSON.stringify(next, null, 2)}\n`);
  return next;
}

export async function getMeasurements(id: string): Promise<Measurement[]> {
  if (!isSafeSegment(id)) return [];
  if (API_URL) {
    const res = await fetch(`${API_URL}/worlds/${encodeURIComponent(id)}/measurements`, {
      headers: apiHeaders(),
      cache: "no-store",
    });
    if (res.status === 404) return [];
    if (!res.ok) throw apiError(res.status);
    return parseMeasurements(((await res.json()) as MeasurementsFile).measurements ?? []);
  }
  try {
    const raw = await readFile(join(ASSETS_DIR, "worlds", id, "measurements.json"), "utf8");
    return parseMeasurements((JSON.parse(raw) as MeasurementsFile).measurements ?? []);
  } catch {
    return [];
  }
}

export async function saveMeasurements(id: string, measurements: Measurement[]): Promise<MeasurementsFile | null> {
  if (!isSafeSegment(id)) return null;
  const file: MeasurementsFile = {
    schema: MEASUREMENTS_SCHEMA,
    worldId: id,
    measurements,
    updatedAt: new Date().toISOString(),
  };
  if (API_URL) {
    const res = await fetch(`${API_URL}/worlds/${encodeURIComponent(id)}/measurements`, {
      method: "PUT",
      headers: { ...apiHeaders(), "content-type": "application/json" },
      body: JSON.stringify(file),
      cache: "no-store",
    });
    if (res.status === 404) return null;
    if (!res.ok) throw apiError(res.status);
    return (await res.json()) as MeasurementsFile;
  }
  const dir = join(ASSETS_DIR, "worlds", id);
  if (!(await readLocalManifest(id))) return null;
  await mkdir(dir, { recursive: true });
  await writeFile(join(dir, "measurements.json"), `${JSON.stringify(file, null, 2)}\n`);
  return file;
}

function apiError(status: number): Error {
  return new Error(
    status === 401 || status === 403
      ? "Worlds API rejected the API key — check WANDER_API_KEY matches the backend"
      : `Worlds API responded ${status}`,
  );
}

function mimeFor(file: string): string {
  return MIME[extname(file).toLowerCase()] ?? "application/octet-stream";
}

async function readLocalManifest(id: string): Promise<WorldManifest | null> {
  try {
    const raw = await readFile(join(ASSETS_DIR, "worlds", id, "world.json"), "utf8");
    const manifest = parseManifest(JSON.parse(raw));
    if (manifest.id !== id) {
      console.warn(`[worlds] ${id}/world.json declares id "${manifest.id}"; skipping`);
      return null;
    }
    return manifest;
  } catch (err) {
    if ((err as NodeJS.ErrnoException).code !== "ENOENT")
      console.warn(`[worlds] could not read ${id}/world.json:`, (err as Error).message);
    return null;
  }
}

function safeParse(input: unknown): WorldManifest[] {
  try {
    return [parseManifest(input)];
  } catch (err) {
    console.warn("[worlds] skipping invalid manifest from API:", (err as Error).message);
    return [];
  }
}
