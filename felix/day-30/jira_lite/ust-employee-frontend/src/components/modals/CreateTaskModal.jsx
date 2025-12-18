import React, { useState } from 'react';
import { api } from '../../services/api';

const CreateTaskModal = ({ token, empId, currentRole, employees = [], managers = [], onClose, onSuccess }) => {
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    assigned_to: '',                  // manager will set, admin leaves empty
    reviewer: '',                     // admin selects manager, manager uses own id
    priority: 'Low',
    status: 'To Do',
    expected_completion_date: ''
  });
  const [loading, setLoading] = useState(false);

  const isAdmin = currentRole === 'admin';
  const isManager = currentRole === 'manager';

  const handleSubmit = async () => {
    // common checks
    if (!formData.title || !formData.description || !formData.expected_completion_date) {
      alert('Please fill all required fields');
      return;
    }

    let payload = {
      title: formData.title,
      description: formData.description,
      priority: formData.priority,
      status: 'To Do',
      expected_completion_date: formData.expected_completion_date,
      assigned_by: empId,
      assigned_at: new Date().toISOString(),
      updated_by: empId,
      remarks: []
    };

    if (isAdmin) {
      // admin must select reviewer (manager)
      if (!formData.reviewer) {
        alert('Please select a reviewer (manager).');
        return;
      }
      payload = {
        ...payload,
        reviewer: parseInt(formData.reviewer, 10),
        assigned_to: null
      };
    } else if (isManager) {
      // manager: reviewer is themself; must assign to one of their developers
      if (!formData.assigned_to) {
        alert('Please select a developer to assign this task to.');
        return;
      }
      payload = {
        ...payload,
        reviewer: empId,
        assigned_to: parseInt(formData.assigned_to, 10)
      };
    } else {
      alert('You do not have permission to create tasks.');
      return;
    }

    setLoading(true);
    try {
      await api.createTask(token, payload);
      onSuccess();
    } catch (error) {
      console.error('Error creating task:', error);
      alert('Failed to create task');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
      <div className="bg-white rounded-2xl shadow-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        <div className="p-6 border-b border-gray-200 flex items-center justify-between">
          <h2 className="text-2xl font-bold text-gray-900">Create New Task</h2>
          <span className="text-xs text-gray-500 capitalize">Role: {currentRole}</span>
        </div>

        <div className="p-6 space-y-4">
          <div>
            <label className="block text-sm font-semibold text-gray-700 mb-2">
              Title *
            </label>
            <input
              type="text"
              value={formData.title}
              onChange={(e) => setFormData({ ...formData, title: e.target.value })}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
          </div>

          <div>
            <label className="block text-sm font-semibold text-gray-700 mb-2">
              Description *
            </label>
            <textarea
              value={formData.description}
              onChange={(e) => setFormData({ ...formData, description: e.target.value })}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              rows="4"
            />
          </div>

          <div className="grid grid-cols-2 gap-4">
            {isAdmin && (
              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  Reviewer (Manager) *
                </label>
                <select
                  value={formData.reviewer}
                  onChange={(e) => setFormData({ ...formData, reviewer: e.target.value })}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                >
                  <option value="">Select manager</option>
                  {managers.map((mgr) => (
                    <option key={mgr.emp_id} value={mgr.emp_id}>
                      {mgr.name} (ID: {mgr.emp_id})
                    </option>
                  ))}
                </select>
              </div>
            )}

            {isManager && (
              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  Assign To (Developer) *
                </label>
                <select
                  value={formData.assigned_to}
                  onChange={(e) => setFormData({ ...formData, assigned_to: e.target.value })}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                >
                  <option value="">Select developer</option>
                  {employees.map((emp) => (
                    <option key={emp.id || emp.emp_id} value={emp.emp_id ?? emp.id}>
                      {emp.name} (ID: {emp.emp_id ?? emp.id})
                    </option>
                  ))}
                </select>
              </div>
            )}

            <div>
              <label className="block text-sm font-semibold text-gray-700 mb-2">
                Priority
              </label>
              <select
                value={formData.priority}
                onChange={(e) => setFormData({ ...formData, priority: e.target.value })}
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              >
                <option value="Low">Low</option>
                <option value="Medium">Medium</option>
                <option value="High">High</option>
              </select>
            </div>
          </div>

          <div>
            <label className="block text-sm font-semibold text-gray-700 mb-2">
              Expected Completion Date *
            </label>
            <input
              type="date"
              value={formData.expected_completion_date}
              onChange={(e) =>
                setFormData({ ...formData, expected_completion_date: e.target.value })
              }
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
          </div>

          <div className="flex gap-3 pt-4">
            <button
              onClick={onClose}
              className="flex-1 px-6 py-3 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-semibold transition-colors"
            >
              Cancel
            </button>
            <button
              onClick={handleSubmit}
              disabled={loading}
              className="flex-1 px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-lg hover:shadow-lg font-semibold transition-all disabled:opacity-50"
            >
              {loading ? 'Creating...' : 'Create Task'}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CreateTaskModal;
