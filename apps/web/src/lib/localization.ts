/**
 * VPS image queries mirrored from the phone — the TypeScript side of
 * `localizationQuery*` in `shared/contracts/navigation.schema.json`.
 *
 * The Niantic SDK sends camera frames to VPS itself; the phone reports each
 * request it saw (`Vps2LocalizationRequestRecord`) with the JPEG it sent and the
 * camera pose at capture time in the site frame. The backend keeps the newest
 * 50 per world under `worlds/<id>/localizations/`; the viewer polls them to
 * draw the phone on the splat next to the image it sent.
 */
import { assetUrl, type Quat, type Vec3 } from "./world-manifest";

export const LOCALIZATION_QUERY_SCHEMA = "wander.localization-query/v1";
export const LOCALIZATIONS_SCHEMA = "wander.localizations/v1";

export type Pose = { position: Vec3; rotation: Quat };

export type TrackingState = "localized" | "limited" | "lost";
export type AnchorState = "tracked" | "limited" | "notTracked";
export type QueryStatus = "completed" | "failed" | "frameRejected" | "pending" | "unknown";
export type QueryRequestType =
  | "vpsLocalize"
  | "universalLocalize"
  | "getGraph"
  | "getReplacedNodes"
  | "registerNode"
  | "unknown";

export type LocalizationQueryRequest = {
  identifier: string;
  frameId?: number;
  type: QueryRequestType;
  status: QueryStatus;
  /** `Vps2LocalizationError` case name; "none" on success. */
  error?: string;
  startedAt: string;
  endedAt?: string;
  latencyMs?: number;
  frameMatch?: "exact" | "nearest" | "fallback";
};

export type LocalizationQueryResult = {
  trackingState: TrackingState;
  anchorState?: AnchorState;
  confidence?: number;
  /** Camera pose when the query frame was captured (site frame). */
  pose?: Pose;
  /** Where the phone was when the result came back, if it had moved. */
  currentPose?: Pose;
};

export type LocalizationQueryImage = {
  /** Volume path of the JPEG, e.g. worlds/<id>/localizations/<queryId>.jpg. */
  path?: string;
  width: number;
  height: number;
  /** portrait: image up = camera −X, image right = camera +Y. landscape: image axes = camera axes. */
  orientation?: "portrait" | "landscape";
  fovDeg?: { horizontal: number; vertical: number };
};

export type NodeRef = {
  id: string;
  name?: string;
  kind?: "waypoint" | "entrance" | "destination";
  position: Vec3;
  distanceMetres?: number;
};

export type LocalizationQuery = {
  schema: typeof LOCALIZATION_QUERY_SCHEMA;
  id: string;
  worldId: string;
  sessionId?: string;
  deviceId: string;
  role?: "chest" | "left" | "right" | "back";
  nianticSiteId: string;
  capturedAt: string;
  receivedAt: string;
  image: LocalizationQueryImage;
  request: LocalizationQueryRequest;
  result: LocalizationQueryResult;
  nearestNode?: NodeRef;
  offGraphMetres?: number;
};

/** `GET /worlds/{id}/localizations` */
export type LocalizationQueries = {
  schema: typeof LOCALIZATIONS_SCHEMA;
  worldId: string;
  queries: LocalizationQuery[];
  updatedAt?: string;
};

/** What the phone posts to `POST /worlds/{id}/localize/query` (validated loosely by the proxy in local mode). */
export type LocalizationQueryUpload = Omit<
  LocalizationQuery,
  "schema" | "id" | "worldId" | "receivedAt" | "nearestNode" | "offGraphMetres"
> & { imageBase64: string };

export const LOCALIZATIONS_KEPT = 50;

/** Did VPS actually localize this frame? (A completed request can still carry `localizationFailed`.) */
export function querySucceeded(q: LocalizationQuery): boolean {
  return q.request.status === "completed" && (q.request.error ?? "none") === "none";
}

/** Same-origin URL of the stored query JPEG. */
export function queryImageUrl(q: LocalizationQuery): string | null {
  return q.image.path ? assetUrl(q.image.path) : null;
}

/** Short status for pills: what happened to the query. */
export function queryOutcome(q: LocalizationQuery): { label: string; tone: "ok" | "warn" | "bad" } {
  if (querySucceeded(q)) {
    if (q.result.trackingState === "localized") return { label: "Localized", tone: "ok" };
    if (q.result.trackingState === "limited") return { label: "Limited", tone: "warn" };
    return { label: "Localized · no anchor", tone: "warn" };
  }
  if (q.request.status === "frameRejected") return { label: `Rejected · ${humanError(q.request.error)}`, tone: "warn" };
  if (q.request.status === "pending") return { label: "Pending", tone: "warn" };
  return { label: `Failed · ${humanError(q.request.error)}`, tone: "bad" };
}

const ERRORS: Record<string, string> = {
  none: "ok",
  badCameraAngle: "camera at floor or sky",
  badTracking: "ARKit tracking poor",
  badNetworkConnection: "no network",
  localizationFailed: "no match in map",
  noMapFound: "no map nearby",
  authFailure: "auth failed",
  permissionDenied: "site not permitted",
  quotaExceeded: "quota exceeded",
  requestsLimitExceeded: "rate limited",
  internalServer: "server error",
  internalClient: "bad response",
  unknown: "unknown error",
};

