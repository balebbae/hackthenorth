"use client";

import { useState, type ReactNode } from "react";
import { UploadSplatDialog, type UploadDialogMode } from "./UploadSplatDialog";

type Props = {
  mode?: UploadDialogMode;
  className?: string;
  children: ReactNode;
  "aria-label"?: string;
};

/** A button that opens the splat upload dialog. Usable from server components. */
export function UploadSplatButton({ mode = { kind: "new" }, className = "btn-primary", children, ...rest }: Props) {
  const [open, setOpen] = useState(false);
  return (
    <>
      <button type="button" className={className} onClick={() => setOpen(true)} {...rest}>
        {children}
      </button>
      <UploadSplatDialog open={open} mode={mode} onClose={() => setOpen(false)} />
    </>
  );
}
