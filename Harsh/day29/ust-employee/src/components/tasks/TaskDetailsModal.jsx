import React, { useState, useEffect } from "react";
import { X, AlertCircle, User } from "lucide-react";
import ApiService from "../../services/api";
import { API_BASE_URL } from "../../utils/constants";

const TaskDetailsModal = ({ task, onClose, onUpdate, assignedEmployee }) => {
  // TaskDetailsModal is view-only. Edits (status changes, uploads, feedback)
  // should be performed in the edit/create modal (TaskModal).
  // Keep minimal state for error reporting.
  const [error, setError] = useState("");
  const [attachments, setAttachments] = useState([]);
  const [remarks, setRemarks] = useState([]);

  useEffect(() => {
    let mounted = true;
    const load = async () => {
      try {
        const data = await ApiService.getTask(task.task_id);
        if (!mounted) return;
        // attachments may be included directly on task; otherwise fall back to attachments endpoint
        const atts = data.attachments || [];
        if (atts && atts.length > 0) {
          setAttachments(atts);
          return;
        }

        // fallback: use attachments listing endpoint and filter client-side
        try {
          const fallback = await ApiService.getAttachmentsForTask(task.task_id);
          if (!mounted) return;
          setAttachments(fallback || []);
        } catch (err) {
          // ignore fallback failure
        }
        // try to load remarks from remarks endpoint
        try {
          const r = await ApiService.listRemarks(task.task_id);
          if (!mounted) return;
          setRemarks(r || []);
        } catch (err) {
          // ignore remarks fetch errors
        }
      } catch (err) {
        // show minimal error for visibility
        if (mounted) setError(err.message || "Failed to load attachments");
      }
    };
    if (task && task.task_id) load();
    return () => (mounted = false);
  }, [task]);

  // No status/file handlers here — view-only modal.

  const formatDate = (dateString) =>
    dateString ? new Date(dateString).toLocaleDateString() : "-";

  return (
    <div className="fixed inset-0 bg-black/30 backdrop-blur-sm flex items-center justify-center p-4 z-50 overflow-auto">
      <div className="bg-white rounded-2xl shadow-2xl w-full max-w-md max-h-[90vh] overflow-y-auto p-6 border border-gray-200">
        <div className="flex items-start justify-between mb-4">
          <h2 className="text-2xl font-bold text-gray-800">{task.title}</h2>
          <button
            onClick={onClose}
            className="text-gray-400 hover:text-gray-600 transition"
          >
            <X size={24} />
          </button>
        </div>

        {error && (
          <div className="bg-red-100 border border-red-300 text-red-700 px-4 py-3 rounded flex items-center gap-2 mb-4">
            <AlertCircle size={20} />
            <span className="text-sm">{error}</span>
          </div>
        )}

        {/* Single block layout: stacked fields without compartments */}
        <div className="space-y-4 text-sm text-slate-700">
          <div>
            <div className="text-xs text-slate-500">Task Number</div>
            <div className="font-medium text-slate-800">{task.task_id}</div>
          </div>

          <div>
            <div className="text-xs text-slate-500">Details</div>
            <div className="text-slate-800">
              {task.description || "No additional details provided."}
            </div>
          </div>

          <div className="flex items-center gap-3">
            <div className="w-12 h-12 rounded-full bg-slate-100 overflow-hidden flex items-center justify-center text-slate-700 font-semibold">
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
            <div>
              <div className="text-xs text-slate-500">Assigned To</div>
              <div className="font-medium text-slate-800">
                {assignedEmployee ? assignedEmployee.emp_name : "Unassigned"}
              </div>
              {assignedEmployee?.email && (
                <div className="text-xs text-slate-500">
                  {assignedEmployee.email}
                </div>
              )}
            </div>
          </div>

          <div>
            <div className="text-xs text-slate-500">Priority</div>
            <div className="font-medium text-slate-800">
              {task.priority || "-"}
            </div>
          </div>

          <div>
            <div className="text-xs text-slate-500">Due Date</div>
            <div className="font-medium text-slate-800">
              {formatDate(task.expected_closure)}
            </div>
          </div>

          <div>
            <div className="text-xs text-slate-500">Reviewer / Created By</div>
            <div className="font-medium text-slate-800">
              {task.reviewer ? `Reviewer ID: ${task.reviewer}` : "No reviewer"}
              {task.creator_name
                ? ` — Created by ${task.creator_name} (#${task.created_by})`
                : ""}
            </div>
          </div>

          {((task.notifications && task.notifications.length) || 0) +
            ((task.remarks && task.remarks.length) || 0) >
            0 && (
            <div>
              <div className="text-xs text-slate-500">
                Notifications / Remarks
              </div>
              <div className="space-y-2 mt-2">
                {task.notifications &&
                  task.notifications.map((n, i) => (
                    <div key={`n-${i}`} className="text-sm text-slate-700">
                      {n}
                    </div>
                  ))}
                {remarks && remarks.length > 0
                  ? remarks.map((r) => (
                      <div
                        key={`r-${r.id || r._id}`}
                        className="text-sm text-slate-700"
                      >
                        {r.text}
                      </div>
                    ))
                  : task.remarks &&
                    task.remarks.map((r, i) => (
                      <div key={`r-${i}`} className="text-sm text-slate-700">
                        {r}
                      </div>
                    ))}
              </div>
            </div>
          )}

          {/* Attachments (if any) */}
          <div>
            <div className="text-xs text-slate-500">Attachments</div>
            <div className="mt-2 space-y-2">
              {(() => {
                // merge attachments from primary attachments list and remarks that have file_id
                const combined = [...(attachments || [])];
                (remarks || []).forEach((r) => {
                  if (r.file_id) {
                    combined.push({
                      id: r.file_id,
                      file_name: r.filename || r.fileName || r.filename,
                    });
                  }
                });

                if (combined.length === 0) {
                  return (
                    <div className="text-sm text-slate-500">No attachments</div>
                  );
                }

                return combined.map((a) => {
                  const href = a.file_path
                    ? a.file_path.startsWith("http")
                      ? a.file_path
                      : `${API_BASE_URL}${a.file_path}`
                    : a.id
                    ? ApiService.getRemarkAttachmentUrl(a.id)
                    : "#";
                  const name =
                    a.file_name || a.fileName || a.filename || "file";
                  return (
                    <div
                      key={a.id || name}
                      className="flex items-center justify-between border rounded px-3 py-2"
                    >
                      <div className="truncate text-sm text-slate-700 mr-2">
                        {name}
                      </div>
                      <div className="flex items-center gap-2">
                        <a
                          href={href}
                          target="_blank"
                          rel="noreferrer"
                          download={name}
                          className="text-blue-600 text-xs font-medium hover:underline"
                        >
                          Download
                        </a>
                      </div>
                    </div>
                  );
                });
              })()}
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
