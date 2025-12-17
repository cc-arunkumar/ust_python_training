import React, { useState, useEffect } from "react";
import { PRIORITIES } from "../utils/constants";

function TaskFormModal({ task, employees, onClose, onSave }) {
  const [formData, setFormData] = useState({
    title: "",
    description: "",
    dept_name: "",
    assigned_to: "",
    reviewer: "",
    priority: "MEDIUM",
    status: "TO_DO",
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
        status: task.status || "TO_DO",
        expected_closure: task.expected_closure || "",
      });
    }
  }, [task]);

  // only users who are managers should appear as reviewer options
  const managerOptions = employees.filter((emp) => {
    const roleMatches =
      emp.role && String(emp.role).toUpperCase().includes("MANAGER");
    const designationMatches =
      emp.designation &&
      String(emp.designation).toLowerCase().includes("manager");
    return roleMatches || designationMatches;
  });

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Validate assigned_to and reviewer are not the same
    if (
      formData.assigned_to &&
      formData.reviewer &&
      formData.assigned_to === formData.reviewer
    ) {
      alert("Assigned to and Reviewer cannot be the same person");
      return;
    }

    const dataToSend = { ...formData };

    // Convert empty strings to null for optional fields
    if (!dataToSend.assigned_to) dataToSend.assigned_to = null;
    if (!dataToSend.reviewer) dataToSend.reviewer = null;
    if (!dataToSend.dept_name) dataToSend.dept_name = null;
    if (!dataToSend.description) dataToSend.description = null;
    if (!dataToSend.expected_closure) dataToSend.expected_closure = null;

    console.log("Sending task data:", dataToSend); // Debug log

    await onSave(dataToSend);
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg p-6 w-full max-w-2xl max-h-[90vh] overflow-y-auto">
        <div className="mb-4">
          <h2 className="text-2xl font-bold">
            {task ? "Edit Task" : "Create New Task"}
          </h2>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-1">Title *</label>
            <input
              type="text"
              value={formData.title}
              onChange={(e) =>
                setFormData({ ...formData, title: e.target.value })
              }
              className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium mb-1">
              Description
            </label>
            <textarea
              value={formData.description}
              onChange={(e) =>
                setFormData({ ...formData, description: e.target.value })
              }
              className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
              rows="3"
            />
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium mb-1">
                Department
              </label>
              <input
                type="text"
                value={formData.dept_name}
                onChange={(e) =>
                  setFormData({ ...formData, dept_name: e.target.value })
                }
                className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
              />
            </div>

            <div>
              <label className="block text-sm font-medium mb-1">Priority</label>
              <select
                value={formData.priority}
                onChange={(e) =>
                  setFormData({ ...formData, priority: e.target.value })
                }
                className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
              >
                {PRIORITIES.map((priority) => (
                  <option key={priority} value={priority}>
                    {priority}
                  </option>
                ))}
              </select>
            </div>
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium mb-1">
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
                className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
              >
                <option value="">Select Employee</option>
                {employees.map((emp) => (
                  <option key={emp.emp_id} value={emp.emp_id}>
                    {emp.emp_name} ({emp.designation || "N/A"})
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label className="block text-sm font-medium mb-1">Reviewer</label>
              <select
                value={formData.reviewer}
                onChange={(e) =>
                  setFormData({
                    ...formData,
                    reviewer: e.target.value ? parseInt(e.target.value) : "",
                  })
                }
                className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
              >
                <option value="">Select Reviewer</option>
                {managerOptions.map((emp) => (
                  <option
                    key={emp.emp_id}
                    value={emp.emp_id}
                    disabled={formData.assigned_to === emp.emp_id}
                  >
                    {emp.emp_name} ({emp.designation || "Manager"})
                  </option>
                ))}
              </select>
            </div>
          </div>

          <div>
            <label className="block text-sm font-medium mb-1">
              Expected Closure
            </label>
            <input
              type="datetime-local"
              value={formData.expected_closure}
              onChange={(e) =>
                setFormData({ ...formData, expected_closure: e.target.value })
              }
              className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div className="flex gap-2 justify-end">
            <button
              type="submit"
              className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
            >
              {task ? "Update Task" : "Create Task"}
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

export default TaskFormModal;
