import React, { useState } from 'react';
import {
  LogOut,
  Users,
  CheckSquare,
  User,
  RefreshCw,
  LayoutGrid,
  List,
  Menu
} from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import EmployeesPage from '../employees/EmployeesPage';
import TasksPage from '../tasks/TasksPage';
import KanbanBoard from '../tasks/KanbanBoard';

const Layout = () => {
  const { user, activeRole, logout, changeRole, hasMultipleRoles } = useAuth();
  const [currentPage, setCurrentPage] = useState('tasks');
  const [taskView, setTaskView] = useState('list');
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [dropdownOpen, setDropdownOpen] = useState(false);

  const renderPage = () => {
    if (currentPage === 'employees') return <EmployeesPage />;
    return taskView === 'board' ? <KanbanBoard /> : <TasksPage />;
  };

  const roleStyles = {
    ADMIN: 'bg-purple-500/10 text-purple-700',
    MANAGER: 'bg-blue-500/10 text-blue-700',
    DEVELOPER: 'bg-green-500/10 text-green-700'
  };

  return (
    <div className="min-h-screen flex bg-slate-100">

      {/* SIDEBAR */}
      <aside
        className={`transition-all duration-300
        ${sidebarOpen ? 'w-64' : 'w-16'}
        bg-gradient-to-b from-indigo-600 to-indigo-800 text-white shadow-xl`}
      >
        <div className="h-16 flex items-center justify-between px-4">
          {sidebarOpen && (
            <h1 className="text-xl font-semibold tracking-wide">
              TaskPro
            </h1>
          )}
          <button
            onClick={() => setSidebarOpen(!sidebarOpen)}
            className="p-2 rounded-lg hover:bg-white/10"
          >
            <Menu size={20} />
          </button>
        </div>

        <nav className="mt-6 px-3 space-y-2">
          <SidebarButton
            icon={<CheckSquare size={18} />}
            label="Tasks"
            active={currentPage === 'tasks'}
            open={sidebarOpen}
            onClick={() => setCurrentPage('tasks')}
          />
          <SidebarButton
            icon={<Users size={18} />}
            label="Employees"
            active={currentPage === 'employees'}
            open={sidebarOpen}
            onClick={() => setCurrentPage('employees')}
          />
        </nav>
      </aside>

      {/* MAIN */}
      <div className="flex-1 flex flex-col">

        {/* NAVBAR */}
        <header className="bg-white/80 backdrop-blur shadow-md px-6 py-4 flex items-center justify-between">

          {/* LEFT */}
          <div className="flex items-center gap-4">
            <span
              className={`px-4 py-1.5 rounded-full text-xs font-semibold
              ${roleStyles[activeRole]}`}
            >
              {activeRole}
            </span>

            {currentPage === 'tasks' && (
              <div className="flex bg-slate-100 rounded-xl p-1">
                <ViewButton
                  active={taskView === 'list'}
                  icon={<List size={14} />}
                  label="List"
                  onClick={() => setTaskView('list')}
                />
                <ViewButton
                  active={taskView === 'board'}
                  icon={<LayoutGrid size={14} />}
                  label="Board"
                  onClick={() => setTaskView('board')}
                />
              </div>
            )}
          </div>

          {/* RIGHT */}
          <div className="flex items-center gap-3">

            <div className="flex items-center gap-2 bg-slate-100 px-4 py-2 rounded-xl">
              <User size={16} className="text-slate-500" />
              <span className="text-sm font-medium text-slate-800">
                {user?.email}
              </span>
            </div>

            {hasMultipleRoles() && (
              <div className="relative">
                <button
                  onClick={() => setDropdownOpen(!dropdownOpen)}
                  className="flex items-center gap-2 px-4 py-2 rounded-xl text-sm font-medium bg-slate-100 hover:bg-slate-200 transition"
                >
                  <RefreshCw size={16} />
                  Switch Role
                </button>

                {dropdownOpen && (
                  <div className="absolute right-0 mt-2 w-40 bg-white border border-gray-200 rounded-xl shadow-lg z-50">
                    {user.role.map((role) => (
                      <button
                        key={role}
                        onClick={() => {
                          changeRole(role);
                          setDropdownOpen(false);
                        }}
                        className={`w-full text-left px-4 py-2 text-sm hover:bg-indigo-100 transition
                          ${activeRole === role ? 'font-semibold text-indigo-700' : 'text-gray-700'}`}
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
          </div>
        </header>

        {/* CONTENT */}
        <main className="flex-1 p-6 overflow-y-auto">
          <div className="bg-white rounded-2xl shadow-sm p-6 min-h-full">
            {renderPage()}
          </div>
        </main>
      </div>
    </div>
  );
};

/* ---------- COMPONENTS ---------- */

const SidebarButton = ({ icon, label, active, open, onClick }) => (
  <button
    onClick={onClick}
    className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium
    transition-all
    ${active
      ? 'bg-white/20 shadow text-white'
      : 'text-indigo-100 hover:bg-white/10'}`}
  >
    {icon}
    {open && <span>{label}</span>}
  </button>
);

const ViewButton = ({ icon, label, active, onClick }) => (
  <button
    onClick={onClick}
    className={`flex items-center gap-1 px-4 py-1.5 rounded-lg text-sm transition
    ${active
      ? 'bg-white shadow font-medium'
      : 'text-slate-500 hover:text-slate-700'}`}
  >
    {icon}
    {label}
  </button>
);

const ActionButton = ({ icon, label, onClick, danger }) => (
  <button
    onClick={onClick}
    className={`flex items-center gap-2 px-4 py-2 rounded-xl text-sm font-medium
    transition shadow-sm
    ${danger
      ? 'text-red-600 bg-red-50 hover:bg-red-100'
      : 'text-slate-700 bg-slate-100 hover:bg-slate-200'}`}
  >
    {icon}
    {label}
  </button>
);

export default Layout;
