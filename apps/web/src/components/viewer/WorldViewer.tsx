"use client";

import Link from "next/link";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { Icon, type IconName } from "@/components/Icon";
import { LogoMark } from "@/components/Logo";
import {
  EMPTY_GRAPH,
  formatSplatCount,
  type Measurement,
  type NavigationGraph,
  type NavNodeKind,
  type Vec3,
  type WorldManifest,
} from "@/lib/world-manifest";
import { STATUS_META, type WorldStatus } from "@/lib/worlds";
import { InspectorPanel, type PanelTab } from "./InspectorPanel";
import type { ViewerMode, ViewerTool } from "./SplatViewerEngine";
import { useSplatViewer, type PickHandler } from "./useSplatViewer";
import { ViewerOverlay } from "./ViewerOverlays";

type Props = {
  worldId: string;
  name: string;
  status: WorldStatus;
  manifest: WorldManifest | null;
  /** Same-origin URL of the splat (via /api/worlds), or null when nothing is uploaded yet. */
  splatUrl: string | null;
  initialMeasurements: Measurement[];
  /** Where the server is reading worlds from; only changes the empty-state hint. */
  source: "api" | "local";
};

const MODES: { id: ViewerMode; label: string; icon: IconName }[] = [
  { id: "orbit", label: "Orbit", icon: "orbit" },
  { id: "walk", label: "Walk", icon: "walk" },
];

const TOOLS: { id: ViewerTool; label: string; icon: IconName; key: string }[] = [
  { id: "navigate", label: "Navigate", icon: "pointer", key: "1" },
  { id: "measure", label: "Measure", icon: "ruler", key: "2" },
  { id: "stop", label: "Add stop", icon: "pin", key: "3" },
];

const isEditing = () => {
  const el = document.activeElement;
  return el instanceof HTMLInputElement || el instanceof HTMLTextAreaElement || el instanceof HTMLSelectElement;
};

/**
 * Full-viewport world editor: the splat canvas fills the page; a floating
 * header, a bottom tool dock and a collapsible inspector sit on top. Graph and
 * measurement edits live here and are pushed into the engine via the hook.
 */
