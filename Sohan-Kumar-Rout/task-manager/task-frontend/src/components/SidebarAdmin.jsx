import React from "react";
import { Link } from "react-router-dom";

const SidebarAdmin = () => {
  return (
    <div className="w-64 bg-[#0F1A2A] text-white min-h-screen p-6">
      <h2 className="text-2xl font-bold mb-8 text-blue-400">Admin Panel</h2>

      <nav className="space-y-4">
        <Link to="/admin/employees" className="block bg-gray-800 p-3 rounded">
          Employees
        </Link>

        <Link to="/admin/employees/create" className="block bg-gray-800 p-3 rounded">
          Create Employee
        </Link>

        <Link to="/admin/tasks" className="block bg-gray-800 p-3 rounded">
          Tasks
        </Link>

        <Link to="/admin/tasks/create" className="block bg-gray-800 p-3 rounded">
          Create Task
        </Link>

        {/* ⭐ NEW: Kanban Board Link */}
        <Link to="/admin/kanban" className="block bg-gray-800 p-3 rounded">
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

export default SidebarAdmin;
