import { useEffect } from "react";
import { Settings, Users } from "lucide-react";

const RoleSelector = ({ user, onRoleSelect, onSwitchRole }) => {
  // Props: user, callbacks
  // Support user.role being a string (e.g. 'ADMIN') or an array (e.g. ['ADMIN','MANAGER'])
  const hasRole = (role) => {
    if (!user || user.role == null) return false;
    return Array.isArray(user.role)
      ? user.role.includes(role)
      : user.role === role;
  };

  useEffect(() => {
    // If user only has employee role, auto-select employee and skip selector
    if (hasRole("EMPLOYEE") && !hasRole("ADMIN") && !hasRole("MANAGER")) {
      onRoleSelect("EMPLOYEE");
    }
  }, [user, onRoleSelect]);

  if (!user) return null;
  // If user doesn't have any elevated role, nothing to select here
  if (!hasRole("ADMIN") && !hasRole("MANAGER")) return null;

  const handleRoleSelect = (role) => {
    onRoleSelect(role);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center p-4">
      <div className="bg-white rounded-2xl shadow-xl w-full max-w-2xl p-8">
        <h2 className="text-2xl font-bold text-gray-900 mb-2 text-center">
          Welcome, {user.name}
        </h2>
        <p className="text-gray-600 mb-8 text-center">
          Select your role to continue
        </p>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {hasRole("ADMIN") && (
            <button
              onClick={() => handleRoleSelect("ADMIN")}
              className="p-8 border-2 border-gray-200 rounded-xl hover:border-indigo-500 hover:bg-indigo-50 transition-all group"
            >
              <div className="flex flex-col items-center">
                <div className="w-16 h-16 bg-indigo-100 rounded-full flex items-center justify-center mb-4 group-hover:bg-indigo-200">
                  <Settings className="w-8 h-8 text-indigo-600" />
                </div>
                <h3 className="text-xl font-semibold text-gray-900 mb-2">
                  Admin Panel
                </h3>
                <p className="text-gray-600 text-center text-sm">
                  Manage employees, assign tasks, and configure system settings
                </p>
              </div>
            </button>
          )}
          {(hasRole("MANAGER") || hasRole("ADMIN")) && (
            <button
              onClick={() => handleRoleSelect("MANAGER")}
              className="p-8 border-2 border-gray-200 rounded-xl hover:border-green-500 hover:bg-green-50 transition-all group"
            >
              <div className="flex flex-col items-center">
                <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mb-4 group-hover:bg-green-200">
                  <Users className="w-8 h-8 text-green-600" />
                </div>
                <h3 className="text-xl font-semibold text-gray-900 mb-2">
                  Manager Dashboard
                </h3>
                <p className="text-gray-600 text-center text-sm">
                  Create tasks, review work, and manage team progress
                </p>
              </div>
            </button>
          )}
        </div>
      </div>
    </div>
  );
};

export default RoleSelector;
