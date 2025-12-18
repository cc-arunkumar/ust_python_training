import React from "react";
import { Button } from "@/components/ui/button";
import { PanelLeft, Menu } from "lucide-react";
import { useSidebar } from "@/components/ui/sidebar";

interface SidebarToggleProps {
  className?: string;
  ariaLabel?: string;
  compact?: boolean;
}

/**
 * SidebarToggle - small button to toggle the sidebar open/collapse state.
 * Uses the project's `useSidebar` hook from `components/ui/sidebar`.
 */
const SidebarToggle: React.FC<SidebarToggleProps> = ({
  className,
  ariaLabel = "Toggle sidebar",
  compact = false,
}) => {
  // If used outside SidebarProvider, fall back to a no-op
  let toggle: () => void = () => {};
  try {
    const ctx = useSidebar();
    toggle = ctx?.toggleSidebar ?? toggle;
  } catch (e) {
    // ignore - useSidebar throws when not inside provider
    // fallback will be a no-op
  }

  return (
    <Button
      variant="ghost"
      size="icon"
      onClick={toggle}
      className={className}
      aria-label={ariaLabel}
      title={ariaLabel}
    >
      {compact ? (
        <Menu className="h-4 w-4" />
      ) : (
        <PanelLeft className="h-5 w-5" />
      )}
    </Button>
  );
};

export default SidebarToggle;
