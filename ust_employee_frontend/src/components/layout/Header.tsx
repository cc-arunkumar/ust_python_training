import React from "react";
import { useAuth } from "@/contexts/AuthContext";
import { Shield, Users, Code2, LogOut, LayoutDashboard } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { useNavigate, useLocation } from "react-router-dom";

type ViewMode = "admin" | "manager" | "employee";

interface HeaderProps {
  currentView: ViewMode;
  onViewChange: (view: ViewMode) => void;
}

const Header: React.FC<HeaderProps> = ({ currentView, onViewChange }) => {
  const { user, logout, isAdmin, isManager } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

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

  return (
    <header className="sticky top-0 z-50 w-full border-b border-border bg-card/95 backdrop-blur supports-[backdrop-filter]:bg-card/60">
      <div className="flex h-16 items-center justify-between px-6">
        <div className="flex items-center gap-6">
          <div className="flex items-center gap-3">
            <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-primary">
              <LayoutDashboard className="h-5 w-5 text-primary-foreground" />
            </div>
            <div>
              <h1 className="text-lg font-semibold text-foreground">
                UST Task Manager
              </h1>
              <p className="text-xs text-muted-foreground">
                Employee Management System
              </p>
            </div>
          </div>

          <nav className="hidden md:flex items-center gap-2 ml-8">
            {isAdmin && (
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
            {(isAdmin || isManager) && (
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
          </nav>
        </div>

        <div className="flex items-center gap-4">
          <div className="hidden sm:flex flex-col items-end">
            <span className="text-sm font-medium text-foreground">
              {user?.employee?.name}
            </span>
            <span className="text-xs text-muted-foreground capitalize">
              {user?.role.join(", ")}
            </span>
          </div>
          <Avatar className="h-9 w-9 border-2 border-primary/20">
            <AvatarFallback className="bg-primary/10 text-primary text-sm font-semibold">
              {user?.employee?.name ? getInitials(user.employee.name) : "U"}
            </AvatarFallback>
          </Avatar>
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
    </header>
  );
};

export default Header;
