"use client";

import { useRef, useState, type ReactNode } from "react";
import { Icon } from "@/components/Icon";
import { issueLabel, issueTarget, type GraphIssue, type NavmeshParams } from "@/lib/navmesh";
import { formatBytes, uploadMeshForWorld, UploadError, type UploadProgress } from "@/lib/upload-client";
import { graphLengthMetres, type NavigationGraph, type WorldManifest } from "@/lib/world-manifest";
import type { ViewerSelection } from "./SplatViewerEngine";
import type { MeshTools } from "./useMeshTools";
import type { ViewerState } from "./useSplatViewer";

export type MeshTabProps = {
  manifest: WorldManifest | null;
  graph: NavigationGraph;
  mesh: ViewerState["mesh"];
  showMesh: boolean;
  onShowMesh: (visible: boolean) => void;
  tools: MeshTools;
  selection: ViewerSelection | null;
  onSelect: (sel: ViewerSelection | null) => void;
  onFocusNode: (id: string) => void;
  /** Called after a graph write (snap / accept) with the manifest the server returned. */
  onGraphSaved: (manifest: WorldManifest, text: string) => void;
  /** Called after a mesh upload so the page can re-read the manifest. */
  onMeshUploaded: () => void;
  /** Whether the server can run the mesh tools (needs the worlds backend). */
  source: "api" | "local";
};

/**
 * Mesh tab: the aligned Scaniverse mesh as a layer, the graph validator
 * (edges through walls, off-floor nodes, floor snapping) and the review gate
 * for graphs generated from the mesh. Generated geometry only becomes the
 * world's graph when the reviewer accepts it here.
 */
export function MeshTab(p: MeshTabProps) {
  const { manifest, tools } = p;
  if (!manifest) return <p className="p-4 text-body-sm text-void-black/50">Add world.json to this world to attach a mesh.</p>;
  return (
    <div>
      <MeshLayer {...p} manifest={manifest} />
      {tools.hasMesh && p.source === "local" && (
        <p className="border-b border-hairline p-4 text-body-sm text-void-black/50">
          Graph checks and generation run in the worlds backend. Set <code>WANDER_API_URL</code> to use them here.
        </p>
      )}
      {tools.hasMesh && p.source === "api" && (
        <>
          <Validator {...p} />
          <Proposal {...p} />
        </>
      )}
    </div>
  );
}

/* ------------------------------------------------------------------ layer */

