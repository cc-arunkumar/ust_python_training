import React, { useState } from "react";
import { Link } from "react-router-dom";
import { FaBars, FaSignOutAlt } from "react-icons/fa";
import KanbanBoard from "./KanbanBoard";
import { FaColumns } from "react-icons/fa";

/* -------------------- Helpers -------------------- */
const NavItem = ({ to, label, emoji, minimized, active }) => (
  <Link
    to={to}
    className={`flex items-center gap-3 p-3 rounded-xl font-medium
    transition-all duration-300
    ${
      active
        ? "bg-white/70 text-[#2A4D69] shadow-md"
        : "bg-[#BFD7ED] hover:bg-[#9BBCE0]"
    }
    hover:shadow-lg hover:scale-[1.03]`}
  >
    {/* Emoji always visible */}
    <span className="text-lg">{emoji}</span>
    {/* Label only when not minimized */}
    {!minimized && <span>{label}</span>}
  </Link>
);

const SidebarEmployee = () => {
  const [isMinimized, setIsMinimized] = useState(false);
  const [isKanbanOpen, setIsKanbanOpen] = useState(false);
  const [user] = useState({
    image:
      "https://img.freepik.com/premium-photo/cute-girl-3d-character-design-cartoon-girl-avatar_432516-5510.jpg?w=2000",
  });

  return (
    <div
      className={`${
        isMinimized ? "w-20" : "w-64"
      } min-h-screen p-4 transition-all duration-500
      bg-gradient-to-b from-[#A7C7E7] to-[#D6EAF8]
      text-gray-900 shadow-xl`}
    >
      {/* Toggle Button */}
      <button
        onClick={() => setIsMinimized(!isMinimized)}
        className="mb-6 w-full flex items-center justify-center
        bg-white/70 p-2 rounded-xl
        hover:bg-white transition
        shadow-md hover:shadow-xl"
      >
        <FaBars size={18} />
      </button>

      {/* Profile Image */}
      <div className="flex justify-center mb-6">
        {user && (
          <img
            src={user.image}
            alt="Profile"
            className="w-16 h-16 rounded-full object-cover border-2 border-white shadow-md"
          />
        )}
      </div>

      {/* Title */}
      {!isMinimized && (
        <h2 className="text-2xl font-bold mb-8 text-[#2A4D69] tracking-wide ml-4">
          Pihoo
        </h2>
      )}

      {/* Navigation */}
      <nav className="space-y-4">
        <NavItem
          to="/employee/tasks"
          label="My Tasks"
          emoji="📝"
          minimized={isMinimized}
          active={window.location.pathname === "/employee/tasks"}
        />
        {/* Quick access to Kanban (opens modal) */}
        <div className="mt-2">
          <button
            onClick={() => setIsKanbanOpen(true)}
            className={`flex items-center gap-3 p-3 rounded-xl font-medium w-full
              transition-all duration-300
              bg-white/70 text-[#2A4D69] shadow-md hover:shadow-lg hover:scale-[1.02]`}
            title="Open Kanban"
          >
            <FaColumns />
            {!isMinimized && <span>Open Kanban</span>}
          </button>
        </div>
      </nav>

      {/* Spacer */}
      <div className="flex-1 mt-10" />

  {/* Logout */}
      <button
        onClick={() => {
          localStorage.clear();
          window.location.href = "/login";
        }}
        className={`w-full flex items-center justify-center gap-2
        bg-gradient-to-r from-[#F4A6A6] to-[#FADADD]
        hover:from-[#E68A8A] hover:to-[#F4A6A6]
        p-3 rounded-xl font-semibold
        transition-all duration-300
        shadow-md hover:shadow-xl hover:scale-[1.03]
        ${isMinimized ? "text-xs" : "text-base"}`}
      >
        <FaSignOutAlt size={16} />
        {!isMinimized && "Logout"}
      </button>
      {/* Kanban modal (opens when employee wants to view/reply) */}
      {isKanbanOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-40" onClick={() => setIsKanbanOpen(false)}>
          <div className="w-full max-w-6xl h-[80vh] bg-white rounded-md overflow-hidden shadow-xl" onClick={(e) => e.stopPropagation()}>
            <div className="flex items-center justify-between p-3 border-b">
              <h3 className="text-lg font-semibold">Kanban Board</h3>
              <button onClick={() => setIsKanbanOpen(false)} className="px-3 py-1 rounded bg-gray-100">Close</button>
            </div>
            <div className="h-full overflow-auto">
              <KanbanBoard />
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default SidebarEmployee;
