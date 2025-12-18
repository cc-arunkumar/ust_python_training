import React, { useState, useEffect } from 'react';
import { X, User, Mail, Briefcase, UserCog, Phone, Building, Shield, Edit3 } from 'lucide-react';

const EditEmployeeModal = ({ token, employee, onClose, onSuccess, api }) => {
  const [formData, setFormData] = useState({
    emp_id: employee?.emp_id || '',
    name: employee?.name || '',
    email: employee?.email || '',
    designation: employee?.designation || '',
    manager_id: employee?.manager_id || '',
    status: employee?.status || 'active',
    department: employee?.department || '',
    phone: employee?.phone || ''
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    if (employee) {
      setFormData({
        emp_id: employee.emp_id || '',
        name: employee.name || '',
        email: employee.email || '',
        designation: employee.designation || '',
        manager_id: employee.manager_id || '',
        status: employee.status || 'active',
        department: employee.department || '',
        phone: employee.phone || ''
      });
    }
  }, [employee]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: name === 'emp_id' || name === 'manager_id' ? parseInt(value) || '' : value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const employeePayload = {
        name: formData.name,
        email: formData.email,
        designation: formData.designation,
        manager_id: formData.manager_id,
      };

      // Check if api is available
      if (!api || !api.updateEmployee) {
        throw new Error('API service not available');
      }

      await api.updateEmployee(
        token,
        formData.manager_id,
        formData.emp_id,
        employeePayload
      );

      onSuccess();
    } catch (err) {
      console.error('Error updating employee:', err);
      setError(err.message || 'Failed to update employee');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-gradient-to-br from-blue-500/20 via-purple-500/20 to-pink-500/20 backdrop-blur-sm flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-3xl shadow-2xl max-w-3xl w-full border-2 border-white/50 relative overflow-hidden">
        {/* Decorative background elements */}
        <div className="absolute top-0 right-0 w-96 h-96 bg-gradient-to-br from-blue-400/10 to-purple-400/10 rounded-full blur-3xl -z-10"></div>
        <div className="absolute bottom-0 left-0 w-96 h-96 bg-gradient-to-tr from-pink-400/10 to-blue-400/10 rounded-full blur-3xl -z-10"></div>

        {/* Header */}
        <div className="relative bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 px-8 py-6 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-12 h-12 bg-white/20 backdrop-blur-sm rounded-xl flex items-center justify-center">
              <Edit3 className="text-white" size={24} />
            </div>
            <div>
              <h2 className="text-2xl font-bold text-white">Edit Employee</h2>
              <p className="text-blue-100 text-sm">Update employee information</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-2 hover:bg-white/20 rounded-xl transition-all text-white"
          >
            <X size={24} />
          </button>
        </div>

        {/* Scrollable Content */}
        <div className="p-8">
          {error && (
            <div className="mb-6 p-4 bg-gradient-to-r from-red-50 to-pink-50 border-2 border-red-200 rounded-xl text-red-600 text-sm font-medium flex items-start gap-3">
              <div className="w-5 h-5 bg-red-500 rounded-full flex items-center justify-center flex-shrink-0 mt-0.5">
                <span className="text-white text-xs font-bold">!</span>
              </div>
              <span>{error}</span>
            </div>
          )}

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Employee ID - Read Only */}
            <div className="md:col-span-2">
              <label className="flex items-center gap-2 text-sm font-bold text-gray-700 mb-3">
                <Shield size={18} className="text-gray-500" />
                Employee ID (Read Only)
              </label>
              <input
                type="number"
                name="emp_id"
                value={formData.emp_id}
                readOnly
                className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl bg-gradient-to-r from-gray-100 to-gray-50 font-bold text-gray-600 cursor-not-allowed"
              />
            </div>

            {/* Full Name */}
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

            {/* Email */}
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

            {/* Designation */}
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
                placeholder="e.g., Software Engineer"
                className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-4 focus:ring-pink-500/20 focus:border-pink-500 transition-all outline-none bg-gray-50 hover:bg-white font-medium"
              />
            </div>

            {/* Department */}
            {/* <div>
              <label className="flex items-center gap-2 text-sm font-bold text-gray-700 mb-3">
                <Building size={18} className="text-indigo-600" />
                Department
              </label>
              <input
                type="text"
                name="department"
                value={formData.department}
                onChange={handleChange}
                placeholder="e.g., Engineering"
                className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-4 focus:ring-indigo-500/20 focus:border-indigo-500 transition-all outline-none bg-gray-50 hover:bg-white font-medium"
              />
            </div> */}

            {/* Phone */}
            {/* <div>
              <label className="flex items-center gap-2 text-sm font-bold text-gray-700 mb-3">
                <Phone size={18} className="text-green-600" />
                Phone
              </label>
              <input
                type="tel"
                name="phone"
                value={formData.phone}
                onChange={handleChange}
                placeholder="Enter phone number"
                className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-4 focus:ring-green-500/20 focus:border-green-500 transition-all outline-none bg-gray-50 hover:bg-white font-medium"
              />
            </div> */}

            {/* Status */}
            <div>
              <label className="flex items-center gap-2 text-sm font-bold text-gray-700 mb-3">
                <UserCog size={18} className="text-orange-600" />
                Status *
              </label>
              <div className="relative">
                <select
                  name="status"
                  value={formData.status}
                  onChange={handleChange}
                  required
                  className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-4 focus:ring-orange-500/20 focus:border-orange-500 transition-all outline-none bg-gray-50 hover:bg-white font-bold appearance-none cursor-pointer"
                >
                  <option value="active">✅ Active</option>
                  <option value="inactive">⛔ Inactive</option>
                </select>
                <div className={`absolute right-4 top-1/2 -translate-y-1/2 w-3 h-3 rounded-full ${
                  formData.status === 'active' 
                    ? 'bg-gradient-to-br from-green-500 to-emerald-500' 
                    : 'bg-gradient-to-br from-red-500 to-pink-500'
                }`}></div>
              </div>
            </div>
          </div>
        </div>

        {/* Footer with Action Buttons */}
        <div className="border-t-2 border-gray-100 p-8 bg-gradient-to-r from-gray-50/50 to-blue-50/30">
          <div className="flex gap-4">
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
                {loading ? 'Updating...' : '💾 Update Employee'}
              </span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default EditEmployeeModal;