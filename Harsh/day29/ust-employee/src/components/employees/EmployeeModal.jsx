import React, { useState } from 'react';
import { X, AlertCircle } from 'lucide-react';
import ApiService from '../../services/api';

const EmployeeModal = ({ employee, onClose, onSuccess }) => {
  const [formData, setFormData] = useState({
    emp_id: employee?.emp_id || '',
    emp_name: employee?.emp_name || '',
    email: employee?.email || '',
    designation: employee?.designation || '',
    manager_id: employee?.manager_id || '',
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
      const payload = { ...formData };
      
      // Convert to appropriate types
      if (payload.emp_id) {
        payload.emp_id = parseInt(payload.emp_id);
      }
      if (payload.manager_id) {
        payload.manager_id = parseInt(payload.manager_id);
      } else {
        payload.manager_id = null;
      }

      if (employee) {
        await ApiService.updateEmployee(employee.emp_id, payload);
      } else {
        await ApiService.createEmployee(payload);
      }
      
      onSuccess();
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center p-4 z-50">
      <div className="bg-gray-800 rounded-lg shadow-2xl p-6 w-full max-w-md border border-gray-700">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-2xl font-bold text-white">
            {employee ? 'Edit Employee' : 'Add Employee'}
          </h2>
          <button
            onClick={onClose}
            className="text-gray-400 hover:text-gray-200 transition"
          >
            <X size={24} />
          </button>
        </div>

        {error && (
          <div className="bg-red-900 bg-opacity-50 border border-red-700 text-red-200 px-4 py-3 rounded mb-4 flex items-start gap-2">
            <AlertCircle size={20} className="flex-shrink-0 mt-0.5" />
            <span className="text-sm">{error}</span>
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4">
          {!employee && (
            <div>
              <label className="block text-sm font-medium text-gray-300 mb-1">
                Employee ID *
              </label>
              <input
                type="number"
                value={formData.emp_id}
                onChange={(e) => handleChange('emp_id', e.target.value)}
                className="w-full px-3 py-2 bg-gray-700 border border-gray-600 text-white rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none"
                required
              />
            </div>
          )}

          <div>
            <label className="block text-sm font-medium text-gray-300 mb-1">
              Employee Name *
            </label>
            <input
              type="text"
              value={formData.emp_name}
              onChange={(e) => handleChange('emp_name', e.target.value)}
              className="w-full px-3 py-2 bg-gray-700 border border-gray-600 text-white rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-300 mb-1">
              Email *
            </label>
            <input
              type="email"
              value={formData.email}
              onChange={(e) => handleChange('email', e.target.value)}
              className="w-full px-3 py-2 bg-gray-700 border border-gray-600 text-white rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-300 mb-1">
              Designation *
            </label>
            <input
              type="text"
              value={formData.designation}
              onChange={(e) => handleChange('designation', e.target.value)}
              className="w-full px-3 py-2 bg-gray-700 border border-gray-600 text-white rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none"
              placeholder="e.g., Senior Developer"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-300 mb-1">
              Manager ID (Optional)
            </label>
            <input
              type="number"
              value={formData.manager_id}
              onChange={(e) => handleChange('manager_id', e.target.value)}
              className="w-full px-3 py-2 bg-gray-700 border border-gray-600 text-white rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none"
              placeholder="Leave empty if no manager"
            />
          </div>

          <div className="flex gap-3 pt-4">
            <button
              type="button"
              onClick={onClose}
              className="flex-1 px-4 py-2 border border-gray-600 text-gray-300 rounded-lg hover:bg-gray-700 transition font-medium"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={loading}
              className="flex-1 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 disabled:bg-blue-800 disabled:cursor-not-allowed transition font-medium"
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