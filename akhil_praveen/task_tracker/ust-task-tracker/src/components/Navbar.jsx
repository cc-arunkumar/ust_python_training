import React from 'react';
import { CheckCircle2, LogOut } from 'lucide-react';
import { logout } from '../api/taskApi';

function Navbar({ onLogout }) {
  const handleLogout = () => {
    logout(); // This removes the token from localStorage
    onLogout();
  };

  return (
    <nav className="bg-white shadow-md sticky top-0 z-10">
      <div className="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
        <div className="flex items-center space-x-3">
          <div className="bg-gradient-to-r from-indigo-500 to-purple-600 w-10 h-10 rounded-full flex items-center justify-center">
            <CheckCircle2 className="text-white" size={20} />
          </div>
          <h1 className="text-2xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">
            UST Task Tracker
          </h1>
        </div>
        <button
          onClick={handleLogout}
          className="flex items-center space-x-2 px-4 py-2 rounded-lg bg-red-500 text-white hover:bg-red-600 transition-colors"
        >
          <LogOut size={18} />
          <span>Logout</span>
        </button>
      </div>
    </nav>
  );
}

export default Navbar;