function MeshLayer({ manifest, mesh, showMesh, onShowMesh, onMeshUploaded }: MeshTabProps & { manifest: WorldManifest }) {
  const file = manifest.assets.mesh?.split("/").pop();
  const inputRef = useRef<HTMLInputElement>(null);
  const [upload, setUpload] = useState<{ progress: UploadProgress | null; error: string | null; running: boolean }>({
    progress: null,
    error: null,
    running: false,
  });

  const onFile = async (picked: File | undefined) => {
    if (!picked) return;
    setUpload({ progress: { loaded: 0, total: picked.size }, error: null, running: true });
    try {
      await uploadMeshForWorld(manifest, picked, (progress) => setUpload((s) => ({ ...s, progress })));
      setUpload({ progress: null, error: null, running: false });
      onMeshUploaded();
    } catch (err) {
      setUpload({
        progress: null,
        running: false,
        error: err instanceof UploadError || err instanceof Error ? err.message : "Upload failed",
      });
    } finally {
      if (inputRef.current) inputRef.current.value = "";
    }
  };

  return (
    <div className="border-b border-hairline p-4">
      <div className="flex items-center justify-between">
        <h3 className="text-caption font-semibold tracking-[0.01em] text-void-black/50 uppercase">Mesh layer</h3>
        {mesh.status === "ready" && mesh.triangles !== null && (
          <span className="text-caption text-void-black/40">{mesh.triangles.toLocaleString()} triangles</span>
        )}
      </div>

      {file ? (
        <dl className="mt-2 grid grid-cols-[auto_1fr] gap-x-4 gap-y-1.5 text-body-sm">
          <Row label="File">
            <span title={manifest.assets.mesh} className="break-all">
              {file}
            </span>
          </Row>
          <Row label="Frame">{manifest.meshFrame === "splat" ? "splat (through alignment)" : "world (aligned)"}</Row>
          <Row label="Status">
            {mesh.status === "loading" && "Loading…"}
            {mesh.status === "ready" && "Loaded"}
            {mesh.status === "none" && "—"}
            {mesh.status === "error" && <span className="text-wander-pink">{mesh.error ?? "Failed to load"}</span>}
          </Row>
        </dl>
      ) : (
        <p className="mt-2 text-body-sm text-void-black/50">
          No mesh on this version. Upload the Scaniverse <code>.glb</code> aligned to the VPS frame: it draws as a layer, gives
          clicks a real surface to land on, and lets Wander check and generate waypoints.
        </p>
      )}

      <div className="mt-3 flex flex-col gap-2">
        {file && (
          <label className="flex cursor-pointer items-center justify-between gap-3 rounded-lg px-2 py-1.5 text-body-sm text-void-black hover:bg-void-black/5">
            <span className="inline-flex items-center gap-2">
              <Icon name="layers" size={15} />
              Show mesh in the scene
            </span>
            <input
              type="checkbox"
              className="size-4 accent-wander-blue"
              checked={showMesh}
              disabled={mesh.status !== "ready"}
              onChange={(e) => onShowMesh(e.target.checked)}
            />
          </label>
        )}
        <input
          ref={inputRef}
          type="file"
          accept=".glb,model/gltf-binary"
          className="sr-only"
          aria-label="Choose a mesh file"
          onChange={(e) => onFile(e.target.files?.[0])}
        />
        {!file && (
          <button type="button" className="btn-ghost w-full" disabled={upload.running} onClick={() => inputRef.current?.click()}>
            <Icon name="upload" size={15} />
            {upload.running && upload.progress
              ? `Uploading… ${formatBytes(upload.progress.loaded)} / ${formatBytes(upload.progress.total)}`
              : `Upload mesh.glb to ${manifest.version}`}
          </button>
        )}
        {upload.error && (
          <p role="alert" className="text-caption text-wander-pink">
            {upload.error}
          </p>
        )}
      </div>
    </div>
  );
}

/* -------------------------------------------------------------- validator */

function Validator({ graph, tools, selection, onSelect, onFocusNode, onGraphSaved }: MeshTabProps) {
  const { validation, validating, validate, snappedCount, saving, saveGraph, preview } = tools;
  const disabled = graph.nodes.length === 0 || validating.running || preview;

  return (
    <div className="border-b border-hairline p-4">
      <div className="flex items-center justify-between">
        <h3 className="text-caption font-semibold tracking-[0.01em] text-void-black/50 uppercase">Check waypoints</h3>
        {validation && (
          <span className="text-caption text-void-black/40">
            {validation.issues.length === 0 ? "No issues" : `${validation.issues.length} issues`} · floor {validation.floorY.toFixed(2)} m
          </span>
        )}
      </div>
      <p className="mt-2 text-body-sm text-void-black/50">
        Flags edges that cut through walls, waypoints off the scanned floor, and heights that do not sit on it. Flagged parts
        turn pink in the scene.
      </p>
      <button type="button" className="btn-ghost mt-3 w-full" disabled={disabled} onClick={validate}>
        <Icon name="check" size={15} />
        {validating.running ? "Checking…" : graph.nodes.length === 0 ? "No waypoints to check" : "Check against the mesh"}
      </button>
      {validating.error && <Alert>{validating.error}</Alert>}

      {validation && (
        <>
          {validation.issues.length > 0 && (
            <IssueList issues={validation.issues} selection={selection} onSelect={onSelect} onFocusNode={onFocusNode} />
          )}
          {snappedCount > 0 && (
            <button
              type="button"
              className="btn-primary mt-3 w-full"
              disabled={saving.running}
              onClick={async () => {
                const manifest = await saveGraph(validation.graph);
                if (manifest) onGraphSaved(manifest, `Snapped ${snappedCount} waypoints to the floor`);
              }}
            >
              <Icon name="save" size={15} />
              {saving.running ? "Saving…" : `Snap ${snappedCount} ${snappedCount === 1 ? "waypoint" : "waypoints"} to the floor`}
            </button>
          )}
          {saving.error && <Alert>{saving.error}</Alert>}
        </>
      )}
    </div>
  );
}

