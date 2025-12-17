import React from 'react';
import { Shield, Users, Code } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { USER_ROLES, ROLE_DESCRIPTIONS } from '../../utils/constants';

const RoleSelector = () => {
  const { user, selectRole } = useAuth();

  const getRoleIcon = (role) => {
    switch (role) {
      case USER_ROLES.ADMIN:
        return <Shield size={48} className="text-purple-400" />;
      case USER_ROLES.MANAGER:
        return <Users size={48} className="text-blue-400" />;
      case USER_ROLES.DEVELOPER:
        return <Code size={48} className="text-green-400" />;
      default:
        return <Shield size={48} className="text-gray-400" />;
    }
  };

  const getRoleColor = (role) => {
    switch (role) {
      case USER_ROLES.ADMIN:
        return 'from-purple-600 to-purple-800 hover:from-purple-700 hover:to-purple-900';
      case USER_ROLES.MANAGER:
        return 'from-blue-600 to-blue-800 hover:from-blue-700 hover:to-blue-900';
      case USER_ROLES.DEVELOPER:
        return 'from-green-600 to-green-800 hover:from-green-700 hover:to-green-900';
      default:
        return 'from-gray-600 to-gray-800 hover:from-gray-700 hover:to-gray-900';
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 flex items-center justify-center p-4">
      <div className="max-w-4xl w-full">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-white mb-2">Select Your Role</h1>
          <p className="text-gray-400">
            You have access to multiple roles. Choose how you want to proceed.
          </p>
          <p className="text-gray-500 mt-2">
            Logged in as: <span className="text-blue-400">{user?.email}</span>
          </p>
        </div>

        <div className="grid gap-6 md:grid-cols-3">
          {user?.role?.map((role) => (
            <button
              key={role}
              onClick={() => selectRole(role)}
              className={`bg-gradient-to-br ${getRoleColor(role)} p-6 rounded-xl shadow-xl transform transition-all duration-200 hover:scale-105 hover:shadow-2xl`}
            >
              <div className="flex flex-col items-center space-y-4">
                <div className="bg-white bg-opacity-10 p-4 rounded-full">
                  {getRoleIcon(role)}
                </div>
                <div className="text-center">
                  <h3 className="text-2xl font-bold text-white mb-2">
                    {role}
                  </h3>
                  <p className="text-gray-200 text-sm">
                    {ROLE_DESCRIPTIONS[role]}
                  </p>
                </div>
              </div>
            </button>
          ))}
        </div>

        <div className="mt-8 text-center">
          <p className="text-gray-400 text-sm">
            You can change your role anytime from the settings menu
          </p>
        </div>
      </div>
    </div>
  );
};

export default RoleSelector;