"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { Icon, type IconName } from "@/components/Icon";
import { LogoMark } from "@/components/Logo";
import { UploadSplatDialog } from "@/components/worlds/UploadSplatDialog";
import {
  EMPTY_GRAPH,
  formatSplatCount,
  type Measurement,
  type NavigationGraph,
  type Vec3,
  type WorldManifest,
  type WorldNote,
} from "@/lib/world-manifest";
import { STATUS_META, type WorldStatus } from "@/lib/worlds";
import { InspectorPanel, type PanelTab } from "./InspectorPanel";
import type { ViewerMode, ViewerSelection, ViewerTool } from "./SplatViewerEngine";
import { useSplatViewer, type PickHandler } from "./useSplatViewer";
import { ViewerOverlay } from "./ViewerOverlays";

type Props = {
  worldId: string;
  name: string;
  status: WorldStatus;
  manifest: WorldManifest | null;
  /** Same-origin URL of the splat (via /api/worlds), or null when nothing is uploaded yet. */
  splatUrl: string | null;
  initialNotes: WorldNote[];
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
  { id: "note", label: "Add note", icon: "pin", key: "3" },
];

const AUTOSAVE_MS = 900;

type SaveState = { status: "clean" | "dirty" | "saving" | "saved" | "error"; error?: string };

const isEditing = () => {
  const el = document.activeElement;
  return el instanceof HTMLInputElement || el instanceof HTMLTextAreaElement || el instanceof HTMLSelectElement;
};

/**
 * Full-viewport world editor: the splat canvas fills the page; a floating
 * header, a bottom tool dock and a collapsible inspector sit on top. Notes and
 * measurements live here, are pushed into the engine via the hook, and
 * autosave to the world through /api/worlds.
 */
