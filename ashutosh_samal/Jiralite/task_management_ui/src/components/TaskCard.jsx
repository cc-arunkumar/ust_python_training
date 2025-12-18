import { useState } from "react";
import { useNavigate } from "react-router-dom";
import toast from "react-hot-toast";
import {
  updateTaskStatus,
  deleteTask,
  updateTaskPriority,
} from "../api/task.api";

/* 🎨 Priority styles */
const priorityStyles = {
  HIGH: "border-red-500 text-red-600",
  MEDIUM: "border-yellow-500 text-yellow-600",
  LOW: "border-green-500 text-green-600",
};

export default function TaskCard({ task, role, refresh }) {
  const navigate = useNavigate();

  const [status, setStatus] = useState(task.status);
  const [priority, setPriority] = useState(task.priority);
  const [remarks, setRemarks] = useState("");
  const [showRemarks, setShowRemarks] = useState(false);
  const [loading, setLoading] = useState(false);

  /* 🔁 STATUS CHANGE */
  const handleStatusChange = async (newStatus) => {
    // Manager review → show remark box
    if (role === "MANAGER" && task.status === "REVIEW") {
      setStatus(newStatus);
      setShowRemarks(true);
      return;
    }

    await submitStatus(newStatus);
  };

  const submitStatus = async (newStatus) => {
    try {
      setLoading(true);
      await updateTaskStatus(task.t_id, {
        status: newStatus,
        remarks: remarks || null,
      });
      toast.success(`Task moved to ${newStatus.replace("_", " ")}`);
      refresh();
    } catch {
      toast.error("Failed to update status");
    } finally {
      setLoading(false);
      setShowRemarks(false);
      setRemarks("");
    }
  };

  /* 🔁 PRIORITY CHANGE */
  const handlePriorityChange = async (newPriority) => {
    try {
      setPriority(newPriority);
      await updateTaskPriority(task.t_id, newPriority);
      toast.success(`Priority set to ${newPriority}`);
      refresh();
    } catch {
      toast.error("Failed to update priority");
    }
  };

  /* ❌ DELETE TASK */
  const handleDelete = async () => {
    if (!window.confirm(`Delete TASK-${task.t_id}? This cannot be undone.`))
      return;

    try {
      await deleteTask(task.t_id);
      toast.success(`TASK-${task.t_id} deleted`);
      refresh();
    } catch {
      toast.error("Failed to delete task");
    }
  };

  return (
    <div
      className="bg-white rounded-lg shadow p-4 space-y-2 cursor-pointer
                 hover:ring-1 hover:ring-gray-300 transition"
      onClick={() => navigate(`/tasks/${task.t_id}/edit`)}
    >
      {/* 🔹 TASK ID + PRIORITY */}
      <div
        className="flex justify-between items-center"
        onClick={(e) => e.stopPropagation()}
      >
        <span className="text-xs text-gray-500">
          TASK-{task.t_id}
        </span>

        {(role === "ADMIN" || role === "MANAGER") ? (
          <select
            value={priority}
            onChange={(e) => handlePriorityChange(e.target.value)}
            className={`text-xs font-semibold px-2 py-1 rounded border ${priorityStyles[priority]}`}
          >
            <option value="HIGH">HIGH</option>
            <option value="MEDIUM">MEDIUM</option>
            <option value="LOW">LOW</option>
          </select>
        ) : (
          <span
            className={`text-xs font-semibold px-2 py-1 rounded border ${priorityStyles[priority]}`}
          >
            {priority}
          </span>
        )}
      </div>

      {/* 🔹 TITLE */}
      <h3 className="font-semibold text-gray-800">
        {task.title}
      </h3>

      {/* 🔹 DESCRIPTION */}
      <p className="text-sm text-gray-600 line-clamp-3">
        {task.description}
      </p>

      {/* 🔹 STATUS DROPDOWN */}
      <select
        value={status}
        onChange={(e) => handleStatusChange(e.target.value)}
        disabled={loading}
        onClick={(e) => e.stopPropagation()}
        className="w-full border rounded px-2 py-1 text-sm"
      >
        <option value="TO_DO">TO DO</option>
        <option value="IN_PROGRESS">IN PROGRESS</option>
        <option value="REVIEW">REVIEW</option>

        {(role === "MANAGER" || role === "ADMIN") && (
          <option value="DONE">DONE</option>
        )}
      </select>

      {/* 🔹 MANAGER REVIEW BOX */}
      {showRemarks && role === "MANAGER" && (
        <div
          className="space-y-2"
          onClick={(e) => e.stopPropagation()}
        >
          <textarea
            placeholder="Add review remarks (optional)"
            className="w-full border rounded p-2 text-sm"
            value={remarks}
            onChange={(e) => setRemarks(e.target.value)}
          />

          <div className="flex justify-end gap-2">
            <button
              onClick={() => {
                setShowRemarks(false);
                setStatus(task.status);
              }}
              className="text-sm px-3 py-1 border rounded"
            >
              Cancel
            </button>

            <button
              onClick={() => submitStatus(status)}
              className="text-sm px-3 py-1 bg-blue-600 text-white rounded"
            >
              Submit Review
            </button>
          </div>
        </div>
      )}

      {/* 🔴 DELETE ICON */}
      {(role === "ADMIN" || role === "MANAGER") && (
        <button
          onClick={(e) => {
            e.stopPropagation(); // 🔑 critical
            handleDelete();
          }}
          title="Delete task"
          className="mt-2 text-red-500 hover:text-red-700 transition"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="w-4 h-4"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            strokeWidth={2}
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6M9 7h6m-7 0V5a1 1 0 011-1h4a1 1 0 011 1v2"
            />
          </svg>
        </button>
      )}
    </div>
  );
}
