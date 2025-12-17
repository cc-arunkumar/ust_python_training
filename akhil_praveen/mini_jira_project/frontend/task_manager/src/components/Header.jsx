import React from "react";
import { LogOut, List, Users } from "lucide-react";

function Header({
  role,
  activeTab,
  onTabChange,
  onLogout,
  canManageEmployees,
}) {
  return (
    <header className="bg-gradient-to-r from-indigo-600 to-purple-600 text-white shadow-md">
      <div className="container mx-auto flex items-center justify-between py-4 px-6">
        <div className="flex items-center gap-3">
          <div className="text-xl font-semibold">Mini Jira</div>
          <div className="text-sm opacity-90">Task management simplified</div>
        </div>

        <nav className="flex items-center gap-3">
          <button
            onClick={() => onTabChange("tasks")}
            className={`px-4 py-2 rounded-md font-medium transition ${
              activeTab === "tasks"
                ? "bg-white text-indigo-600"
                : "hover:bg-white/10"
            }`}
          >
            Tasks
          </button>

          {canManageEmployees && (
            <button
              onClick={() => onTabChange("employees")}
              className={`px-4 py-2 rounded-md font-medium transition ${
                activeTab === "employees"
                  ? "bg-white text-indigo-600"
                  : "hover:bg-white/10"
              }`}
            >
              <Users size={14} className="inline mr-2" /> Employees
            </button>
          )}

          <div className="ml-4 text-sm mr-4 opacity-90">
            <div className="text-xs">Role</div>
            <div className="font-medium">{role || "Guest"}</div>
          </div>

          <button
            onClick={onLogout}
            className="flex items-center gap-2 px-3 py-2 bg-white/20 hover:bg-white/30 rounded-md"
            title="Logout"
          >
            <LogOut /> Logout
          </button>
        </nav>
      </div>
    </header>
  );
}

export default Header;
