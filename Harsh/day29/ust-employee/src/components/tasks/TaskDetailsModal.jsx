import React, { useState } from "react";
import { X, AlertCircle, User } from "lucide-react";
import ApiService from "../../services/api";

const TaskDetailsModal = ({ task, onClose, onUpdate, assignedEmployee }) => {
  // TaskDetailsModal is view-only. Edits (status changes, uploads, feedback)
  // should be performed in the edit/create modal (TaskModal).
  // Keep minimal state for error reporting.
  const [error, setError] = useState("");

  // No status/file handlers here — view-only modal.

  const formatDate = (dateString) =>
    dateString ? new Date(dateString).toLocaleDateString() : "-";

  return (
    <div className="fixed inset-0 bg-white bg-opacity-30 backdrop-blur-sm flex items-center justify-center p-4 z-50 overflow-auto backdrop-blur-sm bg-white/30">
      <div className="bg-white rounded-2xl shadow-2xl w-full max-w-4xl max-h-[90vh] overflow-y-auto flex flex-col sm:flex-row p-6 border border-gray-200">
        {/* Left: Task Info */}
        <div className="flex-1 pr-4 border-b sm:border-b-0 sm:border-r border-gray-200 sm:pr-6 sm:mr-6 space-y-4">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-2xl font-bold text-gray-800">Task Overview</h2>
            <button
              onClick={onClose}
              className="text-gray-400 hover:text-gray-600 transition"
            >
              <X size={24} />
            </button>
          </div>

          {error && (
            <div className="bg-red-100 border border-red-300 text-red-700 px-4 py-3 rounded flex items-center gap-2">
              <AlertCircle size={20} />
              <span className="text-sm">{error}</span>
            </div>
          )}
          {/* upload success removed in view-only modal */}

          <div className="space-y-3">
            <div>
              <h3 className="text-xs font-semibold text-gray-500 uppercase mb-1">
                Task Number
              </h3>
              <p className="text-gray-800 font-medium">{task.task_id}</p>
            </div>

            <div>
              <h3 className="text-xs font-semibold text-gray-500 uppercase mb-1">
                Task Name
              </h3>
              <p className="text-gray-900 font-semibold text-lg">
                {task.title}
              </p>
            </div>

            <div>
              <h3 className="text-xs font-semibold text-gray-500 uppercase mb-1">
                Details
              </h3>
              <p className="text-gray-700">
                {task.description || "No additional details provided."}
              </p>
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div>
                <h3 className="text-xs font-semibold text-gray-500 uppercase mb-1">
                  Assigned To
                </h3>
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-full bg-slate-100 overflow-hidden flex items-center justify-center text-slate-700 font-semibold">
                    {assignedEmployee && assignedEmployee.avatar ? (
                      <img
                        src={assignedEmployee.avatar}
                        alt={assignedEmployee.emp_name || "avatar"}
                        className="w-full h-full object-cover"
                      />
                    ) : assignedEmployee && assignedEmployee.emp_name ? (
                      <span className="uppercase">
                        {assignedEmployee.emp_name.charAt(0)}
                      </span>
                    ) : (
                      <User size={18} />
                    )}
                  </div>

                  {task.priority && (
                    <span className="inline-block px-2 py-1 rounded-full text-xs font-medium bg-gray-100 text-slate-700">
                      {task.priority}
                    </span>
                  )}

                  {/* Notifications are available from the task list header; details view is read-only and hides the bell. */}
                </div>
              </div>
              <div>
                <h3 className="text-xs font-semibold text-gray-500 uppercase mb-1">
                  Reviewed By
                </h3>
                <p className="text-gray-800">
                  {task.reviewer
                    ? `Employee ID: ${task.reviewer}`
                    : "Pending assignment"}
                </p>
              </div>
              <div>
                <h3 className="text-xs font-semibold text-gray-500 uppercase mb-1">
                  Created By
                </h3>
                <p className="text-gray-800">
                  {task.creator_name
                    ? `${task.creator_name} (#${task.created_by})`
                    : `Employee ID: `}
                </p>
              </div>
              <div>
                <h3 className="text-xs font-semibold text-gray-500 uppercase mb-1">
                  Due Date
                </h3>
                <p className="text-gray-800">
                  {formatDate(task.expected_closure)}
                </p>
              </div>
            </div>
          </div>
        </div>

        {/* Right: Read-only info (edits are done in the edit modal) */}
        <div className="flex-1 mt-6 sm:mt-0 space-y-5">
          <div>
            <h3 className="text-sm font-semibold text-gray-600 uppercase mb-2">
              Additional Info
            </h3>
            <div className="space-y-3">
              <div>
                <h4 className="text-xs font-semibold text-gray-500 uppercase mb-1">
                  Reviewed By
                </h4>
                <p className="text-gray-800">
                  {task.reviewer
                    ? `Employee ID: ${task.reviewer}`
                    : "Pending assignment"}
                </p>
              </div>

              <div>
                <h4 className="text-xs font-semibold text-gray-500 uppercase mb-1">
                  Created By
                </h4>
                <p className="text-gray-800">
                  {task.creator_name
                    ? `${task.creator_name} (#${task.created_by})`
                    : `Employee ID: ${task.created_by || "-"}`}
                </p>
              </div>

              <div>
                <h4 className="text-xs font-semibold text-gray-500 uppercase mb-1">
                  Due Date
                </h4>
                <p className="text-gray-800">
                  {formatDate(task.expected_closure)}
                </p>
              </div>
            </div>
          </div>

          <div className="flex justify-end">
            <button
              onClick={onClose}
              className="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-100 transition font-medium"
            >
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default TaskDetailsModal;
