"use client";

import { useState, type ReactNode } from "react";
import { Icon } from "@/components/Icon";
import {
  formatSplatCount,
  graphLengthMetres,
  measurementLength,
  type Measurement,
  type NavigationGraph,
  type NavNodeKind,
  type WorldManifest,
} from "@/lib/world-manifest";
import { STATUS_META, type WorldStatus } from "@/lib/worlds";
import { formatMetres } from "./SplatViewerEngine";

export type PanelTab = "stops" | "measure" | "details";

export const NODE_TONE: Record<NavNodeKind, string> = {
  waypoint: "bg-wander-blue",
  entrance: "bg-wander-sky",
  destination: "bg-wander-pink",
};

const KINDS: { id: NavNodeKind; label: string }[] = [
  { id: "waypoint", label: "Waypoint" },
  { id: "entrance", label: "Entrance" },
  { id: "destination", label: "Destination" },
];

const TABS: { id: PanelTab; label: string }[] = [
  { id: "stops", label: "Stops" },
  { id: "measure", label: "Measure" },
  { id: "details", label: "Details" },
];

type Props = {
  tab: PanelTab;
  onTab: (t: PanelTab) => void;
  onClose: () => void;
  name: string;
  status: WorldStatus;
  manifest: WorldManifest | null;
  splatUrl: string | null;
  numSplats: number | null;
  graph: NavigationGraph;
  measurements: Measurement[];
  selectedNode: string | null;
  autoLink: boolean;
  onAutoLink: (v: boolean) => void;
  onSelectNode: (id: string | null) => void;
  onFocusNode: (id: string) => void;
  onRenameNode: (id: string, name: string) => void;
  onKindNode: (id: string, kind: NavNodeKind) => void;
  onDeleteNode: (id: string) => void;
  onToggleEdge: (a: string, b: string) => void;
  onStartStop: () => void;
  onStartMeasure: () => void;
  onLabelMeasurement: (id: string, label: string) => void;
  onDeleteMeasurement: (id: string) => void;
  onClearMeasurements: () => void;
};

/** Right-hand panel: edit stops and edges, review measurements, read the manifest. */
export function InspectorPanel(p: Props) {
  return (
    <aside
      aria-label="World inspector"
      className="card pointer-events-auto flex max-h-full flex-col overflow-hidden p-0"
    >
      <div className="flex items-center gap-1 border-b border-hairline p-2">
        <div role="tablist" aria-label="Inspector" className="flex flex-1 items-center gap-0.5">
          {TABS.map((t) => (
            <button
              key={t.id}
              role="tab"
              type="button"
              aria-selected={p.tab === t.id}
              onClick={() => p.onTab(t.id)}
              className={`rounded-[6px] px-2.5 py-1 text-body-sm font-medium transition-colors duration-200 ${
                p.tab === t.id ? "bg-sky-tint text-wander-blue" : "text-void-black/60 hover:text-void-black"
              }`}
            >
              {t.label}
              {t.id === "stops" && p.graph.nodes.length > 0 && (
                <span className="ml-1 text-caption text-void-black/40">{p.graph.nodes.length}</span>
              )}
              {t.id === "measure" && p.measurements.length > 0 && (
                <span className="ml-1 text-caption text-void-black/40">{p.measurements.length}</span>
              )}
            </button>
          ))}
        </div>
        <button type="button" className="btn-icon size-7" aria-label="Close panel" onClick={p.onClose}>
          <Icon name="x" size={15} />
        </button>
      </div>

      <div className="min-h-0 flex-1 overflow-y-auto">
        {p.tab === "stops" && <StopsTab {...p} />}
        {p.tab === "measure" && <MeasureTab {...p} />}
        {p.tab === "details" && <DetailsTab {...p} />}
      </div>
    </aside>
  );
}

/* ------------------------------------------------------------------ stops */

