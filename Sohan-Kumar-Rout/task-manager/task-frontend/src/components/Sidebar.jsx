import React from "react";
import { NavLink } from "react-router-dom";

const Sidebar = () => {
  const linkClasses =
    "block p-2 rounded hover:bg-[#2A3244] transition";
  const activeClasses =
    "block p-2 rounded bg-blue-600 text-white";

  return (
    <div className="w-64 h-screen bg-[#1F2635] text-white p-6 shadow-lg">
      <h2 className="text-2xl font-bold mb-8 text-blue-400">Admin Panel</h2>

      {/* ADMIN SECTION */}
      <div className="mb-6">
        <h3 className="text-lg font-semibold mb-2 text-gray-300">Admin</h3>

        <NavLink
          to="/employees/add"
          className={({ isActive }) =>
            isActive ? activeClasses : linkClasses
          }
        >
          Create Employee
        </NavLink>

        <NavLink
          to="/tasks/create"
          className={({ isActive }) =>
            isActive ? activeClasses : linkClasses
          }
        >
          Create Task
        </NavLink>

        <NavLink
          to="/tasks"
          className={({ isActive }) =>
            isActive ? activeClasses : linkClasses
          }
        >
          View Tasks
        </NavLink>
      </div>

      {/* EMPLOYEE SECTION */}
      <div>
        <h3 className="text-lg font-semibold mb-2 text-gray-300">Employee</h3>

        <NavLink
          to="/employees"
          className={({ isActive }) =>
            isActive ? activeClasses : linkClasses
          }
        >
          View Employees
        </NavLink>
      </div>
    </div>
  );
};

export default Sidebar;
