import React from "react";
import { Link } from "react-router-dom";

const Sidebar = () => {
  return (
    <div className="w-64 bg-[#111827] text-white min-h-screen p-6">
      <h2 className="text-2xl font-bold mb-8 text-blue-400">Manager Panel</h2>

      <nav className="space-y-4">
        <Link
          to="/manager/tasks/create"
          className="block bg-[#1F2937] p-3 rounded hover:bg-[#374151]"
        >
          Create Task
        </Link>

        <Link
          to="/manager/tasks"
          className="block bg-[#1F2937] p-3 rounded hover:bg-[#374151]"
        >
          View Tasks
        </Link>

        <Link
          to="/manager/employees"
          className="block bg-[#1F2937] p-3 rounded hover:bg-[#374151]"
        >
          List Employees
        </Link>
      </nav>

      <button
        onClick={() => {
          localStorage.clear();
          window.location.href = "/login";
        }}
        className="mt-10 w-full bg-red-600 p-3 rounded hover:bg-red-700"
      >
        Logout
      </button>
    </div>
  );
};

export default Sidebar;
