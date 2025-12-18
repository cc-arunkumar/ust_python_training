import React, { useState } from "react";
import {
  X,
  CheckCircle,
  Calendar,
  AlertCircle,
  User,
  Users,
} from "lucide-react";
import { api } from "../../services/api";

const CreateTaskModal = ({
  token,
  empId,
  currentRole,
  employees = [],
  managers = [],
  onClose,
  onSuccess,
}) => {
  // Calculate default date (7 days from today)
  const getDefaultDate = () => {
    const date = new Date();
    date.setDate(date.getDate() + 7);
    return date.toISOString().split("T")[0];
  };

  const [formData, setFormData] = useState({
    title: "",
    description: "",
    assigned_to: "",
    reviewer: "",
    priority: "Low",
    status: "To Do",
    expected_completion_date: getDefaultDate(),
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const isAdmin = currentRole === "admin";
  const isManager = currentRole === "manager";

  const handleSubmit = async () => {
    setError("");

    // Validation
    if (
      !formData.title ||
      !formData.description ||
      !formData.expected_completion_date
    ) {
      setError(
        "Please fill all required fields (Title, Description, Deadline)"
      );
      return;
    }

    // If a manager creates the task and assigns it directly, start it in 'In Progress'
    const initialStatus = isManager ? "In Progress" : "To Do";

    let payload = {
      title: formData.title,
      description: formData.description,
      priority: formData.priority,
      status: initialStatus,
      expected_completion_date: formData.expected_completion_date,
      assigned_by: empId,
      assigned_at: new Date().toISOString(),
      updated_by: empId,
      remarks: [],
    };

    if (isAdmin) {
      if (!formData.reviewer) {
        setError("Please select a reviewer (manager)");
        return;
      }
      payload = {
        ...payload,
        reviewer: parseInt(formData.reviewer, 10),
        assigned_to: null,
      };
    } else if (isManager) {
      if (!formData.assigned_to) {
        setError("Please select a developer to assign this task to");
        return;
      }
      payload = {
        ...payload,
        reviewer: empId,
        assigned_to: parseInt(formData.assigned_to, 10),
      };
    } else {
      setError("You do not have permission to create tasks");
      return;
    }

    console.log("Creating task with payload:", payload);
    setLoading(true);

    try {
      const response = await api.createTask(token, payload);
      console.log("Task created successfully:", response);
      onSuccess();
    } catch (error) {
      console.error("Error creating task:", error);
      setError(
        error.message ||
          "Failed to create task. Please check the console for details."
      );
    } finally {
      setLoading(false);
    }
  };

  const priorityColors = {
    Low: {
      gradient: "from-green-500 to-emerald-500",
      border: "border-green-500",
      ring: "ring-green-500/50",
      glow: "shadow-green-500/50",
    },
    Medium: {
      gradient: "from-yellow-500 to-orange-500",
      border: "border-yellow-500",
      ring: "ring-yellow-500/50",
      glow: "shadow-yellow-500/50",
    },
    High: {
      gradient: "from-red-500 to-pink-500",
      border: "border-red-500",
      ring: "ring-red-500/50",
      glow: "shadow-red-500/50",
    },
  };

  return (
    <div className="fixed inset-0 bg-black/40 backdrop-blur-sm flex items-center justify-center p-4 z-50">
      <div className="bg-white rounded-3xl shadow-2xl w-full max-w-3xl border-2 border-gray-200 relative overflow-hidden max-h-[90vh] overflow-y-auto">
        {/* Header - Solid Blue */}
        <div className="sticky top-0 z-10 bg-blue-600 px-8 py-6 flex items-center justify-between">
          <div>
            <h2 className="text-2xl font-bold text-white mb-1">
              Create New Task
            </h2>
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
          {/* Error Message */}
          {error && (
            <div className="mb-6 p-4 bg-red-50 border-2 border-red-200 rounded-xl flex items-start gap-3">
              <AlertCircle
                className="text-red-600 flex-shrink-0 mt-0.5"
                size={20}
              />
              <div>
                <p className="text-red-900 font-semibold text-sm">Error</p>
                <p className="text-red-700 text-sm mt-1">{error}</p>
              </div>
            </div>
          )}

          <div className="space-y-6">
            {/* Title and Assigned To - Horizontal Layout */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {/* Title */}
              <div>
                <label className="flex items-center gap-2 text-sm font-bold text-gray-700 mb-3">
                  <CheckCircle size={18} className="text-blue-600" />
                  Task Title *
                </label>
                <input
                  type="text"
                  value={formData.title}
                  onChange={(e) =>
                    setFormData({ ...formData, title: e.target.value })
                  }
                  placeholder="Enter task title..."
                  className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-4 focus:ring-blue-500/20 focus:border-blue-500 transition-all outline-none bg-gray-50 hover:bg-white font-medium"
                />
              </div>

              {/* Assign To (for Manager) or Reviewer (for Admin) */}
              {isManager && (
                <div>
                  <label className="flex items-center gap-2 text-sm font-bold text-gray-700 mb-3">
                    <User size={18} className="text-cyan-600" />
                    Assign To (Developer) *
                  </label>
                  <select
                    value={formData.assigned_to}
                    onChange={(e) =>
                      setFormData({ ...formData, assigned_to: e.target.value })
                    }
                    className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-4 focus:ring-cyan-500/20 focus:border-cyan-500 transition-all outline-none bg-gray-50 hover:bg-white font-medium appearance-none cursor-pointer"
                  >
                    <option value="">Select a developer...</option>
                    {employees.map((emp) => (
                      <option
                        key={emp.id || emp.emp_id}
                        value={emp.emp_id ?? emp.id}
                      >
                        {emp.name} (ID: {emp.emp_id ?? emp.id})
                      </option>
                    ))}
                  </select>
                  {employees.length === 0 && (
                    <p className="text-xs text-amber-600 mt-2">
                      ⚠️ No developers available
                    </p>
                  )}
                </div>
              )}

              {isAdmin && (
                <div>
                  <label className="flex items-center gap-2 text-sm font-bold text-gray-700 mb-3">
                    <Users size={18} className="text-indigo-600" />
                    Reviewer (Manager) *
                  </label>
                  <select
                    value={formData.reviewer}
                    onChange={(e) =>
                      setFormData({ ...formData, reviewer: e.target.value })
                    }
                    className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-4 focus:ring-indigo-500/20 focus:border-indigo-500 transition-all outline-none bg-gray-50 hover:bg-white font-medium appearance-none cursor-pointer"
                  >
                    <option value="">Select a manager...</option>
                    {managers.map((mgr) => (
                      <option key={mgr.emp_id} value={mgr.emp_id}>
                        {mgr.name} (ID: {mgr.emp_id})
                      </option>
                    ))}
                  </select>
                  {managers.length === 0 && (
                    <p className="text-xs text-amber-600 mt-2">
                      ⚠️ No managers available
                    </p>
                  )}
                </div>
              )}
            </div>

            {/* Description - Full Width */}
            <div>
              <label className="flex items-center gap-2 text-sm font-bold text-gray-700 mb-3">
                <AlertCircle size={18} className="text-purple-600" />
                Description *
              </label>
              <textarea
                value={formData.description}
                onChange={(e) =>
                  setFormData({ ...formData, description: e.target.value })
                }
                placeholder="Provide detailed information about the task..."
                className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-4 focus:ring-purple-500/20 focus:border-purple-500 transition-all outline-none bg-gray-50 hover:bg-white font-medium resize-none"
                rows="4"
              />
            </div>

            {/* Priority and Deadline - Horizontal Layout */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {/* Priority with Glowing Border */}
              <div>
                <label className="flex items-center gap-2 text-sm font-bold text-gray-700 mb-3">
                  <AlertCircle size={18} className="text-orange-600" />
                  Priority
                </label>
                <div className="relative">
                  <select
                    value={formData.priority}
                    onChange={(e) =>
                      setFormData({ ...formData, priority: e.target.value })
                    }
                    className={`w-full px-4 py-3 border-2 ${
                      priorityColors[formData.priority].border
                    } rounded-xl focus:ring-4 ${
                      priorityColors[formData.priority].ring
                    } transition-all outline-none bg-white font-bold appearance-none cursor-pointer shadow-lg ${
                      priorityColors[formData.priority].glow
                    }`}
                  >
                    <option value="Low"> Low Priority</option>
                    <option value="Medium"> Medium Priority</option>
                    <option value="High"> High Priority</option>
                  </select>
                  <div
                    className={`absolute right-4 top-1/2 -translate-y-1/2 w-3 h-3 rounded-full bg-gradient-to-br ${
                      priorityColors[formData.priority].gradient
                    } animate-pulse`}
                  ></div>
                </div>
              </div>

              {/* Expected Completion Date with Enhanced Calendar */}
              <div>
                <label className="flex items-center gap-2 text-sm font-bold text-gray-700 mb-3">
                  <Calendar size={18} className="text-pink-600" />
                  Deadline *
                </label>
                <div className="relative">
                  <input
                    type="date"
                    value={formData.expected_completion_date}
                    onChange={(e) =>
                      setFormData({
                        ...formData,
                        expected_completion_date: e.target.value,
                      })
                    }
                    min={new Date().toISOString().split("T")[0]}
                    className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-4 focus:ring-pink-500/20 focus:border-pink-500 transition-all outline-none bg-white hover:bg-gray-50 font-medium cursor-pointer shadow-sm"
                    style={{
                      colorScheme: "light",
                    }}
                  />
                  <Calendar
                    size={18}
                    className="absolute right-4 top-1/2 -translate-y-1/2 text-pink-500 pointer-events-none"
                  />
                </div>
                <p className="text-xs text-gray-500 mt-2">
                  Default: 7 days from today
                </p>
              </div>
            </div>
          </div>

          {/* Action Buttons */}
          <div className="flex gap-3 mt-8 justify-end">
            <button
              onClick={onClose}
              className="px-3 py-1.5 border-2 border-gray-300 text-gray-700 rounded-md hover:bg-gray-50 font-semibold transition-all hover:shadow-sm text-sm"
            >
              Cancel
            </button>
            <button
              onClick={handleSubmit}
              disabled={loading}
              className="px-3 py-1.5 bg-blue-600 text-white rounded-md hover:bg-blue-700 hover:shadow-sm font-semibold transition-all disabled:opacity-50 disabled:cursor-not-allowed text-sm"
            >
              {loading ? "Creating..." : "Create Task"}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CreateTaskModal;
