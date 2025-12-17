import React from 'react';
import { Shield, Users, Code, ArrowRight } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { USER_ROLES, ROLE_DESCRIPTIONS } from '../../utils/constants';

const RoleSelector = () => {
  const { user, selectRole } = useAuth();

  const ROLE_META = {
    [USER_ROLES.ADMIN]: {
      icon: <Shield size={26} className="text-purple-600" />,
      accent: 'hover:border-purple-400'
    },
    [USER_ROLES.MANAGER]: {
      icon: <Users size={26} className="text-blue-600" />,
      accent: 'hover:border-blue-400'
    },
    [USER_ROLES.DEVELOPER]: {
      icon: <Code size={26} className="text-green-600" />,
      accent: 'hover:border-green-400'
    }
  };

  return (
    <div className="min-h-screen grid grid-cols-1 lg:grid-cols-2">

      {/* LEFT PANEL */}
      <div className="hidden lg:flex flex-col justify-between p-12 bg-gradient-to-br from-indigo-600 to-blue-700 text-white">
        <div>
          <h1 className="text-4xl font-bold mb-4">
            TaskFlow
          </h1>
          <p className="text-indigo-100 max-w-sm">
            A unified workspace to manage tasks, teams, and delivery — all in one place.
          </p>
        </div>

        <div className="space-y-3 text-sm text-indigo-100">
          <p>✔ Role-based dashboards</p>
          <p>✔ Secure task management</p>
          <p>✔ Real-time collaboration</p>
        </div>

        <p className="text-xs text-indigo-200">
          © 2025 TaskFlow Inc.
        </p>
      </div>

      {/* RIGHT PANEL */}
      <div className="flex items-center justify-center bg-gray-50 px-6">
        <div className="w-full max-w-lg">

          {/* Header */}
          <div className="mb-8">
            <h2 className="text-3xl font-bold text-gray-900">
              Choose how you want to continue
            </h2>
            <p className="text-gray-500 mt-2">
              You’re signed in as <span className="font-medium">{user?.email}</span>
            </p>
          </div>

          {/* Role List */}
          <div className="space-y-4">
            {user?.role?.map((role) => (
              <button
                key={role}
                onClick={() => selectRole(role)}
                className={`group w-full flex items-center justify-between p-5 rounded-xl 
                            bg-white border border-gray-200 transition-all duration-300
                            hover:shadow-lg hover:-translate-y-1 ${ROLE_META[role]?.accent}`}
              >
                <div className="flex items-center gap-4">
                  <div className="p-3 rounded-lg bg-gray-100">
                    {ROLE_META[role]?.icon}
                  </div>
                  <div className="text-left">
                    <h3 className="text-lg font-semibold text-gray-800">
                      {role}
                    </h3>
                    <p className="text-sm text-gray-500">
                      {ROLE_DESCRIPTIONS[role]}
                    </p>
                  </div>
                </div>

                <ArrowRight
                  size={20}
                  className="text-gray-400 group-hover:text-gray-700 transition"
                />
              </button>
            ))}
          </div>

          {/* Footer */}
          <p className="mt-8 text-xs text-gray-400">
            Your access level determines what features are available.
          </p>
        </div>
      </div>
    </div>
  );
};

export default RoleSelector;
