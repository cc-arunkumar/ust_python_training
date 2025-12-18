import React, { useState } from "react";
import { X, AlertCircle } from "lucide-react";
import ApiService from "../../services/api";
import { TASK_STATUSES } from "../../utils/constants";

const PRIORITIES = {
  LOW: "Low",
  MEDIUM: "Medium",
  HIGH: "High",
};

const TaskModal = ({ task, onClose, onSuccess }) => {
  const [formData, setFormData] = useState({
    title: task?.title || "",
    description: task?.description || "",
    assigned_to: task?.assigned_to || "",
    reviewer: task?.reviewer || "",
    status: task?.status || TASK_STATUSES.TODO,
    priority: task?.priority || "MEDIUM",
    expected_closure: task?.expected_closure || "",
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [files, setFiles] = useState([]);
  const [comment, setComment] = useState("");

  const handleChange = (field, value) => {
    setFormData((prev) => ({ ...prev, [field]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");

    try {
      const payload = {
        ...formData,
        assigned_to: formData.assigned_to
          ? parseInt(formData.assigned_to)
          : null,
        reviewer: formData.reviewer ? parseInt(formData.reviewer) : null,
      };

      // include comment as remarks if provided
      if (comment && comment.trim().length > 0) {
        payload.remarks = [comment.trim()];
      }

      if (task) {
        const updated = await ApiService.updateTask(task.task_id, payload);

        // upload files after update
        if (files && files.length > 0) {
          for (const f of files) {
            await ApiService.uploadFile(task.task_id, f);
          }
        }
      } else {
        const created = await ApiService.createTask(payload);

        if (files && files.length > 0 && created && created.task_id) {
          for (const f of files) {
            await ApiService.uploadFile(created.task_id, f);
          }
        }
      }

      onSuccess();
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-black/30 backdrop-blur-sm flex items-center justify-center p-4 z-50">
      <div className="bg-white rounded-2xl shadow-2xl w-full max-w-3xl max-h-[90vh] overflow-y-auto p-6">
        {/* Header */}
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-2xl font-bold text-gray-900">
            {task ? "Update Task" : "New Task"}
          </h2>
          <button
            onClick={onClose}
            className="text-gray-500 hover:text-gray-700"
          >
            <X size={24} />
          </button>
        </div>

        {/* Error */}
        {error && (
          <div className="bg-red-100 border border-red-300 text-red-700 px-4 py-3 rounded mb-4 flex gap-2">
            <AlertCircle size={20} />
            <span className="text-sm">{error}</span>
          </div>
        )}

        {/* Form */}
        <form
          onSubmit={handleSubmit}
          className="grid grid-cols-1 md:grid-cols-2 gap-4"
        >
          {/* Task Title */}
          <div className="md:col-span-2">
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Task Title *
            </label>
            <input
              type="text"
              value={formData.title}
              onChange={(e) => handleChange("title", e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
              required
            />
          </div>

          {/* Description */}
          <div className="md:col-span-2">
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Task Details
            </label>
            <textarea
              rows={3}
              value={formData.description}
              onChange={(e) => handleChange("description", e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
            />
          </div>

          {/* Assign To */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Assign To (Employee ID)
            </label>
            <input
              type="number"
              value={formData.assigned_to}
              onChange={(e) => handleChange("assigned_to", e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
            />
          </div>

          {/* Reviewer */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Reviewer (Employee ID)
            </label>
            <input
              type="number"
              value={formData.reviewer}
              onChange={(e) => handleChange("reviewer", e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
            />
          </div>

          {/* Status */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Task Status *
            </label>
            <select
              value={formData.status}
              onChange={(e) => handleChange("status", e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
            >
              {Object.values(TASK_STATUSES).map((status) => (
                <option key={status} value={status}>
                  {status.replace("_", " ")}
                </option>
              ))}
            </select>
          </div>

          {/* Priority */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Priority *
            </label>
            <select
              value={formData.priority}
              onChange={(e) => handleChange("priority", e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
            >
              {Object.entries(PRIORITIES).map(([key, label]) => (
                <option key={key} value={key}>
                  {label}
                </option>
              ))}
            </select>
          </div>

          {/* Expected Completion */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Expected Completion
            </label>
            <input
              type="date"
              value={formData.expected_closure}
              onChange={(e) => handleChange("expected_closure", e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
            />
          </div>

          {/* File Upload */}
          <div className="md:col-span-2">
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Attach Files
            </label>
            <input
              type="file"
              multiple
              onChange={(e) => setFiles(Array.from(e.target.files || []))}
              className="w-full text-gray-700"
            />
            <p className="text-xs text-slate-500 mt-1">
              You can attach one or more files. Files will be uploaded and
              linked to the task.
            </p>
          </div>

          {/* Feedback / Comment */}
          <div className="md:col-span-2">
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Feedback / Comment
            </label>
            <textarea
              rows={3}
              value={comment}
              onChange={(e) => setComment(e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
              placeholder="Add feedback or comments that will be stored with the task"
            />
          </div>

          {/* Buttons */}
          <div className="md:col-span-2 flex gap-3 pt-6">
            <button
              type="button"
              onClick={onClose}
              className="flex-1 px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-100"
            >
              Close
            </button>
            <button
              type="submit"
              disabled={loading}
              className="flex-1 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 disabled:bg-blue-400"
            >
              {loading ? "Saving..." : "Save Task"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default TaskModal;
