import Link from "next/link";
import { Icon, type IconName } from "@/components/Icon";
import { LogoMark } from "@/components/Logo";
import { Avatar } from "./Avatar";
import { CURRENT_USER, DEVICES, SPACES } from "@/lib/worlds";

const PRIMARY_NAV: { label: string; icon: IconName; href: string; active?: boolean }[] = [
  { label: "Recents", icon: "clock", href: "/dashboard", active: true },
  { label: "Shared with you", icon: "users", href: "/dashboard" },
  { label: "Starred", icon: "star", href: "/dashboard" },
  { label: "Trash", icon: "trash", href: "/dashboard" },
];

/** Figma-style left rail: workspace switcher, search, nav, spaces, devices, account. */
export function Sidebar() {
  return (
    <aside className="hidden w-[260px] shrink-0 flex-col border-r border-hairline bg-pure-white lg:sticky lg:top-0 lg:flex lg:h-dvh lg:overflow-y-auto">
      {/* Workspace switcher */}
      <button
        type="button"
        className="mx-3 mt-3 flex items-center gap-2 rounded-lg px-2 py-2 text-left transition-colors duration-200 hover:bg-void-black/5"
      >
        <LogoMark size={24} />
        <span className="flex-1 truncate text-body-sm font-semibold text-void-black">
          HTN 2026
        </span>
        <Icon name="chevronsUpDown" size={14} className="text-void-black/40" />
      </button>

      {/* Search */}
      <div className="px-3 pt-2">
        <label className="relative block">
          <span className="sr-only">Search worlds</span>
          <Icon
            name="search"
            size={15}
            className="pointer-events-none absolute top-1/2 left-2.5 -translate-y-1/2 text-void-black/40"
          />
          <input
            type="search"
            placeholder="Search worlds…"
            className="input py-1.5 pl-8 pr-12 text-body-sm"
          />
          <kbd className="pointer-events-none absolute top-1/2 right-2 -translate-y-1/2 rounded-sm border border-hairline bg-stellar-white px-1.5 py-0.5 text-[11px] text-void-black/50">
            ⌘K
          </kbd>
        </label>
      </div>

      {/* Primary nav */}
      <nav aria-label="Dashboard" className="mt-3 px-3">
        <ul className="space-y-0.5">
          {PRIMARY_NAV.map((item) => (
            <li key={item.label}>
              <Link
                href={item.href}
                aria-current={item.active ? "page" : undefined}
                className={`flex items-center gap-2.5 rounded-lg px-2 py-1.5 text-body-sm font-medium transition-colors duration-200 ${
                  item.active
                    ? "bg-sky-tint text-wander-blue"
                    : "text-void-black/70 hover:bg-void-black/5 hover:text-void-black"
                }`}
              >
                <Icon name={item.icon} size={16} />
                {item.label}
              </Link>
            </li>
          ))}
        </ul>
      </nav>

      {/* Spaces */}
      <div className="mt-6 px-3">
        <div className="flex items-center justify-between px-2">
          <h2 className="text-caption font-semibold tracking-[0.01em] text-void-black/50 uppercase">
            Spaces
          </h2>
          <button type="button" className="btn-icon size-6" aria-label="New space">
            <Icon name="plus" size={14} />
          </button>
        </div>
        <ul className="mt-1.5 space-y-0.5">
          {SPACES.map((s) => (
            <li key={s.id}>
              <Link
                href="/dashboard"
                className="flex items-center gap-2.5 rounded-lg px-2 py-1.5 text-body-sm text-void-black/80 transition-colors duration-200 hover:bg-void-black/5 hover:text-void-black"
              >
                <span
                  aria-hidden="true"
                  className="inline-block size-2.5 rounded-sm"
                  style={{ background: s.color }}
                />
                <span className="flex-1 truncate">{s.name}</span>
                <span className="text-caption text-void-black/40">{s.worlds}</span>
              </Link>
            </li>
          ))}
        </ul>
      </div>

      {/* Devices */}
      <div className="mt-6 px-3">
        <h2 className="px-2 text-caption font-semibold tracking-[0.01em] text-void-black/50 uppercase">
          Devices
        </h2>
        <ul className="mt-1.5 space-y-0.5">
          {DEVICES.map((d) => (
            <li
              key={d.name}
              className="flex items-center gap-2.5 rounded-lg px-2 py-1.5 text-body-sm text-void-black/80"
            >
              <span
                aria-hidden="true"
                className={`inline-block size-2 rounded-full ${
                  d.online ? "bg-wander-blue" : "bg-void-black/20"
                }`}
              />
              <span className="flex-1 truncate">{d.name}</span>
              <span className="text-caption text-void-black/40">
                {d.online ? `${d.battery}%` : "Offline"}
              </span>
            </li>
          ))}
        </ul>
      </div>

      <div className="flex-1" />

      {/* Account */}
      <div className="border-t border-hairline p-3">
        <Link
          href="/login"
          className="flex items-center gap-2.5 rounded-lg px-2 py-1.5 text-body-sm text-void-black/70 transition-colors duration-200 hover:bg-void-black/5 hover:text-void-black"
        >
          <Icon name="users" size={16} />
          Invite teammates
        </Link>
        <div className="mt-1 flex items-center gap-2.5 rounded-lg px-2 py-1.5">
          <Avatar person={CURRENT_USER} size={28} />
          <span className="min-w-0 flex-1">
            <span className="block truncate text-body-sm font-medium text-void-black">
              {CURRENT_USER.name}
            </span>
            <span className="block text-caption text-void-black/50">Free plan</span>
          </span>
          <Link href="/" className="btn-icon" aria-label="Log out">
            <Icon name="logout" size={16} />
          </Link>
        </div>
      </div>
    </aside>
  );
}
