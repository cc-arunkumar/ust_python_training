import React from 'react';
import { ClipboardList, LogOut, Menu, ChevronDown } from 'lucide-react';
import { ROLE_COLORS } from '../../utils/constants';

const Header = ({ user, activeView, onViewChange, onLogout, onMenuToggle }) => {
  return (
    <header className="bg-white border-b border-gray-200 sticky top-0 z-40">
      <div className="px-4 py-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-4">
            <button
              onClick={onMenuToggle}
              className="lg:hidden text-gray-600 hover:text-gray-800 transition"
            >
              <Menu className="w-6 h-6" />
            </button>
            
            <div className="flex items-center gap-3">
              <div className={`w-10 h-10 bg-gradient-to-br ${ROLE_COLORS[activeView]} rounded-xl flex items-center justify-center shadow-md`}>
                <ClipboardList className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="text-xl font-bold text-gray-800">Task Manager</h1>
                <p className="text-xs text-gray-500 capitalize">{activeView} View</p>
              </div>
            </div>
          </div>
          
          <div className="flex items-center gap-4">
            {user.roles.length > 1 && (
              <div className="relative">
                <select
                  value={activeView}
                  onChange={(e) => onViewChange(e.target.value)}
                  className="appearance-none bg-gray-100 text-gray-700 px-4 py-2 pr-10 rounded-lg font-medium cursor-pointer hover:bg-gray-200 transition outline-none"
                >
                  {user.roles.map(role => (
                    <option key={role} value={role} className="capitalize">
                      {role} View
                    </option>
                  ))}
                </select>
                <ChevronDown className="absolute right-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-500 pointer-events-none" />
              </div>
            )}
            
            <div className="flex items-center gap-3 border-l border-gray-200 pl-4">
              <div className="text-right hidden sm:block">
                <p className="text-sm font-medium text-gray-800">{user.name}</p>
                <p className="text-xs text-gray-500">ID: {user.emp_id}</p>
              </div>
              <button
                onClick={onLogout}
                className="p-2 text-gray-600 hover:bg-red-50 hover:text-red-600 rounded-lg transition"
                title="Logout"
              >
                <LogOut className="w-5 h-5" />
              </button>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;