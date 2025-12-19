import { useState } from "react";
import { useDraggable } from "@dnd-kit/core";
import {
  X,
  Calendar,
  User,
  Flag,
  MessageSquare,
  Upload,
  Paperclip,
} from "lucide-react";

const TaskCard = ({ task, token, onUpdateTask, draggable = true }) => {
  const [showModal, setShowModal] = useState(false);
  const [remark, setRemark] = useState("");
  const [file, setFile] = useState(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState("");

  // Conditionally enable draggable behavior (Admin view uses draggable=false)
  let setNodeRef = undefined;
  let listeners = {};
  let attributes = {};
  let transform = null;
  let isDragging = false;

  if (draggable) {
    const draggableResult = useDraggable({
      id: String(task.task_id),
      data: { status: task.status },
    });
    setNodeRef = draggableResult.setNodeRef;
    listeners = draggableResult.listeners || {};
    attributes = draggableResult.attributes || {};
    transform = draggableResult.transform;
    isDragging = draggableResult.isDragging;
  }

  const style = {
    transform: transform
      ? `translate3d(${transform.x}px, ${transform.y}px, 0)`
      : undefined,
    opacity: isDragging ? 0.6 : 1,
  };

  const handleCardClick = (e) => {
    // Prevent modal from opening while dragging
    if (!isDragging) {
      setShowModal(true);
    }
  };

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      // Limit file size to 5MB
      if (selectedFile.size > 5 * 1024 * 1024) {
        setError("File size must be less than 5MB");
        return;
      }
      setFile(selectedFile);
      setError("");
    }
  };

  const handleSubmitRemark = async () => {
    if (!remark.trim() && !file) {
      setError("Please add a remark or upload a file");
      return;
    }

    setIsSubmitting(true);
    setError("");

    try {
      // Import api from your services
      const { api } = await import("../../services/api");

      // Call the new API method
      const data = await api.addTaskRemark(task.task_id, remark, file, token);

      // Update task with new remark
      if (onUpdateTask) {
        const updatedRemarks = Array.isArray(task.remarks)
          ? [...task.remarks, data.remark]
          : [data.remark];

        onUpdateTask({
          ...task,
          remarks: updatedRemarks,
        });
      }

      // Reset form
      setRemark("");
      setFile(null);
      setError("");
      alert("Remark added successfully!");
    } catch (err) {
      setError(err.message || "Failed to submit remark");
    } finally {
      setIsSubmitting(false);
    }
  };

  const getPriorityColor = (priority) => {
    switch (priority) {
      case "HIGH":
        return "text-red-600 bg-red-50";
      case "MEDIUM":
        return "text-amber-600 bg-amber-50";
      case "LOW":
        return "text-green-600 bg-green-50";
      default:
        return "text-gray-600 bg-gray-50";
    }
  };

  return (
    <>
      {/* Task Card */}
      <div
        ref={setNodeRef || undefined}
        style={style}
        {...(listeners || {})}
        {...(attributes || {})}
        onClick={handleCardClick}
        className={`bg-white rounded-xl border p-4 shadow ${
          draggable ? "cursor-grab" : ""
        } hover:shadow-md transition`}
      >
        <h3 className="font-semibold text-gray-800 mb-1">{task.name}</h3>
        <p className="text-xs text-gray-500">{task.task_id}</p>
        <div className="mt-2 flex items-center gap-2">
          <span
            className={`text-xs px-2 py-0.5 rounded-full ${getPriorityColor(
              task.priority
            )}`}
          >
            {task.priority}
          </span>
        </div>
      </div>

      {/* Modal */}
      {showModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
          <div className="bg-white rounded-2xl shadow-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
            {/* Modal Header */}
            <div className="sticky top-0 bg-white border-b px-6 py-4 flex justify-between items-center">
              <h2 className="text-xl font-bold text-gray-800">Task Details</h2>
              <button
                onClick={() => setShowModal(false)}
                className="text-gray-500 hover:text-gray-700 p-1 rounded-lg hover:bg-gray-100"
              >
                <X size={20} />
              </button>
            </div>

            {/* Modal Content */}
            <div className="p-6 space-y-6">
              {/* Task Info */}
              <div>
                <h3 className="text-2xl font-semibold text-gray-900 mb-2">
                  {task.name}
                </h3>
                <p className="text-sm text-gray-500 mb-4">ID: {task.task_id}</p>

                {task.description && (
                  <div className="mb-4">
                    <h4 className="font-medium text-gray-700 mb-2">
                      Description
                    </h4>
                    <p className="text-gray-600 text-sm">{task.description}</p>
                  </div>
                )}

                <div className="grid grid-cols-2 gap-4">
                  <div className="flex items-center gap-2 text-sm">
                    <Flag
                      className={getPriorityColor(task.priority)}
                      size={16}
                    />
                    <span className="text-gray-700">Priority:</span>
                    <span
                      className={`font-medium px-2 py-0.5 rounded ${getPriorityColor(
                        task.priority
                      )}`}
                    >
                      {task.priority}
                    </span>
                  </div>

                  <div className="flex items-center gap-2 text-sm">
                    <User className="text-blue-600" size={16} />
                    <span className="text-gray-700">Assigned to:</span>
                    <span className="font-medium">{task.assigned_to}</span>
                  </div>

                  <div className="flex items-center gap-2 text-sm">
                    <Calendar className="text-purple-600" size={16} />
                    <span className="text-gray-700">Created:</span>
                    <span className="font-medium">
                      {task.created_at
                        ? new Date(task.created_at).toLocaleDateString()
                        : "—"}
                    </span>
                  </div>

                  <div className="flex items-center gap-2 text-sm">
                    <Calendar className="text-orange-600" size={16} />
                    <span className="text-gray-700">Deadline:</span>
                    <span className="font-medium">
                      {task.expected_closure
                        ? new Date(task.expected_closure).toLocaleDateString()
                        : "—"}
                    </span>
                  </div>
                </div>
              </div>

              {/* Previous Remarks */}
              {Array.isArray(task.remarks) && task.remarks.length > 0 && (
                <div>
                  <h4 className="font-medium text-gray-700 mb-3 flex items-center gap-2">
                    <MessageSquare size={16} />
                    Previous Remarks
                  </h4>
                  <div className="space-y-2 max-h-40 overflow-y-auto">
                    {task.remarks.map((rem, idx) => (
                      <div
                        key={idx}
                        className="bg-gray-50 p-3 rounded-lg text-sm"
                      >
                        <p className="text-gray-700">
                          {rem.text || rem.remark_text || "No comment"}
                        </p>
                        <p className="text-xs text-gray-500 mt-1">
                          {rem.created_at
                            ? new Date(rem.created_at).toLocaleString()
                            : ""}
                          {rem.file_url && (
                            <a
                              href={rem.file_url}
                              target="_blank"
                              rel="noopener noreferrer"
                              className="ml-2 text-blue-600 hover:underline"
                            >
                              <Paperclip size={12} className="inline" /> View
                              File
                            </a>
                          )}
                        </p>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Add Remark Section */}
              <div className="border-t pt-6">
                <h4 className="font-medium text-gray-700 mb-3">Add Remark</h4>

                {error && (
                  <div className="mb-3 bg-red-50 border border-red-300 text-red-700 p-3 rounded-lg text-sm">
                    {error}
                  </div>
                )}

                <textarea
                  value={remark}
                  onChange={(e) => setRemark(e.target.value)}
                  placeholder="Enter your remark here..."
                  className="w-full border rounded-lg p-3 text-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
                  rows={4}
                  disabled={isSubmitting}
                />

                {/* File Upload */}
                <div className="mt-3">
                  <label className="flex items-center gap-2 cursor-pointer">
                    <input
                      type="file"
                      onChange={handleFileChange}
                      className="hidden"
                      disabled={isSubmitting}
                    />
                    <div className="flex items-center gap-2 bg-gray-100 hover:bg-gray-200 px-4 py-2 rounded-lg text-sm transition">
                      <Upload size={16} />
                      <span>{file ? file.name : "Upload File (Optional)"}</span>
                    </div>
                  </label>
                  {file && (
                    <button
                      onClick={() => setFile(null)}
                      className="mt-2 text-xs text-red-600 hover:text-red-700"
                    >
                      Remove file
                    </button>
                  )}
                </div>

                {/* Submit Button */}
                <button
                  onClick={handleSubmitRemark}
                  disabled={isSubmitting || (!remark.trim() && !file)}
                  className="mt-4 w-full bg-blue-600 hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed text-white py-3 rounded-lg font-medium transition"
                >
                  {isSubmitting ? "Submitting..." : "Submit Remark"}
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default TaskCard;
