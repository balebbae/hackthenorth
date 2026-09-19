import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import { SparkRenderer, SplatMesh } from "@sparkjsdev/spark";
import type { Alignment, Measurement, NavigationGraph, NavNodeKind, Vec3 } from "@/lib/world-manifest";
import { WalkControls } from "./WalkControls";

export type ViewerMode = "orbit" | "walk";
export type ViewerTool = "navigate" | "measure" | "stop";
export type LoadStatus = "empty" | "loading" | "ready" | "error";

export type EngineEvent =
  | { type: "status"; status: LoadStatus; error?: string }
  | { type: "progress"; loaded: number; total: number }
  | { type: "loaded"; numSplats: number }
  /** A click landed on the splat. `point` is in world space, `graphPoint` in the graph's frame. */
  | { type: "pick"; tool: ViewerTool; point: Vec3; graphPoint: Vec3 }
  /** A click landed on an existing stop. */
  | { type: "pick-node"; tool: ViewerTool; id: string }
  /** A click hit nothing. */
  | { type: "pick-miss"; tool: ViewerTool };

export type EngineOptions = {
  /** Fills this element with the canvas; it is also the keyboard focus target for walk mode. */
  container: HTMLElement;
  splatUrl: string | null;
  alignment?: Alignment;
  onEvent: (event: EngineEvent) => void;
};

/* Wander palette, mirrored from globals.css. */
const NAVY = 0x1e293b;
const BLUE = 0x2e4885;
const PINK = 0xd85598;
const SKY = 0x60baf4;
const WHITE = 0xffffff;
const SLATE = 0x475569;

const NODE_RADIUS = 0.14;
const EDGE_RADIUS = 0.035;
const MEASURE_RADIUS = 0.05;
const MEASURE_LINE_RADIUS = 0.012;
const EYE_HEIGHT = 1.6;
const CLICK_MAX_PX = 5;
const CLICK_MAX_MS = 400;
const HOVER_THROTTLE_MS = 70;
const X_FLIP = new THREE.Quaternion().setFromAxisAngle(new THREE.Vector3(1, 0, 0), Math.PI);
const ORBIT_DIRECTION = new THREE.Vector3(0.65, 0.55, 0.85).normalize();
const UP = new THREE.Vector3(0, 1, 0);

const LABEL_CLASS =
  "absolute left-0 top-0 whitespace-nowrap rounded-full border border-hairline bg-pure-white/95 px-2 py-0.5 text-caption font-medium text-void-black will-change-transform";

export function supportsWebGL2(): boolean {
  try {
    const gl = document.createElement("canvas").getContext("webgl2");
    // Release the probe context right away; browsers cap live WebGL contexts.
    gl?.getExtension("WEBGL_lose_context")?.loseContext();
    return !!gl;
  } catch {
    return false;
  }
}

type Label = { el: HTMLDivElement; position: THREE.Vector3; offsetY: number; nodeId?: string };

/**
 * Owns the Three.js scene for one world: Spark splat rendering, orbit / walk
 * camera controls, picking for the measure and stop tools, the navigation
 * graph and measurement overlays, HTML labels, and camera framing. React owns
 * the data (graph, measurements, selection) and pushes it in through setters;
 * the engine reports user interaction back through `onEvent`.
 */
export class SplatViewerEngine {
  private readonly renderer: THREE.WebGLRenderer;
  private readonly scene = new THREE.Scene();
  private readonly camera: THREE.PerspectiveCamera;
  private readonly spark: SparkRenderer;
  /** Alignment (splat → world) is applied here; the SplatMesh is its child. */
  private readonly root = new THREE.Group();
  private readonly graphGroup = new THREE.Group();
  private readonly measureGroup = new THREE.Group();
  private readonly grid: THREE.GridHelper;
  private readonly orbit: OrbitControls;
  private readonly walk: WalkControls;
  private readonly raycaster = new THREE.Raycaster();
  private readonly resizeObserver: ResizeObserver;
  private readonly labelLayer: HTMLDivElement;
  private readonly labels: Label[] = [];
  private readonly disposers: (() => void)[] = [];