export function humanError(code: string | undefined): string {
  if (!code) return "unknown";
  return ERRORS[code] ?? code.replace(/([a-z])([A-Z])/g, "$1 $2").toLowerCase();
}

/* ---------------------------------------------------------------- validation */

const isNum = (v: unknown): v is number => typeof v === "number" && Number.isFinite(v);
const isStr = (v: unknown): v is string => typeof v === "string";
const isObj = (v: unknown): v is Record<string, unknown> => typeof v === "object" && v !== null && !Array.isArray(v);
const isVec = (v: unknown, n: number): boolean => Array.isArray(v) && v.length === n && v.every(isNum);
const isPose = (v: unknown): v is Pose => isObj(v) && isVec(v.position, 3) && isVec(v.rotation, 4);

const TRACKING = new Set(["localized", "limited", "lost"]);
const STATUS = new Set(["completed", "failed", "frameRejected", "pending", "unknown"]);
const TYPES = new Set(["vpsLocalize", "universalLocalize", "getGraph", "getReplacedNodes", "registerNode", "unknown"]);

/** Problems with one stored record (empty = valid). Lenient on optional fields so a newer backend still renders. */
export function validateQuery(q: unknown, path = "query"): string[] {
  const errs: string[] = [];
  if (!isObj(q)) return [`${path} must be an object`];
  for (const k of ["id", "worldId", "deviceId", "nianticSiteId", "capturedAt", "receivedAt"] as const)
    if (!isStr(q[k])) errs.push(`${path}.${k} must be a string`);
  if (!isObj(q.image) || !isNum(q.image.width) || !isNum(q.image.height)) errs.push(`${path}.image needs width and height`);
  if (!isObj(q.request) || !isStr(q.request.identifier) || !STATUS.has(q.request.status as string) || !TYPES.has(q.request.type as string))
    errs.push(`${path}.request needs identifier, type and status`);
  if (!isObj(q.result) || !TRACKING.has(q.result.trackingState as string)) errs.push(`${path}.result.trackingState is invalid`);
  else {
    if (q.result.pose !== undefined && !isPose(q.result.pose)) errs.push(`${path}.result.pose must be a pose`);
    if (q.result.currentPose !== undefined && !isPose(q.result.currentPose)) errs.push(`${path}.result.currentPose must be a pose`);
  }
  return errs;
}

/** Validate the phone's upload body (used by the Next.js proxy when no backend is configured). */
export function validateQueryUpload(u: unknown): string[] {
  const errs: string[] = [];
  if (!isObj(u)) return ["upload must be an object"];
  for (const k of ["deviceId", "nianticSiteId", "capturedAt", "imageBase64"] as const)
    if (!isStr(u[k]) || !u[k]) errs.push(`${k} is required`);
  if (isStr(u.imageBase64) && u.imageBase64.length > 4_000_000) errs.push("imageBase64 is too large");
  if (!isObj(u.image) || !isNum(u.image.width) || !isNum(u.image.height)) errs.push("image needs width and height");
  if (!isObj(u.request) || !isStr(u.request.identifier) || !STATUS.has(u.request.status as string) || !TYPES.has(u.request.type as string) || !isStr(u.request.startedAt))
    errs.push("request needs identifier, type, status and startedAt");
  if (!isObj(u.result) || !TRACKING.has(u.result.trackingState as string)) errs.push("result.trackingState is invalid");
  else if (u.result.pose !== undefined && !isPose(u.result.pose)) errs.push("result.pose must be a pose");
  return errs;
}

/** Keep the records that parse; drop (and warn about) anything malformed rather than failing the whole feed. */
export function parseQueries(input: unknown): LocalizationQuery[] {
  const list = Array.isArray(input) ? input : isObj(input) && Array.isArray(input.queries) ? input.queries : [];
  const out: LocalizationQuery[] = [];
  list.forEach((q, i) => {
    const errs = validateQuery(q, `queries[${i}]`);
    if (errs.length) console.warn("[localization] skipping record:", errs.join("; "));
    else out.push(q as LocalizationQuery);
  });
  return out;
}

/** Newest first, by capture time (the backend already orders this way; re-sort defensively). */
export function sortQueries(list: LocalizationQuery[]): LocalizationQuery[] {
  return [...list].sort((a, b) => b.capturedAt.localeCompare(a.capturedAt));
}

/** Relative age like "3 s ago" / "2 min ago" for the live pill. */
export function formatAge(iso: string, now = Date.now()): string {
  const s = Math.max(0, Math.round((now - Date.parse(iso)) / 1000));
  if (s < 1) return "just now";
  if (s < 60) return `${s} s ago`;
  const m = Math.round(s / 60);
  if (m < 60) return `${m} min ago`;
  const h = Math.round(m / 60);
  return h < 48 ? `${h} h ago` : `${Math.round(h / 24)} d ago`;
}
