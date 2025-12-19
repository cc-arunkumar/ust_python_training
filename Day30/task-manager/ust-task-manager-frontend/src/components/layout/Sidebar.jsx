import { NavLink } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";
import { LayoutDashboard, CheckSquare, Users, LogOut } from "lucide-react";

function Sidebar() {
  const { user, logout } = useAuth();

  const navItems = [
    {
      name: "Dashboard",
      path: "/dashboard",
      icon: <LayoutDashboard size={20} />,
      roles: ["admin", "manager", "employee"],
    },
    {
      name: "Tasks",
      path: "/tasks",
      icon: <CheckSquare size={20} />,
      roles: ["admin", "manager", "employee"],
    },
    {
      name: "Employees",
      path: "/employees",
      icon: <Users size={20} />,
      roles: ["admin", "manager"],
    },
  ];

  return (
    <div className="w-64 bg-slate-900 text-white h-full flex flex-col shadow-xl">
      {/* Logo Area */}
      <div className="h-16 flex items-center px-6 border-b border-slate-700 bg-slate-950">
        <div className="w-8 h-8 bg-blue-500 rounded-lg flex items-center justify-center mr-3 font-bold text-xl">
          U
        </div>
        <span className="font-bold text-lg tracking-wide">Jira Lite</span>
      </div>

      {/* Navigation */}
      <nav className="flex-1 py-6 px-3 space-y-1">
        {navItems.map(
          (item) =>
            item.roles.includes(user?.role) && (
              <NavLink
                key={item.path}
                to={item.path}
                className={({ isActive }) =>
                  `flex items-center gap-3 px-4 py-3 rounded-lg transition-all duration-200 group ${
                    isActive
                      ? "bg-blue-600 text-white shadow-md"
                      : "text-slate-400 hover:bg-slate-800 hover:text-white"
                  }`
                }
              >
                {item.icon}
                <span className="font-medium">{item.name}</span>
              </NavLink>
            )
        )}
      </nav>

      {/* User Profile Snippet */}
      <div className="p-4 border-t border-slate-700 bg-slate-950">
        <div className="flex items-center gap-3 mb-3">
          <div className="w-10 h-10 rounded-full bg-gradient-to-tr from-blue-500 to-purple-600 flex items-center justify-center font-bold text-white">
            {user?.role?.charAt(0).toUpperCase()}
          </div>
          <div>
            <p className="text-sm font-semibold text-white capitalize">
              {user?.role}
            </p>
            <p className="text-xs text-slate-400">ID: {user?.emp_id}</p>
          </div>
        </div>
        <button
          onClick={logout}
          className="w-full flex items-center justify-center gap-2 bg-red-500/10 text-red-400 hover:bg-red-500 hover:text-white py-2 rounded-md transition-all text-sm font-medium"
        >
          <LogOut size={16} /> Logout
        </button>
      </div>
    </div>
  );
}

export default Sidebar;