  private readonly sphereGeo = new THREE.SphereGeometry(1, 20, 14);
  private readonly nodeMaterials: Record<NavNodeKind, THREE.MeshBasicMaterial> = {
    waypoint: overlayMaterial(BLUE),
    entrance: overlayMaterial(SKY),
    destination: overlayMaterial(PINK),
  };
  private readonly edgeMaterial = overlayMaterial(BLUE);
  private readonly measureMaterial = overlayMaterial(SKY);
  private readonly pendingMaterial = overlayMaterial(WHITE);
  private readonly selectionRing: THREE.Mesh;
  private readonly hoverMarker: THREE.Mesh;
  private readonly previewLine: THREE.Mesh;

  private mesh: SplatMesh | null = null;
  private nodeMeshes = new Map<string, THREE.Mesh>();
  private nodePositions = new Map<string, THREE.Vector3>();
  private graphFrame: "world" | "splat" = "world";
  /** Robust (outlier-trimmed) bounds in splat-local space. */
  private localBounds: THREE.Box3 | null = null;
  private mode: ViewerMode = "orbit";
  private tool: ViewerTool = "navigate";
  private pendingPoint: THREE.Vector3 | null = null;
  private pointerDown: { x: number; y: number; t: number; id: number } | null = null;
  private lastHover = 0;
  private lastTime = 0;
  private disposed = false;

  constructor(private readonly opts: EngineOptions) {
    const { container } = opts;

    this.renderer = new THREE.WebGLRenderer({
      antialias: false, // per Spark guidance: MSAA costs a lot and does nothing for splats
      alpha: false,
      powerPreference: "high-performance",
    });
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    this.renderer.setClearColor(NAVY, 1);
    this.renderer.domElement.className = "block h-full w-full touch-none";
    container.appendChild(this.renderer.domElement);

    this.labelLayer = document.createElement("div");
    this.labelLayer.className = "pointer-events-none absolute inset-0 overflow-hidden";
    container.appendChild(this.labelLayer);

    this.camera = new THREE.PerspectiveCamera(60, 1, 0.05, 500);
    this.camera.position.set(4, 3, 6);

    this.spark = new SparkRenderer({ renderer: this.renderer });
    this.scene.add(this.spark, this.root, this.measureGroup);
    this.applyAlignment(opts.alignment);

    this.grid = new THREE.GridHelper(20, 20, SLATE, 0x334155);
    this.grid.visible = !opts.splatUrl;
    this.scene.add(this.grid);

    this.selectionRing = new THREE.Mesh(
      new THREE.TorusGeometry(NODE_RADIUS * 1.7, 0.02, 10, 40),
      overlayMaterial(WHITE),
    );
    this.selectionRing.rotation.x = Math.PI / 2;
    this.selectionRing.renderOrder = 1002;
    this.selectionRing.visible = false;
    this.scene.add(this.selectionRing);

    this.hoverMarker = new THREE.Mesh(this.sphereGeo, this.pendingMaterial);
    this.hoverMarker.scale.setScalar(MEASURE_RADIUS);
    this.hoverMarker.renderOrder = 1003;
    this.hoverMarker.visible = false;
    this.previewLine = new THREE.Mesh(new THREE.CylinderGeometry(1, 1, 1, 8, 1, true), this.pendingMaterial);
    this.previewLine.renderOrder = 1002;
    this.previewLine.visible = false;
    this.scene.add(this.hoverMarker, this.previewLine);

    this.orbit = new OrbitControls(this.camera, this.renderer.domElement);
    this.orbit.enableDamping = true;
    this.orbit.dampingFactor = 0.12;
    this.orbit.screenSpacePanning = true;
    this.orbit.maxPolarAngle = Math.PI; // splats can be viewed from below when the scan is flipped

    this.walk = new WalkControls(this.camera, container);

    this.resizeObserver = new ResizeObserver(() => this.resize());
    this.resizeObserver.observe(container);
    this.resize();

    const canvas = this.renderer.domElement;
    this.listen(canvas, "pointerdown", this.onPointerDown);
    this.listen(canvas, "pointerup", this.onPointerUp);
    this.listen(canvas, "pointermove", this.onPointerMove);
    this.listen(canvas, "pointerleave", () => this.setHover(null));

    if (opts.splatUrl) this.loadSplat(opts.splatUrl);
    else {
      this.frameBox(this.worldBounds());
      opts.onEvent({ type: "status", status: "empty" });
    }

    this.renderer.setAnimationLoop((time) => this.tick(time));
  }