export function WorldViewer({
  worldId,
  name,
  status,
  manifest,
  splatUrl,
  initialNotes,
  initialMeasurements,
  source,
}: Props) {
  /* ------------------------------------------------------------ edit state */
  const graph = useMemo<NavigationGraph>(() => manifest?.navigationGraph ?? EMPTY_GRAPH, [manifest]);
  const [notes, setNotes] = useState(initialNotes);
  const [measurements, setMeasurements] = useState(initialMeasurements);
  const [selection, setSelection] = useState<ViewerSelection | null>(null);
  const [pendingPoint, setPendingPoint] = useState<Vec3 | null>(null);

  const [panelOpen, setPanelOpen] = useState(true);
  const [panelTab, setPanelTab] = useState<PanelTab>("notes");
  const [notice, setNotice] = useState<{ tone: "ok" | "error"; text: string } | null>(null);
  const [uploadOpen, setUploadOpen] = useState(false);
  const router = useRouter();

  const canSave = !!manifest;

  /* -------------------------------------------------------------- autosave */
  const notesSave = useAutosave(`/api/worlds/${encodeURIComponent(worldId)}/notes`, { notes }, notes, canSave);
  const measureSave = useAutosave(
    `/api/worlds/${encodeURIComponent(worldId)}/measurements`,
    { measurements },
    measurements,
    canSave,
  );
  const save = combineSave(notesSave.state, measureSave.state);
  const dirty = save.status !== "clean" && save.status !== "saved";

  /* ------------------------------------------------------------ mutations */
  const addNote = useCallback((position: Vec3) => {
    const id = `note-${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 6)}`;
    setNotes((list) => [
      ...list,
      { id, title: `Note ${list.length + 1}`, position, createdAt: new Date().toISOString() },
    ]);
    setSelection({ kind: "note", id });
    setPanelOpen(true);
    setPanelTab("notes");
  }, []);

  const updateNote = useCallback(
    (id: string, patch: Partial<Pick<WorldNote, "title" | "location" | "description">>) =>
      setNotes((list) =>
        list.map((n) => {
          if (n.id !== id) return n;
          const next = { ...n, ...patch };
          const changed = (["title", "location", "description"] as const).some((k) => next[k] !== n[k]);
          return changed ? { ...next, updatedAt: new Date().toISOString() } : n;
        }),
      ),
    [],
  );

  const deleteNote = useCallback((id: string) => {
    setNotes((list) => list.filter((n) => n.id !== id));
    setSelection((s) => (s?.kind === "note" && s.id === id ? null : s));
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
      if (e.type === "pick-note") {
        setSelection((s) => (s?.kind === "note" && s.id === e.id && e.tool === "navigate" ? null : { kind: "note", id: e.id }));
        setPanelOpen(true);
        setPanelTab("notes");
        return;
      }
      if (e.type === "pick-node") {
        setSelection((s) => (s?.kind === "node" && s.id === e.id ? null : { kind: "node", id: e.id }));
        setPanelTab("details");
        return;
      }
      if (e.type === "pick-miss") {
        if (e.tool === "navigate") setSelection(null);
        else setNotice({ tone: "error", text: "Click on the scan itself — that spot has no splats." });
        return;
      }
      if (e.tool === "note") addNote(e.point);
      else if (e.tool === "measure") {
        if (pendingPoint) {
          addMeasurement(pendingPoint, e.point);
          setPendingPoint(null);
        } else setPendingPoint(e.point);
      }
    },
    [addNote, addMeasurement, pendingPoint],
  );

  const { containerRef, state, api, focusViewer } = useSplatViewer({
    splatUrl,
    alignment: manifest?.alignment,
    graph,
    notes,
    measurements,
    selection,
    pendingPoint,
    onPick,
  });

  const pickTool = useCallback(
    (tool: ViewerTool) => {
      api.setTool(tool);
      if (tool !== "measure") setPendingPoint(null);
      if (tool === "note") setPanelTab("notes");
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
        else if (selection) setSelection(null);
        else if (state.tool !== "navigate") pickTool("navigate");
        return;
      }
      if ((e.key === "Delete" || e.key === "Backspace") && selection?.kind === "note") {
        e.preventDefault();
        deleteNote(selection.id);
        return;
      }
      const tool = TOOLS.find((t) => t.key === e.key);
      if (tool) pickTool(tool.id);
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [pendingPoint, selection, state.tool, pickTool, deleteNote]);

  useEffect(() => {
    if (!notice) return;
    const t = setTimeout(() => setNotice(null), notice.tone === "ok" ? 2500 : 4000);
    return () => clearTimeout(t);
  }, [notice]);

  // Warn before leaving while a save is still pending.
  useEffect(() => {
    if (!dirty) return;
    const onLeave = (e: BeforeUnloadEvent) => e.preventDefault();
    window.addEventListener("beforeunload", onLeave);
    return () => window.removeEventListener("beforeunload", onLeave);
  }, [dirty]);

  /* ---------------------------------------------------------------- render */
  const interactive = state.status === "ready" || state.status === "empty";
  const meta = STATUS_META[status];
  const hint = hintFor(state.tool, state.mode, !!pendingPoint);

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
          <SaveBadge
            save={save}
            canSave={canSave}
            onRetry={() => {
              notesSave.retry();
              measureSave.retry();
            }}
          />
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
            {graph.nodes.length > 0 && (
              <ToolButton
                icon="route"
                label={state.showGraph ? "Hide waypoints" : "Show waypoints"}
                pressed={state.showGraph}
                disabled={!interactive}
                onClick={() => api.setShowGraph(!state.showGraph)}
              />
            )}
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
              notes={notes}
              measurements={measurements}
              selection={selection}
              onSelect={setSelection}
              onFocusNode={(id) => {
                api.focusNode(id);
                focusViewer();
              }}
              onFocusNote={(id) => {
                api.focusNote(id);
                focusViewer();
              }}
              onUpdateNote={updateNote}
              onDeleteNote={deleteNote}
              onStartNote={() => pickTool("note")}
              onStartMeasure={() => pickTool("measure")}
              onLabelMeasurement={(id, label) =>
                setMeasurements((list) => list.map((m) => (m.id === id ? { ...m, label: label || undefined } : m)))
              }
              onDeleteMeasurement={(id) => setMeasurements((list) => list.filter((m) => m.id !== id))}
              onClearMeasurements={() => setMeasurements([])}
              onUploadSplat={manifest ? () => setUploadOpen(true) : undefined}
            />
          </div>
        </div>
      )}

      {/* Bottom bar: hint pinned left, stats pinned right, tool dock truly centred regardless of their widths */}
      <div className="pointer-events-none absolute inset-x-3 bottom-3 flex items-end justify-between gap-2">
        <span className="hidden max-w-[26vw] rounded-lg border border-hairline bg-pure-white/90 px-2.5 py-1 text-caption text-void-black/70 md:block">
          {interactive ? hint : "\u00a0"}
        </span>

        <div className="pointer-events-auto absolute bottom-0 left-1/2 flex -translate-x-1/2 items-center gap-1 rounded-xl border border-hairline bg-pure-white p-1">
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

      <ViewerOverlay
        state={state}
        api={api}
        name={name}
        worldId={worldId}
        manifest={manifest}
        source={source}
        onUpload={manifest ? () => setUploadOpen(true) : undefined}
      />

      {manifest && (
        <UploadSplatDialog
          open={uploadOpen}
          mode={{ kind: "existing", manifest }}
          onClose={() => setUploadOpen(false)}
          onDone={() => {
            setNotice({ tone: "ok", text: "Splat uploaded — reloading the scene" });
            router.refresh(); // re-reads the manifest; the new splatUrl remounts the engine
          }}
        />
      )}
    </div>
  );
}

