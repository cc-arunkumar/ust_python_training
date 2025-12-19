import React, { useEffect, useState } from "react";
import { Link, useLocation } from "react-router-dom";
import { FiUsers, FiClipboard, FiPlusSquare, FiLayout, FiLogOut, FiChevronLeft } from "react-icons/fi";
import { getMyProfile } from "../services/employeeService";

const SidebarManager = () => {
  const [user, setUser] = useState(null);
  const [collapsed, setCollapsed] = useState(false);
  const location = useLocation();

  useEffect(() => {
    const init = async () => {
      const nameFromStorage = localStorage.getItem("user_name");
      const image = "https://img.freepik.com/premium-photo/3d-avatar-cartoon-character_113255-95871.jpg";

      if (nameFromStorage) {
        setUser({ name: nameFromStorage, image });
        return;
      }

      // try fetching from backend
      try {
        const profile = await getMyProfile();
        setUser({ name: profile.name, image });
      } catch (err) {
        // fallback to emp_id
        setUser({ name: localStorage.getItem("emp_id"), image });
      }
    };

    init();
  }, []);

  const navItems = [
    { to: "/manager/dashboard", label: "Dashboard", icon: <FiLayout /> },
    // removed Tasks and Create Task per request
    { to: "/manager/kanban", label: "Kanban Board", icon: <FiLayout /> },
    // removed Employees link from manager sidebar per request
  ];

  return (
  <aside className={`${collapsed ? 'w-20' : 'w-72'} bg-gray-700 text-gray-100 border-r border-gray-600 min-h-screen p-4 flex flex-col justify-between transition-all duration-300`}>
      <div>
        <div className="flex items-center gap-3 mb-6 justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-indigo-600 to-purple-600 flex items-center justify-center text-white font-bold">TM</div>
            {!collapsed && (
              <div>
                <div className="text-lg font-semibold">Task Manager</div>
                <div className="text-xs text-gray-400">Manager Console</div>
              </div>
            )}
          </div>

          <button onClick={() => setCollapsed(!collapsed)} className="p-2 rounded bg-gray-800 hover:bg-gray-700 transition">
            <FiChevronLeft className={`transform transition ${collapsed ? 'rotate-180' : ''}`} />
          </button>
        </div>

        {user && (
          <div className={`flex items-center gap-3 p-3 rounded-md ${collapsed ? 'bg-transparent' : 'bg-gray-600'} mb-6`}>
            <img src={user.image} alt="Profile" className="w-10 h-10 rounded-full object-cover" />
            {!collapsed && (
              <div>
                <div className="font-medium text-gray-100">{user.name || 'User'}</div>
              </div>
            )}
          </div>
        )}

        <nav className="space-y-2">
          {navItems.map((item) => {
            const active = location.pathname === item.to;
            return (
              <Link key={item.to} to={item.to} className={`flex items-center gap-3 p-3 rounded-md transition-all duration-200 ${active ? 'bg-indigo-700 text-white' : 'text-gray-300 hover:bg-gray-800 hover:text-white'}`}>
                <div className="text-xl">{item.icon}</div>
                {!collapsed && <div className="text-sm font-medium">{item.label}</div>}
              </Link>
            );
          })}
        </nav>
      </div>

      <div>
        <button
          onClick={() => {
            localStorage.clear();
            window.location.href = "/login";
          }}
          className={`w-full flex items-center gap-2 justify-center px-4 py-2 rounded-md text-white bg-red-600 hover:bg-red-700 transition ${collapsed ? 'text-xs' : 'text-base'}`}
        >
          <FiLogOut />
          {!collapsed && <span>Logout</span>}
        </button>
      </div>
    </aside>
  );
};

export default SidebarManager;
