import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { FaBars, FaCaretDown, FaCaretUp, FaUsers } from "react-icons/fa"; // hamburger icon and toggle icons
import { getEmployees } from "../services/employeeService"; // Assuming you have this service

const SidebarManager = () => {
  const [isMinimized, setIsMinimized] = useState(false);
  const [employees, setEmployees] = useState([]);
  const [isEmployeeSectionOpen, setIsEmployeeSectionOpen] = useState(false);
  const [user, setUser] = useState(null); // User data (profile image, name, role)

  useEffect(() => {
    const loadEmployees = async () => {
      try {
        const eRes = await getEmployees();
        const eData = Array.isArray(eRes) ? eRes : eRes?.data || [];
        setEmployees(eData);
      } catch (error) {
        console.error("Error loading employees", error);
      }
    };

    // Load user profile data from localStorage
    const userData = {
      image: "https://www.bing.com/th/id/OIP.Crq9sn3Qu3HyHwPJi2zW8QHaHa?w=186&h=211&c=8&rs=1&qlt=90&o=6&cb=ucfimg1&pid=3.1&rm=2&ucfimg=1", // Direct image URL
      name: localStorage.getItem("user_name"), // Fetch user name
      role: localStorage.getItem("role"), // Fetch user role
    };
    setUser(userData);

    loadEmployees();
  }, []);

  return (
    <div
      className={`${
        isMinimized ? "w-20" : "w-64"
      } bg-[#2C3E50] text-white min-h-screen p-4 transition-all duration-300`}
    >
      {/* Profile Section */}
      <div className="text-center mb-8">
        {user && (
          <div className="flex flex-col items-center justify-center gap-4 mb-6">
            {/* Profile Image */}
            <img
              src={user.image} // Direct image URL
              alt="Profile"
              className="w-16 h-16 rounded-full object-cover"
            />
            {/* User Role */}
            <div>
              <p className="font-semibold text-lg">{user.name}</p>
              <p className="text-sm text-gray-300">{user.role}</p>
            </div>
          </div>
        )}
      </div>

      {/* Toggle button */}
      <button
        onClick={() => setIsMinimized(!isMinimized)}
        className="mb-6 w-full flex items-center justify-center bg-gray-700 p-2 rounded"
      >
        <FaBars size={20} />
      </button>

      {/* Sidebar content */}
      <h2
        className={`text-2xl font-bold mb-8 text-blue-400 ${isMinimized ? "hidden" : "block"}`}
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

      {/* Collapsible Employee Section */}
      <div className="mt-6 bg-[#1e2a3b] p-4 rounded-lg">
        <div
          className="flex justify-between items-center cursor-pointer"
          onClick={() => setIsEmployeeSectionOpen(!isEmployeeSectionOpen)}
        >
          {/* Show only logo/icon when minimized */}
          {isMinimized ? (
            <FaUsers size={20} className="text-white" />
          ) : (
            <h3 className="text-xl font-semibold text-white">Employees</h3>
          )}
          {isEmployeeSectionOpen ? (
            <FaCaretUp size={20} className="text-white" />
          ) : (
            <FaCaretDown size={20} className="text-white" />
          )}
        </div>

        {isEmployeeSectionOpen && !isMinimized && (
          <table className="w-full text-sm text-left text-gray-400 mt-4">
            <thead className="bg-gray-600">
              <tr>
                <th className="px-3 py-2">Name</th>
                <th className="px-3 py-2">Status</th>
              </tr>
            </thead>
            <tbody>
              {employees.length > 0 ? (
                employees.map((emp) => (
                  <tr key={emp.id} className="border-b border-gray-700">
                    <td className="px-3 py-2">{emp.name}</td>
                    <td className="px-3 py-2">{emp.status || "Active"}</td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="2" className="text-center py-3">No employees found</td>
                </tr>
              )}
            </tbody>
          </table>
        )}
      </div>

      {/* Logout button */}
      <button
        onClick={() => {
          localStorage.clear();
          window.location.href = "/login";
        }}
        className={`mt-10 w-full bg-red-600 p-3 rounded ${isMinimized ? "text-xs" : "text-base"}`}
      >
        {isMinimized ? "⏻" : "Logout"}
      </button>
    </div>
  );
};

export default SidebarManager;
