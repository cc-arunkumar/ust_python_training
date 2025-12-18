import React, { useState } from 'react';
import { X, CheckCircle, Calendar, AlertCircle, User, Users } from 'lucide-react';

const CreateTaskModal = ({ token, empId, currentRole, employees = [], managers = [], onClose, onSuccess, api }) => {
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    assigned_to: '',
    reviewer: '',
    priority: 'Low',
    status: 'To Do',
    expected_completion_date: ''
  });
  const [loading, setLoading] = useState(false);

  const isAdmin = currentRole === 'admin';
  const isManager = currentRole === 'manager';

  const handleSubmit = async () => {
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

  const priorityColors = {
    Low: 'from-green-500 to-emerald-500',
    Medium: 'from-yellow-500 to-orange-500',
    High: 'from-red-500 to-pink-500'
  };

  return (
    <div className="fixed inset-0 bg-gradient-to-br from-blue-500/20 via-purple-500/20 to-pink-500/20 backdrop-blur-sm flex items-center justify-center p-4 z-50">
      <div className="bg-white rounded-3xl shadow-2xl w-full max-w-3xl border-2 border-white/50 relative overflow-hidden">
        {/* Decorative background elements */}
        <div className="absolute top-0 right-0 w-96 h-96 bg-gradient-to-br from-blue-400/10 to-purple-400/10 rounded-full blur-3xl -z-10"></div>
        <div className="absolute bottom-0 left-0 w-96 h-96 bg-gradient-to-tr from-pink-400/10 to-blue-400/10 rounded-full blur-3xl -z-10"></div>

        {/* Header */}
        <div className="relative bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 px-8 py-6 flex items-center justify-between">
          <div>
            <h2 className="text-2xl font-bold text-white mb-1">Create New Task</h2>
            <div className="flex items-center gap-2">
              <span className="px-3 py-1 bg-white/20 backdrop-blur-sm rounded-full text-xs font-semibold text-white capitalize">
                {currentRole}
              </span>
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
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Title - Full Width */}
            <div className="md:col-span-2">
              <label className="flex items-center gap-2 text-sm font-bold text-gray-700 mb-3">
                <CheckCircle size={18} className="text-blue-600" />
                Task Title *
              </label>
              <input
                type="text"
                value={formData.title}
                onChange={(e) => setFormData({ ...formData, title: e.target.value })}
                placeholder="Enter a descriptive title..."
                className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-4 focus:ring-blue-500/20 focus:border-blue-500 transition-all outline-none bg-gray-50 hover:bg-white font-medium"
              />
            </div>

            {/* Description - Full Width */}
            <div className="md:col-span-2">
              <label className="flex items-center gap-2 text-sm font-bold text-gray-700 mb-3">
                <AlertCircle size={18} className="text-purple-600" />
                Description *
              </label>
              <textarea
                value={formData.description}
                onChange={(e) => setFormData({ ...formData, description: e.target.value })}
                placeholder="Provide detailed information about the task..."
                className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-4 focus:ring-purple-500/20 focus:border-purple-500 transition-all outline-none bg-gray-50 hover:bg-white font-medium resize-none"
                rows="3"
              />
            </div>

            {/* Conditional Fields */}
            {isAdmin && (
              <div className="md:col-span-2">
                <label className="flex items-center gap-2 text-sm font-bold text-gray-700 mb-3">
                  <Users size={18} className="text-indigo-600" />
                  Reviewer (Manager) *
                </label>
                <select
                  value={formData.reviewer}
                  onChange={(e) => setFormData({ ...formData, reviewer: e.target.value })}
                  className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-4 focus:ring-indigo-500/20 focus:border-indigo-500 transition-all outline-none bg-gray-50 hover:bg-white font-medium appearance-none cursor-pointer"
                >
                  <option value="">Select a manager...</option>
                  {managers.map((mgr) => (
                    <option key={mgr.emp_id} value={mgr.emp_id}>
                      {mgr.name} (ID: {mgr.emp_id})
                    </option>
                  ))}
                </select>
              </div>
            )}

            {isManager && (
              <div className="md:col-span-2">
                <label className="flex items-center gap-2 text-sm font-bold text-gray-700 mb-3">
                  <User size={18} className="text-cyan-600" />
                  Assign To (Developer) *
                </label>
                <select
                  value={formData.assigned_to}
                  onChange={(e) => setFormData({ ...formData, assigned_to: e.target.value })}
                  className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-4 focus:ring-cyan-500/20 focus:border-cyan-500 transition-all outline-none bg-gray-50 hover:bg-white font-medium appearance-none cursor-pointer"
                >
                  <option value="">Select a developer...</option>
                  {employees.map((emp) => (
                    <option key={emp.id || emp.emp_id} value={emp.emp_id ?? emp.id}>
                      {emp.name} (ID: {emp.emp_id ?? emp.id})
                    </option>
                  ))}
                </select>
              </div>
            )}

            {/* Priority */}
            <div>
              <label className="flex items-center gap-2 text-sm font-bold text-gray-700 mb-3">
                <AlertCircle size={18} className="text-orange-600" />
                Priority
              </label>
              <div className="relative">
                <select
                  value={formData.priority}
                  onChange={(e) => setFormData({ ...formData, priority: e.target.value })}
                  className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-4 focus:ring-orange-500/20 focus:border-orange-500 transition-all outline-none bg-gray-50 hover:bg-white font-bold appearance-none cursor-pointer"
                >
                  <option value="Low">🟢 Low Priority</option>
                  <option value="Medium">🟡 Medium Priority</option>
                  <option value="High">🔴 High Priority</option>
                </select>
                <div className={`absolute right-4 top-1/2 -translate-y-1/2 w-3 h-3 rounded-full bg-gradient-to-br ${priorityColors[formData.priority]}`}></div>
              </div>
            </div>

            {/* Expected Completion Date */}
            <div>
              <label className="flex items-center gap-2 text-sm font-bold text-gray-700 mb-3">
                <Calendar size={18} className="text-pink-600" />
                Deadline *
              </label>
              <input
                type="date"
                value={formData.expected_completion_date}
                onChange={(e) => setFormData({ ...formData, expected_completion_date: e.target.value })}
                className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-4 focus:ring-pink-500/20 focus:border-pink-500 transition-all outline-none bg-gray-50 hover:bg-white font-medium"
              />
            </div>
          </div>

          {/* Action Buttons */}
          <div className="flex gap-4 mt-8">
            <button
              onClick={onClose}
              className="flex-1 px-6 py-4 border-2 border-gray-300 text-gray-700 rounded-xl hover:bg-gray-50 font-bold transition-all hover:scale-105 hover:shadow-lg"
            >
              Cancel
            </button>
            <button
              onClick={handleSubmit}
              disabled={loading}
              className="flex-1 px-6 py-4 bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 text-white rounded-xl hover:shadow-2xl font-bold transition-all disabled:opacity-50 hover:scale-105 relative overflow-hidden group"
            >
              <div className="absolute inset-0 bg-gradient-to-r from-pink-600 via-purple-600 to-blue-600 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
              <span className="relative z-10">
                {loading ? 'Creating...' : '✨ Create Task'}
              </span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CreateTaskModal;