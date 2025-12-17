import React from "react";
import { Link } from "react-router-dom";

const SidebarManager = () => {
  return (
    <div className="w-64 bg-[#0F1A2A] text-white min-h-screen p-6">
      <h2 className="text-2xl font-bold mb-8 text-blue-400">Manager Panel</h2>

      <nav className="space-y-4">
        <Link to="/manager/tasks/create" className="block bg-gray-800 p-3 rounded">
          Create Task
        </Link>

        <Link to="/manager/tasks" className="block bg-gray-800 p-3 rounded">
          View Tasks
        </Link>

        <Link to="/manager/employees" className="block bg-gray-800 p-3 rounded">
          Employees Under Me
        </Link>

        {/* ⭐ NEW: Kanban Board Link */}
        <Link to="/manager/kanban" className="block bg-gray-800 p-3 rounded">
          Kanban Board
        </Link>
      </nav>

      <button
        onClick={() => {
          localStorage.clear();
          window.location.href = "/login";
        }}
        className="mt-10 w-full bg-red-600 p-3 rounded"
      >
        Logout
      </button>
    </div>
  );
};

export default SidebarManager;
