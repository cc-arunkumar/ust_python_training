import React from "react";
import { NavLink } from "@/components/NavLink";
import {
  LayoutGrid,
  LayoutDashboard,
  Users,
  Settings,
  X,
  Menu,
} from "lucide-react";

interface SidebarProps {
  isOpen?: boolean;
  onClose?: () => void;
  onToggle?: () => void;
}

const Sidebar: React.FC<SidebarProps> = ({
  isOpen = true,
  onClose,
  onToggle,
}) => {
  // on small screens we show a fixed drawer when open, otherwise keep the md sidebar
  const baseClass = isOpen ? "block" : "hidden md:block";

  return (
    <aside
      // Position the sidebar below the header (header is h-16).
      // - On small screens: act as a fixed drawer when open, hidden when closed.
      // - On md+ screens: sticky under the header and toggle width between 16rem and 4rem.
      // Start below header (header height = h-16). Use remaining viewport height.
      className={`
           ${baseClass}
           fixed md:sticky
           left-0 top-16
           z-40
           border-r border-border bg-card
            h-[calc(100vh-4rem)]
           transition-[width,transform,opacity]
           duration-200 ease-in-out
           ${isOpen ? "w-64" : "w-0 md:w-16"}
           overflow-hidden
         `}
    >
      <div className="p-4">
        {/* Make the title live in the sidebar — clicking it will toggle the sidebar */}
        <div
          className={`h-full overflow-hidden ${isOpen ? "px-4" : "px-2"} pt-4`}
        >
          {/* LOGO / TITLE (TOGGLE BUTTON) */}
          <button
            onClick={onToggle}
            className="flex items-center gap-3 w-full px-2 py-2 rounded hover:bg-muted"
          >
            <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-primary">
              <img src="/favicon.ico" alt="UST" className="h-5 w-5" />
            </div>

            {isOpen ? (
              <div className="text-left">
                <div className="text-sm font-semibold">UST Task Manager</div>
                <div className="text-xs text-muted-foreground">
                  Employee Management System
                </div>
              </div>
            ) : (
              // show hamburger icon when collapsed so user can expand the sidebar
              <div className="ml-2">
                <Menu className="h-5 w-5 text-foreground" />
              </div>
            )}
          </button>
        </div>
        <div className="flex items-center justify-between mb-3 md:hidden">
          <div className="text-sm font-semibold">Menu</div>
          <button onClick={onClose} className="p-1 rounded hover:bg-muted/60">
            <X className="h-4 w-4" />
          </button>
        </div>

        <nav className="flex flex-col gap-1">
          <NavLink
            to="/dashboard"
            className="flex items-center gap-3 px-3 py-2 rounded hover:bg-muted"
            activeClassName="bg-muted/70 font-semibold"
          >
            <LayoutDashboard className="h-4 w-4" />
            Dashboard
          </NavLink>

          <NavLink
            to="/dashboard/tasks"
            className="flex items-center gap-3 px-3 py-2 rounded hover:bg-muted"
            activeClassName="bg-muted/70 font-semibold"
          >
            <LayoutGrid className="h-4 w-4" />
            Tasks
          </NavLink>

          <NavLink
            to="/dashboard/employees"
            className="flex items-center gap-3 px-3 py-2 rounded hover:bg-muted"
            activeClassName="bg-muted/70 font-semibold"
          >
            <Users className="h-4 w-4" />
            Employees
          </NavLink>

          <NavLink
            to="/dashboard/settings"
            className="flex items-center gap-3 px-3 py-2 rounded hover:bg-muted"
            activeClassName="bg-muted/70 font-semibold"
          >
            <Settings className="h-4 w-4" />
            Settings
          </NavLink>
        </nav>
      </div>
    </aside>
  );
};

export default Sidebar;
