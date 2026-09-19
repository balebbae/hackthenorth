"use client";

import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { Alignment, Measurement, NavigationGraph, Vec3, WorldNote } from "@/lib/world-manifest";
import type {
  EngineEvent,
  LoadStatus,
  LocalizationMarker,
  MeshStatus,
  SplatViewerEngine,
  ViewerMode,
  ViewerSelection,
  ViewerTool,
} from "./SplatViewerEngine";

export type ViewerStatus = "booting" | "unsupported" | LoadStatus;

export type ViewerState = {
  status: ViewerStatus;
  error: string | null;
  progress: { loaded: number; total: number } | null;
  numSplats: number | null;
  mode: ViewerMode;
  tool: ViewerTool;
  showGraph: boolean;
  /** Collision-mesh layer (`assets.mesh`): load state and whether it is drawn. */
  mesh: { status: MeshStatus; triangles: number | null; error: string | null };
  showMesh: boolean;
};

export type ViewerApi = {
  setMode: (mode: ViewerMode) => void;
  setTool: (tool: ViewerTool) => void;
  setShowGraph: (visible: boolean) => void;
  setShowMesh: (visible: boolean) => void;
  resetView: () => void;
  focusNode: (id: string) => void;
  focusNote: (id: string) => void;
  /** Orbit the camera around the phone marker. */
  focusPhone: () => void;
  /** Walk mode with the camera placed exactly at the phone's pose. */
  viewFromPhone: () => void;
  retry: () => void;
};

/** Interaction events forwarded from the engine to whoever owns the data. */
export type PickHandler = (
  e:
    | { type: "pick"; tool: ViewerTool; point: Vec3; graphPoint: Vec3; surface: "mesh" | "splat" }
    | { type: "pick-node"; tool: ViewerTool; id: string }
    | { type: "pick-note"; tool: ViewerTool; id: string }
    | { type: "pick-miss"; tool: ViewerTool },
) => void;

type Options = {
  splatUrl: string | null;
  meshUrl?: string | null;
  meshFrame?: "world" | "splat";
  alignment?: Alignment;
  /** Data the engine renders; owned by the caller. */
  graph: NavigationGraph;
  /** Node ids and "from|to" edge keys to draw as rejected (pink). */
  graphFlags?: { nodes: Set<string>; edges: Set<string> };
  notes: WorldNote[];
  measurements: Measurement[];
  selection: ViewerSelection | null;
  pendingPoint: Vec3 | null;
  /** Phone marker for the selected VPS image query; null hides it. */
  localization: LocalizationMarker | null;
  /** Recent localized positions, newest first. */
  localizationTrail: Vec3[];
  followPhone: boolean;
  onPick: PickHandler;
};

const INITIAL: ViewerState = {
  status: "booting",
  error: null,
  progress: null,
  numSplats: null,
  mode: "orbit",
  tool: "navigate",
  showGraph: true,
  mesh: { status: "none", triangles: null, error: null },
  showMesh: false,
};

/**
 * Mounts a `SplatViewerEngine` into the returned container ref and keeps it in
 * sync with the caller's graph / notes / measurement / selection state.
 * Three.js and Spark are imported lazily inside the effect so the page still
 * server-renders and the ~3 MB renderer bundle only ships to browsers that
 * open a world.
 */