/* --------------------------------------------------------------- proposal */

const PARAM_FIELDS: { key: keyof Omit<NavmeshParams, "frame" | "seed" | "floorSlopeDeg">; label: string; step: number; min: number; max: number }[] = [
  { key: "cell", label: "Cell size (m)", step: 0.05, min: 0.05, max: 1 },
  { key: "agentRadius", label: "Person radius (m)", step: 0.05, min: 0.1, max: 1 },
  { key: "stepHeight", label: "Step height (m)", step: 0.05, min: 0.05, max: 0.6 },
  { key: "spacing", label: "Waypoint spacing (m)", step: 0.25, min: 0.5, max: 6 },
];

function Proposal({ graph, tools, onGraphSaved }: MeshTabProps) {
  const { proposal, building, build, params, setParams, preview, setPreview, discardProposal, saving, saveGraph } = tools;
  const [showParams, setShowParams] = useState(false);

  return (
    <div className="p-4">
      <div className="flex items-center justify-between">
        <h3 className="text-caption font-semibold tracking-[0.01em] text-void-black/50 uppercase">Generate waypoints</h3>
        {proposal && (
          <span className="text-caption text-void-black/40">
            {proposal.graph.nodes.length} · {Math.round(graphLengthMetres(proposal.graph))} m
          </span>
        )}
      </div>
      <p className="mt-2 text-body-sm text-void-black/50">
        Grids the walkable floor from the mesh and proposes a waypoint graph. It is only a proposal until you accept it;
        accepting replaces the current {graph.nodes.length} waypoints.
      </p>

      <button
        type="button"
        className="btn-text mt-2 w-full justify-between px-2"
        aria-expanded={showParams}
        onClick={() => setShowParams((v) => !v)}
      >
        <span className="text-caption text-void-black/60">Grid settings</span>
        <Icon name={showParams ? "chevronDown" : "chevronRight"} size={14} />
      </button>
      {showParams && (
        <div className="grid grid-cols-2 gap-2 px-1 pb-1">
          {PARAM_FIELDS.map((f) => (
            <label key={f.key} className="flex flex-col gap-1 text-caption text-void-black/60">
              {f.label}
              <input
                type="number"
                className="input px-2 py-1 text-body-sm tabular-nums"
                value={params[f.key]}
                step={f.step}
                min={f.min}
                max={f.max}
                onChange={(e) => {
                  const v = Number(e.target.value);
                  if (Number.isFinite(v)) setParams({ ...params, [f.key]: v });
                }}
              />
            </label>
          ))}
        </div>
      )}

      <button type="button" className="btn-ghost mt-2 w-full" disabled={building.running} onClick={build}>
        <Icon name="route" size={15} />
        {building.running ? "Gridding the mesh…" : proposal ? "Generate again" : "Generate from the mesh"}
      </button>
      {building.error && <Alert>{building.error}</Alert>}

      {proposal && (
        <div className="mt-3 rounded-lg border border-hairline bg-stellar-white p-3">
          <div className="flex items-center justify-between gap-2">
            <span className="pill-sm bg-pink-tint text-wander-pink">Proposed · not live</span>
            <span className="text-caption text-void-black/40">{new Date(proposal.createdAt).toLocaleString()}</span>
          </div>
          <dl className="mt-2 grid grid-cols-[auto_1fr] gap-x-4 gap-y-1 text-body-sm">
            <Row label="Walkable">
              {(proposal.grid.walkableCells * proposal.grid.cell ** 2).toFixed(0)} m² of{" "}
              {(proposal.grid.floorCells * proposal.grid.cell ** 2).toFixed(0)} m² floor
            </Row>
            <Row label="Floor">{proposal.grid.floorY.toFixed(2)} m</Row>
            <Row label="Grid">
              {proposal.grid.width} × {proposal.grid.height} @ {proposal.params.cell} m
            </Row>
            {proposal.currentGraphIssues.length > 0 && (
              <Row label="Current graph">{proposal.currentGraphIssues.length} issues against this mesh</Row>
            )}
          </dl>
          <OccupancyPreview rows={proposal.grid.rows} />

          <label className="mt-3 flex cursor-pointer items-center justify-between gap-3 rounded-lg px-1 py-1 text-body-sm text-void-black">
            <span className="inline-flex items-center gap-2">
              <Icon name="eye" size={15} />
              Preview in the scene
            </span>
            <input type="checkbox" className="size-4 accent-wander-blue" checked={preview} onChange={(e) => setPreview(e.target.checked)} />
          </label>

          <div className="mt-3 flex gap-2">
            <button
              type="button"
              className="btn-primary flex-1"
              disabled={saving.running}
              onClick={async () => {
                const manifest = await saveGraph(proposal.graph);
                if (manifest) {
                  discardProposal();
                  onGraphSaved(manifest, `Accepted ${proposal.graph.nodes.length} generated waypoints`);
                }
              }}
            >
              <Icon name="check" size={15} />
              {saving.running ? "Saving…" : "Accept as the graph"}
            </button>
            <button type="button" className="btn-text" onClick={discardProposal}>
              Dismiss
            </button>
          </div>
          {saving.error && <Alert>{saving.error}</Alert>}
        </div>
      )}
    </div>
  );
}

