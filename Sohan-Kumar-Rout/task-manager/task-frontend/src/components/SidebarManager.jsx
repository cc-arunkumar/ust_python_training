import React, { useState } from "react";
import { Link } from "react-router-dom";
import { FaBars } from "react-icons/fa"; // hamburger icon

const SidebarManager = () => {
  const [isMinimized, setIsMinimized] = useState(false);

  return (
    <div
      className={`${
        isMinimized ? "w-20" : "w-64"
      } bg-[#0F1A2A] text-white min-h-screen p-4 transition-all duration-300`}
    >
      {/* Toggle button */}
      <button
        onClick={() => setIsMinimized(!isMinimized)}
        className="mb-6 w-full flex items-center justify-center bg-gray-700 p-2 rounded"
      >
        <FaBars size={20} />
      </button>

      {/* Sidebar content */}
      <h2
        className={`text-2xl font-bold mb-8 text-blue-400 ${
          isMinimized ? "hidden" : "block"
        }`}
      >
        Manager Panel
      </h2>

      <nav className="space-y-4">
        <Link
          to="/manager/dashboard"
          className="block bg-gray-800 p-3 rounded text-center"
        >
          {isMinimized ? "🏠" : "Dashboard"}
        </Link>

        <Link
          to="/manager/kanban"
          className="block bg-gray-800 p-3 rounded text-center"
        >
          {isMinimized ? "📋" : "Kanban Board"}
        </Link>
      </nav>

      {/* Logout button */}
      <button
        onClick={() => {
          localStorage.clear();
          window.location.href = "/login";
        }}
        className={`mt-10 w-full bg-red-600 p-3 rounded ${
          isMinimized ? "text-xs" : "text-base"
        }`}
      >
        {isMinimized ? "⏻" : "Logout"}
      </button>
    </div>
  );
};

export default SidebarManager;
