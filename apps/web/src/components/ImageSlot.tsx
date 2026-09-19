import Image from "next/image";
import type { ImageAsset } from "@/lib/images";
import { hasImage } from "@/lib/images.server";
import { ImagePlaceholder } from "./ImagePlaceholder";

type Props = {
  asset: ImageAsset;
  className?: string;
  imgClassName?: string;
  priority?: boolean;
  sizes?: string;
};

/**
 * Server component: renders the real image when it exists in /public,
 * otherwise a labelled placeholder. Keeps the intrinsic aspect ratio either way.
 */
export function ImageSlot({
  asset,
  className = "",
  imgClassName = "",
  priority,
  sizes,
}: Props) {
  const ready = hasImage(asset);
  return (
    <div
      className={`relative min-w-0 overflow-hidden ${className}`}
      style={{ aspectRatio: `${asset.width} / ${asset.height}` }}
    >
      {ready ? (
        <Image
          src={asset.src}
          alt={asset.alt}
          width={asset.width}
          height={asset.height}
          priority={priority}
          sizes={sizes}
          className={`h-full w-full object-cover ${imgClassName}`}
        />
      ) : (
        <ImagePlaceholder asset={asset} />
      )}
    </div>
  );
}
