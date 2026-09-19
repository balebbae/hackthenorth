import Link from "next/link";
import { Logo } from "@/components/Logo";

const NAV_ITEMS = [
  { label: "Product", href: "#product" },
  { label: "How it works", href: "#how-it-works" },
  { label: "Maps", href: "#maps" },
  { label: "Dashboard", href: "/dashboard" },
];

/** Fixed 64px top bar: logo left, centered links, right-aligned actions. */
export function SiteNav() {
  return (
    <header className="fixed inset-x-0 top-0 z-40 h-[var(--nav-height)] bg-pure-white shadow-[var(--shadow-nav)]">
      <div className="container-page flex h-full items-center justify-between">
        <Logo />
        <nav aria-label="Primary" className="hidden md:block">
          <ul className="flex items-center">
            {NAV_ITEMS.map((item) => (
              <li key={item.href}>
                <Link href={item.href} className="nav-link">
                  {item.label}
                </Link>
              </li>
            ))}
          </ul>
        </nav>
        <div className="flex items-center gap-1">
          <Link href="/login" className="nav-link hidden sm:inline-flex">
            Log in
          </Link>
          <Link href="/login" className="btn-primary">
            Get started
          </Link>
        </div>
      </div>
    </header>
  );
}
