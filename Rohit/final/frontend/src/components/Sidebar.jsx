import { useState } from "react";
import { NavLink } from "react-router-dom";
import {
  ChevronLeftIcon,
  ChevronRightIcon,
  HomeIcon,
  ClipboardDocumentListIcon,
  UsersIcon,
} from "@heroicons/react/24/solid";

export default function Sidebar() {
  const [collapsed, setCollapsed] = useState(false);

  const linkClass = ({ isActive }) =>
    `flex items-center gap-3 px-4 py-2 rounded-lg transition-all duration-200 text-base font-medium ${
      isActive
        ? "bg-gradient-to-r from-cyan-500 to-blue-600 text-white shadow-md"
        : "text-gray-300 hover:bg-gradient-to-r hover:from-slate-700 hover:to-slate-800 hover:text-cyan-300"
    }`;

  return (
    <div
      className={`h-screen bg-gradient-to-b from-slate-900 via-slate-800 to-slate-900 text-white flex flex-col transition-all duration-300 ${
        collapsed ? "w-20" : "w-64"
      }`}
    >
      {/* Header with toggle button */}
      <div className="flex items-center justify-between p-4 border-b border-slate-700">
        {!collapsed && (
          <div className="text-2xl font-extrabold tracking-wide text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-500">
            Jira Lite
          </div>
        )}
        <button
          onClick={() => setCollapsed(!collapsed)}
          className="text-gray-400 hover:text-cyan-300 focus:outline-none transition-colors"
        >
          {collapsed ? (
            <ChevronRightIcon className="h-6 w-6" />
          ) : (
            <ChevronLeftIcon className="h-6 w-6" />
          )}
        </button>
      </div>

      {/* Navigation */}
      <nav className="flex-1 space-y-2 mt-4">
        <NavLink to="/" className={linkClass}>
          <HomeIcon className="h-6 w-6" />
          {!collapsed && "Dashboard"}
        </NavLink>
        <NavLink to="/tasks" className={linkClass}>
          <ClipboardDocumentListIcon className="h-6 w-6" />
          {!collapsed && "Tasks"}
        </NavLink>
        <NavLink to="/users" className={linkClass}>
          <UsersIcon className="h-6 w-6" />
          {!collapsed && "Users"}
        </NavLink>
      </nav>

      {/* Footer */}
      {!collapsed && (
        <div className="p-4 text-xs text-gray-400 border-t border-slate-700">
          v1.0
        </div>
      )}
    </div>
  );
}
