"use client";

import { nextVersion, type WorldManifest } from "./world-manifest";
import type { WorldStatus } from "./worlds";

/**
 * Browser-side upload flows against the Next.js proxy (/api/worlds). XHR is
 * used for the file itself because `fetch` still has no upload progress in
 * Safari.
 */

export type UploadProgress = { loaded: number; total: number };

export class UploadError extends Error {
  constructor(
    public readonly status: number,
    message: string,
  ) {
    super(message);
  }
}

async function readError(res: Response, fallback: string): Promise<string> {
  const body = (await res.json().catch(() => null)) as { error?: string } | null;
  return body?.error ?? `${fallback} (${res.status})`;
}

/** PUT one file to `worlds/<id>/<version>/<filename>` with progress. Resolves to the stored path. */
export function uploadSplatFile(
  worldId: string,
  version: string,
  file: File,
  onProgress: (p: UploadProgress) => void,
  signal?: AbortSignal,
): Promise<{ path: string; bytes: number }> {
  const url = `/api/worlds/${encodeURIComponent(worldId)}/${encodeURIComponent(version)}/${encodeURIComponent(file.name)}`;
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.open("PUT", url);
    xhr.setRequestHeader("content-type", "application/octet-stream");
    xhr.upload.onprogress = (e) => onProgress({ loaded: e.loaded, total: e.lengthComputable ? e.total : file.size });
    xhr.onerror = () => reject(new UploadError(0, "Network error while uploading"));
    xhr.onabort = () => reject(new UploadError(0, "Upload cancelled"));
    xhr.onload = () => {
      let body: { path?: string; bytes?: number; error?: string } = {};
      try {
        body = JSON.parse(xhr.responseText);
      } catch {
        /* non-JSON error page */
      }
      if (xhr.status >= 200 && xhr.status < 300 && body.path)
        resolve({ path: body.path, bytes: body.bytes ?? file.size });
      else reject(new UploadError(xhr.status, body.error ?? `Upload failed (${xhr.status})`));
    };
    signal?.addEventListener("abort", () => xhr.abort(), { once: true });
    xhr.send(file);
  });
}

export type NewWorldInput = {
  id: string;
  name: string;
  space?: string;
  nianticSiteId?: string;
  file: File | null;
  /** Aligned collision mesh (.glb); goes into the same version as the splat. */
  mesh?: File | null;
};

/** Create the manifest, then (optionally) upload the splat and mesh and mark the world ready. */
export async function createWorldWithSplat(
  input: NewWorldInput,
  onProgress: (p: UploadProgress) => void,
  onStage: (stage: string) => void,
  signal?: AbortSignal,
): Promise<WorldManifest> {
  onStage("Creating world");
  const res = await fetch("/api/worlds", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({
      id: input.id,
      name: input.name,
      space: input.space || undefined,
      nianticSiteId: input.nianticSiteId || null,
      splatFilename: input.file ? safeFilename(input.file.name) : undefined,
    }),
    signal,
  });
  if (!res.ok) throw new UploadError(res.status, await readError(res, "Could not create the world"));
  let manifest = (await res.json()) as WorldManifest;
  if (!input.file && !input.mesh) return manifest;

  if (input.file) {
    onStage("Uploading splat");
    const file = renameFile(input.file, safeFilename(input.file.name));
    await uploadSplatFile(manifest.id, manifest.version, file, onProgress, signal);
  }
  if (input.mesh) {
    onStage("Uploading mesh");
    await uploadMeshForWorld(manifest, input.mesh, onProgress, signal);
  }

  onStage("Finishing");
  manifest = await patchWorld(manifest.id, { status: input.nianticSiteId ? "aligned" : "processing" }, signal);
  return manifest;
}

/**
 * Upload a splat for an existing world. Tries the manifest's current version
 * first (fills in a missing file); if that version already has the file, the
 * upload goes to the next version and the manifest is switched over.
 */
export async function uploadSplatForWorld(
  manifest: WorldManifest,
  rawFile: File,
  onProgress: (p: UploadProgress) => void,
  onStage: (stage: string) => void,
  signal?: AbortSignal,
): Promise<WorldManifest> {
  const file = renameFile(rawFile, safeFilename(rawFile.name));
  const currentFile = manifest.assets.splat.split("/").pop();
  let version = manifest.version;

  onStage(`Uploading to ${version}`);
  let stored: { path: string };
  try {
    stored = await uploadSplatFile(manifest.id, version, file, onProgress, signal);
  } catch (err) {
    if (!(err instanceof UploadError) || err.status !== 409) throw err;
    version = nextVersion(manifest.version);
    onStage(`Uploading to ${version}`);
    stored = await uploadSplatFile(manifest.id, version, file, onProgress, signal);
  }

  onStage("Switching version");
  const status: WorldStatus = manifest.nianticSiteId ? "aligned" : "processing";
  const needsSwitch = version !== manifest.version || file.name !== currentFile;
  return patchWorld(
    manifest.id,
    needsSwitch ? { version, assets: { ...manifest.assets, splat: stored.path }, status } : { status },
    signal,
  );
}

export const MESH_FILENAME = "mesh.glb";

/**
 * Upload the aligned collision mesh (Scaniverse .glb) into the world's current
 * version as `mesh.glb`. The server registers it under `assets.mesh` itself, so
 * no manifest patch is needed; versions are immutable, so an existing mesh is a 409.
 */
export async function uploadMeshForWorld(
  manifest: WorldManifest,
  rawFile: File,
  onProgress: (p: UploadProgress) => void,
  signal?: AbortSignal,
): Promise<{ path: string; bytes: number }> {
  if (!rawFile.name.toLowerCase().endsWith(".glb")) throw new UploadError(400, "The mesh must be a .glb file");
  try {
    return await uploadSplatFile(manifest.id, manifest.version, renameFile(rawFile, MESH_FILENAME), onProgress, signal);
  } catch (err) {
    if (err instanceof UploadError && err.status === 409)
      throw new UploadError(409, `${manifest.version} already has a mesh — upload a new splat version first, then add the mesh to it`);
    throw err;
  }
}

async function patchWorld(id: string, patch: unknown, signal?: AbortSignal): Promise<WorldManifest> {
  const res = await fetch(`/api/worlds/${encodeURIComponent(id)}`, {
    method: "PATCH",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(patch),
    signal,
  });
  if (!res.ok) throw new UploadError(res.status, await readError(res, "Could not update the world"));
  return (await res.json()) as WorldManifest;
}

/** Keep the extension, normalise the rest to a safe, predictable `scene.<ext>`. */
export function safeFilename(name: string): string {
  const ext = name.slice(name.lastIndexOf(".")).toLowerCase();
  return `scene${ext}`;
}

function renameFile(file: File, name: string): File {
  return file.name === name ? file : new File([file], name, { type: file.type, lastModified: file.lastModified });
}

export function formatBytes(n: number): string {
  if (n >= 1_073_741_824) return `${(n / 1_073_741_824).toFixed(2)} GB`;
  if (n >= 1_048_576) return `${(n / 1_048_576).toFixed(1)} MB`;
  if (n >= 1024) return `${Math.round(n / 1024)} KB`;
  return `${n} B`;
}