function StopsTab(p: Props) {
  const { graph, selectedNode } = p;
  const selected = graph.nodes.find((n) => n.id === selectedNode) ?? null;
  const edgesOf = (id: string) => graph.edges.filter((e) => e.from === id || e.to === id).length;
  const linked = (a: string, b: string) =>
    graph.edges.some((e) => (e.from === a && e.to === b) || (e.from === b && e.to === a));
  const length = graphLengthMetres(graph);

  return (
    <div className="p-3">
      <div className="flex items-center justify-between gap-2 px-1">
        <p className="text-caption text-void-black/50">
          {graph.nodes.length} stops · {graph.edges.length} links · {Math.round(length)} m
        </p>
        <label className="flex items-center gap-1.5 text-caption text-void-black/70">
          <input
            type="checkbox"
            checked={p.autoLink}
            onChange={(e) => p.onAutoLink(e.target.checked)}
            className="size-3.5 accent-wander-blue"
          />
          Auto-link new stops
        </label>
      </div>

      <button type="button" className="btn-ghost mt-3 w-full" onClick={p.onStartStop}>
        <Icon name="pin" size={15} />
        Drop a stop on the scan
      </button>

      {graph.nodes.length === 0 ? (
        <p className="mt-4 px-1 text-body-sm text-void-black/50">
          No stops yet. Pick the tool above (or press <kbd className="rounded-sm border border-hairline px-1">3</kbd>)
          and click the scan where someone should be guided.
        </p>
      ) : (
        <ol className="mt-3 space-y-0.5">
          {graph.nodes.map((n, i) => {
            const isSel = n.id === selectedNode;
            return (
              <li key={n.id}>
                <div
                  className={`group flex items-center gap-2 rounded-lg px-2 py-1.5 transition-colors duration-200 ${
                    isSel ? "bg-sky-tint" : "hover:bg-void-black/5"
                  }`}
                >
                  <button
                    type="button"
                    onClick={() => p.onSelectNode(isSel ? null : n.id)}
                    onDoubleClick={() => p.onFocusNode(n.id)}
                    title="Click to select · double-click to fly to"
                    className="flex min-w-0 flex-1 items-center gap-2 text-left text-body-sm text-void-black/80"
                  >
                    <span className="w-4 text-right text-caption text-void-black/40">{i + 1}</span>
                    <span
                      aria-hidden="true"
                      className={`inline-block size-2.5 rounded-full ${NODE_TONE[n.kind ?? "waypoint"]}`}
                    />
                    <span className={`flex-1 truncate ${isSel ? "font-medium text-wander-blue" : ""}`}>
                      {n.name ?? n.id}
                    </span>
                    <span className="text-caption text-void-black/40">{edgesOf(n.id)}↔</span>
                  </button>
                  {selected && selected.id !== n.id && (
                    <button
                      type="button"
                      aria-pressed={linked(selected.id, n.id)}
                      title={
                        linked(selected.id, n.id)
                          ? `Unlink from ${selected.name ?? selected.id}`
                          : `Link to ${selected.name ?? selected.id}`
                      }
                      onClick={() => p.onToggleEdge(selected.id, n.id)}
                      className={`btn-icon size-6 ${
                        linked(selected.id, n.id) ? "text-wander-blue" : "opacity-0 group-hover:opacity-100 focus-visible:opacity-100"
                      }`}
                    >
                      <Icon name="link" size={13} />
                    </button>
                  )}
                </div>
                {isSel && (
                  <NodeEditor
                    key={n.id}
                    name={n.name ?? ""}
                    kind={n.kind ?? "waypoint"}
                    position={n.position}
                    onName={(v) => p.onRenameNode(n.id, v)}
                    onKind={(k) => p.onKindNode(n.id, k)}
                    onFocus={() => p.onFocusNode(n.id)}
                    onDelete={() => p.onDeleteNode(n.id)}
                  />
                )}
              </li>
            );
          })}
        </ol>
      )}
      {selected && graph.nodes.length > 1 && (
        <p className="mt-3 px-1 text-caption text-void-black/40">
          Hover another stop and press its link icon to connect it to “{selected.name ?? selected.id}”.
        </p>
      )}
    </div>
  );
}

function NodeEditor({
  name,
  kind,
  position,
  onName,
  onKind,
  onFocus,
  onDelete,
}: {
  name: string;
  kind: NavNodeKind;
  position: [number, number, number];
  onName: (v: string) => void;
  onKind: (k: NavNodeKind) => void;
  onFocus: () => void;
  onDelete: () => void;
}) {
  // Keyed by node id in the parent, so a fresh editor mounts per stop.
  const [draft, setDraft] = useState(name);

  return (
    <div className="mx-2 mt-1 mb-2 rounded-lg border border-hairline bg-stellar-white p-2.5">
      <label className="label text-caption text-void-black/60" htmlFor="stop-name">
        Name
      </label>
      <input
        id="stop-name"
        className="input mt-1 py-1 text-body-sm"
        value={draft}
        placeholder="e.g. Elevator bank"
        onChange={(e) => setDraft(e.target.value)}
        onBlur={() => draft !== name && onName(draft.trim())}
        onKeyDown={(e) => {
          if (e.key === "Enter") (e.target as HTMLInputElement).blur();
        }}
      />
      <div role="radiogroup" aria-label="Stop kind" className="mt-2 flex items-center gap-1">
        {KINDS.map((k) => (
          <button
            key={k.id}
            type="button"
            role="radio"
            aria-checked={kind === k.id}
            onClick={() => onKind(k.id)}
            className={`pill-sm border transition-colors duration-200 ${
              kind === k.id
                ? "border-transparent bg-sky-tint text-wander-blue"
                : "border-hairline bg-pure-white text-void-black/60 hover:text-void-black"
            }`}
          >
            <span aria-hidden="true" className={`size-1.5 rounded-full ${NODE_TONE[k.id]}`} />
            {k.label}
          </button>
        ))}
      </div>
      <div className="mt-2 flex items-center justify-between gap-2">
        <span className="font-mono text-[11px] text-void-black/40">
          {position.map((v) => v.toFixed(2)).join(", ")}
        </span>
        <span className="flex items-center gap-1">
          <button type="button" className="btn-text px-2 py-1 text-caption" onClick={onFocus}>
            <Icon name="frame" size={13} />
            Fly to
          </button>
          <button
            type="button"
            className="btn-text px-2 py-1 text-caption text-wander-pink hover:bg-pink-tint"
            onClick={onDelete}
          >
            <Icon name="trash" size={13} />
            Delete
          </button>
        </span>
      </div>
    </div>
  );
}

