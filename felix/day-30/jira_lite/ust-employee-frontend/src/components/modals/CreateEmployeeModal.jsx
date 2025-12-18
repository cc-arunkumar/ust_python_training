import React, { useState } from 'react';
import { X, User, Mail, Briefcase, UserCog } from 'lucide-react';

const CreateEmployeeModal = ({ token, managerId, onClose, onSuccess }) => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    designation: '',
    manager_id: managerId
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: name === 'manager_id' ? parseInt(value) || '' : value
    }));
  };

  const handleSubmit = async () => {
    setError('');
    setLoading(true);

    try {
      // Validate required fields
      if (!formData.name || !formData.email || !formData.designation || !formData.manager_id) {
        throw new Error('Please fill in all required fields');
      }

      // Employee payload (matches backend Employee model)
      const employeePayload = {
        name: formData.name,
        email: formData.email,
        designation: formData.designation,
        manager_id: formData.manager_id
      };

      // Make API call to create employee
      const API_BASE_URL = 'http://localhost:8000/api/v1'
      
      const response = await fetch(`${API_BASE_URL}/employees`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(employeePayload)
      });

      if (!response.ok) {
        let errorMessage = 'Failed to create employee';
        try {
          const errorData = await response.json();
          errorMessage = errorData.message || errorData.detail || errorMessage;
        } catch {
          errorMessage = `Error: ${response.status} ${response.statusText}`;
        }
        throw new Error(errorMessage);
      }

      // Try to parse response, but don't fail if empty
      try {
        await response.json();
      } catch {
        // Some APIs return empty response on success
      }

      onSuccess();
    } catch (err) {
      console.error('Error creating employee:', err);
      setError(err.message || 'Failed to create employee');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-gradient-to-br from-blue-500/20 via-purple-500/20 to-pink-500/20 backdrop-blur-sm flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-3xl shadow-2xl max-w-lg w-full border-2 border-white/50 relative overflow-hidden">
        {/* Decorative background elements */}
        <div className="absolute top-0 right-0 w-64 h-64 bg-gradient-to-br from-blue-400/10 to-purple-400/10 rounded-full blur-3xl -z-10"></div>
        <div className="absolute bottom-0 left-0 w-64 h-64 bg-gradient-to-tr from-pink-400/10 to-blue-400/10 rounded-full blur-3xl -z-10"></div>

        {/* Header */}
        <div className="relative bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 px-8 py-6 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-12 h-12 bg-white/20 backdrop-blur-sm rounded-xl flex items-center justify-center">
              <User className="text-white" size={24} />
            </div>
            <div>
              <h2 className="text-2xl font-bold text-white">Create Employee</h2>
              <p className="text-blue-100 text-sm">Add a new team member</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-2 hover:bg-white/20 rounded-xl transition-all text-white"
          >
            <X size={24} />
          </button>
        </div>

        {/* Content */}
        <div className="p-8">
          {error && (
            <div className="mb-6 p-4 bg-gradient-to-r from-red-50 to-pink-50 border-2 border-red-200 rounded-xl text-red-600 text-sm font-medium flex items-start gap-3">
              <div className="w-5 h-5 bg-red-500 rounded-full flex items-center justify-center flex-shrink-0 mt-0.5">
                <span className="text-white text-xs font-bold">!</span>
              </div>
              <span>{error}</span>
            </div>
          )}

          <div className="space-y-5">
            <div>
              <label className="flex items-center gap-2 text-sm font-bold text-gray-700 mb-3">
                <User size={18} className="text-blue-600" />
                Full Name *
              </label>
              <input
                type="text"
                name="name"
                value={formData.name}
                onChange={handleChange}
                required
                placeholder="Enter full name..."
                className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-4 focus:ring-blue-500/20 focus:border-blue-500 transition-all outline-none bg-gray-50 hover:bg-white font-medium"
              />
            </div>

            <div>
              <label className="flex items-center gap-2 text-sm font-bold text-gray-700 mb-3">
                <Mail size={18} className="text-purple-600" />
                Email *
              </label>
              <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                required
                placeholder="employee@company.com"
                className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-4 focus:ring-purple-500/20 focus:border-purple-500 transition-all outline-none bg-gray-50 hover:bg-white font-medium"
              />
            </div>

            <div>
              <label className="flex items-center gap-2 text-sm font-bold text-gray-700 mb-3">
                <Briefcase size={18} className="text-pink-600" />
                Designation *
              </label>
              <input
                type="text"
                name="designation"
                value={formData.designation}
                onChange={handleChange}
                required
                placeholder="e.g., Software Engineer, Manager"
                className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-4 focus:ring-pink-500/20 focus:border-pink-500 transition-all outline-none bg-gray-50 hover:bg-white font-medium"
              />
            </div>

            <div>
              <label className="flex items-center gap-2 text-sm font-bold text-gray-700 mb-3">
                <UserCog size={18} className="text-indigo-600" />
                Manager ID *
              </label>
              <input
                type="number"
                name="manager_id"
                value={formData.manager_id}
                onChange={handleChange}
                required
                placeholder="Enter manager ID..."
                className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-4 focus:ring-indigo-500/20 focus:border-indigo-500 transition-all outline-none bg-gray-50 hover:bg-white font-medium"
              />
            </div>
          </div>

          {/* Action Buttons */}
          <div className="flex gap-4 mt-8">
            <button
              type="button"
              onClick={onClose}
              className="flex-1 px-6 py-4 border-2 border-gray-300 text-gray-700 rounded-xl hover:bg-gray-50 font-bold transition-all hover:scale-105 hover:shadow-lg"
            >
              Cancel
            </button>
            <button
              type="button"
              onClick={handleSubmit}
              disabled={loading}
              className="flex-1 px-6 py-4 bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 text-white rounded-xl hover:shadow-2xl font-bold transition-all disabled:opacity-50 disabled:cursor-not-allowed hover:scale-105 relative overflow-hidden group"
            >
              <div className="absolute inset-0 bg-gradient-to-r from-pink-600 via-purple-600 to-blue-600 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
              <span className="relative z-10">
                {loading ? 'Creating...' : '✨ Create Employee'}
              </span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CreateEmployeeModal;