import React from "react";
import { Link } from "react-router-dom";

const SidebarEmployee = () => {
  return (
    <div className="w-64 bg-[#0F1A2A] text-white min-h-screen p-6">
      <h2 className="text-2xl font-bold mb-8 text-blue-400">Employee Panel</h2>

      <nav className="space-y-4">
        <Link to="/employee/tasks" className="block bg-gray-800 p-3 rounded">
          My Tasks
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

export default SidebarEmployee;
