import { Outlet, useNavigate, useLocation } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import {
  LayoutDashboard,
  CheckSquare,
  Users,
  UserCog,
  LogOut,
  Menu,
  X,
  ChevronLeft,
  ChevronRight,
} from "lucide-react";
import { useState, useEffect } from "react";
import { employeeAPI } from "../services/api";

const LayoutNew = () => {
  const { user, logout, activeRole, setActiveRole } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [collapsed, setCollapsed] = useState(false);
  const [employeeName, setEmployeeName] = useState<string | null>(null);

  useEffect(() => {
    let mounted = true;
    if (user?.e_id) {
      employeeAPI
        .getById(user.e_id, activeRole || "")
        .then((emp) => {
          if (!mounted) return;
          if (emp && (emp as any).name) setEmployeeName((emp as any).name);
        })
        .catch((err) => {
          console.debug("could not fetch employee name:", err?.message ?? err);
        });
    }
    return () => {
      mounted = false;
    };
  }, [user?.e_id, activeRole]);

  const menuItems = [
    { icon: LayoutDashboard, label: "Dashboard", path: "/" },
    { icon: CheckSquare, label: "Tasks", path: "/tasks" },
    { icon: Users, label: "Employees", path: "/employees" },
    { icon: UserCog, label: "Users", path: "/users" },
  ];

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  const isActive = (path: string) => location.pathname === path;

  return (
    <div className="min-h-screen flex bg-gradient-to-br from-blue-50 via-white to-purple-50">
      <aside
        className={`fixed lg:static inset-y-0 left-0 z-50 bg-white border-r border-gray-200 transform transition-all duration-300 ease-in-out flex-shrink-0 ${
          sidebarOpen ? "translate-x-0" : "-translate-x-full lg:translate-x-0"
        } ${collapsed ? "w-20" : "w-64"}`}
        onClick={() => {
          if (collapsed) setCollapsed(false);
        }}
      >
        <div className="flex flex-col h-full">
          <div className="flex items-center justify-between p-4 border-b border-gray-200">
            <div className="flex items-center gap-3">
              <h1
                className={`text-lg font-bold ${
                  collapsed ? "text-sm" : "text-2xl"
                } bg-gradient-to-r from-primary-600 to-purple-600 bg-clip-text text-transparent`}
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
              >
                <X size={24} />
              </button>
            </div>
          </div>

          <nav
            className={`flex-1 p-2 ${collapsed ? "space-y-3" : "space-y-1"}`}
          >
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
                  className={`w-full flex items-center ${
                    collapsed ? "justify-center py-4" : "gap-3 px-4 py-3"
                  } rounded-lg transition-all duration-200 ${
                    active
                      ? "bg-primary-50 text-primary-700 border-l-4 border-primary-500"
                      : "text-gray-700 hover:bg-gray-50"
                  }`}
                >
                  <Icon size={20} />
                  {!collapsed && (
                    <span className="font-medium">{item.label}</span>
                  )}
                </button>
              );
            })}
          </nav>
        </div>
      </aside>

      {/* Main content grows to fill remaining space; don't add extra static left margin. */}
      <div className="flex-1 flex flex-col">
        <header className="bg-white border-b border-gray-200 px-4 lg:px-8 py-3 flex items-center justify-between gap-4">
          <div className="flex items-center gap-2 lg:gap-3">
            <button
              onClick={() => setSidebarOpen(true)}
              className="lg:hidden text-gray-500 hover:text-gray-700"
            >
              <Menu size={24} />
            </button>
            <h1 className="text-lg lg:text-xl font-bold bg-gradient-to-r from-primary-600 to-purple-600 bg-clip-text text-transparent">
              Welcome Back!
              {user && (
                <span className="ml-3 text-sm lg:text-base font-medium text-gray-700 bg-clip-text text-transparent bg-none">
                  {employeeName ||
                    ((user as any)?.name ??
                      (user as any)?.full_name ??
                      (user as any)?.employee?.name) ||
                    ""}
                </span>
              )}
            </h1>
          </div>

          <div className="flex items-center gap-3 lg:gap-4">
            {user?.role && user.role.length > 0 && (
              <div className="flex items-center gap-2">
                <label
                  htmlFor="active-role-select-header"
                  className="hidden lg:block text-xs font-medium text-gray-600"
                >
                  Active role
                </label>
                <select
                  id="active-role-select-header"
                  value={activeRole || ""}
                  onChange={(e) => setActiveRole(e.target.value)}
                  className="text-xs lg:text-sm px-2 py-1 border border-gray-300 rounded-md bg-white focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all duration-150"
                >
                  <option value="" disabled>
                    Select role
                  </option>
                  {user.role.map((r) => (
                    <option key={r} value={r}>
                      {r}
                    </option>
                  ))}
                </select>
              </div>
            )}

            <button
              onClick={handleLogout}
              className="flex items-center gap-1 lg:gap-2 text-xs lg:text-sm text-red-600 hover:text-red-700 hover:bg-red-50 px-2 lg:px-3 py-1 rounded-md transition-all duration-150"
            >
              <LogOut size={16} />
              <span className="hidden sm:inline font-medium">Logout</span>
            </button>
          </div>
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

export default LayoutNew;
