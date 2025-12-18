import React, { useState, useEffect } from "react";
import { Link, useLocation } from "react-router-dom";
import {
  FaBars,
  FaHome,
  FaTasks,
  FaSignOutAlt,
} from "react-icons/fa";

/* -------------------- Helpers -------------------- */
const NavItem = ({ to, icon: Icon, label, minimized, active }) => (
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
    <Icon size={18} />
    {!minimized && <span>{label}</span>}
  </Link>
);

/* -------------------- Sidebar -------------------- */
const SidebarManager = () => {
  const [isMinimized, setIsMinimized] = useState(false);
  const [user, setUser] = useState(null);
  const { pathname } = useLocation();

  useEffect(() => {
    const userData = {
      image:
        "https://img.freepik.com/premium-photo/3d-illustration-cartoon-character-avatar-profile_1183071-136.jpg?w=740",
    };
    setUser(userData);
  }, []);

  return (
    <div
      className={`${
        isMinimized ? "w-20" : "w-64"
      } min-h-screen p-4 transition-all duration-500
      bg-gradient-to-b from-[#A7C7E7] to-[#D6EAF8]
      text-gray-900 shadow-xl`}
    >
            {/* Toggle */}
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
<h2
  className="text-2xl font-bold mb-8 text-[#2A4D69] tracking-wide ml-4"
>
  Manager
</h2>

      )}

      {/* Navigation */}
      <nav className="space-y-4">
        <NavItem
          to="/manager/dashboard"
          icon={FaHome}
          label="Dashboard"
          minimized={isMinimized}
          active={pathname === "/manager/dashboard"}
        />

        <NavItem
          to="/manager/kanban"
          icon={FaTasks}
          label="Kanban Board"
          minimized={isMinimized}
          active={pathname === "/manager/kanban"}
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

export default SidebarManager;
