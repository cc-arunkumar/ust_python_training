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
} from "lucide-react";
import { STATUS_CONFIG, PRIORITY_COLORS } from "../utils/constants";

function TaskCard({
  task = {},
  employees = [],
  userRole = "",
  onUpdateStatus,
  onEdit,
  currentEmpId = null,
}) {
  const [showStatusMenu, setShowStatusMenu] = useState(false);
  const [showReviewInput, setShowReviewInput] = useState(false);
  const [pendingStatus, setPendingStatus] = useState(null);
  const [reviewText, setReviewText] = useState("");

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

  const statusCfg = STATUS_CONFIG[task.status] || STATUS_CONFIG.TO_DO;
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

    // Always ask for review/remarks when changing to REVIEW, IN_PROGRESS or DONE
    const isReviewer =
      currentEmpId != null && Number(currentEmpId) === Number(task.reviewer);

    // If reviewer-only remarks are required (REVIEW/DONE) and the current user is NOT the reviewer,
    // skip showing the reviewer textarea and proceed without remarks (backend will enforce review writes).
    if (newStatus === "REVIEW" || newStatus === "DONE") {
      if (!isReviewer) {
        // proceed without remarks
        onUpdateStatus && onUpdateStatus(task.task_id, newStatus, null);
        setShowStatusMenu(false);
        return;
      }
      // current user is reviewer -> allow them to add reviewer remarks
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

    // For other status changes, update directly
    onUpdateStatus && onUpdateStatus(task.task_id, newStatus, null);
    setShowStatusMenu(false);
  };

  const submitReview = () => {
    console.log("Submitting review:", {
      taskId: task.task_id,
      status: pendingStatus,
      review: reviewText,
      userRole: userRole,
    });

    const isReviewer =
      currentEmpId != null && Number(currentEmpId) === Number(task.reviewer);

    // If trying to submit reviewer remarks but not the designated reviewer, block here (server also enforces)
    if (
      reviewText &&
      reviewText.trim() &&
      (pendingStatus === "REVIEW" || pendingStatus === "DONE") &&
      !isReviewer
    ) {
      alert("Only the designated reviewer can add reviewer remarks.");
      return;
    }

    // Call the update function with review text (even if empty)
    onUpdateStatus &&
      onUpdateStatus(task.task_id, pendingStatus, reviewText.trim() || null);

    // Reset states
    setShowReviewInput(false);
    setPendingStatus(null);
    setReviewText("");
  };

  const cancelReview = () => {
    setShowReviewInput(false);
    setPendingStatus(null);
    setReviewText("");
  };

  const StatusIcon = statusIcons[task.status] || Clock;

  return (
    <div className="bg-white rounded-lg shadow-sm p-3 hover:shadow-md transition cursor-pointer relative">
      {/* Priority Badge - Top Right */}
      <div className="absolute top-2 right-2">
        <span className={`text-xs font-semibold ${priorityClasses}`}>
          {task.priority || "MEDIUM"}
        </span>
      </div>

      {/* Title */}
      <div className="pr-16 mb-2">
        <h3 className="text-sm font-semibold text-gray-800 line-clamp-2">
          {task.title}
        </h3>
      </div>

      {/* Description */}
      <p className="text-xs text-gray-600 line-clamp-2 mb-3">
        {task.description || "No description"}
      </p>

      {/* Info Section */}
      <div className="space-y-1 text-xs text-gray-500 mb-3">
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
      <div className="flex items-center justify-between gap-2">
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
              {/* Backdrop to close menu */}
              <div
                className="fixed inset-0 z-10"
                onClick={(e) => {
                  e.stopPropagation();
                  setShowStatusMenu(false);
                }}
              />

              {/* Dropdown Menu */}
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
          className="p-1.5 hover:bg-indigo-50 text-indigo-600 rounded-md transition"
          title="Edit Task"
        >
          <Edit2 size={14} />
        </button>
      </div>

      {/* Review Input Section */}
      {showReviewInput && (
        <div
          className="mt-3 pt-3 border-t"
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
            className="w-full px-2 py-1.5 border rounded text-xs mb-2 focus:ring-1 focus:ring-indigo-400 focus:outline-none"
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