/* ---------------------------------------------------------------- pieces */

function SaveBadge({ save, canSave, onRetry }: { save: SaveState; canSave: boolean; onRetry: () => void }) {
  if (!canSave)
    return (
      <span className="pill-sm bg-stellar-white text-void-black/60" title="Add world.json to this world to persist notes">
        Not saved · no world.json
      </span>
    );
  switch (save.status) {
    case "dirty":
    case "saving":
      return <span className="pill-sm bg-pink-tint text-wander-pink">Saving…</span>;
    case "saved":
      return (
        <span className="pill-sm bg-sky-tint text-wander-blue">
          <Icon name="check" size={11} />
          Saved
        </span>
      );
    case "error":
      return (
        <button type="button" onClick={onRetry} className="pill-sm bg-wander-pink text-pure-white" title={save.error}>
          Save failed · retry
        </button>
      );
    default:
      return null;
  }
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

const MOVE_HINT = "W A S D move · Q / E height · Arrows turn · Shift hurry";

function hintFor(tool: ViewerTool, mode: ViewerMode, pending: boolean): string {
  if (tool === "measure") return pending ? "Click the second point · Esc cancels" : "Click a point on the scan to start measuring";
  if (tool === "note") return "Click the scan to pin a note · Esc to finish";
  return mode === "walk" ? `Drag to look · ${MOVE_HINT}` : `Drag to orbit · Scroll to zoom · ${MOVE_HINT}`;
}

/* -------------------------------------------------------------- autosave */

/**
 * PUTs `body` to `url` shortly after `value` changes (debounced). Reports a
 * small state machine for the header badge; `retry()` re-sends after an error.
 */
function useAutosave<T>(url: string, body: unknown, value: T, enabled: boolean) {
  const [state, setState] = useState<SaveState>({ status: "clean" });
  const saved = useRef(value);
  const [attempt, setAttempt] = useState(0);
  const bodyRef = useRef(body);
  useEffect(() => {
    bodyRef.current = body;
  }, [body]);

  useEffect(() => {
    if (!enabled || value === saved.current) return;
    setState({ status: "dirty" });
    let cancelled = false;
    const t = setTimeout(async () => {
      setState({ status: "saving" });
      try {
        const res = await fetch(url, {
          method: "PUT",
          headers: { "content-type": "application/json" },
          body: JSON.stringify(bodyRef.current),
        });
        if (!res.ok) throw new Error((await res.json().catch(() => null))?.error ?? `Save failed (${res.status})`);
        if (cancelled) return;
        saved.current = value;
        setState({ status: "saved" });
      } catch (err) {
        if (!cancelled) setState({ status: "error", error: err instanceof Error ? err.message : "Save failed" });
      }
    }, AUTOSAVE_MS);
    return () => {
      cancelled = true;
      clearTimeout(t);
    };
  }, [url, value, enabled, attempt]);

  return { state, retry: () => setAttempt((n) => n + 1) };
}

function combineSave(a: SaveState, b: SaveState): SaveState {
  const order: SaveState["status"][] = ["error", "saving", "dirty", "saved", "clean"];
  for (const s of order) {
    if (a.status === s) return a;
    if (b.status === s) return b;
  }
  return a;
}
