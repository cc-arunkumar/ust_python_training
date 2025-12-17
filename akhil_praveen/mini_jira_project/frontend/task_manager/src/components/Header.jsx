import React from "react";
import { LogOut, List, Users } from "lucide-react";

function Header({
  role,
  activeTab,
  onTabChange,
  onLogout,
  canManageEmployees,
  onRoleChange,
}) {
  const username = localStorage.getItem("username") || "User";
  // roles are stored under 'roles' as comma-separated list; active role stored under 'role'
  const storedRolesRaw =
    localStorage.getItem("roles") || localStorage.getItem("role") || "";
  const storedRoles = storedRolesRaw
    .split(",")
    .map((r) => r.trim())
    .filter(Boolean);
  const roles = storedRoles.length ? storedRoles : [role].filter(Boolean);
  const activeRole = localStorage.getItem("role") || role;

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

          <div className="ml-4 text-sm mr-4 opacity-90 flex items-center gap-3">
            <div className="flex items-center gap-3 bg-white/90 text-indigo-900 rounded-md px-3 py-1 shadow-sm">
              <div className="text-left">
                <div className="text-xs opacity-80">{username}</div>
                <div className="font-medium text-sm">
                  {activeRole || "Guest"}
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
                  className="px-2 py-1 rounded bg-white text-xs border text-indigo-700"
                  title="Switch role"
                >
                  {roles.map((r) => (
                    <option key={r} value={r} className="text-sm">
                      {r}
                    </option>
                  ))}
                </select>
              )}
            </div>
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
