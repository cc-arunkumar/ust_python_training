import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const SidebarAdmin = () => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // Fetch user data from localStorage or API
    const userData = {
      image: "https://www.bing.com/th/id/OIP.Crq9sn3Qu3HyHwPJi2zW8QHaHa?w=186&h=211&c=8&rs=1&qlt=90&o=6&cb=ucfimg1&pid=3.1&rm=2&ucfimg=1", // Profile image URL
      name: localStorage.getItem("user_name"), // Fetch user name
      role: localStorage.getItem("role"), // Fetch user role
    };
    setUser(userData);
  }, []);

  return (
    <div className="w-64 bg-[#2C3E50] text-white min-h-screen p-6">
      {/* Profile Section */}
      <div className="text-center mb-8">
        {user && (
          <div className="flex flex-col items-center justify-center gap-4 mb-6">
            {/* Profile Image */}
            <img
              src={user.image}
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

      {/* Navigation Links */}
      <nav className="space-y-4">
        <Link to="/admin/employees" className="block p-3 rounded hover:bg-blue-600 transition duration-300">
          Employees
        </Link>

        <Link to="/admin/employees/create" className="block p-3 rounded hover:bg-blue-600 transition duration-300">
          Create Employee
        </Link>

        <Link to="/admin/tasks" className="block p-3 rounded hover:bg-blue-600 transition duration-300">
          Tasks
        </Link>

        <Link to="/admin/tasks/create" className="block p-3 rounded hover:bg-blue-600 transition duration-300">
          Create Task
        </Link>

        <Link to="/admin/kanban" className="block p-3 rounded hover:bg-blue-600 transition duration-300">
          Kanban Board
        </Link>
      </nav>

      {/* Logout Button */}
      <button
        onClick={() => {
          localStorage.clear();
          window.location.href = "/login";
        }}
        className="mt-10 w-full bg-red-600 p-3 rounded hover:bg-red-700 transition duration-300"
      >
        Logout
      </button>
    </div>
  );
};

export default SidebarAdmin;
