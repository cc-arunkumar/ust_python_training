import React, { useState, useEffect } from 'react';
import { LogOut, ChevronDown, Users, LayoutDashboard } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';
import { api } from '../../services/api';

const Header = ({ onChangeView, onNavigate }) => {
  const { user, logout, token } = useAuth();
  const [userRoles, setUserRoles] = useState([]);
  const [currentView, setCurrentView] = useState('developer');
  const [showRoleDropdown, setShowRoleDropdown] = useState(false);

  useEffect(() => {
    const fetchUserRoles = async () => {
      try {
        const userData = await api.getUserById(token, user.emp_id);
        if (userData && Array.isArray(userData.role)) {
          setUserRoles(userData.role);
          setCurrentView(userData.role[0] || 'developer');
          if (onChangeView) {
            onChangeView(userData.role[0] || 'developer');
          }
        }
      } catch (err) {
        console.error('Failed to fetch roles:', err);
      }
    };

    fetchUserRoles();
  }, [token, user.emp_id]);

  const handleRoleChange = (role) => {
    setCurrentView(role);
    if (onChangeView) {
      onChangeView(role);
    }
    setShowRoleDropdown(false);
  };

  const canAccessEmployees = userRoles.some(role => ['admin', 'manager'].includes(role));

  return (
    <header className="bg-white shadow-md sticky top-0 z-40">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo and Title */}
          <div className="flex items-center">
            <h1 className="text-2xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
              TaskFlow
            </h1>
          </div>

          {/* Navigation - Only show if onNavigate prop is provided */}
          {onNavigate && (
            <nav className="flex items-center gap-4">
              <button
                onClick={() => onNavigate('/dashboard')}
                className="flex items-center gap-2 px-4 py-2 text-gray-700 hover:bg-gray-100 rounded-lg transition-colors"
              >
                <LayoutDashboard size={18} />
                <span className="hidden sm:inline">Dashboard</span>
              </button>

              {canAccessEmployees && (
                <button
                  onClick={() => onNavigate('/employees')}
                  className="flex items-center gap-2 px-4 py-2 text-gray-700 hover:bg-gray-100 rounded-lg transition-colors"
                >
                  <Users size={18} />
                  <span className="hidden sm:inline">Employees</span>
                </button>
              )}
            </nav>
          )}

          {/* User Info and Controls */}
          <div className="flex items-center gap-4">
            {/* Role Selector */}
            {userRoles.length > 1 && (
              <div className="relative">
                <button
                  onClick={() => setShowRoleDropdown(!showRoleDropdown)}
                  className="flex items-center gap-2 px-4 py-2 bg-gray-100 hover:bg-gray-200 rounded-lg transition-colors"
                >
                  <span className="text-sm font-medium text-gray-700 capitalize">
                    {currentView}
                  </span>
                  <ChevronDown size={16} className="text-gray-600" />
                </button>

                {showRoleDropdown && (
                  <div className="absolute right-0 mt-2 w-48 bg-white rounded-lg shadow-lg border border-gray-200 py-1">
                    {userRoles.map(role => (
                      <button
                        key={role}
                        onClick={() => handleRoleChange(role)}
                        className={`w-full px-4 py-2 text-left text-sm hover:bg-gray-50 transition-colors capitalize ${
                          currentView === role ? 'bg-blue-50 text-blue-600 font-medium' : 'text-gray-700'
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
                <p className="text-sm font-medium text-gray-800">{user.name || 'User'}</p>
                <p className="text-xs text-gray-500">ID: {user.emp_id}</p>
              </div>

              <button
                onClick={logout}
                className="flex items-center gap-2 px-4 py-2 text-red-600 hover:bg-red-50 rounded-lg transition-colors"
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
      {userRoles.length === 1 && (
        <div className="sm:hidden border-t border-gray-200 px-4 py-2 bg-gray-50">
          <p className="text-xs text-gray-600">
            Role: <span className="font-medium capitalize">{currentView}</span>
          </p>
        </div>
      )}
    </header>
  );
};

export default Header;