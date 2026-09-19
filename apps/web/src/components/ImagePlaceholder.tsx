import type { ImageAsset } from "@/lib/images";

type Props = {
  asset: ImageAsset;
  className?: string;
  /** Compact variant hides the filename/size details (used for small thumbnails). */
  compact?: boolean;
};

/**
 * Visual stand-in for an image that hasn't been generated yet. Shows the
 * target path so the file can be dropped straight into /public.
 */
export function ImagePlaceholder({ asset, className = "", compact }: Props) {
  return (
    <div
      role="img"
      aria-label={`Placeholder: ${asset.alt}`}
      title={asset.prompt}
      className={`flex h-full w-full min-w-0 flex-col items-center justify-center gap-2 overflow-hidden rounded-lg border border-dashed border-void-black/20 bg-pure-white p-4 text-center ${className}`}
    >
      <svg
        aria-hidden="true"
        viewBox="0 0 24 24"
        className="size-6 text-void-black/40"
        fill="none"
        stroke="currentColor"
        strokeWidth="1.5"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        <rect x="3" y="5" width="18" height="14" rx="2" />
        <circle cx="9" cy="10" r="1.5" />
        <path d="m21 16-5-5-9 8" />
      </svg>
      {!compact && (
        <>
          <span className="text-caption font-medium text-void-black/60">
            Image placeholder
          </span>
          <code className="max-w-full text-caption break-all text-void-black/40">
            {asset.src} · {asset.width}×{asset.height}
          </code>
        </>
      )}
    </div>
  );
}
