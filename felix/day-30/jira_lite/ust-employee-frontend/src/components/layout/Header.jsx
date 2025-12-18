import React, { useState, useEffect } from 'react';
import { LogOut, ChevronDown, Users, LayoutDashboard } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';
import { api } from '../../services/api';

const Header = ({ currentView, userRoles, onChangeView, onNavigate, onUserNameFetched }) => {
  const { user, logout, token } = useAuth();
  const [showRoleDropdown, setShowRoleDropdown] = useState(false);
  const [userName, setUserName] = useState('');

  useEffect(() => {
    const fetchUserName = async () => {
      try {
        const userData = await api.getEmployeeById(token, user.emp_id);
        const name = userData?.name || user.name || 'User';
        setUserName(name);
        
        // Pass the name to parent component (Dashboard)
        if (onUserNameFetched) {
          onUserNameFetched(name);
        }
      } catch (err) {
        console.error('Failed to fetch user name:', err);
        const fallbackName = user.name || 'User';
        setUserName(fallbackName);
        
        if (onUserNameFetched) {
          onUserNameFetched(fallbackName);
        }
      }
    };

    if (user.emp_id && token) {
      fetchUserName();
    }
  }, [token, user.emp_id, user.name, onUserNameFetched]);

  const handleRoleChange = (role) => {
    if (onChangeView) {
      onChangeView(role);
    }
    setShowRoleDropdown(false);
  };

  const canAccessEmployees = userRoles?.some((role) =>
    ['admin', 'manager'].includes(role)
  );

  return (
    <header className="bg-gradient-to-r from-blue-600 via-purple-600 to-indigo-600 shadow-xl sticky top-0 z-40 backdrop-blur-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo and Title */}
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-white rounded-xl shadow-lg flex items-center justify-center transform hover:scale-110 transition-transform duration-200">
              <div className="w-6 h-6 bg-gradient-to-br from-blue-500 to-purple-600 rounded-lg"></div>
            </div>
            <h1 className="text-2xl font-bold text-white tracking-tight hover:tracking-wide transition-all duration-300">
              TaskFlow
            </h1>
          </div>

          {/* Navigation */}
          {onNavigate && (
            <nav className="flex items-center gap-2">
              <button
                onClick={() => onNavigate('/dashboard')}
                className="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-400 hover:to-blue-400 text-white rounded-xl transition-all duration-200 shadow-lg hover:shadow-cyan-500/50 transform hover:scale-105"
              >
                <LayoutDashboard size={18} />
                <span className="hidden sm:inline font-medium">Dashboard</span>
              </button>

              {canAccessEmployees && (
                <button
                  onClick={() => onNavigate('/employees')}
                  className="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-400 hover:to-pink-400 text-white rounded-xl transition-all duration-200 shadow-lg hover:shadow-purple-500/50 transform hover:scale-105"
                >
                  <Users size={18} />
                  <span className="hidden sm:inline font-medium">Employees</span>
                </button>
              )}
            </nav>
          )}

          {/* User Info and Controls */}
          <div className="flex items-center gap-4">
            {/* Role Selector */}
            {userRoles && userRoles.length > 1 && (
              <div className="relative">
                <button
                  onClick={() => setShowRoleDropdown(!showRoleDropdown)}
                  className="flex items-center gap-2 px-4 py-2 bg-white/20 hover:bg-white/30 rounded-xl transition-all duration-200 backdrop-blur-sm border border-white/30 hover:border-white/50 shadow-lg"
                >
                  <span className="text-sm font-semibold text-white capitalize">
                    {currentView}
                  </span>
                  <ChevronDown size={16} className="text-white/90" />
                </button>

                {showRoleDropdown && (
                  <div className="absolute right-0 mt-2 w-48 bg-white rounded-xl shadow-2xl border border-gray-100 py-2 animate-in fade-in slide-in-from-top-2 duration-200">
                    {userRoles.map((role) => (
                      <button
                        key={role}
                        onClick={() => handleRoleChange(role)}
                        className={`w-full px-4 py-2.5 text-left text-sm hover:bg-gradient-to-r hover:from-blue-50 hover:to-purple-50 transition-all duration-150 capitalize ${
                          currentView === role
                            ? 'bg-gradient-to-r from-blue-50 to-purple-50 text-blue-700 font-semibold border-l-4 border-blue-600'
                            : 'text-gray-700 font-medium'
                        }`}
                      >
                        {role}
                      </button>
                    ))}
                  </div>
                )}
              </div>
            )}

            {/* User Info */}
            <div className="flex items-center gap-3">
              <div className="text-right hidden sm:block">
                <p className="text-sm font-semibold text-white">
                  {userName}
                </p>
                <p className="text-xs text-white/70">ID: {user.emp_id}</p>
              </div>

              <button
                onClick={logout}
                className="flex items-center gap-2 px-4 py-2 bg-white/10 text-white hover:bg-red-500 rounded-xl transition-all duration-200 backdrop-blur-sm border border-white/20 hover:border-red-400 shadow-lg hover:shadow-red-500/50"
                title="Logout"
              >
                <LogOut size={18} />
                <span className="hidden sm:inline font-medium">Logout</span>
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Mobile Role Indicator */}
      {userRoles && userRoles.length === 1 && (
        <div className="sm:hidden border-t border-white/20 px-4 py-2 bg-white/10 backdrop-blur-sm">
          <p className="text-xs text-white/80">
            Role: <span className="font-semibold capitalize text-white">{currentView}</span>
          </p>
        </div>
      )}
    </header>
  );
};

export default Header;