  /* ---------------------------------------------------------------- public */

  setMode(mode: ViewerMode) {
    if (mode === this.mode) return;
    this.mode = mode;
    if (mode === "walk") {
      const bounds = this.worldBounds();
      if (!bounds.containsPoint(this.camera.position)) {
        // Drop in at eye height in the middle of the scan, facing the way the orbit view was looking.
        const c = bounds.getCenter(new THREE.Vector3());
        const eye = Math.min(bounds.min.y + EYE_HEIGHT, bounds.max.y);
        const forward = new THREE.Vector3(0, 0, -1).applyQuaternion(this.camera.quaternion).setY(0);
        if (forward.lengthSq() < 1e-6) forward.set(0, 0, -1);
        this.camera.position.set(c.x, eye, c.z);
        this.camera.lookAt(this.camera.position.clone().add(forward));
      }
      this.orbit.enabled = false;
      this.walk.syncFromCamera();
      this.walk.enabled = true;
      this.opts.container.focus({ preventScroll: true });
    } else {
      this.walk.enabled = false;
      // Put the orbit pivot a few metres ahead so the switch doesn't swing the camera.
      const ahead = new THREE.Vector3(0, 0, -1).applyQuaternion(this.camera.quaternion);
      this.orbit.target.copy(this.camera.position).addScaledVector(ahead, 3);
      this.orbit.enabled = true;
      this.orbit.update();
    }
  }

  setTool(tool: ViewerTool) {
    this.tool = tool;
    this.renderer.domElement.style.cursor = tool === "navigate" ? "" : "crosshair";
    if (tool !== "measure") this.setPendingPoint(null);
    this.setHover(null);
  }

  setShowGraph(visible: boolean) {
    this.graphGroup.visible = visible;
    for (const l of this.labels) if (l.el.dataset.kind === "node") l.el.hidden = !visible;
    if (!visible) this.selectionRing.visible = false;
  }

  /** Replace the rendered navigation graph. Cheap: graphs are tens of nodes. */
  setGraph(graph: NavigationGraph) {
    const frame = graph.frame ?? "world";
    if (frame !== this.graphFrame || !this.graphGroup.parent) {
      this.graphGroup.removeFromParent();
      (frame === "splat" ? this.root : this.scene).add(this.graphGroup);
      this.graphFrame = frame;
    }
    this.clearGroup(this.graphGroup);
    this.removeLabels("node");
    this.nodeMeshes = new Map();
    this.nodePositions = new Map();

    for (const node of graph.nodes) {
      const p = new THREE.Vector3(...node.position);
      this.nodePositions.set(node.id, p);
      const m = new THREE.Mesh(this.sphereGeo, this.nodeMaterials[node.kind ?? "waypoint"]);
      m.scale.setScalar(NODE_RADIUS);
      m.position.copy(p);
      m.renderOrder = 1001;
      m.userData.nodeId = node.id;
      this.graphGroup.add(m);
      this.nodeMeshes.set(node.id, m);
      this.addLabel("node", node.name ?? node.id, this.graphGroup.localToWorld(p.clone()), NODE_RADIUS * 2.2, node.id);
    }
    for (const edge of graph.edges) {
      const a = this.nodePositions.get(edge.from);
      const b = this.nodePositions.get(edge.to);
      if (a && b) this.graphGroup.add(this.tube(a, b, EDGE_RADIUS, this.edgeMaterial, 1000));
    }
    if (this.mesh === null && graph.nodes.length) {
      this.grid.position.y = new THREE.Box3().setFromPoints([...this.nodePositions.values()]).min.y - 0.01;
    }
  }

