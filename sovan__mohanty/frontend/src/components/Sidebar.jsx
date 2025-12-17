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
    `flex items-center gap-2 px-4 py-2 rounded transition-colors duration-200 text-lg ${
      isActive
        ? "bg-gray-700 text-white dark:bg-gray-600 dark:text-gray-100"
        : "text-gray-200 hover:bg-gray-700 dark:text-gray-300 dark:hover:bg-gray-700"
    }`;

  return (
    <div
      className={`h-screen bg-gray-800 dark:bg-gray-900 text-white flex flex-col transition-all duration-300 ${
        collapsed ? "w-16" : "w-64"
      }`}
    >
      {/* Header with toggle button */}
      <div className="flex items-center justify-between p-4">
        {!collapsed && (
          <div className="text-2xl font-bold text-gray-100 dark:text-gray-200">
            Jira Lite
          </div>
        )}
        <button
          onClick={() => setCollapsed(!collapsed)}
          className="text-gray-300 hover:text-white focus:outline-none"
        >
          {collapsed ? (
            <ChevronRightIcon className="h-6 w-6" />
          ) : (
            <ChevronLeftIcon className="h-6 w-6" />
          )}
        </button>
      </div>

      {/* Navigation */}
      <nav className="flex-1 space-y-1">
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
        <div className="p-4 text-sm text-gray-400 dark:text-gray-500">v1.0</div>
      )}
    </div>
  );
}
