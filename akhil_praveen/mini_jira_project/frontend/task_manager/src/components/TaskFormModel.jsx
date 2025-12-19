import React, { useState, useEffect } from "react";
import { X, Calendar, Tag, User, UserCheck, AlertCircle } from "lucide-react";
import { PRIORITIES } from "../utils/constants";

function TaskFormModal({
  task,
  employees = [],
  onClose,
  onSave,
  userRole = "",
  currentEmpId = null,
}) {
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
    } else {
      setFormData({
        title: "",
        description: "",
        dept_name: "",
        assigned_to: "",
        reviewer: "",
        priority: "MEDIUM",
        status: "TO_DO",
        expected_closure: "",
      });
    }
  }, [task]);

  // compute visible employees based on role and currentEmpId
  const visibleEmployees = React.useMemo(() => {
    const roleUpper = (userRole || "").toUpperCase();
    // Admins should not be able to set assignee
    if (roleUpper.includes("ADMIN")) return [];
    if (roleUpper.includes("MANAGER")) {
      if (currentEmpId == null) return [];
      // managers can only assign their direct reports (exclude the manager themself)
      return (employees || []).filter((e) => {
        try {
          return Number(e.manager_id) === Number(currentEmpId);
        } catch (ex) {
          return false;
        }
      });
    }
    // For developers or others, only show themselves (sensible fallback)
    if (currentEmpId == null) return [];
    return (employees || []).filter(
      (e) => Number(e.emp_id) === Number(currentEmpId)
    );
  }, [employees, userRole, currentEmpId]);

  // if manager creating new task, default reviewer to the manager
  useEffect(() => {
    const roleUpper = (userRole || "").toUpperCase();
    if (!task && roleUpper.includes("MANAGER") && currentEmpId != null) {
      setFormData((f) => ({ ...f, reviewer: Number(currentEmpId) }));
    }
  }, [task, userRole, currentEmpId]);

  // compute visible reviewers and whether reviewer select should be locked
  const visibleReviewers = React.useMemo(() => {
    const roleUpper = (userRole || "").toUpperCase();
    // If manager, restrict reviewer to the manager themself
    if (roleUpper.includes("MANAGER")) {
      if (currentEmpId == null) return [];
      return (employees || []).filter(
        (e) => Number(e.emp_id) === Number(currentEmpId)
      );
    }
    // Admins and others can choose from all employees
    return employees || [];
  }, [employees, userRole, currentEmpId]);

  const lockReviewer = React.useMemo(() => {
    const roleUpper = (userRole || "").toUpperCase();
    // lock when a manager is creating a new task (regardless of admin flags)
    return roleUpper.includes("MANAGER") && !task;
  }, [userRole, task]);

  const lockAssignForAdmin = React.useMemo(() => {
    const roleUpper = (userRole || "").toUpperCase();
    return roleUpper.includes("ADMIN");
  }, [userRole]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const roleUpper = (userRole || "").toUpperCase();

    // Admins are not allowed to assign tasks to users. Enforce on client-side by
    // clearing assigned_to and letting reviewer be set.
    if (roleUpper.includes("ADMIN")) {
      if (formData.assigned_to) {
        // silently remove assignment (avoid surprising UX); log for debugging
        console.info("Admin assignment cleared by client policy");
      }
      formData.assigned_to = null;
    }

    // Managers can only assign to their direct reports
    if (roleUpper.includes("MANAGER") && formData.assigned_to) {
      const allowed = (employees || []).some(
        (e) =>
          Number(e.manager_id) === Number(currentEmpId) &&
          Number(e.emp_id) === Number(formData.assigned_to)
      );
      if (!allowed) {
        alert("Managers can only assign tasks to their direct reports.");
        return;
      }
    }

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

  const priorityColors = {
    LOW: "bg-gray-100 text-gray-700 border-gray-300",
    MEDIUM: "bg-amber-100 text-amber-700 border-amber-300",
    HIGH: "bg-red-100 text-red-700 border-red-300",
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm p-4">
      <div className="w-full max-w-3xl bg-white rounded-2xl shadow-2xl overflow-hidden max-h-[90vh] flex flex-col animate-fadeIn">
        {/* Header */}
        <div className="flex items-center justify-between px-8 py-6 bg-gradient-to-r from-indigo-50 to-purple-50 border-b border-gray-100">
          <div>
            <h2 className="text-2xl font-bold text-gray-800">
              {task ? "Edit Task" : "Create New Task"}
            </h2>
            <p className="text-sm text-gray-600 mt-1">
              {task
                ? "Update task details below"
                : "Fill in the details to create a new task"}
            </p>
          </div>
          <button
            onClick={onClose}
            className="p-2 rounded-xl hover:bg-white/50 transition-all"
          >
            <X size={24} className="text-gray-600" />
          </button>
        </div>

        {/* Form Content */}
        <form onSubmit={handleSubmit} className="flex-1 overflow-y-auto p-8">
          <div className="space-y-6">
            {/* Title */}
            <div>
              <label className="block text-sm font-bold text-gray-700 mb-2 flex items-center gap-2">
                <span>Task Title</span>
                <span className="text-red-500">*</span>
              </label>
              <input
                type="text"
                value={formData.title}
                onChange={(e) =>
                  setFormData({ ...formData, title: e.target.value })
                }
                required
                placeholder="Enter a clear, concise task title..."
                className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all text-gray-800 font-medium"
              />
            </div>

            {/* Description */}
            <div>
              <label className="block text-sm font-bold text-gray-700 mb-2">
                Description
              </label>
              <textarea
                value={formData.description}
                onChange={(e) =>
                  setFormData({ ...formData, description: e.target.value })
                }
                rows="4"
                placeholder="Add detailed task description, requirements, or notes..."
                className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent resize-none transition-all text-gray-700"
              />
            </div>

            {/* Department and Priority Row */}
            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-bold text-gray-700 mb-2 flex items-center gap-2">
                  <Tag size={16} />
                  Department
                </label>
                <input
                  type="text"
                  value={formData.dept_name}
                  onChange={(e) =>
                    setFormData({ ...formData, dept_name: e.target.value })
                  }
                  placeholder="e.g., Engineering, Marketing"
                  className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all"
                />
              </div>

              <div>
                <label className="block text-sm font-bold text-gray-700 mb-2 flex items-center gap-2">
                  <AlertCircle size={16} />
                  Priority
                </label>
                <div className="grid grid-cols-3 gap-2">
                  {PRIORITIES.map((p) => (
                    <button
                      key={p}
                      type="button"
                      onClick={() => setFormData({ ...formData, priority: p })}
                      className={`px-4 py-3 rounded-xl font-semibold text-sm border-2 transition-all ${
                        formData.priority === p
                          ? priorityColors[p] + " scale-105 shadow-md"
                          : "bg-white border-gray-200 text-gray-600 hover:border-gray-300"
                      }`}
                    >
                      {p}
                    </button>
                  ))}
                </div>
              </div>
            </div>

            {/* Assignee and Reviewer Row */}
            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-bold text-gray-700 mb-2 flex items-center gap-2">
                  <User size={16} />
                  Assign To
                </label>
                <select
                  value={formData.assigned_to}
                  onChange={(e) =>
                    setFormData({
                      ...formData,
                      assigned_to: e.target.value
                        ? parseInt(e.target.value)
                        : "",
                    })
                  }
                  className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-500 bg-white cursor-pointer appearance-none font-medium text-gray-700"
                >
                  <option value="">Select Employee</option>
                  {(visibleEmployees || []).map((emp) => (
                    <option key={emp.emp_id} value={emp.emp_id}>
                      {emp.emp_name}{" "}
                      {emp.designation ? `(${emp.designation})` : ""}
                    </option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-sm font-bold text-gray-700 mb-2 flex items-center gap-2">
                  <UserCheck size={16} />
                  Reviewer
                </label>
                {lockReviewer ? (
                  <div className="flex items-center justify-between px-4 py-3 border-2 border-gray-200 rounded-xl bg-gray-50 text-gray-700">
                    <div>
                      {(() => {
                        const me = (employees || []).find(
                          (e) => Number(e.emp_id) === Number(currentEmpId)
                        );
                        return me
                          ? `${me.emp_name} ${
                              me.designation ? `(${me.designation})` : ""
                            }`
                          : "You";
                      })()}
                    </div>
                    <div className="text-xs text-gray-500">(Reviewer)</div>
                  </div>
                ) : (
                  <select
                    value={formData.reviewer}
                    onChange={(e) =>
                      setFormData({
                        ...formData,
                        reviewer: e.target.value
                          ? parseInt(e.target.value)
                          : "",
                      })
                    }
                    className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-500 bg-white cursor-pointer appearance-none font-medium text-gray-700"
                  >
                    <option value="">Select Reviewer</option>
                    {(visibleReviewers || []).map((emp) => (
                      <option
                        key={emp.emp_id}
                        value={emp.emp_id}
                        disabled={formData.assigned_to === emp.emp_id}
                      >
                        {emp.emp_name}{" "}
                        {emp.designation ? `(${emp.designation})` : ""}
                      </option>
                    ))}
                  </select>
                )}
              </div>
            </div>

            {/* Expected Closure Date */}
            <div>
              <label className="block text-sm font-bold text-gray-700 mb-2 flex items-center gap-2">
                <Calendar size={16} />
                Expected Closure Date
              </label>
              <input
                type="datetime-local"
                value={formData.expected_closure}
                onChange={(e) =>
                  setFormData({ ...formData, expected_closure: e.target.value })
                }
                className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-500 transition-all"
              />
            </div>
          </div>

          {/* Action Buttons */}
          <div className="flex justify-end gap-3 pt-8 border-t-2 border-gray-100 mt-8">
            <button
              type="button"
              onClick={onClose}
              className="px-6 py-3 rounded-xl bg-gray-100 hover:bg-gray-200 text-gray-700 font-semibold transition-all"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="px-6 py-3 rounded-xl bg-gradient-to-r from-indigo-600 to-purple-600 hover:shadow-lg text-white font-semibold transition-all hover:scale-105 active:scale-95"
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