export function WorldViewer({ worldId, name, status, manifest, splatUrl, initialMeasurements, source }: Props) {
  /* ------------------------------------------------------------ edit state */
  const initialGraph = useMemo<NavigationGraph>(
    () => manifest?.navigationGraph ?? { ...EMPTY_GRAPH },
    [manifest],
  );
  const [graph, setGraph] = useState<NavigationGraph>(initialGraph);
  const [savedGraph, setSavedGraph] = useState(initialGraph);
  const [measurements, setMeasurements] = useState(initialMeasurements);
  const [savedMeasurements, setSavedMeasurements] = useState(initialMeasurements);
  const [selectedNode, setSelectedNode] = useState<string | null>(null);
  const [pendingPoint, setPendingPoint] = useState<Vec3 | null>(null);
  const [autoLink, setAutoLink] = useState(true);
  const [lastAdded, setLastAdded] = useState<string | null>(null);
  const graphRef = useRef(graph);
  useEffect(() => {
    graphRef.current = graph;
  }, [graph]);

  const [panelOpen, setPanelOpen] = useState(true);
  const [panelTab, setPanelTab] = useState<PanelTab>("stops");
  const [saving, setSaving] = useState(false);
  const [notice, setNotice] = useState<{ tone: "ok" | "error"; text: string } | null>(null);

  const graphDirty = JSON.stringify(graph) !== JSON.stringify(savedGraph);
  const measureDirty = JSON.stringify(measurements) !== JSON.stringify(savedMeasurements);
  const dirty = graphDirty || measureDirty;
  const canSave = !!manifest;

  /* ------------------------------------------------------------ mutations */
  const updateGraph = useCallback((fn: (g: NavigationGraph) => NavigationGraph) => setGraph((g) => fn(g)), []);

  const addStop = useCallback(
    (position: Vec3) => {
      const g = graphRef.current;
      const id = nextId(g, "stop");
      const linkFrom = autoLink ? (selectedNode ?? lastAdded) : null;
      const from = linkFrom && g.nodes.some((n) => n.id === linkFrom) ? linkFrom : null;
      setGraph({
        ...g,
        nodes: [...g.nodes, { id, name: `Stop ${g.nodes.length + 1}`, kind: "waypoint", position }],
        edges: from ? [...g.edges, { from, to: id }] : g.edges,
      });
      setLastAdded(id);
      setSelectedNode(id);
      setPanelOpen(true);
      setPanelTab("stops");
    },
    [autoLink, selectedNode, lastAdded],
  );

  const deleteNode = useCallback((id: string) => {
    setGraph((g) => ({
      ...g,
      nodes: g.nodes.filter((n) => n.id !== id),
      edges: g.edges.filter((e) => e.from !== id && e.to !== id),
    }));
    setSelectedNode((s) => (s === id ? null : s));
    setLastAdded((s) => (s === id ? null : s));
  }, []);

  const toggleEdge = useCallback((a: string, b: string) => {
    setGraph((g) => {
      const idx = g.edges.findIndex((e) => (e.from === a && e.to === b) || (e.from === b && e.to === a));
      return {
        ...g,
        edges: idx >= 0 ? g.edges.filter((_, i) => i !== idx) : [...g.edges, { from: a, to: b }],
      };
    });
  }, []);

  const addMeasurement = useCallback((a: Vec3, b: Vec3) => {
    setMeasurements((list) => [
      ...list,
      { id: `m-${Date.now().toString(36)}`, points: [a, b], createdAt: new Date().toISOString() },
    ]);
    setPanelTab("measure");
  }, []);

  /* --------------------------------------------------------------- viewer */
  const onPick = useCallback<PickHandler>(
    (e) => {
      if (e.type === "pick-node") {
        setSelectedNode((s) => (s === e.id && e.tool === "navigate" ? null : e.id));
        if (e.tool !== "measure") setPanelTab("stops");
        return;
      }
      if (e.type === "pick-miss") {
        if (e.tool === "navigate") setSelectedNode(null);
        else setNotice({ tone: "error", text: "Click on the scan itself — that spot has no splats." });
        return;
      }
      if (e.tool === "stop") addStop(e.graphPoint);
      else if (e.tool === "measure") {
        if (pendingPoint) {
          addMeasurement(pendingPoint, e.point);
          setPendingPoint(null);
        } else setPendingPoint(e.point);
      }
    },
    [addStop, addMeasurement, pendingPoint],
  );

  const { containerRef, state, api, focusViewer } = useSplatViewer({
    splatUrl,
    alignment: manifest?.alignment,
    graph,
    measurements,
    selectedNode,
    pendingPoint,
    onPick,
  });

  const pickTool = useCallback(
    (tool: ViewerTool) => {
      api.setTool(tool);
      if (tool !== "measure") setPendingPoint(null);
      if (tool === "stop") setPanelTab("stops");
      if (tool === "measure") setPanelTab("measure");
      focusViewer();
    },
    [api, focusViewer],
  );

  /* ------------------------------------------------------------ keyboard */
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.metaKey || e.ctrlKey || e.altKey || isEditing()) return;
      if (e.key === "Escape") {
        if (pendingPoint) setPendingPoint(null);
        else if (selectedNode) setSelectedNode(null);
        else if (state.tool !== "navigate") pickTool("navigate");
        return;
      }
      if ((e.key === "Delete" || e.key === "Backspace") && selectedNode) {
        e.preventDefault();
        deleteNode(selectedNode);
        return;
      }
      const tool = TOOLS.find((t) => t.key === e.key);
      if (tool) pickTool(tool.id);
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [pendingPoint, selectedNode, state.tool, pickTool, deleteNode]);

  useEffect(() => {
    if (!notice) return;
    const t = setTimeout(() => setNotice(null), notice.tone === "ok" ? 2500 : 4000);
    return () => clearTimeout(t);
  }, [notice]);

  // Warn before leaving with unsaved stops / measurements.
  useEffect(() => {
    if (!dirty) return;
    const onLeave = (e: BeforeUnloadEvent) => e.preventDefault();
    window.addEventListener("beforeunload", onLeave);
    return () => window.removeEventListener("beforeunload", onLeave);
  }, [dirty]);

  /* ------------------------------------------------------------------ save */
  async function save() {
    if (!canSave || !dirty || saving) return;
    setSaving(true);
    try {
      if (graphDirty) {
        const res = await fetch(`/api/worlds/${encodeURIComponent(worldId)}/graph`, {
          method: "PUT",
          headers: { "content-type": "application/json" },
          body: JSON.stringify(graph),
        });
        if (!res.ok) throw new Error((await res.json().catch(() => null))?.error ?? `Save failed (${res.status})`);
        setSavedGraph(graph);
      }
      if (measureDirty) {
        const res = await fetch(`/api/worlds/${encodeURIComponent(worldId)}/measurements`, {
          method: "PUT",
          headers: { "content-type": "application/json" },
          body: JSON.stringify({ measurements }),
        });
        if (!res.ok) throw new Error((await res.json().catch(() => null))?.error ?? `Save failed (${res.status})`);
        setSavedMeasurements(measurements);
      }
      setNotice({ tone: "ok", text: "Saved to the world" });
    } catch (err) {
      setNotice({ tone: "error", text: err instanceof Error ? err.message : "Save failed" });
    } finally {
      setSaving(false);
    }
  }

  /* ---------------------------------------------------------------- render */
  const interactive = state.status === "ready" || state.status === "empty";
  const meta = STATUS_META[status];
  const linkSource = graph.nodes.find((n) => n.id === (selectedNode ?? lastAdded));
  const hint = hintFor(state.tool, state.mode, !!pendingPoint, autoLink ? linkSource?.name ?? linkSource?.id : undefined);

  return (
    <div className="relative h-dvh w-full overflow-hidden bg-wander-navy">
      <div
        ref={containerRef}
        role="application"
        aria-label={`${name} — 3D scene`}
        aria-busy={state.status === "loading" || state.status === "booting"}
        tabIndex={0}
        className="absolute inset-0 outline-none focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-wander-blue"
      />

      {/* Header */}
      <header className="pointer-events-none absolute inset-x-3 top-3 flex items-start justify-between gap-2">
        <div className="pointer-events-auto flex items-center gap-1 rounded-lg border border-hairline bg-pure-white p-1 pr-3">
          <Link href="/dashboard" className="btn-icon size-7" aria-label="Back to worlds">
            <Icon name="arrowLeft" size={16} />
          </Link>
          <LogoMark size={20} />
          <span className="max-w-[40vw] truncate text-body-sm font-semibold text-void-black">{name}</span>
          <span className={`pill-sm ml-1 ${meta.className}`}>{meta.label}</span>
          {dirty && <span className="pill-sm bg-pink-tint text-wander-pink">Unsaved</span>}
        </div>

        <div className="pointer-events-auto flex items-center gap-2">
          <div
            role="radiogroup"
            aria-label="Camera mode"
            className="flex items-center gap-0.5 rounded-lg border border-hairline bg-pure-white p-0.5"
          >
            {MODES.map((m) => (
              <button
                key={m.id}
                type="button"
                role="radio"
                aria-checked={state.mode === m.id}
                disabled={!interactive}
                onClick={() => {
                  api.setMode(m.id);
                  focusViewer();
                }}
                className={`inline-flex items-center gap-1.5 rounded-[6px] px-2.5 py-1 text-body-sm font-medium transition-colors duration-200 disabled:opacity-50 ${
                  state.mode === m.id ? "bg-sky-tint text-wander-blue" : "text-void-black/60 hover:text-void-black"
                }`}
              >
                <Icon name={m.icon} size={15} />
                <span className="hidden sm:inline">{m.label}</span>
              </button>
            ))}
          </div>
          <div className="flex items-center gap-0.5 rounded-lg border border-hairline bg-pure-white p-0.5">
            <ToolButton icon="frame" label="Reset view" disabled={!interactive} onClick={api.resetView} />
            <ToolButton icon="flip" label="Flip up axis" disabled={state.status !== "ready"} onClick={api.flipUp} />
            <ToolButton
              icon="route"
              label={state.showGraph ? "Hide stops and links" : "Show stops and links"}
              pressed={state.showGraph}
              disabled={!interactive}
              onClick={() => api.setShowGraph(!state.showGraph)}
            />
            <ToolButton
              icon="panelRight"
              label={panelOpen ? "Hide inspector" : "Show inspector"}
              pressed={panelOpen}
              onClick={() => setPanelOpen((v) => !v)}
            />
          </div>
        </div>
      </header>

      {/* Inspector */}
      {panelOpen && (
        <div className="pointer-events-none absolute inset-x-3 top-16 bottom-20 flex justify-end lg:inset-x-auto lg:right-3">
          <div className="flex max-h-full w-full lg:w-[340px]">
            <InspectorPanel
              tab={panelTab}
              onTab={setPanelTab}
              onClose={() => setPanelOpen(false)}
              name={name}
              status={status}
              manifest={manifest}
              splatUrl={splatUrl}
              numSplats={state.numSplats}
              graph={graph}
              measurements={measurements}
              selectedNode={selectedNode}
              autoLink={autoLink}
              onAutoLink={setAutoLink}
              onSelectNode={setSelectedNode}
              onFocusNode={(id) => {
                api.focusNode(id);
                focusViewer();
              }}
              onRenameNode={(id, v) =>
                updateGraph((g) => ({ ...g, nodes: g.nodes.map((n) => (n.id === id ? { ...n, name: v || undefined } : n)) }))
              }
              onKindNode={(id, kind: NavNodeKind) =>
                updateGraph((g) => ({ ...g, nodes: g.nodes.map((n) => (n.id === id ? { ...n, kind } : n)) }))
              }
              onDeleteNode={deleteNode}
              onToggleEdge={toggleEdge}
              onStartStop={() => pickTool("stop")}
              onStartMeasure={() => pickTool("measure")}
              onLabelMeasurement={(id, label) =>
                setMeasurements((list) => list.map((m) => (m.id === id ? { ...m, label: label || undefined } : m)))
              }
              onDeleteMeasurement={(id) => setMeasurements((list) => list.filter((m) => m.id !== id))}
              onClearMeasurements={() => setMeasurements([])}
            />
          </div>
        </div>
      )}

      {/* Bottom dock */}
      <div className="pointer-events-none absolute inset-x-3 bottom-3 flex items-end justify-between gap-2">
        <span className="hidden max-w-[28vw] rounded-lg border border-hairline bg-pure-white/90 px-2.5 py-1 text-caption text-void-black/70 md:block">
          {interactive ? hint : "\u00a0"}
        </span>

        <div className="pointer-events-auto flex items-center gap-1 rounded-xl border border-hairline bg-pure-white p-1">
          <div role="radiogroup" aria-label="Tool" className="flex items-center gap-0.5">
            {TOOLS.map((t) => (
              <button
                key={t.id}
                type="button"
                role="radio"
                aria-checked={state.tool === t.id}
                aria-keyshortcuts={t.key}
                title={`${t.label} (${t.key})`}
                disabled={!interactive}
                onClick={() => pickTool(t.id)}
                className={`inline-flex flex-col items-center gap-0.5 rounded-lg px-3 py-1.5 text-caption font-medium transition-colors duration-200 disabled:opacity-50 ${
                  state.tool === t.id ? "bg-sky-tint text-wander-blue" : "text-void-black/60 hover:bg-void-black/5 hover:text-void-black"
                }`}
              >
                <Icon name={t.icon} size={17} />
                {t.label}
              </button>
            ))}
          </div>
          <span aria-hidden="true" className="mx-1 h-8 w-px bg-hairline" />
          <button
            type="button"
            className="btn-primary self-center"
            disabled={!canSave || !dirty || saving}
            title={canSave ? "Save stops and measurements to the world" : "Add world.json to this world to enable saving"}
            onClick={save}
          >
            <Icon name="save" size={15} />
            {saving ? "Saving…" : "Save"}
          </button>
        </div>

        <span className="pill hidden bg-pure-white/90 text-void-black/80 md:inline-flex">
          {state.status === "ready" ? `${formatSplatCount(state.numSplats ?? manifest?.stats?.splatCount)} splats` : "—"}
          {manifest?.alignment && (
            <>
              <span aria-hidden="true" className="text-void-black/30">
                ·
              </span>
              {manifest.alignment.frame}
            </>
          )}
        </span>
      </div>

      {notice && (
        <div
          role="status"
          className={`pointer-events-none absolute bottom-24 left-1/2 -translate-x-1/2 rounded-lg border px-3 py-1.5 text-body-sm font-medium ${
            notice.tone === "ok"
              ? "border-transparent bg-sky-tint text-wander-blue"
              : "border-transparent bg-wander-pink text-pure-white"
          }`}
        >
          {notice.text}
        </div>
      )}

      <ViewerOverlay state={state} api={api} name={name} worldId={worldId} manifest={manifest} source={source} />
    </div>
  );
}

