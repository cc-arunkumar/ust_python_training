import React, { useState } from 'react';
import { X, AlertCircle, UserPlus } from 'lucide-react';
import ApiService from '../../services/api';
import toast from 'react-hot-toast';

const inputClass =
  "mt-1 w-full rounded-xl border border-gray-200 bg-white px-3 py-2 text-sm " +
  "focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition";

const EmployeeModal = ({ employee, onClose, onSuccess }) => {
  const [formData, setFormData] = useState({
    emp_id: employee?.emp_id ?? '',
    emp_name: employee?.emp_name ?? '',
    email: employee?.email ?? '',
    designation: employee?.designation ?? '',
    manager_id: employee?.manager_id ?? '',
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleChange = (field, value) => {
    setFormData(prev => ({ ...prev, [field]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const payload = {
        emp_id: Number(formData.emp_id),
        emp_name: formData.emp_name.trim(),
        email: formData.email.trim(),
        designation: formData.designation.trim(),
        manager_id:
          formData.manager_id === '' ? null : Number(formData.manager_id),
      };

      if (employee) {
        await ApiService.updateEmployee(employee.emp_id, payload);
        toast.success('Employee updated successfully');
      } else {
        await ApiService.createEmployee(payload);
        toast.success('Employee added successfully');
      }

      onSuccess();
    } catch (err) {
      const msg = err?.response?.data?.detail || err.message || 'Operation failed';
      setError(msg);
      toast.error(msg);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40 backdrop-blur-sm">
      <div className="w-full max-w-xl rounded-2xl bg-white shadow-xl border border-gray-200">

        {/* Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-gray-200">
          <div className="flex items-center gap-2">
            <UserPlus className="text-blue-600" />
            <h2 className="text-lg font-semibold text-gray-800">
              {employee ? 'Edit Employee' : 'Add Employee'}
            </h2>
          </div>
          <button onClick={onClose} className="text-gray-400 hover:text-gray-700">
            <X />
          </button>
        </div>

        {/* Error */}
        {error && (
          <div className="mx-6 mt-4 flex items-center gap-2 rounded-xl bg-red-50 px-4 py-3 text-red-700 border border-red-200">
            <AlertCircle size={18} />
            <span className="text-sm">{error}</span>
          </div>
        )}

        {/* Form */}
        <form onSubmit={handleSubmit} className="px-6 py-6 space-y-4">

          {!employee && (
            <div>
              <label className="text-sm font-medium text-gray-600">
                Employee ID *
              </label>
              <input
                type="number"
                value={formData.emp_id}
                onChange={(e) => handleChange('emp_id', e.target.value)}
                required
                className={inputClass}
              />
            </div>
          )}

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label className="text-sm font-medium text-gray-600">Name *</label>
              <input
                type="text"
                value={formData.emp_name}
                onChange={(e) => handleChange('emp_name', e.target.value)}
                required
                className={inputClass}
              />
            </div>

            <div>
              <label className="text-sm font-medium text-gray-600">Email *</label>
              <input
                type="email"
                value={formData.email}
                onChange={(e) => handleChange('email', e.target.value)}
                required
                className={inputClass}
              />
            </div>
          </div>

          <div>
            <label className="text-sm font-medium text-gray-600">
              Designation *
            </label>
            <input
              type="text"
              value={formData.designation}
              onChange={(e) => handleChange('designation', e.target.value)}
              required
              className={inputClass}
            />
          </div>

          <div>
            <label className="text-sm font-medium text-gray-600">
              Manager ID (Optional)
            </label>
            <input
              type="number"
              value={formData.manager_id}
              onChange={(e) => handleChange('manager_id', e.target.value)}
              className={inputClass}
            />
          </div>

          {/* Buttons */}
          <div className="flex gap-3 pt-6">
            <button
              type="button"
              onClick={onClose}
              className="flex-1 rounded-xl border border-gray-300 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 transition"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={loading}
              className="flex-1 rounded-xl bg-blue-600 py-2 text-sm font-medium text-white hover:bg-blue-700 disabled:bg-blue-400 transition"
            >
              {loading ? 'Saving...' : 'Save'}
            </button>
          </div>

        </form>
      </div>
    </div>
  );
};

export default EmployeeModal;