  setSelectedNode(id: string | null) {
    const p = id ? this.nodePositions.get(id) : undefined;
    if (!p || !this.graphGroup.visible) {
      this.selectionRing.visible = false;
      return;
    }
    this.graphGroup.updateMatrixWorld(true);
    this.selectionRing.position.copy(this.graphGroup.localToWorld(p.clone()));
    this.selectionRing.visible = true;
  }

  /** Replace the rendered measurements (world frame). */
  setMeasurements(list: Measurement[]) {
    this.clearGroup(this.measureGroup);
    this.removeLabels("measure");
    for (const m of list) {
      const a = new THREE.Vector3(...m.points[0]);
      const b = new THREE.Vector3(...m.points[1]);
      for (const p of [a, b]) {
        const s = new THREE.Mesh(this.sphereGeo, this.measureMaterial);
        s.scale.setScalar(MEASURE_RADIUS);
        s.position.copy(p);
        s.renderOrder = 1001;
        this.measureGroup.add(s);
      }
      this.measureGroup.add(this.tube(a, b, MEASURE_LINE_RADIUS, this.measureMaterial, 1000));
      const mid = a.clone().add(b).multiplyScalar(0.5);
      this.addLabel("measure", `${m.label ? `${m.label} · ` : ""}${formatMetres(a.distanceTo(b))}`, mid, 0.08);
    }
  }

  /** First point of an in-progress measurement (world frame), or null to cancel. */
  setPendingPoint(point: Vec3 | null) {
    this.pendingPoint = point ? new THREE.Vector3(...point) : null;
    this.removeLabels("pending");
    if (this.pendingPoint) {
      const s = new THREE.Mesh(this.sphereGeo, this.pendingMaterial);
      s.scale.setScalar(MEASURE_RADIUS);
      s.position.copy(this.pendingPoint);
      s.renderOrder = 1003;
      s.userData.pending = true;
      this.measureGroup.add(s);
    } else {
      for (const child of [...this.measureGroup.children]) if (child.userData.pending) this.measureGroup.remove(child);
      this.previewLine.visible = false;
    }
  }

  /** Frame the whole scan from an elevated three-quarter angle (orbit mode). */
  resetView() {
    if (this.mode === "walk") this.setMode("orbit");
    this.frameBox(this.worldBounds());
  }

  /** Move the camera to look at a navigation node. */
  focusNode(id: string) {
    const local = this.nodePositions.get(id);
    if (!local) return;
    this.graphGroup.updateMatrixWorld(true);
    const target = this.graphGroup.localToWorld(local.clone());

    if (this.mode === "walk") {
      this.camera.position.set(target.x, target.y + EYE_HEIGHT - 0.2, target.z);
      this.walk.syncFromCamera();
      return;
    }
    const offset = this.camera.position.clone().sub(this.orbit.target);
    if (offset.lengthSq() < 1e-4) offset.copy(ORBIT_DIRECTION);
    offset.setLength(4);
    this.orbit.target.copy(target);
    this.camera.position.copy(target).add(offset);
    this.orbit.update();
  }

  /** Rotate the scan 180° about X for exports that arrive upside down. */
  flipUp() {
    this.root.quaternion.premultiply(X_FLIP);
    this.root.updateMatrixWorld(true);
    this.refreshLabelPositions();
    this.resetView();
  }

  dispose() {
    if (this.disposed) return;
    this.disposed = true;
    this.renderer.setAnimationLoop(null);
    this.resizeObserver.disconnect();
    for (const off of this.disposers) off();
    this.orbit.dispose();
    this.walk.dispose();
    this.mesh?.dispose();
    this.spark.dispose();
    this.clearGroup(this.graphGroup);
    this.clearGroup(this.measureGroup);
    for (const m of [...Object.values(this.nodeMaterials), this.edgeMaterial, this.measureMaterial, this.pendingMaterial])
      m.dispose();
    this.sphereGeo.dispose();
    this.selectionRing.geometry.dispose();
    (this.selectionRing.material as THREE.Material).dispose();
    this.previewLine.geometry.dispose();
    this.grid.geometry.dispose();
    (this.grid.material as THREE.Material).dispose();
    this.renderer.dispose();
    this.renderer.forceContextLoss();
    this.renderer.domElement.remove();
    this.labelLayer.remove();
  }

