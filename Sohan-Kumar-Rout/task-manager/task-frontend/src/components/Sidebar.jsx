import React from "react";
import { Link } from "react-router-dom";

const Sidebar = () => {
  return (
    <div className="
      w-64 min-h-screen p-6 
      bg-white text-black 
      dark:bg-gray-900 dark:text-white 
      border-r border-gray-300 dark:border-gray-700
      transition-all duration-300
    ">
      <h2 className="text-2xl font-bold mb-8 text-blue-600 dark:text-blue-400">
        Manager Panel
      </h2>

      <nav className="space-y-4">
        <Link
          to="/manager/tasks/create"
          className="block p-3 rounded 
            bg-gray-200 dark:bg-gray-800 
            hover:bg-gray-300 dark:hover:bg-gray-700 
            transition"
        >
          Create Task
        </Link>

        <Link
          to="/manager/tasks"
          className="block p-3 rounded 
            bg-gray-200 dark:bg-gray-800 
            hover:bg-gray-300 dark:hover:bg-gray-700 
            transition"
        >
          View Tasks
        </Link>

        <Link
          to="/manager/employees"
          className="block p-3 rounded 
            bg-gray-200 dark:bg-gray-800 
            hover:bg-gray-300 dark:hover:bg-gray-700 
            transition"
        >
          List Employees
        </Link>
      </nav>

      <button
        onClick={() => {
          localStorage.clear();
          window.location.href = "/login";
        }}
        className="mt-10 w-full bg-red-600 p-3 rounded hover:bg-red-700 text-white"
      >
        Logout
      </button>
    </div>
  );
};

export default Sidebar;
