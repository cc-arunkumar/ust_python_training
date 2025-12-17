import React from "react";
import {
  LayoutDashboard,
  Plus,
  FileText,
  Users,
  TrendingUp,
  LogOut,
  Menu,
} from "lucide-react";
import { USER_ROLES } from "../utils/constants";

const Sidebar = ({ user, isOpen, onToggle, onCreateTask, onLogout }) => {
  const sidebarItems = [
    {
      icon: LayoutDashboard,
      label: "Dashboard",
      roles: [USER_ROLES.ADMIN, USER_ROLES.MANAGER, USER_ROLES.DEVELOPER],
    },
    {
      icon: Plus,
      label: "Create Task",
      roles: [USER_ROLES.ADMIN, USER_ROLES.MANAGER],
      onClick: onCreateTask,
    },
    {
      icon: FileText,
      label: "All Tasks",
      roles: [USER_ROLES.ADMIN, USER_ROLES.MANAGER, USER_ROLES.DEVELOPER],
    },
    {
      icon: Users,
      label: "Team",
      roles: [USER_ROLES.ADMIN, USER_ROLES.MANAGER],
    },
    {
      icon: TrendingUp,
      label: "Analytics",
      roles: [USER_ROLES.ADMIN, USER_ROLES.MANAGER],
    },
  ];

  const filteredSidebarItems = sidebarItems.filter((item) =>
    item.roles.includes(user.role)
  );

  return (
    <div
      className={`${
        isOpen ? "w-64" : "w-20"
      } bg-white border-r border-gray-200 transition-all duration-300 flex flex-col`}
    >
      {/* Header */}
      <div className="p-6 border-b border-gray-200">
        <div className="flex items-center justify-between">
          {isOpen && (
            <div>
              <h2 className="text-xl font-bold text-gray-900">TaskFlow</h2>
              <p className="text-xs text-gray-500 mt-1">
                {user.role.toUpperCase()}
              </p>
            </div>
          )}
          <button
            onClick={onToggle}
            className="p-2 hover:bg-gray-100 rounded-lg"
          >
            <Menu className="w-5 h-5" />
          </button>
        </div>
      </div>

      {/* Navigation */}
      <div className="flex-1 py-6">
        <nav className="space-y-2 px-3">
          {filteredSidebarItems.map((item, index) => (
            <button
              key={index}
              onClick={item.onClick}
              className="w-full flex items-center gap-3 px-3 py-3 text-gray-700 hover:bg-blue-50 hover:text-blue-600 rounded-lg transition-colors"
            >
              <item.icon className="w-5 h-5 flex-shrink-0" />
              {isOpen && <span className="font-medium">{item.label}</span>}
            </button>
          ))}
        </nav>
      </div>

      {/* User Profile & Logout */}
      <div className="p-4 border-t border-gray-200">
        <div
          className={`${
            isOpen
              ? "flex items-center gap-3"
              : "flex flex-col items-center gap-2"
          } mb-4`}
        >
          <div className="w-10 h-10 bg-gradient-to-br from-blue-600 to-purple-600 rounded-full flex items-center justify-center text-white font-semibold">
            {user.name.charAt(0).toUpperCase()}
          </div>
          {isOpen && (
            <div className="flex-1 min-w-0">
              <p className="font-semibold text-gray-900 truncate">
                {user.name}
              </p>
              <p className="text-xs text-gray-500">ID: {user.emp_id}</p>
            </div>
          )}
        </div>
        <button
          onClick={onLogout}
          className="w-full flex items-center justify-center gap-2 px-4 py-2 bg-red-50 text-red-600 rounded-lg hover:bg-red-100 transition-colors"
        >
          <LogOut className="w-4 h-4" />
          {isOpen && <span className="font-medium">Logout</span>}
        </button>
      </div>
    </div>
  );
};

export default Sidebar;
