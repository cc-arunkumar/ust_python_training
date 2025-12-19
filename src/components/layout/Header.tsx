import React from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "@/context/AuthContext";
import { Role } from "@/types";
import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { Badge } from "@/components/ui/badge";
import {
  ChevronDown,
  LogOut,
  User,
  Shield,
  Users,
  Code,
  Bell,
  Menu,
} from "lucide-react";
import ThemeToggle from "@/components/ui/themeToggle";
import notificationService, {
  Notification,
} from "@/services/notificationService";

const roleIcons: Record<Role, React.ElementType> = {
  admin: Shield,
  manager: Users,
  developer: Code,
};

const roleColors: Record<Role, string> = {
  admin: "bg-destructive/10 text-destructive border-destructive/20",
  manager:
    "bg-status-inprogress/10 text-status-inprogress border-status-inprogress/20",
  developer: "bg-primary/10 text-primary border-primary/20",
};

interface HeaderProps {
  onMenuClick?: () => void;
}

const Header: React.FC<HeaderProps> = ({ onMenuClick }) => {
  const { user, currentRole, switchRole, logout } = useAuth();
  const navigate = useNavigate();
  const [notifications, setNotifications] = React.useState<Notification[]>([]);
  const [unreadCount, setUnreadCount] = React.useState<number>(0);
  // start polling notifications
  useNotifications(setNotifications, setUnreadCount);

  if (!user) return null;

  const RoleIcon = roleIcons[currentRole];

  return (
    <header className="h-16 border-b border-border bg-card px-4 lg:px-6 flex items-center justify-between sticky top-0 z-40 cool-header">
      <div className="flex items-center gap-4">
        <Button
          variant="ghost"
          size="icon"
          className="lg:hidden"
          onClick={onMenuClick}
        >
          <Menu className="h-5 w-5" />
        </Button>

        <div className="hidden md:block">
          <div className="text-sm text-muted-foreground">
            Welcome back,{" "}
            <span className="font-semibold text-primary-foreground">
              {user.name.split(" ")[0]}
            </span>
          </div>
        </div>
      </div>

      <div className="flex items-center gap-3">
        <ThemeToggle />
        {/* Role Switcher */}
        {user.roles.length > 1 && (
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button variant="outline" size="sm" className="gap-2">
                <RoleIcon className="h-4 w-4" />
                <span className="capitalize hidden sm:inline">
                  {currentRole}
                </span>
                <ChevronDown className="h-3 w-3" />
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end" className="w-48">
              <DropdownMenuLabel>Switch Role</DropdownMenuLabel>
              <DropdownMenuSeparator />
              {user.roles.map((role) => {
                const Icon = roleIcons[role];
                return (
                  <DropdownMenuItem
                    key={role}
                    onClick={() => switchRole(role)}
                    className="gap-2 cursor-pointer"
                  >
                    <Icon className="h-4 w-4" />
                    <span className="capitalize">{role}</span>
                    {currentRole === role && (
                      <Badge variant="secondary" className="ml-auto text-xs">
                        Active
                      </Badge>
                    )}
                  </DropdownMenuItem>
                );
              })}
            </DropdownMenuContent>
          </DropdownMenu>
        )}

        {/* Single role badge */}
        {user.roles.length === 1 && (
          <Badge
            variant="outline"
            className={`gap-1.5 ${roleColors[currentRole]}`}
          >
            <RoleIcon className="h-3 w-3" />
            <span className="capitalize">{currentRole}</span>
          </Badge>
        )}

        {/* Notifications */}
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant="ghost" size="icon" className="relative">
              <Bell className="h-5 w-5" />
              {unreadCount > 0 && (
                <span className="absolute -top-1 -right-1 inline-flex items-center justify-center px-1.5 py-0.5 text-xs font-medium leading-none rounded-full bg-destructive text-destructive-foreground">
                  {unreadCount}
                </span>
              )}
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end" className="w-80">
            <DropdownMenuLabel>Notifications</DropdownMenuLabel>
            <div className="max-h-64 overflow-y-auto">
              {notifications.length === 0 && (
                <div className="p-3 text-sm text-muted-foreground">
                  No notifications
                </div>
              )}
              {notifications.map((n) => (
                <DropdownMenuItem
                  key={n.id}
                  className={`flex flex-col items-start gap-1 py-2 ${
                    n.read ? "" : "bg-secondary/5"
                  }`}
                  onClick={async () => {
                    try {
                      await notificationService.markRead(n.id);
                      // update local state to mark as read
                      setNotifications((prev) =>
                        prev.map((p) =>
                          p.id === n.id ? { ...p, read: true } : p
                        )
                      );
                      setUnreadCount((c) => Math.max(0, c - 1));
                      // navigate to task if present
                      if (n.task_id) navigate(`/task/${n.task_id}`);
                    } catch (e) {
                      // ignore
                    }
                  }}
                >
                  <div className="text-sm font-medium">
                    {n.message || "Notification"}
                  </div>
                  <div className="text-xs text-muted-foreground">
                    {n.created_at
                      ? new Date(n.created_at).toLocaleString()
                      : ""}
                  </div>
                </DropdownMenuItem>
              ))}
            </div>
            <DropdownMenuSeparator />
            <div className="px-3 py-2">
              <Button
                variant="ghost"
                size="sm"
                onClick={async () => {
                  await notificationService.markAllRead();
                  await fetchNotificationsOnce(
                    setNotifications,
                    setUnreadCount
                  );
                }}
              >
                Mark all read
              </Button>
            </div>
          </DropdownMenuContent>
        </DropdownMenu>

        {/* User Menu */}
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant="ghost" className="gap-2 px-2">
              <Avatar className="h-8 w-8">
                <AvatarFallback className="bg-primary text-primary-foreground text-sm font-medium">
                  {user.name
                    .split(" ")
                    .map((n) => n[0])
                    .join("")}
                </AvatarFallback>
              </Avatar>
              <div className="hidden md:block text-left">
                <p className="text-sm font-medium leading-none">{user.name}</p>
                <p className="text-xs text-muted-foreground">{user.email}</p>
              </div>
              <ChevronDown className="h-4 w-4 text-muted-foreground hidden md:block" />
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end" className="w-56">
            <DropdownMenuLabel>
              <div className="flex flex-col space-y-1">
                <p className="text-sm font-medium">{user.name}</p>
                <p className="text-xs text-muted-foreground">{user.email}</p>
              </div>
            </DropdownMenuLabel>
            <DropdownMenuSeparator />
            <DropdownMenuItem
              className="gap-2 cursor-pointer"
              onClick={() => navigate("/profile")}
            >
              <User className="h-4 w-4" />
              Profile
            </DropdownMenuItem>
            <DropdownMenuSeparator />
            <DropdownMenuItem
              className="gap-2 cursor-pointer text-destructive focus:text-destructive"
              onClick={logout}
            >
              <LogOut className="h-4 w-4" />
              Sign out
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </div>
    </header>
  );
};

async function fetchNotificationsOnce(
  setNotifications: any,
  setUnreadCount: any
) {
  try {
    const list = await notificationService.listNotifications(false);
    setNotifications(list);
    setUnreadCount(list.filter((n: Notification) => !n.read).length);
  } catch (e) {
    // ignore fetch errors
  }
}

function useNotifications(setNotifications: any, setUnreadCount: any) {
  React.useEffect(() => {
    let mounted = true;
    const fetchNotifications = async () => {
      if (!mounted) return;
      await fetchNotificationsOnce(setNotifications, setUnreadCount);
    };
    fetchNotifications();
    const id = setInterval(fetchNotifications, 30_000);
    return () => {
      mounted = false;
      clearInterval(id);
    };
  }, [setNotifications, setUnreadCount]);
}

// Hook usage inside module scope to avoid linter complaints in component
// We'll call it inside the component render via a function reference

export default Header;
