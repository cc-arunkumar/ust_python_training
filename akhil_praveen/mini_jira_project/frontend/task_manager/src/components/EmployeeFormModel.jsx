import React, { useState, useEffect } from 'react';

function EmployeeFormModal({ employee, employees, onClose, onSave }) {
  const [formData, setFormData] = useState({
    emp_name: '',
    email: '',
    designation: '',
    manager_id: null,
  });

  useEffect(() => {
    if (employee) {
      setFormData({
        emp_name: employee.emp_name || '',
        email: employee.email || '',
        designation: employee.designation || '',
        manager_id: employee.manager_id || null,
      });
    }
  }, [employee]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    await onSave(formData);
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg p-6 w-full max-w-md">
        <h2 className="text-2xl font-bold mb-4">
          {employee ? 'Edit Employee' : 'Add New Employee'}
        </h2>
        
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-1">Name *</label>
            <input
              type="text"
              value={formData.emp_name}
              onChange={(e) =>
                setFormData({ ...formData, emp_name: e.target.value })
              }
              className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium mb-1">Email *</label>
            <input
              type="email"
              value={formData.email}
              onChange={(e) =>
                setFormData({ ...formData, email: e.target.value })
              }
              className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium mb-1">Designation</label>
            <input
              type="text"
              value={formData.designation}
              onChange={(e) =>
                setFormData({ ...formData, designation: e.target.value })
              }
              className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div>
            <label className="block text-sm font-medium mb-1">Manager</label>
            <select
              value={formData.manager_id || ''}
              onChange={(e) =>
                setFormData({
                  ...formData,
                  manager_id: e.target.value ? parseInt(e.target.value) : null,
                })
              }
              className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
            >
              <option value="">No Manager</option>
              {employees
                .filter((emp) => !employee || emp.emp_id !== employee.emp_id)
                .map((emp) => (
                  <option key={emp.emp_id} value={emp.emp_id}>
                    {emp.emp_name}
                  </option>
                ))}
            </select>
          </div>

          <div className="flex gap-2 justify-end">
            <button
              type="submit"
              className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
            >
              {employee ? 'Update' : 'Create'}
            </button>
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 bg-gray-300 rounded-lg hover:bg-gray-400"
            >
              Cancel
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default EmployeeFormModal;