  /* --------------------------------------------------------------- picking */

  private onPointerDown = (e: PointerEvent) => {
    if (e.pointerType === "mouse" && e.button !== 0) return;
    this.pointerDown = { x: e.clientX, y: e.clientY, t: performance.now(), id: e.pointerId };
  };

  private onPointerUp = (e: PointerEvent) => {
    const d = this.pointerDown;
    this.pointerDown = null;
    if (!d || d.id !== e.pointerId) return;
    const moved = Math.hypot(e.clientX - d.x, e.clientY - d.y);
    if (moved > CLICK_MAX_PX || performance.now() - d.t > CLICK_MAX_MS) return;
    this.pick(e);
  };

  private onPointerMove = (e: PointerEvent) => {
    if (this.tool === "navigate" || this.pointerDown) return;
    const now = performance.now();
    if (now - this.lastHover < HOVER_THROTTLE_MS) return;
    this.lastHover = now;
    this.setHover(this.intersectSplat(e)?.point ?? null);
  };

  private pick(e: PointerEvent) {
    const { onEvent } = this.opts;
    this.setRayFromEvent(e);

    // Existing stops take priority so they can be selected in any tool.
    if (this.graphGroup.visible && this.nodeMeshes.size) {
      const hit = this.raycaster.intersectObjects([...this.nodeMeshes.values()], false)[0];
      if (hit) return onEvent({ type: "pick-node", tool: this.tool, id: hit.object.userData.nodeId as string });
    }
    if (this.tool === "navigate") return;

    const hit = this.intersectSplat();
    if (!hit) return onEvent({ type: "pick-miss", tool: this.tool });
    this.graphGroup.updateMatrixWorld(true);
    const graphPoint = this.graphGroup.worldToLocal(hit.point.clone());
    onEvent({ type: "pick", tool: this.tool, point: hit.point.toArray() as Vec3, graphPoint: graphPoint.toArray() as Vec3 });
  }

  private setRayFromEvent(e: PointerEvent) {
    const rect = this.renderer.domElement.getBoundingClientRect();
    const ndc = new THREE.Vector2(
      ((e.clientX - rect.left) / rect.width) * 2 - 1,
      -((e.clientY - rect.top) / rect.height) * 2 + 1,
    );
    this.raycaster.setFromCamera(ndc, this.camera);
  }

  private intersectSplat(e?: PointerEvent): THREE.Intersection | null {
    if (!this.mesh?.isInitialized) return null;
    if (e) this.setRayFromEvent(e);
    const hits: THREE.Intersection[] = [];
    this.mesh.raycast(this.raycaster, hits);
    hits.sort((a, b) => a.distance - b.distance);
    return hits[0] ?? null;
  }

  private setHover(point: THREE.Vector3 | null) {
    if (!point) {
      this.hoverMarker.visible = false;
      this.previewLine.visible = false;
      return;
    }
    this.hoverMarker.position.copy(point);
    this.hoverMarker.visible = true;
    if (this.tool === "measure" && this.pendingPoint) {
      this.placeTube(this.previewLine, this.pendingPoint, point, MEASURE_LINE_RADIUS);
      this.previewLine.visible = true;
    } else this.previewLine.visible = false;
  }

  /* -------------------------------------------------------------- internal */

  private loadSplat(url: string) {
    const { onEvent } = this.opts;
    onEvent({ type: "status", status: "loading" });

    const mesh = new SplatMesh({
      url,
      onProgress: (e) =>
        onEvent({ type: "progress", loaded: e.loaded, total: e.lengthComputable ? e.total : 0 }),
    });
    this.mesh = mesh;
    this.root.add(mesh);

    mesh.initialized
      .then((m) => {
        if (this.disposed) return;
        this.localBounds = robustBounds(m);
        this.resetView();
        onEvent({ type: "loaded", numSplats: m.numSplats });
        onEvent({ type: "status", status: "ready" });
      })
      .catch((err: unknown) => {
        if (this.disposed) return;
        onEvent({ type: "status", status: "error", error: describeError(err) });
      });
  }

