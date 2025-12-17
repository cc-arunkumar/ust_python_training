import React, { useState, useEffect } from "react";
import { X } from "lucide-react";
import { PRIORITIES } from "../utils/constants";

function TaskFormModal({ task, employees = [], onClose, onSave }) {
  const [formData, setFormData] = useState({
    title: "",
    description: "",
    dept_name: "",
    assigned_to: "",
    reviewer: "",
    priority: "MEDIUM",
    status: "TODO",
    expected_closure: "",
  });

  useEffect(() => {
    if (task) {
      setFormData({
        title: task.title || "",
        description: task.description || "",
        dept_name: task.dept_name || "",
        assigned_to: task.assigned_to || "",
        reviewer: task.reviewer || "",
        priority: task.priority || "MEDIUM",
        status: task.status || "TODO",
        expected_closure: task.expected_closure || "",
      });
    } else {
      setFormData({
        title: "",
        description: "",
        dept_name: "",
        assigned_to: "",
        reviewer: "",
        priority: "MEDIUM",
        status: "TODO",
        expected_closure: "",
      });
    }
  }, [task]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (
      formData.assigned_to &&
      formData.reviewer &&
      formData.assigned_to === formData.reviewer
    ) {
      alert("Assigned to and Reviewer cannot be the same person");
      return;
    }

    const dataToSend = { ...formData };
    if (!dataToSend.assigned_to) dataToSend.assigned_to = null;
    if (!dataToSend.reviewer) dataToSend.reviewer = null;
    if (!dataToSend.dept_name) dataToSend.dept_name = null;
    if (!dataToSend.description) dataToSend.description = null;
    if (!dataToSend.expected_closure) dataToSend.expected_closure = null;

    await onSave(dataToSend);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4">
      <div className="w-full max-w-3xl bg-white rounded-xl shadow-2xl overflow-hidden max-h-[90vh] flex flex-col">
        {/* Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b bg-gradient-to-r from-indigo-50 to-purple-50">
          <h2 className="text-lg font-bold text-gray-800">
            {task ? "Edit Task" : "Create New Task"}
          </h2>
          <button
            onClick={onClose}
            className="p-2 rounded-lg hover:bg-white/50 transition"
          >
            <X size={20} />
          </button>
        </div>

        {/* Form Content */}
        <form onSubmit={handleSubmit} className="flex-1 overflow-y-auto p-6">
          <div className="space-y-4">
            {/* Title */}
            <div>
              <label className="block text-sm font-semibold text-gray-700 mb-2">
                Title <span className="text-red-500">*</span>
              </label>
              <input
                type="text"
                value={formData.title}
                onChange={(e) =>
                  setFormData({ ...formData, title: e.target.value })
                }
                required
                placeholder="Enter task title..."
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-400 focus:border-transparent"
              />
            </div>

            {/* Description */}
            <div>
              <label className="block text-sm font-semibold text-gray-700 mb-2">
                Description
              </label>
              <textarea
                value={formData.description}
                onChange={(e) =>
                  setFormData({ ...formData, description: e.target.value })
                }
                rows="4"
                placeholder="Add task description..."
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-400 focus:border-transparent resize-none"
              />
            </div>

            {/* Department and Priority */}
            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  Department
                </label>
                <input
                  type="text"
                  value={formData.dept_name}
                  onChange={(e) =>
                    setFormData({ ...formData, dept_name: e.target.value })
                  }
                  placeholder="e.g., Engineering"
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-400 focus:border-transparent"
                />
              </div>

              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  Priority
                </label>
                <select
                  value={formData.priority}
                  onChange={(e) =>
                    setFormData({ ...formData, priority: e.target.value })
                  }
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-400 bg-white"
                >
                  {PRIORITIES.map((p) => (
                    <option key={p} value={p}>
                      {p}
                    </option>
                  ))}
                </select>
              </div>
            </div>

            {/* Assignee and Reviewer */}
            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  Assign To
                </label>
                <select
                  value={formData.assigned_to}
                  onChange={(e) =>
                    setFormData({
                      ...formData,
                      assigned_to: e.target.value ? parseInt(e.target.value) : "",
                    })
                  }
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-400 bg-white"
                >
                  <option value="">Select Employee</option>
                  {(employees || []).map((emp) => (
                    <option key={emp.emp_id} value={emp.emp_id}>
                      {emp.emp_name} {emp.designation ? `(${emp.designation})` : ''}
                    </option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  Reviewer
                </label>
                <select
                  value={formData.reviewer}
                  onChange={(e) =>
                    setFormData({
                      ...formData,
                      reviewer: e.target.value ? parseInt(e.target.value) : "",
                    })
                  }
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-400 bg-white"
                >
                  <option value="">Select Reviewer</option>
                  {(employees || []).map((emp) => (
                    <option
                      key={emp.emp_id}
                      value={emp.emp_id}
                      disabled={formData.assigned_to === emp.emp_id}
                    >
                      {emp.emp_name} {emp.designation ? `(${emp.designation})` : ''}
                    </option>
                  ))}
                </select>
              </div>
            </div>

            {/* Expected Closure */}
            <div>
              <label className="block text-sm font-semibold text-gray-700 mb-2">
                Expected Closure Date
              </label>
              <input
                type="datetime-local"
                value={formData.expected_closure}
                onChange={(e) =>
                  setFormData({ ...formData, expected_closure: e.target.value })
                }
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-400"
              />
            </div>
          </div>

          {/* Action Buttons */}
          <div className="flex justify-end gap-3 pt-6 border-t mt-6">
            <button
              type="button"
              onClick={onClose}
              className="px-6 py-2 rounded-lg bg-gray-100 hover:bg-gray-200 text-gray-700 font-medium transition"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="px-6 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white font-medium transition"
            >
              {task ? "Update Task" : "Create Task"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default TaskFormModal;