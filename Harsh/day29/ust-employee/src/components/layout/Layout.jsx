import React, { useState, useEffect } from "react";
import { LogOut, CheckSquare, User, RefreshCw, Menu } from "lucide-react";

import { useAuth } from "../../context/AuthContext";
import EmployeesPage from "../employees/EmployeesPage";
import UsersPage from "../users/UsersPage";
import KanbanBoard from "../tasks/KanbanBoard";
// Note: TasksPage removed; KanbanBoard used as the default task view
import ApiService from "../../services/api";

const Layout = () => {
  const { user, activeRole, logout, changeRole, hasMultipleRoles, hasRole } =
    useAuth();

  const [currentPage, setCurrentPage] = useState("tasks");
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [dropdownOpen, setDropdownOpen] = useState(false);

  const [tasks, setTasks] = useState([]);
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    loadDashboardData();
  }, [activeRole, user?.email]);

  const loadDashboardData = async () => {
    try {
      const allTasks = await ApiService.getTasks();
      const allEmployees = await ApiService.getEmployees();

      // sanity guards: ensure arrays
      const tasksArr = Array.isArray(allTasks) ? allTasks : [];
      const employeesArr = Array.isArray(allEmployees) ? allEmployees : [];

      // Admin can see all tasks and all employees
      if (activeRole === "ADMIN") {
        setTasks(tasksArr);
        setEmployees(employeesArr);
        return;
      }

      // Manager can see tasks assigned to their team and employees under them
      if (activeRole === "MANAGER") {
        // employees data shape uses emp_id and manager_id (see EmployeesPage)
        // Try to locate the manager's employee record by matching email -> emp_id
        const currentManager = employeesArr.find(
          (emp) => emp.email === user?.email
        );

        // If we found the manager's employee record, use emp_id to find direct reports.
        // Otherwise, fallback to zero team members.
        const managerEmpId = currentManager
          ? Number(currentManager.emp_id)
          : null;

        const teamEmployees = managerEmpId
          ? employeesArr.filter(
              (emp) => Number(emp.manager_id) === managerEmpId
            )
          : [];

        const teamIds = teamEmployees
          .map((e) => Number(e.emp_id))
          .filter(Boolean);

        // Tasks use assigned_to as Employee ID (number). Include tasks assigned to manager (if we have id)
        // or any team member. If we don't have managerEmpId, just include tasks assigned to any teamIds (empty)
        const managerTasks = tasksArr.filter((task) => {
          const assignedToRaw = task?.assigned_to;
          const assignedTo =
            assignedToRaw == null ? null : Number(assignedToRaw);

          return (
            (managerEmpId != null && assignedTo === managerEmpId) ||
            (assignedTo != null && teamIds.includes(assignedTo))
          );
        });

        // Dev helper: log derived values (safe in dev only)
        // eslint-disable-next-line no-console
        console.debug(
          "[Dashboard] managerEmpId=",
          managerEmpId,
          "teamIds=",
          teamIds,
          "managerTasks=",
          managerTasks.length
        );

        setTasks(managerTasks);
        setEmployees(teamEmployees);
        return;
      }

      // Developer can only see tasks assigned to them
      if (activeRole === "DEVELOPER") {
        // Find the developer's employee record to get emp_id (tasks use employee IDs)
        const currentEmp = employeesArr.find(
          (emp) => emp.email === user?.email
        );
        const devEmpId = currentEmp ? Number(currentEmp.emp_id) : null;

        const devTasks = tasksArr.filter((task) => {
          const assignedToRaw = task?.assigned_to;
          const assignedTo =
            assignedToRaw == null ? null : Number(assignedToRaw);
          return (
            devEmpId != null && assignedTo != null && assignedTo === devEmpId
          );
        });

        // Dev helper: log derived values
        // eslint-disable-next-line no-console
        console.debug(
          "[Dashboard] developerEmpId=",
          devEmpId,
          "devTasks=",
          devTasks.length
        );

        setTasks(devTasks);
        // Show only the developer user in the employees panel
        setEmployees(currentEmp ? [currentEmp] : []);
        return;
      }
      // fallback: clear
      setTasks([]);
      setEmployees([]);
    } catch (err) {
      // fail safe - log and clear state
      // eslint-disable-next-line no-console
      console.error("Failed to load dashboard data", err);
      setTasks([]);
      setEmployees([]);
    }
  };

  // Dashboard stats moved into KanbanBoard per UX request

  const renderPage = () => {
    if (currentPage === "employees")
      return <EmployeesPage initialEmployees={employees} />;
    if (currentPage === "users") return <UsersPage />;
    return (
      <KanbanBoard
        initialTasks={tasks}
        initialEmployees={employees}
        onTasksChanged={loadDashboardData}
      />
    );
  };

  const roleStyles = {
    ADMIN: "bg-purple-100 text-purple-700",
    MANAGER: "bg-blue-100 text-blue-700",
    DEVELOPER: "bg-green-100 text-green-700",
  };

  return (
    <div className="min-h-screen flex bg-gradient-to-br from-slate-100 to-slate-200">
      {/* SIDEBAR */}
      <aside
        className={`${
          sidebarOpen ? "w-64" : "w-16"
        } bg-indigo-700 text-white transition-all duration-300 ease-in-out border-r border-indigo-500`}
      >
        <div className="h-16 flex items-center justify-between px-4">
          {sidebarOpen && (
            <h1 className="text-xl font-semibold animate-fade-in">JIRA Lite</h1>
          )}
          <button
            onClick={() => setSidebarOpen(!sidebarOpen)}
            className="hover:scale-110 transition-transform"
          >
            <Menu size={20} />
          </button>
        </div>

        <nav className="mt-6 px-3 space-y-2">
          <SidebarButton
            icon={<CheckSquare size={18} />}
            label="Tasks"
            active={currentPage === "tasks"}
            open={sidebarOpen}
            onClick={() => setCurrentPage("tasks")}
          />
          {/* Users button (admin only) */}
          {hasRole && hasRole("ADMIN") && (
            <SidebarButton
              icon={<User size={18} />}
              label="Users"
              active={currentPage === "users"}
              open={sidebarOpen}
              onClick={() => setCurrentPage("users")}
            />
          )}
          {/* Employees button moved into KanbanBoard header per UX change */}
        </nav>
      </aside>

      {/* MAIN */}
      <div className="flex-1 flex flex-col">
        {/* NAVBAR */}
        <header className="bg-white/80 backdrop-blur border-b border-slate-200 px-6 py-4 flex justify-between animate-slide-down">
          <div className="flex items-center gap-4">
            {/* left header area (view toggles removed) */}
          </div>

          <div className="flex items-center gap-3">
            {/* Role badge should be left of email */}
            <span
              className={`px-4 py-1 rounded-full text-xs font-semibold border ${roleStyles[activeRole]}`}
            >
              {activeRole}
            </span>

            <div className="flex items-center gap-2 bg-slate-100 px-4 py-2 rounded-lg border border-slate-200">
              <User size={16} />
              <span className="text-sm">{user?.email}</span>
            </div>

            {hasMultipleRoles() && (
              <div className="relative">
                <button
                  onClick={() => setDropdownOpen(!dropdownOpen)}
                  className="bg-slate-100 px-3 py-2 rounded-lg border border-slate-200 hover:rotate-180 transition-transform duration-300"
                >
                  <RefreshCw size={16} />
                </button>

                {dropdownOpen && (
                  <div className="absolute right-0 mt-2 bg-white border border-slate-200 rounded-lg shadow animate-scale-in w-40">
                    {user.role.map((role) => (
                      <button
                        key={role}
                        onClick={() => {
                          changeRole(role);
                          setDropdownOpen(false);
                        }}
                        className="w-full text-left px-4 py-2 hover:bg-slate-100 text-sm transition-colors"
                      >
                        {role}
                      </button>
                    ))}
                  </div>
                )}
              </div>
            )}

            <ActionButton
              icon={<LogOut size={16} />}
              label="Logout"
              danger
              onClick={logout}
            />

            {/* Profile avatar moved to the far right of the header controls */}
            <div className="relative group">
              <div className="w-9 h-9 rounded-full border border-slate-300 shadow-sm flex items-center justify-center bg-white text-slate-700 font-semibold uppercase">
                {user?.email?.charAt(0)}
              </div>

              {/* Hover tooltip with profile details */}
              <div className="hidden group-hover:flex absolute right-0 mt-3 transform translate-y-0 w-56 bg-white border border-slate-200 rounded-md shadow-lg p-3 flex-col text-sm z-50">
                <div className="font-semibold text-slate-800 truncate">
                  {user?.name || user?.email}
                </div>
                <div className="text-slate-500 truncate text-xs">
                  {user?.email}
                </div>
                <div className="mt-2 text-xs text-slate-600">
                  Role: {activeRole}
                </div>
              </div>
            </div>
          </div>
        </header>

        {/* CONTENT */}
        <main className="flex-1 p-6 animate-fade-in">
          {/* Dashboard stats removed from Layout — moved to KanbanBoard */}

          <div className="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm animate-slide-up mt-8">
            {renderPage()}
          </div>
        </main>
      </div>
    </div>
  );
};

