"use client";

import { useState, useTransition, type FormEvent, type ReactNode } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { Icon } from "@/components/Icon";
import { BRAND } from "@/lib/brand";

type Mode = "login" | "signup";

const COPY: Record<Mode, { title: string; sub: string; cta: string }> = {
  login: {
    title: "Welcome back",
    sub: "Log in to manage your worlds, routes, and devices.",
    cta: "Log in",
  },
  signup: {
    title: "Create your workspace",
    sub: "Map a space, drop waypoints, and walk it within the hour.",
    cta: "Create account",
  },
};

/**
 * UI-only auth form. There is no authentication yet: submitting simply
 * navigates to the dashboard so the flow can be demoed end to end.
 */
export function LoginForm() {
  const router = useRouter();
  const [mode, setMode] = useState<Mode>("login");
  const [showPassword, setShowPassword] = useState(false);
  const [pending, startTransition] = useTransition();
  const copy = COPY[mode];

  function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    startTransition(() => router.push("/dashboard"));
  }

  return (
    <div className="w-full max-w-sm">
      <h1 className="text-[32px] leading-[1.15] font-medium tracking-[-0.9px] text-void-black">
        {copy.title}
      </h1>
      <p className="editorial mt-2">{copy.sub}</p>

      <div className="mt-8 grid gap-2">
        <SsoButton label="Continue with Google" glyph={<GoogleGlyph />} />
        <SsoButton label="Continue with Apple" glyph={<AppleGlyph />} />
      </div>

      <div
        role="separator"
        className="my-6 flex items-center gap-3 text-caption text-void-black/40"
      >
        <span className="h-px flex-1 bg-hairline" />
        or
        <span className="h-px flex-1 bg-hairline" />
      </div>

      <form onSubmit={handleSubmit} className="grid gap-4" noValidate>
        {mode === "signup" && (
          <div className="grid gap-1.5">
            <label htmlFor="name" className="label">
              Name
            </label>
            <input
              id="name"
              name="name"
              type="text"
              autoComplete="name"
              placeholder="Ada Lovelace"
              className="input"
            />
          </div>
        )}

        <div className="grid gap-1.5">
          <label htmlFor="email" className="label">
            Email
          </label>
          <input
            id="email"
            name="email"
            type="email"
            autoComplete="email"
            placeholder="you@team.com"
            className="input"
          />
        </div>

        <div className="grid gap-1.5">
          <div className="flex items-center justify-between">
            <label htmlFor="password" className="label">
              Password
            </label>
            {mode === "login" && (
              <Link
                href="#"
                className="text-caption font-medium text-wander-blue hover:underline"
              >
                Forgot password?
              </Link>
            )}
          </div>
          <div className="relative">
            <input
              id="password"
              name="password"
              type={showPassword ? "text" : "password"}
              autoComplete={mode === "login" ? "current-password" : "new-password"}
              placeholder="••••••••••"
              className="input pr-11"
            />
            <button
              type="button"
              onClick={() => setShowPassword((v) => !v)}
              aria-label={showPassword ? "Hide password" : "Show password"}
              aria-pressed={showPassword}
              className="btn-icon absolute top-1/2 right-1.5 -translate-y-1/2"
            >
              <Icon name={showPassword ? "eye" : "lock"} size={16} />
            </button>
          </div>
        </div>

        {mode === "login" && (
          <label className="flex items-center gap-2 text-body-sm text-void-black/90">
            <input
              type="checkbox"
              name="remember"
              defaultChecked
              className="size-4 rounded-sm border-hairline accent-wander-blue"
            />
            Keep me signed in
          </label>
        )}

        <button
          type="submit"
          disabled={pending}
          className="btn-primary btn-lg mt-2 w-full"
        >
          {pending ? "Opening your workspace…" : copy.cta}
          {!pending && <Icon name="arrowRight" size={16} />}
        </button>
      </form>

      <p className="mt-6 text-center text-body-sm text-void-black/60">
        {mode === "login" ? "New to " + BRAND.name + "?" : "Already have an account?"}{" "}
        <button
          type="button"
          onClick={() => setMode(mode === "login" ? "signup" : "login")}
          className="font-medium text-wander-blue hover:underline"
        >
          {mode === "login" ? "Create an account" : "Log in"}
        </button>
      </p>

      <p className="mt-8 text-center text-caption text-void-black/40">
        By continuing you agree to the Terms and acknowledge the Privacy Policy.
      </p>
    </div>
  );
}

function SsoButton({ label, glyph }: { label: string; glyph: ReactNode }) {
  return (
    <button
      type="button"
      className="inline-flex w-full items-center justify-center gap-3 rounded-lg border border-hairline bg-pure-white px-4 py-[10px] text-body-sm font-medium text-void-black/90 transition-colors duration-200 hover:bg-void-black/[0.03] active:bg-void-black/5"
    >
      {glyph}
      {label}
    </button>
  );
}

function GoogleGlyph() {
  return (
    <svg aria-hidden="true" viewBox="0 0 24 24" width="18" height="18">
      <path
        fill="#4285F4"
        d="M23.5 12.3c0-.8-.1-1.6-.2-2.3H12v4.4h6.5a5.6 5.6 0 0 1-2.4 3.7v3h3.9c2.3-2.1 3.5-5.2 3.5-8.8Z"
      />
      <path
        fill="#34A853"
        d="M12 24c3.2 0 6-1.1 7.9-2.9l-3.9-3a7.2 7.2 0 0 1-10.7-3.8H1.4v3.1A12 12 0 0 0 12 24Z"
      />
      <path
        fill="#FBBC05"
        d="M5.3 14.3a7.2 7.2 0 0 1 0-4.6V6.6H1.4a12 12 0 0 0 0 10.8l3.9-3.1Z"
      />
      <path
        fill="#EA4335"
        d="M12 4.8c1.8 0 3.3.6 4.6 1.8l3.4-3.4A12 12 0 0 0 1.4 6.6l3.9 3.1A7.2 7.2 0 0 1 12 4.8Z"
      />
    </svg>
  );
}

function AppleGlyph() {
  return (
    <svg aria-hidden="true" viewBox="0 0 24 24" width="18" height="18" fill="currentColor">
      <path d="M16.7 12.6c0-2.4 2-3.6 2.1-3.7a4.6 4.6 0 0 0-3.6-2c-1.5-.1-3 .9-3.7.9-.8 0-2-.9-3.2-.9A4.8 4.8 0 0 0 4.2 9.4c-1.7 3-.4 7.5 1.3 9.9.8 1.2 1.8 2.5 3.1 2.5 1.2-.1 1.7-.8 3.2-.8s1.9.8 3.2.8 2.2-1.2 3-2.4a10 10 0 0 0 1.4-2.8 4.4 4.4 0 0 1-2.7-4ZM14.3 5.4A4.3 4.3 0 0 0 15.3 2a4.4 4.4 0 0 0-2.9 1.5 4.1 4.1 0 0 0-1 3.2 3.6 3.6 0 0 0 2.9-1.3Z" />
    </svg>
  );
}
