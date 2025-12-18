import React, { useState } from "react";
import {
  User,
  CheckCircle,
  Clock,
  PlayCircle,
  Pause,
  Edit2,
  ChevronDown,
  AlertCircle,
  GripVertical,
} from "lucide-react";
import { STATUS_CONFIG, PRIORITY_COLORS } from "../utils/constants";

function TaskCard({
  task = {},
  employees = [],
  userRole = "",
  onUpdateStatus,
  onEdit,
  currentEmpId = null,
  statusConfig = null,
}) {
  const [showStatusMenu, setShowStatusMenu] = useState(false);
  const [showReviewInput, setShowReviewInput] = useState(false);
  const [pendingStatus, setPendingStatus] = useState(null);
  const [reviewText, setReviewText] = useState("");
  const [isDragging, setIsDragging] = useState(false);

  const statusIcons = {
    TO_DO: Clock,
    IN_PROGRESS: PlayCircle,
    REVIEW: Pause,
    DONE: CheckCircle,
    BLOCKED: AlertCircle,
  };

  const assignee = (employees || []).find((e) => e.emp_id === task.assigned_to);
  const reviewer = (employees || []).find((e) => e.emp_id === task.reviewer);

  const formatExpected = (dt) => {
    if (!dt) return null;
    try {
      const d = new Date(dt);
      if (isNaN(d)) return null;
      return d.toLocaleDateString(undefined, {
        day: "2-digit",
        month: "short",
      });
    } catch (e) {
      return null;
    }
  };

  const statusCfg = statusConfig || STATUS_CONFIG[task.status] || STATUS_CONFIG.TO_DO;
  const priorityClasses = PRIORITY_COLORS[task.priority] || "text-gray-600";

  const canMarkDone =
    (userRole || "").toUpperCase().includes("ADMIN") ||
    (userRole || "").toUpperCase().includes("MANAGER");

  const getAvailableStatuses = () => {
    const all = Object.keys(STATUS_CONFIG);
    if (!canMarkDone) return all.filter((s) => s !== "DONE");
    return all;
  };

  const handleStatusSelect = (newStatus) => {
    if (newStatus === "DONE" && !canMarkDone) {
      alert("Only Managers and Admins can mark tasks as Done");
      setShowStatusMenu(false);
      return;
    }

    const isReviewer =
      currentEmpId != null && Number(currentEmpId) === Number(task.reviewer);

    if (newStatus === "REVIEW" || newStatus === "DONE") {
      if (!isReviewer) {
        onUpdateStatus && onUpdateStatus(task.task_id, newStatus, null);
        setShowStatusMenu(false);
        return;
      }
      setPendingStatus(newStatus);
      setShowReviewInput(true);
      setShowStatusMenu(false);
      return;
    }

    if (newStatus === "IN_PROGRESS") {
      setPendingStatus(newStatus);
      setShowReviewInput(true);
      setShowStatusMenu(false);
      return;
    }

    onUpdateStatus && onUpdateStatus(task.task_id, newStatus, null);
    setShowStatusMenu(false);
  };

  const submitReview = () => {
    const isReviewer =
      currentEmpId != null && Number(currentEmpId) === Number(task.reviewer);

    if (
      reviewText &&
      reviewText.trim() &&
      (pendingStatus === "REVIEW" || pendingStatus === "DONE") &&
      !isReviewer
    ) {
      alert("Only the designated reviewer can add reviewer remarks.");
      return;
    }

    onUpdateStatus &&
      onUpdateStatus(task.task_id, pendingStatus, reviewText.trim() || null);

    setShowReviewInput(false);
    setPendingStatus(null);
    setReviewText("");
  };

  const cancelReview = () => {
    setShowReviewInput(false);
    setPendingStatus(null);
    setReviewText("");
  };

  // Drag handlers
  const handleDragStart = (e) => {
    setIsDragging(true);
    e.dataTransfer.effectAllowed = "move";
    e.dataTransfer.setData("taskId", task.task_id);
    e.dataTransfer.setData("currentStatus", task.status);
  };

  const handleDragEnd = () => {
    setIsDragging(false);
  };

  const StatusIcon = statusIcons[task.status] || Clock;

  return (
    <div
      draggable
      onDragStart={handleDragStart}
      onDragEnd={handleDragEnd}
      className={`${statusCfg.cardBg} rounded-lg p-3 hover:shadow-sm transition cursor-pointer relative border-l-4 ${statusCfg.color.replace('bg-', 'border-')} ${
        isDragging ? 'opacity-50 shadow-none' : 'shadow-xs'
      }`}
      style={{ boxShadow: isDragging ? 'none' : '0 1px 2px 0 rgba(0, 0, 0, 0.05)' }}
    >
      {/* Drag Handle */}
      <div className="absolute top-2 left-2 text-gray-400 cursor-grab active:cursor-grabbing">
        <GripVertical size={14} />
      </div>

      {/* Priority Badge - Top Right */}
      <div className="absolute top-2 right-2">
        <span className={`text-xs font-semibold px-2 py-1 rounded ${priorityClasses}`}>
          {task.priority || "MEDIUM"}
        </span>
      </div>

      {/* Title */}
      <div className="px-4 pr-16 mb-2">
        <h3 className="text-sm font-semibold text-gray-800 line-clamp-2">
          {task.title}
        </h3>
      </div>

      {/* Description */}
      <p className="text-xs text-gray-600 line-clamp-2 mb-3 px-1">
        {task.description || "No description"}
      </p>

      {/* Info Section */}
      <div className="space-y-1 text-xs text-gray-500 mb-3 px-1">
        {task.expected_closure && (
          <div className="flex items-center gap-1">
            <span className="font-medium">Expected:</span>
            <span className="text-gray-700">
              {formatExpected(task.expected_closure)}
            </span>
          </div>
        )}
        {task.dept_name && (
          <div className="flex items-center gap-1">
            <span className="font-medium">Dept:</span>
            <span className="text-gray-700">{task.dept_name}</span>
          </div>
        )}
        {assignee && (
          <div className="flex items-center gap-1">
            <User size={12} className="inline" />
            <span className="text-gray-700">{assignee.emp_name}</span>
          </div>
        )}
        {reviewer && (
          <div className="flex items-center gap-1">
            <span className="font-medium">Reviewer:</span>
            <span className="text-gray-700">{reviewer.emp_name}</span>
          </div>
        )}
      </div>

      {/* Status and Edit Row */}
      <div className="flex items-center justify-between gap-2 px-1">
        <div className="relative flex-1">
          <button
            onClick={(e) => {
              e.stopPropagation();
              setShowStatusMenu((s) => !s);
            }}
            className={`flex items-center gap-1 px-2 py-1 rounded-full text-xs font-medium w-full justify-center ${statusCfg.color} text-white`}
          >
            <StatusIcon size={12} />
            <span className="truncate">{statusCfg.label}</span>
            <ChevronDown size={12} />
          </button>

          {showStatusMenu && (
            <>
              <div
                className="fixed inset-0 z-10"
                onClick={(e) => {
                  e.stopPropagation();
                  setShowStatusMenu(false);
                }}
              />

              <div className="absolute left-0 bottom-full mb-1 bg-white rounded-md shadow-lg border z-20 min-w-[140px]">
                {getAvailableStatuses().map((s) => {
                  const cfg = STATUS_CONFIG[s];
                  const Icon = statusIcons[s] || Clock;
                  const disabled = s === "DONE" && !canMarkDone;
                  return (
                    <button
                      key={s}
                      onClick={(e) => {
                        e.stopPropagation();
                        handleStatusSelect(s);
                      }}
                      disabled={disabled}
                      className={`w-full text-left px-3 py-2 hover:bg-gray-50 flex items-center gap-2 text-xs ${
                        disabled ? "opacity-50 cursor-not-allowed" : ""
                      }`}
                    >
                      <Icon size={12} />
                      {cfg.label}
                      {disabled && <span className="ml-auto text-xs">🔒</span>}
                    </button>
                  );
                })}
              </div>
            </>
          )}
        </div>

        <button
          onClick={(e) => {
            e.stopPropagation();
            onEdit && onEdit(task);
          }}
          className="p-1.5 hover:bg-white/70 text-indigo-600 rounded-md transition"
          title="Edit Task"
        >
          <Edit2 size={14} />
        </button>
      </div>

      {/* Review Input Section */}
      {showReviewInput && (
        <div
          className="mt-3 pt-3 border-t bg-white/50 rounded p-2"
          onClick={(e) => e.stopPropagation()}
        >
          <div className="mb-2">
            <p className="text-xs text-gray-600 mb-1">
              Changing status to:{" "}
              <strong className="text-indigo-600">
                {STATUS_CONFIG[pendingStatus]?.label}
              </strong>
            </p>
            <p className="text-xs text-gray-500">
              Add remarks as{" "}
              <strong>{canMarkDone ? "Reviewer" : "Developer"}</strong>
            </p>
          </div>
          <textarea
            value={reviewText}
            onChange={(e) => setReviewText(e.target.value)}
            placeholder={`Add ${
              canMarkDone ? "reviewer" : "developer"
            } remarks... (optional)`}
            className="w-full px-2 py-1.5 border rounded text-xs mb-2 focus:ring-1 focus:ring-indigo-400 focus:outline-none bg-white"
            rows="3"
            autoFocus
          />
          <div className="flex gap-2">
            <button
              onClick={submitReview}
              className="flex-1 bg-indigo-600 text-white py-1.5 rounded text-xs font-medium hover:bg-indigo-700 transition"
            >
              {reviewText.trim()
                ? "Submit with Remarks"
                : "Submit without Remarks"}
            </button>
            <button
              onClick={cancelReview}
              className="flex-1 bg-gray-200 text-gray-700 py-1.5 rounded text-xs font-medium hover:bg-gray-300 transition"
            >
              Cancel
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default TaskCard;