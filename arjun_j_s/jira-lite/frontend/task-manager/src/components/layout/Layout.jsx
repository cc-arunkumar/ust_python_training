import React, { useState } from 'react';
import { LogOut, Users, CheckSquare, User, RefreshCw, LayoutGrid, List } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import EmployeesPage from '../employees/EmployeesPage';
import TasksPage from '../tasks/TasksPage';
import KanbanBoard from '../tasks/KanbanBoard';

const Layout = () => {
  const { user, activeRole, logout, changeRole, hasMultipleRoles } = useAuth();
  const [currentPage, setCurrentPage] = useState('tasks');
  const [taskView, setTaskView] = useState('board'); // 'list' or 'board'

  const renderPage = () => {
    switch (currentPage) {
      case 'tasks':
        return taskView === 'board' ? <KanbanBoard /> : <TasksPage />;
      case 'employees':
        return <EmployeesPage />;
      default:
        return <TasksPage />;
    }
  };

  const getRoleBadgeColor = () => {
    switch (activeRole) {
      case 'ADMIN':
        return 'bg-purple-600 text-purple-100';
      case 'MANAGER':
        return 'bg-blue-600 text-blue-100';
      case 'DEVELOPER':
        return 'bg-green-600 text-green-100';
      default:
        return 'bg-gray-600 text-gray-100';
    }
  };

  return (
    <div className="min-h-screen bg-gray-900">
      {/* Navigation Bar */}
      <nav className="bg-gray-800 shadow-lg border-b border-gray-700">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            {/* Left side - Logo and Navigation */}
            <div className="flex space-x-8">
              <div className="flex items-center">
                <h1 className="text-xl font-bold text-white">
                  JiraLite
                </h1>
              </div>
              
              <div className="flex space-x-4 items-center">
                <button
                  onClick={() => setCurrentPage('tasks')}
                  className={`px-3 py-2 rounded-md text-sm font-medium transition ${
                    currentPage === 'tasks'
                      ? 'bg-blue-600 text-white'
                      : 'text-gray-300 hover:bg-gray-700 hover:text-white'
                  }`}
                >
                  <CheckSquare size={18} className="inline mr-2" />
                  Tasks
                </button>
                
                <button
                  onClick={() => setCurrentPage('employees')}
                  className={`px-3 py-2 rounded-md text-sm font-medium transition ${
                    currentPage === 'employees'
                      ? 'bg-blue-600 text-white'
                      : 'text-gray-300 hover:bg-gray-700 hover:text-white'
                  }`}
                >
                  <Users size={18} className="inline mr-2" />
                  Employees
                </button>

                {/* Task View Toggle - Only show when on tasks page */}
                {currentPage === 'tasks' && (
                  <div className="flex items-center bg-gray-700 rounded-md ml-4">
                    <button
                      onClick={() => setTaskView('board')}
                      className={`px-3 py-2 rounded-l-md text-sm font-medium transition flex items-center gap-1 ${
                        taskView === 'board'
                          ? 'bg-gray-600 text-white'
                          : 'text-gray-300 hover:text-white'
                      }`}
                      title="Board View"
                    >
                      <LayoutGrid size={16} />
                      Board
                    </button>
                    <button
                      onClick={() => setTaskView('list')}
                      className={`px-3 py-2 rounded-r-md text-sm font-medium transition flex items-center gap-1 ${
                        taskView === 'list'
                          ? 'bg-gray-600 text-white'
                          : 'text-gray-300 hover:text-white'
                      }`}
                      title="List View"
                    >
                      <List size={16} />
                      List
                    </button>
                  </div>
                )}
              </div>
            </div>

            {/* Right side - User info and Actions */}
            <div className="flex items-center space-x-4">
              <div className="flex items-center space-x-3 bg-gray-700 px-4 py-2 rounded-lg">
                <User size={18} className="text-gray-400" />
                <div className="text-sm">
                  <p className="font-medium text-white">{user?.email}</p>
                  <p className="text-xs text-gray-400">Role: {activeRole}</p>
                </div>
                <span className={`text-xs font-semibold px-2 py-1 rounded ${getRoleBadgeColor()}`}>
                  {activeRole}
                </span>
              </div>

              {/* Only show Switch Role button if user has multiple roles */}
              {hasMultipleRoles() && (
                <button
                  onClick={changeRole}
                  className="text-gray-300 hover:text-white hover:bg-gray-700 px-3 py-2 rounded-lg transition flex items-center gap-2"
                  title="Change Role"
                >
                  <RefreshCw size={18} />
                  <span className="text-sm font-medium">Switch Role</span>
                </button>
              )}
              
              <button
                onClick={logout}
                className="text-gray-300 hover:text-white hover:bg-gray-700 px-3 py-2 rounded-lg transition flex items-center gap-2"
                title="Logout"
              >
                <LogOut size={18} />
                <span className="text-sm font-medium">Logout</span>
              </button>
            </div>
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto">
        {renderPage()}
      </main>
    </div>
  );
};

export default Layout;