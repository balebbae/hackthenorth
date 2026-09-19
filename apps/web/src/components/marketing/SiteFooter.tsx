import Link from "next/link";
import { Logo } from "@/components/Logo";
import { BRAND } from "@/lib/brand";

const COLUMNS = [
  {
    title: "Product",
    links: [
      { label: "Voice guidance", href: "#product" },
      { label: "Obstacle sensing", href: "#product" },
      { label: "3D maps", href: "#maps" },
      { label: "Dashboard", href: "/dashboard" },
    ],
  },
  {
    title: "Team",
    links: [
      { label: "How it works", href: "#how-it-works" },
      { label: "Toolkit", href: "#maps" },
      { label: "Log in", href: "/login" },
    ],
  },
];

export function SiteFooter() {
  return (
    <footer className="border-t border-hairline">
      <div className="container-page grid gap-10 py-12 md:grid-cols-[1.4fr_1fr_1fr]">
        <div className="max-w-xs">
          <Logo />
          <p className="mt-4 text-body-sm text-void-black/60">
            {BRAND.description}
          </p>
        </div>
        {COLUMNS.map((col) => (
          <div key={col.title}>
            <h3 className="text-caption font-semibold tracking-[0.01em] text-void-black/60 uppercase">
              {col.title}
            </h3>
            <ul className="mt-3 space-y-2">
              {col.links.map((l) => (
                <li key={l.label}>
                  <Link
                    href={l.href}
                    className="text-body-sm text-void-black/90 transition-colors duration-200 hover:text-wander-blue"
                  >
                    {l.label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
      <div className="container-page flex flex-col gap-2 border-t border-hairline py-6 text-caption text-void-black/40 sm:flex-row sm:items-center sm:justify-between">
        <span>
          © {new Date().getFullYear()} {BRAND.name}. Built at Hack the North.
        </span>
        <span>Fonts: Inter · Source Serif 4</span>
      </div>
    </footer>
  );
}
