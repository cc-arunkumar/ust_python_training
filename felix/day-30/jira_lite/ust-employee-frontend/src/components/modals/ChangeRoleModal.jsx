import React, { useState, useEffect } from 'react';
import { X, Shield } from 'lucide-react';
import { api } from '../../services/api';

const ChangeRoleModal = ({ token, employee, onClose, onSuccess }) => {
  const [currentRoles, setCurrentRoles] = useState([]);
  const [selectedRoles, setSelectedRoles] = useState([]);
  const [loading, setLoading] = useState(false);
  const [fetchLoading, setFetchLoading] = useState(true);
  const [error, setError] = useState('');

  const availableRoles = ['developer', 'manager', 'admin'];

  useEffect(() => {
    fetchCurrentRoles();
  }, []);

  const fetchCurrentRoles = async () => {
    try {
      setFetchLoading(true);
      const userData = await api.getUserById(token, employee.emp_id);
      const roles = Array.isArray(userData.role) ? userData.role : [];
      setCurrentRoles(roles);
      setSelectedRoles(roles);
    } catch (err) {
      console.error('Error fetching user roles:', err);
      setError('Failed to fetch current roles');
    } finally {
      setFetchLoading(false);
    }
  };

  const handleRoleToggle = (role) => {
    setSelectedRoles(prev => {
      if (prev.includes(role)) {
        // Prevent removing all roles
        if (prev.length === 1) {
          setError('User must have at least one role');
          return prev;
        }
        return prev.filter(r => r !== role);
      } else {
        setError('');
        return [...prev, role];
      }
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (selectedRoles.length === 0) {
      setError('Please select at least one role');
      return;
    }

    setError('');
    setLoading(true);

    try {
      // Send roles as array to backend
      await api.updateUserRole(token, employee.emp_id, { role: selectedRoles });
      onSuccess();
    } catch (err) {
      console.error('Error updating roles:', err);
      setError(err.message || 'Failed to update roles');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-lg shadow-xl max-w-md w-full">
        <div className="border-b border-gray-200 px-6 py-4 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Shield className="text-purple-600" size={24} />
            <h2 className="text-xl font-bold text-gray-800">Change User Role</h2>
          </div>
          <button
            onClick={onClose}
            className="p-2 hover:bg-gray-100 rounded-lg transition-colors"
          >
            <X size={20} />
          </button>
        </div>

        <form onSubmit={handleSubmit} className="p-6">
          {error && (
            <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-600 text-sm">
              {error}
            </div>
          )}

          <div className="mb-4">
            <p className="text-sm text-gray-600 mb-1">Employee</p>
            <p className="text-lg font-semibold text-gray-800">{employee.name}</p>
            <p className="text-sm text-gray-500">ID: {employee.emp_id}</p>
          </div>

          {fetchLoading ? (
            <div className="py-8 text-center">
              <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mx-auto"></div>
              <p className="text-gray-600 mt-2 text-sm">Loading roles...</p>
            </div>
          ) : (
            <>
              <div className="mb-4">
                <label className="block text-sm font-medium text-gray-700 mb-3">
                  Select Roles (can select multiple)
                </label>
                <div className="space-y-2">
                  {availableRoles.map(role => (
                    <label
                      key={role}
                      className="flex items-center p-3 border border-gray-300 rounded-lg hover:bg-gray-50 cursor-pointer transition-colors"
                    >
                      <input
                        type="checkbox"
                        checked={selectedRoles.includes(role)}
                        onChange={() => handleRoleToggle(role)}
                        className="w-4 h-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                      />
                      <span className="ml-3 text-gray-700 capitalize font-medium">
                        {role}
                      </span>
                      {role === 'admin' && (
                        <span className="ml-auto text-xs bg-purple-100 text-purple-700 px-2 py-1 rounded">
                          Full Access
                        </span>
                      )}
                      {role === 'manager' && (
                        <span className="ml-auto text-xs bg-blue-100 text-blue-700 px-2 py-1 rounded">
                          Team Lead
                        </span>
                      )}
                      {role === 'developer' && (
                        <span className="ml-auto text-xs bg-green-100 text-green-700 px-2 py-1 rounded">
                          Base Role
                        </span>
                      )}
                    </label>
                  ))}
                </div>
              </div>

              <div className="p-3 bg-blue-50 border border-blue-200 rounded-lg text-blue-700 text-sm mb-4">
                <p className="font-semibold mb-1">Role Permissions:</p>
                <ul className="list-disc list-inside space-y-1 text-xs">
                  <li><strong>Admin:</strong> Full system access, manage all employees</li>
                  <li><strong>Manager:</strong> Create tasks, manage team members</li>
                  <li><strong>Developer:</strong> View and update assigned tasks</li>
                </ul>
              </div>

              <div className="flex gap-3 justify-end">
                <button
                  type="button"
                  onClick={onClose}
                  className="px-6 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 transition-colors"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  disabled={loading || selectedRoles.length === 0}
                  className="px-6 py-2 bg-gradient-to-r from-purple-600 to-blue-600 text-white rounded-lg hover:shadow-lg transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  {loading ? 'Updating...' : 'Update Roles'}
                </button>
              </div>
            </>
          )}
        </form>
      </div>
    </div>
  );
};

export default ChangeRoleModal;