export function useSplatViewer({
  splatUrl,
  meshUrl = null,
  meshFrame = "world",
  alignment,
  graph,
  graphFlags,
  notes,
  measurements,
  selection,
  pendingPoint,
  localization,
  localizationTrail,
  followPhone,
  onPick,
}: Options) {
  const containerRef = useRef<HTMLDivElement>(null);
  const engineRef = useRef<SplatViewerEngine | null>(null);
  const [state, setState] = useState<ViewerState>(INITIAL);
  const [attempt, setAttempt] = useState(0);
  const [engineReady, setEngineReady] = useState(0);

  // Server props are plain data; key the effect on their content (not identity)
  // so a router refresh doesn't tear down the renderer and re-download the splat.
  const alignmentKey = useMemo(() => JSON.stringify(alignment ?? null), [alignment]);
  // Latest UI toggles / callbacks, read by the engine when it (re)mounts and by event handlers.
  const latest = useRef({ mode: INITIAL.mode, tool: INITIAL.tool, showGraph: INITIAL.showGraph, showMesh: INITIAL.showMesh, onPick });
  useEffect(() => {
    latest.current.onPick = onPick;
  }, [onPick]);

  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;
    let cancelled = false;
    let engine: SplatViewerEngine | null = null;
    const alignment = JSON.parse(alignmentKey) as Alignment | null;

    setState((s) => ({ ...s, status: "booting", error: null, progress: null, numSplats: null, mesh: INITIAL.mesh }));

    const onEvent = (e: EngineEvent) => {
      switch (e.type) {
        case "status":
          return setState((s) => ({ ...s, status: e.status, error: e.error ?? null }));
        case "progress":
          return setState((s) => ({ ...s, progress: { loaded: e.loaded, total: e.total } }));
        case "loaded":
          return setState((s) => ({ ...s, numSplats: e.numSplats }));
        case "mesh":
          return setState((s) => ({
            ...s,
            mesh: { status: e.status, triangles: e.triangles ?? null, error: e.error ?? null },
          }));
        default:
          return latest.current.onPick(e);
      }
    };

    import("./SplatViewerEngine")
      .then((mod) => {
        if (cancelled) return;
        if (!mod.supportsWebGL2()) {
          setState((s) => ({ ...s, status: "unsupported" }));
          return;
        }
        engine = new mod.SplatViewerEngine({
          container,
          splatUrl,
          meshUrl,
          meshFrame,
          alignment: alignment ?? undefined,
          onEvent,
        });
        engine.setMode(latest.current.mode);
        engine.setTool(latest.current.tool);
        engine.setShowGraph(latest.current.showGraph);
        engine.setShowMesh(latest.current.showMesh);
        engineRef.current = engine;
        setEngineReady((n) => n + 1); // re-run the data sync effects below
      })
      .catch((err: unknown) => {
        if (cancelled) return;
        setState((s) => ({
          ...s,
          status: "error",
          error: err instanceof Error ? err.message : "Failed to start the viewer.",
        }));
      });

    return () => {
      cancelled = true;
      engine?.dispose();
      engineRef.current = null;
    };
  }, [splatUrl, meshUrl, meshFrame, alignmentKey, attempt]);

  // Data → engine. Each is cheap to re-apply, so plain effects are enough.
  useEffect(() => {
    engineRef.current?.setGraph(graph, graphFlags);
  }, [graph, graphFlags, engineReady]);
  useEffect(() => {
    engineRef.current?.setNotes(notes);
  }, [notes, engineReady]);
  useEffect(() => {
    engineRef.current?.setSelection(selection);
  }, [selection, graph, notes, engineReady]);
  useEffect(() => {
    engineRef.current?.setMeasurements(measurements);
  }, [measurements, engineReady]);
  useEffect(() => {
    engineRef.current?.setPendingPoint(pendingPoint);
  }, [pendingPoint, engineReady]);
  useEffect(() => {
    engineRef.current?.setLocalization(localization);
  }, [localization, engineReady]);
  useEffect(() => {
    engineRef.current?.setLocalizationTrail(localizationTrail);
  }, [localizationTrail, engineReady]);
  useEffect(() => {
    engineRef.current?.setFollowPhone(followPhone);
  }, [followPhone, engineReady]);

  const api = useMemo<ViewerApi>(
    () => ({
      setMode: (mode) => {
        latest.current.mode = mode;
        engineRef.current?.setMode(mode);
        setState((s) => ({ ...s, mode }));
      },
      setTool: (tool) => {
        latest.current.tool = tool;
        engineRef.current?.setTool(tool);
        setState((s) => ({ ...s, tool }));
      },
      setShowGraph: (visible) => {
        latest.current.showGraph = visible;
        engineRef.current?.setShowGraph(visible);
        setState((s) => ({ ...s, showGraph: visible }));
      },
      setShowMesh: (visible) => {
        latest.current.showMesh = visible;
        engineRef.current?.setShowMesh(visible);
        setState((s) => ({ ...s, showMesh: visible }));
      },
      resetView: () => {
        latest.current.mode = "orbit";
        engineRef.current?.resetView();
        setState((s) => ({ ...s, mode: "orbit" }));
      },
      focusNode: (id) => engineRef.current?.focusNode(id),
      focusNote: (id) => engineRef.current?.focusNote(id),
      focusPhone: () => {
        latest.current.mode = "orbit";
        engineRef.current?.focusPhone();
        setState((s) => ({ ...s, mode: "orbit" }));
      },
      viewFromPhone: () => {
        latest.current.mode = "walk";
        engineRef.current?.viewFromPhone();
        setState((s) => ({ ...s, mode: "walk" }));
      },
      retry: () => setAttempt((n) => n + 1),
    }),
    [],
  );

  const focusViewer = useCallback(() => containerRef.current?.focus({ preventScroll: true }), []);

  return { containerRef, state, api, focusViewer };
}
