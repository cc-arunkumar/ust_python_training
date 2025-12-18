import React, { useState } from 'react';
import { X, Shield, Eye, EyeOff, AlertCircle } from 'lucide-react';
import { api } from '../../services/api';

const CreateUserModal = ({ token, onClose, onSuccess }) => {
  const [formData, setFormData] = useState({
    emp_id: '',
    password: '',
    role: [],
    status: 'active'
  });
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const availableRoles = ['admin', 'manager', 'developer'];

  const handleRoleToggle = (role) => {
    setFormData(prev => ({
      ...prev,
      role: prev.role.includes(role)
        ? prev.role.filter(r => r !== role)
        : [...prev.role, role]
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    if (!formData.emp_id) {
      setError('Employee ID is required');
      return;
    }
    if (!formData.password || formData.password.length < 4) {
      setError('Password must be at least 4 characters');
      return;
    }
    if (formData.role.length === 0) {
      setError('At least one role must be selected');
      return;
    }

    setLoading(true);
    try {
      await api.createUser(token, {
        emp_id: parseInt(formData.emp_id),
        password: formData.password,
        role: formData.role,
        status: formData.status
      });
      onSuccess();
    } catch (err) {
      setError(err.message || 'Failed to create user');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-3xl shadow-2xl max-w-md w-full max-h-[90vh] overflow-y-auto border-2 border-gray-100">
        {/* Header */}
        <div className="sticky top-0 bg-gradient-to-r from-red-500 to-pink-600 p-6 rounded-t-3xl border-b-2 border-pink-200">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-12 h-12 bg-white/20 backdrop-blur-sm rounded-xl flex items-center justify-center">
                <Shield className="text-white" size={24} />
              </div>
              <div>
                <h2 className="text-2xl font-bold text-white">Create New User</h2>
                <p className="text-pink-100 text-sm mt-1">Add system access for an employee</p>
              </div>
            </div>
            <button
              onClick={onClose}
              className="p-2 hover:bg-white/20 rounded-xl transition-all text-white"
            >
              <X size={24} />
            </button>
          </div>
        </div>

        {/* Form */}
        <form onSubmit={handleSubmit} className="p-6 space-y-5">
          {error && (
            <div className="bg-red-50 border-2 border-red-200 rounded-xl p-4 flex items-start gap-3">
              <AlertCircle className="text-red-600 flex-shrink-0 mt-0.5" size={20} />
              <div>
                <p className="text-red-900 font-semibold text-sm">Error</p>
                <p className="text-red-700 text-sm mt-1">{error}</p>
              </div>
            </div>
          )}

          {/* Employee ID */}
          <div>
            <label className="block text-sm font-bold text-gray-700 mb-2">
              Employee ID *
            </label>
            <input
              type="number"
              required
              value={formData.emp_id}
              onChange={(e) => setFormData({ ...formData, emp_id: e.target.value })}
              className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-4 focus:ring-red-500/20 focus:border-red-500 transition-all outline-none font-medium"
              placeholder="Enter employee ID"
            />
            <p className="text-xs text-gray-500 mt-1">Must match an existing employee record</p>
          </div>

          {/* Password */}
          <div>
            <label className="block text-sm font-bold text-gray-700 mb-2">
              Password *
            </label>
            <div className="relative">
              <input
                type={showPassword ? 'text' : 'password'}
                required
                value={formData.password}
                onChange={(e) => setFormData({ ...formData, password: e.target.value })}
                className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-4 focus:ring-red-500/20 focus:border-red-500 transition-all outline-none font-medium pr-12"
                placeholder="Enter password"
              />
              <button
                type="button"
                onClick={() => setShowPassword(!showPassword)}
                className="absolute right-3 top-1/2 transform -translate-y-1/2 p-2 hover:bg-gray-100 rounded-lg transition-all"
              >
                {showPassword ? <EyeOff size={18} className="text-gray-500" /> : <Eye size={18} className="text-gray-500" />}
              </button>
            </div>
            <p className="text-xs text-gray-500 mt-1">Minimum 4 characters</p>
          </div>

          {/* Roles */}
          <div>
            <label className="block text-sm font-bold text-gray-700 mb-3">
              Roles * (Select at least one)
            </label>
            <div className="space-y-2">
              {availableRoles.map((role) => (
                <label
                  key={role}
                  className={`flex items-center gap-3 p-4 border-2 rounded-xl cursor-pointer transition-all ${
                    formData.role.includes(role)
                      ? 'border-red-500 bg-red-50 shadow-md'
                      : 'border-gray-200 hover:border-gray-300 hover:bg-gray-50'
                  }`}
                >
                  <input
                    type="checkbox"
                    checked={formData.role.includes(role)}
                    onChange={() => handleRoleToggle(role)}
                    className="w-5 h-5 text-red-600 rounded focus:ring-2 focus:ring-red-500"
                  />
                  <div className="flex-1">
                    <span className={`font-bold capitalize ${
                      formData.role.includes(role) ? 'text-red-900' : 'text-gray-700'
                    }`}>
                      {role}
                    </span>
                    <p className="text-xs text-gray-500 mt-0.5">
                      {role === 'admin' && 'Full system access and user management'}
                      {role === 'manager' && 'Manage team and assign tasks'}
                      {role === 'employee' && 'View and complete assigned tasks'}
                    </p>
                  </div>
                </label>
              ))}
            </div>
          </div>

          {/* Status */}
          <div>
            <label className="block text-sm font-bold text-gray-700 mb-2">
              Status
            </label>
            <select
              value={formData.status}
              onChange={(e) => setFormData({ ...formData, status: e.target.value })}
              className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-4 focus:ring-red-500/20 focus:border-red-500 transition-all outline-none font-medium"
            >
              <option value="active">Active</option>
              <option value="inactive">Inactive</option>
            </select>
          </div>

          {/* Buttons */}
          <div className="flex gap-3 pt-4">
            <button
              type="button"
              onClick={onClose}
              className="flex-1 px-6 py-3 border-2 border-gray-300 text-gray-700 rounded-xl hover:bg-gray-50 transition-all font-bold"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={loading}
              className="flex-1 px-6 py-3 bg-gradient-to-r from-red-600 to-pink-600 text-white rounded-xl hover:shadow-xl transition-all font-bold disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {loading ? 'Creating...' : 'Create User'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default CreateUserModal;