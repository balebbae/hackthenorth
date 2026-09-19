import Image from "next/image";
import Link from "next/link";
import { BRAND } from "@/lib/brand";

type MarkProps = { size?: number; className?: string; priority?: boolean };

/** Brand mark: the Wander gradient orb. Works on light and navy surfaces. */
export function LogoMark({ size = 28, className = "", priority }: MarkProps) {
  return (
    <Image
      src="/brand/wander-mark.png"
      alt=""
      aria-hidden="true"
      width={size}
      height={size}
      priority={priority}
      className={`shrink-0 object-contain ${className}`}
    />
  );
}

type LogoProps = {
  href?: string;
  className?: string;
  size?: number;
  /** Use on dark (navy) surfaces. */
  inverted?: boolean;
};

export function Logo({ href = "/", className = "", size = 28, inverted }: LogoProps) {
  return (
    <Link
      href={href}
      className={`inline-flex items-center gap-2 rounded-lg ${
        inverted ? "text-pure-white" : "text-void-black"
      } ${className}`}
      aria-label={`${BRAND.name} home`}
    >
      <LogoMark size={size} priority />
      <span className="text-body font-semibold tracking-[-0.01em]">
        {BRAND.name}
      </span>
    </Link>
  );
}