/* COMPONENTS */

const SidebarButton = ({ icon, label, active, open, onClick }) => (
  <button
    onClick={onClick}
    className={`w-full flex items-center gap-3 px-4 py-3 rounded-lg transition-all duration-200 ${
      active ? "bg-white/20 border border-white/30" : "hover:bg-white/10"
    }`}
  >
    {icon}
    {open && <span className="animate-fade-in">{label}</span>}
  </button>
);

// ViewButton removed — view toggles handled by KanbanBoard only now

const ActionButton = ({ icon, label, onClick, danger }) => (
  <button
    onClick={onClick}
    className={`flex items-center gap-2 px-4 py-2 rounded-lg text-sm border transition-all hover:scale-105 ${
      danger
        ? "bg-red-50 text-red-600 border-red-200 hover:bg-red-100"
        : "bg-slate-100 border-slate-200"
    }`}
  >
    {icon} {label}
  </button>
);

const StatCard = ({ title, value, icon, progress }) => (
  <div className="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm hover:shadow-md transition-all duration-300 hover:-translate-y-1">
    <div className="flex justify-between items-center">
      <div>
        <p className="text-sm text-slate-500">{title}</p>
        <h2 className="text-3xl font-semibold">{value}</h2>
      </div>
      <div className="p-3 bg-slate-100 rounded-xl">{icon}</div>
    </div>

    {progress !== undefined && (
      <div className="mt-4">
        <div className="h-2 bg-slate-200 rounded-full overflow-hidden">
          <div
            className="h-full bg-blue-600 rounded-full transition-all duration-700"
            style={{ width: `${progress}%` }}
          />
        </div>
      </div>
    )}
  </div>
);

export default Layout;