/* ---------------------------------------------------------------- measure */

function MeasureTab(p: Props) {
  const total = p.measurements.reduce((s, m) => s + measurementLength(m), 0);
  return (
    <div className="p-3">
      <div className="flex items-center justify-between gap-2 px-1">
        <p className="text-caption text-void-black/50">
          {p.measurements.length} measurements · {formatMetres(total)} total
        </p>
        {p.measurements.length > 0 && (
          <button type="button" className="btn-text px-2 py-0.5 text-caption" onClick={p.onClearMeasurements}>
            Clear all
          </button>
        )}
      </div>
      <button type="button" className="btn-ghost mt-3 w-full" onClick={p.onStartMeasure}>
        <Icon name="ruler" size={15} />
        Measure a distance
      </button>
      {p.measurements.length === 0 ? (
        <p className="mt-4 px-1 text-body-sm text-void-black/50">
          Click two points on the scan to measure the straight-line distance between them — door widths,
          corridor lengths, step heights. Distances are in metres.
        </p>
      ) : (
        <ul className="mt-3 space-y-1">
          {p.measurements.map((m, i) => (
            <li key={m.id} className="flex items-center gap-2 rounded-lg px-2 py-1 hover:bg-void-black/5">
              <span className="w-4 text-right text-caption text-void-black/40">{i + 1}</span>
              <span aria-hidden="true" className="inline-block size-2.5 rounded-full bg-wander-sky" />
              <input
                aria-label={`Label for measurement ${i + 1}`}
                className="min-w-0 flex-1 rounded-sm bg-transparent px-1 py-0.5 text-body-sm text-void-black placeholder:text-void-black/40 focus:bg-pure-white focus:outline-none focus:ring-2 focus:ring-wander-blue/20"
                placeholder="Add a label"
                defaultValue={m.label ?? ""}
                key={`${m.id}-${m.label ?? ""}`}
                onBlur={(e) => e.target.value.trim() !== (m.label ?? "") && p.onLabelMeasurement(m.id, e.target.value.trim())}
                onKeyDown={(e) => {
                  if (e.key === "Enter") (e.target as HTMLInputElement).blur();
                }}
              />
              <span className="text-body-sm font-medium text-void-black tabular-nums">
                {formatMetres(measurementLength(m))}
              </span>
              <button
                type="button"
                className="btn-icon size-6"
                aria-label="Delete measurement"
                onClick={() => p.onDeleteMeasurement(m.id)}
              >
                <Icon name="trash" size={13} />
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

/* ---------------------------------------------------------------- details */

function DetailsTab({ name, status, manifest, splatUrl, numSplats }: Props) {
  const meta = STATUS_META[status];
  const splatFile = manifest?.assets.splat.split("/").pop();
  return (
    <div>
      <div className="border-b border-hairline p-4">
        <span className={`pill-sm ${meta.className}`}>{meta.label}</span>
        <h2 className="mt-2 text-heading-sm font-bold text-void-black">{name}</h2>
        {manifest?.description && <p className="mt-1 text-body-sm text-slate">{manifest.description}</p>}
      </div>
      <dl className="grid grid-cols-[auto_1fr] gap-x-4 gap-y-2 p-4 text-body-sm">
        <Row label="Niantic site">
          {manifest?.nianticSiteId ?? <span className="text-void-black/40">Not published</span>}
        </Row>
        <Row label="Version">{manifest?.version ?? "—"}</Row>
        <Row label="Splat">
          {splatFile ? (
            <span title={manifest?.assets.splat} className="break-all">
              {splatFile}
            </span>
          ) : (
            "—"
          )}
        </Row>
        <Row label="Splats">{formatSplatCount(numSplats ?? manifest?.stats?.splatCount)}</Row>
        <Row label="Frame">
          {manifest?.alignment?.frame ?? <span className="text-void-black/40">Unaligned</span>}
        </Row>
        <Row label="Graph frame">{manifest?.navigationGraph?.frame ?? "world"}</Row>
        {manifest?.stats?.captureApp && <Row label="Captured with">{manifest.stats.captureApp}</Row>}
        {manifest?.updatedAt && <Row label="Updated">{new Date(manifest.updatedAt).toLocaleString()}</Row>}
      </dl>
      {splatUrl && (
        <div className="border-t border-hairline p-3">
          <a href={splatUrl} download={splatFile} className="btn-ghost w-full">
            <Icon name="download" size={15} />
            Download {splatFile ?? "splat"}
          </a>
        </div>
      )}
    </div>
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
