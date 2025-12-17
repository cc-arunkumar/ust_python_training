import React from 'react';
import { LogOut, List, Users } from 'lucide-react';

function Header({ role, activeTab, onTabChange, onLogout, canManageEmployees }) {
  return (
    <header className="bg-gradient-to-r from-blue-600 to-blue-700 shadow-lg">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between py-4">
          <div className="flex items-center gap-3">
            <h1 className="text-2xl font-bold text-white">Jira Lite</h1>
            <span className="px-3 py-1 bg-blue-500 text-white text-xs rounded-full">
              {role}
            </span>
          </div>

          <div className="flex items-center gap-4">
            <nav className="flex gap-2">
              <button
                onClick={() => onTabChange('tasks')}
                className={`px-4 py-2 rounded-md text-sm font-medium transition flex items-center gap-2 ${
                  activeTab === 'tasks'
                    ? 'bg-white text-blue-600 shadow-sm'
                    : 'text-gray-600 hover:text-gray-800'
                }`}
              >
                <List size={18} />
                Tasks
              </button>
              {canManageEmployees && (
                <button
                  onClick={() => onTabChange('employees')}
                  className={`px-4 py-2 rounded-md text-sm font-medium transition flex items-center gap-2 ${
                    activeTab === 'employees'
                      ? 'bg-white text-blue-600 shadow-sm'
                      : 'text-gray-600 hover:text-gray-800'
                  }`}
                >
                  <Users size={18} />
                  Employees
                </button>
              )}
            </nav>

            <button
              onClick={onLogout}
              className="px-4 py-2 bg-red-500 text-white rounded-md hover:bg-red-600 flex items-center gap-2 text-sm font-medium transition"
            >
              <LogOut size={18} />
              Logout
            </button>
          </div>
        </div>
      </div>
    </header>
  );
}

export default Header;