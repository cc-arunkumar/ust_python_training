import React, { useState, useEffect, useRef } from "react";
import { X, AlertCircle, Trash } from "lucide-react";
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
    priority: task?.priority || "MEDIUM",
    expected_closure: task?.expected_closure || "",
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [files, setFiles] = useState([]);
  const [comment, setComment] = useState("");
  const [employees, setEmployees] = useState([]);
  const [existingAttachments, setExistingAttachments] = useState([]);
  const [loadingAttachments, setLoadingAttachments] = useState(false);
  const [attachedLabel, setAttachedLabel] = useState("");

  const handleChange = (field, value) => {
    setFormData((prev) => ({ ...prev, [field]: value }));
  };

  const handleFileChange = (e) => {
    const selectedFiles = Array.from(e.target.files || []);
    if (selectedFiles.length === 0) return;

    // If editing an existing task, upload immediately (create a remark with file)
    if (task && task.task_id) {
      (async () => {
        try {
          const names = [];
          for (const f of selectedFiles) {
            const res = await ApiService.createRemark(task.task_id, null, f);
            // res should contain file_id and filename
            const fileId = res.file_id || res.fileId || res.file_id;
            const filename = res.filename || f.name;
            const href = fileId
              ? ApiService.getRemarkAttachmentUrl(fileId)
              : null;
            setExistingAttachments((prev) => [
              ...prev,
              { id: fileId, name: filename, href },
            ]);
            names.push(filename);
          }
          setAttachedLabel(
            names.length === 1 ? names[0] : `${names.length} files`
          );
        } catch (err) {
          setError(err.message || "Failed to upload attachment");
        }
      })();
    } else {
      setFiles((prev) => [...prev, ...selectedFiles]);
      setAttachedLabel(
        selectedFiles.length === 1
          ? selectedFiles[0].name
          : `${(files?.length || 0) + selectedFiles.length} files`
      );
    }
  };

  const handleDeleteFile = (fileName) => {
    setFiles(files.filter((file) => file.name !== fileName));
  };

  const removeExistingAttachment = async (att) => {
    // Optimistic UI removal
    setExistingAttachments((prev) => prev.filter((a) => a !== att));
    if (!att.id) return;
    try {
      // Attempt server delete; backend may or may not support this route
      await ApiService.request(`/tasks/remarks/attachments/${att.id}`, {
        method: "DELETE",
      });
    } catch (err) {
      // rollback on failure
      setExistingAttachments((prev) => [...prev, att]);
      setError(err.message || "Failed to delete attachment");
    }
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

      if (comment && comment.trim().length > 0) {
        payload.remarks = [comment.trim()];
      }

      if (task) {
        const updated = await ApiService.updateTask(task.task_id, payload);

        // Upload files after task update
        if (files.length > 0) {
          for (const file of files) {
            await ApiService.uploadFile(task.task_id, file);
          }
        }
      } else {
        const created = await ApiService.createTask(payload);

        if (created && created.task_id && files.length > 0) {
          for (const file of files) {
            await ApiService.uploadFile(created.task_id, file);
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

  useEffect(() => {
    const loadEmployees = async () => {
      try {
        const data = await ApiService.getEmployees();
        setEmployees(data || []);
      } catch (err) {
        setError("Failed to load employees.");
      }
    };

    loadEmployees();
  }, []);

  // Load existing attachments and remarks for the task when editing
  useEffect(() => {
    let mounted = true;
    const loadAttachments = async () => {
      if (!task || !task.task_id) return;
      setLoadingAttachments(true);
      try {
        const t = await ApiService.getTask(task.task_id);
        if (!mounted) return;
        const atts = t.attachments || [];

        let remarks = [];
        try {
          remarks = await ApiService.listRemarks(task.task_id);
        } catch (e) {
          // ignore
        }

        const combined = [];
        (atts || []).forEach((a) => {
          combined.push({
            id: a.id || a.file_id || a._id || null,
            name: a.file_name || a.filename || a.fileName || a.name || "file",
            href: a.file_path || a.url || null,
          });
        });

        (remarks || []).forEach((r) => {
          if (r.file_id) {
            combined.push({
              id: r.file_id,
              name: r.filename || r.fileName || r.name || "file",
              href: ApiService.getRemarkAttachmentUrl(r.file_id),
            });
          }
        });

        if (mounted) {
          setExistingAttachments(combined);
          if (!attachedLabel) {
            setAttachedLabel(
              combined.length === 1
                ? combined[0].name
                : combined.length > 1
                ? `${combined.length} files`
                : ""
            );
          }
        }
      } catch (err) {
        // ignore loading errors
      } finally {
        if (mounted) setLoadingAttachments(false);
      }
    };

    loadAttachments();
    return () => (mounted = false);
  }, [task]);

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

          {/* Assign To (Dropdown) */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Assign To *
            </label>
            <select
              value={formData.assigned_to}
              onChange={(e) => handleChange("assigned_to", e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
              required
            >
              <option value="">Select Employee</option>
              {employees.map((emp) => (
                <option key={emp.emp_id} value={emp.emp_id}>
                  {emp.emp_name}
                </option>
              ))}
            </select>
          </div>

          {/* Reviewer (Dropdown) */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Reviewer *
            </label>
            <select
              value={formData.reviewer}
              onChange={(e) => handleChange("reviewer", e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
              required
            >
              <option value="">Select Reviewer</option>
              {employees.map((emp) => (
                <option key={emp.emp_id} value={emp.emp_id}>
                  {emp.emp_name}
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
              onChange={handleFileChange}
              className="w-full text-gray-700"
            />
            {files.length > 0 && (
              <div className="mt-2">
                <ul className="list-disc pl-4">
                  {files.map((file) => (
                    <li
                      key={file.name}
                      className="flex justify-between items-center"
                    >
                      <span>{file.name}</span>
                      <button
                        type="button"
                        onClick={() => handleDeleteFile(file.name)}
                        className="text-red-600 hover:text-red-800"
                      >
                        <Trash size={14} />
                      </button>
                    </li>
                  ))}
                </ul>
              </div>
            )}
            {/* Existing attachments for editing tasks */}
            {task && existingAttachments && existingAttachments.length > 0 && (
              <div className="mt-4">
                <div className="text-sm text-slate-600 mb-2">
                  Existing Attachments
                </div>
                <div className="space-y-2">
                  {existingAttachments.map((a) => (
                    <div
                      key={a.id || a.name}
                      className="flex items-center justify-between border rounded px-3 py-2"
                    >
                      <div className="truncate text-sm text-slate-700 mr-2">
                        {a.name}
                      </div>
                      <div className="flex items-center gap-2">
                        {a.href ? (
                          <a
                            href={a.href}
                            target="_blank"
                            rel="noreferrer"
                            className="text-blue-600 text-xs font-medium hover:underline"
                          >
                            Download
                          </a>
                        ) : (
                          <span className="text-xs text-slate-500">
                            No link
                          </span>
                        )}
                        <button
                          type="button"
                          onClick={() => removeExistingAttachment(a)}
                          className="text-red-600 hover:text-red-800"
                        >
                          <Trash size={14} />
                        </button>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}
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
