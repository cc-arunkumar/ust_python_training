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

      {/* Admin Section */}
      <div className="mb-6">
        <h3 className="text-lg font-semibold mb-2 text-gray-300">Admin</h3>
        <NavLink
          to="/"
          className={({ isActive }) =>
            isActive ? activeClasses : linkClasses
          }
        >
          Dashboard
        </NavLink>
      </div>

      {/* Manager Section */}
      <div className="mb-6">
        <h3 className="text-lg font-semibold mb-2 text-gray-300">Manager</h3>

        <NavLink
          to="/managers"
          className={({ isActive }) =>
            isActive ? activeClasses : linkClasses
          }
        >
          View Managers
        </NavLink>

        <NavLink
          to="/managers/add"
          className={({ isActive }) =>
            isActive ? activeClasses : linkClasses
          }
        >
          Add Manager
        </NavLink>
      </div>

      {/* Employee Section */}
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

        <NavLink
          to="/employees/add"
          className={({ isActive }) =>
            isActive ? activeClasses : linkClasses
          }
        >
          Add Employee
        </NavLink>
      </div>
    </div>
  );
};

export default Sidebar;