function ToolButton({
  icon,
  label,
  onClick,
  disabled,
  pressed,
}: {
  icon: IconName;
  label: string;
  onClick: () => void;
  disabled?: boolean;
  pressed?: boolean;
}) {
  return (
    <button
      type="button"
      aria-label={label}
      title={label}
      aria-pressed={pressed}
      disabled={disabled}
      onClick={onClick}
      className={`inline-flex size-7 items-center justify-center rounded-[6px] transition-colors duration-200 disabled:opacity-50 ${
        pressed ? "bg-sky-tint text-wander-blue" : "text-void-black/60 hover:text-void-black"
      }`}
    >
      <Icon name={icon} size={15} />
    </button>
  );
}

function hintFor(tool: ViewerTool, mode: ViewerMode, pending: boolean, linkFrom?: string): string {
  if (tool === "measure") return pending ? "Click the second point · Esc cancels" : "Click a point on the scan to start measuring";
  if (tool === "stop") return `Click the scan to drop a stop${linkFrom ? ` · links from “${linkFrom}”` : ""} · Esc to finish`;
  return mode === "walk"
    ? "Drag to look · W A S D to move · Q / E height · Shift to hurry"
    : "Drag to orbit · Scroll to zoom · Right-drag to pan · Click a stop to select it";
}

function nextId(g: NavigationGraph, prefix: string): string {
  const taken = new Set(g.nodes.map((n) => n.id));
  let i = g.nodes.length + 1;
  while (taken.has(`${prefix}-${i}`)) i++;
  return `${prefix}-${i}`;
}