  private applyAlignment(a: Alignment | undefined) {
    if (!a) return;
    this.root.position.set(a.position[0], a.position[1], a.position[2]);
    this.root.quaternion.set(a.rotation[0], a.rotation[1], a.rotation[2], a.rotation[3]).normalize();
    this.root.scale.setScalar(a.scale);
    this.root.updateMatrixWorld(true);
  }

  private tube(a: THREE.Vector3, b: THREE.Vector3, radius: number, material: THREE.Material, renderOrder: number) {
    const m = new THREE.Mesh(new THREE.CylinderGeometry(1, 1, 1, 10, 1, true), material);
    this.placeTube(m, a, b, radius);
    m.renderOrder = renderOrder;
    return m;
  }

  /** Stretch a unit cylinder between two points. */
  private placeTube(m: THREE.Mesh, a: THREE.Vector3, b: THREE.Vector3, radius: number) {
    const length = Math.max(a.distanceTo(b), 1e-4);
    m.position.copy(a).add(b).multiplyScalar(0.5);
    m.scale.set(radius, length, radius);
    m.quaternion.setFromUnitVectors(UP, b.clone().sub(a).normalize());
  }

  private clearGroup(group: THREE.Group) {
    for (const child of [...group.children]) {
      group.remove(child);
      const geo = (child as THREE.Mesh).geometry;
      if (geo && geo !== this.sphereGeo) geo.dispose();
    }
  }

  private addLabel(
    kind: "node" | "measure" | "pending",
    text: string,
    position: THREE.Vector3,
    offsetY: number,
    nodeId?: string,
  ) {
    const el = document.createElement("div");
    el.className = LABEL_CLASS;
    el.dataset.kind = kind;
    el.textContent = text;
    el.hidden = kind === "node" && !this.graphGroup.visible;
    this.labelLayer.appendChild(el);
    this.labels.push({ el, position: position.clone(), offsetY, nodeId });
  }

  private removeLabels(kind: string) {
    for (let i = this.labels.length - 1; i >= 0; i--) {
      if (this.labels[i].el.dataset.kind === kind) {
        this.labels[i].el.remove();
        this.labels.splice(i, 1);
      }
    }
  }

  /** After the root transform changes, node labels (stored in world space) must be recomputed. */
  private refreshLabelPositions() {
    if (this.graphFrame !== "splat") return;
    this.graphGroup.updateMatrixWorld(true);
    for (const l of this.labels) {
      const p = l.nodeId ? this.nodePositions.get(l.nodeId) : undefined;
      if (p) l.position.copy(this.graphGroup.localToWorld(p.clone()));
    }
  }

  private updateLabels() {
    const w = this.labelLayer.clientWidth;
    const h = this.labelLayer.clientHeight;
    const v = new THREE.Vector3();
    for (const l of this.labels) {
      if (l.el.hidden) continue;
      v.copy(l.position).addScaledVector(UP, l.offsetY).project(this.camera);
      const visible = v.z > -1 && v.z < 1 && Math.abs(v.x) < 1.2 && Math.abs(v.y) < 1.2;
      l.el.style.visibility = visible ? "visible" : "hidden";
      if (!visible) continue;
      const x = ((v.x + 1) / 2) * w;
      const y = ((1 - v.y) / 2) * h;
      l.el.style.transform = `translate(${x.toFixed(1)}px, ${y.toFixed(1)}px) translate(-50%, -100%)`;
    }
  }

  private frameBox(bounds: THREE.Box3) {
    const center = bounds.getCenter(new THREE.Vector3());
    const radius = Math.max(bounds.getSize(new THREE.Vector3()).length() / 2, 0.5);
    const distance = (radius / Math.sin(THREE.MathUtils.degToRad(this.camera.fov / 2))) * 1.05;

    this.camera.position.copy(center).addScaledVector(ORBIT_DIRECTION, distance);
    this.camera.near = Math.max(0.02, distance / 1000);
    this.camera.far = Math.max(200, distance * 40);
    this.camera.updateProjectionMatrix();
    this.orbit.target.copy(center);
    this.orbit.update();
  }

