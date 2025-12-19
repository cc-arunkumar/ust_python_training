import React, { useState } from "react";
import { useAuth } from "@/contexts/AuthContext";
import {
  Shield,
  Users,
  Code2,
  LogOut,
  LayoutDashboard,
  Sun,
  Moon,
  Bell,
  Menu,
} from "lucide-react";
import {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
} from "@/components/ui/dropdown-menu";
import { useTasks } from "@/contexts/TaskContext";
import { useEmployees } from "@/contexts/EmployeesContext";
import { Button } from "@/components/ui/button";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { useNavigate, useLocation } from "react-router-dom";

type ViewMode = "admin" | "manager" | "employee";

interface HeaderProps {
  currentView: ViewMode;
  onViewChange: (view: ViewMode) => void;
  onToggleSidebar?: () => void;
}

const Header: React.FC<HeaderProps> = ({
  currentView,
  onViewChange,
  onToggleSidebar,
}) => {
  const { user, logout, isAdmin, isManager, isEmployee } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const { tasks } = useTasks();
  const { getEmployeeById } = useEmployees();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  const getInitials = (name: string) => {
    return name
      .split(" ")
      .map((n) => n[0])
      .join("")
      .toUpperCase();
  };

  const [showFull, setShowFull] = useState(false);

  // track read notification ids (persisted in localStorage)
  const [readNotifications, setReadNotifications] = React.useState<string[]>(
    () => {
      try {
        const raw = localStorage.getItem("readNotifications");
        return raw ? JSON.parse(raw) : [];
      } catch (e) {
        return [];
      }
    }
  );

  const notificationItems = React.useMemo(() => {
    const items: any[] = [];
    try {
      tasks.forEach((t: any) => {
        if (!user) return;
        const uid = user?.e_id;
        if (isAdmin) {
          if (t.assigned_to) {
            const assignee =
              getEmployeeById(String(t.assigned_to))?.name ||
              String(t.assigned_to);
            items.push({
              id: t.t_id + "-assigned",
              title: `Assigned to ${assignee}`,
              desc: t.title,
              t_id: t.t_id,
            });
          }
          if (t.status === "REVIEW")
            items.push({
              id: t.t_id + "-review",
              title: `In review`,
              desc: t.title,
              t_id: t.t_id,
            });
        } else if (isManager) {
          if (t.created_by === uid)
            items.push({
              id: t.t_id + "-created",
              title: `You created task`,
              desc: t.title,
              t_id: t.t_id,
            });
          if (t.assigned_to === uid)
            items.push({
              id: t.t_id + "-assigned-to-you",
              title: `Assigned to you`,
              desc: t.title,
              t_id: t.t_id,
            });
          if (t.reviewer === uid && t.status === "REVIEW")
            items.push({
              id: t.t_id + "-review",
              title: `Needs review`,
              desc: t.title,
              t_id: t.t_id,
            });
        } else {
          if (t.assigned_to === uid)
            items.push({
              id: t.t_id + "-assigned-to-you",
              title: `Assigned to you`,
              desc: t.title,
              t_id: t.t_id,
            });
          if (t.reviewer === uid && t.status === "REVIEW")
            items.push({
              id: t.t_id + "-review",
              title: `Ready for review`,
              desc: t.title,
              t_id: t.t_id,
            });
        }
      });
    } catch (e) {
      // ignore
    }

    // filter out read notifications
    return items.filter((it) => !readNotifications.includes(it.id));
  }, [tasks, user, isAdmin, isManager, getEmployeeById, readNotifications]);

  const [theme, setTheme] = React.useState<"light" | "dark">(() => {
    try {
      const stored = localStorage.getItem("theme");
      if (stored === "dark") return "dark";
      if (stored === "light") return "light";
    } catch (e) {
      // ignore
    }
    // fallback to prefers-color-scheme
    if (typeof window !== "undefined" && window.matchMedia) {
      return window.matchMedia("(prefers-color-scheme: dark)").matches
        ? "dark"
        : "light";
    }
    return "light";
  });

  React.useEffect(() => {
    try {
      const root = document.documentElement;
      if (theme === "dark") root.classList.add("dark");
      else root.classList.remove("dark");
      localStorage.setItem("theme", theme);
    } catch (e) {
      // ignore
    }
  }, [theme]);

  const toggleTheme = () => setTheme((t) => (t === "dark" ? "light" : "dark"));

  return (
    // Header spans full width at the top. Sidebar will start below it.
    <header className="sticky top-0 z-50 w-full border-b border-border bg-card/95 backdrop-blur supports-[backdrop-filter]:bg-card/60">
      <div className="flex h-16 items-center justify-between px-6">
        <div className="flex items-center gap-6">
          <button
            // Always show hamburger on the left so users can toggle sidebar
            className="p-2 rounded hover:bg-muted/60"
            onClick={() => onToggleSidebar && onToggleSidebar()}
            aria-label="Toggle sidebar"
            title="Toggle sidebar"
          >
            <Menu className="h-5 w-5" />
          </button>

          <img src="/favicon.ico" alt="UST" className="h-5 w-5" />

          <div className="flex items-center gap-3">
            <div className="flex h-50 w-50 items-center justify-center text-black rounded-lg ">
              <div className="text-2xl font-bold">Jira-Lite</div>
            </div>
          </div>

          <nav className="hidden md:flex items-center gap-2 ml-8">
            {/**
             * Render role buttons only if the logged-in user's roles include them.
             * We keep the isAdmin/isManager flags for other logic but rely on
             * the user's `role` array for button visibility so a user with
             * exactly ['admin','employee'] won't see the manager button.
             */}
            {React.useMemo(() => {
              const roles = new Set(
                (user?.role || []).map((r: string) => String(r).toLowerCase())
              );

              return (
                <>
                  {roles.has("admin") && (
                    <button
                      onClick={() => onViewChange("admin")}
                      className={`nav-button nav-button-admin ${
                        currentView === "admin"
                          ? "nav-button-active ring-[hsl(var(--role-admin))]"
                          : ""
                      }`}
                    >
                      <Shield className="h-4 w-4" />
                      Admin
                    </button>
                  )}

                  {roles.has("manager") && (
                    <button
                      onClick={() => onViewChange("manager")}
                      className={`nav-button nav-button-manager ${
                        currentView === "manager"
                          ? "nav-button-active ring-[hsl(var(--role-manager))]"
                          : ""
                      }`}
                    >
                      <Users className="h-4 w-4" />
                      Manager
                    </button>
                  )}

                  {roles.has("employee") && (
                    <button
                      onClick={() => onViewChange("employee")}
                      className={`nav-button nav-button-developer ${
                        currentView === "employee"
                          ? "nav-button-active ring-[hsl(var(--role-developer))]"
                          : ""
                      }`}
                    >
                      <Code2 className="h-4 w-4" />
                      Employee
                    </button>
                  )}
                </>
              );
            }, [user, currentView, onViewChange])}
          </nav>
        </div>

        <div className="flex items-center gap-4">
          {/* Notifications dropdown */}
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <button
                className="relative p-2 rounded hover:bg-muted/60"
                aria-label="Notifications"
              >
                <Bell className="h-5 w-5" />
                {/* badge (only show unread notifications count) */}
                {notificationItems.length > 0 ? (
                  <span className="absolute -top-1 -right-1 inline-flex items-center justify-center rounded-full bg-rose-600 text-white text-[10px] px-1.5 py-0.5">
                    {notificationItems.length}
                  </span>
                ) : null}
              </button>
            </DropdownMenuTrigger>

            <DropdownMenuContent align="end" className="w-80">
              <DropdownMenuLabel>Notifications</DropdownMenuLabel>
              <div className="max-h-64 overflow-auto">
                {notificationItems && notificationItems.length > 0 ? (
                  notificationItems.map((it) => (
                    <DropdownMenuItem
                      key={it.id}
                      onSelect={() => {
                        // mark as read (persist locally) then navigate to tasks board
                        try {
                          const next = Array.from(
                            new Set([...readNotifications, it.id])
                          );
                          localStorage.setItem(
                            "readNotifications",
                            JSON.stringify(next)
                          );
                          setReadNotifications(next);
                        } catch (e) {
                          // ignore
                        }
                        navigate("/dashboard/tasks");
                      }}
                      className="flex flex-col items-start gap-1"
                    >
                      <div className="text-sm font-medium">{it.title}</div>
                      <div className="text-xs text-muted-foreground line-clamp-2">
                        {it.desc}
                      </div>
                    </DropdownMenuItem>
                  ))
                ) : (
                  <div className="p-3 text-sm text-muted-foreground">
                    No notifications
                  </div>
                )}
              </div>
            </DropdownMenuContent>
          </DropdownMenu>
          <div className="hidden sm:flex flex-col items-end">
            <span className="text-sm font-medium text-foreground">
              {user?.employee?.name}
            </span>
            <span className="text-xs text-muted-foreground capitalize">
              {user?.role.join(", ")}
            </span>
          </div>
          <div className="relative">
            {/* Avatar */}
            <Avatar
              onClick={() => setShowFull((v) => !v)}
              className="h-9 w-9 border-2 border-primary/20 cursor-pointer overflow-hidden"
            >
              <AvatarImage
                src="https://wallpaperaccess.com/full/8946245.jpg"
                alt="UST"
                className="object-cover"
              />
              <AvatarFallback>U</AvatarFallback>
            </Avatar>

            {/* Popup image – same style, bigger */}
            {showFull && (
              <div className="absolute top-12 right-0 z-50">
                <img
                  src="https://wallpaperaccess.com/full/8946245.jpg"
                  alt="UST"
                  className="h-full w-full object-contain"
                />
              </div>
            )}
          </div>
          <div className="flex items-center gap-2">
            <Button
              variant="ghost"
              size="icon"
              onClick={toggleTheme}
              className="text-muted-foreground hover:text-foreground"
              aria-label="Toggle theme"
              title={
                theme === "dark"
                  ? "Switch to light mode"
                  : "Switch to dark mode"
              }
            >
              {theme === "dark" ? (
                <Sun className="h-5 w-5" />
              ) : (
                <Moon className="h-5 w-5" />
              )}
            </Button>

            <Button
              variant="ghost"
              size="icon"
              onClick={handleLogout}
              className="text-muted-foreground hover:text-foreground"
            >
              <LogOut className="h-5 w-5" />
            </Button>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
