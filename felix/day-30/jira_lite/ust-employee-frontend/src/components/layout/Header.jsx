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
                  className="flex items-center gap-3 px-5 py-3 bg-gradient-to-r from-emerald-400/90 via-teal-400/90 to-cyan-400/90 hover:from-emerald-500 hover:via-teal-500 hover:to-cyan-500 text-white font-bold rounded-2xl transition-all duration-300 backdrop-blur-xl border-2 border-emerald-300/50 hover:border-emerald-400/70 shadow-2xl hover:shadow-emerald-500/40 hover:scale-105 hover:-translate-y-1 group relative overflow-hidden"
                >
                  {/* Animated background glow */}
                  <div className="absolute inset-0 bg-gradient-to-r from-white/20 to-transparent rounded-2xl blur animate-pulse opacity-75 group-hover:opacity-100 transition-opacity"></div>
                  
                  {/* Active indicator dot */}
                  <div className="w-3 h-3 bg-white rounded-full shadow-lg animate-ping group-hover:animate-none"></div>
                  
                  <span className="relative z-10 text-sm font-bold bg-gradient-to-r from-white via-emerald-50 to-cyan-50 bg-clip-text text-transparent drop-shadow-lg">
                    {currentView}
                  </span>
                  
                  <ChevronDown 
                    size={18} 
                    className="relative z-10 text-white/90 group-hover:rotate-180 transition-transform duration-300" 
                  />
                </button>


                {showRoleDropdown && (
                  <div className="absolute right-0 mt-2 w-48 bg-white rounded-xl shadow-2xl border border-gray-100 py-2 animate-in fade-in slide-in-from-top-2 duration-200">
                    {userRoles.map((role) => (
                      <button
                        key={role}
                        onClick={() => handleRoleChange(role)}
                        className={`w-full px-4 py-3 text-left text-sm font-semibold rounded-xl transition-all duration-200 shadow-sm hover:shadow-lg transform hover:scale-[1.02] hover:-translate-y-0.5 group capitalize ${
                          currentView === role
                            ? 'bg-gradient-to-r from-emerald-400 via-teal-400 to-cyan-400 text-white shadow-emerald-500/50 border-2 border-emerald-300 ring-2 ring-emerald-500/30 shadow-lg'
                            : 'bg-gradient-to-r from-gray-50 to-white text-gray-700 border-2 border-gray-200 hover:from-emerald-50 hover:to-teal-50 hover:text-emerald-700 hover:border-emerald-300'
                        }`}
                      >
                        <span className="flex items-center gap-2">
                          {currentView === role ? (
                            <div className="w-2 h-2 bg-white rounded-full animate-ping"></div>
                          ) : (
                            <div className="w-2 h-2 bg-gray-300 group-hover:bg-emerald-400 rounded-full transition-colors"></div>
                          )}
                          {role}
                        </span>
                      </button>

                    ))}
                  </div>
                )}
              </div>
            )}

            {/* User Info */}
            <div className="flex items-center gap-3">
              {/* User Profile Card */}
              <div className="hidden sm:flex items-center gap-3 bg-white/10 backdrop-blur-sm rounded-xl px-4 py-2 border border-white/20 shadow-lg">
                {/* Profile Picture */}
                <div className="relative">
                  <div className="w-10 h-10 bg-gradient-to-br from-cyan-400 to-blue-500 rounded-full flex items-center justify-center text-white font-bold text-lg shadow-lg ring-2 ring-white/30">
                    {userName.charAt(0).toUpperCase()}
                  </div>
                  <div className="absolute -bottom-0.5 -right-0.5 w-3 h-3 bg-green-400 rounded-full border-2 border-white shadow-sm"></div>
                </div>
                
                {/* User Details */}
                <div className="text-left">
                  <p className="text-sm font-bold text-white leading-tight">
                    {userName}
                  </p>
                  <p className="text-xs text-white/80 font-medium">
                    ID: {user.emp_id}
                  </p>
                </div>
              </div>

              <button
                onClick={logout}
                className="flex items-center gap-2 px-5 py-2.5 bg-gradient-to-r from-red-500 to-pink-500 hover:from-red-400 hover:to-pink-400 text-white rounded-xl transition-all duration-200 shadow-xl hover:shadow-red-500/50 transform hover:scale-110 border-2 border-red-400/50 font-bold"
                title="Logout"
              >
                <LogOut size={18} />
                <span className="hidden sm:inline">Logout</span>
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