import React from "react";
import { Link } from "react-router-dom";

export default function Sidebar() {
  return (
    <aside className="w-64 bg-white border-r p-4 h-full">
      <nav className="space-y-2">
        <Link
          to="/dashboard"
          className="block px-3 py-2 rounded hover:bg-gray-100"
        >
          Dashboard
        </Link>
        <Link
          to="/employees"
          className="block px-3 py-2 rounded hover:bg-gray-100"
        >
          Employees
        </Link>
        <Link to="/tasks" className="block px-3 py-2 rounded hover:bg-gray-100">
          Tasks
        </Link>
      </nav>
    </aside>
  );
}
