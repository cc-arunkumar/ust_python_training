import React, { useEffect } from "react";
import { LogOut, List, Users, Sparkles } from "lucide-react";
import computeRemarkId from "../utils/remarkId";
import { subscribe } from "../utils/events";

function Header({
  role,
  activeTab,
  onTabChange,
  onLogout,
  canManageEmployees,
  canManageUsers,
  onRoleChange,
  onRefresh,
}) {
  const username = localStorage.getItem("username") || "User";
  const storedRolesRaw =
    localStorage.getItem("roles") || localStorage.getItem("role") || "";
  const storedRoles = storedRolesRaw
    .split(",")
    .map((r) => r.trim())
    .filter(Boolean);
  const roles = storedRoles.length ? storedRoles : [role].filter(Boolean);
  const activeRole = localStorage.getItem("role") || role;

  useEffect(() => {
    // Refresh app data when relevant in-app events occur (remarks or generic app updates)
    const handler = (payload) => {
      try {
        onRefresh && onRefresh();
      } catch (e) {}
    };

    const unsubRemarks = subscribe("remarks:updated", handler);
    const unsubApp = subscribe("app:updated", handler);

    // also listen for storage events that indicate read remarks changed in other tabs
    const storageHandler = (ev) => {
      try {
        if (!ev || !ev.key) return;
        if (/^task_\d+_read_remarks$/.test(ev.key)) {
          onRefresh && onRefresh();
        }
      } catch (e) {}
    };
    window.addEventListener("storage", storageHandler);

    return () => {
      try {
        unsubRemarks && unsubRemarks();
      } catch (e) {}
      try {
        unsubApp && unsubApp();
      } catch (e) {}
      try {
        window.removeEventListener("storage", storageHandler);
      } catch (e) {}
    };
  }, [onRefresh]);

  return (
    <header className="bg-white border-b border-gray-200 shadow-sm sticky top-0 z-50 backdrop-blur-lg bg-white/95">
      <div className="container mx-auto flex items-center justify-between py-2.5 px-4">
        {/* Logo Section */}
        <div className="flex items-center gap-3">
          <div className="flex items-center gap-2 group">
            <div className="relative">
              <div className="absolute inset-0 bg-gradient-to-r from-indigo-600 to-purple-600 rounded-lg blur opacity-75 group-hover:opacity-100 transition"></div>
              <div className="relative bg-gradient-to-r from-indigo-600 to-purple-600 p-1.5 rounded-lg">
                <Sparkles className="text-white" size={18} />
              </div>
            </div>
            <div>
              <div className="text-base font-bold bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">
                Jira Lite
              </div>
              <div className="text-[10px] text-gray-500">Task Management</div>
            </div>
          </div>
        </div>

        {/* Navigation */}
        <nav className="flex items-center gap-2">
          <button
            onClick={() => onTabChange("tasks")}
            className={`px-3 py-1.5 rounded-lg font-medium transition-all text-sm ${
              activeTab === "tasks"
                ? "bg-gradient-to-r from-indigo-600 to-purple-600 text-white shadow-md"
                : "hover:bg-gray-100 text-gray-700"
            }`}
          >
            <List size={14} className="inline mr-1.5" />
            Tasks
          </button>

          {canManageEmployees && (
            <button
              onClick={() => onTabChange("employees")}
              className={`px-3 py-1.5 rounded-lg font-medium transition-all text-sm ${
                activeTab === "employees"
                  ? "bg-gradient-to-r from-indigo-600 to-purple-600 text-white shadow-md"
                  : "hover:bg-gray-100 text-gray-700"
              }`}
            >
              <Users size={14} className="inline mr-1.5" />
              Employees
            </button>
          )}

          {canManageUsers && (
            <button
              onClick={() => onTabChange("users")}
              className={`px-3 py-1.5 rounded-lg font-medium transition-all text-sm ${
                activeTab === "users"
                  ? "bg-gradient-to-r from-indigo-600 to-purple-600 text-white shadow-md"
                  : "hover:bg-gray-100 text-gray-700"
              }`}
            >
              <Users size={14} className="inline mr-1.5" />
              Users
            </button>
          )}

          {/* User Info */}
          <div className="ml-3 flex items-center gap-2">
            <div className="flex items-center gap-2 bg-gradient-to-r from-indigo-50 to-purple-50 rounded-lg px-3 py-1.5 border border-indigo-100">
              <div className="flex items-center gap-2">
                <div className="w-7 h-7 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-full flex items-center justify-center text-white font-bold text-xs shadow-sm">
                  {username.charAt(0).toUpperCase()}
                </div>
                <div className="text-left">
                  <div className="text-xs font-semibold text-gray-800">
                    {username}
                  </div>
                  <div className="text-[10px] text-gray-600">
                    {activeRole || "Guest"}
                  </div>
                </div>
              </div>
              {roles.length > 1 && (
                <select
                  value={activeRole}
                  onChange={(e) => {
                    const newRole = e.target.value;
                    localStorage.setItem("role", newRole);
                    onRoleChange && onRoleChange(newRole);
                  }}
                  className="px-2 py-1 rounded-md bg-white text-[10px] border border-indigo-200 text-indigo-700 font-medium hover:border-indigo-300 transition cursor-pointer"
                  title="Switch role"
                >
                  {roles.map((r) => (
                    <option key={r} value={r} className="text-xs">
                      {r}
                    </option>
                  ))}
                </select>
              )}
            </div>

            <button
              onClick={onLogout}
              className="flex items-center gap-1.5 px-3 py-1.5 bg-gray-100 hover:bg-red-50 hover:text-red-600 text-gray-700 rounded-lg transition-all font-medium text-sm"
              title="Logout"
            >
              <LogOut size={14} />
              Logout
            </button>
          </div>
        </nav>
      </div>
    </header>
  );
}

export default Header;
