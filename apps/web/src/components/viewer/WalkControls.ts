import * as THREE from "three";

const UP = new THREE.Vector3(0, 1, 0);
const MAX_PITCH = Math.PI / 2 - 0.05;

const MOVE_KEYS: Record<string, [number, number, number]> = {
  KeyW: [0, 0, -1],
  ArrowUp: [0, 0, -1],
  KeyS: [0, 0, 1],
  ArrowDown: [0, 0, 1],
  KeyA: [-1, 0, 0],
  ArrowLeft: [-1, 0, 0],
  KeyD: [1, 0, 0],
  ArrowRight: [1, 0, 0],
  KeyE: [0, 1, 0],
  Space: [0, 1, 0],
  KeyQ: [0, -1, 0],
  KeyC: [0, -1, 0],
};

/**
 * First-person "walk the scan" controls: drag to look, WASD / arrows to move
 * on the horizontal plane, Q/E to change height, Shift to hurry. Keyboard
 * input is read from the focusable viewer element (not the document) so
 * typing elsewhere on the page never moves the camera. Everything is removed
 * again in `dispose()`.
 */
export class WalkControls {
  enabled = false;
  /** Metres per second — scans are metric. */
  moveSpeed = 1.6;
  sprintMultiplier = 3;
  /** Radians per CSS pixel of drag. */
  lookSpeed = 0.0022;

  private yaw = 0;
  private pitch = 0;
  private readonly keys = new Set<string>();
  private drag: { id: number; x: number; y: number } | null = null;
  private readonly move = new THREE.Vector3();
  private readonly tmp = new THREE.Vector3();
  private readonly forward = new THREE.Vector3();
  private readonly right = new THREE.Vector3();
  private readonly euler = new THREE.Euler(0, 0, 0, "YXZ");
  private readonly disposers: (() => void)[] = [];

  constructor(
    private readonly camera: THREE.PerspectiveCamera,
    private readonly element: HTMLElement,
  ) {
    this.syncFromCamera();
    this.listen(element, "pointerdown", this.onPointerDown);
    this.listen(element, "pointermove", this.onPointerMove);
    this.listen(element, "pointerup", this.onPointerUp);
    this.listen(element, "pointercancel", this.onPointerUp);
    this.listen(element, "keydown", this.onKeyDown);
    this.listen(element, "keyup", this.onKeyUp);
    this.listen(element, "blur", () => this.keys.clear());
  }

  /** Read yaw/pitch back from the camera after something else moved it. */
  syncFromCamera() {
    this.euler.setFromQuaternion(this.camera.quaternion, "YXZ");
    this.yaw = this.euler.y;
    this.pitch = THREE.MathUtils.clamp(this.euler.x, -MAX_PITCH, MAX_PITCH);
    this.applyRotation();
  }

  update(deltaSeconds: number) {
    if (!this.enabled || this.keys.size === 0) return;
    this.move.set(0, 0, 0);
    for (const code of this.keys) {
      const v = MOVE_KEYS[code];
      if (v) this.move.add(this.tmp.set(v[0], v[1], v[2]));
    }
    if (this.move.lengthSq() === 0) return;
    this.move.normalize();

    const sprint = this.keys.has("ShiftLeft") || this.keys.has("ShiftRight");
    const step = this.moveSpeed * (sprint ? this.sprintMultiplier : 1) * Math.min(deltaSeconds, 0.1);

    // Walk on the horizontal plane relative to where the camera faces.
    this.forward.set(0, 0, -1).applyQuaternion(this.camera.quaternion).setY(0);
    if (this.forward.lengthSq() < 1e-6) this.forward.set(0, 0, -1);
    this.forward.normalize();
    this.right.crossVectors(this.forward, UP).normalize();

    this.camera.position
      .addScaledVector(this.forward, -this.move.z * step)
      .addScaledVector(this.right, this.move.x * step)
      .addScaledVector(UP, this.move.y * step);
  }

  dispose() {
    for (const off of this.disposers) off();
    this.disposers.length = 0;
  }

  private applyRotation() {
    this.euler.set(this.pitch, this.yaw, 0, "YXZ");
    this.camera.quaternion.setFromEuler(this.euler);
  }

  private onPointerDown = (e: PointerEvent) => {
    if (!this.enabled || (e.pointerType === "mouse" && e.button !== 0)) return;
    this.drag = { id: e.pointerId, x: e.clientX, y: e.clientY };
    this.element.setPointerCapture(e.pointerId);
    this.element.focus({ preventScroll: true });
  };

  private onPointerMove = (e: PointerEvent) => {
    if (!this.enabled || !this.drag || e.pointerId !== this.drag.id) return;
    const dx = e.clientX - this.drag.x;
    const dy = e.clientY - this.drag.y;
    this.drag.x = e.clientX;
    this.drag.y = e.clientY;
    this.yaw -= dx * this.lookSpeed;
    this.pitch = THREE.MathUtils.clamp(this.pitch - dy * this.lookSpeed, -MAX_PITCH, MAX_PITCH);
    this.applyRotation();
  };

  private onPointerUp = (e: PointerEvent) => {
    if (this.drag?.id !== e.pointerId) return;
    this.drag = null;
    if (this.element.hasPointerCapture(e.pointerId)) this.element.releasePointerCapture(e.pointerId);
  };

  private onKeyDown = (e: KeyboardEvent) => {
    if (!this.enabled || e.metaKey || e.ctrlKey || e.altKey) return;
    if (e.code in MOVE_KEYS || e.code === "ShiftLeft" || e.code === "ShiftRight") {
      this.keys.add(e.code);
      e.preventDefault();
    }
  };

  private onKeyUp = (e: KeyboardEvent) => {
    this.keys.delete(e.code);
  };

  private listen<K extends keyof HTMLElementEventMap>(
    target: HTMLElement,
    type: K,
    handler: (ev: HTMLElementEventMap[K]) => void,
  ) {
    target.addEventListener(type, handler);
    this.disposers.push(() => target.removeEventListener(type, handler));
  }
}
