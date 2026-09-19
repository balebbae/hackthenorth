/**
 * The phone hand-off link shown as a QR code in the world viewer
 * (`shared/contracts/README.md` › "Phone hand-off link").
 *
 *   wander://connect?v=1&world=<id>&site=<nianticSiteId>&backend=<url>&name=<name>
 *
 * It carries *which* world, site and backend the phone should use — never
 * the API key or the Niantic developer token, which stay on the phone.
 */
export const CONNECT_SCHEME = "wander";
export const CONNECT_HOST = "connect";
export const CONNECT_VERSION = "1";

export type ConnectLinkInput = {
  worldId: string;
  name?: string;
  nianticSiteId?: string | null;
  /** Base URL of the worlds API the phone should post to. */
  backendUrl?: string | null;
};

export function buildConnectLink(input: ConnectLinkInput): string {
  // RFC 3986 percent-encoding (spaces → %20), not form encoding: Swift's URLComponents
  // does not turn "+" back into a space.
  const params: [string, string][] = [
    ["v", CONNECT_VERSION],
    ["world", input.worldId],
  ];
  if (input.nianticSiteId) params.push(["site", input.nianticSiteId]);
  if (input.backendUrl) params.push(["backend", input.backendUrl.replace(/\/+$/, "")]);
  if (input.name) params.push(["name", input.name.slice(0, 80)]);
  const query = params.map(([k, v]) => `${k}=${encodeURIComponent(v)}`).join("&");
  return `${CONNECT_SCHEME}://${CONNECT_HOST}?${query}`;
}

/** Inverse of `buildConnectLink`; null when the URL is not a v1 connect link. */
export function parseConnectLink(raw: string): ConnectLinkInput | null {
  let url: URL;
  try {
    url = new URL(raw.trim());
  } catch {
    return null;
  }
  if (url.protocol !== `${CONNECT_SCHEME}:` || url.host !== CONNECT_HOST) return null;
  if ((url.searchParams.get("v") ?? "1") !== CONNECT_VERSION) return null;
  const worldId = url.searchParams.get("world");
  if (!worldId || !/^[a-z0-9][a-z0-9._-]{0,63}$/.test(worldId)) return null;
  return {
    worldId,
    name: url.searchParams.get("name") ?? undefined,
    nianticSiteId: url.searchParams.get("site"),
    backendUrl: url.searchParams.get("backend"),
  };
}

/** True when the phone could actually reach this URL (not a loopback address on the dev machine). */
export function isReachableFromPhone(backendUrl: string): boolean {
  try {
    const { hostname } = new URL(backendUrl);
    return !["localhost", "127.0.0.1", "::1", "[::1]", "0.0.0.0"].includes(hostname);
  } catch {
    return false;
  }
}