  /** Robust bounds transformed into world space (falls back to the graph / a default box). */
  private worldBounds(): THREE.Box3 {
    if (this.localBounds && this.mesh) {
      this.mesh.updateMatrixWorld(true);
      return this.localBounds.clone().applyMatrix4(this.mesh.matrixWorld);
    }
    const points = [...this.nodePositions.values()];
    if (points.length) {
      this.graphGroup.updateMatrixWorld(true);
      return new THREE.Box3()
        .setFromPoints(points.map((p) => this.graphGroup.localToWorld(p.clone())))
        .expandByScalar(2);
    }
    return new THREE.Box3(new THREE.Vector3(-4, 0, -4), new THREE.Vector3(4, 2.5, 4));
  }

  private resize() {
    const { clientWidth: w, clientHeight: h } = this.opts.container;
    if (w === 0 || h === 0) return;
    this.renderer.setSize(w, h, false);
    this.camera.aspect = w / h;
    this.camera.updateProjectionMatrix();
  }

  private tick(time: number) {
    const dt = this.lastTime ? (time - this.lastTime) / 1000 : 0;
    this.lastTime = time;
    if (this.mode === "orbit") this.orbit.update();
    else this.walk.update(dt);
    this.renderer.render(this.scene, this.camera);
    this.updateLabels();
  }

  private listen<K extends keyof HTMLElementEventMap>(
    target: HTMLElement,
    type: K,
    handler: (ev: HTMLElementEventMap[K]) => void,
  ) {
    target.addEventListener(type, handler);
    this.disposers.push(() => target.removeEventListener(type, handler));
  }
}

/** Flat, always-on-top material so overlays read as UI through the splats. */
function overlayMaterial(color: number): THREE.MeshBasicMaterial {
  return new THREE.MeshBasicMaterial({
    color,
    transparent: true,
    opacity: 0.95,
    depthTest: false,
    depthWrite: false,
  });
}

export function formatMetres(m: number): string {
  if (m < 1) return `${Math.round(m * 100)} cm`;
  return `${m.toFixed(m < 10 ? 2 : 1)} m`;
}

/**
 * Bounding box from the 3rd–97th percentile of splat centres. Trained splats
 * usually include a halo of far-away floaters that would otherwise make the
 * framed view tiny, so the raw `getBoundingBox()` is not usable for framing.
 */
function robustBounds(mesh: SplatMesh): THREE.Box3 {
  const n = mesh.numSplats;
  if (n === 0) return new THREE.Box3(new THREE.Vector3(-1, -1, -1), new THREE.Vector3(1, 1, 1));

  const stride = Math.max(1, Math.floor(n / 120_000));
  const xs: number[] = [];
  const ys: number[] = [];
  const zs: number[] = [];
  mesh.forEachSplat((i, center) => {
    if (i % stride) return;
    xs.push(center.x);
    ys.push(center.y);
    zs.push(center.z);
  });
  if (xs.length < 8) return mesh.getBoundingBox();

  const pct = (arr: number[], p: number) => {
    arr.sort((a, b) => a - b);
    return arr[Math.round(p * (arr.length - 1))];
  };
  const box = new THREE.Box3(
    new THREE.Vector3(pct(xs, 0.03), pct(ys, 0.03), pct(zs, 0.03)),
    new THREE.Vector3(pct(xs, 0.97), pct(ys, 0.97), pct(zs, 0.97)),
  );
  // Guard against degenerate boxes (e.g. a perfectly flat scan).
  const size = box.getSize(new THREE.Vector3());
  if (size.x < 0.1) box.expandByVector(new THREE.Vector3(0.5, 0, 0));
  if (size.y < 0.1) box.expandByVector(new THREE.Vector3(0, 0.5, 0));
  if (size.z < 0.1) box.expandByVector(new THREE.Vector3(0, 0, 0.5));
  return box;
}

function describeError(err: unknown): string {
  const msg = err instanceof Error ? err.message : String(err);
  if (/404|not found/i.test(msg)) return "The splat file was not found on the volume.";
  if (/network|fetch|failed to load/i.test(msg)) return "Could not download the splat. Check the worlds API and try again.";
  return msg || "Failed to load the splat.";
}