/** Tiny top-down map of the occupancy grid ('.' walkable, 'x' blocked, ' ' unscanned). */
function OccupancyPreview({ rows }: { rows: string[] }) {
  const height = rows.length;
  const width = rows[0]?.length ?? 0;
  if (!height || !width) return null;
  const rects: ReactNode[] = [];
  // Run-length encode each row so a 200×200 grid stays a few hundred elements.
  rows.forEach((row, z) => {
    let start = 0;
    for (let x = 1; x <= row.length; x++) {
      if (x < row.length && row[x] === row[start]) continue;
      const c = row[start];
      if (c !== " ")
        rects.push(
          <rect key={`${z}-${start}`} x={start} y={z} width={x - start} height={1} fill={c === "." ? "#60baf4" : "#1e293b"} />,
        );
      start = x;
    }
  });
  return (
    <svg
      viewBox={`0 0 ${width} ${height}`}
      role="img"
      aria-label="Top-down occupancy grid: sky is walkable, navy is blocked"
      className="mt-3 max-h-48 w-full rounded-lg border border-hairline bg-pure-white"
      shapeRendering="crispEdges"
      preserveAspectRatio="xMidYMid meet"
    >
      {rects}
    </svg>
  );
}

/* ----------------------------------------------------------------- pieces */

function IssueList({
  issues,
  selection,
  onSelect,
  onFocusNode,
}: {
  issues: GraphIssue[];
  selection: ViewerSelection | null;
  onSelect: (sel: ViewerSelection | null) => void;
  onFocusNode: (id: string) => void;
}) {
  const selected = selection?.kind === "node" ? selection.id : null;
  return (
    <ul className="mt-3 max-h-56 space-y-0.5 overflow-y-auto">
      {issues.map((issue, i) => {
        const node = "node" in issue ? issue.node : issue.from;
        const isSel = node === selected;
        return (
          <li key={i}>
            <button
              type="button"
              title={`${issue.message} · double-click to fly to`}
              onClick={() => onSelect(isSel ? null : { kind: "node", id: node })}
              onDoubleClick={() => onFocusNode(node)}
              className={`flex w-full items-center gap-2 rounded-lg px-2 py-1.5 text-left text-body-sm transition-colors duration-200 ${
                isSel ? "bg-sky-tint text-wander-blue" : "text-void-black/80 hover:bg-void-black/5 hover:text-void-black"
              }`}
            >
              <span aria-hidden="true" className="inline-block size-2.5 shrink-0 rounded-full bg-wander-pink" />
              <span className="flex-1 truncate">{issueTarget(issue)}</span>
              <span className="shrink-0 text-caption text-void-black/50">{issueLabel(issue)}</span>
            </button>
          </li>
        );
      })}
    </ul>
  );
}

function Alert({ children }: { children: ReactNode }) {
  return (
    <p role="alert" className="mt-2 text-caption text-wander-pink">
      {children}
    </p>
  );
}

function Row({ label, children }: { label: string; children: ReactNode }) {
  return (
    <>
      <dt className="text-void-black/50">{label}</dt>
      <dd className="min-w-0 text-void-black">{children}</dd>
    </>
  );
}
