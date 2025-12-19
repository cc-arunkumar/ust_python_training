import React, { useState } from "react";
import { Link } from "react-router-dom";
import { FaBars, FaSignOutAlt, FaUsers, FaUserPlus, FaTasks, FaPlusSquare, FaColumns } from "react-icons/fa";

const NavItem = ({ to, label, icon, minimized, active }) => (
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
    {/* Icon always visible */}
    <span className="text-lg">{icon}</span>
    {/* Label only when not minimized */}
    {!minimized && <span>{label}</span>}
  </Link>
);

const SidebarAdmin = () => {
  const [isMinimized, setIsMinimized] = useState(false);
  const [user] = useState({
    image:
      "https://tse2.mm.bing.net/th/id/OIP.RCWlu9of5SqQXSJ8hTxkEwHaHa?cb=ucfimg2&ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3",
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
          Admin
        </h2>
      )}

      {/* Navigation */}
      <nav className="space-y-4">
        <NavItem
          to="/admin/employees"
          label="Employees"
          icon={<FaUsers size={18} />}
          minimized={isMinimized}
          active={window.location.pathname === "/admin/employees"}
        />
        <NavItem
          to="/admin/employees/create"
          label="Create Employee"
          icon={<FaUserPlus size={18} />}
          minimized={isMinimized}
          active={window.location.pathname === "/admin/employees/create"}
        />
        <NavItem
          to="/admin/tasks"
          label="Tasks"
          icon={<FaTasks size={18} />}
          minimized={isMinimized}
          active={window.location.pathname === "/admin/tasks"}
        />
        <NavItem
          to="/admin/tasks/create"
          label="Create Task"
          icon={<FaPlusSquare size={18} />}
          minimized={isMinimized}
          active={window.location.pathname === "/admin/tasks/create"}
        />
        <NavItem
          to="/admin/kanban"
          label="Kanban Board"
          icon={<FaColumns size={18} />}
          minimized={isMinimized}
          active={window.location.pathname === "/admin/kanban"}
        />
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
    </div>
  );
};

export default SidebarAdmin;
