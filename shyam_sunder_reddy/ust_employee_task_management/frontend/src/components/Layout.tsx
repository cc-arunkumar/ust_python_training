import React, { useEffect, useState } from "react";
import { Outlet, useNavigate, useLocation } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import {
  CheckSquare,
  Users,
  UserCog,
  LogOut,
  Menu,
  X,
  ChevronLeft,
  ChevronRight,
} from "lucide-react";
import { employeeAPI } from "../services/api";

const Layout: React.FC = () => {
  const { user, logout, activeRole, setActiveRole } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [employeeName, setEmployeeName] = useState<string | null>(null);
  const [collapsed, setCollapsed] = useState(false);

  useEffect(() => {
    let mounted = true;
    const userId = (user as any)?.e_id ?? (user as any)?.id;
    if (!userId) return;
    employeeAPI
      .getById(userId, activeRole || "")
      .then((emp) => {
        if (!mounted) return;
        if (emp && (emp as any).name) setEmployeeName((emp as any).name);
      })
      .catch(() => {});
    return () => {
      mounted = false;
    };
  }, [(user as any)?.e_id, activeRole]);

  const menuItems = [
    { icon: CheckSquare, label: "Tasks", path: "/tasks" },
    { icon: Users, label: "Employees", path: "/employees" },
    { icon: UserCog, label: "Users", path: "/users" },
  ];

  const isActive = (path: string) => location.pathname === path;

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  const rolesArray = React.useMemo(() => {
    const r = (user as any)?.role;
    if (!r) return [] as string[];
    if (Array.isArray(r)) return r;
    if (typeof r === "string")
      return r
        .split(",")
        .map((s) => s.trim())
        .filter(Boolean);
    return [] as string[];
  }, [user?.role]);

  return (
    <div className="min-h-screen flex bg-gradient-to-br from-blue-50 via-white to-purple-50">
      <aside
        className={`fixed lg:static inset-y-0 left-0 z-50 bg-white border-r border-gray-200 transform transition-transform duration-300 ease-in-out ${
          sidebarOpen ? "translate-x-0" : "-translate-x-full lg:translate-x-0"
        } ${collapsed ? "w-20" : "w-64"}`}
      >
        <div className="flex flex-col h-full">
          <div className="flex items-center justify-between p-4 border-b border-gray-200">
            <div className="flex items-center gap-3">
              <h1
                className={`font-bold bg-gradient-to-r from-primary-600 to-purple-600 bg-clip-text text-transparent ${
                  collapsed ? "text-sm" : "text-2xl"
                }`}
              >
                {collapsed ? "UST" : "UST Task Manager"}
              </h1>
            </div>

            <div className="flex items-center gap-2">
              <button
                onClick={(e) => {
                  e.stopPropagation();
                  setCollapsed((c) => !c);
                }}
                className="hidden lg:inline-flex items-center justify-center p-1 rounded-md text-gray-600 hover:bg-gray-100"
                title={collapsed ? "Expand sidebar" : "Collapse sidebar"}
              >
                {collapsed ? (
                  <ChevronRight size={18} />
                ) : (
                  <ChevronLeft size={18} />
                )}
              </button>

              <button
                onClick={() => setSidebarOpen(false)}
                className="lg:hidden text-gray-500 hover:text-gray-700"
                aria-label="Close menu"
              >
                <X size={20} />
              </button>
            </div>
          </div>

          <nav className="flex-1 p-2 space-y-1">
            {menuItems.map((item) => {
              const Icon = item.icon;
              const active = isActive(item.path);
              return (
                <button
                  key={item.path}
                  onClick={() => {
                    navigate(item.path);
                    setSidebarOpen(false);
                  }}
                  className={`w-full flex items-center gap-3 px-3 py-2 rounded-lg transition-all duration-200 text-left ${
                    active
                      ? "bg-primary-50 text-primary-700 border-l-4 border-primary-500"
                      : "text-gray-700 hover:bg-gray-50"
                  }`}
                >
                  <Icon size={18} />
                  {!collapsed && (
                    <span className="font-medium">{item.label}</span>
                  )}
                </button>
              );
            })}
          </nav>

          <div className="p-4 border-t border-gray-200">
            <div className="mb-2">
              <h2 className="text-sm font-medium text-gray-600">
                Welcome Back!
              </h2>
              {user && (
                <div className="mt-1 text-sm text-gray-700">
                  {employeeName ||
                    (user as any)?.name ||
                    (user as any)?.full_name ||
                    (user as any)?.employee?.name ||
                    ""}
                </div>
              )}
            </div>

            <div className="flex items-center gap-3">
              {rolesArray.length > 0 && (
                <select
                  id="active-role-select"
                  value={activeRole || ""}
                  onChange={(e) => setActiveRole(e.target.value)}
                  className="text-sm px-2 py-1 border border-gray-300 rounded-md bg-white focus:outline-none focus:ring-2 focus:ring-primary-500"
                >
                  <option value="" disabled>
                    Select role
                  </option>
                  {rolesArray.map((r) => (
                    <option key={r} value={r}>
                      {r}
                    </option>
                  ))}
                </select>
              )}

              <button
                onClick={handleLogout}
                className="flex items-center gap-2 text-sm text-red-600 hover:text-red-700 hover:bg-red-50 px-2 py-1 rounded-md"
              >
                <LogOut size={16} />
                <span className="hidden sm:inline">Logout</span>
              </button>
            </div>
          </div>
        </div>
      </aside>

      <div
        className={`flex-1 flex flex-col ${
          collapsed ? "lg:ml-20" : "lg:ml-64"
        }`}
      >
        <header className="p-4 border-b border-gray-200 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <button
              onClick={() => setSidebarOpen((s) => !s)}
              className="lg:hidden p-2 rounded-md text-gray-600 hover:bg-gray-100"
            >
              <Menu size={18} />
            </button>
            <div>
              <h1 className="text-xl font-semibold">
                {(user as any)?.name || ""}
              </h1>
              <p className="text-sm text-gray-500">
                {(user as any)?.email || ""}
              </p>
            </div>
          </div>

          <div />
        </header>

        <main className="flex-1 p-6 lg:p-8 overflow-auto">
          <div className="max-w-7xl mx-auto page-transition">
            <Outlet />
          </div>
        </main>
      </div>

      {sidebarOpen && (
        <div
          className="fixed inset-0 bg-black bg-opacity-50 z-40 lg:hidden"
          onClick={() => setSidebarOpen(false)}
        />
      )}
    </div>
  );
};

export default Layout;
