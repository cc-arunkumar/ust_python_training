import React, { useEffect, useState } from 'react';
import { LayoutDashboard, LogOut, User } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';
import { api } from '../../services/api'; // adjust path if needed

const Header = ({ onChangeView }) => {
  const { user, logout } = useAuth();
  const [roles, setRoles] = useState([]);

  useEffect(() => {
    const fetchRoles = async () => {
      try {
        // if (!user?.emp_id || !user?.token) return;


        const userData = await api.getUserById(user.token, user.emp_id);


        if (userData && Array.isArray(userData.role)){
          setRoles(userData.role);
        } else {
          setRoles(['developer']); // fallback if no roles in DB
          console.warn('No roles found in DB response, defaulting to developer');
        }
        // console.log(`type of data`,typeof userData)
        // console.log('Setting roles from fetched user data:', userData.role);
        // setRoles(userData.role)
      } catch (err) {
        console.error('Failed to fetch roles:', err);
        setRoles(['developer']); // fallback
      }
    };

    fetchRoles();
  }, [user]);

  return (
    <header className="bg-white border-b border-gray-200 shadow-sm sticky top-0 z-10">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Left side: Logo + Title */}
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-gradient-to-br from-blue-600 to-purple-600 rounded-lg flex items-center justify-center">
              <LayoutDashboard className="text-white" size={24} />
            </div>
            <div>
              <h1 className="text-xl font-bold text-gray-900">Jira Lite</h1>
              <p className="text-xs text-gray-500 capitalize">
                {roles.join(', ')} Dashboard
              </p>
            </div>
          </div>

          {/* Right side: Role-based buttons + User info + Logout */}
          <div className="flex items-center gap-4">
            {/* Role-based view buttons */}
            {roles.length > 0 && (
              <div className="flex items-center gap-2">
                {roles.map((role) => (
                  <button
                    key={role}
                    onClick={() => onChangeView?.(role)}
                    className="px-3 py-2 text-sm font-medium text-gray-700 bg-gray-100 hover:bg-gray-200 rounded-lg transition-colors capitalize"
                  >
                    {role} View
                  </button>
                ))}
              </div>
            )}

            {/* User info */}
            <div className="flex items-center gap-2 px-3 py-2 bg-gray-100 rounded-lg">
              <User size={16} className="text-gray-600" />
              <span className="text-sm font-medium text-gray-700">
                ID: {user?.emp_id}
              </span>
            </div>

            {/* Logout */}
            <button
              onClick={logout}
              className="flex items-center gap-2 px-4 py-2 text-red-600 hover:bg-red-50 rounded-lg transition-colors"
            >
              <LogOut size={18} />
              <span className="text-sm font-medium">Logout</span>
            </button>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;